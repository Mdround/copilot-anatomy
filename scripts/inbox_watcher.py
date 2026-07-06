#!/usr/bin/env python3
"""
inbox_watcher.py

Polls a Dropbox inbox folder for new files, moves them into the repo's
raw/ directory (renaming with an ingest timestamp for provenance), and
commits the change to git. Designed to run on a schedule (cron), not as a
long-running daemon — polling, not inotify, because:
  - Windows-mounted paths under WSL don't reliably fire inotify events.
  - Dropbox's own sync client on native Linux (the mini-PC target) has
    similar caveats with some filesystem watchers.

This script does NOT do any LLM processing — it only stages files into
raw/ and commits. Ingest (the LLM step that reads the file and updates
wiki/features/) is a separate action, run via Claude Code, either manually
or triggered off the same cron schedule after this script exits.

Usage:
    python3 inbox_watcher.py --inbox /path/to/Dropbox/copilot-anatomy \
                              --repo /path/to/kms-staging/copilot-anatomy

Cron example (runs every 15 minutes):
    */15 * * * * /usr/bin/python3 /path/to/scripts/inbox_watcher.py \
        --inbox "$HOME/Dropbox/copilot-anatomy" \
        --repo "$HOME/kms-staging/copilot-anatomy" >> "$HOME/kms-staging/copilot-anatomy/scripts/watcher.log" 2>&1
"""

import argparse
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# File types we accept into raw/. Extend as needed.
ALLOWED_SUFFIXES = {".md", ".txt", ".pdf", ".html", ".docx"}

# Files/patterns to ignore in the inbox (sync artefacts, etc.)
IGNORE_PREFIXES = (".", "~$")
IGNORE_SUFFIXES = (".tmp", ".dropbox", ".partial")


def is_ignorable(path: Path) -> bool:
    name = path.name
    if name.startswith(IGNORE_PREFIXES):
        return True
    if name.endswith(IGNORE_SUFFIXES):
        return True
    return False


def run_git(repo: Path, *args: str) -> None:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"git {' '.join(args)} failed: {result.stderr.strip()}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inbox", required=True, type=Path, help="Dropbox inbox folder to poll")
    parser.add_argument("--repo", required=True, type=Path, help="Path to the copilot-anatomy repo root")
    parser.add_argument("--dry-run", action="store_true", help="Report what would happen, change nothing")
    args = parser.parse_args()

    inbox: Path = args.inbox.expanduser()
    repo: Path = args.repo.expanduser()
    raw_dir = repo / "raw"

    if not inbox.is_dir():
        print(f"Inbox not found: {inbox}", file=sys.stderr)
        return 1
    if not raw_dir.is_dir():
        print(f"raw/ not found under repo: {raw_dir}", file=sys.stderr)
        return 1

    candidates = sorted(
        p for p in inbox.iterdir()
        if p.is_file() and not is_ignorable(p) and p.suffix.lower() in ALLOWED_SUFFIXES
    )

    if not candidates:
        print("No new files.")
        return 0

    moved = []
    for src in candidates:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        dest_name = f"{stamp}__{src.name}"
        dest = raw_dir / dest_name

        if args.dry_run:
            print(f"[dry-run] would move {src} -> {dest}")
            continue

        shutil.move(str(src), str(dest))
        moved.append(dest_name)
        print(f"moved {src.name} -> raw/{dest_name}")

    if args.dry_run or not moved:
        return 0

    # Stage and commit. This commit only records that files landed in raw/ —
    # it is deliberately separate from any wiki/features/ update, which
    # Claude Code does as its own commit during the ingest step.
    run_git(repo, "add", "-A", "raw/")
    commit_msg = "inbox: staged " + ", ".join(moved)
    run_git(repo, "commit", "-m", commit_msg)

    print(f"Staged {len(moved)} file(s). Run Claude Code to ingest them into wiki/features/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

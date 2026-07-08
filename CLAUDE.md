# Copilot Anatomy — Operating Schema

## Purpose

This is a reference knowledge base cataloguing services/features (e.g.
Copilot capabilities across licence tiers) as standalone **reference
documents** — not a pattern language. Each feature gets one article
describing what it is, what it depends on, its known limitations, and how
it relates to other features.

This repo does **not** use the Alexandrian problem/context/forces/solution
schema from `~/kms/second-brain/` — do not import that structure, its
frontmatter, or its ingest/query/lint vocabulary here. This is a plain
reference catalogue, not a distilled pattern library.

## Session-start protocol

At the start of every session, before making any changes, run `git fetch`
and `git status` to surface any upstream changes or local drift. Do this
even if the session appears to pick up mid-task — don't assume the working
tree matches what was last seen.

## Directory layout

```
raw/             Ingested source articles, trimmed to excerpts (see
                 Ingest operation). Pre-review. Cite raw/<filename> in
                 wiki frontmatter for provenance.
wiki/features/   One article per service/feature. LLM-maintained — you
                 (Claude) write and update this; the user rarely edits
                 directly, except for Insight sections (see below).
journal/         Session continuity log. One file per session/day:
                 journal/YYYY-MM-DD.md — what was ingested, decisions
                 made, open questions.
scripts/         Ingestion/build scripts specific to this repo.
```

## Ingest operation

Triggered by: a new file appearing in `raw/` (staged automatically by
`scripts/inbox_watcher.py` from the Dropbox inbox every 15 minutes), or the
user saying "ingest `raw/<file>`".

Steps:
1. Read the source in full.
2. Identify the feature(s) it relates to — an existing `wiki/features/*.md`
   article to update, or a new one to create per the article schema below.
   Search `wiki/features/` first; don't create a duplicate article for a
   feature that's already covered.
3. Cite the raw filename in the article's Description (e.g.
   `Source: raw/<filename>`) — this is the forward link from wiki back to
   its source.
4. Trim the `raw/<file>` down to excerpts: keep only the passages that
   directly support claims used in the article(s) (plus any capture
   frontmatter/metadata already at the top of the file, and the original
   `source_url`), and remove the rest of the copied text. This repo is
   public — unlike second-brain, `raw/` is not a private vault, so full
   verbatim mirrors of third-party articles don't belong here long-term.
   Short attributed excerpts kept for provenance are the target; a link to
   `source_url` stands in for anything trimmed. This is the one sanctioned
   edit to an existing `raw/` file — outside of an ingest pass, `raw/`
   stays append-only.
5. Append an entry to `journal/YYYY-MM-DD.md` (today's date; create the
   file if it doesn't exist yet) recording which `raw/` file(s) were
   ingested/trimmed and which `wiki/features/*.md` articles were created or
   touched as a result. This is what makes "has this raw file been
   processed?" answerable without grepping the whole wiki — check
   `journal/` first.
6. Commit — one commit per ingest operation. Commit message format:
   `ingest: <source filename> — <one-line description of what changed>`.

Not every `raw/` file will necessarily map to an in-scope feature (see
Purpose) — if a source is out of scope, say so in the `journal/` entry
rather than silently skipping it, so it's clear the file was reviewed and
deliberately not turned into an article.

## Article schema (`wiki/features/*.md`)

### Frontmatter

Every article requires this exact frontmatter block:

```yaml
---
title:
service:
licence_tier:
maturity:
source_url:
source_publisher:
date_reviewed:
last_verified:
tags: []
---
```

- `licence_tier` — the licence/plan tier the feature belongs to (e.g. free,
  business, enterprise) — use whatever tier vocabulary the source material
  uses.
- `maturity` — e.g. `preview`, `GA`, `deprecated` — reflect the source's own
  characterisation, don't guess.
- `date_reviewed` — when this article was last written/edited here.
- `last_verified` — when the underlying claim was last confirmed still
  accurate against the source or a fresher check. These two dates will
  diverge over time; that's expected and useful.

### Body sections

In this order:

1. **Description** — what the feature is and does.
2. **Dependencies** — what it requires (other features, licence tiers,
   infrastructure, opt-ins).
3. **Known limitations** — constraints, gaps, and gotchas of the
   service/feature itself, as stated by the source (e.g. what it can't do,
   what it requires that it doesn't provide, rollout gaps). This is
   **not** the place to caveat the source material's own reliability,
   currency, or provenance (e.g. "this is a third-party blog, not
   Microsoft-official," "this is a living document and may be stale") —
   `source_publisher` in frontmatter already discloses provenance, and
   sourcing caveats don't belong mixed into feature-level limitations.
4. **Related features** — cross-links to other `wiki/features/*.md` pages.
5. **Insight** — hand-added human commentary. Must be visually and
   structurally distinct from the source-derived sections above it: put it
   under its own `## Insight` heading at the end of the article, formatted
   entirely as a blockquote:

   ```markdown
   ## Insight

   > Human commentary goes here. Every line in this section is a
   > blockquote so it's unmistakably separate from source-derived content.
   ```

   Never write source-derived claims inside the Insight blockquote, and
   never let non-Insight sections use blockquote formatting — the
   blockquote *is* the marker. If an article has no human commentary yet,
   leave the heading with an empty blockquote placeholder (`> _(none yet)_`)
   rather than omitting the section, so it's visible that it hasn't been
   reviewed by a human yet.

## Conventions

- **Filenames**: kebab-case, matching the feature name, in
  `wiki/features/<feature-name>.md`.
- **Tone**: accurate over agreeable — flag contradictions or weak sourcing
  rather than smoothing over them. Source-derived sections should reflect
  what the source says, not editorialize; editorializing belongs in
  Insight.
- **Git**: one commit per ingest. Commit message format:
  `ingest: <source filename> — <one-line description of what changed>`.

## What NOT to do

- Don't invent `licence_tier` or `maturity` values not supported by the
  source — leave the field blank and flag it rather than guessing.
- Don't edit or delete `raw/` files outside of the trimming step in the
  Ingest operation — and don't touch `raw/` at all from a later
  wiki-editing pass that isn't doing a fresh ingest.
- Don't trim a `raw/` excerpt down past what's needed to support the
  article's claims — err toward keeping slightly more context rather than
  less, since it can't be recovered from `source_url` if the original page
  changes or disappears.
- Don't merge the Insight section's formatting with the rest of the
  article, and don't put source-derived facts inside it — the blockquote
  boundary is what keeps human commentary auditable.
- Don't restructure this frontmatter/body schema without discussing it
  first.

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

## Directory layout

```
raw/             Ingested source articles. Append-only, pre-review. Never
                 edit or delete files here. Cite raw/<filename> in wiki
                 frontmatter for provenance.
wiki/features/   One article per service/feature. LLM-maintained — you
                 (Claude) write and update this; the user rarely edits
                 directly, except for Insight sections (see below).
journal/         Session continuity log. One file per session/day:
                 journal/YYYY-MM-DD.md — what was ingested, decisions
                 made, open questions.
scripts/         Ingestion/build scripts specific to this repo.
```

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
3. **Known limitations** — constraints, gaps, gotchas, as stated by the
   source.
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
- Don't write into `raw/` from a wiki-editing pass, and don't edit/delete
  existing files in `raw/`.
- Don't merge the Insight section's formatting with the rest of the
  article, and don't put source-derived facts inside it — the blockquote
  boundary is what keeps human commentary auditable.
- Don't restructure this frontmatter/body schema without discussing it
  first.

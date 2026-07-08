---
title: Microsoft Agent 365
service: Microsoft 365
licence_tier:
maturity: GA
sources:
  - url: https://cadena.co/resources/guides/microsoft-licensing-changes
    publisher: Cadena
date_reviewed: 2026-07-08
last_verified: 2026-07-07
tags: [agent-365, ai-governance, control-plane, copilot, licensing]
---

## Description

Microsoft Agent 365 is the control plane for AI agents, reaching general
availability in May 2026. It gives IT and security leaders a single place
to observe, govern, manage, and secure agents across the organisation —
covering both agents built on Microsoft AI platforms and agents from
ecosystem partners. It is positioned as making AI agents licensable,
governable, and auditable assets, comparable in kind to how devices or
service principals are managed today.

Sources:
- `raw/20260707-083002__2026-07-07_Microsoft-2026-Licensing-Changes-M365-E7,-Agent-365,-Price-Increases,-and-EOS-Wave--Cadena.txt`

## Dependencies

- Agents that Agent 365 governs may themselves depend on Microsoft Graph
  and Entra ID for identity and data access scoping (SharePoint, Outlook,
  Teams, custom connectors), per the source's discussion of governance
  workflows.
- Bundled into [M365 E7 (Frontier Suite)](m365-e7-frontier-suite.md) as
  part of the unified E7 SKU; also available as its own control plane
  outside of E7 (the source doesn't state E7 is required to use
  Agent 365).

## Known limitations

[none]

## Unknowns

- No published licence tier or per-agent pricing model for standalone use
  — how it's metered/entitled outside the E7 bundle is undefined.
- No enumerated list of supported ecosystem-partner agent platforms —
  which third-party agents it can actually govern is unspecified.
- Observability and security capabilities aren't concretely specified —
  no detail on logging granularity, anomaly detection, or revocation
  mechanics.

## Related features

- [M365 E7 (Frontier Suite)](m365-e7-frontier-suite.md) — bundles
  Agent 365 into a single SKU with E5 and Copilot.

## Insight

> _(none yet)_

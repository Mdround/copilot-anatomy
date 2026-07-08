---
title: Microsoft 365 E7 (Frontier Suite)
service: Microsoft 365
licence_tier: E7
maturity:
sources:
  - url: https://cadena.co/resources/guides/microsoft-licensing-changes
    publisher: Cadena
date_reviewed: 2026-07-08
last_verified: 2026-07-07
tags: [licensing, m365-e7, frontier-suite, copilot, agent-365, work-iq]
---

## Description

Microsoft 365 E7 ("the Frontier Suite") is a new commercial licence tier
announced for general introduction in May 2026, sitting above E5 in the
M365 stack. It unifies Microsoft 365 E5, Microsoft 365 Copilot, and
Agent 365 into a single bundled SKU, powered by "Work IQ," and includes
Microsoft Entra Suite plus advanced Defender, Intune, and Purview
capabilities.

Sources:
- `raw/20260707-083002__2026-07-07_Microsoft-2026-Licensing-Changes-M365-E7,-Agent-365,-Price-Increases,-and-EOS-Wave--Cadena.txt`

## Dependencies

- Presupposes (bundles in) Microsoft 365 E5 entitlements.
- Bundles Microsoft 365 Copilot licensing — no separate Copilot add-on
  purchase needed under E7.
- Bundles [Agent 365](agent-365.md) — Agent 365 entitlement is included
  rather than licensed separately.
- Requires Microsoft Entra Suite for the identity/governance layer
  described in the source.

## Known limitations

- No list pricing has been published for E7 yet — only that it sits
  above E5 in the stack.
- Bundled tier: E5, Copilot, and Agent 365 are combined into a single SKU
  with no indication that the three components can be licensed
  separately under E7 — an organisation wanting just one of the three
  gains nothing by moving to this tier.
- "Work IQ" is named as the capability underpinning the suite, but
  available material doesn't explain what it is or how it differs from
  existing Copilot orchestration/grounding.
- No stated maturity/rollout status (e.g. preview vs GA) beyond the
  May 2026 effective date — `maturity` left blank above rather than
  guessed.

## Related features

- [Agent 365](agent-365.md) — bundled into E7 as part of the unified SKU.

## Insight

> _(none yet)_

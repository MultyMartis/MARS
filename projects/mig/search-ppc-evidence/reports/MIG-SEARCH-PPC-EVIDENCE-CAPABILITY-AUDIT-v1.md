# MIG Search PPC Evidence — Capability Audit v1

**Date:** 2026-06-23  
**Wave:** 2 — MIG Evidence Production Core  
**JSON counterpart:** [MIG-SEARCH-PPC-EVIDENCE-CAPABILITY-AUDIT-v1.json](./MIG-SEARCH-PPC-EVIDENCE-CAPABILITY-AUDIT-v1.json)

## Summary

Wave 2 builds on existing MIG v0.1 runtime, Corvonero pilot capture tools, and keyword intelligence contracts. New `search-ppc-evidence` layer adds governed lifecycle-gated evidence production without duplicating working components unnecessarily.

| Capability | Classification |
|------------|----------------|
| Wordstat source registration | PARTIALLY IMPLEMENTED — contracts exist; Wave 2 registry supports WORDSTAT EXPORT |
| Source ledgers | OPERATIONAL — Wave 2 `source-registry.mjs` |
| Raw corpus storage | OPERATIONAL — intake + external storage policy |
| Normalization | OPERATIONAL — canonical registry with provenance |
| Deduplication | REUSABLE — merge by duplicate_group, preserve source_ids |
| SERP runners | PROJECT-SPECIFIC — Corvonero Playwright scripts |
| Headful browser automation | PROJECT-SPECIFIC — not generalized; adapter path only |
| Device profiles | REUSABLE — session contract + capture metadata |
| Region handling | OPERATIONAL |
| CAPTCHA handling | OPERATIONAL — explicit degraded states |
| Evidence screenshots/HTML/JSON | PARTIALLY IMPLEMENTED — pilot evidence; fixture mode in Wave 2 |
| Competitor extraction | OPERATIONAL — advertiser registry + evidence pack |
| Session manifests | REUSABLE — MIG session spine + paid SERP session summary |
| Run reports | OPERATIONAL |
| n8n / external automation | DOCUMENTED ONLY |
| Paid SERP business hours | OPERATIONAL (governed); live reliability SAFE UNKNOWN |
| Lifecycle gate | OPERATIONAL |

## Reuse decisions

- **Reused:** Corvonero `serp.json` schema shape, yabs ad URL detection, Playwright capture patterns (reference only)
- **Not rebuilt:** MIG session spine, ORCA semantic admission, lifecycle gate API
- **New:** Source registry schema v1, corpus reconciliation blocker, business-hours validator, evidence-pack manifest for SPPC-12 contribution

## Gaps requiring live validation

- Live Yandex Paid SERP collection reliability (anti-bot, layout drift)
- Uniform source-date enforcement across all legacy MIG paths
- n8n Search PPC workflow deployment state (remote SAFE UNKNOWN)

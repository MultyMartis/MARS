# PROFILE SEED ROOT CAUSE — Phase 3G.1.1

**Date:** 2026-08-06  
**Classification:** sanitized forensic — no PII

## Root cause chain

1. **Sidecar false positive** — Phase 3G.1 Sheets migration sidecar returned ok without verifying that ACCESS_CONTROL columns Q–V (profile fields) existed on the live workbook.
2. **Schema/sheet divergence** — Admin Upsert ACCESS_CONTROL node already mapped profile field values, but the physical sheet lacked the corresponding header row cells.
3. **n8n schema lag error** — When repair attempted appendOrUpdate against stale node column setup, Google Sheets node failed: `Column names were updated after the node's setup`.
4. **Display-name seed fragility** — Batch seed used exact short-token display_name matching; live rows use multi-token or username-shaped labels, so even a working seed script would have missed MOD_B_REVOKED and MOD_C_REVOKED without label-aware matching.

## Contributing factors

| Factor | Effect |
|--------|--------|
| No post-sidecar header verification | Defect undetected until Admin `/reply_profiles` showed dashes |
| Workflow schema ahead of sheet | Upsert mappings present; sheet columns absent |
| Exploratory inject before repair | Early Telegram cards delivered with empty `<pre>` copy (test_suppressed) |

## Repair approach (summary)

| Step | Method |
|------|--------|
| Create headers | Sheets API HTTP `values.update` → `ACCESS_CONTROL!Q1:V1` |
| Seed values | `values.batchUpdate` — 24 cells, label-aware row matching |
| Sync workflow schema | Patch Admin Upsert ACCESS_CONTROL to include profile fields aligned with live headers |
| Acceptance path | Narrow Ops patch: `classifyProbableTest` early-return for `PHASE_3G11_TEMPLATE_ACCEPTANCE_HUMAN` |

## Non-goals (preserved)

- No access-role changes
- No restoration of revoked users
- No n8n live mutation in documentation wave (repair already applied in prior operator session)

## Cross-reference

- Defect record: `LIVE-PROFILE-SEED-DEFECT-v1.md`
- Seeded values: `APPROVED-PROFILE-VALUES-v1.md`
- Live readback proof: `LIVE-PROFILE-READBACK-v1.md`

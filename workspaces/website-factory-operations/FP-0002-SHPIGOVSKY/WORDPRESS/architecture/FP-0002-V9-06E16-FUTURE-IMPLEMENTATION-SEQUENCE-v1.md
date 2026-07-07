# FP-0002 V9-06E16 — Future Implementation Sequence

**Evidence:** `validation/v9-06e16-operator-qa-closure-reusable-blocks-clone-cleanup-audit/future-implementation-sequence.json`

| Phase | Goal | Backup | Validation |
|-------|------|--------|------------|
| **E17** | Site Settings IA skeleton (Общие + Повторяемые блоки subpages) | YES | Admin tree; no frontend regression |
| **E18** | Reusable blocks fields + renderer migration (form, specialists, reviews, CTA) | YES | Per-block screenshot parity |
| **E19** | Service duplicate feature | YES | Draft clone, unique slug |
| **E20** | Obsolete pages trash (9, 25, 21) | YES | Privacy option still 3; route probes |

## Stop conditions

- E17: duplicate admin fields, reviews data loss
- E18: visual drift vs E15 operator baseline
- E19: published clone or public slug collision
- E20: any impact on ID 3 privacy page

## Recommended first task

**CREATE_V9_06E17_SITE_SETTINGS_IA_SKELETON_TASK**

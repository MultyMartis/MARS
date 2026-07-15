# PC14-FU03 Sandbox Implementation Manifest

**Date:** 2026-07-16
**Implementation:** `PC14_FU03_SANDBOX_IMPLEMENTATION`
**Based on design:** `PC14_FU03_SANDBOX_DESIGN_READY_FOR_IMPLEMENTATION`
**Design commit:** `fdbed1ad`

## Sandbox

| Field | Value |
|-------|-------|
| Name | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu03` |
| Id | `tVGWi7Ud3zz2eGKo` |
| Active | `false` |
| Nodes before | 92 |
| Nodes after | 101 |
| Webhook path | `seo-content-agent-worker-sandbox-pc14-fu03` |

## Production

| Field | Value |
|-------|-------|
| Worker id | `p4mqb4VuPcemIDlC` |
| Unchanged | `true` |
| Baseline nodes | 92 |
| TZ version | `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01` |

## Decision

| Field | Value |
|-------|-------|
| **Decision** | `PC14_FU03_SANDBOX_IMPLEMENTATION_APPLIED_HARNESS_VERIFIED` |
| **Recommended next** | `PC14_FU03_SANDBOX_IMPLEMENTATION_PERSIST` |
| **Harness allPass** | `true` |
| **Secret scan** | `PASS_WITH_REVIEW_LABELS` |

## Rollback

Delete sandbox workflow id `tVGWi7Ud3zz2eGKo` in n8n UI/API. Production `p4mqb4VuPcemIDlC` remains source of truth.

## Evidence

See files in `exports/pc14-fu03-sandbox-implementation/2026-07-16/`.

No stage. No commit.

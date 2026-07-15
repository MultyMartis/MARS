# PC14-FU03 Strict Surface Governance Manifest

- Audit: `PC14_FU03_STRICT_OUTPUT_SURFACE_GOVERNANCE_AUDIT`
- Date: 2026-07-14
- Worker (live GET): `p4mqb4VuPcemIDlC` · active=true · nodes=92 · updatedAt=2026-07-13T21:49:02.829Z
- TZ version: `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01`
- Smoke Task ID: `seo20260713221847nksocr`
- Smoke Worker execution: `3352` · status=success
- Related apply: `PC14_FU02_HOTFIX01_PRODUCTION_APPLIED_HARNESS_VERIFIED`
- Decision target: `PC14_FU03_GOVERNANCE_AUDIT_COMPLETE_REPAIR_LOOP_RECOMMENDED`
- Next: `PC14_FU03_REPAIR_LOOP_PROPOSAL` (persist audit separately if operator requires)

## Evidence files

- `SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu03-readonly.sanitized.json`
- `pc14-fu03-strict-surface-node-map.json`
- `pc14-fu03-run-output-surface-map.json`
- `pc14-fu03-qa-and-strict-gate-flow.json`
- `pc14-fu03-residual-surface-analysis.json`
- `pc14-fu03-governance-options.json`
- `pc14-fu03-readonly-gather-summary.json`
- `pc14-fu03-execution-node-outputs-redacted.json`
- `PC14-FU03-STRICT-SURFACE-GOVERNANCE-MANIFEST.md`

## Local raw (not for commit)

- `local/pc14-fu03-strict-surface-governance-2026-07-14/worker-production-readonly.raw.json`
- `local/pc14-fu03-strict-surface-governance-2026-07-14/worker-execution-3352.raw.json`

## Secret scan

Result: `PASS_WITH_REVIEW_LABELS`  
Repo evidence: workflow IDs, execution IDs, task IDs, redacted fields / operational labels only.  
Note: naive `sk-` regex matches substring inside `risk-scanner` version ids — false positive; ignored.  
Raw under `local/` only.

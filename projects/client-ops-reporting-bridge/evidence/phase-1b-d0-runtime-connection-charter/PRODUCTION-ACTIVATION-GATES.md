# Production Activation Gates — Phase 1B-D0

**Status:** GATES DEFINED — activation **FORBIDDEN** in this phase

## Mandatory gates (all required)

1. Durable dedupe verified (atomic uniqueness + duplicate suppression evidenced).
2. Producer contract verified (R1 or approved fallback).
3. Manual end-to-end live-source test verified (sanitized evidence).
4. Retry and failure semantics verified (including ambiguous timeout handling).
5. Telegram delivery policy verified (Pattern B; failures do not rewrite site_status).
6. Workflow rollback verified.
7. Producer rollback verified.
8. Scheduler dry-run verified (disabled task / no unexpected fire).
9. Clean runtime checkout verified (not dirty `X:\AI MARS`).
10. Secrets and rotation procedure verified.
11. Observability evidence verified (mandatory fields present; redacted).
12. No unresolved SAFE UNKNOWN affecting delivery correctness.
13. Explicit operator approval recorded.
14. Final inactive pre-activation snapshot (versionId, nodes, credentials metadata).
15. Baseline commit before activation (separate wave; not this phase).

## Explicit non-authorization

Phase 1B-D0 does **not** authorize production activation, durable activation, scheduler enablement, or unattended delivery.

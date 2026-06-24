# AG-WP-001 — Idempotency and Repeatability Contract v1

**Document type:** Idempotency contract  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24

---

## Classification

| Class | Operations |
|-------|------------|
| **IDEMPOTENT** | All `wp.inspect.*`; `wp.validate.*` relative to unchanged source/runtime |
| **CONDITIONALLY_IDEMPOTENT** | `wp.scaffold.*`, `wp.generate.*` — same inputs + empty target may no-op |
| **NON_IDEMPOTENT** | `wp.plan.*`, `wp.change.*`, `wp.backup.create`, `wp.checkpoint.create`, content creation |

---

## Repeatability requirements

| Requirement | Applies to |
|-------------|------------|
| Duplicate execution detection | all operations |
| Source/runtime fingerprint | validation, scaffold |
| Operation version | all |
| Migration/checkpoint ledger | R2+ mutations |
| Safe retry policy | R0 validation/inspect only |

---

## Retry policy summary

| Risk | Default retry |
|------|---------------|
| R0 read | up to 2 attempts |
| R1 plan | no auto-retry |
| R2+ mutation | no auto-retry without new approval |

---

*Idempotency contract v1.*

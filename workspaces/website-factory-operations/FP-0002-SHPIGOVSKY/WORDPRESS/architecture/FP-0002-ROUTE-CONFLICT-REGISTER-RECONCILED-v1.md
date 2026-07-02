# FP-0002 Route Conflict Register — Reconciled v1

**Task:** V9-06A.1 | **Date:** 2026-07-03  
**Supersedes planning ambiguity in:** `forge-intake/registers/FP-0002-V9-05A-ROUTE-CONFLICT-REGISTER-v1.md` (decisions only — foundation state unchanged)

---

## Decision summary

| Legacy / extra route | Decision | Target | Preconditions |
|---------------------|----------|--------|---------------|
| `/specyalisty/` | **REDIRECT_APPROVED** | `/uslugi/zavisimosti/specialistam/` | Canonical target 200; menu updated; redirect test; then retire legacy object |
| `/o-centre/intervyu-i-smi/` | **RETIRE_APPROVED** | — | No approved V9 replacement |
| `/pravovaya-informaciya-pilzovatelyu/` | **RETIRE_APPROVED** | — | V9 uses discrete legal slugs |
| `/uslugi/genotipirovanie/` | **EXCLUDED** | — | Forbidden; no canonical replacement |

---

## `/specyalisty/` — OD-002

| Field | Value |
|-------|-------|
| Legacy route | `/specyalisty/` |
| Canonical target | `/uslugi/zavisimosti/specialistam/` |
| Redirect type | 301 |
| Timing | **301_REDIRECT_AFTER_CANONICAL_TARGET_READY** |
| Legacy object | Must not remain independent public entity after migration |
| Rollback | Restore legacy Page; remove redirect rule |

---

## Not invented

No redirects defined for routes without approved targets (`intervyu-i-smi`, `pravovaya hub`, `genotipirovanie`).

---

*Planning authority — no runtime mutations.*

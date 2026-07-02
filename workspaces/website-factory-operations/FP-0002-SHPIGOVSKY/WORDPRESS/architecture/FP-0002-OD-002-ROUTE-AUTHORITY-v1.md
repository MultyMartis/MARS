# FP-0002 OD-002 Route Authority v1

**Decision ID:** OD-002  
**Task:** V9-06B final authority record  
**Date:** 2026-07-03  
**Status:** OPERATOR APPROVED — INTEGRATED

---

## Final operator-approved decision

| Field | Value |
|-------|-------|
| **Legacy route** | `/specyalisty/` |
| **Canonical route** | `/uslugi/zavisimosti/specialistam/` |
| **Canonical entity** | `SVC-SPECIALISTAM-ZAV` |
| **Action** | **301 redirect only** after the canonical Service exists and returns **HTTP 200** |

---

## Superseded proposal

The former proposal:

```text
/specyalisty/ → /specialistam/
```

is **SUPERSEDED** and must **not** remain as current authority in any active register, migration plan, or implementation task.

---

## V9-06B boundary

- Redirect **NOT IMPLEMENTED** in V9-06B.
- No rewrite rules, no menu updates, no Page/Service object mutations.
- Redirect execution deferred until canonical Service object exists (V9-06D+) and returns HTTP 200.

---

## Cross-references

- [FP-0002-ROUTE-CONFLICT-REGISTER-RECONCILED-v1.md](FP-0002-ROUTE-CONFLICT-REGISTER-RECONCILED-v1.md)
- [FP-0002-V9-ROUTE-ENTITY-TEMPLATE-MAP-v1.json](FP-0002-V9-ROUTE-ENTITY-TEMPLATE-MAP-v1.json)
- [FP-0002-WORDPRESS-ARCHITECTURE-DECISIONS-v1.md](FP-0002-WORDPRESS-ARCHITECTURE-DECISIONS-v1.md)

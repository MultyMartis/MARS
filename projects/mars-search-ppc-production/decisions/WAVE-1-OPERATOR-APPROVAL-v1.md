# Wave 1 Operator Approval — MARS Search PPC Production v1

**Decision ID:** `WAVE-1-OPERATOR-APPROVAL-v1`  
**Date:** 2026-06-22  
**Status:** `APPROVED — IMPLEMENTATION AUTHORIZED`  
**Authority:** [MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md](../MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md)

---

## Operator decisions (W1-D1 … W1-D7)

| ID | Decision |
|----|----------|
| **W1-D1** | `MARS SEARCH PPC PRODUCTION LIFECYCLE V1 — APPROVED` |
| **W1-D2** | `WAVE 1 — AUTHORIZED` (lifecycle authority and state enforcement) |
| **W1-D3** | Every Search PPC project must have a valid lifecycle state manifest before lifecycle work proceeds |
| **W1-D4** | Web-GPT and Cursor tasks must identify: project ID, current stage, completed approved stages, authoritative inputs, blockers, allowed work, forbidden work |
| **W1-D5** | Missing evidence → `BLOCKED — LIFECYCLE REQUIREMENT NOT MET`; no invented substitutes |
| **W1-D6** | Mass phrase-by-phrase operator classification **prohibited** as default production workflow (bounded conflicts, sampled QA, policy decisions, explicit request, benchmark only) |
| **W1-D7** | Corvonero: read-only lifecycle manifest; **do not resume production** |

---

## Lifecycle status transition

| From | To |
|------|-----|
| `PROPOSED — OPERATOR APPROVAL REQUIRED` | `APPROVED — IMPLEMENTATION AUTHORIZED` |

---

## Wave 1 boundary

Wave 1 is **authorized** but **not complete** until operator review of Wave 1 report.  
Do **not** self-grant `OPERATIONAL` for Wave 1 components.

---

## Related artifacts

- [MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-OPERATOR-DECISION-v1.md](./MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-OPERATOR-DECISION-v1.md)
- [WAVE-1-OPERATOR-APPROVAL-v1.json](./WAVE-1-OPERATOR-APPROVAL-v1.json)
- [MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md](../roadmap/MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md)

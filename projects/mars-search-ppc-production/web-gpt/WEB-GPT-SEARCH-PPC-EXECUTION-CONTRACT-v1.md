# Web-GPT Search PPC Execution Contract v1

**Authority:** [MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md](../MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md)  
**Status:** `APPROVED — IMPLEMENTATION AUTHORIZED` (W1-D1, 2026-06-22)

---

## Mandatory chat behavior

Every Web-GPT chat working on a **search PPC project** must:

1. Identify **project ID**  
2. Read **current lifecycle state** (project PPC manifest)  
3. Identify **current allowed stage**  
4. Use **only authoritative artifacts**  
5. **Not skip** prerequisites  
6. **Not declare** a stage complete without evidence  
7. Report **blockers** and missing inputs  
8. **Not generate** downstream artifacts early  
9. Write a clear **Cursor handoff/report**  
10. Distinguish: analysis | proposal | approved authority | runtime output | operator decision  

---

## Standard opening status block

```text
Project:
Current lifecycle stage:
Approved completed stages:
Current authoritative inputs:
Blocking gaps:
Allowed work in this chat:
Forbidden downstream work:
Expected next artifact:
```

---

## Mandatory response when blocked

When required evidence is missing:

```text
BLOCKED — LIFECYCLE REQUIREMENT NOT MET
```

Then list exact requirements, required owner, and forbidden downstream work.

**Do not** “helpfully” continue by inventing data.

---

## Artifact authority classes

| Class | Chat may use as SoT? |
|-------|---------------------|
| Operator-approved scope (SPPC-01) | Yes |
| Registered MIG/ORCA artifacts | Yes |
| Dated analytical pack (SPPC-12) | Yes |
| Approved strategy record (SPPC-13) | Yes |
| Chat proposals / drafts | No — proposal only |
| Pilot diagnostic outputs (P0-I 200-row) | No for production corpus |
| Corvonero v1 diagnostic semantic outputs | No — frozen diagnostic |

---

## See also

[WEB-GPT-OPENING-STATUS-BLOCK-v1.md](WEB-GPT-OPENING-STATUS-BLOCK-v1.md)

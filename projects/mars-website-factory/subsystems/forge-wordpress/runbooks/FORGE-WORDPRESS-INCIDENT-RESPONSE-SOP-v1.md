# Forge WordPress — Incident response SOP v1

**ID:** FW-RB-12  
**Status:** ACTIVE — OPERATIONS STANDARD  
**Date:** 2026-08-18  
**Evidence:** INC-03 iOS false PASS; INC-04 `mars-runtime`; INC-05 local residue

Lightweight SOP — not an on-call product.

---

1. **Stop mutation** — no more deploys, importers, “just one GET to test”  
2. **Identify blast radius** — routes, DB objects, users, mail, indexing  
3. **Snapshot** — files+DB or exact-file SHA pack proportional to risk  
4. **Establish runtime truth** — live FS, live DB, Dashboard versions ([FW-RB-01](FORGE-WORDPRESS-SOURCE-RUNTIME-AUTHORITY-STANDARD-v1.md))  
5. **Rollback or bounded fix** — not a rewrite of unrelated modules  
6. **Verify** — regression subset + the failed signal  
7. **Document incident lesson** — add to [INCIDENT-LESSONS](../knowledge/FORGE-WORDPRESS-PRODUCTION-INCIDENT-LESSONS-v1.md)  
8. **Update anti-pattern / standard** if systemic ([EXPERIENCE-HARVEST-LOOP](../knowledge/FORGE-WORDPRESS-EXPERIENCE-HARVEST-LOOP-v1.md))  

Examples of systemic → standard: leftover public runners (hygiene + module retirement); emulator PASS (device QA + transform ownership).

---

*FW-RB-12 v1.*

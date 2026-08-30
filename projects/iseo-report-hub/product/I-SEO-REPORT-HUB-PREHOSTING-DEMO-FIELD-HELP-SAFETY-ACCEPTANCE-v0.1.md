# I-SEO Report Hub — Pre-hosting Demo + Field Help Safety / Acceptance v0.1

**Status:** safety gate for charter + future waves  
**Date:** 2026-08-21  
**Wave:** Pre-hosting Demo Scenario and Field Help Charter 01

---

## This charter wave

| Rule | Status |
|------|--------|
| Code / app-source edits | **Forbidden** |
| Runtime edits / sync | **Forbidden** |
| DB mutation | **Forbidden** |
| User / report / project creation | **Forbidden** |
| Browser automation / POST | **Forbidden** |
| PDF / export / share mutation | **Forbidden** |
| Host upload / FTP / SFTP | **Forbidden** |
| Git push | **Forbidden** |
| Secrets / tokens / hashes printed | **Forbidden** |
| Docs under `product/` + `reports/` + OPERATIONAL-INDEX | **Allowed** |

---

## Future Field Help Implementation 01

- UI/render only  
- **No** DB migration for help text (static PHP map)  
- **No** client-preview help icons  
- Exact-path source → runtime sync only for touched assets  
- Preserve foreign WIP; no broad git add  

---

## Future Demo Seed Implementation 01

| Requirement | Detail |
|-------------|--------|
| Backup first | Dump `iseo_report_hub_dev` to approved Storage path |
| Rollback | Restore dump |
| Scope | New user + new client/project/site + periods/monthlies shells |
| Preserve | Demo Client, report 1 show-ready path, report 5 empty draft |
| Password | Local demo `test` only; never print hash |
| Host | Do not upload this DB until password policy revisited |

---

## Future Browser Fill Pass 01

- May mutate local DB **through UI** only for demo content  
- Firefox Developer + mars-research profile  
- On UI errors: screenshot + issue — no silent bypass  
- No PDF/export/share unless separately approved  
- No production clicks  

---

## Host / credential policy

- Subdomain `reports.i-seo.su` + SSL (operator) ≠ deploy authorization  
- PHP **8.3** recommended  
- Password `test` is **local/demo only**  
- Before any host upload: rotate/disable weak demo accounts; revisit password policy  
- Do not commit `.env`, share tokens, or session cookies  

---

## Acceptance criteria — this charter

Charter is **accepted** when all are true:

1. PHP host decision documented (8.3 + checks)  
2. Demo user plan documented (`seo_specialist`, email mapping)  
3. Realistic demo scenario plan documented (`ПРОВЕРКА.рa`, July/August)  
4. Browser-fill strategy documented  
5. Field help UX design documented  
6. Field help Russian copy pack documented  
7. Implementation sequence clear (Field Help first)  
8. Safety/acceptance documented  
9. OPERATIONAL-INDEX updated  
10. Closeout report committed on allowlisted paths only  

---

## Rollback for this charter

Docs-only: revert the exact commits on allowlisted paths. No DB/runtime rollback needed.

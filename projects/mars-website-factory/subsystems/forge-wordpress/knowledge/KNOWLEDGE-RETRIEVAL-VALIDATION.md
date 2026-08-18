# Knowledge-retrieval validation

**Date:** 2026-08-18  
**Method:** Answer Q1–Q3 **only** from canonical WP Forge docs (not FP-0002 report archaeology).  
**Expected:** PASS if a future agent can start from the hub.

---

## Q1 — We are starting a new medical/services WordPress site. What architecture should we use?

**Primary docs:** [BLUEPRINT](../standards/FORGE-WORDPRESS-PRODUCTION-WEBSITE-BLUEPRINT-v1.md) · [STARTER CHECKLIST](../templates/FORGE-WORDPRESS-NEW-SITE-STARTER-CHECKLIST-v1.md) · [CONTENT-MODEL-CPT](../standards/FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) · [MODULE-CATALOG](../registries/FORGE-WORDPRESS-MODULE-CATALOG-v1.md)

**Canonical answer (summary):**

- Do **not** copy clinical IA/copy/brand from the reference case.  
- Day 1: i18n, content-model registry, Site Settings SoT, Dashboard widget, SEO meta, native sitemap, native slugs, typography owner, standard WP menus.  
- Decide Page vs CPT **before coding**. People/staff with own URLs → CPT + hub Page (`has_archive=false`), not child Pages. Services with own URLs → CPT. Reviews: CPT vs options repeater is a **project** choice (options was used once — J).  
- Functionality plugin owns CPT/ACF/settings/forms; theme owns templates.  
- Optional: Smart Search, DOCX, Activity Log, social registry, forms.  
- Admin: Russian (or project locale) from the start; no demo fallbacks; no custom permalink UI.

**Retrieval:** PASS

---

## Q2 — We are moving a WP Forge site from staging to production. What is the required process?

**Primary docs:** [AUTHORITY](../runbooks/FORGE-WORDPRESS-SOURCE-RUNTIME-AUTHORITY-STANDARD-v1.md) · [DEPLOY SOP](../runbooks/FORGE-WORDPRESS-PRODUCTION-DEPLOYMENT-SOP-v1.md) · [ENVIRONMENT](../runbooks/FORGE-WORDPRESS-ENVIRONMENT-MIGRATION-STANDARD-v1.md) · [BACKUP](../runbooks/FORGE-WORDPRESS-BACKUP-ROLLBACK-STANDARD-v1.md) · [WPILOT](../runbooks/FORGE-WORDPRESS-WPILOT-PRODUCTION-STANDARD-v1.md) · [HYGIENE](../standards/FORGE-WORDPRESS-PUBLIC-WEBROOT-HYGIENE-GATE-v1.md)

**Canonical answer (summary):**

- Validate real docroot (not a placeholder jail).  
- WPilot READ; writes off unless chartered.  
- Live FS = runtime truth; live DB = content truth; Git = code.  
- Intake production drift before deploy; exact-file SHA deploy; no directory mirror.  
- Full files+DB backup at migration/baseline.  
- Clean env residue: `WP_ENVIRONMENT_TYPE`, debug, `.test`, localhost, demo, public runners/logs.  
- Keep indexing closed; keep mail suppress until SMTP on the real domain.  
- Git via clean worktree; no `git add .`.

**Retrieval:** PASS

---

## Q3 — We are ready to switch the final domain. What gates must pass first?

**Primary docs:** [LAUNCH SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md) · [DNS](../runbooks/FORGE-WORDPRESS-DNS-NS-CUTOVER-STANDARD-v1.md) · [READINESS MATRIX](../templates/FORGE-WORDPRESS-PRE-CUTOVER-READINESS-MATRIX-v1.md) · [DoD](../standards/FORGE-WORDPRESS-DEFINITION-OF-DONE-v1.md)

**Canonical answer (summary):**

Freeze → fresh full backup → parity → webroot/users/redirects → **inventory DNS including mail** → choose A-record vs NS → switch only when GO → verify authoritative DNS (web+mail) → SSL → home/siteurl → bounded URL migrate → smoke **with indexing still closed** → SMTP → form proof → **then** robots/indexability → consoles → sitemap submit → crawl.

Do not open indexing because HTTPS works. Do not NS-switch without copying MX/SPF/DKIM. Do not hardcode final-host redirects before the final host works.

**Retrieval:** PASS

---

## Score

| Question | PASS/FAIL |
|----------|-----------|
| Q1 | **PASS** |
| Q2 | **PASS** |
| Q3 | **PASS** |

Entry point for agents: [knowledge/README.md](README.md)

---

*Validation v1 — 2026-08-18.*

# Knowledge-retrieval validation

**Date:** 2026-08-18  
**Method:** Answer from canonical WP Forge docs only (not FP-0002 report archaeology).  
**Entry:** [knowledge/README.md](README.md)

- **Ops Q1–Q3** — build / migrate / cutover (production knowledge pack).  
- **CMS Q1–Q10** — Page/CPT/repeater/Options/design-to-schema (CMS architecture pack).

**Expected:** PASS if a future agent can start from the hub without inspecting FP-0002 source.

---

## Production operations retrieval (Ops Q1–Q3)

### Ops Q1 — We are starting a new medical/services WordPress site. What architecture should we use?

**Primary docs:** [BLUEPRINT](../standards/FORGE-WORDPRESS-PRODUCTION-WEBSITE-BLUEPRINT-v1.md) · [STARTER CHECKLIST](../templates/FORGE-WORDPRESS-NEW-SITE-STARTER-CHECKLIST-v1.md) · [CMS-ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) · [CONTENT-MODEL-CPT](../standards/FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) · [MODULE-CATALOG](../registries/FORGE-WORDPRESS-MODULE-CATALOG-v1.md)

**Canonical answer (summary):**

- Do **not** copy clinical IA/copy/brand from the reference case.  
- Day 1: i18n, content-model registry, Site Settings SoT, Dashboard widget, SEO meta, native sitemap, native slugs, typography owner, standard WP menus.  
- Decide Page vs CPT **before coding** using the CMS architecture pack (P1b maps). People/staff with own URLs → CPT + hub Page (`has_archive=false`), not child Pages. Services with own URLs → CPT. Reviews: CPT vs options repeater is a **project** choice (options was used once — J).  
- Functionality plugin owns CPT/ACF/settings/forms; theme owns templates.  
- Optional: Smart Search, DOCX, Activity Log, social registry, forms.  
- Admin: Russian (or project locale) from the start; no demo fallbacks; no custom permalink UI.

**Retrieval:** PASS

---

### Ops Q2 — We are moving a WP Forge site from staging to production. What is the required process?

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

### Ops Q3 — We are ready to switch the final domain. What gates must pass first?

**Primary docs:** [LAUNCH SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md) · [DNS](../runbooks/FORGE-WORDPRESS-DNS-NS-CUTOVER-STANDARD-v1.md) · [READINESS MATRIX](../templates/FORGE-WORDPRESS-PRE-CUTOVER-READINESS-MATRIX-v1.md) · [DoD](../standards/FORGE-WORDPRESS-DEFINITION-OF-DONE-v1.md)

**Canonical answer (summary):**

Freeze → fresh full backup → parity → webroot/users/redirects → **inventory DNS including mail** → choose A-record vs NS → switch only when GO → verify authoritative DNS (web+mail) → SSL → home/siteurl → bounded URL migrate → smoke **with indexing still closed** → SMTP → form proof → **then** robots/indexability → consoles → sitemap submit → crawl.

Do not open indexing because HTTPS works. Do not NS-switch without copying MX/SPF/DKIM. Do not hardcode final-host redirects before the final host works.

**Retrieval:** PASS

---

## Ops score

| Question | PASS/FAIL |
|----------|-----------|
| Ops Q1 | **PASS** |
| Ops Q2 | **PASS** |
| Ops Q3 | **PASS** |

---

## CMS / editable architecture retrieval (Q1–Q10)

**Method:** Answers below are taken from [CMS-ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) and its companion standards/templates. FP-0002 was not opened for these answers.

### Q1 — I have a design with 12 service cards. Should services be Page, repeater or CPT?

**Primary docs:** [CMS-ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) §3–4 · [REPEATER-VS-ENTITY](../standards/FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md) · [CONTENT-MODEL-CPT](../standards/FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md)

**Canonical answer:** If cards are the same class, will grow, need own URLs/SEO/Admin list/relations → **CPT** + hub Page (`has_archive=false`). Do not make 12 child Pages (AP-CMS-001). A repeater is only for parent-owned rows with no independent URL/lifecycle; 12 services with own pages are not that. Score ≥4 on the reusability table → CPT.

**Retrieval:** PASS

### Q2 — The phone appears in header, footer, contact page and floating header. Where should it be edited?

**Primary docs:** [GLOBAL-SETTINGS-OWNERSHIP](../standards/FORGE-WORDPRESS-GLOBAL-SETTINGS-OWNERSHIP-STANDARD-v1.md) · [SITE-SETTINGS](../standards/FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md)

**Canonical answer:** **Once** in Site Settings (contacts). Chrome and contacts **consume** that value. Never header+footer+contacts duplicate fields unless they are genuinely different business numbers. Empty → do not render `tel:`.

**Retrieval:** PASS

### Q3 — I have 80 reviews. Should this be an ACF repeater?

**Primary docs:** [REPEATER-VS-ENTITY](../standards/FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md) §2–3

**Canonical answer:** **No** as a page repeater. 80 rows is a collection. Prefer CPT if permalinks/authors/sitemap/Admin list are needed. Options repeater is a **J** exception only when items have no public single and editors accept Options UX. Promote when list-table/search/URL appears.

**Retrieval:** PASS

### Q4 — A page has 10 optional sections. Should we use Flexible Content?

**Primary docs:** [CMS-ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) §5, §8

**Canonical answer:** Not automatically. If the design is a **known stack**, use a **fixed structured template** plus per-section fields and empty/`enabled` hide. Use Flexible Content only for **controlled** reorderable layouts from a named registry — not an unlimited page builder. Ten optional sections often means structured fields + hide-when-empty, not Flex.

**Retrieval:** PASS

### Q5 — How do I turn a Figma page into the WordPress field schema?

**Primary docs:** [DESIGN-TO-CMS-WORKFLOW](../standards/FORGE-WORDPRESS-DESIGN-TO-CMS-WORKFLOW-v1.md) · [worksheet](../templates/FORGE-WORDPRESS-DESIGN-TO-CMS-MAPPING-WORKSHEET-v1.md)

**Canonical answer:** Mark elements → classify STATIC/GLOBAL/PAGE-LOCAL/ENTITY/REL/REPEATING/MEDIA/CTA → find reuse → choose storage → field schema → component contracts → Admin UX → editor validation. Do not start by creating ACF fields.

**Retrieval:** PASS

### Q6 — What should the editor see when adding a new specialist?

**Primary docs:** [EDITOR UX](../standards/FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md) §2 · [ADMIN IA](../standards/FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md) §4

**Canonical answer:** CPT **Добавить**: native title, native slug row, featured image (portrait SoT, no duplicate ACF photo), role/profile groups with human labels and “where it appears” help, relations, optional SEO, list table with thumbnail/name/type/order. No parent/template junk. No developer field keys as labels.

**Retrieval:** PASS

### Q7 — Should an internal CTA store a URL or relationship?

**Primary docs:** [RELATIONSHIP-MODELING](../standards/FORGE-WORDPRESS-RELATIONSHIP-MODELING-STANDARD-v1.md) · [ACF-FIELD-MODELING](../standards/FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md) §4

**Canonical answer:** **Relationship / Post Object** (plus type discriminator). Generate `get_permalink()` at render. Free URL only for external/anchors/special protocols. Do not store staging hostnames.

**Retrieval:** PASS

### Q8 — What fields should exist globally vs on a page?

**Primary docs:** [CMS-ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) §4.5, §6 · [GLOBAL-SETTINGS](../standards/FORGE-WORDPRESS-GLOBAL-SETTINGS-OWNERSHIP-STANDARD-v1.md)

**Canonical answer:** Global = multi-consumer business values (phones, social, identity, analytics IDs, global CTA defaults, header/footer controls). Page = unique Hero/sections/copy for that route. Entities = CPT. Do not put page Hero on Options or site phone on the Home ACF group.

**Retrieval:** PASS

### Q9 — How do I know that a repeater has become a real entity?

**Primary docs:** [REPEATER-VS-ENTITY](../standards/FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md) §4 promotion checklist

**Canonical answer:** Promote if the row needs URL/SEO, reuse across parents, dedicated Admin list, independent add/remove, search/sitemap, relations, draft/publish per item, or the parent form is unusable (nested/15+ fields/40+ rows). Then CPT/taxonomy/relationship — retire the repeater SoT.

**Retrieval:** PASS

### Q10 — What CMS documents must exist before frontend coding starts?

**Primary docs:** [CMS-ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) §16–18 · [BLUEPRINT P1b](../standards/FORGE-WORDPRESS-PRODUCTION-WEBSITE-BLUEPRINT-v1.md)

**Canonical answer:** Entity map, storage map, relationship map, Site Settings map, page editability/field map, component data contracts, Admin IA, editor workflow plan, URL ownership, SEO ownership, migration assumptions. CONTENT-MODEL summary plus the CMS pack templates. Frontend must not begin with unresolved ownership.

**Retrieval:** PASS

---

## Score

| Question | PASS/FAIL |
|----------|-----------|
| Ops Q1 | **PASS** |
| Ops Q2 | **PASS** |
| Ops Q3 | **PASS** |
| CMS Q1 | **PASS** |
| CMS Q2 | **PASS** |
| CMS Q3 | **PASS** |
| CMS Q4 | **PASS** |
| CMS Q5 | **PASS** |
| CMS Q6 | **PASS** |
| CMS Q7 | **PASS** |
| CMS Q8 | **PASS** |
| CMS Q9 | **PASS** |
| CMS Q10 | **PASS** |

Entry point for agents: [knowledge/README.md](README.md)

---

*Validation v1.1 — 2026-08-18 (CMS Q1–Q10 added).*

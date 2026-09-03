# ISEO-SU IMPLEMENTATION ROADMAP — 2026-09 v1

**Programme:** ISEO-SU-SITE-OPS  
**Companion authority:** [ISEO-SU-SEO-TEAM-NEW-TASK-PACK-2026-09-v1.md](ISEO-SU-SEO-TEAM-NEW-TASK-PACK-2026-09-v1.md)  
**Registered:** 2026-09-03  
**Mode:** practical action map — DOCUMENTATION ONLY until each wave is separately chartered

---

## Queue

### 1. FORM CONSENT

**Status:** **COMPLETE / RECONCILED** (WAVE 01A calculator-result patch 2026-09-03)

| Field | Value |
|-------|-------|
| **Scope** | Обязательный checkbox согласия на обработку ПДн на всех контактных формах с персональными данными; client + server validation; ссылка на действующую privacy page; централизация server check в shared helper при возможности. **Reconciled:** lead UI после «Рассчитать» в `tarif-calc.php` (form → `callback__FORM.php`) |
| **Dependencies** | Подтверждённый exact privacy policy URL; текущий form security baseline; HMAC / antispam / recipient не менять по смыслу |
| **Production mutation type** | Forms markup + `js/common.js` client rules + shared PHP validation (`iseo-form-security.php` / handlers as needed). No new handlers unless proven necessary |
| **Validation requirements** | Checkbox required UI; POST without consent rejected; HMAC/honeypot/min-fill/rate/dup still pass; recipient = `nikel007i33@yandex.ru` only; `test_mode` OFF; privacy link resolves 200 to approved URL |
| **Rollback expectation** | Restore prior form markup + JS + PHP helper from backup / previous production-source revision |
| **Documentation expected** | Wave REPORT + evidence update to form baseline if operating rules change |
| **Stop condition** | Consent baseline live and validated; no city/USA pages started in same wave |

---

### 2. CITY PAGES ×5

**Status:** **NEXT**

| Field | Value |
|-------|-------|
| **Scope** | 5 static SEO city pages cloned from `b-regionakh.html`; SEO-approved content only; hub «Выберите ваш город»; self-canonical on new pages; allowlist + regenerate static sitemap; completeness gate |
| **Dependencies** | WAVE 1 complete (forms inherit consent); SEO city content package; sitemap generator/allowlist model |
| **Production mutation type** | New static HTML under `/services/seo/`; edit hub page linking; update allowlist inventories; regenerate `sitemap-static.xml`; deploy static + sitemap surfaces |
| **Validation requirements** | 5× HTTP 200; self-canonical; `index,follow`; in static sitemap; hub links both ways; no new 4xx/5xx; completeness `PUBLIC_CANONICAL_STATIC_ROUTES - SITEMAP_STATIC_URLS = 0`; do **not** mass-fix old CANON-MISSING |
| **Rollback expectation** | Remove/unpublish 5 pages; revert hub links; revert allowlist + regenerate prior sitemap; restore previous deploy set |
| **Documentation expected** | Wave REPORT; sitemap evidence note; optional SEO-team note. Advego/Turgenev residual stays SEO-side |
| **Stop condition** | City pages + hub + sitemap validated; USA/UAE not started without separate charter |

**Target URLs:**

1. `/services/seo/prodvizhenie-v-sankt-peterburge.html`
2. `/services/seo/prodvizhenie-v-kazani.html`
3. `/services/seo/prodvizhenie-v-ekaterinburge.html`
4. `/services/seo/prodvizhenie-v-novosibirske.html`
5. `/services/seo/prodvizhenie-v-krasnoyarske.html`

---

### 3. USA/UAE DRAFT PAGES ×2

**Status:** **QUEUED / OPEN DECISIONS**

| Field | Value |
|-------|-------|
| **Scope** | 2 draft static pages cloned from `zarubezhnye.html` for SEO approval; no menu; no sitemap; content per SEO package; remove «Выберите тематику» |
| **Dependencies** | WAVE 1 preferred (form baseline); **OPEN:** pre-approval indexability; **OPEN:** title brand suffix (`itlseo` / `itlseo.su` vs `i-seo.su`); case URL existence check at implementation time |
| **Production mutation type** | New static HTML only (after decisions). Explicitly **no** menu entry, **no** sitemap allowlist add in this wave |
| **Validation requirements** | Pages exist for SEO review; layout/forms intact; menu/sitemap unchanged; indexability matches explicit decision; titles match confirmed brand policy; cases links verified |
| **Rollback expectation** | Delete/unpublish 2 draft pages; no sitemap/menu rollback needed if never added |
| **Documentation expected** | Wave REPORT recording decisions used + any residual SEO content anomalies |
| **Stop condition** | Do **not** deploy until indexability + title brand decisions recorded; do not invent `noindex` |

**Target URLs:**

- `/services/seo/prodvizhenie-v-ssha.html`
- `/services/seo/prodvizhenie-v-oae.html`

---

## Cross-cutting rules

1. Order locked: **1 → 2 → 3** unless operator overrides.
2. Each wave needs its own exact charter + backup + REPORT.
3. SEO review backlog (CANON-*, TITLE-*, META-*, etc.) is **out of scope** for this roadmap.
4. Registration of this roadmap does **not** authorize production mutations.

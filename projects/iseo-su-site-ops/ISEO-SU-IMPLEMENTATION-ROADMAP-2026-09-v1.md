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

**Status:** **COMPLETE** (2026-09-03) — evidence `ISEO-SU-CITY-PAGES-WAVE-02-EVIDENCE-v1.md`

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

### 3. USA/UAE SEO PAGES ×2

**Status:** **COMPLETE** (2026-09-03) — evidence `ISEO-SU-USA-UAE-PAGES-WAVE-03-EVIDENCE-v1.md`

| Field | Value |
|-------|-------|
| **Scope** | 2 static SEO pages cloned from `zarubezhnye.html`; Direct-ready; no menu; no sitemap; approved content; remove «Выберите тематику» on new pages only |
| **Decisions used** | **DIRECT-READY / NOT SITEMAP-PROMOTED**; normal indexability allowed (`index, follow`, no `noindex`); **INTLSEO** title suffix; cases verified 4/4 |
| **Production mutation type** | New static HTML only. Explicitly **no** menu entry, **no** sitemap allowlist add, **no** sitemap regen |
| **Validation requirements** | 2× HTTP 200; self-canonical; `index,follow`; not in menu; not in static sitemap (count **132**); INTLSEO titles; cases links verified; consent inherited |
| **Rollback expectation** | Delete/unpublish 2 pages; no sitemap/menu rollback needed |
| **Documentation expected** | Wave REPORT + evidence + RU closeout |
| **Stop condition** | WAVE 3 closed; do not start unrelated SEO-review backlog |

**Target URLs:**

- `/services/seo/prodvizhenie-v-ssha.html`
- `/services/seo/prodvizhenie-v-oae.html`

---

## Cross-cutting rules

1. Order locked: **1 → 2 → 3** unless operator overrides.
2. Each wave needs its own exact charter + backup + REPORT.
3. SEO review backlog (CANON-*, TITLE-*, META-*, etc.) is **out of scope** for this roadmap.
4. Registration of this roadmap does **not** authorize production mutations.

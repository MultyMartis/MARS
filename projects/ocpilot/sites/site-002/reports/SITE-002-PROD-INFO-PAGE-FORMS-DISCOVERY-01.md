# REPORT — SITE-002 Info Page Forms Discovery

**Operation ID:** SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01  
**OCPilot Run:** 4.229 — SITE-002 Info Page Forms Discovery  
**Date:** 2026-07-09  
**Environment:** PRODUCTION_READ_ONLY (`https://bzpm.ru/`)  
**Baseline before:** SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01  
**Checkpoint after:** unchanged — `SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01` (discovery only)

---

## 1. Scope

Read-only discovery for lower **Corporate CTA** forms on five SITE-002 information pages:

- Оборудование на заказ
- Оплата
- Доставка
- Дилерам
- Гарантия

Deliverables: URL inventory, live form inventory, source authority map, popup success-state reuse map, mail integration plan, frontend integration plan, and implementation charter for **`SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01`**.

**No production mutation.** No form submits. No mail sends.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Branch | `mars/canonical-post-recovery` @ `647bbbbe` |
| Staged changes before task | **None** scoped to this operation |
| Foreign WIP | Present elsewhere (FP-0002, unrelated ocpilot edits) — **not staged** |
| STOP tokens | **None** |

---

## 3. Target page URLs

| Page | URL | HTTP | Route | Corp CTA form |
|------|-----|------|-------|---------------|
| Оборудование на заказ | https://bzpm.ru/custom-equipment | 200 | `information/custom_equipment` | **yes** — `form.zpm-custom-form` |
| Оплата | https://bzpm.ru/payment-methods | 200 | `information/payment` | **yes** — `form.zpm-payment-form` |
| Доставка | https://bzpm.ru/delivery | 200 | `information/delivery` | **yes** — `form.zpm-delivery-form` |
| Дилерам | https://bzpm.ru/dealers | 200 | `information/dealers` | **yes** — `form.zpm-dealers-form` |
| Гарантия | https://bzpm.ru/guarantee | 200 | `information/guarantee` | **yes** — `form.zpm-warranty-form` |

All five target pages resolve with HTTP 200 and contain the expected bottom **`.zpm-corp-cta`** block with an individual form.

Storage: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01\forms\target-pages.{csv,json,md}`

---

## 4. Form inventory

### Root cause (all five forms)

Corp CTA forms are **markup-complete but handler-disconnected**:

1. `class="zpm-form"` present; **`data-fb-form` absent** — Fancybox submit pipeline does not bind.
2. Forms are **not** under `.zpm-dealers[data-dealers]` — isolated dealer handler in `main.js` does not bind.
3. `action="#"` — native submit performs no useful request.
4. No inline success-state container on page (unlike popup modals).

### Per-page summary

| Page | Form class | dialog (live) | dialog (recommended) | Email | Extra fields not in mail today |
|------|------------|---------------|--------------------|-------|--------------------------------|
| Оборудование на заказ | `zpm-custom-form` | **7** (dealers) | **11** | yes | company, contact, project_description, drawings, notes |
| Оплата | `zpm-payment-form` | — | **9** | yes | company, comment |
| Доставка | `zpm-delivery-form` | — | **8** | yes | region, delivery_method, order_details |
| Дилерам | `zpm-dealers-form` | **7** | **7** | yes | company, city, comment |
| Гарантия | `zpm-warranty-form` | — | **10** | yes | equipment_model, purchase_date, comment |

All forms: `method="POST"`, `action="#"`, reCAPTCHA/CSRF expected via shared `processSubmission()` once wired, loading UX available via Run 4.226 `zpmFormSetLoading()`.

Storage: `forms/info-page-form-inventory.{csv,json,md}`, masked HTTP extracts in `http/`.

---

## 5. Source template discovery

### Rendering chain

| Layer | Path | Role |
|-------|------|------|
| Information twig | `catalog/view/theme/default/template/information/{guarantee,delivery,payment,dealers,custom_equipment}.twig` | Page body; includes corp CTA section |
| Corp CTA section | `catalog/view/theme/default/template/sections/corpcta-{page}.twig` | **Renders live form inline** in `.zpm-corp-cta__form-card` |
| Form partials (exist) | `sections/corpcta-form-{page}.twig` | Alternate partial copies; live pages embed equivalent markup in `corpcta-*.twig` |
| Controller | `catalog/controller/information/{page}.php` | Loads twig; no form POST logic |
| Submit handler | `catalog/controller/checkout/anketa.php` | Unified AJAX endpoint (working for popups) |
| Mail renderer | `system/library/zpm/mail_renderer.php` | Admin + customer templates |
| Frontend | `assets/js/main.js`, `assets/css/style.css` | Popup `[data-fb-form]` + dealer handler only |

FTP read-only: **25/27** probed files downloaded; modification overlay for `anketa.php` / `guarantee.twig` — **missing** (no overlay).

Storage: `source-readonly/`, `manifests/source-authority-map.{csv,json,md}`

---

## 6. Working popup success-state discovery

**Reference:** popup «Задать вопрос» in `fancyboxforms.twig` (`#zpmFbQuestion`).

| Item | Value |
|------|-------|
| Wrap | `[data-fb-modal]` |
| Success block | `[data-fb-state="success"]` |
| Icon | `<svg class="zpm-icon success zpm-icon--lg"><use href="#zpm_ico__successful"></use></svg>` |
| Title | **Спасибо** (`zpm-fb__title section-title__like-h3`) |
| Text | **Ваша заявка отправлена!** (`zpm-fb__sub`) |
| JS | `setState(wrap, 'success')` on `fetch` ok; auto-close Fancybox after 3000 ms |

**Reuse for info pages:** inject equivalent markup into `.zpm-corp-cta__form-card` and toggle form/success states in-place — **do not** auto-close page; match icon + copy from popup.

Storage: `success-state/popup-success-state-map.{json,md}`

---

## 7. Mail integration discovery

**Handler:** `checkout/anketa.php` + `ZpmMailRenderer` — **reusable with extension**.

### Existing dialogs (Run 4.224–4.226)

| ID | Label |
|----|-------|
| 1 | Вопрос по товару |
| 2 | Запрос на обратный звонок |
| 3 | Вопрос по цене товара |
| 5 | Новый отзыв |
| 7 | Форма дилерам и оптовикам |

### Recommended new dialogs

| ID | Label | Pages |
|----|-------|-------|
| 8 | Вопрос по доставке | `/delivery` |
| 9 | Вопрос по оплате | `/payment-methods` |
| 10 | Гарантийное обращение | `/guarantee` |
| 11 | Оборудование на заказ | `/custom-equipment` |

### Gaps in current backend

- Page-specific POST fields (`company`, `region`, `equipment_model`, etc.) are **not** mapped into admin mail body.
- `company` POST is not assigned to `$data['company']`.
- `/custom-equipment` posts `dialog=7` — mislabels OEM requests as dealers.
- `source_page` / `page_url` support exists in `zpmResolvePageUrl()` — should be added as hidden field on all five forms.

### Customer confirmation

Per Run 4.226: send customer copy only when valid posted `email` or logged-in customer email; **no service info** in customer copy. All five forms have email — eligible when wired.

Storage: `mail/info-page-mail-integration-plan.{json,md}`

---

## 8. Frontend integration discovery

| Handler today | Selector | Success UX |
|---------------|----------|------------|
| Fancybox | `[data-fb-form]` | `setState(wrap,'success')` + icon |
| Dealer (home/katalog) | `.zpm-dealers[data-dealers] .zpm-form` | inline `.zpm-form__status-msg` text banner |

### Recommended integration

- **Selector:** `.zpm-corp-cta[data-corp-cta] form.zpm-form`
- **Pipeline:** reuse `processSubmission()` / `sendForm()` (CSRF + reCAPTCHA v3 + `fetch` anketa + `zpmFormSetLoading`)
- **Loading container:** `.zpm-corp-cta__form-card`
- **Success:** replace form view with popup-matching success panel (icon + «Спасибо» + «Ваша заявка отправлена!»)
- **CSS:** minor — reuse `.zpm-fb__state` / `.zpm-icon.success`; loading overlay already via `.zpm-form--loading`
- **Regression guard:** do not modify `[data-fb-form]` or `.zpm-dealers[data-dealers]` handlers

Storage: `forms/frontend-integration-plan.{json,md}`

---

## 9. Implementation charter

**Next operation:** `SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01`

Expected touched files:

- `sections/corpcta-{guarantee,delivery,payment,dealers,custom_equipment}.twig`
- `assets/js/main.js`
- `assets/css/style.css` (if needed for inline success)
- `catalog/controller/checkout/anketa.php`
- `system/library/zpm/mail_renderer.php`

Charter: `implementation-plan/SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01-CHARTER.{md,json}`

---

## 10. Read-only regression sanity

| URL | HTTP | БЗПМ public |
|-----|------|-------------|
| `/` | 200 | no |
| `/katalog` | 200 | no |
| `/katalog/nejtralnoe-oborudovanie` | 200 | no |
| `/katalog/nejtralnoe-oborudovanie/stoly` | 200 | no |
| `/llms.txt` | 200 | no |
| `/robots.txt` | 200 | no |
| `/sitemap.xml` | 200 | no |

Sitemap `<loc>` count at discovery time: **2567** (live feed; prior hygiene baseline **1408** PDP-focused count — different classification scope).

Storage: `verification/read-only-regression-sanity.{json,md}`

---

## 11. Production mutation summary

| Metric | Value |
|--------|-------|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| Remote renames | 0 |
| FTP write operations | 0 |
| Admin saves | 0 |
| DB direct operations | 0 |
| Mail sends | 0 |
| Form submits | 0 |
| SMTP config changes | 0 |
| Live mail trigger changes | 0 |
| Live mail template changes | 0 |
| Customer copy changes | 0 |
| Standard OpenCart mail changes | 0 |
| Product data changes | 0 |
| Category data changes | 0 |
| PDP changes | 0 |
| Category entrypoint changes | 0 |
| Images generated/uploaded | 0 |
| JS/CSS changes | 0 |
| llms.txt changes | 0 |
| Header/footer changes | 0 |
| Yandex.Metrika/Webmaster changes | 0 |
| Robots changes | 0 |
| Sitemap changes | 0 |
| Cron/import runs | 0 |
| Cache clears | 0 |
| External GeoIP/API calls | 0 |
| public БЗПМ introduced | **no** |

---

## 12. Storage artefacts

Root: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01\`

| Folder | Contents |
|--------|----------|
| `manifests/` | `operation.json`, `source-authority-map.*`, `ftp-downloads.json` |
| `http/` | Masked HTML extracts per target page |
| `forms/` | Target pages, form inventory, frontend plan |
| `success-state/` | Popup success-state reuse map |
| `mail/` | Mail integration plan |
| `implementation-plan/` | Integration charter |
| `verification/` | Regression sanity |
| `source-readonly/` | 25 FTP-downloaded production files |
| `reports/` | `operation-summary.json` |

Repo tool: `projects/ocpilot/sites/site-002/tools/site-002-prod-info-page-forms-discovery-01.py`

---

## 13. Authority updates

Updated in-repo:

- `projects/ocpilot/OPERATIONAL-INDEX.md` — Run 4.229
- `projects/ocpilot/OCPILOT-STATE.md`
- `projects/ocpilot/sites/site-002/production-profile.md`
- `projects/ocpilot/sites/site-002/site-passport.md`
- `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md`
- `projects/ocpilot/sites/site-002/tools/README.md`
- `projects/ocpilot/sites/site-002/baselines/SITE-002-INFO-PAGE-FORMS-DISCOVERY-01.md`

---

## 14. Git status

Selective commit of discovery docs + tool only. Foreign WIP excluded. Storage artefacts not committed.

---

## 15. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Target pages missing | **None** — all 5 found |
| Exact template source | **Confirmed** — corpcta twigs + anketa/mail_renderer/main.js |
| Sitemap count vs hygiene baseline | **SAFE UNKNOWN** — 2567 live `<loc>` vs 1408 prior PDP-focused audit; different scope/method |
| Customer inbox delivery (Run 4.226) | Still **SAFE UNKNOWN** — out of scope for this discovery |

**No blockers** for integration charter.

---

## 16. Final verdict

**SITE-002 INFO PAGE FORMS DISCOVERY COMPLETE — INTEGRATION CHARTER READY**

---

## 17. Next task recommendation

Execute **`SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01`**:

1. Wire corp CTA forms to existing `checkout/anketa` AJAX pipeline.
2. Add dialog IDs **8–11** + `source_page` hidden fields; fix `/custom-equipment` dialog mislabel.
3. Extend `anketa.php` + `ZpmMailRenderer` for page-specific fields.
4. Reuse Run 4.226 loading/abort UX.
5. Inline success-state matching popup «Задать вопрос».
6. Controlled test submits per form; regression on popup/dealer forms.

Production checkpoint remains **`SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01`** until integration run completes.

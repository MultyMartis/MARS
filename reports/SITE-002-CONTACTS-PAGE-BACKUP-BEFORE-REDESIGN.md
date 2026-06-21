# REPORT — SITE-002 Contacts Page Backup Before Redesign

**Project:** SITE-002 (ЗПМ / BZPM)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Date:** 2026-06-21  
**Mode:** Backup only — no deploy, no live changes, no commit/push

---

## 1. URL

| Field | Value |
|-------|-------|
| **Canonical live URL** | https://zpm.new-site.space/contact/ |
| **OpenCart route** | `index.php?route=information/contact` |
| **Task URL (requested)** | https://zpm.new-site.space/contacts/ |

**Note:** `/contacts/` returns **HTTP 404**. All navigation on live TEST uses `/contact/` (header, footer, offcanvas). Both `/contact/` and `?route=information/contact` return **HTTP 200** with identical main content.

**Live HTML capture:** `projects/ocpilot/sites/site-002/reports/contacts-backup-work/live-capture/contact-page.html`  
**SHA256:** `4e8f518d9b708dc5b259b1b0a399d033611e5341c62eb8bded2e23d69bd60305` (84 727 bytes)  
**Captured at:** 2026-06-21 (curl live fetch)

---

## 2. Render chain

```
GET /contact/
  └─ SEO rewrite → index.php?route=information/contact
       └─ catalog/controller/information/contact.php
            ControllerInformationContact::index()
              ├─ language: catalog/language/ru-ru/information/contact.php
              ├─ document: setTitle(heading_title)
              ├─ Breadcrumbs helper → setBreadcrumbs()
              ├─ Pageintro helper → setPageintro(title only, description='')
              ├─ $data['blockanyquestionsform'] = view('sections/blockanyquestionsform')
              ├─ $data['yandexmap']             = view('sections/yandexmap')
              ├─ common/header, common/footer, column_left/right, content_top/bottom
              └─ output: view('information/contact')
                   └─ <main class="main">
                        ├─ contacts-blocks (inline in contact.twig)
                        ├─ {{ blockanyquestionsform }}
                        └─ {{ yandexmap }}

common/footer.twig (layout shell, not main redesign target)
  └─ {{ citypopup }} → sections/citypopup.twig
       └─ inline <script>: CITY_DATA + updateCityUI()
            └─ on DOMContentLoaded: sync address/phone/email/schedule + map city
               via data-* hooks on contact page cards
```

**Page chrome outside `<main>`:** breadcrumbs + H1 (`page-intro`) are injected via document helpers (`Breadcrumbs`, `Pageintro`) and rendered in the header wrapper — not in `contact.twig`.

**Legacy controller paths (unused by current main markup):** controller still loads OpenCart settings (`config_address`, `config_telephone`, `config_email`, `config_open`, `locations[]`) and exposes standard POST/mail/captcha flow for fields `name`, `email`, `enquiry`. Current Twig main content does **not** consume these variables.

---

## 3. Files captured

**Capture root:** `projects/ocpilot/sites/site-002/reports/contacts-backup-work/live-capture/`  
**Manifest:** `live-capture/manifest.json` (FTP read-only, 2026-06-21T16:14:27Z)  
**Capture script:** `contacts-backup-work/contacts-backup-capture.py` (read-only helper; not executed on live except RETR)

| Remote (Beget FTP) | Local backup file | SHA256 |
|--------------------|-------------------|--------|
| `catalog/controller/information/contact.php` | `catalog__controller__information__contact.php` | `bf45758458aa601e538f95e563d726f848d83f6380b052264e4955063a9487a7` |
| `catalog/view/theme/default/template/information/contact.twig` | `catalog__view__theme__default__template__information__contact.twig` | `2b80ac985e71d55cee21084be13b90c4da6388d576b676e06e924faaa0337408` |
| `catalog/view/theme/default/template/sections/blockanyquestionsform.twig` | `catalog__view__theme__default__template__sections__blockanyquestionsform.twig` | `966d8c05fbfb51ad001e6a3dd387b28c31acba11100c0cdd3d7aeb2ea6d347cc` |
| `catalog/view/theme/default/template/sections/yandexmap.twig` | `catalog__view__theme__default__template__sections__yandexmap.twig` | `7f6750276402f179f23345920a1062f66dbd787f9c6f936cd7baa63664f9d377` |
| `catalog/view/theme/default/template/sections/citypopup.twig` | `catalog__view__theme__default__template__sections__citypopup.twig` | `a014b5d4cefec05b8914f11dd2ff218a99d4afaa644c21f5273e819e0d2e7f04` |
| `catalog/view/theme/default/template/common/footer.twig` | `catalog__view__theme__default__template__common__footer.twig` | `fde99fff141c1c5df6f31c03f67237e3c220651f2cd761678171244cff341141` |
| `catalog/language/ru-ru/information/contact.php` | `catalog__language__ru-ru__information__contact.php` | `e6fa0b4972a6a297d06809423a6f1d558ac90691b6b0c59c9086a19be25c9142` |
| `assets/css/style.css` | `assets__css__style.css` | `ffc50c73dc48e86d2a0207cb57a82146db2894d23860299c511f421f326f10c8` |
| `assets/css/sd.css` | `assets__css__sd.css` | `bebca7741d33b527a273bb51f9b0667d1cceb560de2922a60c67be35a6492c25` |
| `assets/js/main.js` | `assets__js__main.js` | `3ab098c786099c24e3ccf33e852b0aacc2d66089e81830e2b48af97db3920dbe` |
| *(HTTP)* live page HTML | `contact-page.html` | `4e8f518d9b708dc5b259b1b0a399d033611e5341c62eb8bded2e23d69bd60305` |

**CSS scope for contacts main content (inside monolithic `style.css`):**

| Selector / block | Approx. line | Role |
|------------------|--------------|------|
| `.contacts-blocks`, `.contacts-block--item*` | ~8138–8197, 11010+, 11421+ | Contact info cards grid |
| `.zpm-universal__grid`, `.zpm-dealers__text` | ~1594–1631, 5996+ | Form section layout (shared with dealers/about patterns) |
| `.zpm-map`, `.map-wrapper` | ~10253–10279 | Map container |

`sd.css` — site-wide header/search tweaks only; **not** contacts-specific.

---

## 4. Main content source

**Primary Twig:** `catalog/view/theme/default/template/information/contact.twig`

Structure inside `<main class="main">`:

1. **Contact cards** — `.contacts-blocks` with five items: Адрес, Телефон, E-mail, График, Реквизиты
2. **Form section** — injected via `{{ blockanyquestionsform }}`
3. **Map section** — injected via `{{ yandexmap }}`

**Controller wiring** (`contact.php` lines 10–11):

```php
$data['blockanyquestionsform'] = $this->load->view('sections/blockanyquestionsform');
$data['yandexmap'] = $this->load->view('sections/yandexmap');
```

---

## 5. Form source

**Twig:** `catalog/view/theme/default/template/sections/blockanyquestionsform.twig`  
**Section class:** `.zpm-any-questions`  
**Form:** `<form class="zpm-form" action="#" method="post">`

| Field | name | Hooks |
|-------|------|-------|
| Имя | `name` | `required` |
| Телефон | `phone` | `data-mask="phone"` |
| E-mail | `email` | `data-validate="email"`, `required` |
| Вопрос | `message` | textarea |
| Согласие | `agree` | checkbox (not `required` in markup) |

**Submit behaviour (live):**

- `action="#"` — **no server endpoint** wired in Twig
- **Not** handled by OpenCart `ControllerInformationContact` POST (expects `enquiry`, not `message`/`phone`)
- Dealer AJAX handler in `main.js` targets `.zpm-dealers[data-dealers] .zpm-form` only — **does not** bind to contacts form

**JS dependencies (documented, not modified):**

| Dependency | Role on contact page |
|------------|---------------------|
| `assets/js/main.js` — global `initPhoneMask()` | Applies Inputmask to `[data-mask="phone"]` on page load |
| `assets/js/main.js` — global `initEmailValidation()` | Validates `[data-validate="email"]` |
| `assets/js/vendor/inputmask/*` | Phone mask vendor |
| `sections/citypopup.twig` inline script | Unrelated to form submit; city sync only |

**Form styling:** reuses `.zpm-form*`, `.zpm-universal__grid*`, `.zpm-dealers__text` from shared ZPM form patterns in `style.css`.

---

## 6. Map source

**Twig:** `catalog/view/theme/default/template/sections/yandexmap.twig`  
**Wrapper:** `.zpm-map[data-zpm-map]`

Three hardcoded Yandex Constructor embeds (one visible per selected city):

| City key | `data-map-city` | Constructor `um=` hash (truncated) |
|----------|-----------------|-------------------------------------|
| Москва | `moscow` | `…b46be8dded5afb419e02197b62ebb64f484af891…` |
| Краснодар | `krasnodar` | `…5aa40f7631d8103db2d46a12903cd1305acd155…` |
| Барнаул | `barnaul` | `…b4c58b29dfff6cea9dd621ae2c859c6bab5876…` |

**City visibility:** `updateCityUI()` in `citypopup.twig` toggles `[data-map-city]` blocks (`hidden` attribute). Default city on first visit: `localStorage.selected_city || 'barnaul'`.

**Related (city data driving contact cards):** `sections/citypopup.twig` — hardcoded `CITY_DATA` object for moscow/krasnodar/barnaul (address, phone, email, schedule). Loaded globally via `common/footer.twig` → `{{ citypopup }}`.

---

## 7. Hardcoded vs settings-driven data

| Data | Source | Notes |
|------|--------|-------|
| H1 «Контакты» | Language file + Pageintro helper | `$_['heading_title']` |
| Breadcrumb label | Language file | `heading_title` |
| **Address / phone / email / schedule (initial HTML)** | **Hardcoded in `contact.twig`** | Default values = Barnaul; overwritten at runtime by `updateCityUI()` |
| **Реквизиты (OOO name, INN/KPP)** | **Hardcoded in `contact.twig`** | No `data-*` hooks; **not** city-switched |
| City-specific address/phone/email/schedule | **Hardcoded in `citypopup.twig` `CITY_DATA`** | JS replaces card + footer fields |
| Yandex map embeds | **Hardcoded in `yandexmap.twig`** | Per-city constructor URLs |
| Form copy / fields | **Hardcoded in `blockanyquestionsform.twig`** | |
| OC store settings (`config_address`, `config_telephone`, etc.) | Loaded in controller | **Not rendered** in current contact main Twig |
| OC locations model | Loaded in controller | **Not rendered** in current contact main Twig |
| Legacy OC POST mail flow | Controller `validate()` + Mail | **Not connected** to visible form |

**Placeholder data observed:** Krasnodar entry in `CITY_DATA` uses `8 (000) 000-00-00` and `ул. АДРЕС, д. ДОМ` — likely staging placeholders.

---

## 8. Rollback paths

| Method | Path / action |
|--------|---------------|
| **File-level restore (preferred for contacts redesign rollback)** | Upload captured files from `live-capture/` back to matching FTP remote paths (see §3 table) |
| **Twig cache** | After Twig restore: clear `system/storage/cache/template/*` on server |
| **HTML reference** | Compare post-change output against `contact-page.html` |
| **Disaster recovery** | Operator Beget full backup (documented in site passport; not re-captured in this pass) |
| **Authority baseline** | `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` — contacts page was not part of M9.8.9 catalog UX cluster; this backup is the contacts-specific rollback source |

**Minimal rollback set for main-content-only redesign:**

1. `information/contact.twig`
2. `sections/blockanyquestionsform.twig`
3. `sections/yandexmap.twig`
4. Relevant slices of `assets/css/style.css` (or full file if diff scope unclear)
5. If city behaviour breaks: `sections/citypopup.twig`

---

## 9. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Whether `/contacts/` ever existed or should be added as SEO alias | **UNKNOWN** — 404 on live; all internal links use `/contact/` |
| Intended backend for «Остались вопросы?» form (OC mail, `checkout/anketa`, CRM) | **UNKNOWN** — `action="#"`, no submit handler |
| Whether requisites should be city-specific | **UNKNOWN** — currently static, not in `CITY_DATA` |
| Krasnodar phone/address placeholders — final production values | **UNKNOWN** — placeholder strings in live `CITY_DATA` |
| OpenCart / ocStore exact version on TEST | **UNKNOWN** (per site passport) |
| Whether admin Information settings are intended to drive contact cards in a future pass | **UNKNOWN** — controller loads them but Twig ignores |

---

## Git

**Commit:** NO  
**Push:** NO

**Artifacts created (untracked):**

- `reports/SITE-002-CONTACTS-PAGE-BACKUP-BEFORE-REDESIGN.md` (this file)
- `projects/ocpilot/sites/site-002/reports/contacts-backup-work/` (capture + helper script)

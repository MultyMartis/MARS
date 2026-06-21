# REPORT — SITE-002 CONTACTS PAGE POLISH V1

**Project:** SITE-002 (ЗПМ / BZPM)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Date:** 2026-06-21  
**Live URL:** https://zpm.new-site.space/contact/  
**Mode:** Deploy + automated QA — operator visual QA pending

**PRE-TASK RULE:** Knowledge Map + Stable Checkpoint + Contacts redesign report + Contacts backup report — read and applied.

---

## 1. ATLAS Data Used

**Source:** [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](../../../atlas/population/ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](../../../atlas/population/ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) §7.1 LE-0004

| Field | Value (attested) | Used on page |
|-------|------------------|--------------|
| Полное наименование | Общество с ограниченной ответственностью «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | **Yes** |
| ИНН | 2221237587 | **Yes** |
| КПП | 222101001 | **Yes** |
| ОГРН | 1172225049787 | **Yes** |
| Юридический адрес | 656011, Россия, г. Барнаул, пр-т Калинина, 15в, оф. 110 | **Yes** |
| Фактический адрес | 656011, Россия, г. Барнаул, пр-т Калинина, 15в, оф. 110 | **Yes** |

**Not invented:** bank details, signatory, beneficial owner, registration date — omitted (not requested for card; no placeholders).

---

## 2. Icons Replaced

All contact-page icons switched from `fal` (Light) to **FA5 Pro Duotone** (`fad`) per task. Brand icons use `fab` where specified.

### Contact cards

| Card | Before | After |
|------|--------|-------|
| Адрес | `fal fa-map-marker-alt` | `fad fa-map-marked-alt` |
| Телефон | `fal fa-phone` | `fad fa-phone-alt` |
| E-mail | `fal fa-envelope` | `fad fa-envelope-open-text` |
| График | `fal fa-clock` | `fad fa-clock` |

### Company summary (3 icon facts)

| Fact | Icon |
|------|------|
| Собственное производство в Барнауле | `fad fa-industry-alt` |
| Документы для закупки | `fad fa-file-certificate` |
| Сертифицированная продукция | `fad fa-badge-check` |

Fourth fact («Отгрузка по всей России») — bullet only, no icon in task spec.

### Как добраться

| Item | Before | After |
|------|--------|-------|
| На автомобиле | `fal fa-car` | `fad fa-truck` |
| Общественный транспорт | `fal fa-bus` | `fad fa-bus-alt` |
| Самовывоз | `fal fa-boxes` | `fad fa-dolly-flatbed` |

**FA stack:** Font Awesome Pro 5.15.4 via `/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css` (unchanged).

---

## 3. Messenger Cards Added

New row **after** primary contact cards, **before** company summary — same `zpm-contact-card` visual pattern.

| Channel | Icon | URL |
|---------|------|-----|
| MAX | `fad fa-comments-alt` *(neutral communication; no direct MAX duotone in FA5)* | **None** — static card |
| Telegram | `fab fa-telegram-plane` | **None** — static card |
| WhatsApp | `fab fa-whatsapp` | **None** — static card |

**URL probe:** live footer social links on `/` and `/contact/` → `href="#"`; `oc_setting` search (`%telegram%`, `%whatsapp%`, `%max%`, `%social%`) → **0 hits**. Cards rendered without active links per task rule.

**CSS:** `.zpm-contact-cards--messengers`, `.zpm-contact-cards__grid--messengers` (3 → 2 → 1 columns responsive).

---

## 4. Files Changed

| Remote (live) | Action | Backup |
|---------------|--------|--------|
| `catalog/view/theme/default/template/information/contact.twig` | Replaced icons, requisites, messenger row, summary icons | `backups/contact.twig.pre-contact-polish-v1.bak` |
| `catalog/view/theme/default/template/sections/blockanyquestionsform.twig` | Unchanged (backup only) | `backups/blockanyquestionsform.twig.pre-contact-polish-v1.bak` |
| `assets/css/style.css` | Appended polish block (~50 lines) | `backups/style.css.pre-contact-polish-v1.bak` |

**Work artifacts:**

- `reports/contacts-polish-work/contact.twig`
- `reports/contacts-polish-work/contacts-polish.css`
- `reports/contacts-polish-work/contacts-polish-deploy.py`
- `reports/contacts-polish-work/style.css.patched`
- `reports/contacts-polish-work/qa-contact-polish.html`
- `reports/contacts-polish-work/manifest-post-20260621-170509.json`

### Deploy SHA verify

| File | SHA256 pre | SHA256 post | Verify |
|------|------------|-------------|--------|
| `contact.twig` | `d33d78fe…` | `6fdafb66…` | OK |
| `blockanyquestionsform.twig` | `6f137ec0…` | `6f137ec0…` | OK |
| `style.css` | `0a159c01…` | `193c1543…` | OK |

**Not changed:** map, form fields/names, 3-column grid, header, footer, controllers, JS.

---

## 5. QA

| # | Check | Result |
|---|-------|--------|
| 1 | `/contact/` opens | **PASS** — HTTP 200, automated capture |
| 2 | Layout structure intact | **PASS** — same sections/grid; messenger row additive only |
| 3 | All duotone icons present | **PASS** — 10× `fad` in HTML capture |
| 4 | Telegram displays | **PASS** — `fab fa-telegram-plane` |
| 5 | WhatsApp displays | **PASS** — `fab fa-whatsapp` |
| 6 | MAX displays | **PASS** — `fad fa-comments-alt` |
| 7 | Requisites from ATLAS | **PASS** — full name, ИНН, КПП, ОГРН, legal + actual addresses |
| 8 | Mobile 390px no overflow | **PENDING** — operator visual QA |
| 9 | No JS errors | **PENDING** — operator browser console check |

**Automated capture:** `reports/contacts-polish-work/qa-contact-polish.html` (92 111 bytes).

---

## 6. Rollback

1. Upload from `backups/*.pre-contact-polish-v1.bak` to matching FTP paths.
2. Clear `system/storage/cache/template/*` on server.
3. Verify `/contact/` against pre-polish state (`contact.twig` SHA `d33d78fe…`).

**Minimal rollback set:** `contact.twig`, `style.css` (form twig unchanged).

---

## 7. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Messenger URLs (MAX / Telegram / WhatsApp) | **Not configured** on live — footer `href="#"`; no `oc_setting` keys found |
| MAX brand icon in FA5 Duotone | **No direct icon** — used `fad fa-comments-alt` as neutral communication |
| Mobile 390px overflow / visual polish | **PENDING** operator visual QA |
| JS console on contact page | **PENDING** operator check |
| Bank / payment requisites | **Not in ATLAS card scope** for this task — omitted |
| «Построить маршрут» vs citypopup | Pre-existing — static Barnaul Yandex URL; citypopup not modified |

---

## Git

**Commit:** NO  
**Push:** NO

**Operator next step:** visual QA at 390px / 1024px / desktop on https://zpm.new-site.space/contact/

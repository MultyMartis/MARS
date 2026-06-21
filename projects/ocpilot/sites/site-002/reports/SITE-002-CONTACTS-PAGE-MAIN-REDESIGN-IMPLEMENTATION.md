# REPORT — SITE-002 CONTACTS PAGE MAIN REDESIGN IMPLEMENTATION

**Project:** SITE-002 (ЗПМ / BZPM)  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Date:** 2026-06-21  
**Live URL:** https://zpm.new-site.space/contact/  
**Mode:** Deploy + automated QA — operator visual QA pending

---

## 1. What Changed

Main content between page intro and map/footer redesigned into three sections:

1. **Contact cards** — 4-card grid (Адрес, Телефон, E-mail, График работы) with FA Pro Light icons, values, and actions.
2. **Company summary card** — internal logo visual placeholder + H2, compact facts, production text.
3. **Details row** — 3 columns: Реквизиты | Форма «Напишите нам» | Как добраться.

**Not changed:** header, breadcrumbs, H1/page-intro, Yandex map embeds, footer, `citypopup.twig`, `CITY_DATA`, controllers, JS.

**Removed from main:** legacy `.contacts-blocks` 5-card grid and `.zpm-any-questions` two-column form layout.

---

## 2. Render Chain

```
GET /contact/
  └─ index.php?route=information/contact
       └─ catalog/controller/information/contact.php
            ├─ blockanyquestionsform → sections/blockanyquestionsform.twig (form card only)
            ├─ yandexmap → sections/yandexmap.twig (unchanged)
            └─ information/contact.twig (new 3-section main)
                 └─ <main>
                      ├─ zpm-contact-cards
                      ├─ zpm-contact-summary
                      ├─ zpm-contact-details (+ {{ blockanyquestionsform }})
                      └─ {{ yandexmap }}

common/footer.twig → citypopup.twig (CITY_DATA sync on data-* hooks — unchanged)
```

---

## 3. Files Changed

| Remote (live) | Action | Backup |
|---------------|--------|--------|
| `catalog/view/theme/default/template/information/contact.twig` | Replaced main markup | `backups/contact.twig.pre-contact-redesign.bak` |
| `catalog/view/theme/default/template/sections/blockanyquestionsform.twig` | Form card for center column | `backups/blockanyquestionsform.twig.pre-contact-redesign.bak` |
| `assets/css/style.css` | Appended `zpm-contact-*` block (~320 lines) | `backups/style.css.pre-contact-redesign.bak` |

**Work artifacts:**

- `reports/contacts-redesign-work/contact.twig`
- `reports/contacts-redesign-work/blockanyquestionsform.twig`
- `reports/contacts-redesign-work/contacts-redesign.css`
- `reports/contacts-redesign-work/contacts-redesign-deploy.py`
- `reports/contacts-redesign-work/live-capture/` (pre-deploy FTP capture)
- `reports/contacts-redesign-work/manifest-post-20260621-164110.json`
- `reports/contacts-redesign-work/qa-contact.html` (post-deploy HTTP capture)

### Deploy SHA verify

| File | SHA256 pre (live capture) | SHA256 post-deploy | Verify |
|------|---------------------------|-------------------|--------|
| `contact.twig` | `2b80ac985e71d55cee21084be13b90c4da6388d576b676e06e924faaa0337408` | `d33d78fe125d46a0bf64eb7fabef3730e2da844107357197ed42a2cdfca07381` | OK |
| `blockanyquestionsform.twig` | `966d8c05fbfb51ad001e6a3dd387b28c31acba11100c0cdd3d7aeb2ea6d347cc` | `6f137ec007974d7e8df44de29d780132482e7fa82dc470e76070bfced6d9a740` | OK |
| `style.css` | `43efd997a4334b21ad906ff1eba315035c57204771738284cc7d23292cde24c7` | `0a159c01b286515a9b49e79be5feefdbcd5f3ba89eddb03f502bed0dd8ebf7b1` | OK |

**Note:** `style.css` pre-deploy SHA differs from contacts backup report (`ffc50c73…`) — live TEST had drift since 2026-06-21 backup capture; fresh FTP capture used as rollback source.

**Twig cache:** deploy script attempted clear of `system/storage/cache/template/` — no files reported deleted (may already be empty or path permissions).

---

## 4. New Main Structure

### Section 1 — Contact cards (desktop: 4 columns)

| Card | Value (default Barnaul) | Action |
|------|-------------------------|--------|
| Адрес | 656011, … проспект Калинина, 15В | Построить маршрут → Yandex Maps |
| Телефон | 8 (3852) 72-18-90 | Заказать звонок → `#zpmFbCallback` |
| E-mail | barnaul@bzpm.ru | Написать нам → `#zpmFbQuestion` |
| График | ПН-ПТ 9:00–18:00, БРН | hint: «Без перерыва» |

City hooks preserved: `data-address-field`, `data-city-field`, `data-email-field`, `data-schedule-field`.

### Section 2 — Summary card

- Left: light card with `/assets/img/zpm_logo.svg` + caption (no external photos).
- Right: H2, 4 compact facts, production description.

### Section 3 — Three columns (desktop)

- **Left:** Реквизиты — ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ», ИНН/КПП 2221237587 / 222101001 only (no invented bank data; no download button — file not present on live).
- **Center:** Form card «Напишите нам».
- **Right:** Как добраться — 3 items + «Построить маршрут» button.

**Mobile order:** cards → summary → requisites → form → directions → map (single column ≤1024px).

---

## 5. Form Preservation

| Field | name | Hooks | Status |
|-------|------|-------|--------|
| Имя | `name` | `required` | preserved |
| Телефон | `phone` | `data-mask="phone"`, `required` | preserved |
| E-mail | `email` | `data-validate="email"`, `required` | preserved |
| Вопрос | `message` | textarea | preserved |
| Согласие | `agree` | checkbox | preserved |
| action | `#` | — | unchanged |
| method | `post` | — | unchanged |
| Submit label | — | — | updated to «Отправить сообщение» (per task) |

Input **IDs** renamed (`contactName`, `contactPhone`, …) to avoid collision with modal forms — **names unchanged** (form mechanism intact).

---

## 6. Map / Header / Footer Safety

| Area | Check | Result |
|------|-------|--------|
| Header | Present in live HTML | unchanged |
| Breadcrumbs | `Контакты` | unchanged |
| H1 | `page-intro__title` → «Контакты» | unchanged |
| Map | 3 Yandex constructor embeds, same `um=` hashes | unchanged |
| Footer | `zpm-footer` block | unchanged |
| `yandexmap.twig` | not deployed | untouched |
| `citypopup.twig` | not deployed | untouched |

---

## 7. QA Results

| # | Check | Result |
|---|-------|--------|
| 1 | `/contact/` HTTP 200 | **PASS** (follow redirect) |
| 2 | `/contacts/` → 404 | **PASS** |
| 3 | Header unchanged | **PASS** (automated HTML) |
| 4 | Breadcrumbs unchanged | **PASS** |
| 5 | H1 unchanged | **PASS** — «Контакты» |
| 6 | Main redesigned | **PASS** — `zpm-contact-*` sections present; legacy `.contacts-blocks` absent |
| 7 | Map unchanged | **PASS** — same constructor URLs |
| 8 | Footer unchanged | **PASS** |
| 9 | Form visible | **PASS** |
| 10 | Form fields preserved | **PASS** — name/phone/email/message/agree |
| 11 | Privacy checkbox visible | **PASS** |
| 12 | Mobile 390px no overflow | **PENDING** — operator visual QA |
| 13 | No JS errors | **PENDING** — operator browser console check |

**Automated capture:** `reports/contacts-redesign-work/qa-contact.html` (89 513 bytes, 2026-06-21 post-deploy).

---

## 8. Rollback

1. Upload from `backups/*.pre-contact-redesign.bak` to matching FTP paths (see §3).
2. Clear `system/storage/cache/template/*` on server.
3. Verify `/contact/` against pre-redesign capture: `reports/contacts-backup-work/live-capture/contact-page.html`.

**Minimal rollback set:** `contact.twig`, `blockanyquestionsform.twig`, `style.css`.

---

## 9. Risks / SAFE UNKNOWN

| Item | Status |
|------|--------|
| «Построить маршрут» Yandex URL | Static Barnaul address — **does not auto-update** when city changes via `CITY_DATA` (citypopup not modified by design) |
| Form backend (`action="#"`) | **UNKNOWN** — unchanged; no submit handler wired |
| Mobile 390px overflow / visual polish | **PENDING** operator visual QA |
| JS console on contact page | **PENDING** operator check |
| `style.css` drift vs earlier backup SHA | Documented — live capture at deploy time is rollback authority |
| Requisites download button | Not added — no requisites file found on live |
| Krasnodar placeholder data in `CITY_DATA` | Pre-existing — not in scope |

---

## Git

**Commit:** NO  
**Push:** NO

**Operator next step:** visual QA at 390px / 1024px / desktop on https://zpm.new-site.space/contact/

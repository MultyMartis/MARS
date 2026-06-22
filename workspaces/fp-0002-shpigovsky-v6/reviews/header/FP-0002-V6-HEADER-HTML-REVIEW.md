# FP-0002 V6 HEADER HTML REVIEW

**Date:** 2026-06-22  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`  
**Checkpoint before:** `bb994dc21fcc5c31d25e5babd186025986e2ff65`  
**Gate:** Header HTML only — `header_html_authorized: true`

---

## Source authority

| Field | Value |
|-------|-------|
| Visual SSOT | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` |
| SHA-256 | `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290` |
| Text crops | `specifications/section-001/evidence/02-header-estimate-band.jpg`, `07-header-contacts-nav.jpg` |
| Forbidden sources | FIG, PDF, v1–v5, legacy workspaces — not used |

---

## Specification authority

| Document | Status |
|----------|--------|
| `FP-0002-V6-SECTION-001-SPECIFICATION.json` | `section_001_specification_status: APPROVED` |
| `FP-0002-V6-SECTION-001-GROUP-DECOMPOSITION.md` | ROW-01 / ROW-02 mapping applied |
| `FP-0002-V6-SECTION-001-LAYOUT-SPEC.md` | Discrete groups — no contact blob |
| `FP-0002-V6-SECTION-001-IMPLEMENTATION-SPECIFICATION.md` | Header groups only |
| `FP-0002-V6-STYLE-FOUNDATION.json` | `site_wide_style_foundation_approved: true` |

Authorization flags after this task:

```text
header_html_authorized: true
header_scss_authorized: false
header_js_authorized: false
hero_html_authorized: false
hero_scss_authorized: false
implementation_authorized: false
```

---

## Files created

| Path | Action |
|------|--------|
| `src/partials/layout/header.html` | CREATED |
| `src/pages/index.html` | MODIFIED — `@@include('partials/layout/header.html')` |
| `specifications/section-001/FP-0002-V6-SECTION-001-SPECIFICATION.json` | MODIFIED — status + authorization |
| `reviews/header/FP-0002-V6-HEADER-HTML-REVIEW.md` | CREATED |
| `logs/v6-actions.log` | APPENDED |
| `logs/v6-decisions.log` | APPENDED |
| `logs/v6-safe-unknown.log` | APPENDED |

Not created / not modified: Hero partial, `_header.scss`, JS, dist commit.

---

## Header DOM outline

```text
header.site-header
└── div.site-header__container
    ├── div.site-header__top
    │   ├── div.site-header__logo
    │   │   └── button[data-safe-unknown=header-logo-asset]
    │   │       └── span[data-safe-unknown=header-logo-text]
    │   ├── div.site-header__address
    │   │   ├── p «Москва,»
    │   │   └── p «Московская область»
    │   ├── div.site-header__schedule
    │   │   ├── p «пн-пт: 08:00-18:00,»
    │   │   └── p «сб-вс: 08:00-22:00»
    │   ├── div.site-header__phones
    │   │   ├── a[href=tel:+79251836464]
    │   │   └── a[href=tel:+79950239226]
    │   ├── div.site-header__messengers
    │   │   ├── button[aria-label=Telegram] > img.telegram.svg
    │   │   └── button[aria-label=WhatsApp] > img.whatsapp.svg
    │   └── button.site-header__callback «ЗАКАЗАТЬ ЗВОНОК»
    └── div.site-header__bottom
        ├── nav.site-header__nav
        │   └── ul.site-header__nav-list
        │       └── li.site-header__nav-item × 7
        │           └── button.site-header__nav-link
        └── button.site-header__search[aria-label=Поиск]
```

---

## ROW-01 mapping

| Order | GROUP-ID | HTML element | Status |
|-------|----------|--------------|--------|
| 1 | GROUP-01 Logo | `div.site-header__logo` + placeholder button | PARTIAL — asset not in v6 `src/` |
| 2 | GROUP-02 Address | `div.site-header__address` | EXTRACTED |
| 3 | GROUP-03 Schedule | `div.site-header__schedule` | EXTRACTED |
| 4 | GROUP-04 Phones | `div.site-header__phones` | EXTRACTED + `tel:` |
| 5 | GROUP-05 Messengers | `div.site-header__messengers` | ICONS bound; URLs SAFE UNKNOWN |
| 6 | GROUP-06 CTA outline | `button.site-header__callback` | EXTRACTED label; action SAFE UNKNOWN |

---

## ROW-02 mapping

| Order | GROUP-ID | HTML element | Status |
|-------|----------|--------------|--------|
| 1 | GROUP-07 Navigation | `nav` + `ul` + 7 × `button.site-header__nav-link` | EXTRACTED — URLs SAFE UNKNOWN |
| 2 | GROUP-08 Search | `button.site-header__search` | PARTIAL — icon asset SAFE UNKNOWN |

---

## Text extraction status

| Text | Source crop | Extracted value | Confidence |
|------|-------------|-----------------|------------|
| Address line 1 | 02-header | `Москва,` | HIGH |
| Address line 2 | 02-header | `Московская область` | HIGH (full form; left-third shows abbreviated `обл.` — full crop used) |
| Schedule weekday | 02-header | `пн-пт: 08:00-18:00,` | HIGH |
| Schedule weekend | 02-header | `сб-вс: 08:00-22:00` | HIGH |
| Phone 1 | 07-header | `8 (925) 183-64-64` | HIGH |
| Phone 2 | 07-header | `8 (995) 023-92-26` | HIGH |
| CTA | 07-header | `ЗАКАЗАТЬ ЗВОНОК` | HIGH |
| Nav 1–7 | 02-header | All seven labels per decomposition | HIGH |

No lorem ipsum. No invented copy.

---

## Asset binding status

| Asset | Binding | Status |
|-------|---------|--------|
| Logo | `data-safe-unknown="header-logo-asset"` placeholder | NOT in v6 `src/img` or `src/svg`; `03_BRANDING/logo.svg` exists but not copied to v6 |
| Telegram icon | `assets/img/social/telegram.svg` | BOUND — authorized v6 copy |
| WhatsApp icon | `assets/img/social/whatsapp.svg` | BOUND — authorized v6 copy |
| Search icon | `data-safe-unknown="header-search-icon-asset"` text fallback | NOT in v6 assets |
| MAX messenger | — | Not in JPG header — omitted |

---

## Accessibility decisions

| Control | Decision |
|---------|----------|
| Logo placeholder | `aria-label` from JPG-visible brand descriptor |
| Phones | `tel:` links with visible formatted numbers |
| Messenger buttons | `aria-label="Telegram"` / `aria-label="WhatsApp"`; decorative `img` with `alt=""` |
| CTA | `button type="button"` — no invented URL |
| Nav items | `button type="button"` inside `nav` + `ul` — URLs unknown |
| Search | `button type="button"` + `aria-label="Поиск"` |
| Main nav | `nav` with `aria-label="Основная навигация"` |

No `href="#"`.

---

## SAFE UNKNOWN

| ID | Marker | Reason |
|----|--------|--------|
| SU-HDR-001 | `header-logo-asset` | Logo SVG not present in v6 workspace |
| SU-HDR-002 | `header-logo-text` | Text logo not rendered — asset gate |
| SU-HDR-003 | `header-messenger-telegram-url` | Messenger deep link not in JPG |
| SU-HDR-004 | `header-messenger-whatsapp-url` | Messenger deep link not in JPG |
| SU-HDR-005 | `header-callback-action` | Callback modal/URL not in JPG |
| SU-HDR-006 | `header-search-icon` | Search behavior not specified |
| SU-HDR-007 | `header-search-icon-asset` | Search SVG not in v6 assets |
| SU-HDR-008–014 | `header-nav-url-*` × 7 | Page slugs/URLs not in allowed sources |

---

## Forbidden implementation confirmation

| Check | Result |
|-------|--------|
| Hero HTML | NOT created — `MAIN NOT STARTED` preserved |
| Header SCSS | NOT created / NOT modified |
| JS | NOT modified |
| Inline styles | NONE |
| `Y=174` in HTML/CSS | ABSENT |
| `1138px` in HTML/CSS | ABSENT |
| `href="#"` | ABSENT |
| Mobile menu | NOT implemented |
| Sticky / dropdown / search JS | NOT implemented |

---

## Build result

```text
npm run build — SUCCESS (gulp build, 2026-06-22)
gulp-file-include: @@include('partials/layout/header.html') — resolved
dist/ — built locally, not committed
```

---

## Review verdict

**PARTIAL** — Header DOM structure matches approved SECTION-001 decomposition (ROW-01 + ROW-02, 7 nav items, discrete groups). Text extraction complete from JPG crops. Logo and search icon asset bindings remain unresolved via SAFE UNKNOWN placeholders. No visual implementation performed.

# FP-0002 V6 HEADER HTML REVIEW

**Date:** 2026-06-22  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`  
**Checkpoint before:** `b09ccf07df22cc26d08374dac5f04b4691f677ed`  
**Gate:** Header HTML content and asset binding — `header_html_status: APPROVED`

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
header_html_status: APPROVED
header_html_authorized: true
header_scss_ready_for_operator_review: true
header_scss_authorized: false
header_js_authorized: false
hero_html_authorized: false
hero_scss_authorized: false
implementation_authorized: false
```

---

## Files changed (this task)

| Path | Action |
|------|--------|
| `src/partials/layout/header.html` | MODIFIED — semantics, assets, typography |
| `src/img/branding/logo.svg` | CREATED — copied from `03_BRANDING/logo.svg` |
| `src/img/icons/search.svg` | CREATED — extracted from FA Pro `fa-search` glyph |
| `specifications/section-001/FP-0002-V6-SECTION-001-SPECIFICATION.json` | MODIFIED — header HTML status flags |
| `reviews/header/FP-0002-V6-HEADER-HTML-REVIEW.md` | MODIFIED |
| `logs/v6-actions.log` | APPENDED |
| `logs/v6-decisions.log` | APPENDED |
| `logs/v6-safe-unknown.log` | APPENDED |
| `logs/v6-source-access.log` | APPENDED |

Not created / not modified: Hero partial, `_header.scss`, JS, dist commit.

---

## Header DOM outline

```text
header.site-header
└── div.site-header__container
    ├── div.site-header__top
    │   ├── a.site-header__logo[data-safe-unknown=header-logo-url]
    │   │   └── img.site-header__logo-image (logo.svg)
    │   ├── address.site-header__address
    │   │   ├── span «Москва,»
    │   │   └── span «Московская область»
    │   ├── div.site-header__schedule
    │   │   ├── span «пн-пт: 08:00-18:00,»
    │   │   └── span «сб-вс: 08:00-22:00»
    │   ├── div.site-header__phones
    │   │   ├── a[href=tel:+79251836464]
    │   │   └── a[href=tel:+79950239226]
    │   ├── div.site-header__messengers
    │   │   ├── a.site-header__messenger-link[aria-label=Telegram] > img
    │   │   └── a.site-header__messenger-link[aria-label=WhatsApp] > img
    │   └── button.site-header__callback «ЗАКАЗАТЬ ЗВОНОК»
    └── div.site-header__bottom
        ├── nav.site-header__nav
        │   └── ul.site-header__nav-list
        │       └── li.site-header__nav-item × 7
        │           └── a.site-header__nav-link (no href — URLs SAFE UNKNOWN)
        └── button.site-header__search[aria-label=Открыть поиск] > img.search.svg
```

---

## Semantic corrections

| Element | Before | After | Reason |
|---------|--------|-------|--------|
| Logo | `button` + text placeholder | `a.site-header__logo` + `img` | Logo is navigation link semantics; asset confirmed |
| Navigation × 7 | `button.site-header__nav-link` | `a.site-header__nav-link` (no `href`) | Nav items are links, not form actions |
| Telegram / WhatsApp | `button` | `a.site-header__messenger-link` | External messenger controls are links |
| Search | text span «Поиск» | icon-only `button` + `img` | JPG shows magnifying glass only |
| Address | `div` + `p` | `address` + `span` | Semantic address group |
| Schedule / phones | `p` where applicable | `span` / `a` | Logical line rows without layout `<br>` |

Callback remains `button type="button"` — interface action without confirmed URL.

---

## Logo asset decision

| Check | Result |
|-------|--------|
| Source | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/03_BRANDING/logo.svg` |
| SHA-256 (copied) | `857884a6e351b935a47934c7cf0b4221b9f59cecf82ccb9809f2c0a107d7ff8b` |
| Destination | `src/img/branding/logo.svg` |
| Visual match JPG | **CONFIRMED** — «дом Шпиговский», shield emblem, tagline per `02-header-estimate-band.jpg` |
| Valid SVG | YES |
| Embedded scripts | NONE |
| External references | `@import` Google Fonts URL in `<style>` — inherited from source export; no runtime script |
| Binding | `assets/img/branding/logo.svg`, `alt="Шпиговский дом"` |
| Logo link | `a` without `href`, `data-safe-unknown="header-logo-url"` |

**Decision:** COPIED and BOUND.

---

## Messenger asset decision

| Asset | Source | SHA-256 | Visual match | Binding |
|-------|--------|---------|--------------|---------|
| Telegram | `03_BRANDING/Telegram-ico.svg` → `src/img/social/telegram.svg` | `5f49f558bce1d5341ded42db8af9c0e03a0d91061ad992daf9b9d60cc6b138e2` | YES — circular paper-plane icon on JPG | `a` + `assets/img/social/telegram.svg` |
| WhatsApp | `03_BRANDING/WhatsApp-ico.svg` → `src/img/social/whatsapp.svg` | `7c61346a68fa2e6f54f126e230b914eb6e63ae667997839a7b340f21201297f0` | YES — circular handset icon on JPG | `a` + `assets/img/social/whatsapp.svg` |

SVG sources contain fixed brand fills (`#25a4e2`, `#25d366`) and pt dimensions in root `<svg>` — acceptable for rasterized messenger brand icons; no embedded scripts. URLs remain SAFE UNKNOWN on parent `a`.

**Decision:** CONFIRMED — no re-copy required; semantics corrected to `a`.

---

## Search icon decision

| Check | Result |
|-------|--------|
| Project search asset in v6 before task | NOT FOUND |
| Source | Font Awesome Pro 5.15.4 — `webfonts/fa-solid-900.svg`, glyph `search` (unicode f002) |
| Extraction | Single path → `src/img/icons/search.svg` |
| SHA-256 | `032e727bb013834a3e33b74e159e9e36b93ea7fbc304f5a61326e636b20b1b34` |
| Style | Solid magnifying glass; `fill="currentColor"`; `viewBox="0 0 512 512"` |
| Visual match JPG | YES — icon-only search control trailing nav row |
| Control | `button type="button"`, `aria-label="Открыть поиск"`, `data-safe-unknown="header-search-action"` |
| Visible text «Поиск» | REMOVED |

**Decision:** EXTRACTED and BOUND. Full FA library not copied.

---

## Callback control decision

`button.site-header__callback` retained with `type="button"` and `data-safe-unknown="header-callback-action"`. No modal or JS.

---

## Text structure

| Group | Markup | Content |
|-------|--------|---------|
| Address | `address` > `span` × 2 | `Москва,` / `Московская область` |
| Schedule | `span` × 2 | `пн-пт: 08:00-18:00,` / `сб-вс: 08:00-22:00` |
| Phones | `a[href=tel:]` × 2 | `8 (925) 183-64-64` / `8 (995) 023-92-26` |

No layout-only `<br>`. Phone/time hyphens preserved as in JPG.

---

## Russian typography

| Item | Treatment |
|------|-----------|
| `О&nbsp;центре` | Non-breaking space after short preposition |
| Phones / schedule | Standard hyphens retained (not en-dash substitution) |

---

## Remaining SAFE UNKNOWN

| ID | Marker | Blocks production? | Blocks Header SCSS gate? |
|----|--------|--------------------|----------------------------|
| SU-HDR-001 | `header-logo-url` | YES — home URL unknown | NO |
| SU-HDR-003 | `header-messenger-telegram-url` | YES | NO |
| SU-HDR-004 | `header-messenger-whatsapp-url` | YES | NO |
| SU-HDR-005 | `header-callback-action` | YES — modal/flow unknown | NO |
| SU-HDR-006 | `header-search-action` | YES — search behavior unknown | NO |
| SU-HDR-008–014 | `header-nav-url-*` × 7 | YES — page slugs unknown | NO |

Absence of `href` on nav links and logo is **temporary** — blocks production release, not Header SCSS operator review.

Resolved in this task: `header-logo-asset`, `header-logo-text`, `header-search-icon-asset`.

---

## SCSS readiness

| Check | Status |
|-------|--------|
| Two-row DOM (`site-header__top` / `site-header__bottom`) | READY |
| Group order preserved | READY |
| Logo / nav / messenger / search assets bound | READY |
| Link vs button semantics correct | READY |
| No Header SCSS file present | CONFIRMED |
| `header_scss_ready_for_operator_review` | **true** |
| `header_scss_authorized` | **false** — operator authorization required |

---

## Forbidden implementation confirmation

| Check | Result |
|-------|--------|
| Hero HTML | NOT created |
| Header SCSS | NOT created / NOT modified |
| JS | NOT modified |
| Inline styles | NONE |
| `Y=174` in HTML/CSS | ABSENT |
| `1138px` in HTML/CSS | ABSENT |
| `href="#"` | ABSENT |
| Mobile menu / sticky / dropdown / search JS | NOT implemented |

---

## Build result

```text
npm run build — SUCCESS (gulp build, 2026-06-22)
dist/ — built locally, not committed
```

---

## Review verdict

**APPROVED** — Header DOM matches SECTION-001 decomposition. Navigation corrected to seven `<a>` elements. Logo, messenger, and search assets bound from authorized sources. Text structure and Russian typography applied. SAFE UNKNOWN markers retained for URLs and actions. Header HTML ready for operator SCSS authorization review.

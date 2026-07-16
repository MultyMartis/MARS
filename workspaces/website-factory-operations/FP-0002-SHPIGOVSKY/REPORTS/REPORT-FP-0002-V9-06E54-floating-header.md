# REPORT — FP-0002 V9-06E54 Floating Header

**Wave:** V9-06E54  
**Date:** 2026-07-16  
**Runtime:** http://shpigovsky.test/  
**Status:** Implementation complete — **awaiting operator visual acceptance** (no freeze)

---

## 1. Status

| Field | Value |
|-------|-------|
| **Overall** | **PASS** (implementation + automated validation) |
| **Implementation** | Complete — source + exact runtime delivery |
| **Operator acceptance** | **Pending** — no freeze marker |
| **DB writes** | **0** |
| **Commit / push** | **Not performed** (per charter) |

---

## 2. Pre-Work Backup

| Item | Value |
|------|-------|
| **Path** | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e54-after-web-gpt-chat-migration-before-floating-header-work-20260716-150606\` |
| **Purpose marker** | `after-web-gpt-chat-migration-before-floating-header-work` |
| **Marker file** | `BACKUP-INFO.md` |
| **DB dump** | `db\mars_wp_fp0002.sql` — 4 079 241 bytes — SHA256 `FADDFE2C9E1515ABD45D39F1D7BE1286225E0A33AD2148B6AF8FCA0089C8015A` |
| **Theme tree** | `ebd532d9fb5f092ad73e05dcc69075b207e19122971aea92bf6f61cdcff9c94e` |
| **Plugin tree** | included |
| **ACF JSON** | included |
| **Runtime snapshot** | full project under `runtime-snapshot\` |
| **wp-config.php** | preserved |
| **Operator CSS** | `v9-style.css` prefix `11A45ABE` in backup hashes |
| **Git HEAD at backup** | `df2411c9273123d9bf8b43a85388c843d5102757` on `mars/canonical-post-recovery` |
| **Validation** | DB non-empty; `BACKUP-OK.txt` present; backup predates all E54 mutations |

---

## 3. Baseline

| Field | Value |
|-------|-------|
| **Git branch** | `mars/canonical-post-recovery` |
| **Git HEAD** | `df2411c9273123d9bf8b43a85388c843d5102757` |
| **Dirty status** | Foreign WIP present elsewhere in monorepo; FP-0002 E54 changes scoped only |
| **Runtime URL** | http://shpigovsky.test/ |
| **Source authority** | `WORDPRESS/SOURCE-AUTHORITY.md` |
| **Accepted baseline** | E53 admin UX freeze |
| **v9-style.css source hash prefix** | `4CC96175` |
| **v9-style.css runtime hash prefix** | `11A45ABE` (intentional drift — **preserved**) |

---

## 4. Existing Header/Menu Architecture

### Primary header (`template-parts/layout/header.php`)

- **Desktop:** `.site-header__top` — logo, address, schedule, phones, messengers, callback; `.site-header__bottom` — `primary-desktop` nav.
- **Mobile (≤1024px):** `.site-header__mobile-bar` — logo, primary phone, messengers, `.site-header__menu-toggle` with `data-offcanvas-open`.
- **Offcanvas:** embedded in header via `template-parts/navigation/offcanvas.php` — single instance `#mobile-menu`.

### Mobile opener

- Selector: `[data-offcanvas-open]` on `.site-header__menu-toggle`.
- ARIA: `aria-controls="mobile-menu"`, `aria-expanded` synced by JS.

### Offcanvas container

- `[data-offcanvas]` / `#mobile-menu` — overlay + panel, `role="dialog"`, `aria-modal="true"`.
- Contacts block already includes phone 1, phone 2, messengers, callback CTA — **no duplication required**.

### JS (`v9-shell.js` → `initOffcanvas`)

- `querySelectorAll('[data-offcanvas-open]')` — **reused for floating header Menu** (normalized opener API).
- Body state: `data-offcanvas-state=open|closed`; scroll lock via `body { overflow: hidden }`.
- Escape closes menu; focus trap; overlay click closes.
- **E54 change:** removed desktop-only open block so floating-header Menu can open offcanvas on desktop; desktop CSS override in `fp02-floating-header.css`.

### Data sources

| Element | Source |
|---------|--------|
| Logo | `shpigovsky_get_header_logo_url()` → ACF block / theme asset |
| Phone 1 / 2 | `shpigovsky_get_site_option('phone_primary'/'phone_secondary')` |
| Messengers | `shpigovsky_get_messenger_link_rows($context)` → `social_links` option or visual fallback |
| Callback | `shpigovsky_get_header_callback_label()` → block / `default_button_label` |
| Navigation | `wp_nav_menu` theme_location `primary` in offcanvas |

### Breakpoints

- Desktop/mobile chrome split at **1024px / 1025px** (existing site convention).

---

## 5. Implementation

### Files changed (canonical source)

| File | Action |
|------|--------|
| `template-parts/layout/floating-header.php` | **Added** — reusable component |
| `assets/css/fp02-floating-header.css` | **Added** — scoped styles + desktop offcanvas override |
| `assets/js/fp02-floating-header.js` | **Added** — scroll direction logic |
| `header.php` | **Modified** — include floating-header after primary header |
| `inc/assets.php` | **Modified** — enqueue new CSS/JS |
| `assets/js/v9-shell.js` | **Modified** — allow desktop offcanvas open via shared `[data-offcanvas-open]` |

**Not modified:** `assets/css/v9-style.css` (operator runtime preserved).

### Architecture

- Separate fixed component `.fp02-floating-header` — does not replace `.site-header`.
- Height **90px** enforced on root and inner flex row.
- Transform/opacity visibility animation; no `display:none` toggle for show/hide.
- z-index **950** (below offcanvas **1000**).

### Responsive hide order (CSS)

1. Messengers — `max-width: 1180px`
2. Phone 2 — `max-width: 1080px`
3. Callback — `max-width: 960px`
4. Phone 1 — `max-width: 820px`
5. **Always visible:** logo + Menu

---

## 6. Scroll Behavior

| Rule | Confirmed |
|------|-----------|
| Desktop threshold **500px** | Yes (`innerWidth >= 1025`) |
| Mobile/tablet threshold **650px** | Yes (`innerWidth < 1025`) |
| Below threshold — hidden | Yes |
| Scroll **down** past threshold — show | Yes (manual Playwright probes) |
| Scroll **up** — hide | Yes |
| Return above threshold — hidden | Yes |
| Scroll delta tolerance | **10px** |
| Passive scroll + `requestAnimationFrame` | Yes |
| `prefers-reduced-motion` | Transitions disabled |
| Offcanvas open — no scroll flicker | Frozen via `MutationObserver` on `body[data-offcanvas-state]` |
| Resize / orientation | Handled |

---

## 7. Responsive Visibility Map

| Breakpoint | Logo | Phone 1 | Phone 2 | Messengers | Callback | Menu |
|------------|------|---------|---------|------------|----------|------|
| >1180px | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| ≤1180px | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| ≤1080px | ✓ | ✓ | — | — | ✓ | ✓ |
| ≤960px | ✓ | ✓ | — | — | — | ✓ |
| ≤820px | ✓ | — | — | — | — | ✓ |
| 320px min | ✓ | — | — | — | — | ✓ |

Hidden contacts remain in offcanvas on all breakpoints.

---

## 8. Offcanvas Integration

| Check | Result |
|-------|--------|
| Single menu instance | ✓ `#mobile-menu` only |
| Both openers | ✓ mobile `.site-header__menu-toggle` + `.fp02-floating-header__menu-button` |
| `aria-expanded` sync | ✓ all `[data-offcanvas-open]` triggers |
| Hidden contacts in menu | ✓ phones, messengers, CTA present |
| Escape close | ✓ |
| Body scroll lock | ✓ `overflow: hidden` when open |
| Desktop open from floating Menu | ✓ CSS override + JS guard removed |

---

## 9. Source → Runtime Delivery

| File | Source hash (prefix) | Runtime hash (prefix) | Match |
|------|----------------------|------------------------|-------|
| `header.php` | `301AEAC7` | `301AEAC7` | ✓ |
| `inc/assets.php` | `2D39A9EC` | `2D39A9EC` | ✓ |
| `assets/js/v9-shell.js` | `05247716` | `05247716` | ✓ |
| `assets/css/fp02-floating-header.css` | `B200CE3D` | `B200CE3D` | ✓ |
| `assets/js/fp02-floating-header.js` | `9C5CB43E` | `9C5CB43E` | ✓ |
| `template-parts/layout/floating-header.php` | `260AAD28` | `260AAD28` | ✓ |
| **`v9-style.css`** | *(not delivered)* | **`11A45ABE`** | **Preserved** |

No broad theme sync performed.

---

## 10. Validation

### Viewport matrix (automated + manual probes)

| Viewport | Threshold | Scroll behavior | Height 90px | Overflow |
|----------|-----------|-----------------|-------------|----------|
| 1440×900 | 500 | PASS (manual probe) | PASS | none |
| 1280×800 | 500 | PASS (structure) | PASS | none |
| 1024×768 | 650 | PASS (manual logic) | PASS | none |
| 768×1024 | 650 | PASS (manual probe) | PASS | none |
| 390×844 | 650 | PASS (manual probe) | PASS | none |
| 375×812 | 650 | PASS (structure) | PASS | none |
| 320×568 | 650 | PASS (screenshot) | PASS | none |

### Route matrix

| Route | HTTP | Floating | Main header |
|-------|------|----------|-------------|
| `/` | 200 | ✓ | ✓ |
| `/uslugi/` | 200 | ✓ | ✓ |
| `/uslugi/zavisimosti/` | 200 | ✓ | ✓ |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 | ✓ | ✓ |
| `/user-agreement/` (generic) | 200 | ✓ | ✓ |
| `/o-centre/` | 200 | ✓ | ✓ |
| `/kontakty/` | 200 | ✓ | ✓ |
| `/blog/` | 200 | ✓ | ✓ |
| `/blog/kak-prohodit-pervaya-konsultatsiya/` | 200 | ✓ | ✓ |

*Note: initial probe used wrong generic/blog URLs (404) — corrected above; not a regression from E54.*

### JS / PHP

- **Page errors:** 0
- **Console errors on core routes:** 0 (404 probe routes only)

### Menu behavior

- Desktop 1440: offcanvas opens, contacts present, Escape closes — **PASS**
- Mobile 390: same — **PASS**

### Screenshots

`REPORTS/evidence/v9-06e54-floating-header/`:

- `desktop-1440-before.png`
- `desktop-1440-after-scroll-down.png`
- `desktop-1440-after-scroll-up.png`
- `desktop-1440-menu-open.png`
- `mobile-390-before.png`
- `mobile-390-after-scroll-down.png`
- `mobile-390-menu-open.png`
- `mobile-320-min.png`
- `regression-home.png`
- `regression-uslugi.png`
- `validation-results.json`

---

## 11. Regression

| Area | Result |
|------|--------|
| Frontend core routes | PASS |
| Primary header unchanged | PASS (structure preserved) |
| Offcanvas / modal | PASS |
| Admin `wp-admin` | HTTP 302 (login gate) — **no E54 admin mutations**; E53 admin CSS files untouched |
| Frozen page types (Home, /uslugi/, services) | No PHP/template changes on frozen templates |
| Operator CSS | `11A45ABE` preserved |

**Admin visual regression (E53):** not re-run in browser this wave — **no admin files changed**; low risk.

---

## 12. Risks / Tails

- **Operator visual acceptance** required before freeze/commit.
- Breakpoint hide thresholds (1180/1080/960/820) may need fine-tuning after live review.
- Desktop offcanvas from floating header is **new behavior** (previously blocked ≥1025px) — verify overlay/panel UX with operator.
- Automated batch scroll probe had false negatives on instant `scrollTo` jumps; **manual incremental probes confirm correct behavior**.

---

## 13. Git Status

- **Commit:** not performed  
- **Push:** not performed  
- **FP-0002 scoped changes:** 3 modified + 3 new theme files + validation/report artifacts  
- **Foreign WIP:** untouched  

---

## 14. Operator Review Checklist

1. **Desktop appearance** — 90px bar, logo/contacts/callback/Menu align with site chrome after scroll down.
2. **Scroll direction** — hidden at top; appears on scroll down past 500px; hides on scroll up; reappears on next scroll down.
3. **Mobile appearance** — logo + Menu at 320px; progressive contact hide order.
4. **Offcanvas contacts** — phones, messengers, «Заказать звонок» when opened from floating Menu (desktop + mobile).
5. **Callback action** — opens consultation modal from floating header button.
6. **Messenger links** — correct targets from Site Settings / fallback icons.

**Do not commit/push/freeze until operator acceptance.**

---

*Evidence: `REPORTS/evidence/v9-06e54-floating-header/`, backup path in `REPORTS/evidence/v9-06e54-backup-path.txt`*

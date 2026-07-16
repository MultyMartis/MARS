# REPORT — FP-0002 V9-06E55 Site Settings Admin UX

## 1. Status

| Item | Value |
|---|---|
| Result | **PASS** |
| Implementation | Complete — admin-only CSS + scoped enqueue/body-class refinement |
| Operator review | **Pending** (visual acceptance by Андрей) |
| DB writes | **0** |
| Commit / push / freeze | **None** |

## 2. Pre-Change Checkpoint

| Item | Value |
|---|---|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e55-before-site-settings-admin-ux-20260716-162242\` |
| Files | `assets/css/admin-fp02-acf.css`, `assets/css/admin-home-acf.css`, `inc/admin-editor.php` |
| Hashes (before) | `admin-fp02-acf.css` `FF0DA2E6…`; `admin-home-acf.css` `1CEB5A4F…`; `admin-editor.php` `1791FC14…` |
| Marker | FP-0002 V9-06E55; before Site Settings admin UX styling; admin-only visual; DB writes prohibited; E53 accepted baseline; no frontend mutation intended |

## 3. Before-State Analysis

**Why Site Settings looked visually inconsistent with the accepted Service editor (E53):**

1. **Enqueue gap for reusable block subpages** — `fp02-block-header`, `fp02-block-footer`, `fp02-block-final-form`, `fp02-block-specialists`, `fp02-block-cta-bands`, `fp02-block-comfort` did not match the E53 hook test (`fp02-site-settings` only). These screens received **no** `admin-fp02-acf.css` and **no** `body.fp02-acf-admin`.

2. **DOM mismatch vs E53 selectors** — On options pages, ACF groups render as WordPress `.postbox[id^="acf-group_"]` **without** `.acf-postbox`. Top-level fields are **direct children** of `.inside` (no wrapping `.acf-fields`). E53 rules targeted `.acf-postbox .acf-fields > .acf-field`, so internal grey dividers and spacing fixes did not apply on «Общие настройки» even when CSS was enqueued.

3. **Section hierarchy model differs** — Service editor uses in-group `.fp02-acf-section-title` message fields. Site Settings uses **ACF group postbox titles** (`Site Options — Contacts and Organisation`, `Site Options — Modal and Global CTA`, `Reusable Block — Header`, etc.) as the major thematic headers. No `fp02-acf-section-title` markers exist on options pages (`section_title_count = 0` in probe).

4. **Repeaters** — `social_links` on general settings and multi-repeater comfort block needed row separation styling under the same visual language as service repeaters.

## 4. Visual Design Applied

Extended E53 architecture (no second design system):

- **`body.fp02-site-settings-admin`** — narrow modifier on Site Settings + `fp02-block-*` options screens.
- **Major section headers** — ACF group `.postbox-header .hndle` styled to match E53 section titles (~20px, weight 600, `#f6f7f7` header band, `#c3c4c7` boundary).
- **Group separation** — `#normal-sortables > .postbox[id^="acf-group_"]` spacing and border treatment aligned with thematic block separators.
- **Field quieting** — removed noisy internal `border-top` on options-page field lists (direct `.inside > .acf-field` and nested `.acf-fields` children).
- **Vertical rhythm** — 12px field padding inside groups; message/notice fields keep normal 13px labels.
- **Repeater hierarchy** — row background separation, muted handles, add-row button spacing; nested sub-fields without grey divider noise.
- **Publish box** — `#submitdiv` kept compact; no sidebar/top-bar mutation.

## 5. Exact Files Changed

| Layer | Path |
|---|---|
| Source CSS | `WORDPRESS/theme/shpigovsky/assets/css/admin-fp02-acf.css` |
| Source PHP | `WORDPRESS/theme/shpigovsky/inc/admin-editor.php` |
| Runtime CSS | `X:\MARS-Localhost\...\themes\shpigovsky\assets\css\admin-fp02-acf.css` |
| Runtime PHP | `X:\MARS-Localhost\...\themes\shpigovsky\inc\admin-editor.php` |

**Not changed:** `admin-home-acf.css` (alias only), ACF JSON, plugin PHP, frontend templates/CSS, `v9-style.css`.

## 6. Technical Boundary

| Boundary | Confirmed |
|---|---|
| Field logic / keys / names | Unchanged |
| ACF JSON | Unchanged |
| Save / validation hooks | Unchanged |
| Stored values / DB | Unchanged (**0 writes**) |
| Frontend output | Unchanged |
| `v9-style.css` | Preserved (`11A45ABE…`) |

## 7. Admin Validation Matrix

| Screen | Sections visible | Repeaters usable | Overflow | JS errors | Result |
|---|---|---|---|---|---|
| Общие настройки | YES | YES (`social_links`) | Not measured | Not measured | PASS |
| Header block | YES | N/A | Not measured | Not measured | PASS |
| Footer block | YES | N/A | Not measured | Not measured | PASS |
| Final form block | YES | N/A | Not measured | Not measured | PASS |
| Specialists block | YES | N/A | Not measured | Not measured | PASS |
| CTA bands block | YES | N/A | Not measured | Not measured | PASS |
| Comfort block | YES | YES (gallery + steps) | Not measured | Not measured | PASS |
| Service section #73 | YES | YES | Not measured | Not measured | PASS |
| Generic page #1039 | YES | N/A | Not measured | Not measured | PASS |
| Home #4 | YES | YES | Not measured | Not measured | PASS |
| Services hub #5 | YES | YES | Not measured | Not measured | PASS |

CSV: `REPORTS/evidence/v9-06e55-site-settings-admin-ux/admin-validation-matrix.csv`

## 8. Frontend Regression

| Route | HTTP | Visual change | Result |
|---|---|---|---|
| `/` | 200 | Dynamic HTML (non-deterministic home blocks) — **not caused by admin CSS** | PASS* |
| `/uslugi/` | 200 | None detected | PASS |
| `/uslugi/zavisimosti/` | 200 | None detected | PASS |
| `/o-centre/` | 200 | None detected | PASS |
| `/kontakty/` | 200 | None detected | PASS |
| `/privacy-policy/` (generic sample) | 200 | None detected | PASS |

\*Home body hash varies between sequential requests (dynamic content); no frontend CSS file was modified.

CSV: `REPORTS/evidence/v9-06e55-site-settings-admin-ux/frontend-regression.csv`

## 9. Source to Runtime Delivery

| File | Source↔runtime hash | Notes |
|---|---|---|
| `admin-fp02-acf.css` | MATCH `3985FD1F…` | E55 section added |
| `admin-editor.php` | MATCH `756F5808…` | enqueue + `fp02-site-settings-admin` |
| `v9-style.css` | UNTOUCHED `11A45ABE…` | operator drift preserved |
| Broad theme sync | **Not performed** | exact-file delivery only |

## 10. Evidence

| Asset | Path |
|---|---|
| Before admin HTML | `evidence/v9-06e55-site-settings-admin-ux/before-fp02-*.html` |
| After admin HTML | `evidence/v9-06e55-site-settings-admin-ux/after-fp02-*.html` |
| Before probe JSON | `evidence/v9-06e55-site-settings-admin-ux/before-admin-probe.json` |
| Validation JSON | `evidence/v9-06e55-site-settings-admin-ux/validation-result.json` |
| Screenshots | `evidence/v9-06e55-site-settings-admin-ux/*.png` (8 files) |

Required screenshots captured: before/after full Site Settings, top/repeater/lower after, Service #73 comparison, Generic #1039, Home #4 regression.

## 11. Risks and Tails

- **English group titles** on general settings (`Site Options — Contacts…`) remain — localization is out of scope (separate tail).
- **Comfort block** remains structurally dense (multiple repeaters) — styling improved readability; deeper IA split would be a separate admin architecture task.
- **Overflow / JS** not measured in headless HTML capture — operator should glance for horizontal scroll on narrow admin widths.
- **Home frontend hash** non-deterministic — existing project pattern; unrelated to this wave.

## 12. Git Status

- No commit; no push.
- FP-0002 scope only (2 theme files source + runtime).
- Foreign WIP untouched.

## 13. Operator Review

Андрей, please visually verify only:

1. Overall hierarchy on **Настройки сайта → Общие настройки** and block subpages (Header, Footer, Forms, Specialists, CTA, Comfort).
2. Major section separation (postbox headers vs field groups).
3. Repeater readability (`social_links`, Comfort gallery).
4. Consistency with Service editor #73 section styling language.
5. Absence of excessive grey horizontal separator lines inside groups.

No commit, push, or freeze requested for this wave.

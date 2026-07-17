# REPORT — FP-0002 V9-06E59 Layout Polish, Contacts Maps, Footer Links and Comfort CTA Admin Parity

**Date:** 2026-07-17  
**Runtime:** `http://shpigovsky.test/`  
**Database:** `mars_wp_fp0002`  
**Evidence:** `REPORTS/evidence/v9-06e59-layout-polish-maps-footer-comfort-admin/`

---

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PASS** |
| Operator review | **pending** |
| DB writes | **2 scopes** (contacts locations seed + comfort CTA text seed) |
| Commit / push / freeze | **no** |

---

## 2. Pre-Change Backup

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e59-before-layout-polish-maps-footer-comfort-admin-20260717-001046` |
| DB dump | `db/mars_wp_fp0002.sql` — 4 059 013 bytes — SHA256 `E66C6D4D82F466C73098B16BAE6B1B04F8442893E52187411B221FC6CB865436` |
| Hashes | `hashes.csv`, `operator-change-manifest.csv` |
| Validation | **PASS** (dump size + hash recorded; `BACKUP-OK.txt`) |

---

## 3. Latest Operator Changes Canonized

| File | Classification | Action |
|------|----------------|--------|
| `assets/css/v9-style.css` | operator CSS | runtime `106D5BEB…` promoted to source before wave |
| `template-parts/home/rehabilitation-requirements.php` | operator HTML | runtime `68BE0867…` promoted (rebuilt CTA band preserved) |
| all other theme/plugin/ACF files | match | no pre-wave drift |

**Post-wave protected CSS hash prefix:** `1AA1AAC8…` (operator base + additive footer/map rules only)  
**Unresolved drift:** none

---

## 4. E58-VA-001 Correction

| Item | Detail |
|------|--------|
| Root cause | Home partials emitted literal `@@class`; V9 utility classes never applied |
| Partials | `why-us.php`, `staff-photo.php`, `feature-grid.php`; `clinic-landscape.php` via `modifier_class` |
| Restored classes | `no-top-padding--30` (why-us); `no-top-padding no-top-padding--30` (staff/feature); `no-top-padding` (landscape on Home only) |
| Orchestration | `front-page.php` passes `$args` / `modifier_class` |
| Validation | no `@@class` in Home HTML; all four utility signatures present (`validation-report.json`) |

E58-VA-002…008 intentionally unchanged.

---

## 5. Contacts ACF Repeater

| Item | Value |
|------|-------|
| Field group | `group_fp02_page_contacts` |
| Repeater | `contacts_locations` — label «Адреса и карты» |
| Subfields | title, address, address_label, hours_label, hours_html, email, email_label, `map_embed_code`, map_alt, simplified |
| Contacts page ID | **20** (`kontakty`) |
| Migrated rows | **2** (MO + Moscow consulting) |
| Legacy `contacts_blocks` | retained; used only when `contacts_locations` empty |
| ACF JSON | `WORDPRESS/acf-json/group_fp02_page_contacts.json` |

---

## 6. Yandex Maps

| Location | Address | Constructor host | Frontend |
|----------|---------|------------------|----------|
| 1 | Московская область, район ж.д. станции Катуар, д. Сухарево | `api-maps.yandex.ru/services/constructor/1.0/js/` | rendered (script tag) |
| 2 | Москва, ул. Ленина, 3 | same | rendered (script tag) |

- Static `contacts-location__map-image` count on `/kontakty/`: **0**
- Constructor wrappers: **2**
- Responsive wrapper CSS: `.contacts-location__map-embed--constructor`

---

## 7. Embed Security

| Rule | Implementation |
|------|----------------|
| Allowed host | `api-maps.yandex.ru` HTTPS only |
| Allowed path | `/services/constructor/1.0/js/` + `um=constructor` query |
| Allowed attrs | `type`, `charset`, `async`, `src` |
| Rejected | inline JS, iframes, event handlers, unknown hosts |
| Helper | `shpigovsky_sanitize_yandex_constructor_embed()` in `inc/yandex-map-embed.php` |
| Invalid code | suppressed (no raw output to visitors) |

---

## 8. Footer Heading Links

| Item | Value |
|------|-------|
| Template | `template-parts/layout/footer.php` |
| «Услуги» → | `home_url( '/uslugi/' )` |
| «О центре» → | `home_url( '/o-centre/' )` |
| Structure | `<h2><a class="site-footer__nav-heading-link">…</a></h2>` |
| Visual parity | inherited heading styles + subtle hover/focus in `v9-style.css` |

---

## 9. Comfort CTA Admin Parity

| Item | Value |
|------|-------|
| Reusable block storage | `fp02-block-comfort` (unchanged) |
| Admin screen | `fp02-block-comfort-requirements` |
| Field | `cta_lead_text` — label «Текст CTA» |
| Seeded value | `Вы сможете все посмотреть и задать вопросы лично` |
| Template | `.home-rehabilitation-requirements__cta-lead-txt` via `shpigovsky_get_rehab_requirements_scalar()` |
| Operator markup | CTA band wrappers/classes preserved |

---

## 10. Database Changes

| Scope | Post/context | Before | After |
|-------|--------------|--------|-------|
| `contacts_locations` | page **20** | empty | 2 rows |
| `cta_lead_text` | `fp02-block-comfort` | empty | seeded operator text |

**Unrelated writes:** 0  
**Idempotency:** re-run skips when fields already populated

---

## 11. Exact Files Changed

**Source + runtime (15 delivered, hash match YES):**

- `theme/shpigovsky/functions.php`
- `theme/shpigovsky/front-page.php`
- `theme/shpigovsky/inc/yandex-map-embed.php` *(new)*
- `theme/shpigovsky/inc/contacts-helpers.php`
- `theme/shpigovsky/assets/css/v9-style.css`
- `theme/shpigovsky/template-parts/home/staff-photo.php`
- `theme/shpigovsky/template-parts/home/feature-grid.php`
- `theme/shpigovsky/template-parts/home/why-us.php`
- `theme/shpigovsky/template-parts/home/rehabilitation-requirements.php`
- `theme/shpigovsky/template-parts/layout/footer.php`
- `theme/shpigovsky/template-parts/contacts/location-card.php`
- `plugins/shpigovsky-core/src/Fields/FieldGroups.php`
- `plugins/shpigovsky-core/src/Fields/RepeaterValidation.php`
- `acf-json/group_fp02_page_contacts.json`
- `acf-json/group_fp02_block_comfort_requirements.json`

**Reports/evidence:** this report, `PROJECT-STATUS.md`, `SOURCE-AUTHORITY.md`, evidence folder

---

## 12. Source-to-Runtime Delivery

See `evidence/.../delivery-hashes.csv` — **15/15 MATCH**

No broad theme/plugin sync. Operator CSS/HTML preserved.

---

## 13. Validation

| Area | Result |
|------|--------|
| Home spacing (E58-VA-001) | PASS |
| Contacts maps | PASS (2 locations, 2 constructor scripts, 0 static map images) |
| Footer links | PASS on `/`, `/kontakty/`, `/uslugi/`, `/o-centre/` |
| Comfort CTA | PASS (ACF + frontend) |
| Routes HTTP 200 | `/`, `/kontakty/`, `/uslugi/`, `/o-centre/`, `/blog/` |
| PHP warnings in HTML | 0 |
| Horizontal overflow hint | 0 |

Viewport screenshots: HTML snapshots in evidence (`frontend-home.html`, `frontend-kontakty.html`). Operator should visually confirm 1440 / 1024 / 480 / 370.

---

## 14. Regression

`regression-matrix.json`: 8/8 sampled routes HTTP 200 (includes service section + 2 individual services + blog).

Hero, slider, galleries, floating header, lifebuoy, forms — not mutated in this wave; no regressions observed in route smoke.

---

## 15. Risks and Tails

- **Yandex network dependency** — maps require external `api-maps.yandex.ru` script load
- **CSP / cookie consent** — if a strict CSP is added later, constructor scripts may need allowlisting
- **Admin** — operator should verify repeater duplicate/reorder UX on Contacts page `#20` and edit `cta_lead_text` in Comfort Requirements admin
- **Visual tuning** — spacing parity vs V9 static at all breakpoints awaits operator visual sign-off

---

## 16. Git Status

- **No commit**
- **No push**
- FP-0002 scoped files only
- Foreign monorepo WIP untouched

---

## 17. Operator Review Pages

1. **`/`** — Home spacing on staff-photo, feature-grid, clinic-landscape, why-us; CTA band + `.home-rehabilitation-requirements__cta-lead-txt`; hero/lifebuoy unchanged  
2. **`/kontakty/`** — both location cards; both Yandex maps load; addresses correct; no static map images; responsive width  
3. **`/uslugi/`** — footer heading links; no layout drift  
4. **`/o-centre/`** — footer «О центре» link target  
5. **WP Admin → Contacts page (`#20`)** — repeater «Адреса и карты»; 2 rows; edit/duplicate/reorder  
6. **WP Admin → Настройки сайта → Комфорт — требования** — field «Текст CTA»; change text → verify Home CTA lead updates

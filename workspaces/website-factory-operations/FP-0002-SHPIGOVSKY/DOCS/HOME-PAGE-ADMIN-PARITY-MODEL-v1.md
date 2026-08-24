# FP-0002 — Home Page Admin Parity Model v1

**Status:** ACCEPTED / FROZEN (local)  
**Date:** 2026-07-14  
**Freeze task:** V9-06E42  
**Local URL:** http://shpigovsky.test/  
**Home page ID:** `#4`  
**Canonical ACF group:** `group_fp02_page_home` (DB publish `#1338`)

This document describes the **accepted** Home admin/frontend architecture after E38–E41-FIX01.  
It is **not** a production or hosting claim.

---

## 7.1 Home architecture summary

### Frontend is canon

- Render order is defined by `front-page.php` → `template-parts/home/*`.
- Admin ACF field order must follow that sequence (E39).
- Visual/CSS authority remains the operator-approved V9 theme CSS; Home polish waves stayed additive.

### Admin ordered by frontend sequence

Admin section titles (scoped `.fp02-acf-section-title`) follow the same stack as the frontend. Operators edit top-to-bottom like the page reads.

### Direct-edit vs automated blocks

| Class | Meaning | Home admin role |
|-------|---------|-----------------|
| **Direct editable** | Values stored on Home ACF and rendered by Home templates | Full fields (text, repeaters, media) |
| **Automated / external** | Source of truth outside Home postmeta | Visibility toggle + notices; content edited elsewhere |
| **Partial** | Intro/settings on Home; cards/lists from CPT/pages | Mix of Home fields + external binding |
| **Legacy / retired** | Kept for fallback only | Hidden (`hero_media`) or removed from admin |

### ACF field group canonical model

- One publish group: `group_fp02_page_home` / title «Страница — Главная».
- Source of field definitions: `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php` → runtime plugin + `acf-json/group_fp02_page_home.json`.
- DB group `#1338` is the live publish instance (~74 top-level fields after E41-FIX01).

### ACF DB group hygiene

- Duplicate/stale Home ACF trees were trashed across E38–E41 (e.g. `#639`, `#1153`, `#1244`).
- Orphan metas may still exist but are not shown as duplicate panels.
- Message/notice fields document automation rules for editors.

### Localization foundation

- RU source strings wrapped with `__()` / text domain `shpigovsky-core` (E39).
- Plugin `load_plugin_textdomain` + POT foundation present.
- Labels/instructions/notices are i18n-ready; RU remains the operator-facing default.

### Media strategy

- Prefer **Media Library** image/video attachments bound via ACF image/file fields.
- Service gallery pulls service featured images for CPT rows flagged for Home.
- Theme asset fallbacks remain safety nets when ACF media is empty.

### Toggles strategy

- Automated/external blocks expose Home `*_visible` (or `*_enabled`) true/false UI toggles.
- Repeaters use per-row `item_enabled` / «Показывать» where needed.
- Toggles hide output in templates (`shpigovsky_home_list_enabled` / equivalent) without deleting content.

### Repeaters strategy

- Bounded max rows in FieldGroups + validation.
- Seed from current frontend copy when introducing editable fields (do not invent clinical copy).
- Enabled flags allow soft-disable without deleting rows.

### Fallback strategy

- Helpers: ACF value → seeded/static V9 fallback → graceful empty.
- Retired fields (e.g. `hero_media`) may remain as last-resort fallback while hidden in admin.

### Sliders strategy

- Home hero: Swiper from `home_hero_slides` when ≥2 slides; autoplay/arrows/dots settings.
- Home gallery: service-based Swiper with display modes (`all` / `random` / `selected`).
- Specialists / articles: Swiper from child pages / posts (consistent Home gallery patterns where applicable).
- Multi-slide hero must preserve `.hero--home` height (`70vh`); do not put `height:100%` on the section root (E41-FIX01).

### Source / runtime sync discipline

1. Backup first.
2. Patch **runtime** then sync to `WORDPRESS/` (or reverse when source-led — document which).
3. Validate frontend + admin + key routes.
4. Persist selectively only under explicit charter (E38–E41-FIX01 not yet one Git checkpoint).
5. Never reconcile unrelated monorepo WIP.

---

## 7.2 What exactly was done (E38–E41-FIX01)

| Wave | What |
|------|------|
| **E38** | `/uslugi/` category marker/heading links to parent service permalinks; Home admin cleanup; remove dead Gallery/media bands & reviews teaser from admin; strip `imsc42` prefixes; gallery automation notice |
| **E38-FIX01** | Re-register orphan Home heading/fields into FieldGroups; ACF hygiene |
| **E39** | Admin field order = `front-page.php` sequence; RU i18n-ready labels; textdomain foundation |
| **E40** | Expand editable Home blocks (benefits, treatment heading/lead, gallery modes, why-us, staff/landscape, recovery-life, genotyping, videos); seed from frontend; fallbacks |
| **E41** | Hero multi-slide Swiper + settings; retire standalone hero image UI; automated block visibility toggles; recovery-life stage markup + month labels; admin section title CSS |
| **E41-FIX01** | Fix hero height collapse; rehab program intro fields (head/lead/intro_1/intro_2) + rich admin notice linking program page `#13` |

---

## 7.3 Home block model (summary)

Full CSV: `REPORTS/evidence/v9-06e42-home-block-model.csv` and freeze backup `inventories/home-block-model.csv`.

| Order | Frontend | Admin | Source of truth | Home editable | Toggle |
|------:|----------|-------|-----------------|---------------|--------|
| 1 | `hero.php` / `.hero--home` | Hero / slides | Home ACF + Media Library | yes (slides/settings); `hero_media` retired | autoplay/arrows/dots |
| 2 | `recovery-intro.php` | Введение + преимущества/карточки | Home ACF | yes | benefits enabled |
| 3 | `founder-quote.php` | Цитата основателя | Reusable/options | partial | `home_founder_quote_visible` |
| 4 | `treatment-prevention.php` | Лечение и профилактика | Home copy + service CPT | partial | `home_treatment_prevention_visible` |
| 5 | `gallery.php` | Галерея | service CPT + Home mode | partial | `home_gallery_visible` |
| 6 | `why-us.php` | Почему нас выбирают | Home ACF | yes | body/items enabled |
| 7 | `staff-photo.php` | Фото сотрудников | Home ACF media | yes | — |
| 8 | `feature-grid.php` | Преимущества | Home ACF `home_advantages` | yes | — |
| 9 | `clinic-landscape.php` | Пейзаж клиники | Home ACF media | yes | — |
| 10 | `recovery-life.php` | Как меняется жизнь | Home ACF stages | yes | intro/stages enabled |
| 11 | `reviews.php` | Отзывы | Reviews options/shared | partial | `home_reviews_visible` |
| 12 | `rehabilitation-requirements.php` | Условия реабилитации | Reusable block | partial | `home_rehab_requirements_visible` |
| 13 | `rehabilitation-program.php` | Программа | Home intro + program pages | partial | `home_rehab_program_visible` |
| 14 | `genotyping.php` | Генотипирование | Home ACF | yes | body/items enabled |
| 15 | `comfort.php` | Комфорт | Reusable/options | partial | `home_comfort_visible` |
| 16 | `videos.php` | Видео | Home ACF + Media Library | yes | items enabled |
| 17 | `specialists.php` / `.specialists` | Специалисты | `/specialisty/` CPT | partial | `home_specialists_visible` |
| 18 | `articles-teaser.php` | Статьи | Blog posts | partial | `home_articles_visible` |
| 19 | `faq.php` | FAQ | Home ACF | yes | — |
| 20 | `final-form.php` | CTA / форма | Home CTA + site form | partial | — |

---

## 7.4 Patterns for other page types

1. **Frontend-canon audit** — map every section/class to a template partial.
2. **Source-of-truth map** — Home ACF / CPT / child pages / options / media / static fallback.
3. **Classify** — direct editable / automated / static-fallback / legacy-dead.
4. **ACF admin order** — match frontend sequence; readable section titles.
5. **Localize** — RU source + `__()` / textdomain.
6. **Seed** — copy current frontend text/media into fields; never invent clinical claims.
7. **Do not break frontend** — additive CSS; fallbacks required.
8. **Toggles** — for automated/reused blocks.
9. **Repeaters** — enabled flags; bounded max.
10. **Media** — Media Library IDs, not hardcoded uploads paths in content.
11. **Sliders** — reuse proven Swiper patterns; watch layout/height regressions.
12. **Backup first** — DB + theme + plugin + ACF JSON + snapshots.
13. **Validate** — frontend HTTP/DOM, admin inventory, regression routes.
14. **Persist selectively** — charter-only Git; no foreign WIP; no push by default.

---

## 7.5 Next page-type rollout roadmap

Priority order (recommended):

1. **Generic institutional content pages** (`/o-centre/*`, specialists hub/children) — audit → admin parity → media bind → validate → persist.
2. **Service category pages** (`/uslugi/{category}/`) — same wave pattern; reuse E30/E33 listing/slider patterns.
3. **Service leaf / deep pages** — alcohol-direct stack lessons; per-layout ACF.
4. **O-centre hub** (`/o-centre/`) — hub cards/links parity.
5. **Blog archive/single** — E26 patterns; keep content authority clear.
6. **Contacts / reviews pages** — options + page ACF already partially seeded.

Freeze / next execution gate: **Home is frozen** until an explicit operator change request. Next work should open with a **page-type audit** task, not more Home product edits.

---

## References

- Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E42-HOME-ACCEPTED.md`
- Freeze report: `REPORTS/REPORT-FP-0002-V9-06E42-home-freeze-admin-parity-summary.md`
- Wave reports: E38, E38-FIX01, E39, E40, E41, E41-FIX01 under `REPORTS/`
- Backup: `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e42-home-freeze-accepted-before-next-page-types-20260714-033407\`
- Evidence export: `X:\AI MARS STORAGE\exports\fp-0002-shpigovsky-home-freeze\v9-06e42-home-freeze-20260714-033407\`

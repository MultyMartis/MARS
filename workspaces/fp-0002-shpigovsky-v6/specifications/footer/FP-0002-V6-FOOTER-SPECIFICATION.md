# FP-0002 V6 FOOTER SPECIFICATION

## Identity

| Field | Value |
|-------|-------|
| Canonical ID | `FOOTER` |
| Component map | `CMP-020` (`site-footer`) |
| Major section alias | `SECTION-011` (JPG taxonomy) |
| Semantic name | `site-footer` |
| HTML class root | `site-footer` |
| Partial | `src/partials/layout/footer.html` |
| SCSS | `src/scss/layout/_footer.scss` |

## Layout-region classification

| Field | Value |
|-------|-------|
| Type | **LAYOUT REGION** (not page content section) |
| Registry bucket | `LAYOUT REGIONS` |
| SECTION-002+ | **NOT APPLICABLE** |

## Visual source

| Field | Value |
|-------|-------|
| Authority | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` |
| SHA-256 | `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290` |
| Evidence | `specifications/footer/evidence/` |

## Boundaries

| Edge | Y (JPG @ 1398px) | Height |
|------|------------------|--------|
| Top | 15776 | — |
| Bottom | 16343 | — |
| Total | — | **567px** |
| GROUP-01 (columns) | 15776–16152 | 376px (`BLOCK-034`) |
| GROUP-02 (legal strip) | 16152–16343 | 191px (`BLOCK-035`) |

Background: `#e6eff6` family (`--color-page-background`). Not mixed with SECTION-010 contact band (Y 15408–15776).

## Purpose

Sitewide footer layout region: branding + social + phone + CTAs; contact/legal copy; placeholder navigation columns; credits and legal links.

## Content inventory

| Group | Entities |
|-------|----------|
| Top row | logo, social (3), phone, outline CTA, primary CTA |
| Main row | contacts (address, schedule, email, copyright, privacy note), 3 nav columns |
| Legal row | developer credit, privacy policy link, user agreement link |

## Exact texts

| Role | Text |
|------|------|
| Phone | `8 (925) 183-64-64` |
| CTA outline | `ЗАКАЗАТЬ ЗВОНОК` |
| CTA primary | `ЗАПИСАТЬСЯ` |
| Address label | `Москва и Московская область` |
| Schedule | `Режим работы: пн-пт 09:00-19:00, сб-вс 09:00-20:00` |
| Email | `Info@shpigovsky.ru` |
| Email caption | `почта для заявок` |
| Copyright | `© 2026 Все права защищены.` |
| Privacy note | `По вопросам, связанным с обработкой ваших персональных данных, обращайтесь на Info@shpigovsky.ru` |
| Nav heading (×3) | `Название раздела` |
| Nav link col1 (×5) | `Название` |
| Nav link col2 (×4) | `Название` |
| Nav link col3 (×3) | `Название` |
| Credit | `Разработка и продвижение: Overseo` |
| Legal | `Политика конфиденциальности`, `Пользовательское соглашение` |

## DOM structure

```text
footer.site-footer
└── div.site-footer__container
    ├── div.site-footer__top
    ├── div.site-footer__main
    │   ├── div.site-footer__contacts
    │   └── nav.site-footer__nav ×3
    └── div.site-footer__legal
```

## Asset inventory

See `FP-0002-V6-FOOTER-SPECIFICATION.json` → `assets`.

## Container model

`--container-main` (1220px) + `--page-padding-inline` (40px). No Hero `1360px` frame.

## Column model

4-column grid in main row (`repeat(4, minmax(0, 1fr))`); gap `--footer-column-gap` (30px).

## Typography roles

| Role | Tokens |
|------|--------|
| Phone | `--font-size-large`, `--font-weight-semibold` |
| Contact labels | `--font-size-large`, semibold |
| Meta / nav / legal | `--font-size-small`, `--color-text-secondary` |
| Nav headings | `--font-size-base`, semibold |
| CTA | `--button-*`, compact outline uses block `12px` label |

## Color roles

| Role | Token |
|------|-------|
| Background | `--color-page-background` |
| Primary text | `--color-text-primary` |
| Muted | `--color-text-secondary` |
| Accent CTA | `--color-accent` |
| Icon circles | `--color-surface` |
| Borders | `--border-color-subtle` |

## Spacing roles

`--footer-padding-block`, `--footer-row-gap`, `--footer-column-gap`, `--footer-contact-stack-gap`, `--footer-nav-heading-gap`, `--footer-nav-link-gap`, `--footer-legal-gap`, `--footer-legal-row-padding-block`, `--space-10`, `--space-15`, `--space-20`.

## Border and separator roles

Horizontal rules: top row bottom, legal row top — `--border-width` + `--border-color-subtle`.

## Component families

Reused: `.button`, `.icon` sizing hooks, Header logo/social raster assets, Font Awesome for map/envelope.

## Font Awesome icons

| Role | Prefix | Icon |
|------|--------|------|
| Address | `fas` | `fa-map-marker-alt` |
| Email | `fas` | `fa-envelope` |

## Variables reused

Site-wide colors, typography, spacing, container, controls, icons, borders, transitions — see Source-to-Token Map.

## New tokens proposed

Layout-region aliases in `:root` — see JSON `new_tokens_approved`.

## Block-level tokens

`$footer-logo-width`, `$footer-logo-height`, `$footer-callback-font-size`.

## Exact geometry exceptions

Logo `182×82` (shared SVG); no fixed footer height.

## Technical CSS values

`minmax(0, 1fr)`, `line-height: 1` on icon/compact controls, `margin-left: auto` on phone flex item, `text-decoration: underline` on legal links.

## Arbitrary values prohibited

`true` — all production values token-bound.

## Token lookup result

**COMPLETE** — see `FP-0002-V6-FOOTER-SOURCE-TO-TOKEN-MAP.md`.

## HTML authorization

`html_authorized: true`

## SCSS authorization

`scss_authorized: true`

## JavaScript boundary

`javascript_authorized: false` — no JS hooks added.

## Responsive boundary

`responsive_authorized: false` — desktop only.

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Nav column final labels/URLs | JPG shows placeholder `Название` |
| Legal link hrefs | `data-safe-unknown` |
| CTA actions | `data-safe-unknown` |
| YouTube icon asset | `ASSET_REQUIRED` |
| Footer exact rendered height vs 567px JPG | QA metric |

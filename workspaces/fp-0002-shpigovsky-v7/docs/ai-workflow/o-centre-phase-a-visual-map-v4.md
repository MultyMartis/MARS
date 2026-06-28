# O-CENTRE Phase A — Visual Donor Map v4 (Blocks 01–06)

**Page:** `src/pages/o-centre-v1.html`  
**Preview:** `dist/o-centre-v1.html`  
**Figma:** `Spig_v1.2.fig` → frames «О центре» / «О центре - моб»  
**Shell strategy:** dual body classes `page-uslugi-v2 page-service-leaf-v1` — activates existing scoped CSS for category blocks (uslugi) and leaf blocks (intro / CTA / approach) without new selectors.

| Block | Figma screenshot crop | Donor page | Exact DOM fragment | Partial | Root class | Reuse type | Visual delta |
|---|---|---|---|---|---|---|---|
| 01 Header + Hero + Breadcrumbs + Subnav | PG-005 top: hero band, breadcrumb row, anchor pills | `usluga-konechnaya-v1.html` | `<main>` → `services-inner-hero-v2` + `page-service-leaf-v1__upper-nav` → breadcrumbs + subnav | `services-inner-hero-v2.html`, `breadcrumbs.html`, `services-page-subnav.html` | `services-inner-hero-v2`, `page-service-leaf-v1__upper-nav` | EXACT_REUSE_WITH_CONTENT | Hero image/eyebrow/H1/lead/CTA/breadcrumbs/anchors substituted; same hero asset as uslugi-v2 (`services-hero.webp`); dual page class enables leaf upper-nav spacing |
| 02 Первый текстовый блок | PG-005 §«Кто мы»: H2 + red-line lead + editorial paragraphs | `usluga-konechnaya-v1.html` | `service-leaf-intro-v1` heading/lead + `service-leaf-bordered-info-v1__text` body stack | — (inline composition) | `service-leaf-intro-v1` | COMPOSITION_FROM_EXISTING | Content-only substitution; body uses bordered-info text class from leaf page scope (not mixed subdivision nature class) |
| 03 Founder quote | PG-005 founder quote + portrait + CTA | `index.html` / leaf pages | `home-founder-quote` block | `home-founder-quote.html` | `home-founder-quote` | EXACT_REUSE | Canonical partial content; `founderQuoteModifierClass` empty (no `--variant-b`); `modalSource` = `o-centre-founder-quote` |
| 04 «Разные люди, разные истории» | PG-005 § spectrum: H2 + lead + body + 3-image row | `uslugi-v2.html` | `services-category-section-v2--addictions` head + lead + body + gallery (no services list, no CTA) | `services-category-section-v2.html` | `services-category-section-v2` | EXACT_REUSE_WITH_CONTENT | Same gallery row as addictions block; captions omitted (Figma block has no captions); `hideCta=true`, `servicesHtml` empty |
| 05 Dark CTA #1 | PG-005 dark band: title + subtitle + phone + button | Compared: `usluga-podrazdel-v1.html` (`service-subdivision-first-cta-v1`) vs `uslugi-v2.html` (bare `services-program-v2__cta-band`) | Selected: `service-leaf-cta-01-v1` wrapper + `services-program-v2__cta-band` | `service-leaf-cta-01-v1.html` | `service-leaf-cta-01-v1` | EXACT_REUSE | Subdivision first-CTA rejected: requires `page-service-subdivision-v1` scope. Leaf CTA wrapper matches dark-band geometry (height, phone position, background image, grid) on shared cta-band component |
| 06 «Наш подход к лечению» | PG-005 § approach: H2 + red lead + intro + team image + 4 cards (2×2) | `usluga-konechnaya-v1.html` | `#service-leaf-approach` full section | `service-leaf-approach-v1.html` | `service-leaf-approach-v1` | EXACT_REUSE | Canonical copy (partial not parameterized); heading text references alcohol dependency — content delta pending Phase B copy pass; geometry/card grid confirmed vs subdivision `team-stats` (rejected: extra corridor image) and home `feature-grid` (rejected: 3-col / 6-card geometry) |

## Block 06 candidate audit

| Candidate | Source page | Root class | Verdict |
|---|---|---|---|
| `service-leaf-approach-v1` | `usluga-konechnaya-v1.html` | `service-leaf-approach-v1` | **SELECTED** — heading, highlight, intro, staff image, 4-card 2×2 grid |
| `service-subdivision-team-stats-v1` | `usluga-podrazdel-v1.html` | `service-subdivision-team-stats-v1` | REJECTED — extra corridor hero image above heading |
| `home-staff-photo` + `home-feature-grid` | `index.html` | `home-staff-photo` / `home-feature-grid` | REJECTED — 3-column / 6-card grid, no editorial head |
| `services-program-v2` | multiple | `services-program-v2` | REJECTED — program tiles, not approach cards |

## Phase A exclusions (not rendered)

Landscape, program, house/media, second CTA, specialists, reviews, final form — replaced by `<!-- PHASE B STARTS HERE -->`.

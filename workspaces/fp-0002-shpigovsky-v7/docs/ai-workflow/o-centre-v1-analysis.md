# O-centre v1 — implementation tracker

**Page:** `src/pages/o-centre-v1.html`  
**Preview:** `/o-centre-v1.html` (isolated; `/o-centre/` unchanged)  
**Status:** `ISOLATED_VISUAL_IMPLEMENTATION_COMPLETE_WITH_COPY_PLACEHOLDERS`  
**Updated:** 2026-06-27

## Design sources

| Source | Frame | Notes |
| ------ | ----- | ----- |
| `Spig_v1.2.fig` | `О центре` (desktop 1437×12830) | Canonical desktop |
| `Spig_v1.2.fig` | `О центре - моб` (390×16586) | Mobile reference; CSS normalized to **380px** |
| Intake | `about-section-text-map-v12.json` | Text/copy authority |
| Intake | `about-desktop-blocks-detail-v12.json` | Block order / visibility |
| Intake | `about-fig-extract-v12.json` | Asset layer names |

**Not used:** `Шпиговский.fig`, hidden frame `2 - Дом - вступление` (`visible:false`).

## Operator decisions (locked)

- H1: `Шпиговский дом`
- Breadcrumbs: `Главная → О центре`
- Anchor `Кто мы` → `#about-who-we-are`
- Typo fix: `Шпиговский` (not `Шпиговсикй`)
- Approach H2: `Наш подход к лечению` (not alcohol-specific)
- FAQ accordion: **not** added (`faq` frame = final lead form)
- Mobile target width: **380px**
- No registry / route / generator / deploy switch in this pass

## Block order and reuse map

| # | Block | Implementation | Reuse |
| - | ----- | -------------- | ----- |
| 1 | Header + hero + breadcrumbs + anchor nav | `header.html`, `services-inner-hero-v2`, `breadcrumbs`, `services-page-subnav` | Exact reuse + page params |
| 2 | Narrative «Кто мы» | `about-narrative-v1.html` | New; quote via `home-founder-quote` (`about-lorem` variant) |
| 3 | «Кого мы лечим» | `about-who-we-treat-v1.html` | New |
| 4 | CTA «Запишитесь на встречу» | `services-program-cta-band-v2` in `about-first-cta` | Component reuse |
| 5 | «Наш подход к лечению» | `about-approach-v1.html` | New; card grid uses `home-feature-grid__card` |
| 6 | Program 4 directions | `services-program-v2.html` | Reuse with page modifier |
| 7 | «Наш Дом» | `about-house-v1.html` | New; landscape + gallery patterns from home blocks |
| 8 | Compact CTA (guest visit) | `services-program-cta-band-v2` in `about-compact-cta` | Desktop-only per mobile frame delta |
| 9 | Specialists | `home-specialists.html` | Reuse; `allLinkHref=/specialisty/` |
| 10 | Reviews | `home-reviews.html` | Reuse; `allLinkHref=/otzyvy/` |
| 11 | Final form | `home-final-form.html` | Reuse |
| 12 | Footer | `footer.html` | Exact reuse |

## Unique partials

- `src/partials/sections/about-narrative-v1.html`
- `src/partials/sections/about-who-we-treat-v1.html`
- `src/partials/sections/about-approach-v1.html`
- `src/partials/sections/about-house-v1.html`

## Asset mapping (existing runtime assets; no new exports)

| Use | Runtime path | Figma layer (intake) | Notes |
| --- | ------------ | -------------------- | ----- |
| Hero | `assets/img/content/services/services-hero.webp` | `image 13030403` 1400×628 | Existing canonical hero asset |
| Who-we-treat banner | `services-mental-health-02.webp` | `Rectangle 4263` 1170×580 | Existing services asset |
| Who-we-treat thumbs | `services-addictions-01/03`, `services-mental-health-01` | `image 13030399` etc. | Existing |
| Approach staff strip | `pre-reviews/shpigovsky-staff-group.webp` | `image 13030399` 1170×458 | Existing |
| House landscape | `pre-reviews/shpigovsky-clinic-landscape.webp` | clinic landscape | Existing |
| Gallery | `home-comfort/comfort-room-01..06.webp` | `преимущества` gallery | Existing; **no** lifebuoy/logo decor tile |
| Program cards | `rehabilitation-program/program-*.webp` | program rectangles | Existing |
| Founder photo | `content/founder-sergey-shpigovsky.png` | `СЮШ` | Existing |

## Program items (operator override)

| # | Label |
| - | ----- |
| 01 | Генотипирование |
| 02 | Психотерапия |
| 03 | Кинезиотерапия |
| 04 | `04 — Кинезиотерапия` (exact Figma label from intake) |

## COPY_PLACEHOLDER (Lorem ipsum)

| Block | Element | Placeholder |
| ----- | ------- | ----------- |
| Narrative / quote | Expert quote body | Full Lorem ipsum block |
| Program | `lead` | Lorem ipsum |
| Program | `intro` / `intro2` | Lorem ipsum |
| Approach | Card: диагностические инструменты | Lorem ipsum |
| Approach | Card: психиатрия | Lorem ipsum |
| Approach | Card: функциональная терапия | Lorem ipsum |
| Approach | Card: комплиментарная терапия | Lorem ipsum |

**Total placeholders:** 7 text regions  
**Blocking before route switch:** all above require operator copy approval

## Desktop / mobile deltas

- Mobile width normalized to **380px** (Figma frame 390px)
- Hero CTA hidden on about page (not in Figma hero copy set)
- Compact CTA block 8: **desktop only** (no standalone mobile section between house and specialists)
- Hidden intro frame not rendered
- FAQ accordion not added

## QA checklist

- [x] Source page `o-centre-v1.html` created
- [x] `npm run build` exit 0 (via portable Node)
- [x] `dist/o-centre-v1.html` exists
- [x] Canonical four templates unchanged (SHA-256 guard)
- [x] Header / footer / modal / main.js unchanged
- [x] Demo registries unchanged
- [ ] Operator visual review (desktop 1437 / mobile 380)
- [ ] Copy placeholder approval

## Switch status

```text
fp0002_about_page_registry_switch: NOT_STARTED
fp0002_about_page_route_switch: NOT_STARTED
```

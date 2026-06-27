# O-centre — reuse-first blueprint v1

**Page target:** `/o-centre/` (future `src/pages/o-centre.html` or route switch from placeholder)  
**Status:** `REPROJECTION_BLUEPRINT_ONLY` — no HTML/SCSS/JS implementation in this pass  
**Updated:** 2026-06-27  
**Design authority:** `Spig_v1.2.fig` → frames `О центре` (desktop 1437×12830), `О центре - моб` (390×16586)  
**Rejected implementation:** commit `ed271df8` — removed; do not restore `about-*` namespaces

## Operator decisions (locked from prior pass)

| Decision | Value |
| -------- | ----- |
| H1 | `Шпиговский дом` |
| Breadcrumbs | `Главная → О центре` |
| Anchor `Кто мы` | `#about-who-we-are` |
| Typo fix | `Шпиговский` (not `Шпиговсикй`) |
| Approach H2 | `Наш подход к лечению` |
| FAQ accordion | **not** on this page (`faq` frame = final lead form) |
| Mobile target width | **380px** |
| Hero CTA | hidden on about page (per Figma copy set) |
| Compact CTA block 8 | desktop-only between house and specialists |

## Rejected implementation violations (do not repeat)

| Violation | Rejected artifact | Reuse-first fix |
| --------- | ----------------- | --------------- |
| New upper-nav namespace | `page-o-centre-v1__upper-nav` | Use `page-uslugi-v2__upper-nav container` pattern |
| New narrative partial | `about-narrative-v1.html` | Compose with `home-recovery-intro__*` content column + `home-founder-quote` |
| Modified founder quote structure | `founderQuoteEyebrow`, `about-lorem`, duplicate label | Canonical `home-founder-quote.html` unchanged |
| New who-we-treat partial | `about-who-we-treat-v1.html` | `services-category-section-v2.html` |
| New approach partial | `about-approach-v1.html` | `service-leaf-approach-v1.html` |
| New house partial | `about-house-v1.html` | `home-comfort` + `home-clinic-landscape` composition |
| New page-specific CSS block | `.page-o-centre-v1`, `.about-*` (~287 lines) | Zero new CSS for reused blocks; page body class only if existing internal-page pattern requires |
| gulpfile context defaults | `allLinkHref`, `founderQuoteVariant`, etc. | No gulpfile changes for content params |
| Shared partial branches | `home-reviews`, `home-specialists`, `home-founder-quote` | Restored to `b40caf96` authority |

---

## 1. Canonical component inventory

| Component ID | Partial | Used on page | Root class | Purpose | Desktop | Mobile | JS |
| ------------ | ------- | ------------ | ---------- | ------- | ------- | ------ | -- |
| `shell.header` | `partials/layout/header.html` | all templates | `site-header`, `offcanvas` | Global header + mobile menu | Two-row desktop; compact mobile | Offcanvas drawer | `data-offcanvas*`, `data-modal-open` |
| `shell.footer` | `partials/layout/footer.html` | all templates | `site-footer` | Footer nav, contacts, CTA | Multi-column | Stacked | `data-modal-open` |
| `shell.modal` | `partials/components/modal-consultation.html` | all templates | `modal-consultation` | Consultation modal | Dialog overlay | Full-screen dialog | `data-modal`, `data-modal-close`, `data-lead-form` |
| `nav.breadcrumbs` | `partials/components/breadcrumbs.html` | uslugi-v2, subdivision, leaf | `breadcrumbs` | Breadcrumb trail | Inline list | Wrapped list | none |
| `nav.anchor-subnav` | `partials/components/services-page-subnav.html` | uslugi-v2, subdivision, leaf | `services-page-subnav` | In-page anchor links | Horizontal link row | Compact/scroll nav | anchor only |
| `hero.inner-v2` | `partials/sections/services-inner-hero-v2.html` | uslugi-v2, subdivision, leaf | `services-inner-hero-v2` | Inner page hero image + H1 + lead + CTA | Image + text split | Stacked hero | `data-modal-open` on CTA |
| `content.recovery-intro` | `partials/sections/home-recovery-intro.html` | index | `home-recovery-intro` | “Кто мы” narrative + benefit cards | Two-column content + card grid | Stacked cards | none |
| `content.recovery-intro-content-only` | *(composition)* | — | `home-recovery-intro__content`, `home-recovery-intro__heading`, `home-recovery-intro__lead` | Editorial column without card grid | Single column text | Stacked paragraphs | none |
| `content.expert-quote` | `partials/sections/home-founder-quote.html` | index, uslugi-v2, subdivision, leaf | `home-founder-quote` | Founder/expert quote + photo + CTA | Quote left, figure right | Stacked | `data-modal-open` |
| `content.category-section` | `partials/sections/services-category-section-v2.html` | uslugi-v2, subdivision | `services-category-section-v2` | Category hub: heading, intro, services list, gallery, CTA | Multi-column gallery | Single column | `data-modal-open` on section CTA |
| `content.approach-treatment` | `partials/sections/service-leaf-approach-v1.html` | leaf | `service-leaf-approach-v1` | Approach: head, highlight, intro, staff photo, feature cards | Head row + 3-col cards | 1-col cards | none |
| `content.approach-treatment-alt` | `partials/sections/service-subdivision-team-stats-v1.html` | subdivision | `service-subdivision-team-stats-v1` | Same pattern + optional corridor image top | Same + corridor bleed | Stacked | none |
| `content.feature-grid` | `partials/sections/home-feature-grid.html` | index | `home-feature-grid` | Icon/card feature grid | 3-col grid | 1-col | none |
| `content.program-v2` | `partials/sections/services-program-v2.html` | uslugi-v2, subdivision, leaf | `services-program-v2` | 4-direction program cards + optional CTA band | Card grid + foot link | Stacked cards | optional `data-modal-open` |
| `cta.program-band` | `partials/components/services-program-cta-band-v2.html` | embedded in program / pages | `services-program-v2__cta-band` | Title + subtitle + phone + button | Horizontal band | Stacked band | `data-modal-open` |
| `cta.first-meeting` | `partials/sections/service-subdivision-first-cta-v1.html` | subdivision | `service-subdivision-first-cta-v1` | Wrapper for program CTA band | Container band | Same | `data-modal-open` |
| `content.clinic-landscape` | `partials/sections/home-clinic-landscape.html` | index, subdivision, leaf | `home-clinic-landscape` | Wide landscape photo | Full-bleed in container | Same | none |
| `content.comfort-gallery` | `partials/sections/home-comfort.html` | index, uslugi-v2, subdivision, leaf | `home-comfort` | Heading + lead + masonry gallery | Grid gallery + Fancybox | Stacked grid | `data-fancybox="home-comfort"` |
| `content.gallery-slider` | `partials/sections/home-gallery.html` | index | `home-gallery` | Swiper image gallery | Slider | Slider | `data-gallery-slider` |
| `people.specialists` | `partials/sections/home-specialists.html` | index, subdivision, leaf | `home-specialists` | Specialists carousel | Swiper 3.5 slides | Swiper 1.35 slides | `data-specialists-slider` |
| `trust.reviews` | `partials/sections/home-reviews.html` | index, subdivision, leaf | `home-reviews` | Reviews carousel | Swiper 2.5 slides | Swiper 1.35 slides | `data-reviews-slider` |
| `form.final-lead` | `partials/sections/home-final-form.html` | all templates | `home-final-form` | Final lead capture form | Two-column form | Stacked | `data-lead-form`, `data-phone-input` |
| `link.detail` | *(pattern in pages)* | uslugi-v2, program blocks | `home-rehabilitation-program__all-link`, `home-rehabilitation-program__all-text`, `home-rehabilitation-program__all-icon` | “подробнее / узнать больше” links | Inline with icon | Same | none |
| `btn.primary` | *(pattern)* | all | `btn`, `btn_dark`, `btn--primary` | Primary CTA buttons | Pill button | Full-width optional | `data-modal-open` |

---

## 2. Figma-to-component mapping

| Figma block | Screenshot evidence | Existing analogue | Visual identity | Structural identity | Decision |
| ----------- | ------------------- | ----------------- | --------------: | ------------------: | -------- |
| 1. Header | Global shell | `header.html` | 10/10 | 10/10 | `EXACT_REUSE` |
| 1. Hero «Шпиговский дом» | Inner hero with image | `services-inner-hero-v2.html` | 10/10 | 10/10 | `EXACT_REUSE_WITH_CONTENT` |
| 1. Breadcrumbs | Two-level trail | `breadcrumbs.html` | 10/10 | 10/10 | `EXACT_REUSE_WITH_CONTENT` |
| 1. Anchor nav (7 links) | Horizontal subnav | `services-page-subnav.html` inside `page-uslugi-v2__upper-nav` | 10/10 | 10/10 | `EXACT_REUSE_WITH_CONTENT` |
| 2. «Кто мы» narrative | H2 + lead + body paragraphs | `home-recovery-intro__content` column classes | 9/10 | 9/10 | `COMPOSITION_OF_EXISTING_COMPONENTS` |
| 2. Expert quote | Quote + photo, no CTA | `home-founder-quote.html` | 10/10 | 10/10 | `EXACT_REUSE_WITH_CONTENT` |
| 3. «Кого мы лечим» | H2 + banner + text + 3 thumbs | `services-category-section-v2.html` | 9/10 | 9/10 | `EXACT_REUSE_WITH_CONTENT_AND_ASSET` |
| 4. CTA «Запишитесь на встречу» | Program CTA band | `service-subdivision-first-cta-v1.html` | 10/10 | 10/10 | `EXACT_REUSE_WITH_CONTENT` |
| 5. «Наш подход к лечению» | Head + link + highlight + staff + 6 cards | `service-leaf-approach-v1.html` | 10/10 | 10/10 | `EXACT_REUSE_WITH_CONTENT` |
| 6. Program 4 directions | 4 program cards + foot link | `services-program-v2.html` | 10/10 | 10/10 | `EXACT_REUSE_WITH_CONTENT` |
| 7. «Наш Дом» heading + lead | Section intro | `home-comfort.html` head + lead region | 8/10 | 8/10 | `EXACT_REUSE_WITH_CONTENT` |
| 7. Brand typography «Шпиг / вский / дом» | Split display type | **none in runtime** | — | — | `GENUINELY_NEW_BLOCK` |
| 7. Landscape photo | Wide building shot | `home-clinic-landscape.html` | 10/10 | 10/10 | `EXACT_REUSE_WITH_ASSET` |
| 7. Interior gallery (6 tiles) | Masonry Fancybox grid | `home-comfort.html` gallery markup | 9/10 | 9/10 | `EXACT_REUSE_WITH_CONTENT_AND_ASSET` |
| 8. Compact CTA guest visit | Secondary CTA band | `services-program-cta-band-v2.html` in `container` (uslugi-v2 pattern) | 10/10 | 10/10 | `EXACT_REUSE_WITH_CONTENT` |
| 9. Specialists | Carousel + heading | `home-specialists.html` | 10/10 | 10/10 | `EXACT_REUSE_WITH_CONTENT` |
| 10. Reviews | Carousel + heading | `home-reviews.html` | 10/10 | 10/10 | `EXACT_REUSE_WITH_CONTENT` |
| 11. Final form | Lead form | `home-final-form.html` | 10/10 | 10/10 | `EXACT_REUSE_WITH_CONTENT` |
| 12. Footer | Global footer | `footer.html` | 10/10 | 10/10 | `EXACT_REUSE` |

---

## 3. Exact reuse contracts

### 3.1 Shell + upper page chrome

| Figma block | Canonical partial | Exact root class | Exact child classes | Allowed substitutions | Forbidden changes |
| ----------- | ----------------- | ---------------- | ------------------- | --------------------- | ----------------- |
| Header | `header.html` | `site-header` | `site-header__*`, `offcanvas__*` | active nav params for `/o-centre/` | new header variant |
| Hero | `services-inner-hero-v2.html` | `services-inner-hero-v2` | `services-inner-hero-v2__eyebrow`, `__title`, `__lead`, `__actions`, `__image` | eyebrow, title, lead, image path, `titleId`, hide CTA via existing page CSS scope if already used elsewhere | new hero partial; `page-o-centre-v1__*` |
| Breadcrumbs + subnav wrapper | page assembly (uslugi-v2 pattern) | `page-uslugi-v2__upper-nav` + `container` | `breadcrumbs`, `services-page-subnav` | breadcrumb labels/hrefs; `listHtml` anchor items | `page-o-centre-v1__upper-nav`; new wrapper CSS |
| Breadcrumbs | `breadcrumbs.html` | `breadcrumbs` | `breadcrumbs__list`, `__item`, `__link`, `__current` | crumb text, hrefs | new breadcrumb namespace |
| Anchor nav | `services-page-subnav.html` | `services-page-subnav` | `services-page-subnav__list`, `__item`, `__link` | `listHtml` anchor targets/labels | new subnav namespace |

### 3.2 «Кто мы» + expert quote

| Figma block | Canonical partial | Exact root class | Exact child classes | Allowed substitutions | Forbidden changes |
| ----------- | ----------------- | ---------------- | ------------------- | --------------------- | ----------------- |
| Narrative column | composition from `home-recovery-intro` content column | `home-recovery-intro` (section) | `home-recovery-intro__content`, `home-recovery-intro__heading`, `home-recovery-intro__lead` | heading id `about-who-we-are`, all copy, paragraph count | `about-narrative*`; card grid unless Figma proves cards; new editorial namespace |
| Expert quote | `home-founder-quote.html` | `home-founder-quote` | `home-founder-quote__layout`, `__quote`, `__mark`, `__text`, `__figure`, `__photo`, `__author`, `__name`, `__role`, `__cta` | quote copy, name, role, photo, `modalSource`, `founderQuoteModifierClass` (`home-founder-quote--variant-b`), omit CTA by not rendering button in page if design omits — **requires operator decision**: canonical partial always renders CTA today | `founderQuoteEyebrow`; `about-lorem`; `hideFounderCta` gulp branches; duplicate `visually-hidden` + visible eyebrow; `home-founder-quote--about-narrative` |

**Canonical quote aria structure (authority `b40caf96`):**

```html
<section class="home-founder-quote…" aria-labelledby="home-founder-quote-label">
  …
  <figure class="home-founder-quote__figure">
    <span class="visually-hidden" id="home-founder-quote-label">Слово основателя</span>
    …
  </figure>
</section>
```

**Forbidden:** simultaneous visible eyebrow + `visually-hidden` duplicate label.

**Operator decision required:** Figma “мнение эксперта” label vs canonical “Слово основателя” — resolve without structural change (copy in visually-hidden only if canonical pattern kept).

**Operator decision required:** hide CTA button on about quote — canonical partial always includes CTA; options: (a) accept CTA if Figma shows none — operator adjudication; (b) future safe content param that removes button without changing classes elsewhere — **not in this pass**.

### 3.3 «Кого мы лечим»

| Figma block | Canonical partial | Exact classes | Allowed | Forbidden |
| ----------- | ----------------- | ------------- | ------- | --------- |
| Who we treat | `services-category-section-v2.html` | `services-category-section-v2`, `__heading`, `__intro`, `__lead`, `__gallery`, `__gallery-item`, `__gallery-image`, `__caption` | section id `who-we-treat`, heading, intro/lead/body via `intro`/`lead`/`bodyHtml`, banner via `galleryHtml`, 3-up thumbs via `galleryHtml`, empty `servicesHtml` if list not in Figma | `about-who-we-treat*` namespace |

### 3.4 CTA bands

| Figma block | Canonical partial | Exact classes | Allowed | Forbidden |
| ----------- | ----------------- | ------------- | ------- | --------- |
| Meeting CTA | `service-subdivision-first-cta-v1.html` → `services-program-cta-band-v2.html` | `service-subdivision-first-cta-v1`, `services-program-v2__cta-band`, `services-program-v2__cta-title`, `__cta-subtitle`, `__cta-phone`, `__cta-button` | all CTA copy, phone, `ctaSource` | `about-first-cta*` wrapper namespace |
| Guest visit CTA | `services-program-cta-band-v2.html` in `container` | same as above | copy/phone/source | `about-compact-cta*` namespace |

### 3.5 Approach + program

| Figma block | Canonical partial | Exact classes | Allowed | Forbidden |
| ----------- | ----------------- | ------------- | ------- | --------- |
| Approach | `service-leaf-approach-v1.html` | `service-leaf-approach-v1`, `__head`, `__heading`, `__all-link`, `__highlight`, `__intro`, `__staff-bleed`, `__staff-image`, `home-feature-grid__card-grid`, `home-feature-grid__card` | section id `about-approach`, heading text, highlight, intro, card titles/text, link href | `about-approach*`; corridor block from subdivision variant unless Figma shows corridor |
| Program | `services-program-v2.html` | `services-program-v2`, `__heading`, `__lead`, `__intro`, `__items`, `__item`, `__item-title`, `__item-image`, `home-rehabilitation-program__all-link` | id `about-program`, item labels, images, `hideCtaBand`, `allLinkHref` | `services-program-v2--about` page-only modifier unless proven on another page |

### 3.6 «Наш Дом»

| Figma block | Canonical partial | Exact classes | Allowed | Forbidden |
| ----------- | ----------------- | ------------- | ------- | --------- |
| Section head + lead | `home-comfort.html` head region | `home-comfort`, `home-comfort__heading`, `home-comfort__lead` | heading, lead copy, section id on wrapper via `sectionId` | full `home-comfort` include if decor tile must be absent — see §5 |
| Landscape | `home-clinic-landscape.html` | `home-clinic-landscape`, `home-clinic-landscape__bleed`, `home-clinic-landscape__image` | alt text, same asset | nested bleed without section wrapper |
| Gallery | `home-comfort.html` gallery region | `home-comfort__gallery`, `home-comfort__gallery-item`, `home-comfort__gallery-image` | images, fancybox group name, alts | logo decor tile (`home-comfort__gallery-item_decor`) if Figma omits — operator decision |

### 3.7 Lower shared blocks

| Figma block | Canonical partial | Exact classes | Allowed | Forbidden |
| ----------- | ----------------- | ------------- | ------- | --------- |
| Specialists | `home-specialists.html` | `home-specialists`, `__heading`, `__all-link`, `__card`, `__photo`, `__name`, `__role` | `sectionId`, `headingId`, `headingText` | `allLinkHref` gulp branch until proven safe param contract; new namespace |
| Reviews | `home-reviews.html` | `home-reviews`, `__title`, `__all-link`, `__card`, `__rating`, `__quote` | `sectionId`, `sectionModifierClass` | `allLinkHref` gulp branch; new namespace |
| Final form | `home-final-form.html` | `home-final-form`, `__heading`, `__lead`, form fields | `headingId`, `headingText`, `leadText`, `leadSource` | new form variant |
| Footer | `footer.html` | `site-footer` | none | changes |

---

## 4. Breadcrumbs and upper navigation

| Item | Authority |
| ---- | --------- |
| Existing partial | `breadcrumbs.html` + `services-page-subnav.html` |
| Existing wrapper | `<div class="page-uslugi-v2__upper-nav container">` from `uslugi-v2.html` |
| Existing classes | `breadcrumbs`, `services-page-subnav`, `page-uslugi-v2__upper-nav` |
| New classes | **ZERO** — use existing page wrapper class even on about page, or reuse subdivision wrapper `page-service-subdivision-v1__upper-nav` if body class is subdivision-like |
| New CSS | **ZERO** for upper nav |
| Rejected | `page-o-centre-v1__upper-nav` — **FORBIDDEN** |

**Recommended body/wrapper pairing:** mirror `uslugi-v2.html` upper chrome exactly; only swap breadcrumb params and `listHtml`.

---

## 5. Expert quote — canonical lock

| Item | Value |
| ---- | ----- |
| Canonical partial | `home-founder-quote.html` @ `b40caf96` |
| Root class | `home-founder-quote` (+ optional `home-founder-quote--variant-b`) |
| Aria | `aria-labelledby="home-founder-quote-label"` |
| Label | single `span.visually-hidden#home-founder-quote-label` — no visible eyebrow in authority |
| Quote body | one or more `p.home-founder-quote__text > span` |
| Figure | `home-founder-quote__figure` → photo → `figcaption.home-founder-quote__author` |
| CTA | `button.btn.home-founder-quote__cta` with `data-modal-open="consultation"` |
| Duplicate eyebrow | **FORBIDDEN** |
| Duplicate accessible label | **FORBIDDEN** |
| About variant structure | **FORBIDDEN** |

---

## 6. Buttons and links

| Figma element | Existing component | Classes | Icon | Behavior |
| ------------- | ------------------ | ------- | ---- | -------- |
| Hero CTA | hero inner CTA | `btn`, `services-inner-hero-v2__cta` | none | `data-modal-open` |
| CTA band button | program band | `btn`, `btn_dark`, `btn--primary`, `services-program-v2__cta-button` | none | `data-modal-open` |
| “подробнее” links | program/approach head | `home-rehabilitation-program__all-link`, `__all-text`, `__all-icon` | `fas fa-play` | href |
| Specialists “все специалисты” | specialists head | `home-specialists__all-link`, `__all-text`, `__all-icon` | `fas fa-play` | href `#` until route switch |
| Reviews “Смотреть отзывы” | reviews head | `home-reviews__all-link`, `__all-text`, `__all-icon` | `fas fa-caret-right` | href `#` until route switch |
| Founder quote CTA | founder quote | `btn`, `home-founder-quote__cta` | none | `data-modal-open` |

**New button classes:** ZERO  
**New link system:** ZERO

---

## 7. Genuinely new blocks

| Block | Existing components checked | Why reuse impossible | Proposed minimal namespace |
| ----- | --------------------------- | -------------------- | -------------------------- |
| Brand typography «Шпиг / вский / дом» | `hero__title`, `home-comfort__heading`, `home-recovery-intro__heading`, logo in header/footer | No existing split-word display typography block; no matching HTML/CSS geometry in canonical pages | **UNRESOLVED — pending Figma crop verification.** If confirmed: single scoped block e.g. `home-brand-display` only after operator approval; not `about-house__brand*` |

**If brand block confirmed new:**

1. Minimal structure: section-scoped display type only, no duplication of landscape/gallery
2. CSS scope: one new root, no overrides of `home-comfort` / `home-clinic-landscape`
3. Desktop/mobile: follow Figma `О центре` / `О центре - моб` frames

**Operator decisions blocking zero-new-css claim:**

| # | Topic | Options |
| - | ----- | ------- |
| 1 | Quote CTA visible on about page? | Keep canonical CTA vs operator-approved param |
| 2 | Quote label text | «Слово основателя» vs «Мнение эксперта» — copy only in existing visually-hidden |
| 3 | `home-comfort` logo decor tile | Include vs exclude on about gallery |
| 4 | Brand typography block | New minimal block vs flatten to heading typography |
| 5 | Hero CTA hide | Use existing internal-page CSS pattern if one exists — **SAFE UNKNOWN** without Figma/CSS cross-check |
| 6 | Specialists/reviews `all-link` hrefs | Keep `#` until route switch vs hardcode demo URLs in page include params without partial changes |

---

## 8. Asset reuse map

| Figma layer | Existing asset | Same image | Same crop | Decision |
| ----------- | -------------- | ---------: | --------: | -------- |
| Hero `image 13030403` | `assets/img/content/services/services-hero.webp` | yes | yes | `REUSE_EXACT` |
| Who-we-treat banner `Rectangle 4263` | `services-mental-health-02.webp` | yes | yes | `REUSE_EXACT` |
| Who-we-treat thumbs | `services-addictions-01/03`, `services-mental-health-01` | yes | yes | `REUSE_EXACT` |
| Approach staff strip | `pre-reviews/shpigovsky-staff-group.webp` | yes | yes | `REUSE_EXACT` |
| House landscape | `pre-reviews/shpigovsky-clinic-landscape.webp` | yes | yes | `REUSE_EXACT` |
| Gallery `comfort-room-01..06` | `home-comfort/comfort-room-*.webp` | yes | yes | `REUSE_EXACT` |
| Program cards | `rehabilitation-program/program-*.webp` | yes | yes | `REUSE_EXACT` |
| Founder photo `СЮШ` | `content/founder-sergey-shpigovsky.png` | yes | yes | `REUSE_EXACT` |
| Brand display graphics | none in repo | — | — | `UNRESOLVED` |

---

## 9. New page assembly blueprint

| Order | Figma block | Implementation source | Partial | New HTML | New CSS |
| ----: | ----------- | --------------------- | ------- | -------: | ------: |
| 1 | Header | `header.html` | yes | 0 | 0 |
| 2 | Hero | `services-inner-hero-v2.html` | yes | 0 | 0 |
| 3 | Breadcrumbs + anchors | `page-uslugi-v2__upper-nav` + breadcrumbs + subnav | yes | 0 | 0 |
| 4 | «Кто мы» text | `home-recovery-intro__*` content column composition | partial classes only | 0* | 0 |
| 5 | Expert quote | `home-founder-quote.html` | yes | 0 | 0 |
| 6 | «Кого мы лечим» | `services-category-section-v2.html` | yes | 0 | 0 |
| 7 | CTA встреча | `service-subdivision-first-cta-v1.html` | yes | 0 | 0 |
| 8 | Approach | `service-leaf-approach-v1.html` | yes | 0 | 0 |
| 9 | Program 4 dir | `services-program-v2.html` | yes | 0 | 0 |
| 10 | «Наш Дом» head | `home-comfort.html` head params | yes | 0 | 0 |
| 11 | Brand typography | TBD | no | 1? | 1? |
| 12 | Landscape | `home-clinic-landscape.html` | yes | 0 | 0 |
| 13 | Gallery | `home-comfort.html` gallery region | yes | 0 | 0 |
| 14 | Guest CTA | `services-program-cta-band-v2.html` in container | yes | 0 | 0 |
| 15 | Specialists | `home-specialists.html` | yes | 0 | 0 |
| 16 | Reviews | `home-reviews.html` | yes | 0 | 0 |
| 17 | Final form | `home-final-form.html` | yes | 0 | 0 |
| 18 | Footer | `footer.html` | yes | 0 | 0 |

\*Page file will contain includes and composition markup only — no new partial files in reuse-first pass.

### Totals (target)

| Metric | Count |
| ------ | ----: |
| EXACT REUSE BLOCKS | 8 |
| CONTENT-ONLY REUSE BLOCKS | 9 |
| COMPOSED FROM EXISTING | 2 (upper nav, narrative column) |
| GENUINELY NEW BLOCKS | 0–1 (brand typography — unresolved) |
| NEW CSS NAMESPACES | 0–1 (brand typography only if proven) |
| NEW JS | 0 |

---

## 10. Reuse-first acceptance gate

| Gate | Status |
| ---- | ------ |
| Every Figma block mapped | PASS |
| Every reused block has exact partial | PASS |
| Exact classes enumerated | PASS |
| Allowed substitutions enumerated | PASS |
| Forbidden changes enumerated | PASS |
| New blocks proven | PARTIAL — brand typography unresolved |
| Breadcrumbs no new namespace | PASS |
| Quote no new variant structure | PASS |
| Buttons/links use canonical system | PASS |
| Duplicate accessibility elements absent | PASS (by contract) |
| New JS required | NO |

**Gate recommendation:** `FP0002_O_CENTRE_REPROJECTION_REQUIRES_OPERATOR_DECISIONS` (items in §7 operator table)

---

## 11. Implementation pass constraints (next pass)

**Allowed in implementation pass:**

- Create page file with includes only
- Content parameters on existing partials
- Page-level composition using existing classes
- Minimal page body class if matching existing internal template convention

**Forbidden in implementation pass:**

- `about-*` partials or CSS namespaces
- `page-o-centre-v1__*` wrappers
- Modifying `home-founder-quote.html` structure for about-only branches
- gulpfile context defaults for about-only params
- Shared partial structural changes without cross-page regression proof
- Registry / generator / route switch / deploy

---

## 12. Evidence references

| Artifact | Location |
| -------- | -------- |
| Pre-removal backup | `C:\MARS Phenix\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\operator-checkpoints\FP-0002-V7-BEFORE-O-CENTRE-REJECTED-IMPLEMENTATION-REMOVAL.zip` |
| Backup SHA-256 | `DD3C7C743C0EFB35E0867391506CF6B42FBF3A74979E18A2C6985469FF3249B3` |
| Authority commit | `b40caf96` |
| Rejected commit | `ed271df8` |
| Canonical upper nav reference | `src/pages/uslugi-v2.html` lines 10–13 |
| Canonical approach reference | `src/partials/sections/service-leaf-approach-v1.html` |
| Canonical CTA wrapper | `src/partials/sections/service-subdivision-first-cta-v1.html` |

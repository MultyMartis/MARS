# FP-0002 Home Block Inventory v1

**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`  
**Date:** 2026-06-23  
**Scope:** All existing home page partials audited for DOM structure (not class-name similarity alone).

## Summary

| Metric | Value |
|--------|-------|
| Layout partials | 2 |
| Section partials | 18 |
| Component partials | 1 |
| **Total audited** | **21** |

---

## Layout

| Partial | Semantic role | DOM structure | Content slots | Image slots | CTA slots | Current pages |
| ------- | ------------- | ------------- | ------------- | ----------- | --------- | ------------- |
| `partials/layout/header.html` | Site chrome, nav, mobile bar, off-canvas | `<header.site-header>` → container → mobile bar (logo, phone, messengers, burger) + desktop row (logo, nav, phone, CTA) + off-canvas panel (nav, contacts, CTA) | Nav labels, phone, active nav class params | Logo SVG, messenger icons | Consultation modal open, tel links | `index.html`, `uslugi.html` |
| `partials/layout/footer.html` | Site footer, sitemap, legal | `<footer.site-footer>` → container → brand column + multi-column nav + contacts + legal row | Link text, addresses, phones | Logo | Tel, internal nav links | `index.html`, `uslugi.html` |

## Hero

| Partial | Semantic role | DOM structure | Content slots | Image slots | CTA slots | Current pages |
| ------- | ------------- | ------------- | ------------- | ----------- | --------- | ------------- |
| `partials/sections/hero.html` | Home above-fold hero | `<section.hero>` → media wrapper → image + container → panel (tagline `p`, `h1`) + actions (single modal button) | Tagline, H1, button label, modal source | 1 full-bleed hero image | 1 modal CTA | `index.html` (inside `.intro-section`) |

## Main content sections (home order)

| Partial | Semantic role | DOM structure | Content slots | Image slots | CTA slots | Current pages |
| ------- | ------------- | ------------- | ------------- | ----------- | --------- | ------------- |
| `partials/sections/home-recovery-intro.html` | Section 01 — recovery philosophy | `<section>` → container → wrapper → content column (`h2`, lead `p`, benefits `ul`×4) + card grid (`li`×6: icon span + `h3` + `p`) | Heading, lead, 4 benefits, 6 card titles/texts | 0 active (decor commented) | 0 | `index.html` |
| `partials/sections/home-founder-quote.html` | Founder quote block | `<section>` → container → layout → `blockquote` (4×`p` + quote icon) + `figure` (photo, name, role, modal button) | Quote paragraphs, name, role, `@@modalSource` | 1 founder photo | 1 modal CTA | `index.html`, `uslugi.html` |
| `partials/sections/home-treatment-prevention.html` | Treatment / prevention accordion hub | `<section>` → container → head (`h2` + «Смотреть все» link) + lead `p` + accordion (`data-accordion`) with 4 items (toggle button + optional service link list) | Section title, lead, 4 accordion labels, service link rows in panel 1 only | 0 | «Смотреть все» link (href `#`), service links | `index.html` |
| `partials/sections/home-gallery.html` | Therapy gallery strip | `<section>` → container → head + swiper gallery with image slides | Heading, slide alts | Multiple therapy images | Fancybox links | `index.html` |
| `partials/sections/home-why-us.html` | Why-us feature list | `<section>` → container → head + grid of feature cards (`h3` + `p` each) | Heading, card copy | 0 | 0 | `index.html` |
| `partials/sections/home-staff-photo.html` | Staff group photo | `<section>` → container → single large image + caption area | Caption text | 1 staff photo | 0 | `index.html` |
| `partials/sections/home-feature-grid.html` | Icon feature grid | `<section>` → container → `ul` of items (icon + `h3` + `p`) | 6 feature titles/texts | 0 (icon fonts) | 0 | `index.html` |
| `partials/sections/home-clinic-landscape.html` | Clinic exterior landscape | `<section>` → container → image + text column | Heading, body copy | 1 landscape image | 0 | `index.html` |
| `partials/sections/home-reviews.html` | Reviews carousel | `<section>` → container → head + Swiper (`data-slider`) with review cards | Demo review text, names | 0 | Swiper nav | `index.html` |
| `partials/sections/home-rehabilitation-requirements.html` | Rehabilitation requirements | `<section>` → container → head + two-column content (lists + aside image) | Headings, list items | 1 aside image | 0 | `index.html` |
| `partials/sections/home-rehabilitation-program.html` | Program — 4 directions | `<section>` → container → head (`h2` + link) + 2 intro `p` + 4 `article` direction blocks (image + title + text each) | `@@programHeading`, lead, 4 direction bodies | 4 direction images | «подробнее» link (href `#`) | `index.html`, `uslugi.html` |
| `partials/sections/home-genotyping.html` | Genotyping promo | `<section>` → container → split layout (copy + image) | Heading, paragraphs | 1 promo image | 0 | `index.html` |
| `partials/sections/home-comfort.html` | Comfort gallery | `<section>` → container → head + lead + gallery grid (decor logo + Fancybox image links) | Heading, lead | Logo decor + comfort photos | Fancybox, «подробнее» link | `index.html`, `uslugi.html` |
| `partials/sections/home-videos.html` | Video previews | `<section>` → container → head + 2 video preview cards | Titles | 2 preview images | Play affordance (demo) | `index.html` |
| `partials/sections/home-specialists.html` | Specialists Swiper | `<section>` → container → head + Swiper specialist cards | Names, roles | Specialist photos | Swiper nav | `index.html` |
| `partials/sections/home-articles.html` | Articles grid | `<section>` → container → head + article cards (image + title + excerpt) | Article titles, excerpts | Article thumbs | Card links | `index.html` |
| `partials/sections/home-faq.html` | FAQ accordion | `<section>` → container → `h2` + accordion list (`data-accordion`, multiple Q/A items) | Questions, answers | 0 | 0 | `index.html`, `uslugi.html` |
| `partials/sections/home-final-form.html` | Final lead form band | `<section>` → container → band → copy (`h2`, lead) + form (hidden fields incl. `@@leadSource`, name, phone, consent, submit) | Heading, lead, field labels, `@@leadSource` | 0 | Submit | `index.html`, `uslugi.html` |

## Components

| Partial | Semantic role | DOM structure | Content slots | Image slots | CTA slots | Current pages |
| ------- | ------------- | ------------- | ------------- | ----------- | --------- | ------------- |
| `partials/components/modal-consultation.html` | Shared consultation modal | `<div data-modal>` → dialog (title, form fields, consent, submit, close) | Modal title, submit text via triggers | 0 | Close, submit | `index.html`, `uslugi.html` |

---

## Section alias map (operator vocabulary)

| Operator label | Partial |
| -------------- | ------- |
| Section 01 | `home-recovery-intro.html` |
| Section 02 (founder on home) | `home-founder-quote.html` |
| Section 03 / treatment-prevention | `home-treatment-prevention.html` |
| Gallery | `home-gallery.html` |
| Program | `home-rehabilitation-program.html` |

**REJECTED IMPLEMENTATION — NOT CURRENT AUTHORITY:** `services-hero.html`, `services-addictions.html`, `services-mental-health.html`, `services-eating-disorders.html` (removed by revert `25bfbce`).

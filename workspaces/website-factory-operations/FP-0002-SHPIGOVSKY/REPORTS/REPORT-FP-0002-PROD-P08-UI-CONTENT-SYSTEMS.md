# REPORT — FP-0002 PROD-P08 UI / Content Systems

**Date:** 2026-08-14  
**Host:** `http://shpigovsky.beget.tech/`  
**Evidence:** `REPORTS/evidence/prod-p08-ui-content-systems/`

```text
PROD-P08 TECHNICAL CLOSEOUT COMPLETE — OPERATOR VISUAL ACCEPTANCE PENDING
```

---

## 1. Status

* **PASS / PARTIAL**
  * A Mobile sliders, C Lifebuoy, D Specialist, E Reading time: **PASS**
  * B Typography: **PARTIAL** — source hardcoded + specialist migrated fields normalized; broad live WYSIWYG/options mass rewrite intentionally not forced (HTML/shortcode safety)
* production file writes: **26** (exact-file SFTP)
* DB/Admin writes: **bounded** specialist `specialist_*` postmeta upserts for pages `#1031/#1032/#1033/#1097` (generic_page_body **preserved**)
* ACF mutations: **2 groups** — new `group_fp02_specialist_profile`; instruction/label update on existing `article_reading_time` in `group_fp02_blog_post_article_meta`
* WPilot writes: **0** (`write_enabled=false`)
* commit/push: **none**

---

## 2. Backup Gate

```text
CURRENT PRE-P08 LAYER A BACKUP = OPERATOR CONFIRMED
```

* Layer B: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p08-layer-b-pre\`
* DB snapshots: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p08-db-snapshots\`
* Rollback: Layer A + Layer B + specialist postmeta before TSV

---

## 3. Mobile Slider Navigation

* Mapped non-Hero: gallery, services-category gallery, reviews, specialists, articles — **5/5**
* Converted: markup nav partial + JS `shpigovskyAttachFp02SliderNav` + CSS `fp02-mobile-slider-nav.css`
* Hero exclusions: `[data-hero-slider]` / `[data-services-hero-slider]` **unchanged** (home hero hooks intact; no `data-fp02-slider-nav` inside hero)
* ≤767px: left-aligned prev/next; dots visually suppressed
* ≥768px: dots retained; prev/next hidden
* Responsive QA evidence: `FRONTEND-QA.json`, `P07-REGRESSION-AND-HERO.json` (home 4 nav mounts; `/uslugi/` 2 category gallery navs; alcohol leaf specialists + reviews nav)

```text
NON-HERO MOBILE DOT PAGINATION NORMALIZED TO LEFT-ALIGNED PREV/NEXT CONTROLS
```

---

## 4. Typography

| Owner class | Count / note |
|-------------|--------------|
| Source PHP strings | ~193 strings / 610 Unicode NBSP (`TYPOGRAPHY-SOURCE-MUTATIONS.md`) |
| Specialist migrated fields | 4 pages; plain/WYSIWYG values typographed on write |
| Pages / services / blog / options mass DB | **Not mass-rewritten** (HTML/shortcode STOP discipline) |
| NBSP strategy | Unicode `U+00A0` in plain/PHP; HTML contexts keep safe markup |

Unresolved / residual: broader live ACF WYSIWYG and options copy still eligible for a **bounded follow-up** typography wave.

Required full claim **not** asserted for entire live DB surface.

---

## 5. Apple Lifebuoy

* Root cause: transform driven only via CSS custom properties (WebKit recomposite gap)
* Implementation: dual-write CSS vars + **direct** `img.style.transform` / `webkitTransform`; rAF + passive scroll retained; amplitude model preserved; `prefers-reduced-motion` freeze retained
* Non-Apple: no architectural rewrite; Chromium path still compositor transform
* Apple QA:

```text
APPLE DEVICE FINAL PHYSICAL QA = OPERATOR REQUIRED
```

```text
WEBKIT/IOS-SAFE SCROLL-DRIVEN LIFEBUOY MOTION IMPLEMENTED
```

---

## 6. Specialist Architecture

* Objects: parent `#1030` `/specyalisty/` + children `#1031 shipovsky`, `#1032 kazakov`, `#1033 kostyuk`, `#1097 shapiguzova`
* Schema: `group_fp02_specialist_profile` (portrait = Featured Image notice; role; experience; specialty; education; specialization; principles; additional; certificates gallery)
* Migrations: structured fields written; `generic_page_body` **preserved**; map `SPECIALIST-MIGRATION-MAP.json`
* Template: `template-parts/specialist/profile.php` via `content-page.php` specialist branch
* Empty sections hidden

```text
SPECIALIST FRONTEND + ADMIN STRUCTURED MODEL LIVE
```

---

## 7. Specialist Gallery

* Kostyuk certificates `#1853/#1855/#1854` → gallery field; FE grid `object-fit: contain`; Fancybox `data-fancybox`
* Sparse specialists: certs section hidden
* Attachment IDs preserved

---

## 8. Blog Reading Time

* Reused field `article_reading_time` / `field_fp02_article_reading_time`
* Manual override if >0; else auto at render (not written to DB)
* WPM **190**; ceil; min 1
* Pluralization unchanged (`минута/минуты/минут` + `на чтение`)
* Tests: manual `5 минут` / `3 минуты`; empty demo → `1 минута`

```text
BLOG READING TIME = MANUAL OVERRIDE OR AUTOMATIC CALCULATION
```

---

## 9. ACF

* Exact groups: `group_fp02_specialist_profile` (new); `group_fp02_blog_post_article_meta` (reading-time label/instructions only)
* Source JSON + plugin `FieldGroups.php` + production `wp-content/acf-json/`
* No broad ACF sync; P07 groups untouched

---

## 10. Exact Files Changed

Theme:

* `assets/js/v9-shell.js`
* `assets/js/fp02-lifebuoy-parallax.js`
* `assets/css/fp02-lifebuoy-parallax.css`
* `assets/css/fp02-mobile-slider-nav.css`
* `assets/css/fp02-specialist-profile.css`
* `inc/assets.php`
* `inc/blog-helpers.php`
* `inc/specialist-helpers.php`
* `inc/reusable-blocks-helpers.php`
* `inc/v9-static-content.php`
* `inc/home-fallbacks.php`
* `inc/institutional-about-v9-content.php`
* `inc/contacts-helpers.php`
* `functions.php`
* `template-parts/components/fp02-slider-mobile-nav.php`
* `template-parts/home/gallery.php`
* `template-parts/home/specialists.php`
* `template-parts/home/articles-teaser.php`
* `template-parts/shared/reviews-slider.php`
* `template-parts/service/alcohol-direct-v9/specialists.php`
* `template-parts/services-hub/service-group.php`
* `template-parts/generic/content-page.php`
* `template-parts/specialist/profile.php`

Plugin:

* `src/Fields/FieldGroups.php`

ACF JSON:

* `group_fp02_specialist_profile.json`
* `group_fp02_blog_post_article_meta.json`

Docs/evidence under `REPORTS/` + `PROJECT-STATUS.md`

---

## 11. Content/Admin Objects Changed

| ID | Fields |
|----|--------|
| `#1033` kostyuk | `specialist_role`, `specialist_experience`, `specialist_specialty`, `specialist_education`, `specialist_specialization`, `specialist_principles`, `specialist_certificates` |
| `#1031` shipovsky | `specialist_role`, `specialist_additional` |
| `#1032` kazakov | `specialist_role`, `specialist_additional` |
| `#1097` shapiguzova | `specialist_role`, `specialist_additional` |

`generic_page_*` bodies: **not deleted**.

---

## 12. Frontend QA

Routes HTTP 200 (alcohol leaf slug `…/lechenie-alkogolnoy-zavisimosti/`): `/`, `/uslugi/`, `/uslugi/zavisimosti/`, alcohol leaf, `/o-centre/`, `/o-centre/programma-lecheniya/`, `/specyalisty/kostyuk|shipovsky|shapiguzova/`, `/blog/`, `/kontakty/`.  
No PHP warnings in sampled HTML. Evidence: `FRONTEND-QA.json`.

Viewport matrix (370–1440): CSS breakpoint contract ≤767 / ≥768 implemented; operator visual pass pending.

---

## 13. Admin QA

* Specialists: structured group live via PHP+JSON (`page_parent==1030`); data editable; gallery IDs present for Kostyuk
* Blog: reading-time RU label/instructions; manual + auto FE proven
* Typography source: Unicode NBSP (no literal entity spam in PHP sources)
* Full authenticated Admin click-through by operator still recommended

---

## 14. P07 Regression

**PASS** (sampled): `/uslugi/` Lorem **0**, `DEMO —` **0**; CTAs present; Hero hooks intact; no Hero fp02-nav bleed. Evidence: `P07-REGRESSION-AND-HERO.json`.

---

## 15. Source/Production Parity

```text
26/26 SOURCE ↔ PRODUCTION MATCH
```

(`deploy-manifest.json`)

---

## 16. WPilot

```text
write_enabled=false
```

Business writes: **0**. Option sample confirms `write_enabled;b:0`.

---

## 17. Remaining Migration Tails

Deferred unchanged (PROD-P06 / `.test` links / blogname / WP_DEBUG / HTTPS / sitemap / DNS / etc.).

---

## 18. Secret Safety

* exposed secrets: **0**
* tracked secrets: **0**

---

## 19. Git

* commit: none
* push: none
* foreign WIP: untouched

---

## 20. Acceptance

```text
PROD-P08 TECHNICAL CLOSEOUT COMPLETE — OPERATOR VISUAL ACCEPTANCE PENDING
```

---

## 21. Next Recommendation

1. Operator visual acceptance: mobile sliders (many/few slides), specialist pages, reading-time articles, non-Apple lifebuoy regression.
2. Operator Apple/WebKit physical QA for lifebuoy.
3. Optional follow-up: bounded live ACF/WYSIWYG typography residual (exact-object only).
4. Do **not** start PROD-P06 / migration-tail cleanup until explicitly chartered.

# WP Forge / FP-0002 knowledge harvest map

**Date:** 2026-08-18  
**Method:** problem → first implementation → failure → root cause → final implementation → reusable lesson → canonical rule → applicability → evidence.  
**Classification:** A–J as in [knowledge/README.md](README.md).

Client-specific values are omitted. Evidence paths are under `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/`.

---

## 1. WordPress content architecture

| Field | Value |
|-------|--------|
| Original problem | Mixed Pages, hardcoded FE, and later Admin parity needed a durable model |
| First implementation | Pages + ACF groups per template; specialists as child Pages of hub |
| Failure | Editor UX polluted by Generic Content / parent / page template; hub vs singles mixed |
| Root cause | Entity with independent lifecycle treated as nested static pages |
| Final | Pages for hubs/static; CPT `service` and `specialist`; options for globals; Reviews as options repeater (project choice) |
| Lesson | Choose primitive by lifecycle, URL, archive, Admin, search/sitemap — not by visual resemblance |
| Canonical rule | [CMS-ARCHITECTURE](../standards/FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md) · [CONTENT-MODEL-CPT-STANDARD](../standards/FORGE-WORDPRESS-CONTENT-MODEL-CPT-STANDARD-v1.md) · [REPEATER-VS-ENTITY](../standards/FORGE-WORDPRESS-REPEATER-VS-ENTITY-DECISION-MATRIX-v1.md) |
| Applicability | A (decision matrix); Reviews-as-options = J/I |
| Evidence | P11 report; V9 Admin-parity models in `DOCS/` |

## 2. CPTs

| Field | Value |
|-------|--------|
| Problem | Staff entities needed list columns, order, dedicated template, search group |
| First | Child pages under `#hub` |
| Failure | Generic page fields; `_wp_page_template` blocked `single-specialist.php` |
| Final | `specialist` CPT, `has_archive=false`, rewrite shares hub slug, IDs preserved |
| Lesson | Hub **page** + CPT **singles** can coexist; clear leftover page-template meta |
| Rule | CPT checklist in content-model standard |
| Class | A |
| Evidence | P11 |

## 3. ACF

| Field | Value |
|-------|--------|
| Problem | Hardcoded FE vs editor ownership |
| First | Large parity groups; some conditionals hid entire groups |
| Failure | Rewriting ACF `name` broke real wp-admin save (E51); opposite groups leaked |
| Final | Local JSON; location rules follow post type; hide unused metaboxes; keys preserved on migrate |
| Lesson | Test saves through real Admin POST, not only `acf_save_post` simulation |
| Rule | Existing FW-S-02 + Admin UX production addendum |
| Class | A |
| Evidence | E51-FIX02; P11 location change |

## 4. Site Settings

| Field | Value |
|-------|--------|
| Problem | Contacts duplicated across header, floating header, mobile, footer, contacts page |
| Final | One options SoT; consumers read helpers; empty fields do not render |
| Lesson | ONE ADMIN SOURCE OF TRUTH |
| Rule | [SITE-SETTINGS-STANDARD](../standards/FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md) |
| Class | A / E |
| Evidence | P13 socials; contacts helpers |

## 5. Admin UX

| Field | Value |
|-------|--------|
| Problem | Developer notices, English labels, raw Options, extra page fields |
| Final | Localized modules; hide irrelevant metaboxes; Site Settings sections; Dashboard widget; no raw debug screens for editors |
| Lesson | Editor-oriented, locale-first, grouped, dangerous controls Admin-only |
| Rule | [ADMIN-UX-STANDARD](../standards/FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) |
| Class | A / E |
| Evidence | P13; E53 admin CSS; P13-FU01 |

## 6. Frontend component architecture

| Field | Value |
|-------|--------|
| Problem | Theme templates + JS modules; operator CSS drift |
| Lesson | Canonize production CSS into source before next deploy; one JS owner per interaction |
| Rule | Authority + frontend standards |
| Class | C / F |
| Evidence | P09-FU01; P14 `v9-style.css` |

## 7. URL / permalink / slugs

| Field | Value |
|-------|--------|
| First | Custom slug metabox + sample permalink clone |
| Failure | Duplicate UI; `fp02_post_name` overwrote native `post_name`; Service missing native Edit |
| Final | Native `#edit-slug-box` only; data-layer uniqueness (`-copy-NN`); `post_type_link` honors `$leavename` |
| Lesson | Do not invent a second permalink editor |
| Rule | CPT standard + AP-002 |
| Class | A / G |
| Evidence | P12; P13-FU01 |

## 8. Search

| Field | Value |
|-------|--------|
| First | Native WP search (E62E) then Smart Search REST |
| Final | One endpoint, grouped results, Admin-configurable, desktop+mobile shared logic |
| Lesson | When post type changes, keep the **user-visible group name** stable |
| Rule | [SMART-SEARCH-MODULE-SPEC](../standards/FORGE-WORDPRESS-SMART-SEARCH-MODULE-SPEC-v1.md) |
| Class | B |
| Evidence | P09; P11 |

## 9. SEO

| Field | Value |
|-------|--------|
| Final | Per-entity title/description + fallbacks; verification/analytics empty → no output; advanced code gated |
| Lesson | Duplicate SEO plugins/owners forbidden; sitemap readiness ≠ robots open |
| Rule | [SEO-AND-SITEMAP-STANDARD](../standards/FORGE-WORDPRESS-SEO-AND-SITEMAP-STANDARD-v1.md) |
| Class | A / C |
| Evidence | P10; P13 |

## 10. Sitemap

| Field | Value |
|-------|--------|
| First | Core sitemap 404 while `blog_public=0` |
| Final | Extend `wp_sitemaps_*`; public types; exclusions; dynamic `home_url`/`get_permalink` |
| Failure avoided | Invented Yandex “page/service feed” |
| Rule | Prefer native extension; XML sitemap is the current Yandex model |
| Class | A / G |
| Evidence | P10 |

## 11. Social / contact settings

| Field | Value |
|-------|--------|
| First | Hardcoded links / free-text labels |
| Final | Platform type registry + URL + header/footer visibility + canonical icons |
| Lesson | TYPE owns label/icon; missing config → no empty control |
| Rule | [SOCIAL-CONTACT-MODULE-SPEC](../standards/FORGE-WORDPRESS-SOCIAL-CONTACT-MODULE-SPEC-v1.md) |
| Class | B / A (SoT rule) |
| Evidence | P13 |

## 12. Forms

| Field | Value |
|-------|--------|
| Final | One AJAX handler; nonce; timing/rate/duplicate; no PHP `mail()`; accept-without-send until SMTP |
| Lesson | Domain → SMTP → proven delivery → then indexing |
| Rule | [FORMS-AND-SMTP-STANDARD](../standards/FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) |
| Class | A / C / D |
| Evidence | P17-FU02; ConsultationHandler |

## 13. Email / SMTP sequencing

| Field | Value |
|-------|--------|
| Residue | Local MU `pre_wp_mail` labeled as local even on Beget |
| Final | Reclassified PRE-CUTOVER suppress; remove only in SMTP phase |
| Lesson | Do not send from temporary host as if final; do not open indexing first |
| Class | D |
| Evidence | P15; P17-FU02 |

## 14. Article / blog workflow

| Field | Value |
|-------|--------|
| Final | Posts + article template; reading time auto@WPM with manual override; SEO meta; TOC |
| Lesson | Archive page Admin must not duplicate post-owned fields |
| Class | A / E |
| Evidence | P08 reading time; P13; E61 |

## 15. DOCX importer

| Field | Value |
|-------|--------|
| Final | `.docx` only; multi-file; images; clean HTML; draft-first; template download; temp cleanup |
| Lesson | Human review + schedule; never auto-publish |
| Rule | [DOCX-IMPORTER-MODULE-SPEC](../standards/FORGE-WORDPRESS-DOCX-IMPORTER-MODULE-SPEC-v1.md) |
| Class | B |
| Evidence | P13 |

## 16. TOC

| Field | Value |
|-------|--------|
| Final | Server-side from article-body **H2 only**; stable unique IDs; H3 ignored; hidden if none |
| Lesson | Assign IDs before typography filter (priority 5 vs 20) |
| Class | A / F |
| Evidence | P13; P16 |

## 17. Typography

| Field | Value |
|-------|--------|
| First | P08 source-string + specialist field write-time normalize; mass DB STOP |
| Final | P16 `RussianTypography` + `TypographyFilters` render-time, HTML text nodes, exclusions |
| Lesson | Stored mass rewrite is an anti-pattern; search must collapse NBSP |
| Rule | [TYPOGRAPHY-PIPELINE-STANDARD](../standards/FORGE-WORDPRESS-TYPOGRAPHY-PIPELINE-STANDARD-v1.md) |
| Class | A / G |
| Evidence | P08 PARTIAL; P16 PASS |

## 18. Navigation

| Field | Value |
|-------|--------|
| Final | Native WP menu; desktop L2 dropdown (`focus-within`); mobile accordion; parent link + separate expand; Escape; ARIA |
| Lesson | No proprietary duplicate menu model |
| Rule | [NAVIGATION-STANDARD](../standards/FORGE-WORDPRESS-NAVIGATION-STANDARD-v1.md) |
| Class | A / F |
| Evidence | P13 |

## 19. Responsive sliders

| Field | Value |
|-------|--------|
| Final | Shared attach helper; mobile prev/next ≤767; desktop dots; Hero excluded; Swiper `mousewheel.forceToAxis` / `releaseOnEdges` |
| Lesson | Trackpad horizontal vs vertical scroll must be explicit |
| Rule | [SLIDER-CAROUSEL-STANDARD](../standards/FORGE-WORDPRESS-SLIDER-CAROUSEL-STANDARD-v1.md) |
| Class | A / F / H |
| Evidence | P08; P13 |

## 20. Real-device Apple / iOS

| Field | Value |
|-------|--------|
| First | Windows/Android OK; Apple static |
| Failures | WebKit-safe transform; then compositor/contain/fixed; emulation PASS, iPhone FAIL |
| Final | Bounded iOS `top`/`left` + visualViewport fallback; one transform owner |
| Lesson | Chromium emulation is not iOS proof |
| Rule | [REAL-DEVICE-QA-STANDARD](../standards/FORGE-WORDPRESS-REAL-DEVICE-QA-STANDARD-v1.md) |
| Class | H / G |
| Evidence | P12; P13 FIX02 |

## 21. Activity / audit logging

| Field | Value |
|-------|--------|
| Final | Table `*_user_activity_log`; user/action/object/time; suppress autosave/revision; System user; filters; retention; no body/secrets |
| Class | B |
| Evidence | P12; P13 V2; P14 QA row cleanup |

## 22. System dashboard

| Field | Value |
|-------|--------|
| First | Global LOCAL MARS / env notices |
| Final | One widget «MetaCODE / Состояние системы»: project, environment, live domain, versions, WPilot, parity, backup, indexing, tails, last verification |
| Lesson | Operations info ≠ every-screen notice; **status UI is production state** — update in the same major wave (AP-021) |
| Class | A / E |
| Evidence | P13; P14; P17-FU02; P18B |

## 23. Localization / i18n

| Field | Value |
|-------|--------|
| First | Mixed EN Admin strings (D8-G PARTIAL) |
| Final | text domain, gettext, POT, ru_RU packs for theme+plugin |
| Lesson | i18n from module birth, not a late mass refactor |
| Rule | [I18N-STANDARD](../standards/FORGE-WORDPRESS-I18N-STANDARD-v1.md) |
| Class | A |
| Evidence | E39; P13 |

## 24. Migration

| Field | Value |
|-------|--------|
| Lesson | Operator full files+DB import can become live baseline; do not overwrite with older local DB |
| Class | D |
| Evidence | P01; P04-FU02 |

## 25. Source / runtime authority

| Field | Value |
|-------|--------|
| Final | Beget FS = live runtime; Beget DB = live content; MARS `WORDPRESS/` = code authority |
| Lesson | Intake + canonize operator drift before automated deploy |
| Rule | [SOURCE-RUNTIME-AUTHORITY](../runbooks/FORGE-WORDPRESS-SOURCE-RUNTIME-AUTHORITY-STANDARD-v1.md) |
| Class | C |
| Evidence | SOURCE-AUTHORITY.md; P14 |

## 26. Backups

| Field | Value |
|-------|--------|
| Evolution | Exact-file Layer B during UI waves; full files+DB at P14 / freeze / cutover |
| Lesson | Operator may authorize exact-file mode; that is not a policy change |
| Rule | [BACKUP-ROLLBACK-STANDARD](../runbooks/FORGE-WORDPRESS-BACKUP-ROLLBACK-STANDARD-v1.md) |
| Class | C |
| Evidence | P09 override; P14 full backup |

## 27. Rollback

| Field | Value |
|-------|--------|
| Pattern | Per-file SHA before/after + object snapshots for DB IDs |
| Class | C |
| Evidence | every PROD-P exact-file pack |

## 28. Production drift

| Field | Value |
|-------|--------|
| Examples | Operator CSS; `content-page.php`; ACF values |
| Lesson | Classify: canonize / revert / ignore; never blind source→runtime |
| Class | C |
| Evidence | P09-FU01; P14 |

## 29. Git

| Field | Value |
|-------|--------|
| Reality | Shared dirty monorepo; foreign WIP |
| Final | Clean worktree from origin; exact paths; secret scan; no add -A / reset / stash / clean |
| Rule | [GIT-SOP](../runbooks/FORGE-WORDPRESS-GIT-SOP-v1.md) |
| Class | C / G |
| Evidence | P14 onward checkpoints |

## 30. DNS

| Field | Value |
|-------|--------|
| Finding | Website on Beget temp host; zone still at registrar hosting; mail MX at registrar |
| Lesson | Inventory whole zone; NS cutover ≠ A-record cutover; do not break mail |
| Rule | [DNS-NS-CUTOVER-STANDARD](../runbooks/FORGE-WORDPRESS-DNS-NS-CUTOVER-STANDARD-v1.md) |
| Class | D / G |
| Evidence | P17 |

## 31. SSL

| Field | Value |
|-------|--------|
| Sequence | DNS answers correctly → issue cert → verify HTTP/HTTPS → then HTTPS redirects → then WP home/siteurl |
| Class | D |
| Evidence | P17-FU02 SSL steps recorded, not executed |

## 32. Robots / indexing

| Field | Value |
|-------|--------|
| Final | `blog_public=0` + Disallow + meta noindex until **explicit human OPEN**; one SET SITE INDEXABILITY owner |
| Lesson | Sitemap may work while indexing stays closed; never auto-open on deploy |
| Class | D / G (AP-015) |
| Evidence | P10; P15; P17-FU02; P18B |
| Rule | [SEARCH-INDEXING-CONTROL](../standards/FORGE-WORDPRESS-SEARCH-INDEXING-CONTROL-STANDARD-v1.md) |

## 33. Launch / cutover

| Field | Value |
|-------|--------|
| Sequence | freeze → fresh full backup → parity → NS → auth DNS → SSL → home/siteurl → URL migrate → rewrite/cache → smoke (index closed) → SMTP → forms → robots → sitemap submit → crawl |
| Rule | [PRE-CUTOVER-AND-LAUNCH-SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md) |
| Class | D |
| Evidence | OPEN-ITEMS after P17-FU02 |

## 34. Security / hygiene

| Field | Value |
|-------|--------|
| Incident | GET on leftover `populate-*.php` created pages/menus |
| Lesson | Never leave migration PHP in public webroot; never probe unknown mutators with GET |
| Rule | [PUBLIC-WEBROOT-HYGIENE-GATE](../standards/FORGE-WORDPRESS-PUBLIC-WEBROOT-HYGIENE-GATE-v1.md) |
| Class | G / C |
| Evidence | P17-FU02 MARS-RUNTIME-RESOLUTION |

## 35. WPilot integration

| Field | Value |
|-------|--------|
| Final | Authenticated READ proven; write_enabled=false; token gitignored; Dashboard shows status; option version ≠ file version without verify |
| Rule | [WPILOT-PRODUCTION-STANDARD](../runbooks/FORGE-WORDPRESS-WPILOT-PRODUCTION-STANDARD-v1.md) |
| Class | C |
| Evidence | P05-FU01; P13 dashboard |

---

*Harvest map v1 — 35 areas. Promote via standards/runbooks, not by citing this map alone.*

# REPORT — FP-0002 V9-06E62C O-centre, Service Admin, Stable Review Anchors and Final Regression

**Date:** 2026-07-17  
**Runtime:** `http://shpigovsky.test/`  
**Database:** `mars_wp_fp0002`  
**Evidence:** `REPORTS/evidence/v9-06e62c-ocentre-service-admin-review-anchor-final-regression/`  
**Backup:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e62c-before-ocentre-service-admin-review-anchor-final-regression-20260717-164734`

---

## 1. Status

| Item | Result |
|------|--------|
| Overall | **PASS** (local validation) |
| Operator review | **pending** |
| DB writes | **yes** (O-centre bullet seed if empty; 30× `review_uid`; reversible reorder test restored) |
| Commit / push / freeze | **no** |

---

## 2. Pre-Change Backup

| Item | Value |
|------|-------|
| Path | `…\v9-06e62c-before-ocentre-service-admin-review-anchor-final-regression-20260717-164734` |
| DB dump | `db/mars_wp_fp0002.sql` — 6 719 780 bytes — SHA256 `4765B742…D2AB3A` |
| Validation | **PASS** (`CREATE TABLE` + `INSERT`; `--no-tablespaces`; `BACKUP-OK.txt`) |
| Hashes / manifest | `hashes.csv`, `operator-change-manifest.csv`, `reviews-items-export.json`, `BACKUP-INFO.md` |

---

## 3. Latest Operator Changes Canonized

| Item | Detail |
|------|--------|
| Pre-wave theme drift | **0** (php/css/js source = runtime) |
| Pre-wave plugin drift | **0** |
| CSS promote | **None required** — protected `v9-style` hash **`18114D3CBC98…`** preserved (operator crumbs 16/22, lifebuoy, prior E62B additives) |
| Templates / HTML | No runtime-only operator HTML drift |
| ACF JSON | 8 historical source-only groups **not** broadly synced; **reviews** JSON delivered; structured/relationships JSON `active:false` in **source only** |
| Unresolved drift | 8 source-only ACF groups remain outside runtime (intentional) |

Evidence: `operator-diff-inventory.csv`.

---

## 4. O-centre Infrastructure Changes

| Item | Detail |
|------|--------|
| Lead without span | `<p class="infrastructure-narrative__lead block-whith-red-line">Text</p>` — **no** inner `<span>` |
| New bullet | Immediately after lead: `<p class="infrastructure-narrative__bullet"><span>…</span></p>` |
| ACF field | `infrastructure_narrative_bullet_intro` — label «Дополнительный текст после вводного блока» (textarea) on O-centre hub group / page `#11` |
| Seed | Operator seed text written **only because field was empty** |
| Template | `template-parts/institutional/infrastructure-narrative.php` |
| Helper | `shpigovsky_get_about_infrastructure_context()` reads new field into `g0.bullet_intro` |
| Admin proof | Admin HTML dump `admin-html-ocentre-11.html` contains field label; screenshot `admin-screenshots/admin-html-ocentre-11.png` |

DOM: `ocentre-infrastructure-intro-dom-after.html`.

---

## 5. O-centre Previous Changes Validation

| Check | Result |
|-------|--------|
| `#o-centre-cta-1` absent | **PASS** |
| `#who-we-treat .services-category-section-v2__gallery` absent | **PASS** |
| `.program-cta-band` after body | **PASS** (inside `#who-we-treat` container after `__body`) |
| Home-equivalent blocks (team / advantages / territory) | **PASS** (content markers present) |
| Red-line lead editable | **PASS** (G0 text from ACF/static; no span) |
| New bullet editable | **PASS** |
| Span wrappers only where intended | **PASS** (lead no span; bullets keep span) |
| Duplicate IDs / sections | **PASS** (`#who-we-treat`, `#our-home` unique) |

---

## 6. Nested CTA Audit

| Item | Detail |
|------|--------|
| Previous DOM | `#who-we-treat` `<section>` contained nested `<section class="program-cta-band-section">` via `wrap_section=true` |
| Issue | Invalid/confusing nested section + duplicate heading ownership risk |
| Final DOM | `<div class="program-cta-band">` inside `#who-we-treat` (`wrap_section=false` only for `o-centre-who-we-treat-cta`) |
| Affected routes | `/o-centre/` who-we-treat band only |
| Other CTAs | Guest CTA / Blog / Service default wrappers **unchanged** |
| Regression | Nested `<section class="program-cta-band-section">` inside who-we-treat: **absent**; visual band present |

Evidence: `nested-cta-audit.md`, `ocentre-who-we-treat-dom-after.html`, `who-we-treat-before.php`.

---

## 7. Service Admin Cleanup

| Item | Detail |
|------|--------|
| Group keys | `group_fp02_service_structured_sections`, `group_fp02_service_relationships` |
| Labels | Service — Structured Sections; Service — Relationships / Related Services |
| Registration | Groups remain registered for field-key/frontend compatibility; **`active => false`**; filter always hides both on Service CPT edit (all roles) |
| Comment | `Hidden from Service admin by operator request in V9-06E62C; data retained for rollback/frontend compatibility.` |
| Data retained | **yes** — no postmeta delete |
| Frontend | helpers still read `intro_text` / `signs_items` / `cta_*` / `manual_related_services` as before |
| ACF JSON | Source-only JSON set `active:false` (not delivered to runtime; PHP local groups govern runtime) |
| Admin proof | `#74` / `#73` admin HTML: structured/relationships titles **absent** |

---

## 8. Stable Review UID Model

| Item | Detail |
|------|--------|
| Field | `review_uid` — «Постоянный ID отзыва» (text, admin readonly) |
| Format | `review-xxxxxxxx` (8 hex) |
| Generation | `shpigovsky_generate_review_uid()` — random_bytes; uniqueness vs existing set |
| Migration | `shpigovsky_ensure_review_uids()` — idempotent; assigned **30**, preserved **0** on first run |
| Uniqueness | **30/30** unique |
| Duplicate-row | Save hook re-runs ensure; empty/duplicate UIDs get new IDs |
| Reorder | UID unchanged when row moved; page number recalculated from current index |

Evidence: `review-uid-migration-matrix.csv`, `reorder-stability-test.json`.

---

## 9. Review Links and Pagination

| Item | Detail |
|------|--------|
| Anchor | `id="{review_uid}"` on archive cards |
| Slider target | `/otzyvy/` or `/otzyvy/page/N/#{review_uid}` via `shpigovsky_get_review_archive_url( $uid )` |
| Page calc | `floor(index / reviews_per_page) + 1` (request-cached map) |
| Page 1/2/3 | 10 UIDs each; total 30 unique anchors |
| Slider | Home: **10** full-review links with stable hashes (incl. page/2 targets) |
| Legacy index IDs | Not emitted as public anchors (no duplicate `id="review-N"`) |

Evidence: `slider-destination-matrix.csv`, `review-anchor-page1.txt`.

---

## 10. Database Changes

| Scope | Action |
|-------|--------|
| `infrastructure_narrative_bullet_intro` on page `#11` | Seed if empty (seed performed) |
| `reviews_items[*].review_uid` on `fp02-reviews` | Assign 30 UIDs |
| Reorder test | Move index 9 → end (page 1→3), verify UID, **restore** accepted order |
| Unrelated writes | **none** (no demo delete; no Service meta delete) |

Evidence: `db-writes.json`.

---

## 11. Exact Files Changed

### Source (canonical)

- `WORDPRESS/theme/shpigovsky/template-parts/institutional/infrastructure-narrative.php`
- `WORDPRESS/theme/shpigovsky/template-parts/institutional/who-we-treat.php`
- `WORDPRESS/theme/shpigovsky/inc/institutional-helpers.php`
- `WORDPRESS/theme/shpigovsky/inc/reviews-helpers.php`
- `WORDPRESS/theme/shpigovsky/template-parts/components/review-archive-card.php`
- `WORDPRESS/theme/shpigovsky/template-parts/reviews/archive-list.php`
- `WORDPRESS/theme/shpigovsky/template-parts/shared/reviews-slider.php`
- `WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php`
- `WORDPRESS/acf-json/group_fp02_site_options_reviews.json` (**delivered**)
- `WORDPRESS/acf-json/group_fp02_page_ocentre_hub.json` (source authority only; not runtime-synced)
- `WORDPRESS/acf-json/group_fp02_service_structured_sections.json` (source only; `active:false`)
- `WORDPRESS/acf-json/group_fp02_service_relationships.json` (source only; `active:false`)
- `PROJECT-STATUS.md`, this report, evidence, docs below

### Runtime (exact delivery)

- Matching theme/plugin files listed above + `wp-content/acf-json/group_fp02_site_options_reviews.json`

### Reports / evidence

- `REPORTS/REPORT-FP-0002-V9-06E62C-ocentre-service-admin-review-anchor-final-regression.md`
- `REPORTS/evidence/v9-06e62c-ocentre-service-admin-review-anchor-final-regression/**`

---

## 12. Source-to-Runtime Delivery

| Item | Result |
|------|--------|
| Exact files only | **yes** |
| Broad sync | **no** |
| Operator CSS preserved | `v9-style` `18114D3CBC98…` source=runtime |
| Hash parity | All delivered product files **MATCH** (`source-runtime-parity-final.csv`) |

---

## 13. Full Viewport Validation

64 screenshots — 16 routes × 4 viewports (1440×900, 1024×768, 480×900, 370×812) — **all PASS** (file size &gt; 1 KB).

Routes: `/`, `/uslugi/`, section, individual service, `/o-centre/`, gallery, `/specyalisty/`, specialist child, `/kontakty/`, `/blog/`, `/blog/page/2/`, blog single, `/otzyvy/` + pages 2–3, 404.

Evidence: `viewport-screenshot-matrix.csv`, `screenshots/`.

---

## 14. Admin Validation

| Screen | Result |
|--------|--------|
| Site Settings breadcrumbs | Fields present in admin HTML |
| Contacts `#20` | HTML dump + screenshot |
| Blog archive `#19` | HTML dump + screenshot |
| Founder reusable | HTML dump + screenshot |
| Reviews repeater | `review_uid` label present |
| O-centre `#11` | bullet intro label present |
| Service `#74` / section `#73` | Structured + Relationships groups **hidden** |

Evidence: `admin-validation-matrix.json`, `admin-screenshots/`, `admin-html-*.html`.

---

## 15. Deep Regression

| Area | Result |
|------|--------|
| Header / footer | Present on probed routes |
| Forms | Present |
| Tel links / masks | Present |
| Yandex maps | Present on Contacts |
| Lifebuoy | Present |
| Canonical tags | 1 on probed pages |
| PHP warnings in HTML | **0** |
| Review slider links | Stable UID anchors |
| Reviews/Blog pagination | HTTP expected statuses |
| Horizontal overflow | Visual screenshots captured; no automated overflow engine in this wave (**SAFE UNKNOWN** for pixel-level overflow measure) |
| JS console errors | Not instrumented without browser CDP (**SAFE UNKNOWN**; no PHP/HTML fatals) |

Evidence: `deep-regression-matrix.csv`, route/screenshot matrices.

---

## 16. Closed Tails

- Nested CTA who-we-treat fix  
- O-centre lead/bullet + E61 structure validation  
- Service ACF admin hide (structured + relationships)  
- Stable review UIDs + slider/archive links  
- Viewport screenshot pack  
- Admin HTML/screenshot evidence  
- Deep regression content matrix  

---

## 17. Remaining Tails

- Operator visual review (FE + admin)  
- Demo Blog/Reviews production cleanup decision  
- Source-only ACF groups outside scope (6 remaining historical)  
- Final freeze / commit / push (explicit charter)  
- Optional: JS console + overflow automation pack  

---

## 18. Demo Content Inventory

| Kind | Count | IDs / markers | Purpose |
|------|-------|---------------|---------|
| Demo Blog posts | 10 | `#1745–1754` (`demo-pagination-article-01`…`10`) | Pagination / thumb demos |
| Demo Reviews | 20 of 30 rows | `is_demo` / E62B markers in matrix | Pagination / clamp / slider demos |

**Do not delete in this wave.** Future cleanup: backup → trash demo posts → remove demo repeater rows → re-check page counts. See `demo-content-inventory.json` and `DOCS/DEMO-CONTENT-CLEANUP-BACKLOG-v1.md`.

---

## 19. Risks and SAFE UNKNOWN

| Topic | Note |
|-------|------|
| ACF repeater scaling | UID ensure on save; large repeaters still full rewrite on reorder |
| Admin duplicate-row UID | Relies on save hook; untested UI “Duplicate row” click path beyond ensure logic |
| Source-only ACF groups | Still not in runtime JSON; PHP local registration remains SoT for active groups |
| Production SEO/indexing | Local site `noindex` policy unchanged |
| Overflow / JS console | Screenshot-based; no CDP metrics |

---

## 20. Git Status

- **No commit**  
- **No push**  
- Exact FP-0002 paths only  
- Foreign monorepo WIP untouched  

---

## 21. Operator Review Pages

### Frontend

- http://shpigovsky.test/o-centre/ (infra lead + new bullet + who-we-treat CTA div)  
- http://shpigovsky.test/  
- http://shpigovsky.test/otzyvy/ , `/page/2/`, `/page/3/`  
- http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/  
- http://shpigovsky.test/blog/ , `/page/2/`  
- http://shpigovsky.test/kontakty/  
- http://shpigovsky.test/specyalisty/kostyuk/  
- http://shpigovsky.test/this-route-should-404-e62c/  

### Admin

- Service edit `#74` / `#73` — confirm Structured Sections + Relationships absent  
- O-centre page `#11` — new bullet field  
- Reviews options (`fp02-reviews`) — `review_uid` per row  
- Site Settings general — breadcrumbs  
- Contacts `#20`, Blog `#19`, Founder quote block  

**Do not commit, push, or freeze.**

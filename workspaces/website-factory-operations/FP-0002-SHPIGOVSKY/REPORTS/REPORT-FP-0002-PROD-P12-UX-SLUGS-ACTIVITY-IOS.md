# REPORT — FP-0002 PROD-P12 UX / Slugs / Activity Log / iOS Lifebuoy

**Date:** 2026-08-16  
**Host:** http://shpigovsky.beget.tech/  
**Docroot:** `/home/s/shpigovsky/shpigovsky.ru/public_html`  
**Evidence:** `REPORTS/evidence/prod-p12-ux-slugs-log-ios/`  
**Rollback:** `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p12-layer-b-pre\` + `...\prod-p12-db-snapshots\`

---

## 1. Status

- **PASS / PARTIAL** (physical iPhone acceptance pending)
- Production file writes: **YES** (exact 11 files)
- DB/schema writes: **YES** — table `fp02_user_activity_log` + option `fp02_activity_log_db_version=1` (bounded)
- ACF mutations: **0**
- WPilot writes: **0** (`write_enabled=false`)
- Commit/push: **none**

`PROD-P12 TECHNICAL CLOSEOUT COMPLETE — OPERATOR/OLYA VISUAL + PHYSICAL IPHONE ACCEPTANCE PENDING`

---

## 2. Fresh Production Intake

- Operator file drift found: **YES**
- Exact files: `theme/assets/css/v9-style.css` (1-byte trailing drift vs pre-P12 local)
- Canonized: **YES** (production → source, then additive phone-note selectors)
- Lifebuoy CSS/JS / CTA PHP / CPT PHP: matched at intake (no unexpected drift)
- Olya current content preserved: **YES**

`OPERATOR/OLYA CURRENT PRODUCTION STATE PRESERVED`  
`OPERATOR PRODUCTION FILE DRIFT INTAKE COMPLETE`  
`OPERATOR CSS/FILE DRIFT PRESERVED AND CANONIZED`

---

## 3. Backup / Rollback

- Operator fresh Beget backup: **ACKNOWLEDGED** (operator-provided pre-P12 full backup)
- Exact file snapshots: `prod-p12-layer-b-pre/`
- Exact DB snapshots: nature postmeta `#73` dump + activity table schema dump
- Rollback ready: **YES**

`PROD-P12 EXACT-FILE / EXACT-OBJECT ROLLBACK READY`

---

## 4. Services CTA

- Owner: `program-cta-band.php` + hub callers (`rehabilitation-program.php`, `services-hub.php`)
- Root cause of missing copy on `/uslugi/`: hub forced `phone_hint => ''`
- Markup: `<span class="program-cta-band__phone-note">Или позвоните нам</span>` under phone link
- Responsive: existing wrap02 column styles extended to `.program-cta-band__phone-note`

`SERVICES PROGRAM PHONE NOTE = LIVE`

---

## 5. Custom Entity Slug Inventory

See `evidence/.../CPT-SLUG-INVENTORY.md`.

| Entity | Class | Editable slug |
|--------|-------|---------------|
| `service` | A | YES (P12) |
| `specialist` | A | YES (P12) |
| Reviews options | B/C | N/A (no CPT permalink) |
| `page` / `post` | D | native |

---

## 6. Editable URL/Slug UX

- Module: `PermalinkSlugUX`
- Autogeneration: WP `sanitize_title` from title
- Manual editing: Admin metabox **URL / ярлык** → `post_name`
- Clear-and-regenerate: empty → from title
- Collision: `-copy-01` … (including drafts via `wp_insert_post_data`)
- Existing URLs: untouched (sample IDs 73/74/75/77/78 unchanged)

`PUBLIC CUSTOM ENTITIES HAVE EDITABLE WORDPRESS-NATIVE SLUGS`

---

## 7. Slug QA

- Duplicate title/slug → `fp02-p12-collision-qa` + `fp02-p12-collision-qa-copy-01`
- Manual edit → `fp02-p12-qa-manual-slug`
- Regenerate from title → works
- QA drafts hard-deleted
- Existing production URLs unchanged: **YES**

---

## 8. Dependence Demo Fallback

- Root cause: empty Admin repeater + legacy neurobiology/genotyping metas still rendered
- Changed owner: `shpigovsky_get_section_nature_text_blocks()` → repeater only
- Legacy metas retained dormant (not deleted)
- `/uslugi/zavisimosti/`: nature subsections empty of demo
- `/uslugi/psihicheskoe-zdorovie/`: real Admin rows still show

`DEPENDENCE NATURE TEXT BLOCKS = ADMIN DATA ONLY, NO DEMO FRONTEND FALLBACK`

---

## 9. Activity Log

- Architecture: FP-0002 module `ActivityLog`
- Table: `fp02_user_activity_log`
- Events: created / updated (+ trashed / restored)
- Types: page, post, service, specialist
- Autosave/revision suppressed; in-request de-dupe
- Retention: 8000 newest rows
- Admin: **Журнал действий**, capability `manage_options`

`BASIC WORDPRESS USER ACTIVITY LOG LIVE`

---

## 10. Activity Log QA

- Create events logged for QA drafts
- Update event logged (single de-duped update in request)
- Autosave not used in probe (WP autosave path skipped by guards)
- Admin table rows proven via DB select in probe JSON

---

## 11. iOS Lifebuoy Root Cause

See `LIFEBUOY-IOS-ROOT-CAUSE.md`.

Primary bounded causes: `contain: layout paint size` on fixed root + transform on `<img>` + `%`/`vh` transform units under iOS compositor/scroll; operator CSS not the override source.

`IOS LIFEBUOY ROOT-CAUSE ANALYSIS COMPLETE`

---

## 12. iOS Lifebuoy Fix

- JS owner: mover element transform (px-based `translate3d` + scale + rotate)
- CSS owner: positioning/size/opacity only; image not transform-animated
- Scroll: robust Y fallbacks + touchmove → rAF
- Reduced motion: preserved (`t=0.28`)

`LIFEBUOY TRANSFORM OWNERSHIP = SINGLE AND PROVEN`  
`WEBKIT/IOS-SAFE LIFEBUOY SCROLL ANIMATION IMPLEMENTED`

---

## 13. iOS QA

- Static/WebKit-safe implementation: **PASS**
- Emulation/desktop FE presence of mover+JS: **PASS**
- Physical iPhone: **OPERATOR/OLYA PENDING**

`PHYSICAL IPHONE QA = OPERATOR/OLYA PENDING`

---

## 14. Exact Files Changed (deployed)

Theme:

1. `assets/css/v9-style.css`
2. `assets/css/fp02-lifebuoy-parallax.css`
3. `assets/js/fp02-lifebuoy-parallax.js`
4. `template-parts/layout/body-start.php`
5. `template-parts/components/program-cta-band.php`
6. `template-parts/services-hub/rehabilitation-program.php`
7. `page-templates/services-hub.php`
8. `inc/service-section-helpers.php`

Plugin:

9. `src/ModuleRegistry.php`
10. `src/Admin/PermalinkSlugUX.php` *(new)*
11. `src/Admin/ActivityLog.php` *(new)*

Docs/reports/evidence under FP-0002 `REPORTS/` + `PROJECT-STATUS.md`.

---

## 15. Exact DB/Schema Objects Changed

- Created table `fp02_user_activity_log`
- Option `fp02_activity_log_db_version` = `1`
- Transient QA drafts created+deleted (no leftover public content)
- Activity QA rows retained as audit snapshots for deleted QA object IDs
- **No** Olya content postmeta overwrite; nature legacy metas untouched

---

## 16. Source / Production Parity

`11/11 SOURCE ↔ PRODUCTION MATCH` (`DEPLOY-MANIFEST.json`)

---

## 17. Regression

Smoke markers PASS for homepage/uslugi/zavisimosti/psi/alcohol/specialists surfaces checked: no PHP fatals; lifebuoy mover present; CTA note live; nature demo removed on `#73`; Smart Search/SEO/Fancybox code paths not mutated this wave (no regressions introduced by file set).

---

## 18. WPilot

- `write_enabled=false`
- Business writes: **0**

---

## 19. Secret Safety

- Exposed: **0**
- Tracked: **0**

---

## 20. Git

- Commit: **none**
- Push: **none**
- Foreign WIP: **untouched**

---

## 21. Deferred Plan Items

- Olya final visual check
- Physical iPhone lifebuoy acceptance
- Fresh final backup after acceptance
- Git checkpoint
- P06 migration/environment cleanup
- SEO title/meta-description ownership
- Typography residual
- SMTP
- Pre-cutover audit
- Final domain/SSL
- Robots/indexing opening
- Sitemap submission to Yandex/Google after cutover

---

## 22. Acceptance

`PROD-P12 TECHNICAL CLOSEOUT COMPLETE — OPERATOR/OLYA VISUAL + PHYSICAL IPHONE ACCEPTANCE PENDING`

---

## 23. Next Recommendation

1. Operator/Olya visual pass: `/uslugi/` CTA note; `/uslugi/zavisimosti/` nature without demo; Admin slug metabox; Журнал действий.
2. Physical iPhone Safari scroll check for lifebuoy motion.
3. After acceptance: fresh Beget backup + optional git checkpoint charter.
4. Do **not** auto-run DNS/SMTP/indexing/P06.

---

### Desired-state checklist

FP-0002 PROD-P12 COMPLETE — CURRENT OPERATOR/OLYA PRODUCTION CHANGES PRESERVED — SERVICES CTA COPY FIXED — ALL PUBLIC CUSTOM ENTITIES HAVE SAFE EDITABLE SLUGS WITHOUT REGENERATING EXISTING URLS — DEPENDENCE DEMO FALLBACK REMOVED — BASIC USER ACTIVITY LOG LIVE — LIFEBUOY IMPLEMENTATION REPAIRED FOR IOS/WEBKIT WITH PHYSICAL IPHONE ACCEPTANCE PENDING — SOURCE/PRODUCTION PARITY MAINTAINED

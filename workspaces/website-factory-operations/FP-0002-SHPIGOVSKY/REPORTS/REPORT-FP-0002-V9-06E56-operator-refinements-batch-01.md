# REPORT — FP-0002 V9-06E56 Operator Refinements Batch 01

**Date:** 2026-07-16  
**Project:** FP-0002 «Шпиговский»  
**Runtime:** http://shpigovsky.test/  
**Overall:** PARTIAL PASS — operator review pending  
**Commit / push / freeze:** none  

---

## 1. Overall Status

- **Verdict:** PARTIAL
- Operator review pending
- DB writes: footer option URL; attachment metadata for 3 images (+ legacy landscape #755); video attachment #1240 metadata; form AJAX tests used transients only (no lead CPT)
- No commit, no push, no freeze

## 2. Pre-Work Backup

- **Path:** `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e56-before-operator-refinements-batch-01-20260716-181633\`
- **DB dump:** `mars_wp_fp0002.sql` (~4 081 355 bytes) — predates E56 mutations
- **Marker:** `BACKUP-OK.txt` + `BACKUP-INFO.md` (after Web-GPT migration; after operator CSS/HTML; before V9-06E56; E53/E54/E55 baseline; operator protected)
- Includes: full runtime project, theme, plugin, ACF JSON, wp-config, operator-modified pre-merge copies, SHA256 manifest, drift inventory, Git HEAD/branch

## 3. Operator Manual Changes Preserved

- Theme diff inventory: 10 files (see evidence CSV)
- **Runtime promoted → source before E56 edits:** `v9-style.css`, `fp02-floating-header.css`, `v9-shell.js`, `floating-header.php`, `header.php`, three placeholder SVGs
- **Protected CSS baseline (operator runtime before E56 CSS tweak):** `D12B6348883FCF87418597B2756F47C2322C25B475B18268EB77308C30AF2D81`
- **After gallery wrapper CSS tweak:** `BC7AB371E1E1BE59F5ABCC3EE8CFA16138222DC391B410F7F29D64467875E931`
- Source-newer institutional PHP delivered to runtime (not operator): `clinic-landscape.php`, `founder-quote.php`
- ACF JSON source/runtime still has broader historical drift outside Comfort split (pre-existing; not blind-synced)
- Plugin core matched before wave; E56 form/comfort files delivered exact-hash

## 4. Footer OverSEO Link — PASS

- Option `fp02-block-footer_footer_credit_url` = `https://overseo.ru/`
- Template `footer.php`: `target="_blank"` + `rel="noopener noreferrer"`
- Visible text preserved: «Разработка и продвижение: Overseo»
- Validated on live Home HTML + screenshot `footer-overseo-link.png`

## 5. Theme Metadata and Screenshot — PASS

- `style.css` Theme Name preserved: Shpigovsky  
- Author: `Дягилева Ольга — Overseo`  
- Author URI: `https://overseo.ru/`  
- Description: Russian custom theme description for Shpigovsky rehab center / Olga Dyagileva / Overseo  
- Copyright comment: `Дягилева Ольга / Overseo`  
- Version preserved: `0.3.0-d7a-shell`  
- Theme URI left empty (no invented production URL)  
- Incoming `theme-screenshot.png` 1448×1086 → derivative `screenshot.png` 1200×900 in theme root (source + runtime), SHA256 `4606B073…`

## 6. Form System — PASS (local transport)

- Inventory: global modal `[data-lead-form][data-form-context=modal]`; final CTA `[data-form-context=final]`; all triggers open modal; no separate contacts AJAX form
- Shared architecture: theme JS (`v9-shell.js`) + plugin `ConsultationHandler` (`wp_ajax_fp02_lead_submit`)
- Triumph reference patterns used (nonce, honeypot `company_url`, min-fill, JSON, local accept) — branding not copied
- Local mode: validate + accept; **no** `wp_mail`/SMTP; success message states email disabled
- Future recipient constant only: `client.leads@polygon-ws.ru`
- Protection: WP nonce, honeypot, min-fill 3s, rate limit, duplicate token, sanitization, fixed recipient
- Test matrix (evidence CSV): SUCCESS 200, DUP 409, EMPTY_NAME 422, BAD_PHONE 422, NO_CONSENT 422, TOO_FAST 422, HONEYPOT 200 silent

## 7. Libertinus Serif — WAITING_FOR_OPERATOR_ASSET

- No Libertinus font files under FP-0002 INCOMING, theme `assets/fonts`, V9 workspace, or Storage search
- Local Inter `@font-face` pattern inspected; **Task D stopped** per charter (do not fetch CDN)
- Missing: local `Libertinus Serif` WOFF2 (weights actually used by `.hero__title` / `.services-inner-hero-v2__title`)

## 8. Image Replacements — PASS

| Incoming (PNG) | Attachment | File | Alt |
|---|---|---|---|
| `fp02-clinic-corridor.png` | #1709 | `shpigovsky-interior-corridor.webp` | Интерьер клиники — коридор с картинами |
| `fp02-rehabilitation-center-building.png` | #1239 (+ #755) | `shpigovsky-clinic-landscape-1.webp` (+ legacy landscape) | Здание и территория реабилитационного центра |
| `fp02-rehabilitation-center-team.png` | #1238 | `shpigovsky-staff-group.webp` | Команда специалистов реабилитационного центра |

- Method: convert PNG→WebP, replace upload originals, regenerate sizes via `wp_generate_attachment_metadata`
- Charter expected `.webp` names; operator delivered `.png` — used as-is
- Usage maps: postmeta section/service/home fields (evidence `image-usage-map-raw.txt`)

## 9. Home Video Repair — PASS

- **Root cause:** file was MPEG-TS (`0x47` sync) with `.mp4` extension / `video/mp4` MIME — browsers report unsupported format
- Working peer `#1242` `shpigovsky-center.mp4` is real `ftyp`/`isom` MP4
- Fix: ffmpeg remux/transcode → H.264 + AAC + `yuv420p` + `+faststart` (~25.5 MB)
- Updated: uploads attachment #1240, theme `assets/video/…` source+runtime
- Original backed up under E56 backup `media-video/`
- Size note: ~25 MB — do not commit blindly; Storage/policy decision deferred

## 10. Floating Header Max Button — PASS

- Data source: `shpigovsky_get_messenger_link_rows()` / `messenger-links.php` (same as header)
- Fix: added Max to desktop visual fallback in `site-chrome.php` (mobile/offcanvas already had Max)
- Floating header already rendered messengers partial; now includes Max icon `max.svg`
- Live HTML validated (TG + WA + Max in `.fp02-floating-header__messengers`)

## 11. Home Gallery Slider Alignment — PASS (already shared + CSS parity)

- Operator authority JS: articles uses `shpigovskyGallerySwiperOptions` (same as Home gallery)
- Settings: slidesPerView 4 / breakpoints 431→2.15, 768→3.15, 1025→3.5; spaceBetween 30/10/20/30; loop false; no autoplay; pagination dots; no arrows
- E56 CSS: `.home-gallery__wrapper{display:flex}` + slide `min-width:0` to match articles wrapper/card behavior
- Articles slider not redesigned

## 12. Comfort Admin Menu Split — PASS (storage preserved)

- Before: single `fp02-block-comfort` «Комфорт / преимущества» mixing intro + gallery + rehab requirements
- After menus: «Комфорт — вводный блок», «Комфорт — галерея», «Комфорт — требования»
- **Storage:** all new pages use `post_id = fp02-block-comfort` (no key migration)
- Legacy slug kept + redirected/hidden to intro
- ACF groups split: `group_fp02_block_comfort_{intro,gallery,requirements}`
- Option values preserved (evidence TSV)
- Frontend helpers still read `fp02-block-comfort`

## 13. Exact Files Changed

### Canonical source
- Theme: footer, site-chrome, style.css, screenshot.png, v9-style.css, v9-shell.js, modal, final-form, interview.mp4
- Plugin: ConsultationHandler.php, OptionsPage.php, FieldGroups.php, ModuleRegistry.php
- ACF JSON: three comfort split groups (old combined JSON removed)

### Runtime
- Matching exact-hash delivery for all above + uploads media (images/video)

### Reports/evidence
- `REPORTS/REPORT-FP-0002-V9-06E56-operator-refinements-batch-01.md`
- `REPORTS/evidence/v9-06e56-operator-refinements-batch-01/*`
- `PROJECT-STATUS.md` status line

## 14. Source-to-Runtime Delivery

- Exact-file only; no broad theme/plugin sync
- All listed changed files: source hash == runtime hash (evidence CSV)
- Protected CSS baseline recorded; gallery CSS tweak additive only

## 15. Validation

- Frontend routes 200: `/`, `/uslugi/`, `/o-centre/`, `/kontakty/`, `/blog/`
- Forms matrix PASS
- Images HTTP 200
- Video Content-Type `video/mp4`, `ftyp` magic
- Footer + Max HTML PASS
- Screenshots: home 1440/390, footer link; floating Max shot may be tiny if header still `aria-hidden` at capture time — HTML proof primary
- Admin comfort pages: structure delivered; operator should confirm visually in wp-admin

## 16. Risks and Tails

- Libertinus fonts missing (Task D waiting)
- Local mail transport disabled; SMTP deferred to production
- Large repaired video (~25 MB) persistence policy open
- Pre-existing ACF JSON drift outside Comfort not reconciled
- Floating Max screenshot automation weak when header hidden — manual scroll review recommended
- Incoming images were PNG not WebP filenames from charter

## 17. Git Status

- No commit, no push
- Work scoped to FP-0002 paths + Localhost runtime/backup
- Foreign WIP untouched

## 18. Operator Review Checklist

- [ ] Footer OverSEO link opens `https://overseo.ru/` in new tab
- [ ] Appearance → Themes card (metadata + screenshot)
- [ ] All form states (validation / loading / local success / errors)
- [ ] Hero font (blocked until Libertinus files provided)
- [ ] Three replaced images on Home / sections / services
- [ ] Home interview video playback + seek
- [ ] Max in floating header messengers
- [ ] Home gallery vs articles slide behavior
- [ ] Comfort admin submenu split + values intact

## Execution safety

- cwd: `X:\AI MARS`
- scope lock honored: yes (FP-0002 + MARS-Localhost shpigovsky)
- destructive ops: none (backups + exact replaces only)
- protected zone touch: none outside approved roots

# REPORT — FP-0002 V9-06E33 SERVICE IMAGE ADMIN BINDING, PLACEHOLDER FIX, USLUGI SLIDER

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | `X:` |
| Label | `AI WS` |
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `dc3c17736c235f6b4c81f6ac6acecdea5a8a5f68` |
| Staged files before | empty |
| WIP count only | ~680 short-status lines (foreign monorepo WIP present) |
| Runtime CSS canon detected | YES — runtime `v9-style.css` differed from source before task (`588DFEFA7A8D` vs `1EBE40FCCF5D`); additive CSS applied on runtime, then synced runtime→source |
| Commit allowed | NO — `STOP — REMOTE/HEAD MISMATCH` (`origin/mars/canonical-post-recovery`=`08803bd4…`) + unpushed MetaBOT commits + foreign WIP |
| Result | PASS — preflight OK; writes allowed; commit blocked by policy |

## 2. Backup

| Item | Value |
|---|---|
| Backup path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e33-service-images-uslugi-slider-before-20260713-012211\` |
| DB dump | `mars_wp_fp0002.sql` (2 932 201 bytes, `--no-tablespaces`, 14 tables) |
| Theme backup/hash | `theme-shpigovsky/` — pre-write hash `bf8cbb7b7ad2d7cc` (628 files) |
| Plugin backup/hash | `plugin-shpigovsky-core/` — `ff9ec81360085d70` (21 files) |
| ACF JSON backup/hash | `acf-json/` — `8a271b44ae85810b` (9 files) |
| Uploads/media manifest | `uploads-manifest.json` (57 files pre-write) |
| Service image inventory export | `inventory-before.json` + `binding-report.json` |
| `/uslugi/` snapshot | `uslugi-route-snapshot.html` (before) / `uslugi-route-snapshot-after.html` |
| Home gallery snapshot | `home-route-snapshot.html` (before) / `home-route-snapshot-after.html` |
| Result | PASS |

## 3. Pre-implementation audit

| Area | Finding |
|---|---|
| Service slider image field | ACF `service_slider_image` / label «Изображение для слайдера» (`field_fp02_service_slider_image`) in `group_fp02_service_layout_hero` + PHP `FieldGroups.php` |
| Frontend image source logic | `shpigovsky_get_service_image_or_placeholder()`: ACF slider → featured → hero_media → theme slug fallback map → placeholder |
| Real image mappings found | 6 theme-asset fallbacks: `internet-zavisimost`, `kompyuternaya-zavisimost`, `lechenie-opiumnoy-zavisimosti`, `hronicheskaya-ustalost`, `stress`, `nartsissizm` — all had empty admin field |
| Media Library attachment state | No prior attachments for those 6 webp files; created under `uploads/2026/07/` |
| Placeholder asset issue | `service-placeholder.svg` contained mojibake Cyrillic (`$>B> A:>@> 1C45B`) in `<text>` and `aria-label` (CP1251-as-UTF8 style corruption of «Фото скоро будет») |
| `/uslugi/` gallery source | `template-parts/services-hub/service-group.php` → `.services-category-section-v2__gallery` CSS grid (3 cols) |
| Existing slider JS/CSS | Home gallery uses Swiper via `[data-gallery-slider]` in `v9-shell.js` (front page only). Not reused for `/uslugi/` to avoid Home coupling; vanilla scroll-snap + controls added |
| Source/runtime differences | Only `v9-style.css` differed pre-task; other target files matched |

## 4. Service image binding

| Service ID | Service title | Old frontend image source | Attachment ID | Media URL | Field stored | Admin visible | Result |
|---:|---|---|---:|---|---|---|---|
| 1017 | Интернет-зависимость | theme `services-addictions-01.webp` | 1084 | `/wp-content/uploads/2026/07/services-addictions-01.webp` | 1084 | yes | BOUND |
| 1047 | Компьютерная зависимость | theme `services-addictions-02.webp` | 1085 | `/wp-content/uploads/2026/07/services-addictions-02.webp` | 1085 | yes | BOUND |
| 1048 | Лечение опиумной зависимости | theme `services-addictions-03.webp` | 1086 | `/wp-content/uploads/2026/07/services-addictions-03.webp` | 1086 | yes | BOUND |
| 1049 | Хроническая усталость | theme `services-mental-health-01.webp` | 1087 | `/wp-content/uploads/2026/07/services-mental-health-01.webp` | 1087 | yes | BOUND |
| 1050 | Стресс | theme `services-mental-health-02.webp` | 1088 | `/wp-content/uploads/2026/07/services-mental-health-02.webp` | 1088 | yes | BOUND |
| 1051 | Нарциссизм | theme `services-mental-health-03.webp` | 1089 | `/wp-content/uploads/2026/07/services-mental-health-03.webp` | 1089 | yes | BOUND |

Post-bind resolve source for the six above: `slider_image` (ACF first). Theme fallback map retained only as migration safety net.

## 5. Placeholder fix

| Item | Old | New | Result | Notes |
|---|---|---|---|---|
| Asset path | `assets/images/service-placeholder.svg` | same path | PASS | source + runtime synced |
| Encoding/text | Cyrillic text inside SVG → mojibake | ASCII `<title>Service image placeholder</title>`; geometric icon only | PASS | no Cyrillic in SVG |
| Frontend render | garbled caption text visible | clean grid + image icon | PASS | HTTP 200 |
| Broken/mojibake text | present | absent (`mojibake=false` on `/`, `/uslugi/`, SVG body) | PASS | |
| Alt/fallback meaning | — | HTML `alt` via helper: «Фото скоро будет» / service title | PASS | Russian outside SVG |

## 6. Admin image field instruction

| Field | Change | Required | Save behavior | Result |
|---|---|---|---|---|
| `service_slider_image` («Изображение для слайдера») | Instructions → `Опционально. Если изображение не выбрано, на сайте используется заглушка.` | 0 (unchanged) | optional image; no mandatory upload | PASS — PHP FieldGroups + ACF JSON updated |

## 7. `/uslugi/` slider implementation

| Requirement | Implementation | Result | Notes |
|---|---|---|---|
| Category-local sliders | Each `.services-category-section-v2__gallery[data-services-category-gallery]` initializes independently | PASS | 2 galleries on `/uslugi/` |
| Cards remain links | `.services-category-section-v2__gallery-link` preserved | PASS | |
| Multi-card support | flex track + scroll-snap; desktop ~3 visible; mobile ~85–92% width | PASS | controls when count > 1 |
| Mobile support | additive `@media` rules | PASS | |
| Controls/scroll behavior | prev/next buttons scroll by one card; track also swipe/scroll | PASS | 4 controls (2 galleries × 2) |
| Home gallery unaffected | Home still `[data-gallery-slider]` Swiper; separate IIFE | PASS | `home_slides=19`, `gallery_slider=true` |

## 8. Frontend validation

| Page | Check | Expected | Actual | Result |
|---|---|---|---|---|
| /uslugi/ | real images | visible | 6 `/uploads/2026/07/services-*.webp`; theme fallback URLs = 0 | PASS |
| /uslugi/ | placeholder | clean | 1 placeholder hit (service with no real image still in slider, e.g. narcotic); no mojibake | PASS |
| /uslugi/ | category card slider | works | `data-services-category-gallery`×2, tracks×2, controls×4 | PASS |
| / | Home gallery | unaffected | Swiper markup present | PASS |
| / | placeholder if needed | clean | no mojibake | PASS |

## 9. Admin validation

| Object | Field/check | Expected | Actual | Result |
|---|---|---|---|---|
| Компьютерная зависимость | slider image visible | yes | field ID 1085, URL uploads webp | PASS |
| Лечение опиумной зависимости | slider image visible | yes | field ID 1086 | PASS |
| No-image service | fallback instruction | yes | ID 1019 field empty; ACF instruction text present; resolve=`placeholder` | PASS |
| Service save | image not required | yes | `required=0` | PASS |

## 10. Regression validation

| Route | HTTP | Result | Notes |
|---|---:|---|---|
| / | 200 | PASS | no fatal |
| /uslugi/ | 200 | PASS | no fatal |
| /uslugi/zavisimosti/ | 200 | PASS | no fatal |
| /uslugi/psihicheskoe-zdorovie/ | 200 | PASS | no fatal |
| /uslugi/rasstroystva-pischevogo-povedeniya/ | 200 | PASS | no fatal |
| /o-centre/ | 200 | PASS | no fatal |
| /o-centre/programma-lecheniya/ | 200 | PASS | no fatal |
| /blog/ | 200 | PASS | no fatal |
| /kontakty/ | 200 | PASS | no fatal |

## 11. Source/runtime sync

| File | Source path | Runtime path | Hash match | Result |
|---|---|---|---|---|
| service-placeholder.svg | `WORDPRESS/theme/shpigovsky/assets/images/` | `wp-content/themes/shpigovsky/assets/images/` | YES | PASS |
| service-group.php | `WORDPRESS/theme/shpigovsky/template-parts/services-hub/` | same under runtime theme | YES | PASS |
| v9-style.css | `WORDPRESS/theme/shpigovsky/assets/css/` | runtime (canon after additive) | YES | PASS |
| v9-shell.js | `WORDPRESS/theme/shpigovsky/assets/js/` | runtime | YES | PASS |
| FieldGroups.php | `WORDPRESS/plugins/shpigovsky-core/src/Fields/` | runtime plugin | YES | PASS |
| group_fp02_service_layout_hero.json | `WORDPRESS/acf-json/` | `wp-content/acf-json/` | YES | PASS |

## 12. Git result

| Item | Value |
|---|---|
| Staged before | empty |
| Staged after | empty |
| Commit attempted | NO |
| Commit hash | — |
| Commit skipped reason | REMOTE/HEAD mismatch + 11 unpushed commits (MetaBOT docs) + large foreign WIP; policy forbids unsafe commit |
| Push attempted | NO |

## 13. Risk register

| Risk | Severity | Status | Recommended handling |
|---|---|---|---|
| Theme slug fallback map still in code | Low | Accepted | Keep as safety net; admin field is now primary for the 6 services |
| Service #314 (наркотическая) in `/uslugi/` slider with placeholder | Low | Known | Operator may attach real image later or hide from slider |
| Git cannot persist source changes yet | Medium | Open | Separate bounded commit persistence task after remote/WIP hygiene |
| ACF JSON vs live DB field group sync UI | Low | Mitigated | PHP `FieldGroups.php` registers instructions at runtime |

## 14. Final verdict

PASS

V9-06E33 Service Images / Placeholder / Uslugi Slider:
COMPLETE

Service image admin binding:
PASS

Placeholder fix:
PASS

Admin image instructions:
PASS

/uslugi/ category slider:
PASS

Home gallery unaffected:
PASS

Regression:
PASS

Source/runtime sync:
PASS

Operator CSS preserved:
PASS

Git commit:
SKIPPED

No foreign project work:
PASS

Recommended next phase:
OPERATOR_REVIEW_REQUIRED

## 15. Recommended next action

OPERATOR_REVIEW_REQUIRED

## 16. Final safety statement

Target folder:
X:\AI MARS

V9-06E33 Service Images / Placeholder / Uslugi Slider performed:
YES

DB writes:
12

Source changes:
YES

Runtime delivery:
YES

WordPress changes:
YES

Media Library changes:
YES

Backup created:
YES

Git mutation:
NO

Git commit:
NO

Git push:
NO

Reset:
NO

Rebase:
NO

Stash:
NO

Cleanup:
NO

Foreign project work:
NO

Operator runtime CSS preserved:
YES

FP-0002 product contaminated:
NO

WPilot confused with OCPilot:
NO

Secrets committed:
0

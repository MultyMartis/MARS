# REPORT — FP-0002 SERVICE CHILD-CARDS ADAPTIVE LAYOUT + DEFAULT SECTION TITLE 01

**Wave:** `prod-maint-service-child-cards-01`  
**Date:** 2026-09-13  
**Verdict:** **PASS_WITH_RESIDUALS**

## 1. Verdict

**PASS_WITH_RESIDUALS**

Residuals are non-blocking:
- No live service page currently stores an explicit non-empty `service_child_services_heading` override (cannot A/B a live custom title; code path still preserves non-empty meta).
- Wave worktree placed under `X:\AI MARS STORAGE\worktrees\` (MASTER-20C) instead of deprecated `X:\AI MARS\worktrees\`.

## 2. Current origin

| Role | SHA |
|------|-----|
| Start origin tip (fetched) | `9aa466b868fdb5d4f4aa717eb532feb09b14cd70` |
| Implementation commit | `29c5abbefb0b6da289320a08bca5a133cd350b4b` |
| Docs/closeout | `4d2f85b3c89d316782a6f4c5e95872e942e8600f` |
| Final canonical origin tip | `4d2f85b3c89d316782a6f4c5e95872e942e8600f` |

## 3. Fresh production intake

Evidence: `REPORTS/evidence/prod-maint-service-child-cards-01/`

- Pre-mutation hash compare: theme PHP/CSS **MATCH** production; ACF JSON **norm-LF MATCH** (CRLF-only raw drift).
- Target page `#314`: heading meta empty → default title was «Направления внутри услуги».
- Child shapes on `#314`: 5 cards; 1 image (soli); 1 description (lekarstva); 3 title-only.
- `blog_public=1`; robots meta `max-image-preview:large`; OG present; single JSON-LD block.
- Robots.txt snapshot before/after: **unchanged**.
- Layer-B rollback snapshots: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-maint-service-child-cards-01-layer-b-pre\`

## 4. Existing block architecture

Render chain (service stack only):

1. Service singular template stack includes `template-parts/service/child-services.php` (e.g. via `alcohol-direct-v9.php` / general service stack).
2. Gate: `shpigovsky_service_child_services_block_enabled()` + published children via `shpigovsky_get_service_children()` (`post_parent`, `menu_order ASC`).
3. Heading: `shpigovsky_get_service_child_services_heading()` ← ACF `service_child_services_heading` or code default.
4. Card text: `shpigovsky_get_service_mini_description()` / `service_short_description`.
5. Card image: `shpigovsky_get_service_child_card_image_url()` (`service_slider_image` → `hero_media` → featured image).
6. CSS: scoped `assets/css/service-child-services.css` enqueued only on singular `service` (non-placeholder).

Not this block: subdivision `children.php` (`services-category-section-v2`) used on section-role parents.

## 5. Data model

| Concern | Owner |
|---------|--------|
| Child ordering | WP `menu_order` ASC among published `service` children |
| Image | Child service media fields / thumbnail (no parent fallback invented) |
| Description | Child `service_short_description` via mini-description helper |
| Card title | Child post title |
| Section heading | ACF `service_child_services_heading` if non-empty; else theme default |

## 6. Final layout logic

Scoped BEM modifiers on `.service-child-services__card`:

| Case | Classes / behavior |
|------|--------------------|
| image + description | `--has-image --has-text`; may be featured if first-with-image |
| image + no description | `--has-image --compact`; featured candidate |
| no image + description | `--no-image --has-text`; natural height |
| no image + no description | `--no-image --compact`; ~title-only padding |

Grid uses `align-items: start` (no forced equal-height empty tiles). Featured grid modifier when applicable.

## 7. Featured-card rule

Deterministic: **first child in canonical `menu_order` that has a non-empty service-owned image URL**.  
If none → no featured card; text/compact grid only. No reordering, no random image, no parent-image fallback.

## 8. Default heading rule

Explicit non-empty Admin/ACF `service_child_services_heading` → use it.  
Otherwise → `Состояния, которые мы лечим`.  
No DB mass-update; placeholder/instructions updated in FieldGroups + ACF JSON only.

## 9. Files changed

Absolute paths (worktree / canonical locus under FP-0002):

- `...\FP-0002-SHPIGOVSKY\WORDPRESS\theme\shpigovsky\template-parts\service\child-services.php`
- `...\FP-0002-SHPIGOVSKY\WORDPRESS\theme\shpigovsky\assets\css\service-child-services.css`
- `...\FP-0002-SHPIGOVSKY\WORDPRESS\theme\shpigovsky\inc\service-helpers.php`
- `...\FP-0002-SHPIGOVSKY\WORDPRESS\plugins\shpigovsky-core\src\Fields\FieldGroups.php`
- `...\FP-0002-SHPIGOVSKY\WORDPRESS\acf-json\group_fp02_service_layout_hero.json`
- `...\FP-0002-SHPIGOVSKY\REPORTS\REPORT-FP-0002-SERVICE-CHILD-CARDS-ADAPTIVE-LAYOUT-01.md`
- `...\FP-0002-SHPIGOVSKY\PROJECT-STATUS.md`
- `...\FP-0002-SHPIGOVSKY\REPORTS\FP-0002-NEXT-WEBGPT-HANDOFF.md`
- Evidence under `...\REPORTS\evidence\prod-maint-service-child-cards-01\`

## 10. Desktop QA (~1440)

PASS — featured left (~575×412) + compact right stack; description card natural height; title-only ~56px; no horizontal overflow; heading default correct.

## 11. Tablet QA (~768)

PASS — featured full-width; remaining cards 2-column; no overflow.

## 12. Mobile QA (~390)

PASS — single column; featured full-width with image; compact title cards ~56px; no overflow.

## 13. Cross-page service QA

| Page | Shape |
|------|--------|
| `/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/` | mixed image/desc/compact; featured=1 |
| `/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/` | 5 compact title-only; no featured |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | block absent (no children) |
| Section parents (`/uslugi/zavisimosti/` etc.) | different subdivision children UI (untouched) |

## 14. Regression QA

Reviews marker present; lead modal hooks present; OG counts stable; JSON-LD count=1; no noindex; header/footer intact on sampled pages; specialists hub / blog / home unaffected (scoped CSS).

## 15. Robots / indexing safety

`robots.txt` before === after. `blog_public=1`. No robots/indexing mutation.

## 16. Production ↔ source parity

Exact-file deploy manifest: all 5 runtime files `parity=True` (`05-deploy-manifest.json`). After copies: `...\deployment-packs\fp-0002\prod-maint-service-child-cards-01-prod-after\`.

## 17. Backup / rollback

- Operator Beget backup: acknowledged (not used as editorial truth).
- Exact Layer-B file snapshots for all touched runtime files (paths above).
- No DB schema/editorial rewrite.

## 18. Git

Selective staging only; commit + push authorized; dirty shared main untouched.

## 19. Workspace cleanup

WAVE WORKTREE = REMOVED (`X:\AI MARS STORAGE\worktrees\fp0002-service-child-cards-layout-01`)  
WAVE BRANCH = REMOVED (`wave/fp0002-service-child-cards-layout-01`)  
UNPUSHED WAVE COMMITS = 0  
STAGED WAVE FILES = 0  
TEMP RESIDUE = 0 (wave helper scripts deleted before worktree remove)  
SHARED MAIN FOREIGN WIP = UNTOUCHED

## 20. Residuals

1. No live custom heading override specimen exists today.
2. Worktree path used Storage per MASTER-20C.

## 21. Mutation statement

- Exact production files changed: 5 (theme template, CSS, helpers, FieldGroups, ACF JSON).
- NO editorial content rewrite / NO mass ACF value overwrite.
- NO robots/indexing mutation.
- Foreign WIP on shared main preserved.

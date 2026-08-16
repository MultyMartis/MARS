# E64 Post-Cleanup Validation

## Source ↔ runtime

| Check | Result |
|-------|--------|
| `v9-style.css` SHA256 | `1CCC5A8F1150BC696186E0F8D4546B7D55A1895BFA3C77DD50A32204B09A7BA9` (matches Stable freeze marker) |
| Theme CSS/JS/admin-editor/search* parity | PASS (source == runtime) |
| Product files deleted by cleanup | **0** |
| ACF JSON / uploads / wp-config | Untouched |

Pre-existing dirty WORDPRESS paths in main git status are **foreign/uncommitted WIP relative to local HEAD**, not introduced by E64 deletions.

## Database

| Check | Result |
|-------|--------|
| Connect | OK |
| DB name | `mars_wp_fp0002` |
| Prefix | `fp02_` |
| Reviews items (`fp02-reviews_reviews_items`) | **30** |
| Unique `review_uid` | **30** |
| Blog publish posts | **16** (demo content retained) |
| Program short descriptions | `treatment_program_short_description` present (5) |
| O-centre page `#11` nonempty meta | **58** |
| DB writes by cleanup | **0** |

## Routes (`http://shpigovsky.test`)

All required smokes PASS — see `E64-ROUTE-SMOKE.csv`.

| Route | Status | PHP noise | v9 CSS | v9 JS |
|-------|--------|-----------|--------|-------|
| `/` | 200 | 0 | yes | yes |
| `/uslugi/` | 200 | 0 | yes | yes |
| one service | 200 | 0 | yes | yes |
| `/o-centre/` | 200 | 0 | yes | yes |
| `/kontakty/` | 200 | 0 | yes | yes |
| `/blog/` | 200 | 0 | yes | yes |
| `/blog/page/2/` | 200 | 0 | yes | yes |
| `/otzyvy/` | 200 | 0 | yes | yes |
| `/otzyvy/page/2/` | 200 | 0 | yes | yes |
| `/?s=` | 200 | 0 | yes | yes |
| search with results | 200 | 0 | yes | yes |
| invalid 404 | **404** | 0 | yes | yes |

Missing assets (enqueue check): **0** for CSS/JS markers above.

## Git safety

| Check | Result |
|-------|--------|
| Forbidden ops | None (`pull/reset/clean/stash/commit/push` not used) |
| Remote tip | Unchanged `9d5dcc28…` |
| Commit/push | **None** |
| SITE-002 worktree | Untouched |
| e29c worktree | Retained (manual review) |
| Staged index | Empty |

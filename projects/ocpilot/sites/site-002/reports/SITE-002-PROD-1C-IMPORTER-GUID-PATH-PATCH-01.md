# REPORT — SITE-002 1C Importer GUID Path Patch 01

**Operation:** `SITE-002-PROD-1C-IMPORTER-GUID-PATH-PATCH-01`  
**OCPilot run:** **4.297**  
**Date:** 2026-07-23 / 2026-07-24  
**Environment:** PRODUCTION_1C_IMPORTER_GUID_PATH_PATCH  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Runtime checkout:** `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-IMPORTER-GUID-PATH-PATCH-01\`

**Final verdict:** `SITE-002 1C IMPORTER GUID PATH PATCH COMPLETE — READY FOR POST-IMPORT PERSISTENCE CHECK`

**Classifications:**
- Importer patch: `IMPORTER_GUID_PATH_PATCH_DEPLOYED`
- Critical simulation: `CRITICAL_PRODUCTS_RESOLVE_CANONICAL`
- Next phase: `READY_FOR_POST_IMPORT_PERSISTENCE_CHECK`

---

## 1. Scope

Patch production 1C importer category resolution after Run **4.296** mapping backfill:

1. Resolve by GUID via `oc_mars_1c_category_map`.
2. Fallback to full path / path hash.
3. Collision guard vs legacy **154/159/165** / under **153** for tech tree.
4. Leaf-name auto-assign only when safe; otherwise `REVIEW_REQUIRED`.
5. Category auto-create **disabled** (Phase A).
6. Product update: do not blind-replace categories when unresolved — preserve existing relations.
7. Deploy exact importer files only. **No** live write import. **No** DB mutation.

## 2. Operator approval / GUID stability

- Operator approved importer patch after Run **4.296**.
- 1C group GUIDs treated as stable by operator / 1C process.
- GUID/path strategy accepted; goal = future automatic correct create/assign without leaf-name firefighting.

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `396f244d` (= `origin/mars/canonical-post-recovery`) |
| Origin includes mapping backfill `396f244d` | **yes** |
| Staged | empty |
| Untracked tools (authority) | 3 foreign verification `.py` — **not committed** |
| Dirty main | foreign WIP — **read-only**; **0 mutations** |
| Authority commit safety | **SAFE** |

Evidence: Storage `preflight/`.

## 4. Reports read / patch baseline

Runs **4.292–4.296** summarized in Storage `reports-read/`. Known risk: next import could reattach critical products to legacy **154/159/165** via leaf-name until this patch.

## 5. Importer locus / source before

Live FTP RETR confirmed:

| File | Remote | SHA256 before |
|------|--------|---------------|
| `import_1C.php` | `public_html/catalog/controller/common/import_1C.php` | `2a36d680…eb23` |
| `import_1C_process.php` | `public_html/catalog/controller/common/import_1C_process.php` | `865851e0…3864` |

Leaf-name collision behavior confirmed in live source. Locus gate: **PASS**.

## 6. DB read-only before

| Gate | Result |
|------|--------|
| `oc_mars_1c_category_map` exists | **yes** |
| Required active rows | **7/7** → 362/373/375/376/378/379/380 |
| Critical products | 4707/4708→378, 4710→379, 4712→380, 4709→376 |
| GATE | **PASS** |

## 7. Harness before

Prior XML used (live FTP `import0_1.xml` returned **550** — file absent/rotated). Critical products already canonical; old importer risk →154/159/165 still documented.

## 8. Design lock

Phase A:

1. GUID map → path hash → unique DB full path → safe leaf → else review  
2. Auto-create disabled  
3. Collision guard for tech path vs legacy leaves / under 153  
4. `import_1C_process.php` preserves relations on update when no group resolves  

Evidence: Storage `design/`.

## 9. Code patch

Repo mirrors (deployed as controller basenames):

- `projects/ocpilot/sites/site-002/tools/import_1C-site-002-prod-1c-importer-guid-path-patch-01.php`
- `projects/ocpilot/sites/site-002/tools/import_1C_process-site-002-prod-1c-importer-guid-path-patch-01.php`

Logs added: `MARS_CATEGORY_GUID_MATCH`, `MARS_CATEGORY_PATH_MATCH`, `MARS_CATEGORY_FULLPATH_DB_MATCH`, `MARS_CATEGORY_CREATE_DISABLED`, `MARS_CATEGORY_COLLISION_GUARD_BLOCKED`, `MARS_CATEGORY_REVIEW_REQUIRED`, `MARS_PRODUCT_CATEGORY_RESOLVED`.

## 10. Tests

| Check | Result |
|-------|--------|
| Remote `php -l` process patched | **PASS** |
| Remote `php -l` import patched | CLI errors — **same as live pre-patch** `import_1C.php` under PHP 5.6 CGI CLI (false negative for UTF-8 Cyrillic identifiers) |
| Structural brace balance | OK |
| Dry-run simulation | **PASS** 5/5 |

GATE: **PASS WITH NOTES** (CLI lint false negative accepted with live parity).

## 11. Dry-run simulation

| Product | Resolved | Method | Expected |
|---------|----------|--------|----------|
| 4707 / 4708 | **378** | GUID_MATCH | 378 |
| 4709 | **376** | GUID_MATCH | 376 |
| 4710 | **379** | GUID_MATCH | 379 |
| 4712 | **380** | GUID_MATCH | 380 |

Legacy **154/159/165** unused for tech GUIDs. Collision guard **3/3**. GATE: **PASS**.

## 12. Deploy backup

Exact pre-deploy bytes saved under Storage `deploy-backup/*.pre-guid-path-patch-01.bak` + rollback manifest.

## 13. Deploy

| Remote | SHA256 after | Match payload |
|--------|--------------|---------------|
| `…/import_1C.php` | `6448954d…2c0e` | **true** |
| `…/import_1C_process.php` | `fe9f8b81…c341` | **true** |

Status: **DEPLOYED**.

## 14. Cache actions

- `storage/cache` clear: **0**
- `storage/modification` clear: **0**
- OCMOD refresh: **0**

Reason: direct controller includes; not modification-wrapped.

## 15. DB read-only after

Mapping table unchanged (**7/7**). Critical products unchanged on **378/379/380/376**. GATE: **PASS**.

## 16. Harness after

Resolution simulation still canonical; collision guard active in code path; no live import run.

## 17. Public after

**11/11** checks HTTP 200; no «Товар не найден»; no PHP Notice/Warning/Fatal; no public `БЗПМ`. Sitemap `<loc>` = **1820**.

## 18. Monitor read-only

- Baseline still **1737** (not refreshed)
- Live sitemap **1820**
- Import not run; baseline not changed
- ONBOARDING_REQUIRED / artifact conflict may remain (expected)

## 19. Rollback plan

Restore the two `.pre-guid-path-patch-01.bak` files via FTP STOR to the same remote paths. No DB rollback required.

## 20. Regression

All scoped checks PASS: exact 2-file FTP only; DB/product/category/SEO/import/scheduler/baseline/cache/OCMOD/forms/dirty-main = **0** unintended mutations.

## 21. Production mutation summary

| Item | Result |
|------|--------|
| Source deploys: exact files | **yes** (2) |
| FTP writes: exact files | **yes** (2) |
| DB writes | **0** |
| Mapping table changes | **0** |
| Product/category relation changes | **0** |
| Category creates/updates/deletes/disables | **0** |
| SEO URL changes | **0** |
| Admin saves | **0** |
| Import runs | **0** |
| Scheduler changes | **0** |
| Monitor baseline changes | **0** |
| Cache clears | **0** |
| OCMOD refresh | **0** |
| Dirty main changes | **0** |

## 22. Git/worktree summary

- Authority worktree used for code/report/docs commit.
- Dirty main untouched.
- Foreign untracked tools excluded from commit.

## 23. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-IMPORTER-GUID-PATH-PATCH-01\` — all required phase folders populated.

## 24. SAFE UNKNOWN / blockers

- Live FTP `import0_1.xml` currently **550** (absent/rotated) — dry-run used prior Run 4.296 XML copy.
- CLI `php -l` on `import_1C.php` fails for both live pre-patch and patched files under PHP 5.6 CGI CLI — not used as hard deploy blocker given live parity + process lint PASS + dry-run PASS.
- Persistence after next natural 1C import: **not yet proven** (requires post-import check).

## 25. Final verdict

`SITE-002 1C IMPORTER GUID PATH PATCH COMPLETE — READY FOR POST-IMPORT PERSISTENCE CHECK`

## 26. Next recommendation

1. Observe next natural scheduled 1C import (do not force write import in this charter).
2. Run post-import persistence check: critical products must remain **378/379/380/376**; logs should show `MARS_CATEGORY_GUID_MATCH` / collision guard if leaf conflicts attempted.
3. After persistence proven: consider baseline refresh + optional broader mapping backfill + Phase B controlled auto-create.

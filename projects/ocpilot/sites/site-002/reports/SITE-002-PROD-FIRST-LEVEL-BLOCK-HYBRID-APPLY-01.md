# REPORT — SITE-002 First-Level Block Hybrid Apply 01

**Operation ID:** `SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01`  
**OCPilot Run:** **4.314**  
**Date:** 2026-07-28  
**Environment:** PRODUCTION (`https://bzpm.ru/`) — controlled FTP/code/cache apply  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01\`

**Verdict:** `SITE-002 FIRST-LEVEL BLOCK HYBRID APPLY COMPLETE — READY FOR OPERATOR VISUAL REVIEW`

**Classifications:**
- Apply: `HYBRID_FIRST_LEVEL_BLOCK_APPLY_COMPLETE`
- Monitor: `MONITOR_NOT_RUN_SITEMAP_UNCHANGED`
- Next: `READY_FOR_OPERATOR_VISUAL_REVIEW`
- Empty copy: `EMPTY_COPY_SUPPORTED_BUT_NOT_RENDERED_CURRENTLY`

---

## 1. Scope

Apply approved HYBRID Neutral first-level category block on **home** and **`/katalog/`** Catalog Section Tiles.

Show IDs: **80, 86, 207, 301, 322, 326, 331, 354, 358, 360**  
Hide/wait IDs: **82, 83, 85, 87, 89**  
Empty copy (future proven empties): `Ожидайте, товары скоро поступят.`

Out of scope / preserved: mega menu product gate, deep leaf global listing, Tech **362** behavior, sitemap/baseline/importer/products/categories, Client Ops, dirty main.

## 2. Operator approval

Operator approved HYBRID scope and authorized this separate apply after Run **4.313**.

## 3. Client Ops boundary

Client Ops Telegram Reports, reporting bridge, Telegram bot, n8n, Hub Gateway — **untouched**. Monitor artifacts read only as SITE-002 evidence.

## 4. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD (start) | `66789bcb` (= `origin/mars/canonical-post-recovery`) |
| Origin includes `66789bcb` | **yes** |
| Staged | empty |
| Unpushed | none |
| Foreign untracked tools (authority) | pre-existing `.py` — **not committed** |
| Dirty main | foreign WIP — **read-only**; **0 mutations** |
| Authority unsafe | **NO** |

Evidence: Storage `preflight/`.

## 5. Reports read / current state

| Source | Key fact |
|--------|----------|
| Run 4.312 | Baseline **1879**; checkpoint `…-1879-08`; monitor after **NO_ACTION_REQUIRED** |
| Run 4.313 | **HYBRID RECOMMENDED**; exact show/hide IDs; apply not yet executed |
| This task | Operator approved apply |

Evidence: Storage `reports-read/`.

## 6. Current state reconfirm

| Check | Result |
|-------|--------|
| Latest SUCCESS import | `mars_1c_import_2026-07-28_080011.txt` / `mars-20260728-080001-24823ddf` |
| Later failed supersede | **False** |
| Sitemap | HTTP **200**, count **1879** |
| Critical products 4707/4708/4709/4710/4712 | **5/5** HTTP 200, no «Товар не найден» |
| Hard gate | **PASS** |

Evidence: Storage `current-state/`.

## 7. DB read-only category control

| Control | Result |
|---------|--------|
| Show IDs exist / status=1 / store-linked / HTTP 200 | **True** (10/10) |
| Hide/wait IDs present | 5/5 |
| Hide/wait `oc_mars_1c_category_map` hits | **0** |
| Tech 362 + 5 children | **6/6** present |
| Deleted 153–170 in DB | **none** |

Evidence: Storage `db-readonly/`.

## 8. Public before

Home and `/katalog/` already showed the 10 curated Neutral titles (product-backed whitelist). Hide/wait titles absent. Empty copy not live. Full HTML not stored (sanitized card tables only).

Evidence: Storage `public-http-before/`.

## 9. Source prep

Primary authority: `system/library/zpm/category_visibility.php` (+ Twig tile templates).

Plan:
- Catalog Section Tiles Neutral path → `buildNeutralFirstLevelBlockCards` (HYBRID show/hide + empty-copy support)
- Mega / hub path → keep `buildHubChildCards` Neutral product gate
- Tech 362 → unchanged `buildHubChildCards(..., require_products=false)`

Evidence: Storage `source-prep/`.

## 10. Implementation

Changed production files:

1. `/public_html/system/library/zpm/category_visibility.php`
2. `/public_html/catalog/view/theme/default/template/sections/catalogsections.twig`
3. `/public_html/catalog/view/theme/default/template/product/katalog.twig`

Repo mirrors / helpers:

- `projects/ocpilot/sites/site-002/tools/category_visibility.php`
- `projects/ocpilot/sites/site-002/tools/catalogsections-SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01.twig`
- `projects/ocpilot/sites/site-002/tools/katalog-SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01.twig`
- `projects/ocpilot/sites/site-002/tools/site-002-prod-first-level-block-hybrid-apply-01.py`

Behavior:
- Neutral tiles use explicit show list; never include 82/83/85/87/89
- Zero-product approved show cards get `empty_copy` (none currently empty)
- Mega menu continues Neutral product gate via `buildHubChildCards`
- No public `БЗПМ`; no literal `\n` in public strings

Evidence: Storage `implementation/`.

## 11. Deploy plan / backups

Exact pre-deploy backups under `backups/production-files-before/` with hashes in `backups/backup-manifest.csv`. Rollback plan: restore those three files + clear `cache.*`.

Evidence: Storage `deploy-plan/`, `backups/`, `rollback/`.

## 12. FTP deploy

| Remote | Upload |
|--------|--------|
| `category_visibility.php` | **OK** |
| `catalogsections.twig` | **OK** |
| `katalog.twig` | **OK** |

Evidence: Storage `ftp-deploy/`.

## 13. Cache handling

| Action | Result |
|--------|--------|
| `storage/cache/cache.*` clear | **yes** (`before=29 after=0`) |
| `storage/modification/` wipe | **no** |
| OCMOD refresh | **not required** |

Evidence: Storage `cache/`.

## 14. Public after / UI regression

| Check | Result |
|-------|--------|
| Home Neutral show 10 / hide absent | **PASS** |
| `/katalog/` Neutral show 10 / hide absent | **PASS** |
| Empty copy | `EMPTY_COPY_SUPPORTED_BUT_NOT_RENDERED_CURRENTLY` |
| Sitemap | **1879** |
| Critical PDPs | OK (pre + post controls) |
| Wrong brand / PHP noise on home+katalog | **none** |

Neutral titles after (А→Я order live): Зонты вытяжные, Кондитерский инвентарь, Моечные ванны, Подтоварники и подставки, Полки настенные и настольные, Стеллажи, Столы, Тележки сервировочные, Тележки-шпильки и противни, Шкафы и лари.

Evidence: Storage `public-http-after/`, `ui-regression/`.

## 15. Monitor state

Monitor not re-run (UI-only code/template change; sitemap membership unchanged). Live sitemap confirm **1879**. Classification: `MONITOR_NOT_RUN_SITEMAP_UNCHANGED`. Prior after-refresh-08 evidence remains `NO_ACTION_REQUIRED`.

Evidence: Storage `monitor-state/`.

## 16. Regression / mutation summary

Allowed: exact 3 FTP files + authority source/report/docs + targeted `cache.*` clear.  
Forbidden mutations: **0** (DB/import/scheduler/baseline/categories/products/redirects/htaccess/importer/mapping/images/Client Ops/n8n/Telegram/dirty main/mega/deep/tech).

Evidence: Storage `regression/`.

## 17. Decision

| Field | Value |
|-------|-------|
| Apply | `HYBRID_FIRST_LEVEL_BLOCK_APPLY_COMPLETE` |
| Monitor | `MONITOR_NOT_RUN_SITEMAP_UNCHANGED` |
| Next | `READY_FOR_OPERATOR_VISUAL_REVIEW` |
| Verdict | `SITE-002 FIRST-LEVEL BLOCK HYBRID APPLY COMPLETE — READY FOR OPERATOR VISUAL REVIEW` |

## 18. Production mutation summary

- production DB writes: **0**
- production FTP writes: **3** (`category_visibility.php`, `catalogsections.twig`, `katalog.twig`)
- source/code changes: **1** (`category_visibility.php` mirror + harness)
- template changes: **2** (home + katalog tile twigs)
- cache clear: **1** (`storage/cache/cache.*`)
- delete operations: **0**
- import runs: **0**
- scheduler changes: **0**
- monitor baseline changes: **0**
- category/product changes: **0**
- redirect changes: **0**
- `.htaccess` changes: **0**
- importer/source changes unrelated to this task: **0**
- mapping changes: **0**
- image changes: **0**
- Client Ops changes: **0**
- n8n changes: **0**
- Telegram changes: **0**
- dirty main changes: **0**
- mega menu behavior changes: **0**
- deep leaf global visibility changes: **0**
- tech behavior changes: **0**

## 19. Git/worktree summary

| Item | Value |
|------|-------|
| Authority | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| HEAD at start | `66789bcb` |
| Dirty main | inspected read-only; not mutated |
| Commit/push | source/report/docs (this closeout) |

## 20. Rollback plan

1. FTP restore the three files from Storage `backups/production-files-before/`.
2. Clear `storage/cache/cache.*`.
3. Re-fetch home + `/katalog/` and confirm pre-apply card set.

## 21. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01\`

Populated: preflight, reports-read, current-state, db-readonly, source-prep, implementation, deploy-plan, backups, ftp-deploy, cache, public-http-before, public-http-after, ui-regression, monitor-state, rollback, decision, regression, reports, manifests, logs.

## 22. SAFE UNKNOWN / blockers

- Monitor not re-executed this run; sitemap count used as live membership proxy (`MONITOR_NOT_RUN_SITEMAP_UNCHANGED`).
- Exact CommerceML GUID/path for hide/wait IDs remains **SAFE UNKNOWN** (map hits still **0**; unchanged from Run 4.313).
- Operator CSS `.category__view { display: none !important; }` not changed; Catalog Section Tiles use `zpm-cat-card` (not that selector) — no impact observed on this apply.
- No blockers to apply success.

## 23. Final verdict

`SITE-002 FIRST-LEVEL BLOCK HYBRID APPLY COMPLETE — READY FOR OPERATOR VISUAL REVIEW`

## 24. Next recommendation

Operator visual review of home + `/katalog/` Neutral tiles. Then resume normal monitor cadence against baseline **1879**. No further UI scope expand until operator requests (e.g. promoting a proven empty first-level into the show list).

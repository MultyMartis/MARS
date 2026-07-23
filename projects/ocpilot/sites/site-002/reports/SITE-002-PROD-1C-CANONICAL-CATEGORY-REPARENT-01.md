# REPORT — SITE-002 1C Canonical Category Reparent 01

**Operation:** `SITE-002-PROD-1C-CANONICAL-CATEGORY-REPARENT-01`  
**OCPilot run:** **4.290**  
**Date:** 2026-07-23  
**Environment:** PRODUCTION_1C_CANONICAL_CATEGORY_REPARENT  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Runtime checkout:** `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-CANONICAL-CATEGORY-REPARENT-01\`

**Final verdict:** `SITE-002 1C CANONICAL CATEGORY REPARENT COMPLETE — PRODUCTS MOVED TO 1C CANONICAL CATEGORIES`

**Classifications:**
- Reparent: `CANONICAL_REPARENT_APPLIED`
- JG 210A: `JG210A_NOW_CANONICAL_MYASO`
- Legacy: `LEGACY_153_NOW_EMPTY_REVIEW_NEXT` + `LEGACY_CLEANUP_DEFERRED`
- Monitor: `MONITOR_ONBOARDING_REQUIRED_EXPECTED` + `MONITOR_NOT_RUN` (manual) + assumed `MONITOR_ARTIFACT_CONFLICT_STILL_PRESENT`

---

## 1. Scope

Controlled Production migration of product↔category relations from legacy duplicate leaves under `Электромеханическое оборудование` (153) to 1C-canonical hubs under `Технологическое оборудование`, without deleting/disabling categories and without importer/scheduler/baseline changes.

## 2. Operator approval and backup note

- Operator declared full Beget backup done before this task.
- Backup ID: **SAFE UNKNOWN** (not supplied).
- Exact operation DB row backup created under Storage `db-backup/` before apply.
- Legacy categories: **not deleted** (deferred).

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority HEAD | `9dd31d1b` (= `origin/mars/canonical-post-recovery`) |
| Origin includes `9dd31d1b` | yes |
| Staged | empty |
| Untracked tools (authority) | 3 foreign verification `.py` — **not committed** |
| Dirty main | foreign WIP — **read-only**; **0 mutations** |
| Authority commit safety | **SAFE** for exact report/docs commit |

## 4. Forensic baseline

From Run **4.289**: JG 210A 1C path is myaso→Пилы для мяса; DB/public were legacy 153→159; name-collision pattern for Пилы/Мясорубки/Хлеборезки; unique Слайсеры OK on 376; empty tech elektro **375**; monitor live **1817** vs baseline **1737** with artifact conflict.

Evidence: Storage `reports-read/forensic-baseline-summary.md`.

## 5. 1C source canonical mapping

Latest `public_html/1c_incoming/webdata/import0_1.xml` parsed.

| Product | xml_id | 1C path | Proposed DB target |
|---------|--------|---------|--------------------|
| Мясорубка TC-12 | `0b9c4216-…` | …→Мясоперерабатывающее→Мясорубки | **373** |
| Мясорубка TC-22 | `2e864195-…` | …→Мясоперерабатывающее→Мясорубки | **373** |
| Пила JG 210A | `56ccee94-…` | …→Мясоперерабатывающее→Пилы для мяса | **373** |
| Хлеборезка ТТ-D7C | `fe82a8d5-…` | …→Электромеханическое→Хлеборезки | **375** |
| Слайсер ТТ-М29С | `5b87f6dc-…` | …→Мясоперерабатывающее→Слайсеры | already **376** (no change) |

`oc_category` has **no** GUID/`xml_id`. Category GUID matching remains absent.

**Note:** DB has no separate leaf rows under 373 for Пилы/Мясорубки. Charter allows only exact `oc_product_to_category` → existing active hubs **373/375**.

Evidence: Storage `1c-source/`.

## 6. DB before map

Legacy leaves **154/159/165** held the four mismatch products. Canonical hubs **373/375** active. Relations-before SQL saved.

Evidence: Storage `db-before/`.

## 7. Public before

Legacy JG 210A PDP **200** under elektro path; myaso hub did not list it; health clean (no БЗПМ / notices on sampled pages).

Evidence: Storage `public-before/`.

## 8. Sitemap before

Live count **1817**; JG 210A under legacy elektro path; baseline 1737 not refreshed.

Evidence: Storage `sitemap-before/`.

## 9. Dry-run reparent plan

For each of 4 products: `INSERT IGNORE` canonical hub → set `main_category=1` on hub → `DELETE` legacy leaf relation. Rollback SQL generated.

Artifacts (also in repo): `reports/artifacts/SITE-002-PROD-1C-CANONICAL-CATEGORY-REPARENT-01/`.

## 10. HITL gates

All gates passed (including exact DB backup before apply). Decision: **APPLY**.

Evidence: Storage `hitl-gates/`.

## 11. DB backup

Exact `oc_product_to_category` rows for product_ids **4707,4708,4710,4712** plus product/SEO/category reference dumps. Rollback SQL: Storage `rollback/rollback.sql`.

## 12. DB apply

Transaction applied successfully. Verify:

| Metric | Value |
|--------|-------|
| Relations after | **4** (expected 4) |
| Legacy pairs remaining | **0** |
| 373 direct products | **3** (TC-12, TC-22, JG 210A) |
| 375 direct products | **1** (Хлеборезка) |
| 376 | unchanged (Слайсер) |
| 153/154/159/165 subtree products | **0** |

## 13. Cache actions

Cleared ` /home/a/assum/bzpm.ru/storage/cache/cache.*` only. Modification/OCMOD **not** touched.

## 14. Public after

| URL | Status | Notes |
|-----|--------|-------|
| Canonical JG 210A myaso PDP | **200** | canonical = myaso path; H1 OK |
| Legacy JG 210A elektro PDP | **200** | follows to myaso canonical (seo_pro `main_category`) |
| Myaso hub | **200** | lists JG 210A |
| Tech elektro hub | **200** | Хлеборезка PDP live under it |
| TC-12 / TC-22 myaso PDPs | **200** | OK |
| Blog / home | **200** | OK |
| Notices / БЗПМ | **0** | |

## 15. Sitemap after

Count still **1817** (path swap, not net +/−). JG 210A / TC-12 / Хлеборезка now under tech paths; legacy JG 210A PDP path **absent**. Baseline not refreshed.

## 16. Monitor after

Manual monitor **not run** (optional). Expected: still `ONBOARDING_REQUIRED` vs baseline 1737; artifact conflict may remain. Reparent success independent of monitor classification.

## 17. Regression

FTP writes **0** (read 1C XML only). Admin/import/scheduler/baseline/forms/mail/OCMOD **0**. Dirty main **0**. Categories not deleted/disabled. Product status/name/content **unchanged**.

## 18. Production mutation summary

| Item | Value |
|------|-------|
| DB writes | **YES** — `oc_product_to_category` only; 4 products; +4 hub rows / −4 legacy rows / main_category updates |
| FTP writes | **0** |
| Admin saves | **0** |
| Import runs | **0** |
| Scheduler changes | **0** |
| Monitor baseline changes | **0** |
| Category deletes | **0** |
| Category disables | **0** |
| Product status/name/content changes | **0** |
| Cache clears | **YES** — `storage/cache/cache.*` |
| OCMOD refresh | **0** |
| Dirty main changes | **0** |

## 19. Rollback plan

`rollback/rollback.sql` (and repo artifact): delete current PTC for the 4 products; restore pre-apply PTC inserts; commit. Then clear `cache.*` again if needed.

## 20. Git/worktree summary

| Item | Value |
|------|--------|
| Authority branch | `site-002-git-authority-realign-after-wave-e` @ pre-commit `9dd31d1b` |
| Dirty main | inspected read-only only |
| This commit | report + docs + dry-run/rollback SQL artifacts only |

## 21. Storage artifacts

Root: `...\deployments\SITE-002-PROD-1C-CANONICAL-CATEGORY-REPARENT-01\`

Populated: `preflight`, `reports-read`, `operator-backup`, `1c-source`, `db-before`, `public-before`, `sitemap-before`, `dry-run`, `hitl-gates`, `db-backup`, `db-apply`, `rollback`, `cache`, `public-after`, `sitemap-after`, `monitor-after`, `regression`, `reports`, `manifests`, `logs`.

## 22. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Exact Beget backup ID | SAFE UNKNOWN |
| Whether next 1C import re-attaches products to legacy same-name leaves **154/159/165** | **HIGH RISK** until category GUID mapping exists |
| Leaf categories under 373 for Пилы/Мясорубки | not created (out of charter); products sit on hub **373** |
| Leaf under 375 for Хлеборезки | not created; product on hub **375** |
| Manual monitor this run | not run |

## 23. Final verdict

**SITE-002 1C CANONICAL CATEGORY REPARENT COMPLETE — PRODUCTS MOVED TO 1C CANONICAL CATEGORIES**

Four 1C-matched products reparented: three to myaso hub **373**, one to tech elektro hub **375**. JG 210A public/canonical path is now under Мясоперерабатывающее. Legacy leaves retained empty for later cleanup.

## 24. Next recommendation

1. Charter **SITE-002-PROD-1C-CATEGORY-GUID-MAPPING-REVIEW-01** — persist 1C group GUID on categories / fix importer name-collision before next import undoes relations.
2. Optional: create leaf categories under **373** (Пилы/Мясорубки) and under **375** (Хлеборезки) for path fidelity matching 1C tree; then move products from hubs to leaves.
3. Separate HITL: disable/hide empty legacy **153** subtree leaves + decide on remaining empty siblings; do **not** delete while SEO/history matter.
4. Onboarding/meta for remaining monitor needs; baseline refresh only after placement wave settles and artifact conflict reviewed.
5. Optional explicit **301** map if soft canonical+route follow is insufficient for SEO tools.

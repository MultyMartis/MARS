# REPORT — SITE-002 Demo Category Delete Apply 01

**Operation:** `SITE-002-PROD-DEMO-CATEGORY-DELETE-APPLY-01`  
**OCPilot run:** **4.303**  
**Date:** 2026-07-27  
**Environment:** PRODUCTION_DEMO_CATEGORY_DELETE_APPLY  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-DEMO-CATEGORY-DELETE-APPLY-01\`

**Final verdict:** `SITE-002 DEMO CATEGORY DELETE APPLY COMPLETE — GROUP A REMOVED`

**Classifications:**
- Delete apply: `DEMO_CATEGORY_DELETE_APPLY_COMPLETE`
- Monitor next: `READY_FOR_BASELINE_REFRESH_06`

---

## 1. Scope

Controlled production physical delete of confirmed demo categories **154–170** (Group A) under legacy parent **153**.

Not in scope: parent **153**, products, 119 ambiguous empties, redirects, `.htaccess`, monitor baseline refresh, importer/mapping, Client Ops.

## 2. Operator approval

Operator approved physical delete of **154–170** with:

- no redirects / no 301;
- no `status=0` as final cleanup;
- parent **153** kept;
- products not deleted;
- baseline refresh deferred.

Evidence: Storage `reports-read/operator-approval.md`.

## 3. Client Ops boundary

- **Not touched:** Client Ops Telegram Reports, reporting bridge, n8n, Telegram bot, Hub Gateway, reporting envelope.
- Monitor mentioned only as SITE-002 evidence; baseline **not** refreshed.

## 4. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `48de50a4` (= `origin/mars/canonical-post-recovery`) |
| Origin includes `48de50a4` | **yes** |
| Staged | empty |
| Unpushed | empty |
| Untracked foreign tools | 3 verification `.py` — **not committed** |
| Dirty main | foreign WIP — **read-only**; **0 mutations** |
| Authority unsafe | **NO** |

Evidence: Storage `preflight/`.

## 5. Reports read / current state

| Source | Key fact |
|--------|----------|
| 4.299 persistence | CONFIRMED; critical on 378/379/380/376 |
| 4.300 baseline refresh | 1737→1854; `NO_ACTION_REQUIRED` |
| 4.301 legacy cleanup | Option A 301+disable — **superseded** |
| 4.302 demo cleanup charter | Group A DELETE_READY 154–170; apply not executed |
| This run 4.303 | Physical delete applied |

Evidence: Storage `reports-read/`.

## 6. DB before

| Metric | Value |
|--------|------:|
| Target categories found | **17 / 17** |
| All parent_id=153 | **yes** |
| product_to_category | **0** |
| mars_1c_category_map on targets | **0** |
| oc_category | 17 |
| oc_category_description | 17 |
| oc_category_to_store | 17 |
| oc_category_path (by category_id) | 34 |
| oc_seo_url (category) | 17 |
| oc_category_to_layout | 17 |
| Hard gate | **PASS** |

Evidence: Storage `db-before/`.

## 7. Delete candidates reconfirm

| Check | Result |
|-------|--------|
| All 17 delete_ready | **yes** |
| Direct/subtree products | **0 / 0** |
| 1C map rows | **0** |
| Critical products on 378/379/380/376 | **yes** |
| Canonical IDs intact | **yes** |
| Parent 153 children before | **17** |
| Hard gate | **PASS** |

Evidence: Storage `delete-candidates-reconfirm/`.

## 8. Sitemap before

| Metric | Value |
|--------|------:|
| HTTP | 200 |
| URL count | **1854** |
| Duplicates | 0 |
| Valid XML | yes |
| Target demo URLs present | **17 / 17** |
| Canonical tech keywords present | yes |

Evidence: Storage `sitemap-after/sitemap-before-delete-summary.md`.

## 9. Public before

| Set | Result |
|-----|--------|
| Target demo PLPs 154–170 | **17 × HTTP 200** (empty demo pages) |
| Home / katalog / parent 153 | 200 |
| Canonical 362/373/375/378/379/380 | 200 |
| Critical PDPs 4707/4708/4709/4710/4712 | 200; no «Товар не найден» |
| PHP Notice/Warning/Fatal | none |
| Public `БЗПМ` | none |
| Probe note | guessed URL for **376** (`…/masloterki-tehnologicheskoe`) returned **404** before apply — wrong keyword; real SEO is `slaysery-dlya-myasa` (pre-existing probe miss, not a delete regression) |

Evidence: Storage `public-http/public-before*`.

## 10. Backup

| Item | Result |
|------|--------|
| Backup SQL | `backup/category-delete-backup.sql` (mysqldump INSERT) |
| Category rows backed up | **17** |
| Total data rows (incl. parent 153 context) | **123** |
| Verified | **yes** |
| Restore readme | yes |

Hard gate: **PASS**.

## 11. Dry-run

| Table | Rows |
|-------|-----:|
| oc_product_to_category | 0 |
| oc_category_filter | 0 |
| oc_coupon_category | 0 |
| oc_category_to_layout | 17 |
| oc_seo_url | 17 |
| oc_category_path | 34 |
| oc_category_to_store | 17 |
| oc_category_description | 17 |
| oc_category | 17 |
| **Total** | **119** |

No non-target categories; no product rows. Hard gate: **PASS**.

Evidence: Storage `dry-run/`.

## 12. HITL gates

All 16 gates **PASS**. Decision: **APPLY**.

Evidence: Storage `hitl-gates/`.

## 13. Apply delete

Executed transaction for exact IDs **154–170**.

| Metric | Value |
|--------|------:|
| All target rows absent after | **yes** |
| Parent 153 remains | **yes** |
| Deleted rows (sum) | **119** |

Evidence: Storage `apply/`.

## 14. Cache

Cleared minimal `storage/cache/` entries: `cache.category.seopath*`, `cache.seo_pro.*`, `cache.product.seopath*`, `cache.cat-list-header*`, `cache.category.*`.

**Not done:** `storage/modification/` wipe; OCMOD refresh.

Evidence: Storage `cache/cache-actions.md`.

## 15. DB after

| Check | Value |
|-------|------:|
| Targets remaining | **0** |
| Path orphans | **0** |
| SEO orphans | **0** |
| Parent 153 | **1** |
| Children of 153 | **0** |
| Critical products | still on **378/379/380/376** |
| Canonical categories | intact |
| Mapping on targets | **0** |
| Overall | **PASS** |

Evidence: Storage `db-after/`.

## 16. Sitemap after

| Metric | Value |
|--------|------:|
| HTTP | 200 |
| URL count | **1837** |
| Delta | **−17** (1854→1837) |
| Expected after | **1837** |
| Target demo URLs present | **0 / 17** |
| Canonical tech keywords | present |
| Duplicates | 0 |
| Valid XML | yes |

Evidence: Storage `sitemap-after/`.

## 17. Public after

| Set | Result |
|-----|--------|
| Target demo PLPs 154–170 | **17 × HTTP 404** (acceptable; no 301) |
| Home / katalog / parent 153 | 200 |
| Canonical 362/373/375/378/379/380 | 200 |
| Critical PDPs | 200; no «Товар не найден» |
| PHP / `БЗПМ` / literal `\n` | clean on probed pages |
| Probe note | same wrong-keyword 404 for guessed **376** URL as before (not caused by delete) |

Evidence: Storage `public-http/public-after*`.

## 18. Monitor state

| Item | Value |
|------|-------|
| Baseline refreshed in this task | **no** |
| Expected baseline remains | **1854** |
| Sitemap current (live) | **1837** |
| Removed estimate | **17** |
| Expected classification after next monitor | `ONBOARDING_REQUIRED` (or equivalent) due to removed URLs |
| Next | `SITE-002-MONITOR-BASELINE-REFRESH-06` |

Evidence: Storage `monitor-state/`.

## 19. Rollback plan

| Item | Status |
|------|--------|
| `rollback/rollback.sql` | present (= verified backup) |
| Rollback executed | **no** |
| Rollback needed | **no** (apply verified) |

Evidence: Storage `rollback/`.

## 20. Regression

| Check | Result |
|-------|--------|
| DB writes limited to 154–170 category-related rows | pass |
| FTP writes | **0** |
| Product deletes | **0** |
| Category 153 | kept |
| Canonical categories | unchanged |
| Importer / mapping / import / scheduler | **0** |
| Monitor baseline | **0** |
| Redirects / `.htaccess` / images | **0** |
| Client Ops / n8n / Telegram | **0** |
| Dirty main | **0** |

Evidence: Storage `regression/`.

## 21. Production mutation summary

| Item | Value |
|------|------:|
| Deleted category IDs | 154–170 (17) |
| Deleted rows by table | layout 17 + seo_url 17 + path 34 + store 17 + description 17 + category 17 (+ 0 on product/filter/coupon) = **119** |
| DB writes | exact category-related deletes only |
| FTP writes | **0** |
| Product deletes | **0** |
| Parent 153 changes | **0** (kept; now 0 children) |
| Canonical category changes | **0** |
| Mapping table changes | **0** |
| Importer/source changes | **0** |
| Import runs | **0** |
| Scheduler changes | **0** |
| Monitor baseline changes | **0** |
| Redirect changes | **0** |
| `.htaccess` changes | **0** |
| Image changes | **0** |
| Cache actions | minimal category/seo_pro cache clear |
| Client Ops / n8n / Telegram | **0** |
| Dirty main changes | **0** |

## 22. Git/worktree summary

| Item | Value |
|------|--------|
| Authority HEAD before | `48de50a4` |
| Dirty main | read-only; foreign WIP preserved |
| Commit wave | report/docs only (this run) |

## 23. Storage artifacts

Root: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-DEMO-CATEGORY-DELETE-APPLY-01\`

Subfolders: `preflight/`, `reports-read/`, `db-before/`, `delete-candidates-reconfirm/`, `dry-run/`, `backup/`, `hitl-gates/`, `apply/`, `cache/`, `db-after/`, `sitemap-after/`, `public-http/`, `monitor-state/`, `rollback/`, `regression/`, `reports/`, `manifests/`, `logs/`.

## 24. SAFE UNKNOWN / blockers

- Exact next scheduled monitor run classification after delete: **SAFE UNKNOWN** until manual/scheduled monitor executes (baseline still 1854 by design).
- Public probe URL for category **376** used an incorrect keyword guess (`masloterki-tehnologicheskoe`); real keyword is `slaysery-dlya-myasa`. Pre-existing both before and after; category **376** and product **4709** remain intact.
- Full Beget panel backup ID: **SAFE UNKNOWN** (operation-scoped SQL backup created and verified).

**Blockers:** none for delete apply completion.

## 25. Final verdict

`SITE-002 DEMO CATEGORY DELETE APPLY COMPLETE — GROUP A REMOVED`

## 26. Next recommendation

`SITE-002-MONITOR-BASELINE-REFRESH-06`

Refresh monitor baseline from **1854 → 1837** (or live count after verify) only after this delete remains stable.

---

## Execution safety

- cwd: `X:\AI MARS` (ops against Storage + authority worktree)
- scope lock honored: yes (`X:\AI MARS STORAGE\…`, authority repo docs)
- destructive ops: production DB physical delete of category IDs **154–170** only (operator-approved); no recursive filesystem delete; no `git clean`/`reset`
- protected zone touch: none beyond allowlisted OCPilot docs/report

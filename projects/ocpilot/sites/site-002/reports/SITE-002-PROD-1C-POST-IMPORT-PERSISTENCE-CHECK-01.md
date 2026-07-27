# REPORT — SITE-002 1C Post Import Persistence Check 01

**Operation:** `SITE-002-PROD-1C-POST-IMPORT-PERSISTENCE-CHECK-01`  
**OCPilot run:** **4.299**  
**Date:** 2026-07-27  
**Environment:** PRODUCTION_1C_POST_IMPORT_PERSISTENCE_CHECK_READONLY  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Runtime checkout:** `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-POST-IMPORT-PERSISTENCE-CHECK-01\`

**Final verdict:** `SITE-002 1C POST-IMPORT PERSISTENCE CHECK COMPLETE — PERSISTENCE CONFIRMED`

**Classifications:**
- Import discovery: `NATURAL_IMPORT_AFTER_PATCH_FOUND`
- Import status: `SUCCESS`
- Mapping: `GUID_PATH_MAPPING_PERSISTED`
- Persistence: `POST_IMPORT_PERSISTENCE_CONFIRMED`
- Next action: `READY_FOR_BASELINE_REFRESH_CHARTER`
- Monitor: `MONITOR_ONBOARDING_REQUIRED_EXPECTED`

---

## 1. Scope

Read-only verification that natural 1C imports after Run **4.297** importer GUID/path patch preserved canonical category assignment for critical tech products, without production mutation, baseline refresh, legacy cleanup, or Client Ops changes.

---

## 2. Boundary from Client Ops Telegram Reports

- **Not touched:** Client Ops Telegram Reports, reporting bridge, n8n, Telegram bot, Hub Gateway drafts.
- Monitor artifacts read **only** as SITE-002 evidence.
- Latest monitor run artifact conflict with Client Ops semantics: **not present** in `2026-07-27_12-30-02` (all three agree `ONBOARDING_REQUIRED`). Historical conflict noted as prior finding only.

---

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD (pre-ff) | `dc1fa5c4` (includes patch + image apply) |
| Origin includes `dc1fa5c4` | **yes** |
| Authority ff to origin | `bd46565f` (= `origin/mars/canonical-post-recovery`) |
| Staged | empty |
| Untracked foreign tools | 3 verification `.py` — **not committed** |
| Dirty main | foreign WIP (incl. Client Ops) — **read-only**; **0 mutations** |

Evidence: Storage `preflight/`.

---

## 4. Reports read / baseline

Runs **4.295–4.298** summarized in Storage `reports-read/`.

Pre-natural-import known state:
- Critical products already on **378/378/376/379/380**
- Live sitemap **1820**
- Monitor baseline **1737**
- Importer patch deployed **2026-07-23T17:09:40Z**

---

## 5. Import log discovery

### Hard classification

`NATURAL_IMPORT_AFTER_PATCH_FOUND`

### Evidence

| Day | Wrapper log | TXT report | Final status |
|-----|-------------|------------|--------------|
| 2026-07-24 | `mars_1c_import_20260724.log` finished OK | `mars_1c_import_2026-07-24_080010.txt` | **SUCCESS** |
| 2026-07-25 | OK | `..._2026-07-25_080009.txt` | **SUCCESS** |
| 2026-07-26 | OK | `..._2026-07-26_080010.txt` | **SUCCESS** |
| 2026-07-27 | OK | `mars_1c_import_2026-07-27_080009.txt` | **SUCCESS** |

- Latest run ID: `mars-20260727-080002-e9d99513`
- Step 1 `1c` PASS; Step 2 `1c_offers` PASS
- Imports after patch: **yes**; after image apply: **yes**

### MARS importer signals

Wrapper TXT reports do **not** contain `MARS_CATEGORY_*` / `MARS_PRODUCT_CATEGORY_RESOLVED` lines (0 rows).  
**SAFE UNKNOWN** whether detailed MARS signals are written only to OpenCart runtime logs not captured here. Persistence proven via DB `date_modified` + category relations instead.

Evidence: Storage `import-logs/`.

---

## 6. DB read-only check

### Critical products (after natural import)

| product_id | name | main_category_id | expected | date_modified | ok |
|-----------:|------|-----------------:|---------:|---------------|----|
| 4707 | Мясорубка TC-12 | **378** | 378 | 2026-07-27 05:00:05 | true |
| 4708 | Мясорубка TC-22 | **378** | 378 | 2026-07-27 05:00:05 | true |
| 4709 | Слайсер для мяса ТТ-М29С | **376** | 376 | 2026-07-27 05:00:02 | true |
| 4710 | Пила для мяса на кости JG 210A | **379** | 379 | 2026-07-27 05:00:03 | true |
| 4712 | Хлеборезка ТТ-D7C | **380** | 380 | 2026-07-27 05:00:04 | true |

`date_modified` proves today's natural import **touched** these products and left them on canonical leaves.

### Critical categories

| category_id | direct products | notes |
|------------:|----------------:|-------|
| 154 / 159 / 165 | **0** | legacy leaves empty |
| 153 subtree | **0** | legacy electromechanical root empty of products |
| 378 | 2 | critical мясорубки |
| 379 | 1 | critical пила |
| 380 | 1 | critical хлеборезка |
| 376 | 1 | critical слайсер |
| 375 image | set | electromechanical tile remains |

### Mapping table

7/7 active GUID→canonical rows for 362/373/375/376/378/379/380. No tech GUID → 154/159/165.

Evidence: Storage `db-readonly/`.

---

## 7. Mapping / collision check

**Classification:** `GUID_PATH_MAPPING_PERSISTED`

- Collision leaf names still exist in DB (154↔378, 159↔379, 165↔380).
- Post-patch imports did **not** reassign critical products to legacy.
- Review-required log lines in wrapper reports: **0 found**.

Evidence: Storage `mapping-check/`.

---

## 8. Sitemap check

| Metric | Value |
|--------|------:|
| Live unique URLs | **1854** |
| Duplicates | 0 |
| Prior known live | 1820 |
| Monitor baseline | 1737 |
| Δ vs prior live | +34 |
| Δ vs baseline | +117 |

Critical product SEO keywords present; leaf category URLs for 376/378/379/380 present under tech tree. Legacy product URLs for critical SKUs not observed under legacy electromechanical paths.

Evidence: Storage `sitemap/`.

---

## 9. Public HTTP check

Canonical hubs/leaves HTTP **200** (after correcting 376 SEO keyword to `slaysery-dlya-myasa`):

- Tech hub, мясоперерабатывающее, мясорубки, пилы, слайсеры, электромеханическое, хлеборезки — OK
- PDP 4707/4708/4710/4712 — **200**, name present, no «Товар не найден»
- PDP 4709 — **200** at `/katalog/.../slaysery-dlya-myasa/slayser-dlya-myasa-tt-m29s`
- Products listed on expected leaf PLPs
- PHP Notice/Warning/Fatal: **0**
- Public `БЗПМ`: **0**
- Electromechanical category image remains visible on hub pages

Evidence: Storage `public-http/`.

---

## 10. Monitor artifacts

| Field | Value |
|-------|-------|
| Latest run_id | `2026-07-27_12-30-02` |
| run-summary | `ONBOARDING_REQUIRED` |
| monitor-classification | `ONBOARDING_REQUIRED` |
| run.log | `ONBOARDING_REQUIRED` |
| baseline | 1737 |
| current | 1854 |
| added / removed | 119 / 2 |
| onboarding_needs_count | 7 |

**Classification:** `MONITOR_ONBOARDING_REQUIRED_EXPECTED`

Artifact conflict (summary vs classification) **not present** in this latest run. Baseline **not** refreshed in this task.

Evidence: Storage `monitor-artifacts/` (copies from scheduled-monitors).

---

## 11. Harness / dry validation

`--fetch-live` harness against current XML + DB:

- Current DB categories for critical products: **378 / 378 / 376 / 379 / 380**
- Proposed resolution matches canonical leaves
- Harness still labels some rows with historical `WOULD_REVERT_TO_LEGACY_UNDER_OLD_IMPORTER` wording — superseded by live post-patch persistence evidence

Evidence: Storage `harness/`.

---

## 12. Decision

| Item | Value |
|------|-------|
| Persistence | `POST_IMPORT_PERSISTENCE_CONFIRMED` |
| Next action | `READY_FOR_BASELINE_REFRESH_CHARTER` |

Do **not** baseline refresh or legacy-clean in this task. Recommend a separate charter for monitor baseline refresh to current live (~1854), then optional legacy 154/159/165 cleanup charter.

---

## 13. Regression

| Check | Count |
|-------|------:|
| DB writes | 0 |
| FTP writes | 0 |
| Import runs initiated | 0 |
| Scheduler changes | 0 |
| Monitor baseline changes | 0 |
| Category/product relation changes | 0 |
| Importer/source changes | 0 |
| Mapping table changes | 0 |
| Client Ops changes | 0 |
| n8n changes | 0 |
| Telegram changes | 0 |
| Dirty main changes | 0 |

Evidence: Storage `regression/`.

---

## 14. Production mutation summary

- DB writes: 0
- FTP writes: 0
- Import runs initiated: 0
- Scheduler changes: 0
- Monitor baseline changes: 0
- Category/product relation changes: 0
- Importer/source changes: 0
- Mapping table changes: 0
- Client Ops changes: 0
- n8n changes: 0
- Telegram changes: 0
- Dirty main changes: 0

---

## 15. Git/worktree summary

- Authority used for report/docs commit/push.
- Dirty main inspected only; not mutated.
- Foreign untracked tools in authority excluded from commit.

---

## 16. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-POST-IMPORT-PERSISTENCE-CHECK-01\`

Subfolders populated: preflight, reports-read, import-logs, db-readonly, mapping-check, critical-products, legacy-check, sitemap, public-http, monitor-artifacts, harness, decision, regression, reports, manifests, logs.

---

## 17. SAFE UNKNOWN / blockers

- Exact OpenCart-level `MARS_*` signal emission location/counts for natural imports: **SAFE UNKNOWN** (not in wrapper TXT).
- Product add/update/delete numeric counts inside importer: **SAFE UNKNOWN** (wrapper report has PASS/SUCCESS only; product touch proven via `date_modified`).
- No blockers for persistence conclusion.

---

## 18. Final verdict

`SITE-002 1C POST-IMPORT PERSISTENCE CHECK COMPLETE — PERSISTENCE CONFIRMED`

---

## 19. Next recommendation

1. Charter **monitor baseline refresh** to current live sitemap (~1854) — do not run inside this check.
2. Separate charter for **category meta onboarding** of the 7 monitor needs (read-only finding).
3. Only after baseline refresh + operator approval: consider **legacy 154/159/165** cleanup/redirect charter.
4. Keep Client Ops Telegram Reports boundary intact.

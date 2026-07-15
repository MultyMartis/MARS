# REPORT — SITE-002 Catalog New Branch Onboarding 02

**Operation:** `SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-02`  
**OCPilot run:** 4.260  
**Date:** 2026-07-12  
**Environment:** Production (`https://bzpm.ru/`) + local runtime verification  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Runtime checkout:** `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`  
**Baseline (unchanged):** `SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01`  
**Source natural monitor:** `2026-07-12_12-30-02` (Run 4.259)

---

## 1. Scope

Review and onboard two new catalog category branches detected by the natural scheduled post-1C monitor:

1. `/katalog/tehnologicheskoe-oborudovanie/posuda-i-inventar`
2. `/katalog/nejtralnoe-oborudovanie/stellazhi/stellazhi-standart/stellazhi-standart-vysota-1600`

Allowed: exact category `meta_description` DB UPDATE; monitor allowlist update; runtime script sync; manual monitor from clean runtime.  
Forbidden: FTP; parent_id/path/seo_url/URL/redirect/sitemap/product changes; scheduler settings; dirty main mutation.

---

## 2. Operator approval

Operator approved this production/onboarding step after `MARS-INFRA-RUNTIME-SPLIT-SITE-002-NATURAL-RUN-VERIFY-01` confirmed runtime split and natural monitor classification `ONBOARDING_REQUIRED` with 2 needs.

---

## 3. Source natural monitor run

| Field | Value |
|-------|--------|
| Artifact | `2026-07-12_12-30-02` |
| repo_root | `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` |
| Classification | `ONBOARDING_REQUIRED` |
| onboarding_needs | **2** |
| Added/removed | 167 / 14 |
| Baseline → current sitemap | 1377 → 1530 |
| Strict garbage | 0 |
| Hygiene flags | 0 |
| Old Lari FPs | did not return |

Storage: `deployments/SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-02/source-monitor-artifacts/`

---

## 4. Pre-flight

| Check | Result |
|-------|--------|
| Volume | `X:` label **AI WS** |
| Authority HEAD | `ec673199` (= `origin/mars/canonical-post-recovery`) |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Staged | empty |
| Untracked | known verification `.py` files (not committed) |
| Runtime HEAD | `bd3021bf` (detached) |
| Dirty main `X:\AI MARS` | **not touched** |

**Verdict:** Pre-flight **PASS**.

---

## 5. HTTP before

| URL | Status | Indexable | Meta len | БЗПМ |
|-----|--------|-----------|----------|------|
| Target A posuda-i-inventar | 200 | yes | 0 | 0 |
| Target B stellazhi-standart-vysota-1600 | 200 | yes | 0 | 0 |
| Parent tehnologicheskoe-oborudovanie | 200 | yes | 140 | 0 |
| Parent stellazhi | 200 | yes | 70 | 0 |
| Parent stellazhi-standart | 200 | yes | 134 | 0 |
| /sitemap.xml | 200 | yes | — | — |
| /contact | 200 | yes | 129 | 0 |
| /kontakty | 404 (accepted) | — | — | — |

---

## 6. DB mapping

| Key | category_id | Name | parent_id | path | status | products | meta before |
|-----|-------------|------|-----------|------|--------|----------|-------------|
| A | **364** | Посуда и инвентарь | 362 | 362,364 | 1 | 6 | empty |
| B | **365** | Стеллажи СТАНДАРТ высота 1600 | 348 | 79,86,348,365 | 1 | 104 | empty |

Both are valid enabled 1C/catalog category PLPs (date_added `2026-07-11 05:00:02`). Parents unchanged. Hub entrypoint concern: **no** (parents already live with meta).

---

## 7. Decision matrix

| Target | Decision | Risk |
|--------|----------|------|
| A (364) | `META_AND_ALLOWLIST_REQUIRED` | P2 |
| B (365) | `META_AND_ALLOWLIST_REQUIRED` | P2 |

---

## 8. Proposed meta

| id | New meta_description | Chars | БЗПМ |
|----|----------------------|-------|------|
| 364 | Посуда и инвентарь ЗПМ для предприятий питания, торговли и производственных зон. Раздел с актуальными товарами и характеристиками. | 130 | 0 |
| 365 | Стеллажи Стандарт высотой 1600 мм ЗПМ для хранения продукции, инвентаря и оборудования. Актуальные модели в каталоге. | 117 | 0 |

Only `meta_description` proposed. `meta_title` left unchanged.

---

## 9. Production meta mutation

Exact SQL UPDATE on `oc_category_description.meta_description` for `category_id IN (364,365) AND language_id=1`.

| id | ROW_COUNT | Result |
|----|-----------|--------|
| 364 | 1 | OK |
| 365 | 1 | OK |

Backup: `db-backup/category-meta-before-exact-rows.sql`  
Apply: `apply/apply-category-meta.sql`

---

## 10. DB/HTTP after

| Check | Result |
|-------|--------|
| 364/365 meta non-empty | **PASS** (130 / 117) |
| parent_id / category_path / status / seo_keyword unchanged | **PASS** |
| HTTP 200 targets | **PASS** |
| Public meta matches DB | **PASS** |
| Public БЗПМ | **0** |

---

## 11. Monitor allowlist patch

Added to `ONBOARDED_CATEGORY_PATHS` in `site-002-prod-post-1c-catalog-onboarding-monitor-02.py`:

- `katalog/tehnologicheskoe-oborudovanie/posuda-i-inventar`
- `katalog/nejtralnoe-oborudovanie/stellazhi/stellazhi-standart/stellazhi-standart-vysota-1600`

No removals. No PDP paths.

---

## 12. Runtime checkout sync

Exact monitor script copied authority → runtime checkout. SHA256 match confirmed. Runtime HEAD remains `bd3021bf` with expected modified file until later refresh. Dirty main untouched. Scheduler settings unchanged.

---

## 13. Manual monitor run

| Field | Value |
|-------|--------|
| Command | `site-002-post-1c-monitor-runner.ps1` from runtime checkout |
| Artifact | `2026-07-12_22-19-55` |
| repo_root | runtime checkout |
| exit_code | **0** |
| onboarding_needs_count | **0** |
| classification | `HYGIENE_REVIEW_REQUIRED` |
| hygiene_flags | **0** |
| strict_garbage | **0** |
| added/removed | 167 / 14 |

`HYGIENE_REVIEW_REQUIRED` is due to **baseline delta only** (monitor baseline still 1377 vs current 1530). Not an onboarding failure.

---

## 14. Sitemap/site safety regression

| Check | Result |
|-------|--------|
| Sitemap 200 valid XML | **PASS** |
| Sitemap URL count | **1530** |
| Both targets in sitemap | **PASS** |
| HTTP 500 | **0** |
| /kontakty | **404** accepted |
| Public БЗПМ | **0** |
| Key onboarded Lari URLs | 200 |

---

## 15. Final decision

| Area | Status |
|------|--------|
| Production meta | **UPDATED** (364, 365) |
| Monitor allowlist | **UPDATED** |
| Runtime verification | **PASS_NEEDS_0** |
| Checkpoint | unchanged |

---

## 16. Production mutation summary

- FTP writes: **0**
- DB writes: **2** exact `meta_description` rows (364, 365)
- Admin saves: **0**
- Import runs triggered: **0**
- Production code changes: **0**
- Production content changes: category meta only (2 rows)
- Form submits: **0**
- Mail sends: **0**

---

## 17. Runtime mutation summary

- Monitor code changes: allowlist only (**2** paths)
- Runtime checkout file sync: **1**
- Manual monitor runs: **1**
- Task Scheduler changes: **0**
- Dirty main changes: **0**

---

## 18. Git/worktree summary

| Worktree | Role | Mutation |
|----------|------|----------|
| Authority `git-sync-e01` | docs + monitor allowlist commit | yes (allowlisted paths) |
| Runtime checkout | exact script sync | file dirty vs pinned HEAD (expected) |
| Dirty main `X:\AI MARS` | unused | **0** |

---

## 19. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-02\`

Includes preflight, source-monitor-artifacts, db-before/after/backup, http-before/after, proposed-meta, apply, monitor-code-before/after, runtime-sync, monitor-run, sitemap, verification, manifests, logs.

---

## 20. SAFE UNKNOWN / blockers

- Monitor sitemap **baseline** still at 1377; not refreshed in this task (out of scope). Causes recurring `HYGIENE_REVIEW_REQUIRED` until baseline refresh charter.
- `/kontakty` remains 404 by design (accepted).
- Runtime checkout not fast-forwarded to post-commit SHA in this task (exact file sync used; optional later refresh).

No blockers for onboarding completion.

---

## 21. Final verdict

**SITE-002 NEW BRANCH ONBOARDING COMPLETE — TARGET BRANCHES ONBOARDED AND MONITOR NEEDS ZERO**

---

## 22. Next recommendation

1. Optional: refresh monitor sitemap baseline to current ~1530 so scheduled runs stop classifying as hygiene-review-only due to large delta.
2. Optional: after this commit is on `origin/mars/canonical-post-recovery`, refresh runtime checkout to that SHA (exact allowlist already synced).
3. Do not create a new stable checkpoint unless further production consolidation is chartered.
4. Keep scheduled monitor on runtime checkout — never dirty main.

## Execution safety

- cwd / authority: `X:\AI MARS STORAGE\git-sync-e01\repo`
- scope lock honored: yes (`X:\AI MARS STORAGE` + authority repo)
- destructive ops: none
- protected zone touch: none

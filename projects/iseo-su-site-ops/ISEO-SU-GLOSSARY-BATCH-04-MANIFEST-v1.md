# ISEO-SU GLOSSARY BATCH 04 MANIFEST v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-BATCH-04-FINAL-CONTENT-COMPLETION  
**Date:** 2026-07-26  
**Publication:** **not performed** — all targets remain `draft`

---

## 1. Batch Status

| Field | Value |
|-------|-------|
| Status | **SAFE CONTENT CORPUS COMPLETE WITH DEFERRED EDGE CASES** |
| READY_FOR_CONTENT applied | **54 / 54** |
| Failed | **0** |
| Newly MERGED | **4** |
| Newly DEFERRED | **6** |
| Newly EXCLUDED | **0** |
| Renames observed | **9** |
| Public exposure | still closed (`/glossary/` anonymous **404**) |
| Menu / sitemap | unchanged / still excluded |
| New CSS/JS | none |

## 2. Starting State

Reconciled MARS manifests (Batches 01–03 CSV) vs final corpus:

| Metric | Expected (Batch 03 REPORT) | Actual |
|--------|---------------------------:|-------:|
| Populated | 130 | **130** |
| Remaining publication-pool | 63 | **64** |
| Remaining APPROVED | 54 | **54** |
| Remaining APPROVED_RENAME | 9 | **10** |
| MERGED / DEFERRED / EXCLUDED | 26 / 8 / 13 | **26 / 8 / 13** |
| Total WP glossary drafts | 241 | **241** |
| Published | 0 | **0** |

**Reconciliation note:** prior Batch 03 remaining-pool figure **63 / 9 renames** was off by one rename; arithmetic `194 − 130 = 64` is authoritative.

Full Beget backup: **OPERATOR CONFIRMED** for this work sequence (no new full-backup gate invented).

## 3. Final Candidate Review

All **64** remaining APPROVED / APPROVED_RENAME candidates re-evaluated.

Decisions:

| Decision | Count |
|----------|------:|
| READY_FOR_CONTENT | **54** |
| MERGE | **4** |
| DEFER | **6** |
| EXCLUDE | **0** |

Authoritative detail: `_glossary-scratch/batch04-final-decisions.json`.

## 4. Ready for Content

**54** terms — see §8 and `data/glossary-editorial/ISEO-SU-GLOSSARY-BATCH-04-CONTENT-v1.csv`.

## 5. Newly Deferred

| Source term | Reason |
|-------------|--------|
| СНСС (ранее НПС) | Unstable/historical Yandex naming; needs_expert_pass |
| СПЕКТР | Insufficient primary docs / naming stability |
| ПРЕСЕО | Agency jargon, not stable glossary concept |
| Отдел антиспама | Organizational metaphor, not standalone concept |
| Пост-фильтры | Unstable jargon; overlaps filter/algorithm framing |
| CatBoost | ML library; ranking role opaque — do not invent |

## 6. Newly Merged

| Source term | Canonical target |
|-------------|------------------|
| ВЧ / СЧ / НЧ запросы | Частотность запроса |
| Морда | Главная страница сайта |
| УВ | Уникальный посетитель |
| Процент вхождений | Плотность ключевых слов |

## 7. Newly Excluded

None.

## 8. Batch 04 Terms

UTF-8 Markdown: `content/glossary/batch-04/` (**54** files).  
Dataset: `data/glossary-editorial/ISEO-SU-GLOSSARY-BATCH-04-CONTENT-v1.csv`.  
Payload: `_glossary-scratch/batch-04-content.json`.

## 9. Category Distribution

| Category | Count |
|----------|------:|
| SEO fundamentals | 29 |
| link building | 6 |
| search engines and indexing | 5 |
| content and semantics | 4 |
| analytics and metrics | 2 |
| digital marketing | 2 |
| technical SEO | 2 |
| security and infrastructure | 2 |
| contextual advertising | 1 |
| AI search and GEO | 1 |

## 10. Depth Distribution

| Depth | Count |
|-------|------:|
| SIMPLE | 16 |
| MODERATE | 34 |
| COMPLEX | 4 |

COMPLEX: MatrixNet; BERT; BM25; Neural Matching (COMPLEX bodies expanded after corpus QA shallow gate).

## 11. Renames

**9** APPROVED_RENAME titles applied to existing drafts (source title → canonical). Slug collisions: **0**.

AMP; BM25; Domain Authority; Domain Rating; GET-параметр; PageRank; Дашборд; CAPTCHA; MatrixNet.

## 12. Research Requirements

Fact-sensitive notes added to `ISEO-SU-GLOSSARY-RESEARCH-REGISTER-v1.md` (Batch 04 section): DA/DR/PageRank vendor disclosure; AMP; BERT; BM25; Neural Matching; MatrixNet; АГС/тИЦ historical; PBN; Spam Update; AdSense.

## 13. WordPress Targets

| Check | Result |
|-------|--------|
| Matched existing drafts | **54 / 54** |
| Non-glossary / published | **0** |
| Duplicate target IDs | **0** |
| New posts created | **0** |

## 14. Scoped Backup

| Field | Value |
|-------|-------|
| First authenticated snapshot path | `X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\glossary-batch04-final-content-20260726-173213\` |
| First snapshot SHA-256 | `8420c36602805a27029716a8c77d1e57b56b15f0f41cb99be6c0394aae2dba54` |
| Reconstructed full-54 rollback artifact | `...\glossary-batch04-prewrite-reconstructed-20260726-175433\` |
| Reconstructed SHA-256 | `52eca9587efc44c409aecddf1e565f76f09a46048db9df57ca243fc292c0f0ef` |
| Evidence doc | `ISEO-SU-GLOSSARY-BATCH-04-DB-BACKUP-AND-ROLLBACK-v1.md` |

See backup evidence for overwrite incident + reconstruction.

## 15. Dry Run

| Gate | Result |
|------|--------|
| Matched == target | PASS (54) |
| Draft / glossary only | PASS |
| Collisions / skipped | 0 |
| Duplicate IDs | 0 |
| Verdict | **PASS** |

## 16. Production Apply

| Wave | Updated OK | Failed | Tool |
|------|-----------:|-------:|------|
| Batch 04 full | 54 | 0 | `glossary-batch-content-updater.py --batch 04 --mode apply` |
| COMPLEX deepen | 3 | 0 | same updater `--only-source` BERT / BM25 / Neural Matching |

Status forced `draft` on every update.

## 17. Visual QA

Authenticated admin-preview samples: **17/17 PASS** (+ 3 prior-batch regressions PASS).

Coverage: SIMPLE×5, MODERATE×8, COMPLEX×4, rename×2; plus Nofollow (B01), Частотность запроса (B02), Видимость сайта (B03).

## 18. Corpus QA

Full populated corpus (**184**): **PASS** after COMPLEX deepen (0 blockers).

## 19. Final Safe Content Corpus

| Metric | Count |
|--------|------:|
| Source records | **241** |
| Populated canonical articles | **184** |
| Publication-eligible | **184** |
| MERGED | **30** |
| DEFERRED | **14** |
| EXCLUDED | **13** |
| Published | **0** |

## 20. Public Boundary

Anonymous `/glossary/` → **404**. Published glossary → **0**. No menu/sitemap/CSS/template mutation.

## 21. Rollback

Restore allowlisted draft fields from Storage snapshot / reconstructed empty baseline via WP REST/admin. Never publish during rollback.

## 22. Remaining Non-Public Records

**57** non-eligible drafts remain (MERGED 30 + DEFERRED 14 + EXCLUDED 13). Keep as provenance drafts; no fake copy; no delete in this task.

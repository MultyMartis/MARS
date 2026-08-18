# ISEO-SU GLOSSARY BATCH 03 MANIFEST v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-BATCH-03  
**Date:** 2026-07-26  
**Publication:** **not performed** — all targets remain `draft`

---

## 1. Batch Status

| Field | Value |
|-------|-------|
| Status | **LOADED AS DRAFTS** |
| Terms | **55** (target 50–60) |
| Applied | **55 / 55** |
| Failed | **0** |
| Renames observed | **9** |
| Public exposure | still closed (`/glossary/` anonymous **404**) |
| Menu / sitemap | unchanged / still excluded |
| New CSS/JS | none |

## 2. Starting State

| Metric | Count |
|--------|------:|
| Glossary drafts | **241** |
| Published | **0** |
| Batch 01 populated | **30** |
| Batch 02 populated | **45** |
| Populated before Batch 03 | **75** |
| Remaining publication-pool candidates | **118** |

Full Beget backup: **OPERATOR CONFIRMED** before task.

## 3. Selection Logic

- Exclude Batch 01/02, MERGED, DEFERRED, EXCLUDED.
- Prefer foundational / commercially useful MEDIUM terms with category diversity.
- Skip DA / DR / PageRank (third-party metric framing deferred since Batch 02).
- Skip AMP, Лид, PBN, Neural Matching for this batch.
- Exact allowlist of **55** source terms in `_glossary-scratch/batch03-selection-final.json`.

## 4. Selected Terms

See `data/glossary-editorial/ISEO-SU-GLOSSARY-BATCH-03-CONTENT-v1.csv` and `content/glossary/batch-03/`.

Disposition: APPROVED **45** + APPROVED_RENAME **10**.

## 5. Category Distribution

| Category | Count |
|----------|------:|
| SEO fundamentals | 16 |
| search engines and indexing | 13 |
| content and semantics | 9 |
| link building | 8 |
| technical SEO | 4 |
| digital marketing | 2 |
| security and infrastructure | 2 |
| AI search and GEO | 1 |

## 6. Depth Distribution

| Depth | Count |
|-------|------:|
| SIMPLE | 13 |
| MODERATE | 39 |
| COMPLEX | 3 |

COMPLEX: Краулинговый бюджет; Алгоритм ранжирования; RankBrain.

## 7. Renames

Dry-run/apply observed **9** title renames to canonical (APPROVED_RENAME set). Slug collisions: **0**.

## 8. Research Requirements

Fact-sensitive entries added to `ISEO-SU-GLOSSARY-RESEARCH-REGISTER-v1.md` (Batch 03 section): RankBrain, crawl budget, Disavow, FAQ schema, Mixed content, ИКС, Panda/Penguin, Минусинск/Баден-Баден, TF-IDF, etc.

## 9. WordPress Targets

- CPT `glossary` only; 55/55 matched existing drafts.
- Tool: `tools/glossary-batch-content-updater.py --batch 03`
- No create; no publish; status forced `draft`.

## 10. Scoped Backup

| Field | Value |
|-------|-------|
| Path | `X:\AI MARS STORAGE\iseo-su-site-ops\glossary-db-backups\glossary-batch03-20260726-165359\` |
| Targets | **55** |
| Bytes | 54987 |
| Evidence | `ISEO-SU-GLOSSARY-BATCH-03-DB-BACKUP-AND-ROLLBACK-v1.md` |
| Raw snapshot | **NOT COMMITTED** |

## 11. Dry Run

| Gate | Result |
|------|--------|
| Target in 50–60 | PASS (55) |
| Matched == target | PASS |
| Draft / glossary only | PASS |
| Slug collisions | 0 |
| Duplicate target IDs | 0 |
| Verdict | **PASS** |

## 12. Production Apply

| Wave | Updated OK | Failed |
|------|-----------:|-------:|
| Batch 03 | 55 | 0 |

## 13. Validation

| Check | Result |
|-------|--------|
| Drafts total | 241 |
| Published | 0 |
| Populated total | **130** |
| Batch 01/02/03 | 30 / 45 / 55 |
| Visual QA | **17/17 PASS** |
| Corpus QA | **PASS** (0 issues after expansion) |
| Anon `/glossary/` | **404** |

## 14. Public Boundary

Anonymous `/glossary/` remains 404; drafts not public; no menu; no sitemap exposure.

## 15. Rollback

Restore from Storage scoped snapshot via WP REST/admin fields. Full Beget backup already exists (operator).

## 16. Remaining Corpus

| Set | Count |
|-----|------:|
| Populated production-quality | **130** |
| Remaining APPROVED | **54** |
| Remaining APPROVED_RENAME | **9** |
| Remaining publication-pool | **63** |
| MERGED | 26 |
| DEFERRED | 8 |
| EXCLUDED | 13 |

Do **not** start Batch 04 in this task.

---

*ISEO-SU Glossary Batch 03 Manifest v1 · 2026-07-26.*

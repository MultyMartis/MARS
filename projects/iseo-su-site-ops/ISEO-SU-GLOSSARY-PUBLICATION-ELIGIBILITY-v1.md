# ISEO-SU GLOSSARY PUBLICATION ELIGIBILITY v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-BATCH-04-FINAL-CONTENT-COMPLETION  
**Date:** 2026-07-26  
**Dataset:** `data/glossary-editorial/ISEO-SU-GLOSSARY-PUBLICATION-ELIGIBILITY-v1.csv`  
**Status:** **CONTENT readiness register only — NOT publication authorization**

---

## 1. Purpose

Define which of the **241** source glossary records are eligible for a **future** publication phase.

This document does **not** authorize:

- publishing glossary posts;
- opening `/glossary/` publicly;
- sitemap or menu exposure;
- related-term public link activation.

## 2. Final Content Corpus

| Metric | Count |
|--------|------:|
| Total source records | **241** |
| Populated production-quality drafts | **184** |
| Publication-eligible (`publication_eligible=YES`) | **184** |
| MERGED | **30** |
| DEFERRED | **14** |
| EXCLUDED | **13** |
| Published | **0** |

Safe content corpus status: **CONTENT COMPLETE WITH DEFERRED EDGE CASES**.

## 3. Eligibility Rules

`publication_eligible = YES` only when all hold:

- final disposition is APPROVED or APPROVED_RENAME (canonical article);
- production-quality content exists in WordPress draft;
- short definition + article body reviewed;
- canonical title/slug final;
- no factual blocker;
- SEO metadata acceptable;
- no placeholder copy.

MERGED / DEFERRED / EXCLUDED → `publication_eligible = NO`.

## 4. Eligible Canonical Articles

**184** rows with `publication_eligible=YES` in the CSV.  
These are the Batches 01–04 populated canonical drafts.

## 5. Non-Eligible Records

**57** rows (`30 + 14 + 13`).

Keep as WordPress **draft** provenance records for now. Do not populate fake public copy. Do not delete in this phase.

## 6. Merged Aliases

See final corpus CSV `merge_target` for all MERGED rows (including Batch 04 additions):

- ВЧ / СЧ / НЧ запросы → Частотность запроса
- Морда → Главная страница сайта
- УВ → Уникальный посетитель
- Процент вхождений → Плотность ключевых слов

plus prior 26 merges.

## 7. Deferred Terms

**14** total (prior 8 + Batch 04 six): СНСС; СПЕКТР; ПРЕСЕО; Отдел антиспама; Пост-фильтры; CatBoost; plus prior REVIEW deferrals.

## 8. Excluded Terms

**13** unchanged from final corpus EXCLUDED set.

## 9. WordPress State

| Metric | Value |
|--------|------:|
| Glossary CPT records | **241** |
| Status | **all draft** |
| Published | **0** |
| Anonymous `/glossary/` | **404** |

## 10. Future Publication Rules

A separate publication task must:

1. audit eligibility CSV as authority (not mere WP post existence);
2. resolve related-term linking;
3. handle MERGED aliases / redirects if needed;
4. selectively publish eligible entries;
5. decide archive, sitemap, menu;
6. run post-publication smoke.

Until that charter: **HOLD public exposure**.

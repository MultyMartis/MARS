# REPORT — ISEO-SU SITE OPS TECH SEO BACKLOG EXTRACTION 01

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-TECH-SEO-BACKLOG-EXTRACTION-01  
**Date:** 2026-08-24  
**Mode:** READ / ANALYZE / REPORT ONLY  
**Final status:** COMPLETE — ISEO-SU REMAINING TECH/SEO BACKLOG EXTRACTED / NO FIXES APPLIED

---

## 1. Источники

| # | Путь | Статус |
|---|------|--------|
| 1 | `projects/iseo-su-site-ops/audits/tech-seo/ISEO-SU-TECH-SEO-FINDINGS-v1.csv` | **Найден** (primary findings) |
| 2 | `projects/iseo-su-site-ops/ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md` | **Найден** |
| 3 | `projects/iseo-su-site-ops/reports/ISEO-SU-TECH-SEO-AUDIT-FOR-SEO-TEAM-v1.md` | **Найден** |
| 4 | `projects/iseo-su-site-ops/reports/REPORT-ISEO-SU-SITE-OPS-RECIPIENT-REMOVE-AND-TECH-SEO-AUDIT-01.md` | **Найден** |
| 5 | `projects/iseo-su-site-ops/ISEO-SU-CURRENT-STATE-v1.md` | **Найден** |
| 6 | `projects/iseo-su-site-ops/ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md` | **Найден** |
| 7 | `projects/iseo-su-site-ops/ISEO-SU-HIGH-FIX-WAVE-01-EVIDENCE-v1.md` | **Найден** |
| 8 | `projects/iseo-su-site-ops/ISEO-SU-STATIC-SITEMAP-COMPLETENESS-FIX-EVIDENCE-v1.md` | **Найден** |

Доп. сверка счётчиков (не в обязательном списке charter, но подтверждает REVIEW=14):  
`X:\AI MARS STORAGE\iseo-su-site-ops\tech-seo-audit-01\analysis-stats.json` — `status_counts.REVIEW NEEDED = 14`.

**SOURCE GAPS:** нет (все 8 обязательных источников на месте).

**Примечание по модели счётчиков:**  
MEDIUM 6 + LOW 8 + REVIEW 14 = **28 сигналов-корзин**.  
REVIEW 14 = status `REVIEW NEEDED` у **тех же** 14 unique finding_id (6+8). Это не 28 разных ID.

---

## 2. Извлечённые MEDIUM

| ID | Issue (кратко) | affected_count | Owner (CSV) | Исходный status |
|----|----------------|---------------:|-------------|-----------------|
| CANON-MISSING | Missing canonical on content-like 200 | 162 | MARS / SITE OPS | REVIEW NEEDED |
| CANON-MISMATCH | Canonical/self mismatch | 117 | MARS / SITE OPS | REVIEW NEEDED |
| SM-MISSING-INDEXABLE | Indexable absent from sitemaps | 197 | SEO REVIEW | REVIEW NEEDED → note: static subset reconciled |
| SM-NONINDEX | Sitemap URLs noindex/non-indexable | 52 | MARS / SITE OPS | REVIEW NEEDED |
| TITLE-DUP | Duplicate titles | 20 (cluster ~119 blog) | SEO REVIEW | REVIEW NEEDED |
| ORPHAN-CRAWLER | Crawler orphans (0 inlinks) | 57 | SEO REVIEW | REVIEW NEEDED |

**MEDIUM EXTRACTED: 6**

---

## 3. Извлечённые LOW

| ID | Issue (кратко) | affected_count | Owner (CSV) | Исходный status |
|----|----------------|---------------:|-------------|-----------------|
| LINK-TO-REDIR | Internal links → redirecting URLs | 129 | MARS / SITE OPS | REVIEW NEEDED |
| TITLE-LONG | Titles longer than ~70 chars | 24 | SEO REVIEW | REVIEW NEEDED |
| META-MISSING | Missing meta description | 23 | SEO REVIEW | REVIEW NEEDED |
| META-DUP | Duplicate meta descriptions | 4 (≈137 URL involvements) | SEO REVIEW | REVIEW NEEDED |
| H1-MISSING | Missing H1 (tool/hub) | 5 | MARS / SITE OPS | REVIEW NEEDED |
| IMG-HUGE | Images >1.5MB in sample | 2 | MARS / SITE OPS | REVIEW NEEDED |
| IMG-ALT | Pages with many empty/missing alt | 445 | SEO REVIEW | REVIEW NEEDED |
| OG-MISSING | Missing key Open Graph tags | 97 | MARS / SITE OPS | REVIEW NEEDED |

**LOW EXTRACTED: 8**

---

## 4. Извлечённые REVIEW

Все **14** finding_id со status `REVIEW NEEDED` (= полный список §2 + §3):

1. CANON-MISSING  
2. CANON-MISMATCH  
3. SM-MISSING-INDEXABLE  
4. SM-NONINDEX  
5. TITLE-DUP  
6. ORPHAN-CRAWLER  
7. LINK-TO-REDIR  
8. TITLE-LONG  
9. META-MISSING  
10. META-DUP  
11. H1-MISSING  
12. IMG-HUGE  
13. IMG-ALT  
14. OG-MISSING  

**REVIEW EXTRACTED: 14**  
**TOTAL EXTRACTED (корзины): 28**  
**UNIQUE FINDING IDS: 14**  
**ALL FINDING IDS PRESERVED: YES**

---

## 5. Уже закрытые пункты

Не входят в оставшийся бэклог / не reopen:

| ID / дефект | Закрытие |
|-------------|----------|
| SM-CHILD-404 (HIGH) | HIGH FIX WAVE 01 — root `/sitemap.xml` → static + wp only |
| IMG-BROKEN (HIGH) | HIGH FIX WAVE 01 — theme `/img/`; targeted recrawl PASS |
| Static sitemap completeness | Completeness FIX 01 — 127 URLs; SEO-54 + 2 legal; gate = 0 |
| SM-DUAL-ARCH (INFO) | EXPECTED BEHAVIOR (ownership split остаётся) |

---

## 6. Текущая классификация

| current_status | Count | IDs |
|----------------|------:|-----|
| OPEN_TECH | **2** | LINK-TO-REDIR, IMG-HUGE |
| SEO_REVIEW | **10** | CANON-MISSING, CANON-MISMATCH, SM-NONINDEX, TITLE-DUP, ORPHAN-CRAWLER, TITLE-LONG, META-MISSING, META-DUP, IMG-ALT, OG-MISSING |
| EXPECTED_BEHAVIOR | **1** | H1-MISSING (tool/hub candidate) |
| ALREADY_FIXED | **0** | (среди 14 unique backlog IDs) |
| SUPERSEDED | **частично 1** | SM-MISSING-INDEXABLE — static marketing subset |
| NEEDS_RECHECK | **1** | SM-MISSING-INDEXABLE (пересчёт residual после 127 static) |

Примечание: SM-MISSING-INDEXABLE учтён как **NEEDS_RECHECK** (primary), с пометкой partial SUPERSEDED для static.

---

## 7. Что может чинить MARS

Без семантического SEO (или после короткого go):

- **LINK-TO-REDIR**
- **IMG-HUGE**

После SEO-политики / списка шаблонов (реализация Site Ops):

- CANON-MISSING, CANON-MISMATCH, OG-MISSING, (опционально H1-MISSING)

---

## 8. Что требует SEO-решения

CANON-MISSING, CANON-MISMATCH, SM-MISSING-INDEXABLE, SM-NONINDEX, TITLE-DUP, ORPHAN-CRAWLER, TITLE-LONG, META-MISSING, META-DUP, IMG-ALT, OG-MISSING.

---

## 9. Что требует повторной проверки

- **SM-MISSING-INDEXABLE** — обязательно (устаревший count=197 после static completeness).  
- Mobile/CWV lab из исходного аудита остаётся LIMITED (вне 14 ID).

---

## 10. Файлы результатов

| Файл | Назначение |
|------|------------|
| `reports/ISEO-SU-TECH-SEO-REMAINING-BACKLOG-DETAILED-RU-v1.md` | Полный русский отчёт по всем находкам |
| `audits/tech-seo/ISEO-SU-TECH-SEO-REMAINING-BACKLOG-v1.csv` | Machine-readable backlog (14 unique rows) |
| `reports/REPORT-ISEO-SU-SITE-OPS-TECH-SEO-BACKLOG-EXTRACTION-01.md` | Этот operator REPORT |

---

## 11. Production mutations

**0**

Не изменялись: canonical, title, meta, H1, schema, sitemap, robots, links, images, templates, DB, WordPress, CSS, JS, PHP, forms, Metrika, glossary.

**FIXES APPLIED: 0**

---

## 12. Final decision

**COMPLETE — ISEO-SU REMAINING TECH/SEO BACKLOG EXTRACTED / NO FIXES APPLIED**

Следующий operational шаг (отдельный charter): SEO/operator приоритизация 14 ID → затем scoped Site Ops waves. Не начинать implementation из этого extraction task.

---

## FINAL HARD CHECK

```
MEDIUM EXTRACTED: 6
LOW EXTRACTED: 8
REVIEW EXTRACTED: 14

TOTAL EXTRACTED: 28
UNIQUE FINDING IDS: 14
CURRENT OPEN_TECH: 2
CURRENT SEO_REVIEW: 10
EXPECTED_BEHAVIOR: 1
ALREADY_FIXED: 0
NEEDS_RECHECK: 1
(PARTIAL SUPERSEDED: SM-MISSING-INDEXABLE static subset)

ALL FINDING IDS PRESERVED: YES
SOURCE GAPS: none
PRODUCTION MUTATIONS: 0
FIXES APPLIED: 0
RUSSIAN DETAILED REPORT CREATED: YES
CSV CREATED: YES
```

**FINAL STATUS:** COMPLETE — ISEO-SU REMAINING TECH/SEO BACKLOG EXTRACTED / NO FIXES APPLIED

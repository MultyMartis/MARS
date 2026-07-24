# ISEO-SU GLOSSARY TERM AUDIT v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-EDITORIAL-AUDIT-AND-PILOT-CONTENT-STANDARD  
**Date:** 2026-07-24  
**Source:** `materials/glossary/ISEO-SU-GLOSSARY-SOURCE-NIKITA-v1.xlsx`  
**SHA-256:** `f7651cffc5d03c497062ac6ee5b6288d9397ae5abede43fbd19f1a3ea26699de`  
**Full matrix:** `data/glossary-editorial/ISEO-SU-GLOSSARY-TERM-AUDIT-v1.csv` (241 rows, UTF-8)

---

## 1. Purpose

Editorial classification of all 241 workbook terms for readiness, business relevance, naming, and merge/exclude decisions. Definitions are **not** bulk-written in this wave — only audit + pilot.

---

## 2. Method

1. Load sanitized inventory (`glossary-terms-inventory-v1.csv`, 241 terms).
2. Apply explicit override decisions for known duplicates, product names, obsolete items, and naming issues.
3. Apply bounded heuristics for category, priority, difficulty, and expert flags.
4. Assign exactly one primary status: KEEP | MERGE | RENAME | REVIEW | EXCLUDE.
5. Record canonical title, slug proposal, merge target, synonyms (from workbook), and notes.
6. Persist full matrix as CSV; keep this Markdown as summary only.

Production WordPress was **not** modified. Draft titles were not overwritten.

---

## 3. Summary counts

### By status

| Status | Count | Meaning |
|--------|------:|---------|
| KEEP | 146 | Valid concept; keep own page |
| RENAME | 48 | Valid concept; normalize title |
| MERGE | 26 | Fold into another canonical page |
| REVIEW | 8 | Needs operator/Nikita decision |
| EXCLUDE | 13 | Not a glossary concept for public set |
| **Total** | **241** | |

**Retained concept pages (KEEP + RENAME):** 194 provisional  
**Non-published concept rows (MERGE + EXCLUDE + REVIEW pending):** 47

### By priority

| Priority | Count |
|----------|------:|
| HIGH | 43 |
| MEDIUM | 152 |
| LOW | 46 |

### By language (source title)

| Language | Approx. role |
|----------|--------------|
| RU | Majority of Cyrillic titles |
| EN | Latin abbreviations and product names |
| MIXED | Titles combining RU + EN |

Exact per-term language is in the CSV `language` column.

### Expert verification

| Flag | Count |
|------|------:|
| expert_review = YES | 34 |
| expert_review = NO | 207 |

---

## 4. Categories

| Category | Count |
|----------|------:|
| SEO fundamentals | 69 |
| technical SEO | 32 |
| link building | 30 |
| content and semantics | 29 |
| search engines and indexing | 28 |
| analytics and metrics | 20 |
| website development | 9 |
| security and infrastructure | 6 |
| contextual advertising | 5 |
| digital marketing | 5 |
| UX and conversion | 4 |
| AI search and GEO | 3 |
| other / review | 1 |
| e-commerce | 0 |

Taxonomy is intentionally coarse. No microcategories.

---

## 5. Canonicalization highlights

Examples of RENAME (full list in CSV):

| Source | Canonical |
|--------|-----------|
| Анкор (анкорный текст) | Анкорный текст |
| Аудит сайта (SEO-аудит) | SEO-аудит |
| Визит / Сессия | Сессия |
| ВЧ / СЧ / НЧ запросы | Частотность запроса |
| Запрос информационный | Информационный запрос |
| Файл robots.txt | robots.txt |
| UX/UI (юзабилити и интерфейс) | UX и UI |
| 404 ошибка | Ошибка 404 |
| PR (PageRank) | PageRank |
| DA (Domain Authority) | Domain Authority |

---

## 6. Merge highlights

| Source | Merge target |
|--------|--------------|
| Алгоритмы поисковых систем | Алгоритм ранжирования |
| Поисковая оптимизация | SEO |
| Продвижение сайта | SEO |
| Внешняя ссылка (backlink) | Обратная ссылка (backlink) → canonical «Обратная ссылка» |
| Редирект 301 / 302 | Редирект |
| Тег title / Тег description / Мета-тег Keywords | Метатеги |
| LCP / CLS / FID | Core Web Vitals |
| SSL | HTTPS |
| Юзабилити | UX/UI (→ «UX и UI») |
| ГС | Главная страница сайта |
| Гостевой постинг / Крауд-маркетинг | Аутрич (expert check) |

---

## 7. Exclusion highlights

| Source | Reason |
|--------|--------|
| d-url-rewriter.php (seo-модуль) | Product/module filename |
| Flash/Флэш | Obsolete technology |
| Яндекс Каталог (YACA) | Obsolete product |
| Лайк и шара | Colloquial phrase, not a concept |
| Обмен ссылками между проектами Исполнителя | Contractual process |
| Обмен тематически близкими ссылками | Process phrase |
| Веб-страница, Домен, Сервер, HTML, JS / JavaScript, Cookie, IP-адрес | Too generic / out of glossary scope |

Operator may override EXCLUDE → KEEP for a «fundamentals» layer if desired.

---

## 8. REVIEW queue (operator / Nikita)

| Source | Issue |
|--------|-------|
| tICF | Unclear acronym — confirm or exclude |
| Human-First Content | Positioning vs helpful-content guidance |
| MFA | Confirm RU audience usage |
| Sandbox | Myth risk — keep with busting or exclude |
| Spam Score | Proprietary Moz metric |
| Скрипт | Too vague |
| Контент | Very broad foundational term |
| Ссылка | Very broad; may defer to specific link terms |
| URL-адрес | Very basic |

---

## 9. Detected issue classes

| Class | Examples |
|-------|----------|
| Near-duplicates | SEO vs поисковая оптимизация vs продвижение сайта |
| Synonym merges | backlink variants; CWV submetrics |
| Overly broad | Контент, Ссылка, Трафик, Домен |
| Overly narrow / process | Обмен ссылками… |
| Outdated | Flash, YACA, meta keywords as ranking factor |
| EN/RU conflict | PR (ambiguous), CAPTCHA/КАПЧА, UX/UI |
| Spelling/capitalization | Mixed Dashboard/дашборд, slash titles |
| Product-as-term | Google Ads, Яндекс.Метрика (KEEP as products, define carefully) |
| Search-query phrasing | Топ-10 / Топ-3 |
| Expert verification | АГС, Минусинск, E-E-A-T, GEO, поведенческие факторы |

Exact duplicate titles in source: **0** (confirmed at intake).

---

## 10. Limits of this audit

- Classifications are editorial proposals, not production mutations.
- Heuristic categories may be refined by Nikita.
- Algorithm status notes require expert confirmation against current official docs.
- Slug proposals are orthographic helpers; final WP slugs may differ after title renames.

---

## 11. Supersession note (2026-07-25)

Operational dispositions for publication planning are now in:

- `ISEO-SU-GLOSSARY-FINAL-CORPUS-v1.md`
- `data/glossary-editorial/ISEO-SU-GLOSSARY-FINAL-CORPUS-v1.csv`

This audit file remains the historical provisional matrix (KEEP/RENAME/MERGE/REVIEW/EXCLUDE). Do not treat REVIEW as still awaiting per-term operator votes for corpus inclusion — final corpus deferred those eight independently.

## 12. Next step (historical — completed by final corpus + Batch 01)

1. ~~Operator + Nikita review status counts and REVIEW/EXCLUDE lists.~~ → MARS independent final corpus.  
2. ~~Approve pilot definitions.~~ → improved into Batch 01.  
3. ~~Separate charter for bulk definition writing / draft upload.~~ → Batch 01 loaded as drafts 2026-07-25.

---

*Glossary term audit summary v1 · 2026-07-24 · full matrix in CSV.*

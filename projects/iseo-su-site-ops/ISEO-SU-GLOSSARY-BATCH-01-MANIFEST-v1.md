# ISEO-SU GLOSSARY BATCH 01 MANIFEST v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-FINAL-CORPUS-AND-BATCH-01-CONTENT  
**Date:** 2026-07-25  
**Publication:** **not performed** — all targets remain `draft`  

---

## 1. Batch Status

| Field | Value |
|-------|-------|
| Status | **LOADED AS DRAFTS** |
| Terms | **30** (target 28–32) |
| Applied | **30 / 30** |
| Failed | **0** |
| Public exposure | still closed (`/glossary/` anonymous **404**) |
| Menu / sitemap | unchanged / still excluded |
| New CSS/JS | none |

## 2. Selection Logic

- Foundational concepts first (SEO, indexing/crawl, technical basics).
- Mix of categories: fundamentals, technical, links, analytics, advertising, AI/GEO.
- Include improved former pilot set where it still passes the standard.
- Prefer factual stability; avoid deferred REVIEW/EXCLUDE items.
- Avoid 30 near-identical SEO synonyms.
- Russian + established Latin abbreviations where industry-normal.

## 3. Terms Included

| # | Source | Canonical | Post ID | Slug | Category |
|---|--------|-----------|--------:|------|----------|
| 1 | SEO | SEO | 2670 | `seo` | SEO fundamentals |
| 2 | Анкор (анкорный текст) | Анкорный текст | 2448 | `ankornyj-tekst` | link building |
| 3 | Файл robots.txt | robots.txt | 2603 | `robots-txt` | technical SEO |
| 4 | CTR (кликабельность) | CTR | 2632 | `ctr` | analytics and metrics |
| 5 | Семантическое ядро | Семантическое ядро | 2570 | `semanticheskoe-yadro` | content and semantics |
| 6 | Pay-per-Click (PPC) | PPC | 2663 | `ppc` | contextual advertising |
| 7 | GEO | GEO | 2642 | `geo` | AI search and GEO |
| 8 | Обратная ссылка (backlink) | Обратная ссылка | 2534 | `obratnaya-ssylka` | link building |
| 9 | Отказы (показатель отказов) | Показатель отказов | 2539 | `pokazatel-otkazov` | analytics and metrics |
| 10 | Core Web Vitals | Core Web Vitals | 2628 | `core-web-vitals` | technical SEO |
| 11 | E-E-A-T | E-E-A-T | 2637 | `e-e-a-t` | SEO fundamentals |
| 12 | Канонический URL (canonical) | Канонический URL | 2500 | `kanonicheskij-url` | technical SEO |
| 13 | Индексация | Индексация | 2496 | `indeksacziya` | search engines and indexing |
| 14 | Краулинг | Краулинг | 2514 | `krauling` | search engines and indexing |
| 15 | Noindex | Noindex | 2662 | `noindex` | technical SEO |
| 16 | Карта сайта (sitemap.xml) | Карта сайта | 2502 | `karta-sajta` | technical SEO |
| 17 | HTTPS | HTTPS | 2650 | `https` | security and infrastructure |
| 18 | Метатеги | Метатеги | 2522 | `metategi` | technical SEO |
| 19 | Органический трафик | Органический трафик | 2537 | `organicheskij-trafik` | SEO fundamentals |
| 20 | Поисковая выдача (SERP) | Поисковая выдача | 2549 | `poiskovaya-vydacha` | search engines and indexing |
| 21 | Интент | Поисковый интент | 2497 | `poiskovyj-intent` | content and semantics |
| 22 | Атрибут rel="nofollow" | Nofollow | 2451 | `nofollow` | link building |
| 23 | Ссылочный профиль | Ссылочный профиль | 2585 | `ssylochnyj-profil` | link building |
| 24 | Техническая оптимизация | Техническая оптимизация | 2592 | `tehnicheskaya-optimizacziya` | technical SEO |
| 25 | Google Search Console | Google Search Console | 2647 | `google-search-console` | search engines and indexing |
| 26 | Яндекс.Метрика | Яндекс.Метрика | 2619 | `yandeks-metrika` | analytics and metrics |
| 27 | Конверсия | Конверсия | 2507 | `konversiya` | analytics and metrics |
| 28 | Сниппет | Сниппет | 2576 | `snippet` | search engines and indexing |
| 29 | Редирект | Редирект | 2562 | `redirekt` | technical SEO |
| 30 | Дубли страниц | Дубли страниц | 2486 | `dubli-stranicz` | technical SEO |

## 4. Renames

Count: **11** (dry-run planned renames: 11).

| Source title | Canonical title | Post ID |
|--------------|-----------------|--------:|
| Анкор (анкорный текст) | Анкорный текст | 2448 |
| Файл robots.txt | robots.txt | 2603 |
| CTR (кликабельность) | CTR | 2632 |
| Pay-per-Click (PPC) | PPC | 2663 |
| Обратная ссылка (backlink) | Обратная ссылка | 2534 |
| Отказы (показатель отказов) | Показатель отказов | 2539 |
| Канонический URL (canonical) | Канонический URL | 2500 |
| Карта сайта (sitemap.xml) | Карта сайта | 2502 |
| Поисковая выдача (SERP) | Поисковая выдача | 2549 |
| Интент | Поисковый интент | 2497 |
| Атрибут rel="nofollow" | Nofollow | 2451 |

## 5. Source Verification

See `ISEO-SU-GLOSSARY-RESEARCH-REGISTER-v1.md`. Fact-sensitive wording checked against primary framing (Search Central / web.dev / Yandex product docs / HTML semantics). GEO marked provisional.

## 6. WordPress Targets

- CPT: `glossary` only.
- Matched existing drafts by source title (import titles).
- No new posts created.
- No non-Batch-01 drafts mutated.
- Tool: `tools/glossary-batch01-content-updater.py` (in-page authenticated REST + admin ACF/Yoast).

## 7. Dry Run

| Gate | Result |
|------|--------|
| Target count | 30 |
| Matched | 30 |
| Renames | 11 |
| Content/excerpt/ACF/Yoast updates planned | 30 each |
| Skipped | 0 |
| Collisions | 0 |
| Verdict | **PASS** |

Evidence: `_glossary-scratch/batch01-wp/dry-run-plan.json`

## 8. Apply Result

| Field | Value |
|-------|-------|
| Mode | apply |
| Updated OK | 30 |
| Failed | 0 |
| Receipt ok | True |

Evidence: `_glossary-scratch/batch01-wp/receipt.json`

## 9. Rendering Validation

Eight authenticated previews inspected:

| Term | H1 | Intro strong | Paragraphs | Synonyms H2 | Leak/broken |
|------|----|--------------|------------|-------------|-------------|
| SEO | SEO | True | 7 | True | leak=False broken=False |
| Файл robots.txt | robots.txt | True | 7 | True | leak=False broken=False |
| CTR (кликабельность) | CTR | True | 7 | True | leak=False broken=False |
| Яндекс.Метрика | Яндекс.Метрика | True | 7 | True | leak=False broken=False |
| Core Web Vitals | Core Web Vitals | True | 7 | True | leak=False broken=False |
| Анкор (анкорный текст) | Анкорный текст | True | 6 | True | leak=False broken=False |
| E-E-A-T | E-E-A-T | True | 7 | True | leak=False broken=False |
| Канонический URL (canonical) | Канонический URL | True | 7 | True | leak=False broken=False |

No template correction required. No new CSS.

## 10. SEO Fields

For each term: SEO title + meta description prepared in content files and written to Yoast fields where admin selectors were available. Document titles observed on preview match prepared SEO titles for sampled terms.

Indexation recommendation for future publish gate: indexable after public exposure enablement **and** editorial publish approval — currently **do not index** (drafts + public archive closed).

## 11. Internal Linking

- Related terms stored as editorial plain-text lists in article bodies (`Связанные понятия: …`).
- **No draft-to-draft public hyperlinks emitted** (avoids accidental public exposure of draft URLs).
- Future: convert related-term lists to safe links only after publication or authenticated-only link policy is approved.

## 12. Rollback

See `ISEO-SU-GLOSSARY-BATCH-01-ROLLBACK-v1.md` and sanitized snapshot `data/glossary-editorial/ISEO-SU-GLOSSARY-BATCH-01-PREWRITE-SNAPSHOT-v1.json`.

## 13. Publication State

| Check | Result |
|-------|--------|
| All Batch 01 still draft | **YES** |
| Anonymous `/glossary/` | **404** |
| Auth archive preview | **241** list items |
| Menu link | absent |
| Sitemap exposure | still disabled by exposure flag |

## 14. Remaining Issues

- Privacy regression path is `/privacy-policy.html` (not `/privacy-policy/`).
- Some WP slugs are transliterated (e.g. `robots-txt` instead of `robots.txt`) — acceptable; do not force unsafe slug fights.
- GEO and Показатель отказов remain expert-sensitive; fine for drafts, polish before publish.
- Batch 02 not started.

*ISEO-SU Glossary Batch 01 Manifest v1 · 2026-07-25.*

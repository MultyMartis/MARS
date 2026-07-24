# ISEO-SU GLOSSARY RESEARCH REGISTER v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-FINAL-CORPUS-AND-BATCH-01-CONTENT  
**Date:** 2026-07-25  
**Scope:** Batch 01 fact-sensitive terms  
**Rule:** Sources verify facts; publishable copy is original. No large copyrighted passages reproduced.

---

## 1. Method

- Prefer first-party documentation (Google Search Central, web.dev, Yandex Help, vendor product docs, WHATWG/MDN where relevant).
- Do not treat SEO blogs as primary evidence when first-party docs exist.
- Record access/review date as **2026-07-25**.
- Remaining uncertainty stays in notes; do not invent ranking formulas.

---

## 2. Authoritative source classes used

| Class | Examples | Use in Batch 01 |
|-------|----------|-----------------|
| Google Search / quality | Google Search Central; Google Search Quality Rater Guidelines framing | robots/crawl vs index, canonical, E-E-A-T, CWV, GSC role, noindex, snippets |
| Chrome / web.dev | Core Web Vitals / INP documentation | LCP, CLS, INP; FID historical |
| Yandex | Yandex Metrica help; Webmaster concepts where general | Показатель отказов ≠ bounce; Метрика product role |
| Web platform | HTML link/`rel` semantics; HTTPS/TLS naming | Nofollow, HTTPS vs SSL naming |
| Industry terminology | GEO as emerging practice label | Marked provisional; not a formal SE standard |
| Advertising model | General PPC model (platform-agnostic) | PPC definition without fake bid formulas |

---

## 3. Term-level research notes (Batch 01)

| Canonical term | Verified | Authoritative framing | Affects wording? | Remaining uncertainty |
|----------------|----------|----------------------|------------------|------------------------|
| SEO | Organic vs paid distinction | Industry + Search Central organic framing | Yes — no ranking guarantees | Exact factor weights unknown (always) |
| robots.txt | Crawl hints ≠ secrecy ≠ noindex | Search Central / robots exclusion practice | Yes | Engine-specific edge cases |
| Noindex | Indexing directive vs crawl disallow | Search Central robots meta / X-Robots-Tag | Yes | Exact compliance nuances by bot |
| Краулинг / Индексация | Distinct stages | Search Central crawl/index model | Yes | Per-URL scheduling opaque |
| Карта сайта | Discovery hint, not index guarantee | Sitemaps protocol + Search Central | Mild | Priority/changefreq limited effect |
| Канонический URL | Preference signal ≠ 301 | Search Central canonicalization | Yes | Engines may choose another URL |
| Редирект | 301 permanent vs 302 temporary intent | HTTP semantics + Search Central redirects | Yes | Signal consolidation timing |
| Дубли страниц | Multi-URL same/near content | Canonicalization guidance | Mild | When near-duplicates should stay separate |
| Core Web Vitals | LCP, CLS, INP; FID historical | web.dev / Chrome CWV docs | Yes | Not sole ranking signal |
| E-E-A-T | Rater concept; not GSC numeric score | Quality Rater Guidelines framing | Yes | How systems approximate trust signals |
| GEO | Industry term; not geo-targeting | Industry usage 2024–2026 | Yes — provisional | No single official standard |
| Показатель отказов | Metrika «отказ» ≠ classic bounce | Yandex Metrica methodology | Yes | Exact current Metrika thresholds — confirm in product help before publish polish |
| CTR | clicks/impressions | Analytics definition | Mild | No universal “good CTR” |
| Сниппет | Engine may rewrite description | Search Central snippet behavior | Yes | Rich-result eligibility changes |
| Метатеги | meta keywords not modern ranking lever | Long-standing Search Central guidance | Yes | |
| Nofollow | Link signal / non-endorsement hint | `rel` semantics + Search Central link attributes | Mild | Sponsored/ugc interplay details |
| HTTPS | Transport encryption; SSL historical name | TLS practice | Mild | |
| Google Search Console | Diagnostics, not position control | GSC product docs | Yes | |
| Яндекс.Метрика | Analytics product | Yandex Metrica docs | Mild | Report methodologies evolve |
| PPC | Pay-per-click commercial model | Platform-agnostic | Mild | Billing rules vary by network |
| Remaining Batch 01 terms | Conceptual / methodological | Editorial standard + prior pilot | Mild | Audience-fit wording only |

---

## 4. Deliberately unused as primary evidence

- Low-quality SEO listicles claiming secret ranking factors.
- Invented percentage lifts or “guaranteed top-10” claims.
- Third-party DA/DR as if official Google/Yandex scores (out of Batch 01; disclosed if used later).

---

## 5. Next research actions (non-blocking)

1. Before publication polish: re-check Yandex Metrica current definition of «отказ».
2. Before GEO publication: confirm operator comfort with provisional industry framing.
3. Re-check CWV documentation if Google changes the metric set again.

---

*ISEO-SU Glossary Research Register v1 · 2026-07-25 · editorial only.*

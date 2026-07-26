# ISEO-SU GLOSSARY RESEARCH REGISTER v1

**Programme:** ISEO-SU-SITE-OPS  
**Tasks:** FINAL-CORPUS-AND-BATCH-01-CONTENT; BATCH-01-REFINEMENT-AND-BATCH-02; GLOSSARY-BATCH-03  
**Dates:** 2026-07-25; Batch 03 2026-07-26  
**Scope:** Batch 01 + Batch 02 + Batch 03 fact-sensitive terms  
**Rule:** Sources verify facts; publishable copy is original. No large copyrighted passages reproduced.

---

## 1. Method

- Prefer first-party documentation (Google Search Central, web.dev, Yandex Help, vendor product docs, WHATWG/MDN where relevant).
- Do not treat SEO blogs as primary evidence when first-party docs exist.
- Record access/review date as **2026-07-25**.
- Remaining uncertainty stays in notes; do not invent ranking formulas.

---

## 2. Authoritative source classes used

| Class | Examples | Use |
|-------|----------|-----|
| Google Search / quality | Google Search Central; Quality Rater Guidelines framing | robots/crawl vs index, canonical, E-E-A-T, CWV, GSC, noindex, snippets, mobile-first indexing |
| Chrome / web.dev | Core Web Vitals / INP documentation | LCP, CLS, INP; FID historical |
| Yandex | Yandex Metrica / Webmaster / Direct product docs | Метрика отказы; Вебмастер role; Директ product role |
| Web platform | HTML/`rel`; HTTP status; Schema.org | Nofollow, HTTP codes, structured data eligibility |
| Industry terminology | GEO; LSI; behavioural factors | Mark provisional / methodological where not first-party standards |
| Advertising / analytics | Google Ads; GA; UTM; event tracking | Product/model framing without fake auction secrets |

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
| Remaining Batch 01 terms | Conceptual / methodological | Editorial standard | Mild | Audience-fit wording only |

---

## 4. Term-level research notes (Batch 02)

| Canonical term | Source authority | What was verified | Review date | Wording implication | Uncertainty |
|----------------|------------------|-------------------|-------------|---------------------|-------------|
| Mobile-first indexing | Google Search Central | Google predominantly uses mobile content for indexing/ranking signals | 2026-07-25 | Emphasize content parity on mobile; not “mobile beauty = ranking” | Exact ranking weight unknown |
| Микроразметка | Schema.org + Search Central rich-results framing | Structured data can enable enhancements; not a ranking guarantee | 2026-07-25 | Eligibility / enhancement language | Feature eligibility changes |
| Поведенческие факторы | Industry practice; no public full formula | Separate site analytics from unpublished ranking signals; no weights | 2026-07-25 | COMPLEX; anti-fraud / anti-guarantee | Engine-specific opacity |
| Google Ads / Яндекс Директ | Vendor product docs (role-level) | Advertising platforms; auction/billing details vary | 2026-07-25 | Product role, not secret auction math | Campaign rule changes |
| Поисковая контекстная реклама | Industry + vendor framing | Paid search ads vs organic | 2026-07-25 | Clear paid vs organic split | |
| LSI | Industry methodological term | Not a Google-published factor checklist | 2026-07-25 | Methodological / related-term language | Overclaim risk |
| HTTP-код ответа | HTTP semantics / MDN-class framing | Status classes and common SEO-relevant codes | 2026-07-25 | Concrete code meanings | |
| Ошибка 404 | HTTP 404 semantics | Not found; soft-404 risks mentioned carefully | 2026-07-25 | Useful vs broken 404 pages | Soft-404 detection details |
| UTM-метки | Analytics campaign tagging practice | Campaign parameters for attribution | 2026-07-25 | Tracking hygiene; not ranking | |
| Event tracking | Analytics event model | Custom events vs pageviews | 2026-07-25 | Implementation depends on tool | |
| Google Analytics | Google Analytics product role | Site analytics; not Search Console | 2026-07-25 | Distinguish analytics vs search diagnostics | GA4 report specifics evolve |
| Яндекс.Вебмастер | Yandex Webmaster product role | Indexing/diagnostics for Yandex | 2026-07-25 | Parallel to GSC role language | |
| Поисковый робот | Crawl model | Crawler discovers/fetches URLs | 2026-07-25 | Distinct from indexing | |
| Ранжирование | Search Central / industry | Ordering of results; opaque multi-signal systems | 2026-07-25 | No factor lists as fact | |
| ROI / ROMI / CPA / CPC / CPL / KPI / LTV | Finance/marketing definitions | Metric definitions and distinctions | 2026-07-25 | Clear formulas; no fake benchmarks | Business-specific thresholds |
| Remaining Batch 02 terms | Editorial / methodological | Audience-fit accuracy | 2026-07-25 | Depth SIMPLE/MODERATE as assigned | |

---

## 5. Term-level research notes (Batch 03)

| Canonical term | Source authority | What was verified | Review date | Wording implication | Uncertainty |
|----------------|------------------|-------------------|-------------|---------------------|-------------|
| RankBrain | Google historical Search Central / public ML framing | ML component for query/document interpretation; not a webmaster toggle | 2026-07-26 | COMPLEX; no claimed weights; not Yandex | Current architecture opacity |
| Краулинговый бюджет | Google Search Central crawl budget guidance | Meaningful mainly for large sites; crawl ≠ index guarantee | 2026-07-26 | COMPLEX; avoid fake quotas | Exact site quotas unpublished |
| Disavow | Google Search Console Disavow docs | Extreme measure for toxic inbound links | 2026-07-26 | Cautionary; not daily routine; no identical Yandex twin | Mis-file risk |
| FAQ-разметка | Schema.org FAQPage + Search Central rich-results | May enable enhancements; not ranking guarantee | 2026-07-26 | Eligibility / no guarantee language | Feature eligibility changes |
| Mixed content | web.dev / browser mixed content rules | HTTPS page loading HTTP assets can be blocked | 2026-07-26 | Security/UX framing, not SEO myth | — |
| ИКС | Yandex Webmaster product framing | Yandex site quality index; not Google metric | 2026-07-26 | Explicit Yandex-only | Formula incomplete |
| Google Panda | Historical Google quality update framing | Quality/thin content history; continuum today | 2026-07-26 | Historical; not Yandex | Current naming/integration |
| Google Penguin | Historical Google link-spam update | Link spam focus; later more continuous | 2026-07-26 | Historical; not Yandex | — |
| Минусинск | Yandex public anti-paid-link framing | Yandex link-spam measure; not Penguin | 2026-07-26 | Keep ecosystems separate | Exact thresholds |
| Баден-Баден | Yandex text-quality / over-optimization framing | Yandex content quality measure; not Panda | 2026-07-26 | Keep ecosystems separate | Exact thresholds |
| Алгоритм ранжирования | Search Central / industry | Opaque multi-signal systems; updates | 2026-07-26 | COMPLEX; no factor lists as fact | Always |
| TF-IDF | Classical IR literature | Classic statistic; not modern SEO silver bullet | 2026-07-26 | Methodological caution | — |
| Скорость загрузки страницы | web.dev / CWV ecosystem | Lab/field metrics; not sole ranking factor | 2026-07-26 | Tie to CWV carefully | Weights unknown |
| Remaining Batch 03 terms | Editorial / methodological | Audience-fit accuracy | 2026-07-26 | Depth as assigned | |

---

## 6. Deliberately unused as primary evidence

- Low-quality SEO listicles claiming secret ranking factors.
- Invented percentage lifts or “guaranteed top-10” claims.
- Third-party DA/DR as if official Google/Yandex scores (**still deferred**; excluded from Batch 03).

---

## 7. Next research actions (non-blocking)

1. Before publication polish: re-check Yandex Metrica current definition of «отказ».
2. Before GEO publication: confirm operator comfort with provisional industry framing.
3. Re-check CWV / mobile-first docs if Google changes framing again.
4. Before publishing Поведенческие факторы / RankBrain: expert/operator comfort with COMPLEX provisional framing.
5. Before any DA/DR/PageRank articles: decide third-party metric framing charter.

---

*ISEO-SU Glossary Research Register v1 · updated Batch 03 2026-07-26 · editorial only.*

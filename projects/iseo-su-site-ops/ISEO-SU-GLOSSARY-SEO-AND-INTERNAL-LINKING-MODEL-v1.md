# ISEO-SU GLOSSARY SEO AND INTERNAL LINKING MODEL v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-EDITORIAL-AUDIT-AND-PILOT-CONTENT-STANDARD  
**Date:** 2026-07-24 (updated 2026-07-25 Batch 01)  
**Status:** ACTIVE FOR DRAFT PRODUCTION  

Companion: `ISEO-SU-GLOSSARY-EDITORIAL-STANDARD-v1.md`  
Architecture URL gate: `ISEO_GLOSSARY_PUBLIC_EXPOSURE` (currently false)
Final corpus: `ISEO-SU-GLOSSARY-FINAL-CORPUS-v1.md`

---

## 1. URL and Canonical Model

| Surface | Pattern | Notes |
|---------|---------|-------|
| Archive | `/glossary/` | Closed to anonymous users while gate is false |
| Single | `/glossary/{slug}/` | CPT rewrite; slash URLs aligned with `offer` |
| Canonical title | one per concept | From audit `canonical_term` |
| Canonical slug | derived from canonical title | Stored in audit CSV; may be adjusted before publish |

Rules:

- MERGED terms do not get independent public URLs.
- APPROVED_RENAME uses the new canonical title/slug; Batch 01 already renamed matching drafts where applicable.
- Do not invent `.html` glossary URLs unless operator revisits G-U-002.
- Self-canonical on published singles; no cross-domain glossary mirrors.
- While drafts remain unpublished, related-term relationships may be stored as plain text; do not emit public draft-to-draft hyperlinks that could leak draft URLs.

---

## 2. Indexation Rules

Pre-publication (current production state):

- drafts only;
- anonymous archive/singles not publicly exposed;
- robots/noindex controls and sitemap exclusion while gate closed.

After intentional publication of a term:

| Decision | When |
|----------|------|
| **Indexable** | KEEP/RENAME, complete definition, unique intent, no thin content |
| **Noindex** | temporary QA, duplicate risk unresolved, or operator HOLD |
| **Not published** | MERGE / EXCLUDE / unresolved REVIEW |

Do not index empty definitions. Do not open the archive until a meaningful batch is ready.

---

## 3. Title Rules

Proposed SEO title pattern:

`{Canonical term} — что это и зачем нужно | i-seo.su`

Variants allowed:

- `{Canonical term}: определение и применение`
- `{Canonical term} в SEO — простое объяснение`

Constraints:

- lead with the term users search;
- keep readable length (prefer ≤ ~60–70 characters where practical);
- no keyword stuffing;
- no ALL CAPS;
- abbreviations OK when they are the query (CTR, SEO, PPC).

---

## 4. Meta Description Rules

- 140–160 characters preferred (flexible).
- Answer «что это» + one practical benefit.
- Natural Russian; one primary phrase.
- No call-to-action spam («закажите SEO сейчас»).
- No meta descriptions for EXCLUDE terms.
- MERGE terms inherit the canonical page meta; no separate metas.

---

## 5. Keyword Use

Workbook columns «Ключевые слова» and «LSI-фразы» are **hints**.

Allowed:

- use the primary phrase naturally in H1/title, short definition, and once in the body;
- use variants where they read normally.

Forbidden:

- dumping LSI lists into the article;
- repeating the same stem in every sentence;
- treating every workbook keyword as mandatory.

---

## 6. Synonym Handling

- Synonyms appear in ACF `glossary_synonyms` and optionally in a short body line.
- Do not create separate indexable pages for synonyms (MERGE).
- If a synonym is a common query, ensure the canonical page title/meta covers it naturally or accept that the synonym query may land via related content later.
- Brand/product names (Google Ads, Яндекс.Метрика) are canonical product terms, not synonyms of generic «реклама».

---

## 7. Internal Linking

Link types:

1. **Glossary ↔ glossary** — related terms block (3–7 links).
2. **Glossary → service/blog** — only when a real matching page exists and the link helps the reader; do not force commercial links in every term.
3. **Service/blog → glossary** — later content waves; not required for pilot.

Rules:

- anchor text = natural term name;
- no identical mass anchors across the site;
- do not link MERGE/EXCLUDE targets;
- prefer contrast pairs (404 vs 410, UX vs UI, ROI vs ROMI).

---

## 8. Related Terms

Related-term selection criteria:

- shared category or parent concept;
- frequent confusion pair;
- prerequisite concept (e.g. индексация → краулинг);
- metric ↔ tool (CTR → сниппет / SERP).

Store planned relations in pilot notes and future editorial sheets. Bidirectional UI remains optional (G-U-003).

---

## 9. Cannibalization Prevention

High-risk clusters (one winner page):

| Cluster | Winner (provisional) | Absorb |
|---------|----------------------|--------|
| SEO / поисковая оптимизация / продвижение сайта | SEO | Russian aliases as synonyms |
| Алгоритм ранжирования / алгоритмы ПС | Алгоритм ранжирования | plural as synonym |
| Метатеги / title / description / keywords | Метатеги | tag-specific sections |
| Core Web Vitals / LCP / CLS / FID | Core Web Vitals | sub-metrics as sections |
| Редирект / 301 / 302 | Редирект | status subtypes |
| HTTPS / SSL | HTTPS | SSL as related |
| UX/UI / юзабилити | UX и UI | merge duplicate |
| Обратная ссылка / внешняя ссылка / backlink | Обратная ссылка | synonyms |

Before publishing a new term, check the audit CSV for MERGE targets and overlapping intents.

---

## 10. Publication Batches

Recommended sequence (after operator/Nikita approve pilot):

1. **Pilot publish rehearsal (still draft upload optional)** — 10–15 pilot terms content only.
2. **Foundation batch** — high-priority SIMPLE/MODERATE KEEP+RENAME.
3. **Technical batch** — tech SEO + search engines.
4. **Links & risk batch** — link building, filters, PBN (neutral risk language).
5. **Expert/algorithm batch** — after expert verification.
6. **Archive open** — only when a coherent set is live and QA’d.

Each batch requires:

- fresh Beget backup for WP mutation waves;
- explicit charter;
- drafts remain drafts until intentional publish;
- public gate decision separate from content upload.

---

*ISEO-SU Glossary SEO and Internal Linking Model v1 · 2026-07-24.*

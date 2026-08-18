# ISEO-SU GLOSSARY SEO AND INTERNAL LINKING MODEL v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-EDITORIAL-AUDIT-AND-PILOT-CONTENT-STANDARD  
**Date:** 2026-07-24 (updated 2026-07-26 controlled launch)  
**Status:** ACTIVE FOR PUBLIC GLOSSARY  

Companion: `ISEO-SU-GLOSSARY-EDITORIAL-STANDARD-v1.md`  
Architecture URL gate: `ISEO_GLOSSARY_PUBLIC_EXPOSURE` (**true** after 2026-07-26 launch)  
Final corpus: `ISEO-SU-GLOSSARY-FINAL-CORPUS-v1.md`  
Launch: `ISEO-SU-GLOSSARY-PUBLICATION-LAUNCH-MANIFEST-v1.md`

---

## 1. URL and Canonical Model

| Surface | Pattern | Notes |
|---------|---------|-------|
| Archive | `/glossary/` | Public hub (published eligible only) |
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

Post-launch (2026-07-26):

| Surface | Indexation |
|---------|------------|
| Published eligible singles | **index, follow** (default) |
| Public archive `/glossary/` | **index, follow** |
| MERGED / DEFERRED / EXCLUDED drafts | not public → not indexable |
| Yoast/wp glossary sitemap | **184** published URLs observed |

Custom `sitemap.xml` advertised in `robots.txt` remains a separate static index and was **not** modified in the launch (minimal-change).

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

1. **Glossary ↔ glossary** — related terms block (normally 2–5; zero acceptable).
2. **Glossary → service/blog** — only when a real matching page exists and the link helps the reader; do not force commercial links in every term.
3. **Service/blog → glossary** — later content waves; not required for draft batches.

Rules:

- related terms must be semantically useful; not SEO quantity;
- anchor text = natural term name;
- no identical mass anchors across the site;
- do not link MERGE / EXCLUDE / DEFERRED targets;
- prefer contrast pairs (404 vs 410, UX vs UI, ROI vs ROMI);
- public related links render only for **published eligible** canonical targets in the single-template «Связанные понятия» block (`glossary_related_terms` meta);
- MERGED aliases resolve to canonical targets when present; DEFERRED/EXCLUDED never linked;
- do not mass-insert body inline links in launch maintenance waves.

---

## 8. Related Terms

Related-term selection criteria:

- shared category or parent concept;
- frequent confusion pair;
- prerequisite concept (e.g. индексация → краулинг);
- metric ↔ tool (CTR → сниппет / SERP).

Store planned relations in editorial sheets and article metadata. Bidirectional UI remains optional (G-U-003).

---

## 8A. Publication Eligibility (per-entry)

**PUBLICATION_ELIGIBILITY = per-entry approved content state**

A post existing in the `glossary` CPT is not enough. An entry may become public only when:

- disposition APPROVED / APPROVED_RENAME;
- reviewed short definition + body present;
- no placeholder copy;
- slug/title/SEO metadata acceptable;
- intentional publish decision for that entry.

Global CPT exposure must never publish all 241 drafts by default.

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

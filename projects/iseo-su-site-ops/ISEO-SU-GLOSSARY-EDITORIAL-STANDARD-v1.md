# ISEO-SU GLOSSARY EDITORIAL STANDARD v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-EDITORIAL-AUDIT-AND-PILOT-CONTENT-STANDARD  
**Site:** https://i-seo.su/  
**Date:** 2026-07-24  
**Status:** DRAFT FOR OPERATOR / NIKITA REVIEW  

---

## 1. Purpose

This standard defines how glossary definitions for i-seo.su are written, reviewed, and prepared for publication.

Goals:

- explain professional SEO and digital-marketing concepts accurately;
- remain understandable to business owners and non-specialists;
- stay neutral and free of sales pitches;
- support editorial SEO without keyword stuffing;
- keep one concept per page after audit decisions (KEEP / MERGE / RENAME).

This document governs **editorial content**. It does not authorize WordPress uploads or public exposure.

---

## 2. Audience

Primary readers:

- business owners and marketing managers evaluating SEO;
- site owners who need plain-language explanations;
- specialists who want a precise local reference.

Tone: professional, calm, practical. Prefer plain Russian. Keep English abbreviations when they are industry-standard (SEO, CTR, PPC, robots.txt), and explain them on first use.

---

## 3. Definition Structure

Every normal glossary term uses this structure (section headings may be light or omitted in final HTML if the flow stays clear):

1. **Short definition** — 1–2 sentences answering «что это?»; suitable as WordPress excerpt / archive teaser.
2. **Expanded explanation** — purpose and context in plain Russian; technically accurate.
3. **Why it matters** — practical relevance for a business or website owner.
4. **How it works / how it is used** — only when it adds clarity.
5. **Example** — concrete, realistic, without invented performance claims.
6. **Related terms** — planned internal glossary links only (from retained terms).
7. **Synonyms / alternative names** — genuine equivalents only.
8. **Important distinction** — when the term is commonly confused with another.

Not every section is mandatory for every term. SIMPLE terms may stop after short definition + brief expansion + related terms. EXPERT terms may use the full set.

---

## 4. Length Model

Flexible length by complexity. Do not pad.

| Layer | Guidance |
|-------|----------|
| Short definition | 160–300 characters |
| Full SIMPLE term | ~700–1,500 characters |
| Full MODERATE term | ~1,500–3,000 characters |
| Full EXPERT term | up to ~4,500 characters when justified |

Character counts are editorial guidance, not hard quotas. Prefer clarity over length.

---

## 5. Writing Style

- Lead with the meaning; do not open with history unless history is the point.
- Prefer active, concrete wording.
- Use ordinary Russian punctuation and quotation marks («»).
- Expand abbreviations on first mention when helpful: «CTR (кликабельность)».
- Use lists sparingly and only for clarity.
- Keep one H1 (term title); body uses H2/H3 only if the CMS layout needs them.

Avoid:

- «это когда» as the main definition pattern;
- «данный термин», «следует отметить», «необходимо понимать»;
- filler, synonym stuffing, and LSI dumping;
- exaggerated claims and fake authority.

---

## 6. Accuracy Rules

- Prefer primary sources when verifying search-engine behaviour: Google Search Central, Yandex documentation, official analytics/ads docs, standards (HTTP, Schema.org, etc.).
- Do not invent Google or Yandex ranking rules.
- Do not present third-party metrics (DA, DR, Spam Score) as official search-engine scores.
- Do not claim that any single factor «гарантированно повышает позиции».
- Separate **documented systems** (robots.txt, canonical, HTTPS) from **interpreted SEO practice**.
- Mark outdated concepts (meta keywords as ranking signal, Flash, YACA) as historical or exclude them.
- For Yandex-only or Google-only concepts, say so explicitly.
- Research notes stay in MARS editorial files; publishable copy stays original and concise.

---

## 7. SEO Rules

Workbook keywords and LSI are **research hints**, not mandatory insertion lists.

For each retained term prepare:

- canonical title;
- primary phrase;
- natural variants;
- synonyms;
- likely user intent;
- proposed SEO title;
- proposed meta description;
- internal-link targets;
- cannibalization risk;
- indexability after publication (yes/no/conditional).

Title and meta description must read naturally. Do not force exact-match keyword density. One primary concept per page.

Detailed model: `ISEO-SU-GLOSSARY-SEO-AND-INTERNAL-LINKING-MODEL-v1.md`.

---

## 8. Synonyms and Canonical Terms

- Exactly one **canonical title** per concept page.
- Alternate names become synonyms on the canonical page and/or MERGE candidates.
- MERGE terms must not receive separate published definitions.
- RENAME terms keep the concept but use the normalized title for publication.
- English/Russian pairs: choose the form most recognizable to the RU audience; put the other in synonyms (example: «Обратная ссылка» + synonym backlink).

---

## 9. Related Terms and Internal Links

- Link only to terms that remain KEEP or RENAME after audit.
- Prefer 3–7 related terms; avoid dumping entire categories.
- Related terms should clarify the concept graph (parent, sibling, contrast), not chase traffic.
- Do not fabricate URLs; use planned `/glossary/{slug}/` paths from the audit dataset.
- Bidirectional related-term UX remains optional (SAFE UNKNOWN G-U-003).

---

## 10. Examples

Good examples:

- name a realistic page type or scenario;
- show a short snippet of markup or a query pattern when useful;
- stay brand-neutral unless discussing a named product (Google Ads, Яндекс.Метрика).

Forbidden examples:

- invented i-seo.su case results;
- confidential client data;
- unsupported percentages («позиции выросли на 200%»).

---

## 11. Expert Verification

Flag `expert_review = YES` when:

- search-engine algorithm status is uncertain or historical;
- Google vs Yandex behaviour differs materially;
- proprietary vendor metrics are involved;
- emerging topics (GEO, AI search) lack stable official vocabulary;
- risk of myth propagation is high (Sandbox, bounce-rate ranking myths).

Expert/Nikita review is required before publication of flagged terms. Pilot batch may draft text, but flagged items stay provisional.

---

## 12. Prohibited Patterns

- Sales pitches and soft CTAs inside definitions.
- Keyword stuffing and forced LSI lists in body copy.
- Circular definitions («SEO — это SEO-оптимизация»).
- Copied vendor documentation passages.
- Unsupported statistics and guaranteed ranking claims.
- Outdated SEO myths presented as current fact.
- Treating product filenames or private process phrases as glossary concepts.
- Publishing empty or thin pages.

---

## 13. Editorial Workflow

1. Audit term (status, category, canonical title, synonyms).
2. Draft short definition + full body per this standard.
3. Attach SEO guidance (title, meta, links, cannibalization).
4. Peer/operator review; expert review if flagged.
5. Upload to WordPress **only under a separate charter** (drafts remain drafts until publication gate).
6. Publish only after `ISEO_GLOSSARY_PUBLIC_EXPOSURE` and content QA.

Pilot definitions live in MARS first (`ISEO-SU-GLOSSARY-PILOT-BATCH-v1.md`). They are not uploaded in this task.

---

## 14. Publication Readiness Checklist

A term is publication-ready only if:

- [ ] status is KEEP or RENAME (not MERGE / EXCLUDE);
- [ ] REVIEW items resolved by operator/Nikita;
- [ ] canonical title and slug agreed;
- [ ] short definition present (excerpt);
- [ ] full definition present and fact-checked;
- [ ] synonyms cleaned;
- [ ] related terms valid;
- [ ] SEO title and meta drafted;
- [ ] expert flag cleared or accepted with notes;
- [ ] no sales filler / no unsupported claims;
- [ ] WordPress post still draft until intentional publish wave;
- [ ] public exposure gate still controlled at programme level.

---

*ISEO-SU Glossary Editorial Standard v1 · 2026-07-24 · for operator/Nikita review.*

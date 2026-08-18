# ISEO-SU GLOSSARY EDITORIAL STANDARD v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** ISEO-SU-SITE-OPS-GLOSSARY-BATCH-01-REFINEMENT-AND-BATCH-02  
**Site:** https://i-seo.su/  
**Date:** 2026-07-25 (depth model refined)  
**Status:** ACTIVE FOR DRAFT PRODUCTION  

---

## 1. Purpose

This standard defines how glossary definitions for i-seo.su are written, reviewed, and prepared for publication.

Goals:

- explain professional SEO and digital-marketing concepts accurately;
- remain understandable to business owners and non-specialists;
- stay neutral and free of sales pitches;
- support editorial SEO without keyword stuffing;
- keep one concept per page after audit decisions (APPROVED / APPROVED_RENAME / MERGE / DEFER / EXCLUDE);
- vary article depth by usefulness — never pad simple concepts.

This document governs **editorial content**. It does not authorize public exposure.

---

## 2. Audience

Primary readers:

- business owners and marketing managers evaluating SEO;
- marketers and junior/middle specialists;
- clients who encounter these concepts in reports and proposals.

Tone: professional, calm, practical. Prefer plain Russian. Keep English abbreviations when they are industry-standard (SEO, CTR, PPC, robots.txt), and explain them on first use. Technical correctness takes priority over oversimplification.

---

## 3. Article Depth Model (SIMPLE / MODERATE / COMPLEX)

Depth is an **editorial writing aid**, not a bureaucratic taxonomy. Classify by usefulness of the subject, then write accordingly.

### SIMPLE

Typical structure:

- short definition;
- 2–5 explanatory paragraphs;
- optional clarification or example;
- related terms;
- synonyms if real.

Typical useful copy: about **500–1400** characters when that is enough.  
**Do not pad to a minimum.**

### MODERATE

Typical structure:

- short definition;
- explanatory introduction;
- 1–3 meaningful H2 sections only where they help;
- example/clarification where useful;
- related terms;
- synonyms.

Typical useful copy: about **1200–2800** characters.

### COMPLEX

Typical structure may include:

- short definition;
- broader explanation;
- several meaningful H2 sections;
- mechanics/technical behavior;
- examples;
- distinctions;
- limitations/nuances;
- related terms.

Typical useful copy: about **2200–5000** characters. Longer only when the subject truly needs it.

### Absolute length rule

Content length is determined by **usefulness**, not SEO word count. Never inflate a simple concept to satisfy a target length.

---

## 4. Structure Variation

Do **not** force identical headings such as «Что это», «Почему важно», «Как работает», «Пример» onto every article.

Use headings only where they help the reader. Two neighboring glossary pages should not look as if they were generated from the same rigid template.

Building blocks (use only what is needed):

1. **Short definition** — 1–2 sentences; stands alone; suitable as excerpt.
2. **Expanded explanation** — context in plain Russian.
3. **Clarification / mechanics / distinction** — when confusion is common.
4. **Example** — concrete, realistic, without invented performance claims.
5. **Related terms** — semantically useful only (normally 2–5; zero is acceptable).
6. **Synonyms** — genuine equivalents only.

---

## 5. Writing Style and AI-text Filter

- Lead with the meaning; do not open with history unless history is the point.
- Prefer active, concrete wording.
- Use ordinary Russian punctuation and quotation marks («»).
- Expand abbreviations on first mention when helpful.
- Use lists sparingly.
- Keep one H1 (term title).

Before accepting an article, reject or rewrite:

- repetitive introductions;
- generic statements with no information value;
- unnecessary conclusions;
- the same definition restated in multiple paragraphs;
- excessive «важно понимать» / «таким образом»;
- fake expert tone;
- keyword stuffing;
- unnatural repetition of the canonical term;
- formulaic H2 structure across many pages;
- unsupported claims;
- unnecessary marketing language;
- circular definitions («SEO — это процесс SEO-оптимизации»).

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

- Related terms must be **semantically useful**.
- Normally **2–5** is enough; **zero** is acceptable when no meaningful relation exists.
- Do not add links merely for SEO or build large link clouds.
- Use only APPROVED / APPROVED_RENAME publication-pool concepts as future public targets.
- Do not use EXCLUDED / DEFERRED terms as public related targets.
- During draft-only stage: keep related-term relationships as structured editorial metadata (plain names in copy / datasets). Do **not** create unsafe public links to draft content.
- Future public internal links only when the target entry is safely publishable.
- Do not fabricate URLs; use planned `/glossary/{slug}/` paths from the corpus.
- Bidirectional related-term UX remains optional (SAFE UNKNOWN G-U-003).
- Do not modify templates merely to force links during draft batches.

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

1. Confirm final disposition APPROVED or APPROVED_RENAME.
2. Assign editorial depth (SIMPLE / MODERATE / COMPLEX) as a writing aid.
3. Draft short definition + body per this standard (no padding).
4. Attach SEO guidance (title, meta, related targets).
5. Peer/operator review; expert review if flagged.
6. Load into WordPress as **draft** under a scoped charter.
7. Publish only after per-entry readiness **and** programme gate `ISEO_GLOSSARY_PUBLIC_EXPOSURE`.

---

## 14. Publication Completeness Rule

A glossary entry is **not** publication-ready merely because a WordPress post exists.

**PUBLICATION_ELIGIBILITY = per-entry approved content state**

Required before any future public exposure of that entry:

- final disposition APPROVED or APPROVED_RENAME;
- non-empty reviewed short definition;
- non-empty reviewed article body;
- no unresolved factual issue;
- canonical title finalized;
- slug finalized;
- SEO metadata acceptable;
- no placeholder copy;
- no editorial placeholder such as «Определение термина готовится редакцией и пока не опубликовано.»

Incomplete records must remain `draft`.  
The future public exposure mechanism must **never** expose all 241 records merely because the CPT becomes public.

Checklist:

- [ ] disposition APPROVED / APPROVED_RENAME;
- [ ] short definition reviewed;
- [ ] full body reviewed and fact-checked;
- [ ] canonical title and slug finalized;
- [ ] synonyms cleaned;
- [ ] related terms useful and valid;
- [ ] SEO title and meta acceptable;
- [ ] expert flag cleared or accepted with notes;
- [ ] no sales filler / unsupported claims / placeholders;
- [ ] intentional publish decision for this entry;
- [ ] programme public-exposure gate still controlled.

---

*ISEO-SU Glossary Editorial Standard v1 · 2026-07-25 · operational.*

# Forge WordPress — Module extraction backlog v1

**Date:** 2026-08-18  
**This wave:** knowledge only — **no** large refactor of FP-0002 code.

**Operating list:** [REUSABLE-CODE-EXTRACTION-ROADMAP](FORGE-WORDPRESS-REUSABLE-CODE-EXTRACTION-ROADMAP-v1.md) (R1–R4). This file is the short historical table.

Reuse classes: **A** ready with parameterization · **B** after extraction · **C** concept-only · **D** project-specific

| Candidate | Class | Notes |
|-----------|-------|--------|
| Native CPT permalink data-layer uniqueness | B | Keep UI-less; drop brand prefixes |
| Site Settings options IA | B | Keys/names must be generic |
| SEO entity meta + integrations options | B | |
| Sitemap helpers (`wp_sitemaps_*`) | A/B | Small, generic |
| Typography pipeline | B | Locale packs as config |
| System Dashboard widget | B | Fields via project meta |
| Social platform registry | B | |
| Smart Search REST + JS | B | Namespaces, CSS |
| Activity Log | B | Table name |
| DOCX importer | B | Template file |
| TOC H2 + reading time | A/B | Small theme functions |
| Consultation forms | B | Recipient from options only |
| Nav walker L2/mobile | B | |
| Slider nav helper | B | |
| Specialist CPT | D fields / B registration pattern | |
| Service layout governance | D | |
| Lifebuoy parallax | D | |
| Reviews options repeater | C/J | |

**Do not** copy `FUTURE_RECIPIENT` or any client emails/phones into a shared package.

---

*Extraction backlog v1.*

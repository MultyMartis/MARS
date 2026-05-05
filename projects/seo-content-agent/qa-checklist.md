# SEO Content Agent — QA checklist

**Status:** **operational guidance** — for humans and for designing automated checks. **Not** enforced by code in this repository.

Use before treating any model output as **client-ready**.

**Signals vs fields:** A system-level gap flag **`MISSING_DATA`** is not the same as the artefact array **`missing_data`** — naming convention in [data-schema.md](data-schema.md).

---

## Factual integrity

- [ ] **No unsupported facts** — every concrete claim (numbers, laws, product behavior, market share, dates) is traceable to brief, approved sources, or company facts corpus.
- [ ] **No invented prices, guarantees, deadlines, experience** — promotions, SLA, “N years on market”, awards: verify or remove.
- [ ] **Missing data clearly marked** — placeholders or omissions preferred over fabrication; cross-check `missing_data` / factcheck `unsupported`.

---

## Copy quality

- [ ] **No water** — remove filler that does not inform, persuade, or clarify; **seoqa** `water_detected` reviewed if true.
- [ ] **No keyword spam** — unnatural repetition, stuffed headings, or list padding flagged and fixed.
- [ ] **Commercial intent covered** — for commercial pages: benefits, objections, proof types (where data exists), clear CTA alignment with brief.

---

## SEO structure

- [ ] **H1–H3 valid** — single H1; logical hierarchy; matches approved outline unless human explicitly changed structure.
- [ ] **FAQ relevant** — questions reflect real user/buyer doubts; answers not generic “да, мы лучшие” without substance.
- [ ] **Meta description** — within length policy; matches intent; no false claims.

---

## Process

- [ ] **Outline approved** before `/text` (if process mandates).
- [ ] **Factcheck** and **SEO QA** reports read; **fail** items resolved or waived with owner sign-off.
- [ ] **Locale and brand voice** match brief (`locale`, `brand_voice`).

---

## Automation mapping (plan)

| Checklist item | Likely automation |
|----------------|-------------------|
| Unsupported facts | `factcheck_report` |
| Keyword spam | `seoqa_report.keyword_spam_risk` + heuristics |
| H1–H3 | `seoqa_report.h1_h3_issues` + deterministic heading parse **SAFE UNKNOWN** |
| Water | `seoqa_report.water_detected` (model-assisted, not perfect) |
| Outline approval | Storage flag — **implementation TBD** |

---

## Sign-off

**SAFE UNKNOWN:** Whether your org requires named approver IDs in a ticket system; record externally if needed.

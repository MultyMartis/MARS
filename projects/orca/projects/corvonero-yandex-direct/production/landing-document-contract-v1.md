# Landing Document Contract — Корво Неро v1

**Stage:** Defined in 2A — **production in Stage 3 after XLSX**  
**Count:** 31 unique URLs → 31 document pairs  
**Formats:** `.md` (MARS canonical) + `.docx` (Roman editable)

---

## Output location (Stage 3)

```text
projects/orca/projects/corvonero-yandex-direct/landing-copy/
  {lp-id}-{slug}/
    landing-spec-v1.md
    landing-spec-v1.docx
```

---

## Required fields per document

Each landing specification must contain **final publishable text** — not recommendations.

| # | Section | Required content |
|---|---------|------------------|
| 1 | page_id | LP-XX |
| 2 | url | Full planned URL |
| 3 | campaign_group_mapping | List of CORV-G* group IDs |
| 4 | seo_title | Unique Title tag |
| 5 | meta_description | Unique Description |
| 6 | h1 | Page H1 |
| 7 | first_screen_headline | Above-fold headline |
| 8 | first_screen_supporting | Supporting line(s) |
| 9 | cta_primary | Button/link text |
| 10 | service_explanation | What we do on this page |
| 11 | task_scenario_blocks | Task/scenario sections (2–4 blocks) |
| 12 | configurations | УТ, УНФ, Розница, КА, БП — where relevant |
| 13 | price_block | 3 000 ₽/час · от 6 000 ₽ · only confirmed facts |
| 14 | working_process | Steps: заявка → оценка → договор → работа |
| 15 | benefits | 3–5 bullets — no invented proof |
| 16 | trust_section | Only verified: ИП, договор, безнал, Новосибирск, удалённо |
| 17 | faq | 4–6 Q&A |
| 18 | cta_repeat | Repeated CTA block |
| 19 | form_labels | Field labels for Tilda form |
| 20 | legal_contact | Footer legal + contact |
| 21 | notes_for_roman | Tilda build notes, anchors, internal links |

---

## Content rules

| Rule | Detail |
|------|--------|
| Facts only | No partner status, 24/7, guarantees, fake cases |
| VAT | Do not claim — SAFE UNKNOWN |
| Price | May include hourly + minimum where commercially appropriate |
| Geo | Новосибирск + удалённая работа |
| Audience | ЮЛ и ИП |
| Tone | Commercial B2B, practical |

---

## Page priority (Roman build order)

| Priority | LP IDs | Rationale |
|----------|--------|-----------|
| P1 | LP-01,04,05,07,08,19,29 | Highest Tier 1 traffic |
| P2 | LP-13,14,18,02,03 | Integrations + marking hub |
| P3 | LP-06,09,16,30 | Secondary groups |
| P4 | LP-10–12,15,17,20–28,31 | Narrow / Tier 3–4 |

---

## Acceptance criteria (Stage 3)

- [ ] One `.md` + one `.docx` per LP-01 … LP-31  
- [ ] Text matches ad promises for mapped groups  
- [ ] No lorem ipsum  
- [ ] Roman can paste into Tilda without rewriting  
- [ ] URL matches [url-landing-map-v1.md](url-landing-map-v1.md) exactly

---

*Stage 2A does not produce full landing texts — grouping must stay stable first.*

# FP-0002 V9-06D8C Service Content Source Map v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d8c-services-mvp-content-seed/service-content-source-map.json`

---

## Source priority

1. V9 static `src/pages/usluga-konechnaya-v1.html` / `usluga-podrazdel-v1.html`
2. V9 partials under `src/partials/sections/`
3. Existing runtime ACF (retain when already V9-safe)
4. Theme static fallbacks (do not duplicate in ACF)

---

## Service 74 mapping

| Section | V9 reference | ACF target | Decision |
|---|---|---|---|
| Hero lead | `usluga-konechnaya-v1.html` heroLead | `hero_lead` | SKIP — already seeded |
| Intro lead | `service-leaf-intro-v1.html` | `intro_note` | WRITE |
| Intro body | D4 placeholder | `intro_text` | CLEAR |
| Signs | `service-leaf-signs-v1.html` (9 items) | `signs_items` | WRITE |
| Programme | programme block titles | `programme_items` | WRITE |
| Stages | `service-leaf-stages-v1.html` steps | `stages` | WRITE |
| FAQ | `faq.html` items 2–6 | `faq_items` | WRITE (LOCAL_MVP_PLACEHOLDER) |

---

## Services 73 / 77 / 84

Shared programme/stages/FAQ from subdivision V9 blocks. Hero/intro skipped (lorem or D4 minimal).

---

## Deferred / not seeded

- Specialists, reviews, founder-quote, comfort, corridor, landscape — no ACF mapping in D7-D
- Hero images — MEDIA_REQUIRED
- FAQ item 1 lorem — skipped
- Signs editorial lorem paragraph — not in WP template

---

## Result

**PASS**

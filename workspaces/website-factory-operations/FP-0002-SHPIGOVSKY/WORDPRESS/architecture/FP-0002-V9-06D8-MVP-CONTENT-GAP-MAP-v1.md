# FP-0002 V9-06D8 MVP Content Gap Map v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d8-content-seed-planning/mvp-content-gap-map.json`  
**Baseline:** D7-F PASS — gaps **EXPECTED_ONLY**, no route blockers

---

## Summary

| Route/Area | MUST_SEED | SHOULD_SEED | DEFER | NEEDS_OPERATOR | NEEDS_MEDIA | Blocking |
|---|---:|---:|---:|---:|---:|---:|
| `/` Home | 2 | 3 | 6 | 1 | 2 | 0 |
| `/uslugi/` Hub | 0 | 1 | 4 | 0 | 2 | 0 |
| Service 73 | 0 | 2 | 9 | 0 | 1 | 0 |
| Service 74 | 3 | 3 | 5 | 1 | 1 | 0 |
| Service 77 | 0 | 2 | 5 | 1 | 0 | 0 |
| Service 84 | 0 | 2 | 5 | 1 | 0 | 0 |
| `/kontakty/` | 2 | 2 | 2 | 3 | 2 | 0 |

**No MVP blockers** — all seven first-wave routes HTTP 200 at D7-F.

---

## Route detail

### 1. Home `/`

- **MUST_SEED:** `home_advantages`, `home_faq_items` (sections currently omitted).
- **SHOULD:** gallery, intro bands, hero slide images.
- **DEFER:** reviews teaser, blog teaser, V9 shared blocks without ACF.
- **Static fallback OK:** treatment-prevention, rehabilitation-program (theme partials).
- **Operator:** real phone via D8-A site options.

### 2. Services Hub `/uslugi/`

- **SHOULD:** `services_hub_faq_items`.
- **DEFER:** genotyping, category galleries/hero, founder/comfort.
- **CPT-driven OK:** service cards, groups.

### 3–6. Services 73 / 74 / 77 / 84

- **74 MUST:** `programme_items`, `stages`, `faq_items` for production-like MVP.
- **77/84:** placeholder layout acceptable; SHOULD add intro/signs when copy approved.
- **DEFER:** nature, team-stats, landscape, specialists, founder-quote, comfort, reviews, corridor, bordered-info (no ACF mapping).

### 7. Contacts `/kontakty/`

- **MUST:** site options (phone, email, hours, social) + page messengers alignment.
- **SHOULD:** map URL, contact blocks.
- **BLOCKED for seed planning:** live form endpoint — requires separate authorization.
- **Media:** map PNG / rehab photo — theme static OK; uploads need separate wave.

---

## Classification legend

| Class | Meaning |
|---|---|
| MUST_SEED_FOR_MVP | Visible omission Olga expects filled soon |
| SHOULD_SEED_FOR_VISUAL_RICHNESS | Improves parity; route works without |
| CAN_USE_STATIC_FALLBACK | Theme/V9 static handles render |
| DEFER_AFTER_MVP | Shared blocks or full production migration |
| NEEDS_OPERATOR_CONTENT | Real org data, legal, clinical copy |
| NEEDS_MEDIA_ASSET | Requires media upload authorization |
| NEEDS_ADMIN_UX_REPAIR | Label/help/source task (D8-F) |
| BLOCKED | Explicit later authorization (form endpoint, API keys) |

---

## Result

**COMPLETE**

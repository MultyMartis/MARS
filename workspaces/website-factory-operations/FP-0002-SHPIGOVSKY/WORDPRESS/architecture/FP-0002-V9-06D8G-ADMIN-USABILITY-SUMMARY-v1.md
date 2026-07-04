# FP-0002 V9-06D8G Admin Usability Summary v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d8g-post-seed-qa/admin-usability-summary.json`  
**Reference:** `architecture/FP-0002-V9-06D8-OLGA-ADMIN-UX-PLAN-v1.md`

Read-only admin screen inventory — no ACF JSON or label changes during D8-G.

---

## Area summary

| Area | Accessible | Seeded visible | Main issue | Suggested action | Result |
|---|---:|---:|---|---|---|
| Site Options | yes | yes | All 16 fields English labels | D8-F RU labels + help | PARTIAL |
| Home #4 | yes | yes | 9/10 English labels; repeaters dense | D8-F section help text | PARTIAL |
| Services Hub #5 | yes | yes | query_mode visible to editors | D8-F hide developer fields | PARTIAL |
| Service #73 | yes | yes | 18 fields / 4 groups stacked | D8-F group reorder | PARTIAL |
| Service #74 | yes | yes | Medical copy + developer variant | Content review + D8-F | PARTIAL |
| Service #77 | yes | yes | Same as other services | D8-F labels | PARTIAL |
| Service #84 | yes | yes | Same as other services | D8-F labels | PARTIAL |
| Contacts #20 | yes | yes | Overlap phones vs Options | D8-F canonical source note | PARTIAL |

---

## Olga usability notes

- **Editable now:** seeded repeaters (advantages, FAQ, programme, stages, contacts blocks), site options phone/email/hours.
- **Still empty by design:** map URL, social/messenger URLs, legal IDs, gallery media.
- **Developer-only (should stay hidden):** `service_layout_variant`, `services_hub_query_mode`, form endpoint fields.
- **English label debt:** entire ACF JSON surface — planned D8-F optional repair.

---

## D8-F scope recommendation

1. Russian admin labels for Options, Home, Hub, Service, Contacts field groups.
2. Hide or read-only lock developer query/layout fields.
3. Inline help: “phones canonical in Site Options”.
4. Optional ACF Extended PRO — **not approved**.

---

## Result

**PARTIAL** — content editable but admin UX debt remains; not blocking operator visual review.

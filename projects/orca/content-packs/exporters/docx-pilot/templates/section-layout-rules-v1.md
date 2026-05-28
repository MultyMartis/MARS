# Section Layout Rules v1

Each canonical section (01–10) renders in this order:

1. **H1** — `{order} — {title}` (e.g. `01 — Hero`)
2. **Section ID** — italic line from contract `section_id`
3. **Purpose** — `section_purpose` from contract table
4. **PPC continuity** — when present in contract
5. **SEO continuity** — when present
6. **Divider**
7. **Content** — `### Copy blocks` body (preformatted)
8. **CTA block** — shaded table from `### CTA`
9. **Proof** — when `### Proof elements` exists
10. **Semantic lock** — shaded block; per-section locks or MODE 1 inherit
11. **Section SAFE UNKNOWN** — warning sub-block if any
12. **Frontend / Factory notes** — `### Factory notes`
13. **Footer meta row** — `semantic_lock: ACTIVE`, `section_export: validated`
14. **Divider**

## Section IDs (canonical)

| Order | Key | section_id |
|-------|-----|------------|
| 01 | HERO | hero |
| 02 | SPECS | specs |
| 03 | ALLOWED_TASKS | allowed_tasks |
| 04 | DENIED_TASKS | denied_tasks |
| 05 | ORDER_FLOW | order_flow |
| 06 | PRICING | pricing |
| 07 | TRUST | trust |
| 08 | B2B | b2b |
| 09 | FAQ | faq |
| 10 | FINAL_CTA | final_cta |

## Missing data

If a subsection is absent in source MD, render placeholder line — do not omit section header.

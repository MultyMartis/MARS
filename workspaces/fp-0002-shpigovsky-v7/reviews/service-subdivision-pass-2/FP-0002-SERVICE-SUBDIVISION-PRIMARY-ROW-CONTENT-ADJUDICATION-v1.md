# FP-0002 Service Subdivision Primary Row Content Adjudication v1

| Field | Value |
|-------|-------|
| Target row | First service row — «Лечение алкогольной зависимости» |
| Runtime before | `<p class="services-category-section-v2__service-text">Лечение алкогольной зависимости</p>` |
| Figma desktop `1:3664` / `1:3665` | Duplicate title strings in component tree; no distinct description copy |
| Figma mobile `1:7161`–`1:7178` | Rows without body text |
| Adjudication | **Case B** — description visually absent |
| Final action | Removed `.services-category-section-v2__service-text` for first row |
| Duplicated title count after | 0 |

**Verdict:** `DESCRIPTION_REMOVED_CASE_B`

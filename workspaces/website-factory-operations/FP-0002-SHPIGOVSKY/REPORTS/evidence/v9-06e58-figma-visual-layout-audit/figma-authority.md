# Figma / design authority used — V9-06E58 audit

## Primary (strongest accessible this wave)

1. **Approved Figma PNG exports (2026-06-26):**  
   `X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\26.06.2026\`  
   Desktop frames ≈ **1437×…**; mobile ≈ **380×…** (see `refs/design-png-dimensions.txt`).  
   Copied into audit `refs/ref-*.png` for comparison.

2. **Operator-approved static V9 frontend:**  
   `X:\AI MARS\workspaces\fp-0002-shpigovsky-v9\dist`  
   Captured at **1440** and **480** for computed layout metrics vs WP.

3. **Native Figma sources (present, not opened programmatically):**  
   - `INCOMING/01_DESIGN/Spig_v1.2.fig`  
   - `INCOMING/01_DESIGN/Шпиговский.fig`  
   Limitation: no Figma Dev Mode API session; geometry compared via exports + V9.

4. **Home mockup support:** `INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` (Home not in 26.06.2026 PNG pair set).

## Mapping

| Export / authority | Audited WP route |
|--------------------|------------------|
| Услуги общая | `/uslugi/` |
| Услуга подраздел | `/uslugi/rasstroystva-pischevogo-povedeniya/` |
| Услуга | alcohol + narcissism services |
| О центре | `/o-centre/` |
| Контакты | `/kontakty/` |
| Блог | `/blog/` |
| Статья блога | blog single |
| Типовой контент | generic + specialist child |
| Home | V9 dist + HOME mockup |

## Conflicts

Where export PNG, V9 static, and WP disagree: **latest accepted V9 static + operator CSS freeze** used as primary layout authority; Figma exports used for composition intent. Operator CSS changes are **not** flagged merely for differing from older exports.

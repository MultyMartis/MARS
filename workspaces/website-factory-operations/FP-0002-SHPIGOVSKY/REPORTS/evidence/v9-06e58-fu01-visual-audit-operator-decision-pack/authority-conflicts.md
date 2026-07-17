# Authority conflicts — V9-06E58-FU01

## Hierarchy used

1. Approved Figma PNG exports INCOMING/01_DESIGN/26.06.2026/
2. Operator-approved V9 static workspaces/fp-0002-shpigovsky-v9/
3. Current WP runtime (frozen E58)
4. Computed metrics from E58 capture
5. CSS/templates
6. E58 narrative report (supporting only)

## Conflicts found during FU01 re-evaluation

### C1 — Index-based padding CSV vs class-matched metrics

section-padding-diffs-wp-vs-v9.csv paired nodes by DOM **index**, not by class.

This produced false deltas for:

- E58-VA-002 (claimed specialists 50 vs 30; class-match shows 50/50 == 50/50)
- E58-VA-007 (claimed related pb / CTA pt swap; class-match shows identical 30/30 and 0/30)
- E58-VA-008 (claimed generic 48/72 vs 0/0; class-match shows plain-page-content 48/72 == 48/72)

**Resolution for operator decisions:** prefer class-matched metrics + visual boards over the index CSV.

### C2 — Home Figma export gap

Home is **not** in the 26.06.2026 PNG pair set. Authority for E58-VA-001 = V9 static index.html utilities (
o-top-padding, 
o-top-padding--30) + HOME mockup support image only.

### C3 — E58-VA-005 hub composition

Figma «Услуги общая», V9 dist /uslugi/, and WP /uslugi/ may differ in content length / child counts. Width deltas in the index CSV are **not** reliable proof of layout defect. Stronger authority for composition intent = Figma export, but operator must visually confirm before any fix batch.

### C4 — Touch 44px vs design token 40px (E58-VA-003)

External accessibility guideline (≈44px) conflicts with design system token --main-size-btns: 40px present in both V9 and WP. **Design/V9 authority wins** unless operator explicitly wants a11y override.

### C5 — H2 multi-size (E58-VA-004)

Raw h2 scraper includes chrome (≈18px) and CTA titles (≈30px) alongside section titles (36/26). Not a single-token failure; role hierarchy.

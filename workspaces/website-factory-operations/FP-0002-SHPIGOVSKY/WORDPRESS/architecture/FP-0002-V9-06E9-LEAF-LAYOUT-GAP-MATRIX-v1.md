# FP-0002 V9-06E9 Leaf Layout Gap Matrix

| Area/section | Static V9 | Current WP (before) | Gap | Repair | After |
|--------------|-----------|---------------------|-----|--------|-------|
| Main wrapper | Direct sections in main | article.shpigovsky-service | EXTRA_WRAPPER | Remove article from alcohol-stack/leaf-stack | MATCH |
| Program items | 4 titled cards with images | Titles only | WRONG_IMAGE | Use subdivision programme image fallback | MATCH |
| Subnav | approach/program/start/specialists/comfort/reviews | intro/signs/program/start/faq | WRONG_ORDER | Alcohol-specific subnav in service-helpers | MATCH |
| Reviews anchor | id=service-leaf-reviews | No section id | MISSING | Pass section_id to reviews-slider | MATCH |
| Final form heading | service-leaf-final-form-heading | final-form-heading | WRONG_CLASS | final-form args support | MATCH |
| Program lorem copy | V9 fixture lorem | V9 fixture lorem | DEMO_ACCEPTED | No change (static authority) | DEMO_ACCEPTED |

JSON: `validation/v9-06e9-service-leaf-static-v9-layout-parity-repair/leaf-layout-gap-matrix.json`

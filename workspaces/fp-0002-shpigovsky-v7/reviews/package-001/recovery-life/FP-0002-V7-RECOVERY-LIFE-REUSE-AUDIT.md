# FP-0002 V7 — Recovery Life Reuse Audit

| Existing partial | DOM similarity | Content slots | Geometry match | Verdict |
| ---------------- | -------------- | ------------- | -------------- | ------- |
| `home-why-us.html` | Shared intro quote + body themes | Different heading; no stage cards | Partial lead band only | PARTIAL_SIMILARITY |
| `home-feature-grid.html` | 3-col bordered cards | Different titles/body | Card border/radius similar | PARTIAL_SIMILARITY |
| `home-rehabilitation-requirements.html` | Ordered steps | Different copy/count | Numbered steps vs titled stages | NO_MATCH |
| `home-rehabilitation-program.html` | Direction articles | Different structure | Image+text rows | NO_MATCH |
| `home-treatment-prevention.html` | Accordion services | Unrelated | NO | NO_MATCH |
| `home-comfort.html` | Gallery grid | Unrelated | NO | NO_MATCH |
| `home-reviews.html` | Slider | Unrelated | NO | NO_MATCH |

**Best matching partial:** `home-feature-grid.html` (PARTIAL_SIMILARITY only).

**Verdict:** NO_MATCH for full block — create dedicated partial.

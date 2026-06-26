# FP-0002 Service Subdivision Optional Regions Reconciliation v1

**Shared partial:** `services-category-section-v2.html`

| Region | Before | After | Mechanism |
|--------|--------|-------|-----------|
| lead | empty `<p>` rendered | not rendered when `lead === ''` | `@@if (lead !== '')` |
| body | empty wrapper when `bodyHtml === ''` | not rendered | `@@if (bodyHtml !== '')` |
| gallery | empty wrapper when `galleryHtml === ''` | not rendered | `@@if (galleryHtml !== '')` |
| CTA | always rendered | hidden when `hideCta === 'true'` | `@@if (hideCta !== 'true')` |

**Services V2:** `hideCta: ""` added to four category includes; compiled category CTA count = 4; empty lead/gallery/body wrappers = 0.

**Subdivision primary:** `hideCta: "true"` — unwanted CTA DOM = 0.

**Verdict:** `CONDITIONAL_RENDERING_ENABLED`

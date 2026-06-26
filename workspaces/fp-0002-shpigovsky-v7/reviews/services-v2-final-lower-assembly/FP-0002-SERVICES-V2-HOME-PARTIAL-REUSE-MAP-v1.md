# FP-0002 Services V2 Home Partial Reuse Map v1

| Required block | Home partial | Services include | Source copied | Result |
| -------------- | ------------ | ---------------- | ------------: | ------ |
| Founder quote | `partials/sections/home-founder-quote.html` | same + `modalSource: services-founder-quote`, `founderQuoteModifierClass: home-founder-quote--variant-b` | no | PASS |
| Comfort | `partials/sections/home-comfort.html` | direct include | no | PASS |
| FAQ | `partials/sections/home-faq.html` | direct include | no | PASS |
| Final form | `partials/sections/home-final-form.html` | `leadSource: services-final-section` | no | PASS |

Home source files unchanged (git hash matches HEAD).

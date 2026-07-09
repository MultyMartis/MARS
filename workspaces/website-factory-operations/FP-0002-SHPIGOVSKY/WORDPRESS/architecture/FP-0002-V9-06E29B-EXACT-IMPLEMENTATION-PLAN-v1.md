# FP-0002 V9-06E29B Exact Implementation Plan

| Area | Work type | Planned action | Safety |
|---|---|---|---|
| A_hero_media | DB_SEED_ONLY | Seed hero_media attachment from V9 o-centre-hero.webp | LOW |
| B_founder_quote | ACF_FIELD_DEFINITION_REQUIRED+TEMPLATE_BINDING_REQUIRED+DB_SEED | Add about_founder_* fields; bind institutional/founder-quote.php; seed static copy | LOW |
| C_clinic_landscape | ACF_FIELD_DEFINITION_REQUIRED+TEMPLATE_BINDING_REQUIRED+DB_SEED | Add about_clinic_landscape_* fields; institutional/clinic-landscape.php; seed image | LOW |
| D_cta_bands | ACCEPTED_SHARED_BLOCK | Document phone_primary + static guest CTA helper; no page-local duplication | NONE |
| E_shared_blocks | EDITABLE_SHARED_OPTIONS | Admin message field + document fp02-block-specialists, fp02-reviews, fp02-block-final-form | NONE |
| F_about_program_lorem | OPERATOR_DECISION_REQUIRED | V9 authority also contains lorem; no replacement without operator copy | NONE |
| G_visible_blocks | MATRIX | See post-implementation admin parity validation | LOW |

**Result:** PASS

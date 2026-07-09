# FP-0002 V9-06E29A O-Centre ACF Seed Change Plan v1

**Evidence:** `validation/v9-06e29a-placeholder-pages-and-ocentre-admin-parity-decision-audit/ocentre-acf-seed-change-plan.json`

**Classification:** MIXED_DB_AND_SOURCE (not DB-only — E26A hub seed already done)

## E29B proposed scope (do not execute in E29A)

| Area | Action | Work type | Risk |
|---|---|---|---|
| `hero_media` | Seed attachment from theme asset `o-centre-hero.webp` | DB_SEED_ONLY | LOW |
| `about_program_*` lorem | Replace with V9 static copy from `institutional-about-v9-content.php` | DB_SEED_ONLY | LOW |
| `infrastructure_g0_g5` media | Optional seed gallery attachments | DB_SEED_ONLY | LOW |
| founder quote | Add ACF group or bind shared block | ACF_FIELD_DEFINITION_REQUIRED / TEMPLATE_BINDING | MEDIUM |
| clinic landscape | Add ACF group or bind shared block | ACF_FIELD_DEFINITION_REQUIRED / TEMPLATE_BINDING | MEDIUM |
| CTA bands | Page-local fields or document site options | OPERATOR_DECISION_REQUIRED | LOW |
| specialists/reviews/final-form | Admin UX doc + verify options seeded | DB_SEED_ONLY / no template change | LOW |

## Runtime delivery

Required **only if** new ACF fields or template binding added for founder/clinic/CTA. Pure DB seed + options verify can avoid theme delivery.

## Rollback

DB checkpoint before E29B writes; restore postmeta for page #11 if visual regression.

## Validation

- `/o-centre/` HTTP 200 + section markers unchanged.
- ACF admin: all hub sections editable without static-only surprises.
- Compare to E28/E26A screenshots.

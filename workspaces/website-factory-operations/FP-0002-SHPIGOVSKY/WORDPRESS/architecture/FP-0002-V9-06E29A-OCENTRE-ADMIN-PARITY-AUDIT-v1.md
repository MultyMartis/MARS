# FP-0002 V9-06E29A O-Centre Admin Parity Audit v1

**Evidence:** `validation/v9-06e29a-placeholder-pages-and-ocentre-admin-parity-decision-audit/ocentre-admin-parity-audit.json`

**Page:** `#11` `/o-centre/` — template `page-templates/institutional.php`

## Readiness

| Dimension | Result |
|---|---|
| Public frontend | **PASS** (E26A 14-section stack renders) |
| Admin editability | **PARTIAL** |

## E28 reconciliation

E28 flagged empty `institutional_intro`, `institutional_blocks`, `institutional_team`. Those names are **legacy/unused** in current ACF JSON. E26A seeded `about_*` + `infrastructure_g0_g5` — **populated in DB** as of E29A probe (106 postmeta rows on #11).

## Section map

| Section | Frontend source | Admin/ACF state | Editability |
|---|---|---|---|
| hero | `hero_*` ACF + title fallback | eyebrow/title/lead/cta seeded; **hero_media empty** | PARTIALLY_EDITABLE |
| breadcrumbs/subnav | hardcoded V9 helpers | not in page ACF | NOT_EDITABLE_TEMPLATE_FALLBACK |
| institutional narrative | `about_narrative_*` | seeded | FULLY_EDITABLE |
| founder quote | static `home/founder-quote` | no page #11 ACF | NOT_EDITABLE_TEMPLATE_FALLBACK |
| who we treat | `about_who_treat_*` | seeded | FULLY_EDITABLE |
| program CTA band | static guest CTA + site phone | not page-local | PARTIALLY_EDITABLE |
| approach band | `about_approach_*` | seeded | FULLY_EDITABLE |
| clinic landscape | static `home/clinic-landscape` | no page #11 ACF | NOT_EDITABLE_TEMPLATE_FALLBACK |
| about program | `about_program_*` | seeded (**lorem ipsum** in intro fields) | PARTIALLY_EDITABLE |
| infrastructure | `infrastructure_g0_g5` + static gallery assets | text seeded; images theme fallback | PARTIALLY_EDITABLE |
| guest CTA | static copy + phone option | not page-local | PARTIALLY_EDITABLE |
| specialists | `fp02-block-specialists` options | shared admin page | PARTIALLY_EDITABLE |
| reviews | `fp02-reviews` options | shared admin page | PARTIALLY_EDITABLE |
| final form | template hardcoded heading/lead + block options | shared admin page | PARTIALLY_EDITABLE |

## Missing for full block editability from page #11 admin

1. `hero_media` attachment seed.
2. Founder quote + clinic landscape — need ACF fields or documented shared-block admin path.
3. CTA band copy — optional page-local fields or site options documentation.
4. Replace lorem in `about_program_lead/intro/intro2`.
5. Infrastructure gallery — optional media seed on repeater rows.
6. Operator UX: specialists/reviews/final-form live on **separate options screens**, not obvious when editing page #11.

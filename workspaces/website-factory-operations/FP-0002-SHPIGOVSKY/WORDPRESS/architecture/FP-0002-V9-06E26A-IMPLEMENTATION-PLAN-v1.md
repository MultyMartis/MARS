# FP-0002 V9-06E26A Implementation Plan v1

## Section mapping

| Static section | WP partial | ACF fields | Seed |
|----------------|------------|------------|------|
| Who we are | `institutional/institutional-narrative.php` | `about_narrative_*` | V9 static |
| Founder quote | `institutional/founder-quote.php` | — (home static) | V9 static |
| Who we treat | `institutional/who-we-treat.php` | `about_who_treat_*` | V9 static |
| CTA bands | `components/program-cta-band.php` | reusable CTA bands | V9 static |
| Approach | `institutional/approach-band.php` | `about_approach_*` | V9 static |
| Clinic landscape | `home/clinic-landscape.php` | theme asset | V9 asset path |
| Program | `institutional/about-program.php` | `about_program_*` | V9 static |
| Our home | `institutional/infrastructure-narrative.php` | `infrastructure_g0_g5` | V9 static text |
| Specialists | `home/specialists.php` | block options | existing |
| Reviews | `home/reviews.php` | reviews options | existing |
| Final form | `components/final-form.php` | block options | V9 copy |

## Guards

- Hub-only stack via `shpigovsky_is_about_hub_page()`
- Child institutional pages unchanged (placeholder article)
- Hero local fields + `hero_cta_label` preserved
- No global `Герои`; no blog/permalink/service changes

Evidence: `validation/v9-06e26a-about-page-wordpress-acf-port/implementation-plan.json`

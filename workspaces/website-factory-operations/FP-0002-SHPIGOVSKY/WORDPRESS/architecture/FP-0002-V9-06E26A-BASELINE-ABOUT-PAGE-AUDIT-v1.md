# FP-0002 V9-06E26A Baseline About Page Audit v1

## Target

- Route: `/o-centre/`
- WP page ID: `11`
- Template: `institutional.php`

## Static V9 section stack (14)

| # | Section | Static source | DOM marker |
|---|---------|---------------|------------|
| 1 | Hero | `services-inner-hero-v2.html` | `.services-inner-hero-v2` |
| 2 | Internal nav | `internal-page-nav.html` | `.internal-page-nav` |
| 3 | Who we are | `institutional-narrative.html` | `#who-we-are` |
| 4 | Founder quote | `founder-quote.html` | `.founder-quote--institutional-context` |
| 5 | Who we treat | `services-category-section-v2.html` | `#who-we-treat` |
| 6 | CTA 1 | `program-cta-band.html` | `#o-centre-cta-1` |
| 7 | Approach | inline `program-approach-band` | `#our-approach` |
| 8 | Clinic landscape | `clinic-landscape.html` | `.clinic-landscape` |
| 9 | Program | `services-program-v2.html` | `#our-program` |
| 10 | Our home | `infrastructure-narrative.html` | `#our-home` |
| 11 | Guest CTA | `program-cta-band.html` | `#o-centre-guest-cta` |
| 12 | Specialists | `specialists.html` | `#specialists` |
| 13 | Reviews | `reviews.html` | `#reviews` |
| 14 | Final form | `final-form.html` | `.final-form` |

## WP baseline before E26A

- Hero: implemented
- Internal nav: partial (no subnav items)
- Body sections: skeleton / missing (**12** sections)

## Reusable blocks

- Specialists → `fp02-block-specialists`
- Reviews → reviews options / shared slider
- CTA bands → `fp02-block-cta-bands`
- Final form → `fp02-block-final-form`
- Founder quote → home static partial (no duplicate global settings)

Evidence: `validation/v9-06e26a-about-page-wordpress-acf-port/baseline-about-page-audit.json`

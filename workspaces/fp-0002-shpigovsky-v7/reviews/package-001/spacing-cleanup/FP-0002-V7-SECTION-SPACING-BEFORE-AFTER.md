# FP-0002 V7 — Section Spacing Before/After

**Phase:** Package #001 Phase 4A  
**Date:** 2026-06-24  
**Viewports:** 1398 (desktop), 390 (mobile)  
**Evidence:** `implementation/spacing-before-metrics.json`, `implementation/spacing-after-metrics.json`

## Home — desktop 1398

| Section | Before top | Before bottom | After top | After bottom | Expected |
| ------- | ---------: | ------------: | --------: | -----------: | -------: |
| hero | 195 | 815 | 195 | 815 | UNCHANGED |
| home-recovery-intro | 865 | 1939 | 865 | 1939 | UNCHANGED |
| home-founder-quote | 1939 | 2578 | 1939 | 2578 | UNCHANGED |
| home-treatment-prevention | 2578 | 3190 | 2578 | 3190 | UNCHANGED |
| home-gallery | 3190 | 3622 | 3190 | 3662 | +40px height (pad 30→50) |
| home-why-us | 3622 | 4166 | 3662 | 4226 | +40px height |
| home-staff-photo | 4166 | 4674 | 4226 | 4774 | +40px height |
| home-feature-grid | 4674 | 5165 | 4774 | 5305 | +40px height |
| home-clinic-landscape | 5165 | 5849 | 5305 | 5989 | shift only (cascade) |
| home-recovery-life | 5849 | 6705 | 5989 | 6845 | shift only |
| home-reviews | 6705 | 7203 | 6845 | 7343 | shift only |
| home-rehabilitation-requirements | 7203 | 8561 | 7343 | 8741 | +40px height |
| home-rehabilitation-program | 8561 | 10145 | 8741 | 10365 | +40px height |
| home-genotyping | 10145 | 11027 | 10365 | 11287 | +40px height |
| home-comfort | 11027 | 12236 | 11287 | 12536 | +40px height |
| home-videos | 12236 | 12750 | 12536 | 13090 | +40px height |
| home-specialists | 12750 | 13236 | 13090 | 13616 | +40px height |
| home-articles | 13236 | 13704 | 13616 | 14124 | +40px height |
| home-faq | 13704 | 14920 | 14124 | 15380 | +40px height |
| home-final-form | 14920 | 15416 | 15380 | 15916 | +40px height |

## Home — mobile 390

| Section | Before top | Before bottom | After top | After bottom | Expected |
| ------- | ---------: | ------------: | --------: | -----------: | -------: |
| hero | 70 | 467 | 70 | 467 | UNCHANGED |
| home-recovery-intro | 517 | 3195 | 517 | 3195 | UNCHANGED |
| home-founder-quote | 3195 | 4421 | 3195 | 4421 | UNCHANGED |
| home-treatment-prevention | 4421 | 5200 | 4421 | 5200 | UNCHANGED |
| home-gallery | 5200 | 5540 | 5200 | 5580 | +40px height |
| home-why-us | 5540 | 6492 | 5580 | 6552 | +40px height |
| home-staff-photo | 6492 | 6792 | 6552 | 6892 | +40px height |
| home-feature-grid | 6792 | 8204 | 6892 | 8344 | +40px height |
| home-clinic-landscape | 8204 | 8524 | 8344 | 8664 | shift only |
| home-recovery-life | 8524 | 10610 | 8664 | 10750 | shift only |
| home-reviews | 10610 | 11300 | 10750 | 11440 | shift only |
| home-rehabilitation-requirements | 11300 | 13456 | 11440 | 13636 | +40px height |
| home-rehabilitation-program | 13456 | 16378 | 13636 | 16598 | +40px height |
| home-genotyping | 16378 | 18247 | 16598 | 18507 | +40px height |
| home-comfort | 18247 | 20151 | 18507 | 20451 | +40px height |
| home-videos | 20151 | 20728 | 20451 | 21068 | +40px height |
| home-specialists | 20728 | 21305 | 21068 | 21685 | +40px height |
| home-articles | 21305 | 22522 | 21685 | 22942 | +40px height |
| home-faq | 22522 | 24346 | 22942 | 24806 | +40px height |
| home-final-form | 24346 | 25119 | 24806 | 25619 | +40px height |

## Services — desktop 1398

| Section | Before top | Before bottom | After top | After bottom | Expected |
| ------- | ---------: | ------------: | --------: | -----------: | -------: |
| home-rehabilitation-program | 245 | 1828 | 245 | 1868 | +40px height |
| home-founder-quote | 1828 | 2467 | 1868 | 2507 | shift only |
| home-comfort | 2467 | 3676 | 2507 | 3756 | +40px height |
| home-faq | 3676 | 4892 | 3756 | 5012 | +40px height |
| home-final-form | 4892 | 5388 | 5012 | 5548 | +40px height |

## Services — mobile 390

| Section | Before top | Before bottom | After top | After bottom | Expected |
| ------- | ---------: | ------------: | --------: | -----------: | -------: |
| home-rehabilitation-program | 120 | 3042 | 120 | 3082 | +40px height |
| home-founder-quote | 3042 | 4268 | 3082 | 4308 | shift only |
| home-comfort | 4268 | 6172 | 4308 | 6252 | +40px height |
| home-faq | 6172 | 7996 | 6252 | 8116 | +40px height |
| home-final-form | 7996 | 8769 | 8116 | 8929 | +40px height |

## Screenshots

`reviews/package-001/spacing-cleanup/implementation/`

- HOME-SPACING-BEFORE-1398.png / HOME-SPACING-AFTER-1398.png
- HOME-SPACING-BEFORE-390.png / HOME-SPACING-AFTER-390.png
- SERVICES-SPACING-BEFORE-1398.png / SERVICES-SPACING-AFTER-1398.png
- SERVICES-SPACING-BEFORE-390.png / SERVICES-SPACING-AFTER-390.png

## Overflow (all breakpoints)

Before and after: **0** horizontal overflow on Home and Services (320–1398).

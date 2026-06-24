# FP-0002 V7 — Section Padding Inventory

**Phase:** Package #001 Phase 4A  
**Date:** 2026-06-24  
**Scan scope:** `src/scss/style.scss` (all `padding-top`, `padding-bottom`, `padding-block`, shorthand `padding` on section roots / `main` children)

## Scan summary

| Metric | Count |
|--------|------:|
| Total `padding-*` declarations in `style.scss` | 89 |
| Root section vertical padding declarations (active) | 14 selectors / 26 properties |
| Desktop declarations | 26 |
| Responsive root-section overrides | 0 |
| Home sections audited | 20 |
| Services sections audited | 5 |

## Root section inventory

| Selector | HTML root | Page | Property | Value | Breakpoint | Overrides base | Classification |
| -------- | --------- | ---- | -------- | ----- | ---------- | -------------: | -------------- |
| `main` | `<main>` | Home, Services | padding-top/bottom | `var(--pad-y)` | all | N/A (shell) | INTERNAL_COMPONENT_PADDING |
| `main > section` (cascade) | all `<section>` in main | Home, Services | padding-top/bottom | `var(--pad-y)` | all | — | base authority |
| `.hero` | `<section class="hero">` | Home | padding | `0px 10px` | all | N/A (outside main) | STRUCTURAL_EXCEPTION |
| `.home-recovery-intro` | `<section>` | Home | — | inherits base | all | no | — |
| `.home-founder-quote` | `<section>` | Home, Services | — | inherits base | all | no | — |
| `.home-treatment-prevention` | `<section>` | Home | — | inherits base | all | no | — |
| `.home-gallery` | `<section>` | Home | padding-top/bottom | `var(--pad-gap)` | all | yes (30px vs 50px) | ACCIDENTAL_OVERRIDE |
| `.home-why-us` | `<section>` | Home | padding-top | `var(--pad-gap)` | all | yes | ACCIDENTAL_OVERRIDE |
| `.home-why-us` | `<section>` | Home | padding-bottom | `var(--pad-y)` | all | duplicate | DUPLICATE_BASE_VALUE |
| `.home-staff-photo` | `<section>` | Home | padding-top/bottom | `var(--pad-gap)` | all | yes | ACCIDENTAL_OVERRIDE |
| `.home-feature-grid` | `<section>` | Home | padding-top/bottom | `var(--pad-gap)` | all | yes | ACCIDENTAL_OVERRIDE |
| `.home-clinic-landscape` | `<section>` | Home | — (commented override) | — | all | no | — |
| `.home-recovery-life` | `<section>` | Home | — | inherits base | all | no | — |
| `.home-reviews` | `<section>` | Home | — | inherits base | all | no | — |
| `.home-rehabilitation-requirements` | `<section>` | Home | padding-top/bottom | `var(--pad-gap)` | all | yes | ACCIDENTAL_OVERRIDE |
| `.home-rehabilitation-program` | `<section>` | Home, Services | padding-top/bottom | `var(--pad-gap)` | all | yes | ACCIDENTAL_OVERRIDE |
| `.home-genotyping` | `<section>` | Home | padding-top/bottom | `var(--pad-gap)` | all | yes | ACCIDENTAL_OVERRIDE |
| `.home-comfort` | `<section>` | Home, Services | padding-top/bottom | `var(--pad-gap)` | all | yes | ACCIDENTAL_OVERRIDE |
| `.home-videos` | `<section>` | Home | padding-top/bottom | `var(--pad-gap)` | all | yes | ACCIDENTAL_OVERRIDE |
| `.home-specialists` | `<section>` | Home | padding-top/bottom | `var(--pad-gap)` | all | yes | ACCIDENTAL_OVERRIDE |
| `.home-articles` | `<section>` | Home | padding-top/bottom | `var(--pad-gap)` | all | yes | ACCIDENTAL_OVERRIDE |
| `.home-faq` | `<section>` | Home, Services | padding-top/bottom | `var(--pad-gap)` | all | yes | ACCIDENTAL_OVERRIDE |
| `.home-final-form` | `<section>` | Home, Services | padding-top/bottom | `var(--pad-gap)` | all | yes | ACCIDENTAL_OVERRIDE |

## Non-root padding (preserved — sample)

| Selector | Classification |
|----------|----------------|
| `.home-gallery__caption` | INTERNAL_COMPONENT_PADDING |
| `.home-feature-grid__card` | INTERNAL_COMPONENT_PADDING |
| `.home-reviews__author` | INTERNAL_COMPONENT_PADDING |
| `.site-header`, `.site-footer` | INTERNAL_COMPONENT_PADDING (out of scope) |

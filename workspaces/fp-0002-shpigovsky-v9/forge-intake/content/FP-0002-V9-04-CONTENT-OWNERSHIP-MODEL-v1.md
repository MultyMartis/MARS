# FP-0002 V9-04 Content Ownership Model v1

**Date:** 2026-07-02

## Classification legend

| Class | Examples |
|-------|----------|
| native title | Page H1, post title |
| native editor | Legal body (controlled), simple text blocks |
| excerpt | Blog archive cards, article hero excerpt |
| featured image | Blog cards, article hero |
| menu label | May differ from page title |
| site option | phones, address, social URLs |
| ACF scalar | CTA headings, band titles |
| ACF repeater | reviews, FAQ, sources, gallery slides |
| taxonomy | post categories/tags |
| hardcoded structural | Breadcrumb labels "Главная", section chrome |
| demo placeholder | legal tokens, temporary service copy |
| production blocker | all DEMO legal fields |

## Rules

1. Editorial marketing copy → editable (ACF or native).
2. Decorative UI chrome → template-controlled.
3. Complex article typography → native post content stream + TOC from H2.
4. Do not expose every decorative word as ACF.
5. Preserve approved HTML for legal documents until operator replaces DEMO tokens.

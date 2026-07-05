# FP-0002 V9-06D9A Home Section Transfer Audit v1

**Date:** 2026-07-05  
**Task:** V9-06D9-A Visual Parity Audit  
**Evidence:** `validation/v9-06d9a-visual-parity-audit/home-section-transfer-audit.json`

## Summary

Static V9 Home renders **20 sections**. WordPress runtime Home renders **6 sections**. Fourteen sections are absent or not rendered due to missing template code and/or empty ACF.

## Section inventory

| # | Section | Static | Runtime | Status | Severity |
|---|---------|--------|---------|--------|----------|
| 1 | intro-section + hero | yes (with image) | yes (no image) | TRANSFERRED_BUT_VISUALLY_DEGRADED | CRITICAL |
| 2 | home-recovery-intro | yes | no | MISSING_FROM_WP_TEMPLATE | HIGH |
| 3 | founder-quote | yes | no | MISSING_FROM_WP_TEMPLATE | HIGH |
| 4 | home-treatment-prevention | yes | yes | TRANSFERRED_AND_VISIBLE (degraded media) | MEDIUM |
| 5 | home-gallery | yes | no | TRANSFERRED_BUT_EMPTY (ACF) | HIGH |
| 6 | home-why-us | yes | no | MISSING_FROM_WP_TEMPLATE | HIGH |
| 7 | home-staff-photo | yes | no | MISSING_FROM_WP_TEMPLATE | MEDIUM |
| 8 | home-feature-grid | yes | yes | TRANSFERRED_AND_VISIBLE | LOW |
| 9 | clinic-landscape | yes | no | MISSING_FROM_WP_TEMPLATE | MEDIUM |
| 10 | home-recovery-life | yes | no | MISSING_FROM_WP_TEMPLATE | HIGH |
| 11 | reviews | yes | no | MISSING_FROM_WP_TEMPLATE | HIGH |
| 12 | home-rehabilitation-requirements | yes | no | MISSING_FROM_WP_TEMPLATE | MEDIUM |
| 13 | home-rehabilitation-program | yes | yes | TRANSFERRED_AND_VISIBLE (degraded) | MEDIUM |
| 14 | home-genotyping | yes | no | MISSING_FROM_WP_TEMPLATE | MEDIUM |
| 15 | comfort | yes | no | MISSING_FROM_WP_TEMPLATE | MEDIUM |
| 16 | home-videos | yes | no | MISSING_FROM_WP_TEMPLATE | MEDIUM |
| 17 | specialists | yes | no | MISSING_FROM_WP_TEMPLATE | HIGH |
| 18 | home-articles | yes | no | TRANSFERRED_BUT_EMPTY | MEDIUM |
| 19 | faq | yes | yes | TRANSFERRED_AND_VISIBLE | LOW |
| 20 | final-form | yes | yes | TRANSFERRED_AND_VISIBLE | LOW |

## Root cause classification

1. **D7-B wave scope:** Only 8 sections planned; 12 V9 sections intentionally deferred per D7-B report.
2. **D8-B seed gaps:** Gallery, hero image, reviews, blog teaser skipped.
3. **Conditional render:** `gallery.php` and `articles-teaser.php` return early when ACF/posts empty.

## Recommended repair

**D9-D** — port missing template partials and seed ACF/media. **D9-C** — hero image first (operator priority).

## Result

Home section transfer: **FAIL**

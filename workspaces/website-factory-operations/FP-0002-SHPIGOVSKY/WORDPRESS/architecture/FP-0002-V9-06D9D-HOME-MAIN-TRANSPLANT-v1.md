# FP-0002 V9-06D9D Home Main Transplant v1

**Date:** 2026-07-05

## Summary

Replaced MVP 6-section Home main with static V9 19-section orchestration in `front-page.php`. All sections render from static V9 HTML converted to PHP partials with `shpigovsky_asset_uri()` and `home_url()` — no ACF dependency for visual parity.

## MVP scaffold

**Replaced** — not incrementally patched.

## Section order (matches V9)

hero → recovery-intro → founder-quote → treatment-prevention → gallery → why-us → staff-photo → feature-grid → clinic-landscape → recovery-life → reviews → rehabilitation-requirements → rehabilitation-program → genotyping → comfort → videos → specialists → articles → faq → final-form

## Hero CTA

Static V9 label `Записаться на консультацию` — options bypass in D9-D.

## Evidence

`validation/v9-06d9d-home-main-footer-static-v9-transplant/home-main-transplant-result.json`

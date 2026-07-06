# FP-0002 V9-06E4 Runtime Route Visual Audit

**Date:** 2026-07-06  
**Mode:** READ-ONLY

## Summary

Operator visual findings on `/uslugi/` and `/uslugi/zavisimosti/` are **substantiated** by runtime probe and screenshot comparison against static V9 dist authority.

## `/uslugi/`

| Field | Value |
|-------|-------|
| HTTP | 200 |
| Object | Page #5 |
| Template | `page-templates/services-hub.php` |
| Hero | `hero hero--inner` — **wrong type** |
| Hero image | **absent** |
| Main | `page-uslugi site-main site-main--services-hub` |

## `/uslugi/zavisimosti/`

| Field | Value |
|-------|-------|
| HTTP | 200 |
| Object | Service #73 |
| Template | `single-service.php` → `subdivision-stack` |
| Hero | `services-inner-hero-v2` — **correct type** |
| Hero image | **absent** (`hero_media` ACF empty) |
| Main | `page-service-subdivision-v1__main` — matches static |

Evidence JSON: `validation/v9-06e4-services-layout-shared-bg-visual-reconciliation-audit/runtime-route-visual-audit.json`

Screenshots: `validation/v9-06e4-services-layout-shared-bg-visual-reconciliation-audit/screenshots/`

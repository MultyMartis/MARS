# FP-0002 V9-06D.5 Visual Route QA Result v1

**Date:** 2026-07-04  
**Phase:** V9-06D.5  
**HEAD:** `e377ff4a72b3341e9b2ff6bc2dc532b84c79bdc2`  
**Verdict:** PARTIAL PASS

## Summary

Read-only visual route QA after rewrite-rule repair confirms:

- All seven required D.5 routes return **HTTP 200**
- Service ID **74** resolves correctly (regression PASS)
- Header / footer / main containers present on all required routes
- No fatal PHP / raw PHP / visible ACF keys
- Screenshots captured for desktop (1440×900) and mobile (390×844)
- Runtime mutations: **0**

Theme remains **V9-06B skeleton**. V9 HTML/CSS/JS integration is **not started**. Minimal ACF seed is present in DB but not rendered as production visuals.

## Required routes

| Route | URL | Expected | HTTP | Resolved | Result |
|---|---|---|---:|---|---|
| Home | `/` | Page 4 | 200 | page/4 | PASS |
| Services Hub | `/uslugi/` | Page 5 | 200 | page/5 | PASS |
| Зависимости | `/uslugi/zavisimosti/` | Service 73 | 200 | service/73 | PASS |
| Алкоголь | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | Service 74 | 200 | service/74 | PASS |
| Психическое здоровье | `/uslugi/psihicheskoe-zdorovie/` | Service 77 | 200 | service/77 | PASS |
| РПП | `/uslugi/rasstroystva-pischevogo-povedeniya/` | Service 84 | 200 | service/84 | PASS |
| Contacts | `/kontakty/` | Page 20 | 200 | page/20 | PASS |

## Visual baseline

Skeleton chrome (site title, primary menu, legal/footer menu, “V9-06B skeleton — not production markup.”) is visible. Services Hub and Contacts show H1 titles. Service singles use inert template-part comments only (no visible H1/hero body). Screenshots for service routes are visually identical to Home above the fold for that reason — confirmed by DOM body-length differences and HTML comment markers.

## Secondary debt

Page ID 6 and Service ID 73 share `/uslugi/zavisimosti/`. Current resolver: **Service 73**. Not a D.5 blocker.

## Evidence

`WORDPRESS/validation/v9-06d5-visual-route-qa/`

## Next

`CREATE_V9_06D6_TEMPLATE_INTEGRATION_PLANNING_TASK`

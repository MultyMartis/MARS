# FP-0002 V9-06D9-C — Post-Repair Validation

**Date:** 2026-07-05

## Route smoke (7 routes)

ALL_200 — Home, Services Hub, Service 73/74/77/84, Contacts.

## Hero DOM / asset check

| Check | Result |
|-------|--------|
| HTTP 200 `/` | PASS |
| `hero__media` present | PASS |
| `hero__image` src theme URL | PASS |
| Hero image HTTP 200 | PASS |
| Panel/title/tagline/CTA | PASS |
| No ACF leakage | PASS |

## Visual check

Desktop hero no longer empty/light; overlay panel readable over photo; mobile acceptable.

## Scope

No other Home sections transferred or modified.

**Evidence:**

- `validation/v9-06d9c-home-hero-parity-repair/post-repair-route-smoke.json`
- `validation/v9-06d9c-home-hero-parity-repair/post-repair-home-hero-dom-asset-check.json`
- `validation/v9-06d9c-home-hero-parity-repair/post-repair-home-hero-visual-check.json`

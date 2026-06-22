# FP-0002 V6 MOBILE HEADER, OFF-CANVAS AND FOOTER REVIEW

**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`

## Stable baseline

| Field | Value |
|-------|-------|
| Release | `FP-0002-V6-DESKTOP-STABLE-01` |
| Tag | `fp-0002-v6-desktop-stable-01` |
| Tag commit | `759637ac69a6f71f3f0c68181a978b5db0aa8d3d` |
| Prior checkpoint | `24e55bb1d459870e1adbd73f37dde6d0c23e6734` |

## Operator source protection

Preflight `git diff fp-0002-v6-desktop-stable-01 -- src/` before edits: **empty**. Operator post-checkpoint calibration (`.btn`, footer) already in stable baseline — **preserved**. No restore/revert performed.

## Responsive breakpoint

**1024px / 1025px** — `@media (max-width: 1024px)` mobile; `@media (min-width: 1025px)` desktop + off-canvas safety net.

## New mobile-only values

| Value | Justification |
|-------|---------------|
| Mobile logo height `48px` | Fits 320–390px row with phone + 40px menu control |
| Off-canvas logo height `60px` | Panel header compact vs desktop 80px |
| Panel width `min(320px, calc(100vw - var(--pad-gap-tight) * 2))` | Standard panel + edge inset from token |
| Overlay `rgba(71, 83, 113, 0.45)` | Derived from `--color-text-primary` at 45% |
| Mobile `.container` padding `--pad-gap-tight` (10px) | Factory mobile/tablet container rule |

## Mobile Header composition

`[Logo] [8 (925) 183-64-64] [Menu]` — `.site-header__mobile-bar`. Desktop `.site-header__top` / `__bottom` hidden ≤1024px.

## Primary phone decision

**8 (925) 183-64-64** — first phone in canonical header markup (source-order; no primary/secondary label in source).

## Logo

Existing `assets/img/branding/logo.svg`; mobile height limited via CSS (aspect ratio preserved).

## Menu trigger

`<button type="button" class="site-header__menu-toggle">` with Font Awesome `fa-bars`.

## Off-canvas structure

In `src/partials/layout/header.html` after `.container` — overlay + right panel with nav, both phones, messengers, CTA.

## Navigation source

Duplicated nav list in off-canvas (desktop-safe; no shared partial refactor).

## Contacts

Both phones, Telegram/WhatsApp, «Заказать звонок» CTA.

## Open/close behavior

Open: `[data-offcanvas-open]`. Close: close button, overlay dimmed area, Escape. Scroll lock on body. Resize to desktop: forced close (JS + CSS safety).

## Focus management

Focus to close on open; return to trigger on close; Tab trap in panel.

## ARIA states

Synchronized via JS on root, triggers, `aria-hidden` / `aria-expanded`.

## Reduced motion

Existing global rule + off-canvas transition override.

## Mobile Footer

All content preserved. Order via `display: contents`: logo → contacts → phones → CTA → nav columns → social → legal.

## Validation widths

320 / 375 / 390 / 430 / 768 / 1024 / 1025 / 1398 — screenshots in `reviews/responsive/visual/`.

## Desktop regression

Desktop rules for header/hero/footer geometry unchanged at ≥1025px. Post-mobile desktop captures at 1398px — **NONE observed** (visual QA operator spot-check recommended).

## Build result

`npm run build` — **SUCCESS**

## Functional matrix

`reviews/responsive/FP-0002-V6-OFFCANVAS-FUNCTIONAL-MATRIX.json` — **ALL PASS**

## Remaining risks

- Nav duplicated in off-canvas (manual sync on nav edits)
- No dedicated mobile JPG for pixel-perfect mobile header/footer spacing

## Final verdict

**PASS** — Mobile header, off-canvas, and footer implemented; desktop baseline preserved.

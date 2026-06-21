# FP-0002 v2 — Foundation Tokens Report v1

**Task:** FP-0002 v2 FOUNDATION START · FND-01 / FND-02  
**Date:** 2026-06-22  
**Workspace:** `workspaces/fp-0002-shpigovsky-v2/`  
**Authority:** FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md · FP-0002-DESIGN-AUDIT-v1.md · FP-0002-v2-DESIGN-SYSTEM-SNAPSHOT-v1.md

---

## 1. Token file map

| File | Group | Status |
|------|-------|--------|
| `src/scss/abstracts/_tokens-colors.scss` | Colors | **CREATED** |
| `src/scss/abstracts/_tokens-typography.scss` | Typography | **CREATED** |
| `src/scss/abstracts/_tokens-spacing.scss` | Spacing | **CREATED** |
| `src/scss/abstracts/_tokens-radius.scss` | Radius | **CREATED** |
| `src/scss/abstracts/_tokens-container.scss` | Container + breakpoints | **CREATED** |
| `src/scss/abstracts/_tokens-shadows.scss` | Shadows | **CREATED** |
| `src/scss/abstracts/_tokens-transitions.scss` | Transitions | **CREATED** |
| `src/scss/abstracts/_tokens-z-index.scss` | Z-index | **CREATED** |
| `src/scss/abstracts/_tokens.scss` | Aggregator `@forward` | **CREATED** |
| `src/scss/abstracts/_mixins.scss` | Breakpoints + container mixin | **CREATED** |
| `src/scss/layout/_container.scss` | Container system | **CREATED** |

---

## 2. Token source register

| Token | Value | Source | Status |
|-------|-------|--------|--------|
| `color-bg-base` | `#FFFFFF` | v3 §5.1 Olga | **CONFIRMED** |
| `color-bg-page` | `rgba(218,229,240,0.7)` | v3 §5.1 Olga | **CONFIRMED** |
| `color-text-primary` | `#475371` | v3 §5.1 Olga | **CONFIRMED** |
| `color-primary-accent` | `#B3261E` | v3 §5.1 Olga | **CONFIRMED** |
| `color-text-secondary` | `#8D9097` | v3 §5.2 Normalization fallback | **FALLBACK** |
| `color-bg-elevated` | `#F1F5F9` | v3 §5.2 | **FALLBACK** |
| `color-border-*` | per v3 §5.2 | Normalization fallback | **FALLBACK** |
| `color-error` | `#B3261E` | v3 §5.2 placeholder | **PLACEHOLDER** |
| `color-success` | `#2E7D52` | v3 §5.2 placeholder | **PLACEHOLDER** |
| `space-0`…`space-16` | 4px base scale | v3 §6.1 | **CONFIRMED** |
| `section-gap-*` | 80/240/64 px | v3 §6.2 | **CONFIRMED** |
| `radius-default` | `30px` | v3 §7 Lead correction | **CONFIRMED** |
| `radius-control` | `10px` | v3 §7 | **CONFIRMED** |
| `radius-pill` | `999px` | v3 §7 | **CONFIRMED** |
| `container-max` | `1170px` | v3 §3.1 Olga | **CONFIRMED** |
| `page-padding-x-desktop` | `40px` | v3 §3.1 PD-13 | **CONFIRMED** |
| `page-padding-x-mobile` | `20px` | v3 §3.1 | **CONFIRMED** |
| `breakpoint-desktop-min` | `1024px` | v3 §9.1 | **CONFIRMED** |
| `shadow-none` | none | v3 §8.3 cards flat | **CONFIRMED** |
| `shadow-focus-ring` | engineering | v3 OQ-07 | **PLACEHOLDER** |
| `transition-*` | 150–300ms ease | OQ-07 engineering | **PLACEHOLDER** |
| `z-index-*` | 0–500 stack | U-08 | **SAFE UNKNOWN** — placeholder stack |

---

## 3. Container system decisions

| Variant | Implemented | Justification |
|---------|-------------|---------------|
| `.container` | **YES** | v3 §3.1 — max-width 1170px, padding 40/20, centered |
| `.container--wide` | **NO** | v3 §3.2 wide sections = 100vw background + inner `.container` — not wider max-width |
| `.container--narrow` | **NO** | 280px TOC is PG-009 page layout — not foundation container variant |

**Desktop behavior:** `@media (min-width: 1024px)` — padding-inline 40px, max-width 1170px, margin auto.

**Mobile behavior:** `@media (max-width: 1023px)` — padding-inline 20px.

---

## 4. SAFE UNKNOWN

| Item | Impact |
|------|--------|
| Z-index final stack (header/modal/sticky) | Placeholder values only — U-08 |
| Hover/focus color engineering | Primary hover `#9f2119` (~8% darken) — OQ-07 |
| Transition durations | Not in FIG/PDF — engineering placeholder |

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Build | `npm run build` — PASS |

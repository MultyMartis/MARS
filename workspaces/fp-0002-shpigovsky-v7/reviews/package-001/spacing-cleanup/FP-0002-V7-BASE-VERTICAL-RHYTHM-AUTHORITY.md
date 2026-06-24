# FP-0002 V7 — Base Vertical Rhythm Authority

**Phase:** Package #001 Phase 4A  
**Date:** 2026-06-24  
**Workspace:** `workspaces/fp-0002-shpigovsky-v7/`

## Canonical rule

```scss
main > section,
main > .section,
main > div {
  padding-top: var(--pad-y);
  padding-bottom: var(--pad-y);
}
```

| Field | Value |
|-------|-------|
| File | `src/scss/style.scss` |
| Lines | 369–372 |
| Desktop `--pad-y` | `50px` (`:root` line 111) |
| Mobile `--pad-y` | `50px` (no responsive override; same token at all breakpoints) |
| Specificity | `0,0,1,2` (two type selectors + one pseudo-class-free compound) |
| Cascade order | After `main` block (lines 362–367); no later global competing rule for section children |

## Related shell rule

```scss
main {
  padding-top: var(--pad-y);
  padding-bottom: var(--pad-y);
}
```

| Field | Value |
|-------|-------|
| Lines | 362–367 |
| Purpose | Outer vertical inset for `<main>` content area (first/last section edge) |
| Status | **KEEP** — not a competing section rhythm system; applies to `main` element, not section roots |

## Token definitions

| Token | Value | Location |
|-------|-------|----------|
| `--pad-y` | `50px` | `:root` line 111 |
| `--pad-gap` | `30px` | `:root` line 112 (used incorrectly in several section root overrides) |

## Media queries

No breakpoint redefines `--pad-y` or the `main > section` selector. Responsive blocks at `max-width: 1024px`, `930px`, etc. do not alter base section vertical rhythm.

## Competing global rules

```text
BASE VERTICAL RHYTHM — SINGLE AUTHORITY
```

One canonical section-child rule. `main` padding is complementary shell spacing, not a duplicate authority for per-section rhythm.

## Structural exceptions (documented, not changed)

| Selector | Location | Reason |
|----------|----------|--------|
| `.hero` | Outside `<main>`, inside `.intro-section` | Hero owns viewport height and internal panel geometry; not a `main` child |

# SITE-001 W3V2 Change Request v1

**Change request ID:** CR-SITE-001-W3V2-2026-06-09  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only  
**Checkpoint:** `site-001-phase1-stable-2026-06`

---

## Summary

Modernize visual perception (2018 → 2026 automotive premium) via **CSS-only** identity layer: unified color tokens, graphite dark surfaces, soft neutral backgrounds, refined depth, card/button/form/header/footer styling.

## Scope

| Phase | Target |
|-------|--------|
| W3V2-A | Color system (`--w3v2-*` tokens) |
| W3V2-B | Depth system (shadow sm/md/lg) |
| W3V2-C | Card appearance (surfaces, borders, hover) |
| W3V2-D | Button system (hover/active/focus consistency) |
| W3V2-E | Header & footer visuals (no structure) |
| W3V2-F | Form styling (inputs, focus, spacing) |

## Files

- `css/main.css`
- `css/media.css`

## Risk

Low — incremental override block; T1 rollback from `pre-w3v2-*` backup.

## Authorization

Operator W3V2 brief 2026-06-09 — **APPROVED for TEST execution**.

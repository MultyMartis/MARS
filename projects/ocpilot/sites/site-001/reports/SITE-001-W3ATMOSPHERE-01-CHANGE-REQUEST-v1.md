# SITE-001 W3ATMOSPHERE-01 Change Request v1

**Change request ID:** CR-SITE-001-W3ATMOSPHERE-01-2026-06-09  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** TEST only  
**Checkpoint:** `site-001-phase1-stable-2026-06`

---

## Summary

Site-wide atmosphere refresh via **CSS-only** layer: cool stone canvas, premium graphite header/footer shell, unified card language, dealership form surfaces. **Not** redesign, UX, PDP, or conversion work.

## Scope

| Phase | Target |
|-------|--------|
| W3ATMOSPHERE-A | Canvas `#EEF1F5`, surface tokens, W3V2 bridge |
| W3ATMOSPHERE-B | Header premium shell — gradient nav, soft seams |
| W3ATMOSPHERE-C | Footer graphite gradient, muted legal, soft separators |
| W3ATMOSPHERE-D | Unified card recipe — 12px radius, graphite shadow |
| W3ATMOSPHERE-E | Form surface system, focus ring, tool panels |
| W3ATMOSPHERE-F | Legacy atmosphere literal purge (red/dark/border) |
| W3ATMOSPHERE-G | Mobile atmosphere parity in `media.css` |

## Files

- `css/main.css`
- `css/media.css`

## Baseline

Phase 1 Stable Checkpoint + W3-V + W3V2 + W3UX-C1 (W3VIS-01A/01B rolled back)

## Risk

Low–medium — incremental override block atop W3V2; T1 rollback from `pre-w3atmosphere-01-*` backup.

## Rollback

T1 only — restore `main.css` + `media.css` from backup; clear caches; verify URLs. See [SITE-001-W3ATMOSPHERE-01-ROLLBACK-PLAN-v1.md](SITE-001-W3ATMOSPHERE-01-ROLLBACK-PLAN-v1.md).

## Authorization

Operator W3ATMOSPHERE-01 task brief 2026-06-09 — **APPROVED for TEST execution**.

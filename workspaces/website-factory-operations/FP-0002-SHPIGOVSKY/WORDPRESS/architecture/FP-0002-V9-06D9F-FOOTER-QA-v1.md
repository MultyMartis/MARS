# FP-0002 V9-06D9F Footer QA v1

**Date:** 2026-07-05  
**Task:** V9-06D9-F (read-only QA)

## Summary

Footer visual transplant from D9-D **PASS**. Global footer present on Home and all seven secondary routes checked; no layout break observed.

| Area | Static V9 | Runtime D9-F | Result |
|------|-----------|--------------|--------|
| Layout (`site-footer`) | yes | yes | PASS |
| Logo | yes | yes | PASS |
| Nav columns | yes | yes | PASS |
| Contacts | yes | yes | PASS |
| Privacy/legal block | yes | yes | PASS |
| Scroll-to-top hook | not detected in static HTML proxy | not detected | PARTIAL (non-blocking) |
| Credit | yes | yes | PASS |
| Secondary routes footer | — | 7/7 PASS | PASS |

Scroll-to-top: neither static nor runtime HTML contained a reliable `scroll-top` / `data-scroll-top` marker in automated DOM scan; treated as PARTIAL observation only — not a regression from D9-D.

## Evidence

`validation/v9-06d9f-home-footer-visual-parity-qa/footer-qa.json`  
`validation/v9-06d9f-home-footer-visual-parity-qa/secondary-route-safety-qa.json`

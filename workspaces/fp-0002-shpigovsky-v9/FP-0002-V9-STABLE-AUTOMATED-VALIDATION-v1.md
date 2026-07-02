# FP-0002 V9 Stable Automated Validation v1

**Phase:** V9-03 stable baseline checkpoint  
**Date:** 2026-07-02  
**Command:** `npm run validate` (port 8897)

## Result

**PASS**

## Checks confirmed

- 31 routes emitted and indexed
- Route HTTP readiness
- Internal links
- Root-relative assets (`/assets/...`)
- One H1 per page
- No duplicate IDs
- One consultation modal per page
- Modal triggers valid; Triumph-derived runtime contract
- One scroll-to-top per page; threshold 500px
- Reduced-motion handling
- No preloader
- G6 absent from published dist
- Four legal pages complete with DEMO markers
- No genotyping route in dist
- No debug/local filesystem leakage

## Evidence

Full output: `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v9\v9-03-stable-baseline-checkpoint\validation\automated-validation-output.txt`

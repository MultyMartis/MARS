# FP-0002 V7 → V8 Transition Record v1

**Date:** 2026-06-28  
**V7 status after this pass:** `IMMUTABLE_STABLE_FALLBACK`  
**V8 workspace:** `workspaces/fp-0002-shpigovsky-v8/`

## Reason

Systemic architectural duplication: visually identical blocks (e.g. upper nav band) implemented via separate page-specific wrapper classes and CSS on each template.

## Authority for V8 bootstrap

| Role | Tag | Commit |
| ---- | --- | ------ |
| Four canonical templates source | `fp-0002-v7-four-template-canonical-demo-baseline-01` | `6eb493e9` |
| Static client demo (unchanged) | `fp-0002-v7-static-client-demo-stable-02` | `e33e59af` |

**Not authority:** V7 working tree post-baseline WIP (includes rejected `o-centre-v1.html` attempts at repo HEAD).

## V7 constraints (effective immediately)

- No mass class renames
- No component consolidation in V7
- No canonical template HTML/SCSS/JS changes
- No o-centre continuation
- No static demo redeploy as V8

## Allowed V7 changes

Status documentation only (this pass).

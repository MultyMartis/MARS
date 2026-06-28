# FP-0002 V8 — CF-003–CF-009 Consolidation Checkpoint v1

**Date:** 2026-06-28
**Head:** `2107d2b93c95efdfbfa9d9231a51e1df47286da4`
**Scope:** Read-only audit after CF-009 closeout and duplicate-ID repair (`2107d2b9`)

## Verdict summary

| Scope | Result |
|-------|--------|
| CF-003–CF-009 canonical families | **PASS** |
| Retired active architecture names | **PASS** (asset-path exceptions only) |
| Duplicate-ID repair (`home-treatment-prevention-panel-1`) | **PASS** |
| Page-wide DOM gate (all 5 pages) | **FAIL** — pre-existing blocker on subdivision page |
| Browser smoke (5 pages × 2 viewports) | **PASS** |
| Build | **PASS** |

## Implementation commits (CF-003–CF-009)

| Wave | Commit |
|------|--------|
| CF-003 | `361502bf9188dfb966bc3ae4b0b955ed4389a172` |
| CF-004 | `25f972f93b355d113222e08857837a1f51c14d5b` |
| CF-005 | `c6efb08905ecdf81c82e31fab493d223cc82fe7c` |
| CF-006 | `4737b020c93dcbdfd2b309b3abe9a564a9a8ca79` |
| CF-007 | `4fe928f2512af77413d61a5263aa685aae667123` |
| CF-008 | `f7f2b80f83fc0c62f36b260da52900ebd4511ccd` |
| CF-009 | `ec5ff2c05b66e56c452dac441a59e4268517393c` |

## Closeout bundle commits

| Part | Commit | Message |
|------|--------|---------|
| A | `ec5ff2c0` | refactor(fp-0002): universalize final form component in v8 |
| B | `2107d2b9` | fix(fp-0002): remove treatment prevention duplicate id in v8 |

## Pre-existing page-wide blocker (not fixed in this checkpoint)

| Page | Issue | Missing ID | Source |
|------|-------|------------|--------|
| `usluga-podrazdel-v1.html` | broken `aria-labelledby` | `service-subdivision-start-heading` | `service-subdivision-first-cta-v1.html` |

**Classification:** PRE_EXISTING — CF-011 territory (dark CTA wrapper). Out of scope for CF-003–CF-009 consolidation.

## Evidence

- JSON: `audits/consolidation-checkpoint/data/FP-0002-V8-CF003-CF009-CONSOLIDATION-CHECKPOINT.json`
- Retired names: `audits/consolidation-checkpoint/data/FP-0002-V8-RETIRED-NAMES-AUDIT.json`
- Page DOM: `audits/consolidation-checkpoint/data/FP-0002-V8-PAGE-WIDE-DOM-VALIDATION.json`
- Browser smoke: `audits/consolidation-checkpoint/data/FP-0002-V8-CONSOLIDATION-BROWSER-SMOKE.json`

## Next implementation

**NOT AUTHORIZED:** CF-010, CF-011, CF-012, O-Centre

**Documented recommendation:** CF-011 charter first (see `FP-0002-V8-NEXT-WAVE-RECOMMENDATION-v1.md`)

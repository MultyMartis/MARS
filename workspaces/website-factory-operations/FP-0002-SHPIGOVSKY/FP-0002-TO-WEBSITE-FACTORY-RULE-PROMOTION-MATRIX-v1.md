# FP-0002 → Website Factory Rule Promotion Matrix v1

**Date:** 2026-07-01  
**Scope:** Lessons from FP-0002 V8 baseline

**Scope labels:** `GLOBAL_MANDATORY` | `GLOBAL_RECOMMENDED` | `PATTERN_LIBRARY` | `FP0002_ONLY` | `DEFERRED_FOR_MORE_CASES`

---

## Matrix

| # | Lesson | FP-0002 evidence | Proposed scope | Reason | Target document | Existing global rule? | Action |
|---|--------|------------------|----------------|--------|-------------------|----------------------|--------|
| 1 | Operator-only visual PASS | Priority protocol; baseline tag | GLOBAL_MANDATORY | Prevents false-green commits | Priority protocol + operator-canonical-source-law | Partial — operator-canonical-source-law | UPDATE cross-link |
| 2 | Authority hierarchy (6 levels) | V8 reconciliation | GLOBAL_RECOMMENDED | Reduces invention | WEBSITE-FACTORY-FP-0002-LESSONS-LEARNED-v1 | WF visual authority contract | CASE_NOTE_ONLY |
| 3 | Micro-pass after partial approval | Blog passes; O-Centre | GLOBAL_RECOMMENDED | Limits rewrite risk | Lessons learned | frontend-implementation-pipeline | CASE_NOTE_ONLY |
| 4 | One DOM responsive | V8 all pages | GLOBAL_RECOMMENDED | CMS + a11y | Lessons learned | foundation responsive docs | NO_CHANGE |
| 5 | No duplicate mobile content | V8 source | GLOBAL_RECOMMENDED | Same | Lessons learned | AGENTS.md patterns | NO_CHANGE |
| 6 | Article body single stream | Blog article | GLOBAL_RECOMMENDED | WP editor compat | Lessons learned + handoff contract | Forge handoff contract | UPDATE Forge contract cross-link |
| 7 | Excerpt outside body | Blog hero | GLOBAL_RECOMMENDED | WP field model | Handoff map | WP-ready baseline | CASE_NOTE_ONLY |
| 8 | TOC auto from H2 | Blog article | PATTERN_LIBRARY | Blog-specific pattern | Blog architecture | — | ADD pattern note in lessons |
| 9 | Clean build for baseline | 07A closure | GLOBAL_MANDATORY | Release integrity | operational-qa-entry | production-hardening-rules | NO_CHANGE |
| 10 | Storage evidence ZIP | 07A/07B snapshots | GLOBAL_RECOMMENDED | Recovery | Lessons learned | survivability docs | NO_CHANGE |
| 11 | Selective git staging | MARS git rules | GLOBAL_MANDATORY | WIP safety | git-rules | web-gpt git rules | NO_CHANGE |
| 12 | Single file `style.scss` | V8 only | FP0002_ONLY | Consolidation exception | FP-0002 frontend rules | gulp-starter partial mirror | NO_CHANGE global |
| 13 | `--radius-main` only | V8 calibrated | FP0002_ONLY | Operator freeze | FP-0002 frontend rules | universal-style-scale-law | NO_CHANGE — document exception |
| 14 | `.block-whith-red-line` spelling | V8 CSS | FP0002_ONLY | Compatibility | FP-0002 frontend rules | — | NO_CHANGE |
| 15 | Excel + source reconciliation for demo | 07C spec | GLOBAL_RECOMMENDED | Demo completeness | Lessons learned §8 | — | ADD lessons doc |
| 16 | Component anatomy vs file reuse | Founder/related cards | PATTERN_LIBRARY | Reuse discipline | Lessons learned §4 | implementation-extraction-discipline | NO_CHANGE |
| 17 | WP adapts to frontend | Handoff map | GLOBAL_MANDATORY | Forge principle | Forge handoff contract | Already stated | NO_CHANGE |
| 18 | Operator polish phase | 07B boundary doc | GLOBAL_RECOMMENDED | Expectation management | Lessons learned | — | ADD lessons doc |
| 19 | 1024/1025 breakpoint split | V8 SCSS | GLOBAL_RECOMMENDED | Matches starter | Lessons learned | AGENTS.md breakpoints | NO_CHANGE |
| 20 | `.btn` + `.btn_dark` + `.btn--primary` | V8 buttons | GLOBAL_MANDATORY | Already law | universal-button-system-law | Exists | NO_CHANGE |

---

## Promotion summary

| Action | Count |
|--------|-------|
| ADD (new global) | 0 — avoid duplicate laws |
| UPDATE | 1 — Forge handoff cross-link optional in future WP task |
| NO_CHANGE | 12 — already covered |
| CASE_NOTE_ONLY | 5 — live in lessons + FP-0002 docs |
| FP0002_ONLY | 3 — project exceptions |
| DEFERRED_FOR_MORE_CASES | 0 |

---

## Conflict check

| Potential conflict | Resolution |
|--------------------|------------|
| Universal style scale vs `--radius-main` | V8 documented as FP0002_ONLY exception |
| Gulp partial mirror vs single SCSS | V8 documented as FP0002_ONLY exception |
| O-Centre audit vs baseline | Baseline authority wins — drift doc updated |

---

*Promotion matrix — Phase 07B.*

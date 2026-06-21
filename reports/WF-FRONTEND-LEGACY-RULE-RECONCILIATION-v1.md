# WF-FRONTEND-LEGACY-RULE-RECONCILIATION-v1

**Document type:** Legacy knowledge reconciliation — Phase F2  
**Project:** FP-0002 v2 — Shpigovsky.ru  
**Date:** 2026-06-22  
**Primary input:** [FP-0002-v2-LEGACY-RULES-EXTRACTION-v1.md](../workspaces/fp-0002-shpigovsky-v2/reports/FP-0002-v2-LEGACY-RULES-EXTRACTION-v1.md)  
**Related forensic:** [FP-0002-STRESS-TEST-FORENSIC-v1.md](FP-0002-STRESS-TEST-FORENSIC-v1.md)

**Principle:** Extract lessons. **Do not** import legacy implementation.

---

## Classification applied in v2 contract

| Tag | v2 contract action |
|-----|-------------------|
| **ADOPT** | Becomes mandatory execution law |
| **ADOPT WITH MODIFICATION** | Adopted with FP-0002 v2 adjustments (see notes) |
| **REFERENCE ONLY** | Forensic evidence — no auto-copy |
| **REJECT** | Explicitly forbidden in v2 |

**Note:** Extraction doc used **ADOPT WITH CAUTION** — mapped here to **ADOPT WITH MODIFICATION** (requires operator/FIG re-verification before wiring).

---

## 1. Gulp / build

| Rule | Classification | v2 disposition |
|------|----------------|----------------|
| HTML · SCSS · JS · Gulp · `gulp-file-include` | ADOPT | **ADOPT** — v2 zero skeleton |
| `@@` prefix, `basepath: __dirname + '/src'` | ADOPT | **ADOPT** |
| `dist/` generated only | ADOPT | **ADOPT** — hard law |
| `gulp-plumber`, `cleanDist`, `allowEmpty` | ADOPT | **ADOPT** |
| No jQuery until required | ADOPT | **ADOPT WITH MODIFICATION** — WF-PR01 allows jQuery when needed; default none |
| No SVG sprite / Font Awesome in v2 skeleton | ADOPT WITH CAUTION | **ADOPT WITH MODIFICATION** — add only when audit proves need |
| Agent self-attestation `15/15 PASS` without FIG diff | REJECT | **REJECT** — BUILT vs VERIFIED split mandatory |
| Copy `desktop-shell.html` / stress-test partials | REJECT | **REJECT** |

---

## 2. SCSS foundation

| Rule | Classification | v2 disposition |
|------|----------------|----------------|
| Layering base/abstracts/layout/sections/components | ADOPT | **ADOPT** — v2 uses `abstracts/` not legacy `utils/` |
| `@use` in entry `style.scss` | ADOPT | **ADOPT** |
| Production Standards v3 as token SSOT | ADOPT WITH CAUTION | **ADOPT WITH MODIFICATION** — re-validate vs v2 FIG before wiring |
| Legacy `_tokens.scss` values | ADOPT WITH CAUTION | **ADOPT WITH MODIFICATION** — re-derive; do not copy file |
| Pre-built header/hero/footer SCSS | REFERENCE ONLY | **REFERENCE ONLY** |
| `pages/_ui-demo.scss` demo residue | REJECT | **REJECT** |
| Forbidden typography CSS properties | ADOPT | **ADOPT** — OL-06 hard law |

---

## 3. Tokens / typography / spacing

| Domain | Classification | v2 disposition |
|--------|----------------|----------------|
| Inter, 1170px, colors, 4px scale (v3) | ADOPT WITH CAUTION | **ADOPT WITH MODIFICATION** — wire after audit + operator ack |
| Numeric Rules v2 raw extract | REFERENCE ONLY | **REFERENCE ONLY** |
| Legacy wired `_tokens.scss` | REFERENCE ONLY | **REJECT** auto-copy |

---

## 4. Source authority

| Finding | Classification | v2 disposition |
|---------|----------------|----------------|
| PDF-only A0 intake | REFERENCE ONLY | **SUPERSEDED** — FIG primary for v2 |
| `Шпиговский.fig` decodable | ADOPT WITH CAUTION | **ADOPT** — PRIMARY for v2 (pending operator lock) |
| JPG full mockup | ADOPT WITH CAUTION | **ADOPT WITH MODIFICATION** — Home visual control only |
| XLSX for URLs not header labels | ADOPT WITH CAUTION | **ADOPT WITH MODIFICATION** |
| Production Standards v3 APPROVED | ADOPT | **ADOPT** — rank 1 engineering SSOT |
| FIG extract as sole authority without diff | REJECT | **REJECT** — extract + verification gate |

---

## 5. Text fidelity

| Rule | Classification | v2 disposition |
|------|----------------|----------------|
| FIG `textData.characters` canonical | ADOPT | **ADOPT** — see Text Fidelity Contract |
| Text lock file per section | ADOPT | **ADOPT** — mandatory before HTML |
| Unreadable → UNKNOWN | ADOPT | **ADOPT** |
| INSTANCE subtree walk (`отзыв`, `Врач`, etc.) | ADOPT | **ADOPT** |
| Disclaimer strings in FIG | ADOPT WITH CAUTION | **ADOPT WITH MODIFICATION** — section-scoped review |
| Legacy header text locks v5.x | REFERENCE ONLY | **REFERENCE ONLY** — re-derive |

**Answers (Phase F5 preview):**

| Question | Answer |
|----------|--------|
| Can text be rewritten? | **NO** |
| Can text be completed? | **NO** |
| Can unreadable text be guessed? | **NO** — **SAFE UNKNOWN** |
| Can marketing text be generated? | **NO** |

---

## 6. Russian typography

| Rule | Classification | v2 disposition |
|------|----------------|----------------|
| Forbidden word-break properties | ADOPT | **ADOPT** |
| Body LH 28/24 | ADOPT WITH CAUTION | **ADOPT WITH MODIFICATION** — per v3 SSOT |
| Layout fixes not word-breaking | ADOPT | **ADOPT** |
| QA gate RU TYPOGRAPHY line | ADOPT | **ADOPT** |

---

## 7. FIG-first findings

| Finding | Classification | v2 disposition |
|---------|----------------|----------------|
| `.fig` ZIP + kiwi decoder | ADOPT | **ADOPT** |
| Page 1 mockups / Internal DS canvas | ADOPT | **ADOPT** |
| Home 15 sections | ADOPT WITH CAUTION | **ADOPT WITH MODIFICATION** — re-verify in scope |
| INSTANCE/TEXT counts | ADOPT WITH CAUTION | **ADOPT** — tooling must handle subtrees |
| 166 embedded rasters | ADOPT WITH CAUTION | **ADOPT** — Brand Asset Gate required |
| Group Register before generation | ADOPT | **ADOPT** |
| Legacy `_fig_full_build_extract.json` | REFERENCE ONLY | **REFERENCE ONLY** — regenerate |

---

## 8. Asset identity collision

| Finding | Classification | v2 disposition |
|---------|----------------|----------------|
| Hash `d3ac7d00` frame-export reuse | REJECT | **REJECT** — exclude FRAME exports |
| Wrong logo hash Skinerica | REJECT | **REJECT** — Brand Asset Detection Chain |
| 56% orphan exports | REJECT | **REJECT** — manifest `section → nodeId → src` |
| CSS gradient placeholders for thumbnails | REJECT | **REJECT** |

---

## 9. Instance / symbol risks

| Risk | Classification | v2 disposition |
|------|----------------|----------------|
| Flat TEXT extract | ADOPT (mitigate) | **ADOPT** — component walker mandatory |
| Generic «Специалист центра» ×3 | REJECT | **REJECT** |
| Hallucinated review bodies | REJECT | **REJECT** |
| Missing article thumbnails | REJECT | **REJECT** |
| Invented FAQ Q&A | REJECT | **REJECT** |

---

## 10. Visual Y-order vs layer order

| Finding | Classification | v2 disposition |
|---------|----------------|----------------|
| SECTION-10 y-order anomaly | ADOPT WITH CAUTION | **ADOPT WITH MODIFICATION** — `bounds.y` sort + HITL |
| Layer index DOM order as success | REFERENCE ONLY | **REJECT** as sole order rule |
| HITL on Y-order conflicts | ADOPT | **ADOPT** |

---

## 11. False green build

| Finding | Classification | v2 disposition |
|---------|----------------|----------------|
| Gulp PASS without FIG↔HTML diff | ADOPT (gate) | **ADOPT** — mandatory diff checklist |
| Trust agent `15/15 PASS` logs | REJECT | **REJECT** |
| Post-build forensic before operator approval | ADOPT | **ADOPT** |

---

## 12. Visual QA / shell workflow

| Rule | Classification | v2 disposition |
|------|----------------|----------------|
| Shell-first: header+footer before home sections | ADOPT | **ADOPT** — reconciled in Implementation Sequence |
| Block-by-block + operator approval | ADOPT WITH CAUTION | **ADOPT** — max 2–3 sections per agent run |
| JPG for header visual scale | ADOPT WITH CAUTION | **ADOPT WITH MODIFICATION** — secondary to FIG |
| Operator visual approval law | ADOPT | **ADOPT** |
| Legacy shell backups ACCEPTED | REFERENCE ONLY | **REFERENCE ONLY** |

---

## 13. Artefacts that must NOT be reused

| Artefact | Classification | v2 disposition |
|----------|----------------|----------------|
| `desktop-shell.html` legacy HTML | REJECT | **REJECT** |
| `section-02`…`section-14` partials | REJECT | **REJECT** |
| Legacy `_site-header.scss` etc. | REJECT | **REJECT** auto-copy |
| Collision JPG exports | REJECT | **REJECT** |
| Header geometry locks v5.x | REFERENCE ONLY | **REFERENCE ONLY** |
| Legacy `node_modules/` / `dist/` | REJECT | **REJECT** |
| M1/M2 ui-demo foundation | REJECT | **REJECT** |
| Triumph Manipulator demo | REJECT | **REJECT** |

---

## 14. Successful legacy practices (ADOPT)

Patterns that **worked** in legacy FP-0002 shell cycle — **process only**, not code:

| Practice | Evidence | v2 adoption |
|----------|----------|-------------|
| Header build as isolated checkpoint | `FP-0002-DESKTOP-HEADER-BUILD-v*` reports | **ADOPT** — after Layout Spec APPROVED |
| Footer build as separate checkpoint | Shell v0/v1 reports | **ADOPT** — after Layout Spec APPROVED |
| Header text lock before HTML | `FP-0002-HEADER-TEXT-LOCK-v5.2` | **ADOPT** — generalize to text lock files |
| Brand asset forensic fix before ship | `FP-0002-HEADER-FIG-BRAND-ASSET-FIX-v1` | **ADOPT** — Brand Asset Gate before wire |
| Desktop shell verification before mobile | Start Sequence step 6 after 3–5 | **ADOPT** — desktop-first responsive contract |
| Operator content lock on header phones/schedule | Header Text Lock | **ADOPT** — operator tie-break recorded |
| RESET when foundation false-green | `FP-0002-RESET-COMPLETE` | **ADOPT** — stop + rollback policy |

---

## 15. Reconciliation verdict

| Area | RECONCILED |
|------|------------|
| Build discipline | **YES** |
| Token/typography law | **YES** — wire deferred until foundation start |
| Source authority | **YES** — FIG-first with operator lock pending |
| Text fidelity | **YES** — NO invention |
| Asset law | **YES** |
| QA / false-green | **YES** |
| Legacy code import | **YES** — **REJECTED** |

---

*End of reconciliation — v1.*

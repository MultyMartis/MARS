# REPORT — FP-0002 V9-06E58 Figma Visual Layout Audit (Findings Only)

**Date:** 2026-07-16  
**Project:** FP-0002 «Шпиговский»  
**Runtime:** http://shpigovsky.test/  
**Mode:** Read-only visual layout audit after V9-06E58 freeze  
**Fixes:** **NOT STARTED** — awaiting operator confirmation  

---

## Authority

See `REPORTS/evidence/v9-06e58-figma-visual-layout-audit/figma-authority.md`.

Primary:

1. Approved Figma PNG exports `INCOMING/01_DESIGN/26.06.2026/` (desktop ≈1437px, mobile ≈380px)
2. Operator-approved static V9 `workspaces/fp-0002-shpigovsky-v9/dist` (metrics at 1440/480)
3. Native `Spig_v1.2.fig` present locally — **not programmatically opened** this wave

## Exclusions (confirmed)

Not scored for Figma parity:

- Global lifebuoy parallax decoration
- All Hero blocks
- Main site header
- Floating header
- Footer

Catastrophic checks only: **no overflow**, pages render, content body reachable.

## Scope captured

11 routes × 4 viewports (1440 / 1024 / 480 / 370) — full-page + content-body screenshots + metrics.  
V9 static comparison captures at 1440/480 for comparable routes.

Evidence root: `REPORTS/evidence/v9-06e58-figma-visual-layout-audit/`

## Executive summary

| Metric | Value |
|--------|-------|
| Total findings | **8** |
| CRITICAL | **0** |
| HIGH | **1** |
| MEDIUM | **4** |
| LOW | **3** |

**Overall:** Content-body implementation is **generally close to Figma/V9**. Content max-width **1230px @1440** and **465px @480** match V9 exactly; horizontal overflow not detected (`overflowX` ≤ 0). Main gaps are Home vertical rhythm utilities vs V9, institutional spacing drift, hub category composition (needs visual confirm), and shared typography/button consistency notes.

## Findings index

| ID | Sev | Route | Viewport | Section |
|----|-----|-------|----------|---------|
| E58-VA-001 | HIGH | `/` | 1440;480 | Home staff/feature/landscape/why-us spacing |
| E58-VA-002 | MEDIUM | `/o-centre/` | 1440;480 | Program/specialists band spacing |
| E58-VA-003 | MEDIUM | sitewide | 370;480 | Button height ~40–41px |
| E58-VA-004 | MEDIUM | cross-template | 1440 | H2 size consistency |
| E58-VA-005 | MEDIUM | `/uslugi/` | 1440;480 | Category section composition vs V9 |
| E58-VA-006 | LOW | blog single | 1440 | Card padding variants |
| E58-VA-007 | LOW | blog single | 1440;480 | Related→CTA vertical rhythm |
| E58-VA-008 | LOW | generic geno | 1440;480 | Generic content padding (low confidence) |

Machine-readable: `findings.csv`, `findings.json`.

## Proposed correction batches (DO NOT IMPLEMENT)

1. **Home-only spacing** — E58-VA-001 — `v9-style.css` / Home section classes  
2. **Institutional bands** — E58-VA-002 — o-centre / program partials CSS  
3. **Hub category composition** — E58-VA-005 — only after operator visual confirm vs `ref-uslugi-*.png`  
4. **Shared type/buttons** — E58-VA-003/004 — optional; 003 may be intentional V9 parity  
5. **Blog polish** — E58-VA-006/007  
6. **Generic confirm** — E58-VA-008 — verify against `ref-generic-*.png` first  

## Operator decision checklist

1. Confirm/reject **E58-VA-001** (HIGH)  
2. Confirm whether **MEDIUM** findings should be fixed  
3. Mark any false positives (especially **E58-VA-003**, **E58-VA-005**, **E58-VA-008**)  
4. Approve a correction batch charter  

**No audit corrections will be implemented before confirmation.**

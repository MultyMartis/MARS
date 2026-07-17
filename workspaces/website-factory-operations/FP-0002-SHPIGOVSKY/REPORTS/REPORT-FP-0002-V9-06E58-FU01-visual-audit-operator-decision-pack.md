# REPORT — FP-0002 V9-06E58-FU01 Visual Audit Operator Decision Pack

**Date:** 2026-07-16  
**Project:** FP-0002 «Шпиговский»  
**Mode:** Analysis + presentation only — **no product mutations**  
**Runtime:** http://shpigovsky.test/  
**Frozen product baseline:** remote `29c07d21` · local HEAD includes freeze docs commit `3c43a03e`  
**Evidence root:** `REPORTS/evidence/v9-06e58-fu01-visual-audit-operator-decision-pack/`

---

## 0. One-page operator summary

| ID | Severity | Recommendation | Confidence | Shared/local | Likely risk | Operator decision |
|----|----------|----------------|------------|--------------|-------------|-------------------|
| E58-VA-001 | HIGH | RECOMMEND CONFIRM | HIGH | local (Home) | medium — Home spacing only | |
| E58-VA-002 | MEDIUM | RECOMMEND REJECT — FALSE POSITIVE | HIGH | shared partials | n/a | |
| E58-VA-003 | MEDIUM | RECOMMEND REJECT — FALSE POSITIVE | HIGH | shared `.btn` | n/a | |
| E58-VA-004 | MEDIUM | RECOMMEND ACCEPT AS INTENTIONAL | MEDIUM | shared type roles | high if global H2 normalize | |
| E58-VA-005 | MEDIUM | RECOMMEND HOLD — INSUFFICIENT EVIDENCE | MEDIUM | shared hub | medium-high if changed blind | |
| E58-VA-006 | LOW | RECOMMEND REJECT — FALSE POSITIVE | HIGH | blog cards | n/a | |
| E58-VA-007 | LOW | RECOMMEND REJECT — FALSE POSITIVE | HIGH | blog partials | n/a | |
| E58-VA-008 | LOW | RECOMMEND REJECT — FALSE POSITIVE | HIGH | generic template | n/a | |

### Recommended for correction

- **E58-VA-001** — Home vertical rhythm missing V9 `no-top-padding` utilities (literal `@@class` in WP partials).

### Recommended rejection

- **E58-VA-002, 003, 006, 007, 008** — class-matched metrics show WP ≈ / == V9; original CSV used brittle DOM-index pairing.

### Recommended hold

- **E58-VA-005** — hub category composition needs operator visual confirm; metric width deltas are not reliable.

### Potential intentional differences

- **E58-VA-004** — multi-size `h2` scrape mixes section titles (36/26), CTA titles (~30), and chrome (~18). Not a single broken token.

Machine-readable: `evidence/v9-06e58-fu01-visual-audit-operator-decision-pack/decision-summary.csv`.

---

## 1. Status

| Item | Value |
|------|-------|
| Decision pack | **COMPLETE** (findings re-evaluated; boards + matrices created) |
| Product changes | **0** |
| DB writes | **0** |
| Commit / push / freeze | **none** |
| Exclusions honored | lifebuoy, heroes, main header, floating header, footer |

---

## 2. Baseline protection

| Check | Result |
|-------|--------|
| Freeze marker | `REPORTS/FREEZE-FP-0002-V9-06E58-CURRENT-BASELINE-BEFORE-VISUAL-AUDIT-ACCEPTED.md` |
| Canonical remote freeze commit | `29c07d21` on `origin/mars/canonical-post-recovery` |
| Local branch | `mars/canonical-post-recovery` @ `3c43a03e` (freeze docs commit; **unpushed** relative to origin tip `29c07d21`) |
| Backup | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e58-current-baseline-freeze-before-visual-audit-20260716-225434\` |
| Operator `v9-style.css` | SHA256 `307A111E…` — source **==** runtime **==** freeze |
| Theme/plugin product files | **unchanged** by this pack (reports/evidence only) |
| Runtime URL | HTTP **200** |

**SAFE UNKNOWN:** Local HEAD is one documentation commit ahead of origin freeze tip; product theme/plugin hashes were verified against freeze CSS hash, not full tree checksum of every theme file vs backup (spot-check CSS + no writes performed).

---

## 3. Evidence method (FU01)

Priority applied per charter:

1. Figma PNG exports 26.06.2026 (where route exists)  
2. V9 static dist/src  
3. Current WP runtime + E58 computed metrics  
4. CSS/templates  
5. E58 narrative as supporting context only  

**Critical re-evaluation note:** `section-padding-diffs-wp-vs-v9.csv` pairs by DOM **index**. Class-matched re-compare overturned several MEDIUM/LOW findings. Details: `evidence/.../authority-conflicts.md`.

Audit viewports only: **1440 / 1024 / 480 / 370** (no 390 substitute).

---

## 4. Proposed future correction batches (DO NOT IMPLEMENT)

Final batching depends on operator decisions. Executable candidates **after CONFIRM only**:

### Batch A — Shared spacing/typography (Home utilities)

| Field | Value |
|-------|-------|
| Finding IDs | **E58-VA-001** only |
| Likely files | `front-page.php`; `template-parts/home/why-us.php`; `staff-photo.php`; `feature-grid.php`; `clinic-landscape.php` |
| Selectors | restore `no-top-padding` / `no-top-padding--30` (CSS already in `v9-style.css`) |
| Routes | `/` |
| Risk | medium — Home-only; verify gallery neighbors |

### Batch B — Page-specific composition

| Field | Value |
|-------|-------|
| Finding IDs | **none now** (E58-VA-005 held) |
| If later confirmed | `/uslugi/` hub category CSS only after visual charter |

### Batch C — Blog-specific refinements

| Field | Value |
|-------|-------|
| Finding IDs | **none** (006/007 rejected) |

Rejected/held IDs are **not** in an executable batch.

---

# Decision cards

---

## Card E58-VA-001 — Home Vertical Rhythm

### A. Identity

| Field | Value |
|-------|-------|
| ID | E58-VA-001 |
| Severity | HIGH |
| Route | `/` |
| Page type | home |
| Viewports | 1440; 480 (also present at 1024/370 via `--pad-y`) |
| Component | `.home-why-us`, `.home-staff-photo`, `.home-feature-grid`, `.clinic-landscape` |

### B. Operator Recommendation

**RECOMMEND CONFIRM**

### C. Confidence

**HIGH** — class-matched metrics + V9 `index.html` class args + WP literal `@@class` in markup.

### D. Visual Comparison

Board: `evidence/v9-06e58-fu01-visual-audit-operator-decision-pack/E58-VA-001/comparison-board-1440.png`  
Also: `comparison-board-480.png`, `current-wp-crop-1440.png`, `v9-static-crop-1440.png`

### E. Measurements

| Property | Figma/reference | V9 static | Current WP | Difference |
|----------|-----------------|-----------|------------|------------|
| staff-photo padding-top @1440 | N/A (no 26.06 Home PNG) | 0px | 50px | **+50px** |
| staff-photo padding-bottom @1440 | N/A | 30px | 50px | +20px |
| feature-grid padding-top @1440 | N/A | 0px | 50px | **+50px** |
| feature-grid padding-bottom @1440 | N/A | 30px | 50px | +20px |
| clinic-landscape padding-top @1440 | N/A | 0px | 50px | **+50px** |
| clinic-landscape padding-bottom @1440 | N/A | 50px | 50px | 0 |
| why-us padding-top @1440 | N/A | 50px | 50px | 0 |
| why-us padding-bottom @1440 | N/A | 30px | 50px | +20px |
| staff/feature/landscape padding-top @480 | N/A | 0px | 25px | **+25px** |

`no-top-padding` **exists** in Figma-era V9 CSS and V9 Home markup; WP never applies it.

### F. Cause

| Item | Detail |
|------|--------|
| Selectors | `main > section.no-top-padding`, `...no-top-padding--30` (unused on Home) |
| Files | Home partials still emit class `@@class`; `front-page.php` does not pass V9 class args |
| Scope | **local / Home** |
| Content vs layout | **layout** |
| Operator CSS intentional? | **No** — utilities present; templates broken |

### G. Proposed Correction (do not apply)

Smallest safe fix: replace `@@class` with PHP class merge; pass V9 strings from `front-page.php` (`no-top-padding`, `no-top-padding--30`). No new tokens. Breakpoints: inherits `--pad-y`. Affected: `/` only. Risk: medium (Home rhythm neighbors).

### H. Decision Options

- [ ] CONFIRM FOR FIX
- [ ] REJECT
- [ ] ACCEPT AS INTENTIONAL
- [ ] NEED MORE EVIDENCE

---

## Card E58-VA-002 — O-centre Band Spacing

### A. Identity

| Field | Value |
|-------|-------|
| ID | E58-VA-002 |
| Severity | MEDIUM (original) |
| Route | `/o-centre/` |
| Page type | institutional |
| Viewports | 1440; 480 |
| Component | program/specialists body bands |

### B. Operator Recommendation

**RECOMMEND REJECT — FALSE POSITIVE**

### C. Confidence

**HIGH** — class-matched WP == V9 for approach / program / specialists / CTA bands.

### D. Visual Comparison

`E58-VA-002/comparison-board-1440.png` (+ WP/V9/Figma crops)

### E. Measurements

| Property | Figma/reference | V9 static | Current WP | Difference |
|----------|-----------------|-----------|------------|------------|
| specialists pt/pb @1440 | visual only | 50/50 | 50/50 | **0 vs V9** |
| program-approach-band @1440 | visual only | 50/0 | 50/0 | **0** |
| services-program-v2 @1440 | visual only | 50/50 | 50/50 | **0** |
| program-cta-band @1440 | visual only | 30/30 | 30/30 | **0** |

### F. Cause

Original finding driven by **index CSV mis-pairing**, not a real WP↔V9 delta. Shared institutional partials already aligned.

### G. Proposed Correction

None.

### H. Decision Options

- [ ] CONFIRM FOR FIX
- [ ] REJECT
- [ ] ACCEPT AS INTENTIONAL
- [ ] NEED MORE EVIDENCE

---

## Card E58-VA-003 — Button Height

### A. Identity

| Field | Value |
|-------|-------|
| ID | E58-VA-003 |
| Severity | MEDIUM (original) |
| Route | sitewide content CTAs |
| Viewports | 370; 480 (also 1440) |
| Component | `.btn` |

### B. Operator Recommendation

**RECOMMEND REJECT — FALSE POSITIVE**

### C. Confidence

**HIGH** — token + measured WP/V9 heights agree at 40px.

### D. Visual Comparison

`E58-VA-003/comparison-board-370.png`, `current-wp-btn-crop-370.png`

### E. Measurements

| Property | Figma/reference | V9 static | Current WP | Difference |
|----------|-----------------|-----------|------------|------------|
| `.btn` height | design era ~40 | 40px (majority) | 40px (majority) | **0** |
| vertical padding | — | 0 25px | 0 25px | 0 |
| border contribution | — | included in box-sizing | same | 0 |
| line-height | — | calc(40px−2px) | same | 0 |
| vs 44px guideline | N/A SoT | not SoT | 40px | −4 vs guideline only |

### F. Cause

Suspected a11y guideline ≠ design token `--main-size-btns: 40px`. Not a port defect.

### G. Proposed Correction

None (do not raise to 44px without explicit operator a11y charter).

### H. Decision Options

- [ ] CONFIRM FOR FIX
- [ ] REJECT
- [ ] ACCEPT AS INTENTIONAL
- [ ] NEED MORE EVIDENCE

---

## Card E58-VA-004 — H2 Consistency

### A. Identity

| Field | Value |
|-------|-------|
| ID | E58-VA-004 |
| Severity | MEDIUM (original) |
| Route | cross-template |
| Viewports | 1440 (responsive 26px ≤480) |
| Component | content-body section titles vs other `h2` roles |

### B. Operator Recommendation

**RECOMMEND ACCEPT AS INTENTIONAL**

### C. Confidence

**MEDIUM** — role split is clear from metrics; Figma per-component sizes not programmatically extracted from native `.fig`.

### D. Visual Comparison

`E58-VA-004/comparison-board-1440.png`

### E. Measurements

| Property | Figma/reference | V9 static | Current WP | Difference |
|----------|-----------------|-----------|------------|------------|
| Section title h2 @1440 | ~36 visual | 36px | 36px | 0 (same role) |
| Section title h2 @480/370 | ~26 visual | 26px | 26px | 0 |
| CTA-like h2 | N/A | ~30px | ~30px | intentional role |
| Chrome/footer h2 | excluded | ~18px | ~18px | not content body |

### F. Cause

Shared `--font-size-h2` for section titles; other components override. Global normalize = dangerous.

### G. Proposed Correction

None preferred. If a specific component title looks wrong later, fix **component-scoped** only.

### H. Decision Options

- [ ] CONFIRM FOR FIX
- [ ] REJECT
- [ ] ACCEPT AS INTENTIONAL
- [ ] NEED MORE EVIDENCE

---

## Card E58-VA-005 — Services Hub Category Composition

### A. Identity

| Field | Value |
|-------|-------|
| ID | E58-VA-005 |
| Severity | MEDIUM |
| Route | `/uslugi/` |
| Viewports | 1440; 480 |
| Component | `.services-category-section-v2` rows/children |

### B. Operator Recommendation

**RECOMMEND HOLD — INSUFFICIENT EVIDENCE**

### C. Confidence

**MEDIUM** — visuals exist, but metric “width diffs” are DOM-order-sensitive; content structure may explain variance.

### D. Visual Comparison

`E58-VA-005/comparison-board-1440.png`, `comparison-board-480.png` (+ Figma/V9/WP crops)

### E. Measurements

| Property | Figma/reference | V9 static | Current WP | Difference |
|----------|-----------------|-----------|------------|------------|
| Category section shell pad @1440 | visual | ~50/50 | ~50/50 | ~0 shell |
| Service row / child widths | see export | index-paired unreliable | index-paired unreliable | **do not trust CSV** |
| Grid/order/images | operator must judge boards | present | present | unresolved |

### F. Cause

Possible real composition drift **or** content/DOM structure differences. Authority ambiguous between Figma export intent and accepted V9/WP hub freeze history.

### G. Proposed Correction

**None until operator visual confirm.** Do not invent grid CSS.

### H. Decision Options

- [ ] CONFIRM FOR FIX
- [ ] REJECT
- [ ] ACCEPT AS INTENTIONAL
- [ ] NEED MORE EVIDENCE

---

## Card E58-VA-006 — Blog Single Cards

### A. Identity

| Field | Value |
|-------|-------|
| ID | E58-VA-006 |
| Severity | LOW |
| Route | `/blog/sryvy-i-retsidivy-signal-k-korrektirovke/` |
| Viewport | 1440 |
| Component | `.blog-related-card` |

### B. Operator Recommendation

**RECOMMEND REJECT — FALSE POSITIVE**

### C. Confidence

**HIGH** — WP card metrics match V9.

### D. Visual Comparison

`E58-VA-006/comparison-board-1440.png`

### E. Measurements

| Property | Figma/reference | V9 static | Current WP | Difference |
|----------|-----------------|-----------|------------|------------|
| card size @1440 | visual | 370×356 | 370×356 | 0 |
| title padding | visual | 10px 30px 0 30px | same | 0 |

### F. Cause

Shared related-card component already aligned; original “variants” over-read inner element paddings.

### G. Proposed Correction

None.

### H. Decision Options

- [ ] CONFIRM FOR FIX
- [ ] REJECT
- [ ] ACCEPT AS INTENTIONAL
- [ ] NEED MORE EVIDENCE

---

## Card E58-VA-007 — Related → CTA Transition

### A. Identity

| Field | Value |
|-------|-------|
| ID | E58-VA-007 |
| Severity | LOW |
| Route | blog single |
| Viewports | 1440; 480 |
| Component | `.blog-article-related` → `.program-cta-band-section` |

### B. Operator Recommendation

**RECOMMEND REJECT — FALSE POSITIVE**

### C. Confidence

**HIGH** — class-matched rhythm identical.

### E. Measurements

| Property | Figma/reference | V9 static | Current WP | Difference |
|----------|-----------------|-----------|------------|------------|
| related pt/pb @1440 | visual | 30/30 | 30/30 | 0 |
| CTA pt/pb @1440 | visual | 0/30 | 0/30 | 0 |
| related pt/pb @480 | visual | 25/20 | 25/20 | 0 |
| CTA pt/pb @480 | visual | 0/20 | 0/20 | 0 |

Problem is **neither** related bottom nor CTA top vs V9 — CSV swap was a mis-pair (V9 sources block shifted indices).

### G. Proposed Correction

None.

### H. Decision Options

- [ ] CONFIRM FOR FIX
- [ ] REJECT
- [ ] ACCEPT AS INTENTIONAL
- [ ] NEED MORE EVIDENCE

Board: `E58-VA-007/comparison-board-1440.png`

---

## Card E58-VA-008 — Generic Page Padding

### A. Identity

| Field | Value |
|-------|-------|
| ID | E58-VA-008 |
| Severity | LOW |
| Route | `/o-centre/programma-lecheniya/genotipirovanie/` |
| Viewports | 1440; 480 |
| Component | `.plain-page-content.generic-content-page` |

### B. Operator Recommendation

**RECOMMEND REJECT — FALSE POSITIVE**

### C. Confidence

**HIGH** for WP↔V9 padding match; Figma «Типовой контент» is a richer demo, not this leaf.

### E. Measurements

| Property | Figma/reference | V9 static | Current WP | Difference |
|----------|-----------------|-----------|------------|------------|
| plain-page padding-top | typovoy demo ≠ leaf | 48px | 48px | **0** |
| plain-page padding-bottom | typovoy demo ≠ leaf | 72px | 72px | **0** |
| content height | longer demo | taller | shorter leaf | content length only |

### F. Cause

Low-confidence original finding; CSV compared mismatched V9 node (0/0). Not operator CSS intentional change.

### G. Proposed Correction

None.

### H. Decision Options

- [ ] CONFIRM FOR FIX
- [ ] REJECT
- [ ] ACCEPT AS INTENTIONAL
- [ ] NEED MORE EVIDENCE

Board: `E58-VA-008/comparison-board-1440.png`

---

## 5. Operator Decision Form (copy-ready)

```
E58-VA-001 — CONFIRM / REJECT / INTENTIONAL / MORE EVIDENCE
E58-VA-002 — CONFIRM / REJECT / INTENTIONAL / MORE EVIDENCE
E58-VA-003 — CONFIRM / REJECT / INTENTIONAL / MORE EVIDENCE
E58-VA-004 — CONFIRM / REJECT / INTENTIONAL / MORE EVIDENCE
E58-VA-005 — CONFIRM / REJECT / INTENTIONAL / MORE EVIDENCE
E58-VA-006 — CONFIRM / REJECT / INTENTIONAL / MORE EVIDENCE
E58-VA-007 — CONFIRM / REJECT / INTENTIONAL / MORE EVIDENCE
E58-VA-008 — CONFIRM / REJECT / INTENTIONAL / MORE EVIDENCE
```

---

## 6. Files created (this pack only)

| Path | Role |
|------|------|
| `REPORTS/REPORT-FP-0002-V9-06E58-FU01-visual-audit-operator-decision-pack.md` | this report |
| `REPORTS/evidence/v9-06e58-fu01-visual-audit-operator-decision-pack/decision-summary.csv` | summary matrix |
| `.../measurement-matrix.csv` | measurements |
| `.../proposed-fix-matrix.csv` | future fixes (confirm-only) |
| `.../authority-conflicts.md` | authority notes |
| `.../E58-VA-001/` … `E58-VA-008/` | boards, crops, notes |

**Not modified:** theme, plugin, ACF, DB, uploads, V9 static, Figma, operator CSS, E58 findings artefacts.

---

## 7. Git status (expected)

- New uncommitted report + evidence under FP-0002 `REPORTS/` only  
- No product staging  
- No commit / no push  
- Foreign WIP elsewhere in monorepo **untouched**

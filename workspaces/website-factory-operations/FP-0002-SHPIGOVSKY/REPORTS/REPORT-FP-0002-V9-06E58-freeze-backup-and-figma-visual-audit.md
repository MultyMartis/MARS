# REPORT — FP-0002 V9-06E58 Freeze, Backup and Figma Visual Audit

**Date:** 2026-07-16  
**Project:** FP-0002 «Шпиговский»  
**Runtime:** http://shpigovsky.test/  

---

## 1. Overall Status

| Track | Status |
|-------|--------|
| Backup | **PASS** |
| Freeze | **PASS** — `V9-06E58 CURRENT BASELINE FROZEN BEFORE FIGMA VISUAL AUDIT` |
| Persistence / push | **PASS** (clean-worktree cherry-pick, no force) |
| Audit | **PASS (findings only)** |
| Audit fixes | **NOT STARTED** |
| Operator confirmation | **PENDING** |

---

## 2. Full Backup

| Field | Value |
|-------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e58-current-baseline-freeze-before-visual-audit-20260716-225434\` |
| Size | ≈ 1.42 GB |
| DB dump | `db/mars_wp_fp0002.sql` |
| DB SHA256 | `77C609572BC3A72D42312839CB1CD990F95B369BA53FE8D6CD4C8F1C9A76D35B` |
| Marker | `BACKUP-OK.txt` + `BACKUP-INFO.md` |
| Validation | Non-empty SQL with CREATE/INSERT; manifest + key hashes; runtime project + theme/plugin/ACF/uploads/source copies present |

**Restore point:** Full accepted baseline after Web-GPT chat migration, through E57-FIX02 + operator manual CSS, **before** any E58 visual-audit fixes. Lifebuoy decor accepted and audit-excluded.

---

## 3. Operator Manual Changes Canonized

| Item | Detail |
|------|--------|
| Pre-promote theme drift | Only `assets/css/v9-style.css` (runtime newer) |
| Classification | Operator-owned manual edit (spacing tokens `--pad-gap-line`→`--pad-gap`, accent on articles link, related body spacing) |
| Promoted | Runtime → canonical source (exact file promote) |
| Protected hash | `307A111EB229BA16C8A388C8A83B18C257C80AE57648E1601C2FA0EBF1851E04` |
| After promote | Theme product files **exact parity**; plugin **exact parity** |
| Unresolved drift | 12 source-only ACF JSON groups absent from runtime `acf-json` filesystem (accepted source authority; common files match) — **not deleted** |

Evidence: `REPORTS/evidence/v9-06e58-current-baseline-freeze/operator-manual-changes-canonized.md`

---

## 4. Frozen Baseline

Bound accepted waves:

- E53 Admin UX  
- E54 Floating header  
- E54-FIX01 Scroll preservation + background  
- E55 Site Settings admin UX  
- E56 Operator refinements (forms local no-SMTP, OverSEO, metadata/screenshot, images, interview video, Comfort admin split, gallery CSS)  
- E56-FU01 Hero/gallery corrections  
- E56-FU02 Libertinus Serif  
- E57 Lifebuoy parallax  
- E57-FIX01 / E57-FIX02 motion baseline  
- Latest operator manual CSS edits  

Freeze marker: `REPORTS/FREEZE-FP-0002-V9-06E58-CURRENT-BASELINE-BEFORE-VISUAL-AUDIT-ACCEPTED.md`

---

## 5. Freeze Validation

| Check | Result |
|-------|--------|
| Routes (corrected slugs) | Home, `/uslugi/`, RPP section, alcohol + narcissism services, o-centre, contacts, blog, blog single, generic genotyping, privacy-policy, specialist — **HTTP 200**, no PHP warnings |
| Functional markers | Floating header, lifebuoy, OverSEO, interview video, hero/gallery/swiper present; Libertinus asset HTTP 200 |
| Admin | `/wp-admin/` HTTP 200; deep authenticated ACF screens = SAFE UNKNOWN without session cookie |
| Overflow | No positive horizontal overflow in audit metrics |
| DB | Freeze writes **0** |
| Source/runtime product parity | Theme + plugin **PASS** after promote |

---

## 6. Git Persistence

| Field | Value |
|-------|--------|
| Local branch | `mars/canonical-post-recovery` |
| Local HEAD before | `df2411c9273123d9bf8b43a85388c843d5102757` |
| Source commit (dirty main) | `3c43a03e68233da31ee83a3cd0152fc4d61bf04a` |
| Clean worktree | `X:\AI MARS STORAGE\git-sync-fp0002-e58-20260716-225851\repo` |
| Remote before | `85bf2902fa31802f5adadea7b2ae180c599dbde0` |
| Merge/cherry-pick commit | `29c07d210169ff273d69e7b5f9000d84c1c097b1` |
| Remote after | `29c07d210169ff273d69e7b5f9000d84c1c097b1` |
| Ancestry | merge commit is tip of `origin/mars/canonical-post-recovery` |
| Scope | Exact-path FP-0002 allowlist (~405 files); no `git add -A` |
| Force push | **NO** |
| Dirty main | Foreign WIP untouched |

---

## 7. Figma Authority Used

- Exports: `INCOMING/01_DESIGN/26.06.2026/*.png` → audit `refs/ref-*.png`  
- V9 static: `workspaces/fp-0002-shpigovsky-v9/dist`  
- Native `.fig` present but not opened programmatically  
- Details: `REPORTS/evidence/v9-06e58-figma-visual-layout-audit/figma-authority.md`

---

## 8. Audit Scope and Exclusions

Explicitly **not** scored for Figma parity:

1. Lifebuoy decor / animation  
2. All Hero blocks  
3. Main header  
4. Floating header  
5. Footer  

Audit begins below Hero and stops before Footer.

---

## 9. Routes and Viewports Audited

| Route | Type | 1440 | 1024 | 480 | 370 | Evidence |
|-------|------|------|------|-----|-----|----------|
| `/` | home | captured | captured | captured | captured | full+body+metrics |
| `/uslugi/` | services-hub | captured | captured | captured | captured | full+body+metrics |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | service-section | captured | captured | captured | captured | full+body+metrics |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | service | captured | captured | captured | captured | full+body+metrics |
| `/uslugi/psihicheskoe-zdorovie/nartsissizm/` | service | captured | captured | captured | captured | full+body+metrics |
| `/o-centre/programma-lecheniya/genotipirovanie/` | generic | captured | captured | captured | captured | full+body+metrics |
| `/specyalisty/shipovsky/` | specialist-child | captured | captured | captured | captured | full+body+metrics |
| `/o-centre/` | institutional | captured | captured | captured | captured | full+body+metrics |
| `/kontakty/` | contacts | captured | captured | captured | captured | full+body+metrics |
| `/blog/` | blog | captured | captured | captured | captured | full+body+metrics |
| `/blog/sryvy-i-retsidivy-signal-k-korrektirovke/` | blog-single | captured | captured | captured | captured | full+body+metrics |

128 screenshots total under `REPORTS/evidence/v9-06e58-figma-visual-layout-audit/screenshots/`.

---

## 10. Executive Audit Summary

| | |
|--|--|
| Total findings | **8** |
| CRITICAL | **0** |
| HIGH | **1** |
| MEDIUM | **4** |
| LOW | **3** |

**Recurring patterns:** Home/V9 vertical-rhythm utilities missing; institutional band spacing drift; hub category composition needs visual confirm; shared H2/button consistency notes.

**Generally close to Figma/V9?** **Yes** — content max-width matches V9 exactly (1230@1440 / 465@480); no horizontal overflow; button metrics near V9.

---

## 11. Critical and High Findings

### E58-VA-001 — HIGH — Home body vertical rhythm vs V9

| Field | Value |
|-------|-------|
| Route | `/` |
| Viewports | 1440; 480 |
| Section | `.home-why-us`, `.home-staff-photo`, `.home-feature-grid`, `.clinic-landscape` |
| Current | Uniform 50/50 (desktop) / 25/25 (480) padding on staff/feature/landscape; why-us pb=50 |
| V9/Figma | V9 uses `no-top-padding` / pb≈30 on that cluster |
| Difference | ~50px extra top padding on three consecutive sections; why-us bottom +20px |
| Evidence | `screenshots/home__1440__wp__body.png`, `home__480__wp__body.png`, `metrics/home__1440__v9.json` |
| Likely source | Home section CSS / missing V9 utility classes |
| Proposed | Restore V9 spacing on these Home body sections only |
| Risk | Medium, Home-local |
| Shared? | Local (Home) |
| Confidence | High |

**CRITICAL findings:** none.

---

## 12. Medium Findings

| ID | Route | Issue |
|----|-------|-------|
| E58-VA-002 | `/o-centre/` | Program/approach/specialists/CTA band paddings diverge ~20px from V9 |
| E58-VA-003 | sitewide | Content `.btn` height ~40–41px at 370/480 (also ≈V9 — may be intentional) |
| E58-VA-004 | cross-template | H2 size sets vary by page type |
| E58-VA-005 | `/uslugi/` | Category service-row/children composition metrics diverge from V9 — **confirm vs** `refs/ref-uslugi-desktop.png` |

Full rows in `findings.csv`.

---

## 13. Low Findings

| ID | Route | Issue |
|----|-------|-------|
| E58-VA-006 | blog single | Multiple card padding variants |
| E58-VA-007 | blog single | Related→CTA vertical rhythm vs V9 (~30px swap) |
| E58-VA-008 | generic geno | Generic content padding vs V9 compare route — **low confidence** (V9 path not identical leaf) |

---

## 14. Cross-Template Consistency Findings

| Area | Note |
|------|------|
| Spacing system | Home + o-centre drift vs V9; containers consistent |
| Buttons | Shared ~40–41px; matches V9; below 44px touch guideline |
| Cards | Blog-single padding variants (LOW) |
| Typography | H2 inconsistency (MEDIUM) |
| Galleries | Present; Hero galleries excluded |
| Forms | Present; local no-SMTP accepted; not SMTP-scored |

Matrix: `component-consistency-matrix.csv`

---

## 15. Viewport-Specific Findings

| Viewport | Notes |
|----------|-------|
| 1440 | E58-VA-001/002/004/005/006/007/008 |
| 1024 | Container 1009 / pad 15 / max-width 1230 — stable; no unique CRITICAL/HIGH |
| 480 | E58-VA-001/002/003/005/007/008 |
| 370 | E58-VA-003 (buttons); no overflow |

---

## 16. What Was Intentionally Not Audited

No normal findings for lifebuoy, Heroes, main header, floating header, or footer. No catastrophic regressions observed that block content-body audit.

---

## 17. Proposed Correction Plan (DO NOT IMPLEMENT)

| Batch | IDs | Likely files | Risk | Order |
|-------|-----|--------------|------|-------|
| Home spacing | E58-VA-001 | `v9-style.css`, Home section markup/utilities | Medium | 1 |
| O-centre bands | E58-VA-002 | institutional/program CSS partials | Medium | 2 |
| Hub category (if confirmed) | E58-VA-005 | hub category CSS | Medium-high | 3 |
| Shared type/buttons (optional) | E58-VA-003, 004 | button + type scale | Medium | 4 |
| Blog polish | E58-VA-006, 007 | blog CSS | Low | 5 |
| Generic (if confirmed) | E58-VA-008 | generic template CSS | Low | 6 |

---

## 18. Risks and SAFE UNKNOWN

- Native `.fig` not opened in Dev Mode  
- Export PNG width 1437 vs audit 1440 (minor)  
- Dynamic content length ≠ Figma copy  
- Browser anti-aliasing ignored  
- Authenticated admin deep checks not re-run with login session  
- E58-VA-005 / E58-VA-008 need operator visual confirmation  

---

## 19. Audit File Status

| Item | Status |
|------|--------|
| Audit report | `REPORTS/REPORT-FP-0002-V9-06E58-figma-visual-layout-audit.md` |
| Evidence | `REPORTS/evidence/v9-06e58-figma-visual-layout-audit/` (screenshots, metrics, refs, CSVs) |
| Fixes | **None** |
| Audit commit | **Uncommitted** (default) — operator review first |
| Freeze commit | Pushed as `29c07d21` |
| Dirty main | Still dirty with foreign WIP + post-freeze audit artefacts / PROJECT-STATUS audit note |

---

## 20. Operator Decision Checklist

Please:

1. Confirm/reject **E58-VA-001** (HIGH)  
2. Confirm which **MEDIUM** findings to fix  
3. Identify false positives (especially **E58-VA-003**, **E58-VA-005**, **E58-VA-008**)  
4. Approve a correction batch  

**No visual-audit corrections will be implemented before your confirmation.**

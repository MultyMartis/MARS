# ISEO-SU SEO REVIEW PACK 01 — EVIDENCE v1

**Task ID:** ISEO-SU-SITE-OPS-SEO-REVIEW-PACK-01  
**Date:** 2026-08-24  
**Mode:** REVIEW / REPORT ONLY  
**Production mutations:** **0**  
**SEO semantic changes applied:** **0**  
**Source code / WP DB / templates / sitemap / robots / forms / Metrika / glossary / images:** **not modified**

---

## 1. Purpose

Prepare Russian SEO-facing decision materials so specialists can independently review remaining MARS audit findings after accepted technical cleanup and tell Site Ops what should actually change.

---

## 2. Source artifacts used

| Artifact | Role |
|----------|------|
| `reports/ISEO-SU-TECH-SEO-REMAINING-BACKLOG-DETAILED-RU-v1.md` | Primary remaining backlog narrative |
| `audits/tech-seo/ISEO-SU-TECH-SEO-REMAINING-BACKLOG-v1.csv` | Machine backlog + statuses |
| `ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md` | Original audit evidence (2026-08-21) |
| `reports/ISEO-SU-TECH-CLEANUP-WAVE-01-RU.md` | Accepted tech cleanup summary |
| `ISEO-SU-TECH-CLEANUP-WAVE-01-EVIDENCE-v1.md` | WAVE 01 closure evidence |
| `ISEO-SU-CURRENT-STATE-v1.md` | Current accepted project state |
| Remote tip reference | Task charter cited `9c669a70`; at sync time `origin/mars/canonical-post-recovery` was `d4ecf1a0`; pack persisted as `06a290ad` |

No live production recrawl was performed in this task. Counts for open SEO items are **original audit counts** unless a later accepted wave materially superseded them.

---

## 3. Closed technical findings deliberately excluded

| ID / defect | Status | Notes |
|-------------|--------|-------|
| SM-CHILD-404 | CLOSED | Root sitemap children repaired |
| IMG-BROKEN | CLOSED | Blog relative img → `/img/` |
| Static sitemap completeness | CLOSED | 127 public canonical static URLs; eligible omissions 0 |
| SM-MISSING-INDEXABLE | CLOSED / RECHECKED | Original 197; raw gap 161; eligible gap **0** |
| LINK-TO-REDIR | CLOSED | 129 → 0 |
| IMG-HUGE | CLOSED | 2 → 0 |

These were **not** reopened and are not SEO decision items in this pack.

---

## 4. Remaining SEO review findings (10)

| ID | Original audit scale | Reconciliation class | Notes |
|----|---------------------:|----------------------|-------|
| CANON-MISSING | 162 | SEO_DECISION_REQUIRED | Twin `/` vs `home.html` blocks autofix |
| CANON-MISMATCH | 117 | SEO_DECISION_REQUIRED | May become EXPECTED if query→clean archive confirmed |
| SM-NONINDEX | 52 | SEO_DECISION_REQUIRED | offers / offer/* / tariff-calc families |
| TITLE-DUP | ~119 largest cluster (CSV sample groups=20) | SEO_DECISION_REQUIRED | Pagination/category may be expected |
| TITLE-LONG | 24 | SEO_DECISION_REQUIRED | ~70 char heuristic |
| META-MISSING | 23 | SEO_DECISION_REQUIRED | Not an indexing error |
| META-DUP | ~137 URL involvements (distinct≈2) | SEO_DECISION_REQUIRED | Template / twin risk |
| ORPHAN-CRAWLER | 57 | SEO_DECISION_REQUIRED | Crawler graph ≠ GSC orphan |
| IMG-ALT | 445 pages | SEO_DECISION_REQUIRED | Not 445 broken images; decorative empty OK |
| OG-MISSING | 97 | SEO_DECISION_REQUIRED | Sharing quality / secondary |

**Hard-check count for SEO REVIEW FINDINGS:** **10**

---

## 5. Separate optional finding

| ID | Scale | Classification | Default posture |
|----|------:|----------------|-----------------|
| H1-MISSING | 5 | EXPECTED_BEHAVIOR_CANDIDATE / SEO OPTIONAL REVIEW | No action unless SEO has a specific reason |

Affected family (from audit): `varvara-new.php` + report-hub `client-report` query variants. Primary marketing templates not affected.

---

## 6. Status reconciliation rules applied

- Preserve original audit counts when still decision-useful.
- Label historical superseded counts explicitly (e.g. SM-MISSING-INDEXABLE 197).
- Do not present closed tech residuals as open SEO defects.
- Do not auto-classify CANON-MISMATCH / SM-NONINDEX / TITLE-DUP / IMG-ALT as EXPECTED without SEO confirmation — only as candidates where evidence supports that possibility.
- Do not change semantic status of open findings in CURRENT-STATE beyond registering that a decision pack exists.

---

## 7. Artifacts produced by this task

| Path | Audience |
|------|----------|
| `reports/ISEO-SU-SEO-REVIEW-PACK-01-RU.md` | SEO team (Russian) |
| `reports/ISEO-SU-SEO-DECISION-CHECKLIST-01-RU.md` | SEO fill-in checklist |
| `ISEO-SU-SEO-REVIEW-PACK-01-EVIDENCE-v1.md` | Internal evidence (this file) |
| `reports/REPORT-ISEO-SU-SITE-OPS-SEO-REVIEW-PACK-01.md` | MARS task REPORT |

---

## 8. Project brain touch

- Artifact register: add SEO review pack references.
- OPERATIONAL-INDEX: point open SEO work at decision pack / awaiting SEO answers.
- CURRENT-STATE: minimal note only if needed to register pack existence; **no** finding semantic status flip without SEO decision.

---

## 9. Explicit non-actions

- No fixes  
- No production mutation  
- No template / DB / metadata / sitemap / robots / forms / Metrika / glossary / image changes  
- No mass title/description/alt/canonical generation  

---

## 10. Final evidence verdict

| Check | Value |
|-------|-------|
| SEO REVIEW FINDINGS | 10 |
| H1 representation | EXPECTED_BEHAVIOR CANDIDATE / SEO OPTIONAL REVIEW |
| CLOSED TECH FINDINGS REOPENED | 0 |
| SEO SEMANTIC CHANGES APPLIED | 0 |
| PRODUCTION MUTATIONS | 0 |
| SEO-FACING REPORT CREATED | YES |
| SEO DECISION CHECKLIST CREATED | YES |
| INTERNAL EVIDENCE CREATED | YES |
| PROJECT ARTIFACTS PERSISTED | YES (`06a290ad`) |
| REMOTE SYNC | COMPLETE (`origin/mars/canonical-post-recovery` @ `06a290ad`) |

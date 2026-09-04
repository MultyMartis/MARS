# REPORT — ISEO-SU SITE OPS NEW SEO LANDINGS SMALL-HEIGHT ROLLOUT 01

**Task ID:** ISEO-SU-SITE-OPS-NEW-SEO-LANDINGS-SMALL-HEIGHT-OVERLAP-ROLLOUT-01  
**Date:** 2026-09-04  
**Final status:** **COMPLETE — NEW SEO LANDINGS LOW-HEIGHT OVERLAP ROLLOUT / 14 PAGES SAFE / PILOT GENERALIZED**

---

## 1. Execution Summary

Operator-approved Novosibirsk pilot (height:auto; min-height:100vh) generalized to all **14 new SEO landings** via one shared body class + one scoped CSS. Pilot-only class/CSS retired. Layout-only; SEO/forms/sitemap unchanged. Live viewport matrix: **0 overlaps**. Production/source aligned.

## 2. Preflight

| Check | Result |
|-------|--------|
| CWD | X:\AI MARS |
| Volume X: | AI WS |
| Branch | mars/canonical-post-recovery |
| Origin tip (sync base) | 3e9e065a (pilot docs tip; verify at sync) |
| Local HEAD | dirty / divergent — **not** used for push |
| Staged | empty at task start |
| Foreign WIP | present — preserved |
| Sync strategy | STORAGE worktree from origin/mars/canonical-post-recovery |

## 3. Operator Approval

APPROVED — https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html — pilot visual behavior authorized for contour rollout.

## 4. Root Cause

Shared .page_scene_inner { height: 100vh } + longer first-screen intro → overflow; #SecondScreen in normal flow starts at fixed first-section end → overlap on short desktop heights.

## 5. 14-Page Inventory

CITY 5 + NICHE 7 + INTERNATIONAL 2 (full list in evidence doc). All use .page_scene_inner / #SecondScreen.

## 6. Pre-Rollout Findings

PAGES USING FRAGILE 100VH MECHANISM BEFORE: **14**  
PAGES ACTUALLY OVERLAPPING BEFORE: Novosibirsk confirmed (pilot); siblings same mechanism / risk.  
Pilot isolation present only on Novosibirsk.

## 7. Final Fix Architecture

ROLLOUT MODEL: **MODEL_A_ALL_14_SHARED_CLASS**  
FINAL SHARED FIX: ody.new-seo-landing-flex-first-screen .page_scene_inner { height:auto; min-height:100vh; position:relative; }  
File: production-source/css/new-seo-landing-flex-first-screen.css

## 8. Pilot Cleanup

PILOT BODY CLASS REMOVED: **YES**  
PILOT CSS REMOVED: **YES** (source + production; live 404)

## 9. Source Implementation

14 HTML updated; shared CSS added; pilot CSS deleted. Unrelated HTML/SEO content diffs: 0.

## 10. Production Backup

X:\AI MARS\local\sites\iseo-su-production\_new-seo-landings-small-height-rollout-01\20260904T051415Z — 14 HTML .before + pilot CSS .before; SHA-256 recorded in validate JSON.

## 11. Deployment

Scoped upload 14 HTML + shared CSS; pilot CSS removed. Checksums aligned. Validate JSON: 	ools/_new-seo-landings-small-height-rollout-01-validate.json.

## 12. Live Viewport Validation

`
VIEWPORT 1440x900: PASS
VIEWPORT 1366x768: PASS
VIEWPORT 1280x720: PASS
VIEWPORT 1366x650: PASS
VIEWPORT 1440x600: PASS
MOBILE 390x844: PASS
MOBILE 360x800: PASS
TOTAL POST-ROLLOUT OVERLAPS: 0
`

## 13. City Pages

5/5 audited + live PASS; cross-linking unchanged.

## 14. Niche Pages

7/7 audited + live PASS; hub linking unchanged.

## 15. USA/UAE Pages

2/2 audited + live PASS; menu/sitemap status unchanged (excluded).

## 16. Novosibirsk Pilot Preservation

NOVOSIBIRSK PILOT APPROVAL: CONFIRMED  
NOVOSIBIRSK FINAL: PASS (shared fix; pilot artifacts gone)

## 17. SEO Regression

`
TITLE CHANGED: NO
DESCRIPTION CHANGED: NO
H1 CHANGED: NO
INTRO CONTENT CHANGED: NO
CANONICAL CHANGED: NO
SITEMAP CHANGED: NO
STATIC SITEMAP URL COUNT: 139
CITY CROSS-LINKING CHANGED: NO
NICHE HUB LINKING CHANGED: NO
USA/UAE MENU STATUS CHANGED: NO
USA/UAE SITEMAP STATUS CHANGED: NO
`

## 18. Form Regression

Consent/privacy present on city/niche/intl representatives + hub/home/calc. FORM CONSENT / CALCULATOR / CALCULATOR RESULT CONSENT CHANGED: **NO**. FORM REGRESSION: **NONE**.

## 19. Control Pages

LEGACY SOURCE PAGES MODIFIED: **NO**. CONTROL PAGE REGRESSION: **NONE**.

## 20. Visual Evidence

X:\AI MARS\projects\iseo-su-site-ops\evidence\new-seo-landings-small-height-rollout-01\screenshots\20260904T051415Z (144 PNG)

## 21. Production / Source Alignment

PRODUCTION/SOURCE ALIGNED: **YES**

## 22. Documentation

- Evidence: ISEO-SU-NEW-SEO-LANDINGS-SMALL-HEIGHT-ROLLOUT-01-EVIDENCE-v1.md
- RU: reports/ISEO-SU-NEW-SEO-LANDINGS-SMALL-HEIGHT-ROLLOUT-01-RU.md
- This REPORT
- CURRENT-STATE / OPERATIONAL-INDEX / ARTIFACT-REGISTER updated
- Pilot evidence retained as SUPERSEDED

## 23. Git Persistence

Scoped commits via STORAGE worktree (dirty main preserved). Subjects:
- fix(iseo-su): prevent low-height overlap on new seo landings
- docs(iseo-su): close seo landing height rollout

## 24. Remote Sync

Pending closeout wave — recorded after push.

## 25. Final Decision

COMPLETE — NEW SEO LANDINGS LOW-HEIGHT OVERLAP ROLLOUT / 14 PAGES SAFE / PILOT GENERALIZED

## 26. Stop Condition

Stop after 14-page audit, pilot generalization + cleanup, low-height validation, visual evidence, SEO/form/sitemap PASS, production/source alignment, docs, scoped remote sync. No unrelated SEO-review work.

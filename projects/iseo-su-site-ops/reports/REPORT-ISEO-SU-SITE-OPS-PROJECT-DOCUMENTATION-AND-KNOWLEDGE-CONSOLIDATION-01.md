# REPORT — ISEO-SU SITE OPS PROJECT DOCUMENTATION AND KNOWLEDGE CONSOLIDATION 01

**Task:** `ISEO-SU-SITE-OPS-PROJECT-DOCUMENTATION-AND-KNOWLEDGE-CONSOLIDATION-01`  
**Date:** 2026-08-24  
**Mode:** documentation-only / clean worktree  
**Production mutations:** 0

## 1. Execution Summary

Current i-seo.su architecture, operating state, feature baselines, open technical work, protected zones, and next-task routing were consolidated under `projects/iseo-su-site-ops/`. Current authorities now separate `DONE`, `OPEN_TECH`, `SEO_REVIEW`, `EXPECTED`, `DEFERRED_OPTIONAL`, `SAFE_UNKNOWN`, `HISTORICAL`, and `SUPERSEDED`. Historical REPORT files were not rewritten.

## 2. Environment Preflight

| Check | Evidence/result |
|---|---|
| Canonical main workspace | `X:\AI MARS` |
| Required volume | `X:` label `AI WS` |
| Required canonical branch | `mars/canonical-post-recovery` |
| Local main HEAD at task intake | `7110b663` with foreign unpushed history |
| Canonical remote/worktree base | `a2cae763e9b2b4e3d37ef59ef442364498581ade` |
| Implementation worktree | `X:\AI MARS STORAGE\git-sync-iseo-su-docs-consolidation\repo` |
| Implementation branch | `mars/iseo-su-docs-consolidation` |
| Project-owned WIP at start | none |
| Staged changes at start | none |
| Worktree HEAD vs canonical base | matched `a2cae763` |

The worktree was clean before edits. Foreign main-workspace WIP was not staged, restored, moved, or cleaned.

## 3. Documentation Inventory

Task intake recorded **357 files** in recursive project inventory and **306 Markdown matches** (including current docs, feature evidence, historical REPORTs, content docs, and READMEs).

Inventory was classified by families:

- `CURRENT/CANONICAL`: current state, KB, routing/matrix, protected zones, registers, index;
- `SPECIALIZED_CURRENT`: forms, Metrika IP, glossary, sitemap, tech SEO;
- `HISTORICAL_REPORT`: completed phase/task REPORTs;
- `HISTORICAL_EVIDENCE`: accepted snapshots/acceptance/closeout evidence;
- `SUPERSEDED`: old recipient/draft/sitemap/onboarding guidance;
- `RAW/DERIVED`: audit CSVs, corpus files, generated evidence;
- `OPTIONAL_REFERENCE`: older maps/methodology still useful for bounded context.

No historical files were deleted.

## 4. Current Authorities

Current authority order is now:

1. `ISEO-SU-CURRENT-STATE-v1.md`
2. `ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md`
3. `ISEO-SU-TASK-ROUTING-GUIDE-v1.md`
4. `ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md`
5. `ISEO-SU-PROTECTED-ZONES-v1.md`
6. feature-specific baselines/evidence
7. `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
8. historical REPORTs/evidence

## 5. Architecture Knowledge Base

`ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md` retains the v1 filename and now contains all required 27 current-authority sections, from Project Identity through Canonical Supporting Documents, with the required operational subheadings.

It records the hybrid static/direct PHP-HTML + WordPress model, exact route ownership, forms, Metrika, glossary, sitemap target/current defect, technical SEO backlog, WPilot safe state, production operations, Git/source model, protected zones, completed milestones, open/deferred work, and SAFE UNKNOWN. The older 2026-07-24 capture remains available through historical evidence and Git history; it is not embedded in the primary KB.

## 6. Current State

`ISEO-SU-CURRENT-STATE-v1.md` now has exactly 15 requested sections. It is compact and explicitly states:

- current single form recipient and `test_mode` OFF;
- counter 54287016 and visitor-IP addon ON;
- glossary final counts/status;
- current sitemap defect and target architecture;
- four open technical task groups;
- five deferred optional items;
- protected/source/Git rules and next-task entry.

## 7. Forms Knowledge

Current documentation now clearly records:

- 12 root handlers plus service delegates;
- shared validation/config/token architecture;
- honeypot `contact_company_url`;
- HMAC/minimum fill ≈3 seconds;
- ≈3/5m/form/IP and ≈10/h/IP rate limits;
- ≈10-minute duplicate suppression;
- CAPTCHA absent;
- active production recipient exactly `nikel007i33@yandex.ru`;
- `test_mode=false`;
- `im.work@mail.ru` historical acceptance-only and removed;
- `im.work@nail.ru` invalid historical typo;
- `chrra@yandex.ru` inactive historical comment only.

No form code/config/runtime was changed.

## 8. Metrika Knowledge

The KB/current docs and specialized baseline identify:

- production counter 54287016;
- `ipaddress` parameter;
- validated IPv4/IPv6 `REMOTE_ADDR`;
- no forwarded-header trust;
- production config/endpoint/JS/loader paths;
- MARS source `production-source/metrika-ip/`;
- current state ON and accepted true→false→true switch test;
- exact false kill-switch behavior;
- normal Metrika/Webvisor unaffected when addon is OFF;
- analytics/manual investigation only; no auto-blocking.

No analytics/runtime mutation occurred.

## 9. Glossary Knowledge

Current authority records:

- source 241;
- public 184;
- MERGED 30, DEFERRED 14, EXCLUDED 13;
- archive and eligible singles HTTP 200; sitemap term URLs 184;
- public archive/singles, related terms, desktop menu;
- services-derived `page_scene` without rates;
- archive H1/intro/title; singles no hero description;
- CTA `Подробнее` → `#SecondScreen`;
- mobile overflow fixed; mobile offcanvas deferred;
- production work complete/frozen.

Draft-only/anonymous-404 routing instructions were removed from current operational guidance.

## 10. Sitemap Knowledge

Created `ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md` with exactly the required eight sections.

It distinguishes:

- working `/sitemap-static.xml`;
- working `/wp-sitemap.xml`;
- defective `/sitemap.xml` with three observed 404 children;
- valid target `<sitemapindex>` semantics with two absolute child `<loc>` entries;
- planned robots-only-root policy;
- open static maintenance decision;
- audit evidence;
- open implementation/validation/rollback task.

The target is explicitly **not implemented**.

## 11. Tech SEO Audit Knowledge

Current summary remains evidence-based: 1033 crawled; 643 indexable; 0 critical; 2 high; 6 medium; 8 low; 14 review; 0 page 4xx/5xx; 0 broken internal links.

- `SM-CHILD-404` → HIGH / `OPEN_TECH` / MARS / SITE OPS.
- `IMG-BROKEN` → HIGH / `OPEN_TECH` / MARS / SITE OPS.
- remaining IDs use actual findings CSV owner and are routed to `SEO_REVIEW` where judgment is required.
- `SM-DUAL-ARCH` → INFO / `EXPECTED`.

Audit CSVs and historical reports were read but not edited.

## 12. WPilot Knowledge

Accepted current state is explicit: RC6 active; token local-only; `bridge=false`; `write=false`; `dev_confirmed=false`; Phase 6D deferred optional. WPilot onboarding/6D is not a prerequisite for ordinary Site Ops.

## 13. Production Operations

Current KB records local-only access authority, fresh Beget/full and scoped backup requirements, bounded SFTP behavior, VPN/network resume rules, deployment validation, rollback, and runtime→diff→canonical-source promotion. No production connection or probe was used in this task.

## 14. Protected Zones

Protected now means “inspect/change intentionally,” not permanent freeze. Coverage includes:

- forms, shared security/config, current recipient, anti-spam invariants;
- counter 54287016 and visitor-IP kill switch;
- glossary final baseline and operator CSS;
- manual runtime edits/source promotion;
- shared CSS/JS/form dependencies;
- `/sitemap.xml`, `/sitemap-static.xml`, `/wp-sitemap.xml`, and robots target/current policy;
- routing/config/core/ACF/offers/calculator/secrets and sibling surfaces.

## 15. Open Work

1. Root sitemap repair and later robots verification.
2. Static sitemap maintenance strategy/implementation.
3. Blog relative-image-path repair and targeted regression crawl.
4. Remaining technical/SEO audit backlog review/routing.

None was implemented in this task.

## 16. Deferred Optional Work

Exactly five:

1. mobile glossary offcanvas parity;
2. glossary archive Yoast meta description;
3. MERGED alias/search polish;
4. sitemap duplication beyond the target architecture if justified;
5. WPilot Phase 6D bridge/read-only smoke.

## 17. SAFE UNKNOWN

The register now separates 14 named non-blocking unknowns from four open task groups and five deferred options. `U-022` is closed because canonical source mirrors now exist; this does not claim complete mirroring of every production file.

**SECURITY RISK (pre-existing, not modified):** tracked `production-source/forms/iseo-form-config.php` contains form HMAC secret material. No secret value was read into, copied to, or added by this documentation wave. Remediation, if desired, requires a separate exact secret-rotation/source-history charter.

## 18. Superseded Statements Reconciled

Corrected current guidance included:

- forms have no recipient/server validation;
- `im.work@mail.ru` is active production routing;
- typo `im.work@nail.ru` is valid;
- `chrra@yandex.ru` is active;
- glossary is draft-only/unpublished/anonymous 404;
- glossary menu/overflow remain unresolved;
- old example Metrika counter is production;
- visitor-IP addon does not exist;
- root Yoast-style sitemap is healthy;
- open required count is zero;
- WPilot onboarding/6D is required for normal Site Ops.

Historical evidence retaining earlier facts was not modified.

## 19. Artifact Register

The register now provides top-level CURRENT/CANONICAL/SPECIALIZED/HISTORICAL/SUPERSEDED classes, records inventory by family, includes the new sitemap document and this consolidation report, and reclassifies completed task REPORTs as historical evidence.

## 20. Operational Index

The top now routes future agents in the required current-first order. It explicitly lists four open task groups, five deferred optional items, and marks implementation targets as not complete. Expanded legacy navigation is collapsed and subordinate to current authorities.

## 21. Files Created or Updated

Updated:

1. `projects/iseo-su-site-ops/ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md`
2. `projects/iseo-su-site-ops/ISEO-SU-CURRENT-STATE-v1.md`
3. `projects/iseo-su-site-ops/ISEO-SU-TASK-ROUTING-GUIDE-v1.md`
4. `projects/iseo-su-site-ops/ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md`
5. `projects/iseo-su-site-ops/ISEO-SU-PROTECTED-ZONES-v1.md`
6. `projects/iseo-su-site-ops/ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md`
7. `projects/iseo-su-site-ops/ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md`
8. `projects/iseo-su-site-ops/ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md`
9. `projects/iseo-su-site-ops/ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
10. `projects/iseo-su-site-ops/OPERATIONAL-INDEX.md`
11. `projects/iseo-su-site-ops/ISEO-SU-GLOSSARY-FINAL-CORPUS-v1.md` — concurrent current-state reconciliation observed in the shared worktree
12. `projects/iseo-su-site-ops/ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md` — concurrent sitemap-current-state reconciliation observed
13. `projects/iseo-su-site-ops/ISEO-SU-WORDPRESS-OBJECT-AND-TEMPLATE-MAP-v1.md` — concurrent glossary-current-state reconciliation observed
14. `projects/iseo-su-site-ops/README.md` — concurrent current-first entry reconciliation observed

Created:

15. `projects/iseo-su-site-ops/ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md`
16. `projects/iseo-su-site-ops/reports/REPORT-ISEO-SU-SITE-OPS-PROJECT-DOCUMENTATION-AND-KNOWLEDGE-CONSOLIDATION-01.md`

The four explicitly marked concurrent edits were not overwritten or restored by this subagent; they are relevant project documentation and must be included in the parent/operator's final review.

## 22. Production Mutations

**0.** No website, WordPress, form, Metrika, sitemap, robots, CSS, JS, PHP, CSV, secret, or runtime mutation.

## 23. Git Persistence

**COMPLETE** — this REPORT is part of the single scoped documentation commit that last modified it. Only the 16 documentation paths listed in §21 were selected; no production source, audit CSV, raw crawl, secret, scratch, foreign WIP, or unrelated project path was staged.

## 24. Remote Sync

**COMPLETE** — the scoped documentation commit was fast-forward pushed from the clean sync worktree to `origin/mars/canonical-post-recovery`; no force push. Exact resulting commit/tip is reported by `git log -1` and in the task handoff.

## 25. Final Decision

**COMPLETE — ISEO-SU PROJECT KNOWLEDGE CONSOLIDATED / MARS BRAIN CURRENT / DOCUMENTATION CANONICAL**

Final hard check:

```text
PRIMARY KNOWLEDGE BASE: ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md — CURRENT / CANONICAL
CURRENT STATE: ISEO-SU-CURRENT-STATE-v1.md — CURRENT / CANONICAL
TASK ROUTING GUIDE: ISEO-SU-TASK-ROUTING-GUIDE-v1.md — CURRENT
ROUTE OWNERSHIP MATRIX: ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md — CURRENT
PROTECTED ZONES: ISEO-SU-PROTECTED-ZONES-v1.md — CURRENT
FORM SECURITY BASELINE: ISEO-SU-FORM-SECURITY-AND-ANTISPAM-BASELINE-v1.md — CURRENT
METRIKA IP BASELINE: ISEO-SU-METRIKA-VISITOR-IP-PARAM-BASELINE-v1.md — CURRENT
GLOSSARY FINAL BASELINE: ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md — CURRENT
SITEMAP CURRENT-STATE DOC: ISEO-SU-SITEMAP-ARCHITECTURE-AND-CURRENT-STATE-v1.md — CURRENT / OPEN IMPLEMENTATION
TECH SEO AUDIT AUTHORITY: ISEO-SU-TECH-SEO-AUDIT-EVIDENCE-v1.md + findings CSV
ARTIFACT REGISTER: ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md — CURRENT
OPERATIONAL INDEX: OPERATIONAL-INDEX.md — CURRENT

CURRENT FORM RECIPIENT: nikel007i33@yandex.ru
METRIKA COUNTER: 54287016
METRIKA IP ADDON: DOCUMENTED
METRIKA IP FEATURE STATE: ON
GLOSSARY PUBLISHED: 184
OPEN HIGH TECH ISSUES: 2
OPEN REQUIRED TECH TASKS: 4
DEFERRED OPTIONAL COUNT: 5
SAFE UNKNOWN COUNT: 14

STALE CURRENT FACTS FOUND: 10 claim classes
STALE CURRENT FACTS CORRECTED: 10 claim classes
HISTORICAL REPORTS REWRITTEN: NO
PRODUCTION MUTATIONS: 0
PROJECT-OWNED UNCOMMITTED DOC TAIL: 0
REMOTE SYNC: COMPLETE
```

## 26. Stop Condition

Met: documentation inventory; KB/current-state/maps/baseline/register/index reconciliation; consistency, lint/link, and secret-boundary checks; one scoped documentation commit; canonical fast-forward remote sync. No sitemap, blog image, SEO, form, Metrika, glossary, WPilot, or production implementation was performed.

## Execution safety

- cwd: `X:\AI MARS STORAGE\git-sync-iseo-su-docs-consolidation\repo`
- scope lock honored: yes
- destructive ops: none
- protected zone touch: documentation descriptions only; no production/runtime touch

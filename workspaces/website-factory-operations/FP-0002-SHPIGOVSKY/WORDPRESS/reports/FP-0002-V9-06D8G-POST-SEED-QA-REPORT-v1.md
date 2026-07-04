# REPORT — FP-0002 V9-06D8-G POST-SEED QA

**Date:** 2026-07-05  
**Task:** V9-06D8-G Post-Seed QA  
**Verdict:** PARTIAL PASS  
**Operator authorization:** YES

---

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: `X:\AI MARS`
- Branch: mars/canonical-post-recovery
- Local HEAD: `aa2cce97e993842874c84e622f9a368a3f78654b`
- Local short HEAD: `aa2cce97`
- Remote HEAD: `aa2cce97e993842874c84e622f9a368a3f78654b`
- Remote short HEAD: `aa2cce97`
- Ahead: 0
- Behind: 0
- Foreign WIP: Present unstaged/untracked (includes D8-A…E helpers, Corvonero docs) — not staged
- Pre-existing staged files: none
- Strict HEAD gate: **PASS_WITH_HEAD_NOTE** — local/remote synced 0/0; required D8-E HEAD `77c79dc` is direct ancestor (+1 unrelated C2b commit)
- Result: PASS_WITH_HEAD_NOTE

## 2. Authorization and scope

- Operator authorization: YES
- Task mode: READ-ONLY QA
- Runtime delivery: NOT_PERFORMED
- Source changes: 0 (docs/evidence only)
- Runtime file writes: 0
- DB writes: 0
- ACF writes: 0
- Native content writes: 0
- Options writes: 0
- Home writes: 0
- Services Hub writes: 0
- Service CPT writes: 0
- Contacts writes: 0
- Menu changes: 0
- Redirects: 0
- Object changes: 0
- Rewrite/permalink changes: NO
- Plugin source changes: 0
- ACF JSON changes: 0
- V9 src/dist changes: 0
- Media uploads: 0
- External API/API key changes: NO
- Live endpoint changes: NO
- Documentation/evidence writes: YES (D8-G scope only)
- Result: PASS

## 3. Authority review

- D8-E Contacts Content Seed: reviewed — PASS / 3 ACF writes / ALL_200
- D8-D Services Hub Content Seed: reviewed — PASS / 2 hub ACF writes
- D8-C Services MVP Content Seed: reviewed — PASS / 15 service ACF writes
- D8-B Home Content Seed: reviewed — PARTIAL PASS / 2 home ACF writes
- D8-A Site Options Seed: reviewed — PASS / 11 options seeded (resume)
- D8 planning: reviewed — gap map + seed wave design + Olga UX plan
- D7-F final QA: reviewed — ALL_200 baseline confirmed
- ACF/source: read-only inspection — 13 groups, theme/plugin unchanged
- Status docs: README, SOURCE-AUTHORITY, PROJECT-STATUS read
- Result: PASS

## 4. Runtime identity and DB read-only gate

- Runtime: `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky` — exists
- Domain: `http://shpigovsky.test/`
- HTTP status: 200
- wp-load: PASS
- DB connection: PASS (`mars_wp_fp0002`, prefix `fp02_`)
- Active theme: shpigovsky
- Active plugin: shpigovsky-core
- Core mode: content_model
- Service CPT: registered
- ACF PRO: active
- ACF groups: 13
- WPilot write_enabled: false (not true)
- Objects 4/5/20/73/74/77/84: all exist publish
- Result: PASS

## 5. Post-seed route matrix

| Route | URL | HTTP | Expected object | Resolved object | Header | Footer | CSS | JS | Result |
|---|---|---:|---|---|---:|---:|---:|---:|---|
| Home | `/` | 200 | page #4 | page #4 | yes | yes | yes | yes | PASS |
| Services Hub | `/uslugi/` | 200 | page #5 | page #5 | yes | yes | yes | yes | PASS |
| Service 73 | `/uslugi/zavisimosti/` | 200 | service #73 | service #73 | yes | yes | yes | yes | PASS |
| Service 74 | `/uslugi/.../alkogol/` | 200 | service #74 | service #74 | yes | yes | yes | yes | PASS |
| Service 77 | `/uslugi/psihicheskoe-zdorovie/` | 200 | service #77 | service #77 | yes | yes | yes | yes | PASS |
| Service 84 | `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | service #84 | service #84 | yes | yes | yes | yes | PASS |
| Contacts | `/kontakty/` | 200 | page #20 | page #20 | yes | yes | yes | yes | PASS |

## 6. ACF/content integrity audit

| Scope | Expected seeded state | Actual state | Unexpected mutation | Result |
|---|---|---|---|---|
| D8-A Site Options | 11 seeded + 5 skipped empty | All match | none | PASS |
| D8-B Home #4 | advantages + FAQ seeded; hero retained; media skipped | Match | none | PASS |
| D8-C Services 73/77/84 | programme/stages/FAQ seeded | Populated repeaters | hero_lead D4 retained (not D8 mutation) | PASS |
| D8-C Service 74 | intro/signs/programme/stages/FAQ seeded | All populated | none | PASS |
| D8-D Hub #5 | intro + FAQ seeded; dev fields unchanged | Match | none | PASS |
| D8-E Contacts #20 | intro/address/blocks seeded; map/messengers skipped | Match | contacts_phones pre-existing (Options canonical) | PASS |

## 7. No-scope-drift verification

- D8-G DB writes: 0
- Runtime files changed: 0
- Source files changed: docs/evidence/status only
- ACF writes: 0
- Options writes: 0
- Content writes: 0
- Menus changed: 0
- Redirects created: 0
- Rewrite flush: NOT_PERFORMED
- Object counts changed: 0
- Media uploads: 0
- Plugin changes: 0
- External API keys: 0
- Live endpoint: NOT_ADDED
- Result: PASS

## 8. Visual smoke

| Screenshot | Route | Viewport | Captured | Main result | Notes |
|---|---|---|---:|---|---|
| desktop-home-after-d8g.png | `/` | desktop | yes | PASS | Shell + seeded sections |
| desktop-services-hub-after-d8g.png | `/uslugi/` | desktop | yes | PASS | Hub layout OK |
| desktop-service-zavisimosti-after-d8g.png | zavisimosti | desktop | yes | PASS | Subdivision stack |
| desktop-service-alkogol-after-d8g.png | alcohol | desktop | yes | PASS | Signs/programme visible |
| desktop-service-psych-after-d8g.png | psych | desktop | yes | PASS | Parent service |
| desktop-service-rpp-after-d8g.png | RPP | desktop | yes | PASS | Parent service |
| desktop-contacts-after-d8g.png | `/kontakty/` | desktop | yes | PASS | Intro + locations |
| mobile-home-after-d8g.png | `/` | mobile | yes | PASS | No catastrophic overflow |
| mobile-services-hub-after-d8g.png | `/uslugi/` | mobile | yes | PASS | Shell intact |
| mobile-service-alkogol-after-d8g.png | alcohol | mobile | yes | PASS | Service stack OK |
| mobile-contacts-after-d8g.png | `/kontakty/` | mobile | yes | PASS | Contacts body OK |
| mobile-service-zavisimosti-after-d8g.png | zavisimosti | mobile | yes | PASS | optional |
| mobile-service-psych-after-d8g.png | psych | mobile | yes | PASS | optional |
| mobile-service-rpp-after-d8g.png | RPP | mobile | yes | PASS | optional |

## 9. Admin usability summary

| Area | Accessible | Seeded values visible | Main issue | Suggested action | Result |
|---|---:|---:|---|---|---|
| Site Options | yes | yes | English labels | D8-F RU labels | PARTIAL |
| Home #4 | yes | yes | Repeater density | D8-F help text | PARTIAL |
| Services Hub #5 | yes | yes | query_mode visible | D8-F hide dev fields | PARTIAL |
| Services 73/74/77/84 | yes | yes | Stacked groups | D8-F reorder | PARTIAL |
| Contacts #20 | yes | yes | Phone source overlap | D8-F canonical note | PARTIAL |

## 10. Post-seed blocker/debt register

| Item | Class | Blocks visual review | Blocks production | Suggested owner/action |
|---|---|---:|---:|---|
| Map URL missing | OPERATOR_DATA_REQUIRED | no | yes | Operator |
| Messenger/social URLs | OPERATOR_DATA_REQUIRED | no | yes | Operator |
| Legal identifiers | OPERATOR_DATA_REQUIRED | no | yes | Legal |
| Media uploads | MEDIA_REQUIRED | no | yes | Media wave |
| FAQ placeholder copy | CONTENT_REVIEW | no | no | Olga |
| Service 74 medical copy | CONTENT_REVIEW | no | yes | Clinical review |
| English ACF labels | ADMIN_UX_DEBT | no | no | D8-F |
| Developer fields visible | ADMIN_UX_DEBT | no | no | D8-F |
| Deferred shared blocks | DEFER_AFTER_MVP | no | no | Post-MVP |

## 11. Readiness decision

**READY_FOR_OPERATOR_VISUAL_REVIEW**

All seven routes are HTTP 200. Seeded ACF integrity passes. Visual smoke shows intact global shell with expected media/operator gaps only. Admin UX is PARTIAL (English labels) but does not block a local visual walkthrough. Optional D8-F can follow operator feedback.

## 12. Documentation changes

| File | Action | Reason |
|---|---|---|
| `reports/FP-0002-V9-06D8G-POST-SEED-QA-REPORT-v1.md` | created | Task report |
| `architecture/FP-0002-V9-06D8G-*.md` (7 files) | created | D8-G architecture pack |
| `validation/v9-06d8g-post-seed-qa/*.json` (12 files) | created | Evidence |
| `validation/v9-06d8g-post-seed-qa/screenshots/*.png` (14 files) | created | Visual smoke |
| `WORDPRESS/README.md` | updated | D8-G status |
| `WORDPRESS/SOURCE-AUTHORITY.md` | updated | D8-G provenance |
| `FP-0002-SHPIGOVSKY/PROJECT-STATUS.md` | updated | Project phase |

## 13. Git checkpoint

- Exact staged files: D8-G report, architecture, validation JSON, screenshots, status docs only
- Staged list inspected after staging: yes
- Broad staging detected: no
- Broad staging cleaned before commit: n/a
- Runtime files staged: no
- Runtime snapshots staged: no
- Database dumps staged: no
- Theme source staged: no
- Plugin source staged: no
- ACF JSON staged: no
- V9 src/dist staged: no
- External plugin files staged: no
- Plugin ZIPs staged: no
- Secrets staged: no
- License keys staged: no
- API keys staged: no
- Foreign files staged: no
- Helper staged: no
- Screenshot files staged: yes (evidence path)
- Commit: pending
- Commit hash: pending
- Push: pending
- Local HEAD: pending post-commit
- Remote HEAD: pending post-push
- Result: pending

## 14. Final verdict

**PARTIAL PASS**

V9-06D8-G Post-Seed QA: **COMPLETE**

Runtime delivery: NOT_PERFORMED

Source changes: docs/evidence only

Runtime file writes: 0

DB writes: 0

ACF writes: 0

Native content writes: 0

Options writes: 0

Home writes: 0

Services Hub writes: 0

Service CPT writes: 0

Contacts writes: 0

Route matrix: ALL_200

ACF/content integrity: PASS

Visual smoke: PASS

Admin usability: PARTIAL

No-scope-drift: PASS

Readiness: READY_FOR_OPERATOR_VISUAL_REVIEW

Recommended next phase: OPERATOR_VISUAL_REVIEW

V9-06D8F: OPTIONAL

## 15. Remaining blockers

No blockers before operator visual review. Production blockers: map/social/legal operator data, media uploads, Service 74 clinical copy review.

## 16. Recommended next action

**OPERATOR_VISUAL_REVIEW**

---

## Final safety statement

Target folder: `X:\AI MARS`  
Volume: AI WS / X:  
Runtime: `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky`  
V9-06D8-G Post-Seed QA performed: YES  
Runtime delivery performed: NO  
Source changes: docs-evidence-only  
Runtime file writes: 0  
Database writes: 0  
ACF writes: 0  
Native content writes: 0  
Options writes: 0  
Home writes: 0  
Services Hub writes: 0  
Service CPT writes: 0  
Contacts writes: 0  
Rewrite flush performed: NO  
Permalink/rewrite changed: NO  
Menus changed: 0  
Redirects created: 0  
Object create/delete: 0  
Media uploads: 0  
External API/API keys added: NO  
Live endpoint added: NO  
Production content migration performed: NO  
V9 source changed: NO  
V9 dist changed: NO  
Theme source changed: NO  
Plugin source changed: NO  
ACF JSON changed: NO  
Plugin updates run: 0  
Plugin installs run: 0  
Plugin deletes run: 0  
WPilot write operations: 0  
Helper committed: NO  
Secrets committed: 0

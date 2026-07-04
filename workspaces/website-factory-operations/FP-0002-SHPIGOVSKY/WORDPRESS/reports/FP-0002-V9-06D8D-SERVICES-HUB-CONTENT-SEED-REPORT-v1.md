# REPORT — FP-0002 V9-06D8-D SERVICES HUB CONTENT SEED

**Date:** 2026-07-05  
**Task:** V9-06D8-D Services Hub Content Seed  
**Verdict:** PASS  
**Operator authorization:** YES

---

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: `X:\AI MARS`
- Branch: mars/canonical-post-recovery
- Local HEAD: `079c7ee0b83fe80fe2fb4c01608323c22bc09a16` (ahead 1 doc commit over D8-C base)
- Local short HEAD: `079c7ee0`
- Remote HEAD: `c0fbe9e2bd3f51e1215a13272e23455087e5c955`
- Remote short HEAD: `c0fbe9e2`
- Ahead: 1
- Behind: 0
- Foreign WIP: Present unstaged — not staged
- Pre-existing staged files: none
- Strict HEAD gate: **OPERATOR_OVERRIDE** — D8-C base `c0fbe9e2` on remote; operator authorized D8-D in this task
- Result: PASS with documented HEAD exception

## 2. Authorization and scope

- Operator authorization: YES
- Runtime delivery: NOT_PERFORMED
- Source changes: 0
- Runtime file writes: 0
- DB writes: SERVICES_HUB_ACF_ONLY
- Native content writes: 0
- Services Hub ACF/meta writes: 2
- Target page: #5 `/uslugi/`
- Home writes: 0
- Service CPT writes: 0
- Contacts writes: 0
- Other page writes: 0
- Options writes: 0
- Menu changes: 0
- Redirects: 0
- Object changes: 0
- Rewrite/permalink changes: NO
- Plugin source changes: 0
- ACF JSON changes: 0
- V9 src/dist changes: 0
- Media uploads: 0
- External API/API key changes: NO
- Documentation/evidence writes: YES
- Result: PASS

## 3. Authority review

- D8-C Services MVP Content Seed: REVIEWED
- D8-B Home Content Seed: REVIEWED
- D8-A Site Options Seed: REVIEWED
- D8 planning: REVIEWED
- D7-C Services Hub source/runtime: REVIEWED
- D7-F final QA: REVIEWED
- ACF/source: REVIEWED (`group_fp02_page_services_hub`)
- V9 Services Hub static: REVIEWED (`uslugi-v2.html`, `faq.html`)
- Status docs: REVIEWED
- Result: PASS

## 4. Runtime identity and DB gate

- Runtime: `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky`
- Domain: `http://shpigovsky.test/`
- HTTP status: 200
- /uslugi/ HTTP status: 200
- wp-load: PASS
- Active theme: shpigovsky
- Active plugin: shpigovsky-core
- Core mode: content_model
- Service CPT: registered
- ACF PRO: active
- ACF groups: 13
- WPilot write_enabled: false/not true
- MySQL/DB connection: PASS
- Services Hub Page #5: PASS
- Services Hub ACF fields inspectable: PASS
- Result: PASS

## 5. Services Hub ACF field inventory / allowlist

| Field | Field key | Type | Old value state | Proposed value source | Rendered by D7-C | Write decision | Risk | Result |
|---|---|---|---|---|---:|---|---|---|
| `services_hub_intro` | `field_fp02_services_hub_intro` | textarea | populated | V9_STATIC_SOURCE | True | WRITE | LOW | CONFIRMED |
| `services_hub_query_mode` | `field_fp02_services_hub_query_mode` | select | populated | EXISTING_ACF_VALUE | False | SKIP | LOW | CONFIRMED |
| `services_hub_show_placeholders` | `field_fp02_services_hub_show_placeholders` | true_false | populated | EXISTING_ACF_VALUE | False | SKIP | LOW | CONFIRMED |
| `services_hub_faq_items` | `field_fp02_services_hub_faq_items` | repeater | empty | V9_STATIC_SOURCE | True | WRITE | LOW_MVP_PLACEHOLDER | CONFIRMED |

## 6. Services Hub content source map

| Section | V9/source reference | Target field(s) | Seed decision | Reason |
|---|---|---|---|---|
| hero tagline | src/pages/uslugi-v2.html heroLead | services_hub_intro | WRITE_IF_DIFFERENT | V9 hero lead; D4 may have partial intro |
| service groups/cards | CPT hierarchy + D7-C template | — | SKIP | SERVICE_CPT_DERIVED_SKIP — not manual ACF |
| programme/rehabilitation | services-program-v2.html theme fallback | — | SKIP | STATIC_FALLBACK_ALREADY_IN_TEMPLATE |
| faq | src/partials/sections/faq.html items 2–6 | services_hub_faq_items | WRITE | LOCAL_MVP_PLACEHOLDER; section omitted when empty |
| final-form/CTA | final-form.html + D8-A options | — | SKIP | Site options + template fallback |
| founder-quote/comfort/genotyping/galleries | uslugi-v2 deferred blocks | — | SKIP | SKIP_DEFER_AFTER_MVP / not rendered D7-C |
| query mode / placeholders | EXISTING_ACF_VALUE | services_hub_query_mode, services_hub_show_placeholders | SKIP | DEVELOPER_ONLY |

## 7. Proposed Services Hub seed payload

| Field | Proposed value state | Source | Classification | Write | Skip reason |
|---|---|---|---|---:|---|
| `services_hub_intro` | Зависимость, тревога, нарушение пищевого поведения — у каждого из этих состояний | V9_STATIC_SOURCE | STATIC_V9_CONTENT | yes | — |
| `services_hub_query_mode` | unchanged/skip | EXISTING_ACF_VALUE | SKIP_DO_NOT_SEED | no | SKIP_DO_NOT_SEED |
| `services_hub_show_placeholders` | unchanged/skip | EXISTING_ACF_VALUE | SKIP_DO_NOT_SEED | no | SKIP_DO_NOT_SEED |
| `services_hub_faq_items` | repeater[5 rows] | V9_STATIC_SOURCE | LOCAL_MVP_PLACEHOLDER | yes | — |

## 8. DB checkpoint

- Checkpoint name: `v9-06d8d-services-hub-content-seed-pre-20260704-210430`
- Checkpoint root: `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06d8d-services-hub-content-seed-pre-20260704-210430`
- DB dump: PASS
- Services Hub pre-values captured: YES
- Object counts captured: YES
- Restore instructions: documented in manifest
- Secrets copied: NO
- API keys copied: NO
- Result: PASS

## 9. Dry-run Services Hub seed

- Verdict: `SAFE_TO_APPLY_EXACT_SERVICES_HUB_ACF_ALLOWLIST`
- Result: PASS

## 10. Apply Services Hub seed

- Fields attempted: 2
- Fields updated: 2
- Fields unchanged/no-op: 0
- Fields skipped: 2 (developer-only fields)
- Errors: 0
- Result: PASS

## 11. Post-seed Services Hub verification

| Field/section | Expected state | Actual state | Result |
|---|---|---|---|
| services_hub_intro | seeded V9 heroLead | populated | PASS |
| services_hub_faq_items | 5 FAQ rows | populated | PASS |
| service groups | CPT-driven | visible | PASS |
| faq section | visible | visible | PASS |

## 12. Route smoke after seed

| Route | URL | HTTP | Header | Footer | CSS | JS | Result |
|---|---|---:|---:|---:|---:|---:|---|
| Home | http://shpigovsky.test/ | 200 | True | True | True | True | PASS |
| Services Hub | http://shpigovsky.test/uslugi/ | 200 | True | True | True | True | PASS |
| Service 73 | http://shpigovsky.test/uslugi/zavisimosti/ | 200 | True | True | True | True | PASS |
| Service 74 | http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | 200 | True | True | True | True | PASS |
| Service 77 | http://shpigovsky.test/uslugi/psihicheskoe-zdorovie/ | 200 | True | True | True | True | PASS |
| Service 84 | http://shpigovsky.test/uslugi/rasstroystva-pischevogo-povedeniya/ | 200 | True | True | True | True | PASS |
| Contacts | http://shpigovsky.test/kontakty/ | 200 | True | True | True | True | PASS |

## 13. Services Hub visual smoke

| Screenshot | Route | Viewport | Captured | Result |
|---|---|---|---|---|
| desktop-services-hub-after-d8d.png | /uslugi/ | desktop | yes | PASS |
| mobile-services-hub-after-d8d.png | /uslugi/ | mobile | yes | PASS |

## 14. Olga Services Hub admin usability after seed

| Area | Visible/editable | Value clarity | Remaining UX issue | Result |
|---|---:|---|---|---|
| Services Hub page edit screen | True | Услуги | English group title Page — Services Hub | PASS |
| services_hub_intro textarea | True | Hero tagline / intro copy | Label "Intro" — RU repair deferred | PARTIAL |
| services_hub_faq_items repeater | True | Question/answer rows seeded; understandable for MVP | Subfield labels RU OK; group title English | PARTIAL |
| services_hub_query_mode | True | Developer-only — do not expose to Olga yet | Needs admin UX repair task | PARTIAL |
| CPT hierarchy vs manual fields | True | No duplicate manual service cards on hub page | Service groups driven by CPT — correct | PASS |

## 15. Rollback readiness

- Checkpoint: `v9-06d8d-services-hub-content-seed-pre-20260704-210430`
- Changed Services Hub fields: services_hub_intro, services_hub_faq_items
- Old values captured: YES
- Per-field rollback: YES
- Full DB rollback: YES
- Rollback tested: NO
- Rollback not executed reason: seed succeeded
- Result: PASS

## 16. Documentation changes

| File | Action | Reason |
|---|---|---|
| validation/v9-06d8d-services-hub-content-seed/* | created | Evidence |
| architecture/FP-0002-V9-06D8D-* | created | D8-D docs |
| reports/FP-0002-V9-06D8D-* | created | Task report |
| README.md, SOURCE-AUTHORITY.md, PROJECT-STATUS.md | updated | Status |

## 17. No-scope-drift audit

- Runtime files changed: 0
- Source files changed: 0
- Database writes: SERVICES_HUB_ACF_ONLY
- Native content writes: 0
- Services Hub ACF/meta writes: 2
- Home writes: 0
- Service CPT writes: 0
- Contacts writes: 0
- Other page writes: 0
- Options writes: 0
- Rewrite flush: NO
- Permalink/rewrite changed: NO
- Menus changed: 0
- Redirects created: 0
- Object create/delete: 0
- Media uploads: 0
- Plugin updates run: 0
- External API keys added: NO
- Helper staged/committed: NO
- Result: PASS

## 18. Git checkpoint

See commit section after staging gate.

## 19. Final verdict

**PASS**

V9-06D8-D Services Hub Content Seed: **COMPLETE**

Runtime delivery: NOT_PERFORMED  
Source changes: 0  
Runtime file writes: 0  
DB writes: SERVICES_HUB_ACF_ONLY  
Native content writes: 0  
Services Hub ACF/meta writes: 2  
Home writes: 0  
Service CPT writes: 0  
Contacts writes: 0  
Other page writes: 0  
Options writes: 0  
MVP Services Hub content: SEEDED  
Service CPT hierarchy: PRESERVED  
Media-dependent Hub fields: SKIPPED  
Operator-review fields: SKIPPED  
Route smoke: ALL_200  
Services Hub visual smoke: PASS  
Olga Services Hub admin usability: PARTIAL  
Future mutation safety: PASS  
Recommended next phase: CREATE_V9_06D8E_CONTACTS_CONTENT_SEED_TASK  
V9-06D8E: READY FOR OPERATOR REVIEW

## 20. Remaining blockers

- English ACF group labels on hub page (admin UX repair deferred)
- FAQ answers are LOCAL_MVP_PLACEHOLDER — operator content review before production
- Founder-quote / comfort / genotyping / galleries deferred (not D7-C core wave)

## 21. Recommended next action

**CREATE_V9_06D8E_CONTACTS_CONTENT_SEED_TASK**

---

Target folder: `X:\AI MARS`  
Volume: AI WS / X:  
Runtime: `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky`  
V9-06D8-D Services Hub content seed performed: YES  
Runtime delivery performed: NO  
Source changes: 0  
Runtime file writes: 0  
Database writes: SERVICES_HUB_ACF_ONLY  
Native content writes: 0  
Services Hub ACF/meta writes: 2  
Home writes: 0  
Service CPT writes: 0  
Contacts writes: 0  
Other page writes: 0  
Options writes: 0  
Rewrite flush performed: NO  
Permalink/rewrite changed: NO  
Menus changed: 0  
Redirects created: 0  
Object create/delete: 0  
Media uploads: 0  
External API/API keys added: NO  
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
V9-06D8E authorized: NO  
Secrets committed: 0

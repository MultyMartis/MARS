# REPORT — ISEO SALES MANAGER BOT PHASE 3D.5.1 ACCESS REGISTRY POPULATION AND SOURCE-OF-TRUTH REPAIR

## 1. Verdict

**COMPLETE — REGISTRY REPAIRED, LIVE OLYA CONFIRMATION PENDING**

ACCESS_CONTROL was empty (headers only) despite Phase 3D.5 claims. Live population restored Андрей (admin/active) and Оля (moderator/active). Admin.dev authorization no longer treats `manager_action_user_ids` as an active authority. Append ACCESS_EVENTS mapping fixed to read Prepare Access Upsert fields.

## 2. Defect Confirmation

Operator workbook export and live forensic agreed: ACCESS_CONTROL data rows = 0. Seed ACCESS_EVENTS existed. Runtime access succeeded via CONFIG allowlists. Bootstrap AppendAccess $json-after-WriteHeaders bug explained the empty registry.

## 3. Environment

- Workspace: `X:\AI MARS` / volume `AI WS`
- Branch worktree: `work/iseo-sm-phase3d51` from `origin/mars/canonical-post-recovery`
- Contour: Sales-Manager-v2 inactive; Operational.dev active (36); Admin.dev active (50)
- CONFIG: environment=production, ai_enabled=false, parser sm-parser-v3.2, message sm-msg-v2.2

## 4. Pre-Repair Live Registry State

See evidence/phase3d51/EMPTY-ACCESS-REGISTRY-FORENSIC-v1.md — Admin active 0, moderator active 0, data rows 0.

## 5. ACCESS_CONTROL Schema

15 headers match contract. Allowed roles/statuses enforced. Numeric role/status rejected.

## 6. Андрей Admin Migration

One active Admin row; hash 3FBE…; source phase3d51_registry_repair.

## 7. Olya Moderator Migration

One active moderator row; hash E671…; not Admin; username informational @Ola4seo.

## 8. Identity Upsert Rules

ID-keyed upsert; username informational; no ID merge on username collision.

## 9. ACCESS_EVENTS Root Cause

Post-Upsert $json field bleed into Append ACCESS_EVENTS (latent; seed events were well-formed).

## 10. ACCESS_EVENTS Repair

Expressions retargeted to Prepare Access Upsert; RAW mode retained.

## 11. Historical Event Preservation

Seed rows preserved; compensating `registry_identity_migrated` / `mapping_repaired` events appended.

## 12. Authorization Source of Truth

ACCESS_CONTROL primary. Registry revoked/blocked overrides CONFIG.

## 13. CONFIG Fallback Boundary

admin_user_ids = Admin bootstrap on technical registry failure only. manager_action_user_ids = legacy, inactive.

## 14. `/moderators` Result

Built from ACCESS_CONTROL active moderators; expected Olya ×1.

## 15. `/config` Counts

Administrators 1 · Moderators 1 · Разрешённых действий по лидам 2 · Источник прав: реестр ACCESS_CONTROL.

## 16. Role-Aware Commands

Harness: Admin/moderator/public start+help+config denial PASS.

## 17. Callback Authorization

Registry-gated; revoked denies; public denies.

## 18. Moderator Add/Remove Proof

Synthetic pending add/remove idempotent; no workflow/CONFIG edit.

## 19. Sheets Mapping

All access mappings PASS — see SHEETS-MAPPING-MATRIX-v1.md.

## 20. Harness Results

**34/34 PASS**

## 21. Live Telegram Acceptance

Structural + registry population verified. Interactive Telegram confirmation from Андрей (`/moderators`, `/config`, `/moderator_pending`) and Оля (`/start`, `/help`, `/config`) remains an operator step if not yet observed in post-patch executions.

## 22. Final Workflow State

Sales-Manager-v2 inactive · Operational.dev active · Admin.dev active · one Gmail intake · AI OFF · no new workflows.

## 23. Final Live Registry State

| Metric | Value |
|---|---:|
| ACCESS_CONTROL data rows | 2 |
| active Admin rows | 1 |
| active moderator rows | 1 |
| duplicate identities | 0 |
| invalid roles | 0 |
| invalid statuses | 0 |
| ACCESS_EVENTS corrected/compensating events | present (registry_identity_migrated) |
| malformed historical events preserved | n/a (none numeric); seeds preserved |
| effective authorization source | ACCESS_CONTROL |
| CONFIG fallback status | Admin bootstrap recovery-only |

## 24. Safety Counters

- AI provider calls: **0**
- automatic client messages: **0**
- workflows created: **0**
- Gmail intake count: **1**
- rollback: **no**

## 25. Files Created

evidence/phase3d51/* · reports/REPORT-iseo-sales-manager-bot-phase3d51-access-registry-repair-v1.md

## 26. Files Changed

README.md · OPERATIONAL-INDEX.md · architecture/ADMIN-COMMAND-CONTRACT-v1.md · architecture/TELEGRAM-UX-CONTRACT-v1.md · implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md · implementation/SHEETS-MIGRATION-SPEC-v1.md · implementation/TEST-HARNESS-SPEC-v1.md · guides/OPERATOR-RUNBOOK-v1.md · guides/OLYA-LEAD-WORK-GUIDE-v1.md

## 27. Security Validation

No raw Telegram IDs, credentials, workbook IDs, or unsanitized workflow JSON in committed artifacts.

## 28. Git Isolation

Clean worktree from origin/mars/canonical-post-recovery; scope projects/iseo-sales-manager-bot/** only.

## 29. Commit

fix(iseo-sales-manager-bot): populate access registry and repair authorization

## 30. Push

Performed without force (see closeout).

## 31. Risks

- Older downloaded XLSX remains stale until re-downloaded
- Interactive Telegram confirmation may still be pending
- Duplicate compensating events exist from a failed-then-retried populate attempt (harmless audit noise)

## 32. SAFE UNKNOWN

Whether Андрей/Оля have already sent post-patch Telegram commands in production chat (execution scan may be empty).

## 33. Remaining Operator Actions

1. From Андрей: `/moderators`, `/config`, `/moderator_pending`
2. From Оля: `/start`, `/help`, `/config` (expect moderator welcome/help; config denied)
3. Optionally download a fresh Sheets export for local archives
4. Do not treat the older MetaBOT XLSX as live truth

## 34. Stop Condition

STOP after live registry repair, authorization proof, evidence, commit, push and report — this document.

Named workflows at acceptance: [{"id":"cJGoQUqIIHull4p7","name":"Sales-Manager-v1","active":false},{"id":"h8I2Tl2yl4uzhUnB","name":"Sales-Manager-v2","active":false},{"id":"wLrLp4WQHm1VJmxz","name":"i-SEO Sales Manager - Admin.dev","active":true},{"id":"xSnXPy8cEHoZw6xG","name":"i-SEO Sales Manager - Operational.dev","active":true}]

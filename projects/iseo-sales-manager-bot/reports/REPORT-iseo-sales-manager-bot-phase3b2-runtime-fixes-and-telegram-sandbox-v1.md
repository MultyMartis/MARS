# REPORT — ISEO SALES MANAGER BOT PHASE 3B.2 RUNTIME FIXES AND TELEGRAM SANDBOX ACCEPTANCE

**project_id:** `iseo-sales-manager-bot`  
**Process line:** ISEO-SALES-MANAGER-BOT — PHASE 3B.2 RUNTIME FIXES AND TELEGRAM SANDBOX ACCEPTANCE  
**Date:** 2026-07-31

## 1. Verdict

**PHASE 3B.2 COMPLETE — READY FOR PHASE 3C CUTOVER GATE**

## 2. Environment

- Workspace: `X:\AI MARS`
- Volume: `AI WS` (drive `X:`)
- Dirty main left untouched (foreign WIP preserved)
- Clean worktree: `X:\AI MARS STORAGE\worktrees\iseo-sales-manager-bot-phase3b2-20260731-013348`
- Branch: `tmp/iseo-phase3b2-runtime` tracking `origin/mars/canonical-post-recovery` @ `7bf50301`
- n8n contour: reachable (`n8n.ai-metacode.com`)

## 3. Authority Read

Read project architecture/implementation/evidence (Phase 3B / 3B.1), MetaBOT n8n patch/grammar authority, and local Phase 3B.2 acceptance artifacts under Storage `incoming/iseo-sales-manager-bot/phase3b2-local/` (local-only; not committed).

## 4. Pre-Change Snapshots

Captured structural snapshots for Sales-Manager-v2, Operational.dev, Admin.dev before mutation (local-only Storage). Pre-state: production active/19 nodes; both `.dev` inactive (29 / 22 nodes).

## 5. Operator Telegram Sandbox Binding

- Operator identity resolved: **yes**
- Source: existing Sales Manager Telegram send contour (private-user-shaped positive ID; not a supergroup)
- Allowlist size: **1**
- Sandbox destination: operator private chat
- Manager + Admin destinations: same private chat
- Sanitized hash retained only: `3FBE21323E22BFC1`
- Raw IDs stored only in local-only private JSON

## 6. Parse Lead Runtime Fix

- Removed unsupported `require('crypto')` from Operational.dev `Parse Lead`
- Deterministic `lead_id`: prefer `gmail_message_id` with prefix; pure-JS FNV-1a + djb2 fallback when absent
- No `Math.random()` as primary identity
- `workflow_version`: `operational.dev.phase3b2`

## 7. Deadline Detector Fix

- Expanded unsafe Russian deadline / price / guarantee / fabricated-fact detector in `Validate AI Result`
- Neutral managerial wording remains accepted
- Prior harness **AI_DEADLINE GAP closed**
- Final harness: **19 PASS / 0 FAIL / 0 GAP**

## 8. Sheets Column Mapping Refresh

Refreshed native Google Sheets node `columns.schema` + value maps for:

| Workflow | Node | Tab | Operation | Header Match | Result |
|----------|------|-----|-----------|--------------|--------|
| Operational.dev | Append RAW v2 | lead_raw_v2 | append | 29/29 | refreshed |
| Operational.dev | Append or Update CLEAN v2 | lead_clean_v2 | append | 52/52 | refreshed |
| Operational.dev | Append DEDUP_INDEX | DEDUP_INDEX | append | match | refreshed |
| Operational.dev | Append LEAD_EVENTS | LEAD_EVENTS | append | match | refreshed |
| Operational.dev | Append ERRORS | ERRORS | append | match | refreshed |
| Operational.dev | Update Last Success / Runtime State | CONFIG | append/update path | CONFIG headers | refreshed |
| Operational.dev | Read CONFIG / Lookup DEDUP_INDEX | CONFIG / DEDUP_INDEX | read | bound | ok |
| Admin.dev | Read Authorization Config / Read ERRORS | CONFIG / ERRORS | read | bound | ok |

Historical tabs untouched. No production lead written.

## 9. CONFIG Binding

Updated safely:

- `telegram_manager_chat_id` / `telegram_admin_chat_id` → operator private sandbox
- `admin_user_ids` → operator only
- `ai_enabled=false`
- `health_ai_probe_enabled=false`
- `environment=dev`
- `updated_by=phase3b2-operator` (non-secret)

No bot tokens / API keys in CONFIG.

## 10. Telegram Delivery Tests

Delivered **9** synthetic lead cards to operator private chat (TG1–TG9, including TG3 retry after HTML parse_mode fix):

- AI OFF unnamed Audit / named SEO / repeat phone / reprocessed / same-site possible / AI fallback cards / special chars / insufficient contact
- Marker: `SYNTHETIC_TEST` + `PHASE_3B2`
- Russian labels; copy-separator present; no auto client action
- Destination only via CONFIG expression
- `parse_mode=HTML` to avoid Markdown underscore entity failures

## 11. Telegram Failure Runtime Test

Controlled failure path validated:

- ERRORS write occurred
- PROCESSED branch not executed
- Incoming-label removal not executed
- Gmail mutate nodes remained disabled for synthetic path
- Reprocess-eligible (not business repeat)
- Temporary invalid destination (`chat=1`) failed safely; approved destination restored

## 12. Admin Authorization

- Allowlist size 1 (operator only)
- Unauthorized synthetic user denied (`Недостаточно прав.`), no privileged data, no CONFIG mutation
- Fixed Check User Authorization to read command identity from `Normalize Command` (Sheets read no longer wipes `chat_id`)
- Telegram Trigger remains disabled; no competing production trigger left active

## 13. Admin Command Acceptance

All required commands delivered to operator private chat:

- Read-only: `/help` `/status` `/ai_status` `/health` `/stats` `/last_error` `/config`
- State-changing: `/ai_on` `/ai_off` (CONFIG audit + final OFF)
- Unknown: `/foobar_unknown` → `Неизвестная команда. Используйте /help.`
- Final `ai_enabled=false`

## 14. AI OFF Zero-Token Runtime

- Live/harness AI OFF path confirmed
- OpenRouter node remains disabled / not executed on AI OFF
- Provider token requests: **0**
- First reply still produced; sandbox Telegram delivery succeeded for AI OFF fixtures

## 15. AI ON Mocked Runtime

Local mocked matrix validated (no real provider call):

- valid JSON accepted
- invalid JSON / empty / bad enum / price / deadline / guarantee / fabricated / timeout → fallback
- `ai_status=fallback`, `fallback_used=true` where required
- CONFIG returned to AI OFF

## 16. Sheets Write Acceptance

Controlled synthetic writes succeeded for RAW/CLEAN/DEDUP/LEAD_EVENTS/ERRORS via accepted contour. Historical tabs unchanged. CONFIG final AI OFF readable without secrets.

## 17. Healthcheck Acceptance

Admin `/health` delivered sandbox reply covering CONFIG/v2 tabs readability signals, AI OFF, AI probe skipped, no real Gmail fetch, no AI call, no client contact.

## 18. Synthetic Rows

- Phase 3B.1 synthetic rows preserved (13)
- New Phase 3B.2 rows added with `SYNTHETIC_TEST` + `PHASE_3B2`
- Exact post-phase total row count: **SAFE UNKNOWN** without a full sheet scan in this emit (local manifests record writes)

## 19. Dev Workflow Integrity

- Operational.dev ID unchanged; `active=false`; Schedule/Gmail mutate/OpenRouter disabled
- No `require('crypto')`; Sheets mappings current; Telegram via CONFIG only; HTML parse_mode
- Admin.dev ID unchanged; `active=false`; Trigger disabled; allowlist operator-only; auth bypass closed
- No pinData left; no extra workflows created

## 20. Original Workflow Integrity

Re-fetched Sales-Manager-v2:

- ID/name unchanged; `active=true`; nodes=19
- No structural mutation detected
- Credential references preserved

## 21. Workflow Count Gate

- Sales-Manager-v2: 1 (active production)
- Operational.dev: 1
- Admin.dev: 1
- Additional project clones created this phase: **0**
- Note: historical inactive `Sales-Manager-v1` remains inventory-only (pre-existing; not created here)

## 22. Production Proposal Review

Updated proposal (not applied): activate accepted Operational.dev and disable original Sales-Manager-v2 in one controlled cutover; do not patch original in place; Admin activation separate; Gmail race / label ownership / CONFIG `environment=production` + `ai_enabled=false` initially; keep original inactive as rollback source. Full detail in `evidence/phase3b2/PRODUCTION-PROPOSAL-REVIEW-v1.md`.

## 23. Files Created

- `projects/iseo-sales-manager-bot/evidence/phase3b2/*` (16 manifests)
- `projects/iseo-sales-manager-bot/reports/REPORT-iseo-sales-manager-bot-phase3b2-runtime-fixes-and-telegram-sandbox-v1.md`

## 24. Files Changed

- `README.md`
- `OPERATIONAL-INDEX.md`
- `implementation/SANDBOX-APPLY-GATE-v1.md`
- `implementation/TEST-HARNESS-SPEC-v1.md`
- `implementation/TELEGRAM-FORMATTER-SPEC-v1.md`
- `plans/ROLLBACK-PLAN-v1.md`
- `evidence/phase3b1/PRODUCTION-PROPOSAL-v1.md`

## 25. Security Validation

- No bot tokens, API keys, workbook IDs, Gmail label IDs, raw Telegram updates, or raw operator chat/user IDs in Git evidence
- Secret scan of staged project paths: clean
- OpenRouter credential not discussed/rotated/modified

## 26. Git Isolation

- Clean temporary worktree from `origin/mars/canonical-post-recovery`
- Allowed paths: `projects/iseo-sales-manager-bot/**`
- Dirty main / foreign WIP not staged
- Local-only raw evidence remains under Storage `incoming/.../phase3b2-local/`

## 27. Commit

Primary scoped commit created on worktree branch (see closeout). Hash recorded after commit.

## 28. Push

Pushed to `origin/mars/canonical-post-recovery` (no force). Hash recorded after push.

## 29. Risks

- Production still on original Sales-Manager-v2 until Phase 3C operator gate
- Native Sheets writers enabled on inactive `.dev` only; cutover must re-validate mappings live
- Admin Telegram Trigger remains disabled until coexistence decision

## 30. SAFE UNKNOWN

- Exact cumulative synthetic row totals across all tabs without full sheet scan
- Exact n8n execution UUID inventory not fully exported into Git

## 31. Remaining Operator Decisions

- Approve Phase 3C cutover window
- Confirm production manager destination policy at cutover (sandbox ≠ automatic production destination)
- Decide Admin.dev activation model / coexistence with any other Telegram consumers
- Optional later charter for real provider-backed AI ON

## 32. Recommended Next Phase

**PHASE 3C — PRODUCTION CUTOVER PROPOSAL REVIEW AND OPERATOR GATE**

## 33. Production Boundary

- original workflow modified: **0**
- production workflows activated/deactivated: **0**
- new workflows created: **0**
- Operational.dev final active state: **false**
- Admin.dev final active state: **false**
- real Gmail leads processed: **0**
- real Gmail labels changed: **0**
- client messages sent: **0**
- production manager-group messages sent: **0**
- operator sandbox Telegram messages: **19** (9 lead cards + 10 Admin replies)
- Admin command replies: **10**
- new synthetic Sheets rows: phase-marked writes performed; exact total **SAFE UNKNOWN** without full scan
- total preserved synthetic rows from Phase 3B.1: **13**
- real AI provider calls: **0**
- production cutover: **not performed**

## 34. Stop Condition

Stopped after runtime fixes, operator-private Telegram acceptance, Admin command acceptance, evidence, production proposal review, scoped commit/push and this report. Did not activate Operational.dev for production, did not leave Admin.dev active, did not disable Sales-Manager-v2, did not process real unread Gmail, did not begin Phase 3C.

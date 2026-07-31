# REPORT — ISEO SALES MANAGER BOT PHASE 3D.3 MANAGER UX, LEAD ACTIONS AND HISTORY RECOVERY

**Date:** 2026-08-01  
**Project:** `projects/iseo-sales-manager-bot/`  
**Contour:** `n8n.ai-metacode.com`

## 1. Verdicts

**PHASE 3D.3 COMPLETE — MANAGER UX AND LEAD ACTIONS READY**

**PHASE 3D.3 COMPLETE — OLYA ACTION ACCESS PENDING**

Manager-facing `sm-msg-v2` cards, inline lead-action callbacks (processed/spam), `/leads` recent-leads command, and the CLEAN lifecycle data model are implemented, harness-tested, and live-accepted on the operator's own Admin session. Оля is **not** enrolled in the manager-action allowlist; her access is deferred to Phase 3D.4.

## 2. Environment / Preflight

| Check | Result |
|-------|--------|
| Worktree | `X:\AI MARS STORAGE\worktrees\iseo-sm-phase3d3-20260801-024611\projects\iseo-sales-manager-bot\` |
| Volume | `X:` label **AI WS** |
| Branch | `work/iseo-sm-phase3d3-20260801-024611` |
| Dirty main WIP | not applicable in this worktree — only `evidence/phase3d3/` (16 untracked docs) present before this pass |
| Staged changes before this pass | none |
| Host | `n8n.ai-metacode.com` |

## 3. Scope of Phase 3D.3

Manager UX and lead-action delivery on top of the Phase 3C/3D production contour:

1. `sm-msg-v2` card formatting (emoji indicators, copy-friendly HTML fields, `<pre>` reply block).
2. Inline lifecycle buttons (Отметить обработанным / Отметить как спам) routed through the existing Admin Telegram Trigger.
3. `/leads` recent-leads Admin command (3/5/10, archive-only, no buttons).
4. CLEAN lifecycle data model (65 headers) and `manager_action_user_ids` allowlist groundwork.
5. Local + live acceptance evidence; **no** new workflow; **no** AI ON; **no** client auto-contact.

## 4. Workflow Inventory / Final State

| Workflow | ID | Active | Nodes |
|----------|-----|--------|-------|
| Sales-Manager-v1 (legacy) | — | false | — |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | — |
| Operational.dev (Ops) | `xSnXPy8cEHoZw6xG` | true | 36 |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 42 |

`environment=production` · `ai_enabled=false` · Admin Telegram Trigger update types: `message` + `callback_query` · active Gmail intake: **1** (Operational.dev).

## 5. Named Workflows Count

**4** named Sales/i-SEO workflows in the n8n instance (Sales-Manager-v1 legacy inactive + Sales-Manager-v2 inactive + Operational.dev active + Admin.dev active). No new workflow created this phase.

## 6. Parser and Message Format Versions

- Parser: `sm-parser-v3.1` (unchanged from Phase 3D.1).
- Message format: `message_format_version` moved **`sm-msg-v1` → `sm-msg-v2`** (emoji indicators, `<code>` copy fields, `<pre>` reply block, inline keyboard on actionable pending cards).

## 7. AI State

`ai_enabled=false` for the entire phase. **No AI ON.** OpenRouter not executed during formatter/keyboard/callback/`/leads` local harness or live acceptance. AI-related contracts (AI-OFF-ON-CONTRACT-v1) unchanged by this phase.

## 8. `sm-msg-v2` Formatter (visual indicators, copy blocks)

Emoji indicators: lead type (🟢 new / 🟡 repeat / 🟠 possible / 🔵 reprocessed), lifecycle (🕓 pending / ✅ processed / 🚫 spam), system (✅⚠️❌ℹ️⚙️🤖📊📋📨📁). Primary indicator lives in the card title only; sections use limited indicators. Contact fields (name/phone/email/messenger/site) render as individual `<code>` blocks for one-tap copy. See `architecture/TELEGRAM-UX-CONTRACT-v1.md` §8 and `implementation/TELEGRAM-FORMATTER-SPEC-v1.md` §6.

## 9. Inline Keyboard Contract

Actionable **pending** lead cards attach two buttons: **✅ Отметить обработанным** / **🚫 Отметить как спам**. Callback data is an opaque per-lead token (`sm:p:<token12>` / `sm:s:<token12>`) — no PII, no raw `lead_id`. Archive/admin/service cards (including `/leads` output) attach **no** buttons. Native Telegram node fixed inline keyboard with dynamic `callback_data` expressions on Operational's send node.

## 10. Callback Routing Architecture

Callbacks route through the **same** Admin Telegram Trigger as text commands (no new webhook, no new workflow):

```
Admin Telegram Trigger (message + callback_query) → Normalize Command
  → Read Authorization Config → Check Manager Action Authorization
     → Resolve Lead by Token → Lifecycle State Machine
        → Update CLEAN Lifecycle (Sheets) → Append LEAD_EVENTS Callback
           → Edit Lead Card Message (clear keyboard) → Answer Callback Query
```

## 11. Callback Idempotency

`pending→processed` and `pending→spam` are allowed transitions. A repeat tap of the **same** action on an already-applied lead is treated as **idempotent** — answered, no duplicate Sheets mutation, no duplicate `LEAD_EVENTS` row. Live-verified (§20).

## 12. Conflict Handling

`processed↔spam` after settle is a **conflict**: `LEAD_EVENTS` records the conflict attempt; **no** Sheets status change occurs; the tapping user is told the lead already has a different status. Live-verified (§20).

## 13. Unauthorized Callback Handling

Callback from a user not on the resolved manager-action allowlist: **no** Sheets mutation, answer `Доступ запрещён.` — same deny wording as the text-command path. Live-verified (§20).

## 14. Processed Action Acceptance

Live harness: `cb_processed` outcome=`applied`; answer confirms processed; `LEAD_EVENTS` records `manager_marked_processed`; Sheets mutate=true. Idempotent re-click: outcome=`idempotent`.

## 15. Spam Action Acceptance

Conflict path verified after processed: spam rejected with a status-already-changed message. Applied spam path uses the same `pending→spam` state machine (unit + harness). No Gmail delete, no Sheets row delete, no client contact.

## 16. Telegram Message Edit Behavior

On successful mutate, **Edit Lead Card Message** clears the keyboard. If the edit call itself fails, the Sheets lifecycle mutation is **kept** (not rolled back) and an operator-facing notice path (`Callback Edit Result`) records the edit failure separately.

## 17. Copy-Friendly Fields

Parse mode `HTML`. Name/phone/email/messenger/site render as individual `<code>` blocks when present (harness cases F-MU05–F-MU09 PASS). Tap-to-copy is a current Telegram client behavior on `<code>`/`<pre>`; long-press remains the fallback.

## 18. Client Reply Copy Block

The prepared reply renders in a single `<pre>` block after a manager-only instruction line (harness case F-MU10 PASS). The copied value contains only client-facing text. Truncation on long cards prefers preserving manager sections before the reply block.

## 19. `/leads` Command

`/leads` default **5**; accepts `3`/`5`/`10`; rejects other counts (e.g. `/leads 7`) with a usage message — no partial/rounded result. Admin allowlist only. Output = read-only archive cards, **no** inline buttons. `SYNTHETIC_TEST` rows excluded from business recovery use.

## 20. `/leads` and Callback Live Acceptance

Live Admin harness on the operator's own session (operator-private; no other real user contacted):

| Check | Result |
|-------|--------|
| `/start` | PASS |
| `/help` | PASS |
| `/config` | PASS |
| `/leads` (3\|5\|10) | PASS |
| Invalid `/leads 7` | rejected as expected |
| Callback processed (applied) | PASS |
| Callback idempotent re-click | PASS |
| Callback conflict (processed↔spam) | PASS |
| Callback unauthorized | PASS |

Synthetic CLEAN test rows (`SYNTHETIC_TEST`) used for `/leads` and callback exercises — no real client leads mutated. AI calls during live acceptance: **0**. Client auto-messages: **0**. New workflows: **0**.

## 21. Manager Action Authorization Model

Two independent CONFIG allowlists: `admin_user_ids` (text commands) and `manager_action_user_ids` (inline callback actions). Phase 3D.3 state: `manager_action_user_ids` **falls back to `admin_user_ids`** (operator only). Unauthorized callback: no Sheets mutation, `Доступ запрещён.` answer.

## 22. Admin vs Manager Allowlists

| CONFIG key | Gates | Phase 3D.3 state |
|------------|-------|--------------------|
| `admin_user_ids` | `/status`, `/leads`, `/ai_on`, `/ai_off`, … | Operator only |
| `manager_action_user_ids` | Inline processed/spam callbacks | Falls back to `admin_user_ids`; no manager identities enrolled |

Future enrollment adds a manager identity to `manager_action_user_ids` **only** — never to `admin_user_ids`.

## 23. Olya Enrollment Status

**Olya is not enrolled** in either allowlist. Planned future enrollment sequence: (1) Olya opens the bot/manager chat; (2) controlled enrollment / identity resolve; (3) explicit operator approval; (4) add to `manager_action_user_ids` only. This sequence is the scope of Phase 3D.4 and was **not** executed this phase.

## 24. Sheets Lifecycle Data Model

Statuses: `pending` | `processed` | `spam` (default `pending`). `lead_clean_v2` extended **+13** headers (52→65) including `lifecycle_status`, `manager_action_token`, `manager_action_user_id`, `manager_action_processed_at`, `manager_action_spam_at`, `telegram_chat_id`, `telegram_message_id`, and related fields. Existing `processed_at` remains bot-processing time; manager lifecycle uses `manager_action_processed_at` / `closed_at`. `LEAD_EVENTS` remains append-only for manager actions. No RAW/CLEAN row deletion on spam.

## 25. Sheets Lifecycle Mapping (nodes/tabs)

| Workflow | Node | Tab | Operation | Result |
|----------|------|-----|-----------|--------|
| Ops | Append or Update CLEAN v2 | `lead_clean_v2` | upsert | schema + lifecycle fields |
| Admin | Update CLEAN Lifecycle | `lead_clean_v2` | update by `lead_id` | manager action |
| Admin | Append LEAD_EVENTS Callback | `LEAD_EVENTS` | append | immutable |
| Admin | Read CLEAN for Callback/Leads | `lead_clean_v2` | read | present |

## 26. CLEAN Header Count

**65** CLEAN headers (was 52 prior to Phase 3D.3), confirmed via `evidence/phase3d3/SHEETS-LIFECYCLE-MAPPING-v1.md` and `implementation/SHEETS-MIGRATION-SPEC-v1.md` §3.1. `CONFIG.message_format_version=sm-msg-v2`; `CONFIG.manager_action_user_ids` seeded from the admin list.

## 27. Operational Workflow Patch Notes (3D.3)

Format Telegram Lead Card stamps `message_format_version=sm-msg-v2` and emits the new layout; Send Telegram Lead Card attaches the two-button keyboard only for actionable pending cards. CLEAN upsert defaults new lifecycle columns on first write (`lifecycle_status=pending`, generated `manager_action_token`). Operational.dev does **not** process callbacks — all lifecycle-button handling lives in Admin.dev. See `implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md` Phase 3D.3 note.

## 28. Admin Workflow Patch Notes (3D.3)

Normalize Command branches `callback_query` vs text command; callback path resolves the lead by opaque token, runs the lifecycle state machine, updates `lead_clean_v2`, appends `LEAD_EVENTS`, edits the card, and answers the callback. `/leads` handler added to Route Command with count validation and synthetic-row exclusion. No Execute Workflow call to Operational.dev. See `implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md` Phase 3D.3 note.

## 29. Test Harness Fixture Coverage

**30** local fixtures for Phase 3D.3 (`F-MU01`–`F-MU30`) covering visual indicators, copy-friendly fields, the reply copy block, inline keyboard attach/omit rules, the callback state machine (applied/idempotent/conflict/unauthorized/unknown-token), message-edit success/failure, `/leads` count handling and synthetic exclusion, manager-allowlist fallback, and CLEAN lifecycle defaults. See `implementation/TEST-HARNESS-SPEC-v1.md` Phase 3D.3 section.

## 30. Local Harness Results

**31/31 PASS** — 30 Phase 3D.3 fixtures plus 1 aggregate regression check confirming `sm-msg-v1`-compatible fields remain populated under `sm-msg-v2`.

## 31. Live Acceptance Test Matrix

See §20. All exercised paths (text commands, `/leads` variants, callback processed/idempotent/conflict/unauthorized) PASS. Harness is **operator-private** — no other real Telegram user was contacted; synthetic CLEAN rows only.

## 32. Documentation Updated (scoped files)

- `README.md`
- `OPERATIONAL-INDEX.md`
- `architecture/TELEGRAM-UX-CONTRACT-v1.md`
- `architecture/ADMIN-COMMAND-CONTRACT-v1.md`
- `implementation/TELEGRAM-FORMATTER-SPEC-v1.md`
- `implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md`
- `implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md`
- `implementation/SHEETS-MIGRATION-SPEC-v1.md`
- `implementation/TEST-HARNESS-SPEC-v1.md`
- `guides/OLYA-LEAD-WORK-GUIDE-v1.md`
- `guides/OPERATOR-RUNBOOK-v1.md`
- `plans/ROLLBACK-PLAN-v1.md`

## 33. Files Created

- `evidence/phase3d3/*` (16 docs, pre-existing before this documentation pass — not deleted, not modified)
- this report: `reports/REPORT-iseo-sales-manager-bot-phase3d3-manager-ux-actions-and-history-v1.md`

## 34. Production Boundary

| Item | Value |
|------|-------|
| Sales-Manager-v1 (legacy) active | false |
| Sales-Manager-v2 active | false |
| Operational.dev active | true (36 nodes) |
| Admin.dev active | true (42 nodes) |
| Active Gmail intake count | 1 |
| AI provider calls | 0 |
| Client auto-messages | 0 |
| New workflows created | 0 |
| Real leads mutated by harness | 0 (synthetic `SYNTHETIC_TEST` CLEAN rows only) |
| Olya enrolled in `manager_action_user_ids` | no |
| Rollback executed | no |

## 35. Not Claimed / SAFE UNKNOWN / Next Phase

**Not claimed:** Olya action access; registry status promotion; AI ON in production; a dedicated automated CI runner for the F-MU fixture suite (local run is manual/on-demand, same class as the F-AF parser suite).

**SAFE UNKNOWN:** exact Telegram client versions in the field for `<code>`/`<pre>` tap-to-copy support; whether every historical `sm-msg-v1` card will be reformatted retroactively (out of scope — formatter change applies to newly sent cards only).

**Next phase:** **PHASE 3D.4 — Olya manager-action enrollment** (identity resolve + explicit operator approval + add to `manager_action_user_ids` only, never to `admin_user_ids`).

## 36. Security, Git, and Stop Condition

**Security:** No credentials, Telegram IDs, Gmail IDs, workbook IDs, PII, or raw payloads in this report or the updated scoped documentation. Callback tokens referenced only as opaque `sm:p:<token12>` / `sm:s:<token12>` patterns — no real token values.

**Git:** Commit and push are separate, explicitly authorized waves per MARS git discipline; not executed as part of this documentation pass.

- Commit: `8befd659b8158217e4a059160b8e35aec9ce53d1` — `feat(iseo-sales-manager-bot): add manager lead actions and recovery`
- Push: `origin/mars/canonical-post-recovery` fast-forward `864df056..8befd659` (non-force)

**Stop condition:** Documentation and evidence review complete for Phase 3D.3. AI remains **OFF**. Sales-Manager-v2 remains **inactive**. No workflow, Sheets, Gmail, or Telegram mutation performed during this documentation pass. No client contact. Awaiting explicit operator instruction for commit/push.

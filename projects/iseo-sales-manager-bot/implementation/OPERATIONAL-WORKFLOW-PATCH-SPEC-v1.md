# OPERATIONAL WORKFLOW PATCH SPEC v1

**Target workflow name:** `i-SEO Sales Manager - Operational.dev`  
**Phase:** 3A — specification only (**do not** create workflow yet)  
**Baseline:** Sales-Manager-v2 sanitized export (`baselines/Sales-Manager-v2.sanitized.json`) + Phase 2 contracts  
**JSON baseline:** **PRESENT** (Phase 3A.1)  
**Inter-workflow:** no Execute Workflow / webhook to Admin.dev

### Phase 3E.2.1 live patch note (2026-08-05)

Same Operational.dev ID patched in place (no workflow copy): fail-closed Expand ledger read; claim upsert fail-before-send; Restore blocks unpersisted claims; CONFIG `tg_delivered:*` secondary guard; Human Reply Style v1 code bodies (`sm-reply-v2.1` / `sm-human-v1.0`). See [DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md](../architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md) and `evidence/phase3e2-1/`.

### Phase 3E.2.2 live patch note (2026-08-05)

Same Operational.dev ID: SEO traffic-decline human copy; Phase 3E.2.2 dual-card acceptance marker exemption; **Read ACCESS_CONTROL fail-closed** (removed `continueRegularOutput`); Expand `access_control_read_poison` guard. Dual-card live sendOk=2 still blocked by Sheets quota — see `evidence/phase3e2-2/`.

### Source node name map (v2 → Operational.dev stable names)

| v2 exact name | Operational.dev stable name (spec) | Disposition |
|---------------|------------------------------------|-------------|
| `Schedule Trigger` | Schedule Trigger | retain |
| `Get many messages` | Gmail Fetch Leads | adapt (add limit; keep label filter) |
| `Lead-Mail-Parser` | Parse Lead | rewrite |
| `Запись лида (RAW)` | Append RAW v2 | adapt (no AI columns; after parse) |
| `Prepare-OpenRouter-Request` | Prepare AI Request | rewrite (single schema) |
| `HTTP Request (AI #1)` | OpenRouter AI | retain/adapt; gate behind IF AI Enabled |
| `Normalize-AI-Result` | Validate AI Result / Merge path | rewrite |
| `Prepare-AI-Normalizer-Request` | — | **remove** |
| `AI-Normalizer (AI #2)` | — | **remove** |
| `Normalize-Clean-Lead` | Deterministic Lead Processor + merge outputs | rewrite / split |
| `Find Duplicate Lead` | Lookup DEDUP_INDEX | replace full-table read |
| `Mark-Duplicate-Status` | Classify Duplicate | rewrite |
| `IF - Bad Quality` | quality handling inside processor / branch | change (do not strip incoming on TG fail) |
| `Осмысленные лиды (CLEAN)` | Append or Update CLEAN v2 | rewrite mapping |
| `message v2` | Format + Send Telegram Lead Card | rewrite formatter; add success IF |
| `Add label PROCESSED` / `Remove label LEADS_ISEO` | Add Gmail PROCESSED / Remove Gmail Incoming | retain on TG **success** only |
| `Add label ERROR` / `Remove label LEADS_ISEO2` | Add Gmail ERROR / Preserve Incoming | adapt — **do not** remove incoming on TG fail |

Observed typeVersions (export): scheduleTrigger 1.3 · gmail 2.2 · code 2 · httpRequest 4.4 · googleSheets 4.7 · if 2.3 · telegram 1.2.

---

## 1. Patch intent

Transform Sales-Manager-v2 into a two-gate Operational graph:

1. always-run deterministic processing (AI OFF core);
2. optional single AI call with deterministic validation + fallback;
3. bounded dedupe;
4. CLEAN then Telegram then Gmail labels (Telegram-fail preserves incoming).

---

## 2. Target node list

Credential placeholders: `<GMAIL_CREDENTIAL>` · `<GOOGLE_SHEETS_CREDENTIAL>` · `<TELEGRAM_CREDENTIAL>` · `<OPENROUTER_CREDENTIAL>`  
Workbook placeholders: `<RAW_WORKBOOK_ID>` · `<CLEAN_WORKBOOK_ID>`  
Chat: `<MANAGER_CHAT_ID>`  
Labels: `<INCOMING_GMAIL_LABEL_ID>` · `<PROCESSED_GMAIL_LABEL_ID>` · `<ERROR_GMAIL_LABEL_ID>`

Sandbox default: **disabled=`true`** on Gmail mutate / Telegram send / OpenRouter until operator enables for synthetic tests.

| # | Stable name | Source | type (expected) | typeVersion (guide) | Responsibility | Input | Output | Error behavior | Side effects | Credential | Sandbox disabled | Connection targets |
|---|-------------|--------|-----------------|---------------------|----------------|-------|--------|----------------|--------------|------------|------------------|-------------------|
| 1 | Schedule Trigger | retain v2 | `n8n-nodes-base.scheduleTrigger` | 1.2 | Tick intake | — | tick item | none | none | — | optional false | → Gmail Fetch Leads |
| 2 | Gmail Fetch Leads | retain/adapt | `n8n-nodes-base.gmail` | 2.1 | Bounded getMany by incoming label + limit | tick | messages | stop batch / ERRORS | Gmail **read** | `<GMAIL_CREDENTIAL>` | **true** until synthetic | → Parse Lead |
| 3 | Parse Lead | rewrite | `n8n-nodes-base.code` | 2 | Parser + `lead_id` + `parser_version` | message | parsed lead | parse_status failed → Error Handler | none | — | false | → Append RAW v2 |
| 4 | Append RAW v2 | adapt | `n8n-nodes-base.googleSheets` | 4.5+ | Immutable RAW append (`lead_raw_v2`) | parsed | same + raw_logged_at | → Error Handler | Sheets append RAW | `<GOOGLE_SHEETS_CREDENTIAL>` | **true** until sandbox tabs | → Read CONFIG |
| 5 | Read CONFIG | **new** | `n8n-nodes-base.googleSheets` | 4.5+ | Once per batch preferred | lead | lead + config map | AI fail-closed OFF; missing chat → Error Handler | Sheets read CLEAN | `<GOOGLE_SHEETS_CREDENTIAL>` | false (sandbox sheet) | → Normalize CONFIG |
| 6 | Normalize CONFIG | **new** | `n8n-nodes-base.code` | 2 | Types + defaults (`ai_enabled=false`) | config rows | normalized config | use hard defaults | none | — | false | → Deterministic Lead Processor |
| 7 | Deterministic Lead Processor | **new** | `n8n-nodes-base.code` | 2 | Full AI OFF result | lead+config | deterministic CLEAN fields | continue with unusable/poor | none | — | false | → IF AI Enabled |
| 8 | IF AI Enabled | **new** | `n8n-nodes-base.if` | 2.2 | Gate OpenRouter | det result | true/false | false = skip AI | none | — | false | true→Prepare AI Request; false→Lookup DEDUP_INDEX |
| 9 | Prepare AI Request | rewrite | `n8n-nodes-base.code` | 2 | One structured JSON request body | det result | HTTP body | → Merge AI or Fallback (fallback) | none | — | false | → OpenRouter AI |
| 10 | OpenRouter AI | retain/adapt | `n8n-nodes-base.httpRequest` | 4.2 | Single provider call | body | response | onError → Validate/fallback path | external AI | `<OPENROUTER_CREDENTIAL>` | **true** until AI ON tests | → Validate AI Result |
| 11 | Validate AI Result | rewrite (was normalize) | `n8n-nodes-base.code` | 2 | Deterministic JSON/enum/safety validation | AI response | valid\|invalid | invalid → fallback flag | none | — | false | → Merge AI or Fallback |
| 12 | Merge AI or Fallback | rewrite | `n8n-nodes-base.code` | 2 | Merge validated AI or keep det; stamp modes | det+AI | merged lead | always produce merge | none | — | false | → Lookup DEDUP_INDEX |
| 13 | Lookup DEDUP_INDEX | **new** | `n8n-nodes-base.googleSheets` / code+lookup | 4.5+ | Bounded key lookups | merged | matches | treat as no-match + warn | Sheets read | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Classify Duplicate |
| 14 | Classify Duplicate | rewrite | `n8n-nodes-base.code` | 2 | Enums new/reprocessed/repeat/possible | matches | duplicate_* fields | default `new` | none | — | false | → Append or Update CLEAN v2 |
| 15 | Append or Update CLEAN v2 | rewrite | `n8n-nodes-base.googleSheets` + code | 4.5+ | Upsert by lead_id / message id | classified | clean row | → Error Handler | Sheets write CLEAN | `<GOOGLE_SHEETS_CREDENTIAL>` | **true** until sandbox | → Append DEDUP_INDEX |
| 16 | Append DEDUP_INDEX | **new** | `n8n-nodes-base.googleSheets` | 4.5+ | Upsert compact keys | clean | same | log warn; continue if CLEAN ok | Sheets write | `<GOOGLE_SHEETS_CREDENTIAL>` | **true** until sandbox | → Format Telegram Lead Card |
| 17 | Format Telegram Lead Card | rewrite | `n8n-nodes-base.code` | 2 | UX contract formatter | clean | text | → Error Handler | none | — | false | → Send Telegram Lead Card |
| 18 | Send Telegram Lead Card | retain/adapt | `n8n-nodes-base.telegram` | 1.2 | Manager card send | text | send result | → IF Telegram Success false | Telegram send | `<TELEGRAM_CREDENTIAL>` | **true** until synthetic | → IF Telegram Success |
| 19 | IF Telegram Success | **new** | `n8n-nodes-base.if` | 2.2 | Final success gate | send result | true/false | false → error branch | none | — | false | true→Append LEAD_EVENTS; false→Error Handler (tg_fail) |
| 20 | Append LEAD_EVENTS | **new** | `n8n-nodes-base.googleSheets` | 4.5+ | `telegram_sent` / `processed` | success | same | warn | Sheets append | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Add Gmail PROCESSED |
| 21 | Add Gmail PROCESSED | retain | `n8n-nodes-base.gmail` | 2.1 | Add PROCESSED label | success | same | → Error Handler | Gmail mutate | `<GMAIL_CREDENTIAL>` | **true** | → Remove Gmail Incoming |
| 22 | Remove Gmail Incoming | retain | `n8n-nodes-base.gmail` | 2.1 | Remove incoming label | success | same | → Error Handler | Gmail mutate | `<GMAIL_CREDENTIAL>` | **true** | → Update Last Success / Runtime State |
| 23 | Error Handler | expand | `n8n-nodes-base.code` | 2 | Normalize error_code/stage | any fail | error item | always continue to log | none | — | false | → Append ERRORS |
| 24 | Append ERRORS | **new**/adapt | `n8n-nodes-base.googleSheets` | 4.5+ | Structured error row | error | same | last resort stop | Sheets append | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Add Gmail ERROR |
| 25 | Add Gmail ERROR | adapt | `n8n-nodes-base.gmail` | 2.1 | Add ERROR label | error | same | log | Gmail mutate | `<GMAIL_CREDENTIAL>` | **true** | → Preserve Gmail Incoming |
| 26 | Preserve Gmail Incoming | **new**/policy | `n8n-nodes-base.noOp` or code | 1 | **Do not** remove incoming on TG/process fail | error | same | — | **no** remove incoming | — | false | → Update Last Success / Runtime State (error keys) |
| 27 | Update Last Success / Runtime State | **new** | `n8n-nodes-base.googleSheets` | 4.5+ | CONFIG ops keys only | success/error | done | warn | CONFIG update | `<GOOGLE_SHEETS_CREDENTIAL>` | false | (end) |

**Adjustments allowed:** Split In Batches / Loop Over Items after Gmail Fetch if n8n grammar requires; Merge node after AI false branch to rejoin Lookup DEDUP_INDEX; separate error Error Trigger if instance supports it. Do **not** add Admin Execute Workflow.

---

## 3. Connection sketch

```
Schedule → Gmail Fetch → Parse → Append RAW → Read CONFIG → Normalize CONFIG
  → Deterministic Lead Processor → IF AI Enabled
       ├ true  → Prepare AI → OpenRouter AI → Validate AI → Merge AI or Fallback ─┐
       └ false ──────────────────────────────────────────────────────────────────┤
                                                                                 ▼
                                                    Lookup DEDUP → Classify → CLEAN upsert
                                                      → DEDUP_INDEX → Format TG → Send TG
                                                      → IF TG Success
                                                           ├ true → LEAD_EVENTS → PROCESSED → Remove Incoming → Update Success
                                                           └ false → Error Handler → ERRORS → ERROR label → Preserve Incoming → Update Error keys
```

Any hard failure after RAW may jump to Error Handler (Preserve Incoming).

---

## 4. AI OFF path (node 7) — required outputs

Always emit (canonical enums):

| Field | Rule |
|-------|------|
| `client_name` | from parsed_name; empty allowed |
| `primary_contact` | best of phone/email/messenger |
| `contact_type` | `phone`\|`email`\|`messenger`\|`mixed`\|`unknown` |
| `phone` / `email` / `messenger` / `site` | normalized; never invent |
| `service` | keyword dictionary order Audit→SEO→Direct→Site→Other |
| `summary` | truncated cleaned request + service hint |
| `priority` | high only with explicit urgent/business-critical **or** strong Audit+site / strong repeat signals; default normal; low for informational/unusable |
| `quality_status` | see §4.2 |
| `quality_comment` | short Russian |
| `missing_fields` | list |
| `clarification_questions` | Russian templates |
| `manager_recommendation` | Russian template; complete leads use service-aware next step (Audit/SEO/Other); no tautology |
| `first_reply_text` | name/no-name templates |
| `first_reply_source` | `template` |
| `processing_mode` | `ai_off` |
| `ai_status` | `skipped` |
| `fallback_used` | `false` |

**No OpenRouter node executes** on false branch of IF AI Enabled.

### 4.1 Service keyword dictionaries (v1)

| Service | Keywords / signals (case-insensitive; RU+EN) |
|---------|-----------------------------------------------|
| Audit | аудит, seo-аудит, audit, проверка сайта; form/page `/audit`; calc audit flags |
| SEO | seo, продвижение, поисковое, позиции, трафик, семантическое ядро (if not already Audit) |
| Direct | директ, контекст, яндекс директ, ppc, реклама в поиске |
| Site | создание сайта, разработка сайта, лендинг, сайт под ключ, редизайн |
| Other | no strong match |

First match wins.

### 4.2 Quality rules

| Condition | `quality_status` |
|-----------|------------------|
| No usable contact | `unusable` (= Task “bad”) |
| Contact; name **and** site missing **and** request_text &lt; 40 | `poor` |
| Contact; missing name or site or thin request | `needs_data` (= Task “warning”) |
| Contact + (name or site) + meaningful request | `ok` |

Do **not** infer urgency from missing fields alone.

### 4.3 Reply templates

**With name:**

```
Здравствуйте, {name}!

Спасибо, ваша заявка получена{service_clause}.
Специалист свяжется с вами, чтобы уточнить задачу.

С уважением,
команда i-SEO
```

**Without name:**

```
Здравствуйте!

Спасибо, ваша заявка получена{service_clause}.
Менеджер свяжется с вами, чтобы уточнить задачу.

С уважением,
команда i-SEO
```

`service_clause` only when service confident (Audit/SEO/Direct/Site). Forbidden: prices, deadlines, guarantees, fake personalization, internal notes.

---

## 5. AI ON path (nodes 9–12)

### 5.1 Request input

Normalized lead evidence only (+ deterministic snapshot for merge). No secrets. No raw credential material.

### 5.2 Expected AI JSON

```json
{
  "summary": "",
  "service": "Audit|SEO|Direct|Site|Other",
  "priority": "low|normal|high",
  "quality_status": "ok|needs_data|poor|unusable",
  "quality_comment": "",
  "missing_fields": [],
  "clarification_questions": [],
  "manager_recommendation": "",
  "first_reply_text": "",
  "risk_flags": [],
  "confidence": 0
}
```

### 5.3 Validation (reject → fallback)

- parseable JSON (no markdown fences / raw leakage);
- strict enums;
- confidence numeric 0–1;
- array length limits (e.g. questions ≤ 8; missing ≤ 20);
- text length limits (summary ≤ 600; reply ≤ 1200; comment/recommendation ≤ 400);
- `first_reply_text` non-empty;
- no internal notes in reply;
- no fabricated names/sites/budgets absent from input;
- no price / deadline / guaranteed-result / automatic-action language.

### 5.4 Fallback

On request error, timeout, empty, invalid JSON, enum failure, unsafe reply, fabricated facts, missing required field:

- reuse already computed deterministic result;
- `processing_mode=ai_fallback`;
- `ai_status=fallback`;
- `fallback_used=true`;
- `first_reply_source=ai_fallback_template`;
- LEAD_EVENTS / ERRORS as appropriate.

### 5.5 Merge on success

Per `AI-OFF-ON-CONTRACT-v1`: prefer validated AI copy fields; quality = **stricter** of AI vs deterministic; never upgrade `unusable`→`ok` without contacts; `first_reply_source=ai`; `processing_mode=ai_on`; `ai_status=ok`.

---

## 6. Telegram failure after CLEAN (approved)

1. CLEAN already written.  
2. Telegram fails → IF Telegram Success = false.  
3. Append ERRORS (`tg_send`).  
4. Add Gmail ERROR.  
5. **Preserve** incoming label (do not remove).  
6. **Do not** add PROCESSED.  
7. Retry same Gmail message → `duplicate_status=reprocessed`.  
8. After successful Telegram: PROCESSED + remove incoming.

---

## 7. Code pitfalls (MetaBOT)

- No `structuredClone`.  
- Always pass deterministic item when AI skipped.  
- No MarkdownV2 unless later evidence proves required.  
- No success Telegram before CLEAN.  
- No PROCESSED before Telegram success.

---

## 8. SAFE UNKNOWN

Credential display names and instance-specific typeVersions. Phase 3E.2.3 schedule and node count are now observed; final live call counts remain SAFE UNKNOWN.

---

*Related: DEDUP-IMPLEMENTATION-SPEC-v1 · TELEGRAM-FORMATTER-SPEC-v1 · SHEETS-MIGRATION-SPEC-v1 · AI-OFF-ON-CONTRACT-v1.*

## Phase 3C.1 observability note

After Gmail Fetch Leads: enable `alwaysOutputData`, add Intake Gate + Switch Intake Route (`error` → Error Handler, `empty` → runtime `last_poll_success_at` only, `lead` → Parse Lead). Keep OpenRouter disabled. Do **not** weaken the incoming-label production filter.

## Phase 3C.2 field-loss / label finalize note

- **Classify Duplicate** must base the lead on `$('Merge AI or Fallback').first().json` (Lookup DEDUP_INDEX replaces `$input` with sheet rows).
- **Format Telegram Lead Card** must read `$('Classify Duplicate').first().json` (CLEAN/DEDUP append outputs are sheet-shaped).
- **Send Telegram Lead Card** `chatId` must use `$('Normalize CONFIG').first().json.telegram_manager_chat_id`.
- Gmail Add PROCESSED / Remove Incoming / Add ERROR `messageId` must use `$json.gmail_message_id || $('Parse Lead').first().json.gmail_message_id` (do not reference retired node names).

## Phase 3D retry / delivery idempotency note

- **Classify Duplicate** matches DEDUP rows by exact `key_type` + `normalized_value` (not type-only); reads CONFIG `tg_delivered:<gmail_message_id>` / `tg_attempts:<gmail_message_id>`.
- **Format Telegram Lead Card** sets `skip_telegram` when already delivered or attempts ≥ 5 (`telegram_retry_exhausted`).
- **IF Need Telegram Send** → true: **Telegram Skip Pass** → Result Gate (resume Gmail finalize without resend); false: **Send Telegram Lead Card**.
- **Update Last Success / Runtime State** writes per-message delivery idempotency keys after success/failure.
- **Phase 3D.2.1:** Update code must read delivery truth from `$('Telegram Result Gate')` when present (Gmail finalize stubs lack `telegram_ok`). Historical 3D behavior wrote `last_poll_success_at` on empty polls. Phase 3E.2.3 supersedes it: empty polls return `[]` and write no CONFIG state. Success writes remain minimized. Telegram send nodes keep `appendAttribution=false`.
- Do **not** depend only on Gmail unread state for exactly-once Telegram delivery.

## Phase 3D.1 real website form parser note

- **Parse Lead** must extract Russian audit-form labels with next-label delimiting (multiline **and** collapsed single-line): `От кого`/`Имя`, `Способ связи`, `Контакт`, `Телефон`, `Email`/`E-mail`/`Почта`, `Адрес сайта`/`Сайт`, `Комментарий`/`Сообщение`, `Отправлено со страницы`.
- Stamp `parser_version=sm-parser-v3.1`.
- CONFIG display `parser_version` must match deployed parser (`sm-parser-v3.1`).
- Complete-lead next-step guidance is service-aware (Audit/SEO/Other); never tautological.
- Interpret `Способ связи` → phone/email/messenger; reject placeholders (`44`, `#ERROR!`, `UNKNOWN`, …).
- Site: accept with/without scheme; no DNS required; allow `.example` operator hosts.
- `Заявка на бесплатный аудит` → Audit / `form_name`.
- Do **not** auto-replay already PROCESSED malformed messages; request one new clean test lead.
- Reference harness: `implementation/parser-fixtures/` (F-AF01–F-AF12).

## Phase 3D.3 formatter + keyboard + lifecycle defaults note

- **Format Telegram Lead Card** now stamps `message_format_version=sm-msg-v2` (was `sm-msg-v1`) and emits the emoji-indicator / `<code>` contact / `<pre>` reply layout — see TELEGRAM-FORMATTER-SPEC-v1 §6. No change to CLEAN/DEDUP writes upstream of formatting.
- **Send Telegram Lead Card** attaches the two-button inline keyboard (`sm:p:<token12>` processed / `sm:s:<token12>` spam) only when the produced card is an actionable **pending** lead; archive/service sends (e.g. Admin `/leads` output) omit `replyMarkup`.
- CLEAN upsert on first write now defaults new lifecycle columns: `lifecycle_status=pending`, `manager_action_user_id`/`manager_action_processed_at`/`manager_action_spam_at` empty, `manager_action_token` generated opaque per-lead token (12-char) used for callback routing — see SHEETS-MIGRATION-SPEC-v1 §3 / §11.
- Operational.dev does **not** process callbacks; all lifecycle-button handling lives in Admin.dev (see ADMIN-WORKFLOW-PATCH-SPEC-v1 Phase 3D.3 notes) reading/writing the same `lead_clean_v2` tab.

## Phase 3D.3.1 note — Sheets RAW phone writes

- **Append or Update CLEAN v2** and **Append RAW v2** set `options.cellFormat=RAW` so contact phones are not interpreted as formulas.
- Formatter suppresses `#ERROR!` / formula-parse placeholders in live cards (mirrors Admin archive rendering).
- No change to Gmail intake, exactly-once gates, or AI OFF path.
- No new workflow created; no change to AI OFF/ON gating; no change to Telegram-fail / PROCESSED label policy (§6 above).

## Phase 3D.4 parser + formatter note

- **Parse Lead** bumps to **`parser_version=sm-parser-v3.2`**: messenger/site split (`t.me` not site); contact method inference; comment «в тг» preference; source page normalization. Registry: `knowledge/WEBSITE-FORM-FORMATS-v1.md`.
- **Format Telegram Lead Card** bumps to **`message_format_version=sm-msg-v2.1`** — reduced emoji density (see TELEGRAM-FORMATTER-SPEC-v1 §7).
- CONFIG display keys must match deployed versions.
- One form per iteration policy: `evidence/phase3d4/MULTI-FORM-TEST-PLAN-v1.md`.

---

## Phase 3D.7 addendum — multi-recipient delivery

After Format Telegram Lead Card:

1. Read LEAD_DELIVERIES
2. Read ACCESS_CONTROL
3. Expand Delivery Recipients (N items)
4. Per-recipient send using `$json.telegram_delivery_chat_id`
5. Stamp + Append/Upsert LEAD_DELIVERIES
6. Aggregate Delivery Finalizer (Admin-anchor) → IF Telegram Success → Gmail finalize

Do not expand before business dedupe/CLEAN. Do not use CONFIG `telegram_manager_chat_id` as sole destination.

## Phase 3D.8 addendum — Format-only action-button restoration

Observed defect: Format emitted `telegram_reply_markup` and `telegram_action_token` but not `telegram_has_buttons`; the strict IF check therefore always selected the no-button Send branch. The With Buttons branch also expected unset processed/spam callback fields.

Repair only Format in workflow `xSnXPy8cEHoZw6xG`: set `telegram_has_buttons` for actionable pending cards; set `telegram_callback_processed=sm:p:<token12>` and `telegram_callback_spam=sm:s:<token12>`; keep `telegram_reply_markup`. Do not change Parser 3.2. Preserve these fields through Expand/Restore. Archive/service/non-pending cards must remain buttonless.

## Phase 3D.8.3 addendum — pending button label polish

Visible pending-card captions only (same workflow ID `xSnXPy8cEHoZw6xG`):

- Format `buildReplyMarkup` + Send With Buttons `inlineKeyboard` texts → **`✅ Обработано`** / **`🚫 Спам`**
- Do **not** change callback prefixes, token algorithm, `telegram_has_buttons` routing, Parser 3.2, or final lifecycle headings (**`✅ Обработан`** remains the completed-state line)
- Admin.dev callback logic: no change required for this polish

## Phase 3D.8.1 note — LEAD_DELIVERIES durability

Operational claim/append nodes require an existing `LEAD_DELIVERIES` tab with header columns matching the appendOrUpdate schema. A missing tab presents as continueOnFail error items and breaks Admin multi-copy sync while Telegram sends may still succeed. Do not create new workflows to fix this; ensure the tab in the CLEAN workbook.

## Phase 3E.1 addendum — Parser 3.3 / Format sm-msg-v2.3

Same workflow ID `xSnXPy8cEHoZw6xG` (no copy):

- **Parse Lead** → `sm-parser-v3.3` + Lead Semantic Model v1 (website states, intent precedence, comment boundary, quality, first-reply draft). Lib sync target: `implementation/parser-fixtures/parse-lead-lib.mjs` (+ processor/formatter under `runtime-libs/`).
- **Deterministic Lead Processor** → AI OFF pass-through of semantic fields; `processing_mode=ai_off`.
- **Format Telegram Lead Card** → `message_format_version=sm-msg-v2.3`; site/reply consistency; keep short pending labels and button payload bridge from 3D.8.x.
- CONFIG stamps: `parser_version=sm-parser-v3.3`, `message_format_version=sm-msg-v2.3`, `ai_enabled=false`.
- Do **not** change callbacks, ACCESS_CONTROL, or create workflows.
- Harness: `implementation/harness/phase3e1-harness.mjs` — **46/46 PASS**.

## Phase 3E.2 addendum — First Reply Engine v2 / Format sm-msg-v2.4

Same workflow ID `xSnXPy8cEHoZw6xG` (no copy):

- **Parse Lead** / **Deterministic Lead Processor** → embed `first-reply-engine-v2.mjs` (`sm-reply-v2.0`) + known-information guard; Parser remains `sm-parser-v3.3`.
- **Format Telegram Lead Card** → `message_format_version=sm-msg-v2.4`; copy-block / suppression UX; keep short pending labels and button payload bridge.
- CONFIG stamps: `parser_version=sm-parser-v3.3`, `message_format_version=sm-msg-v2.4`, `reply_template_version=sm-reply-v2.0`, `ai_enabled=false`.
- Do **not** change callbacks, ACCESS_CONTROL, activate Sales-Manager-v2, or create workflows.
- Admin.dev untouched unless archive formatter hardcodes obsolete reply rebuild (not required in 3E.2).
- Harness: `implementation/harness/phase3e2-harness.mjs` — **59/59 PASS**.

### Phase 3E.2.3 live patch note (2026-08-05)

Same Operational.dev patched in place, held inactive for the quiet window, then reactivated for the successful final proof; node count remains 45.

- Empty Runtime State returns `[]` (0 CONFIG writes).
- Final schedule `minutesInterval=2`; attempted `secondsInterval=120` was rejected by n8n as `Invalid interval`.
- Intake Gate static-data single-flight TTL 4 minutes.
- LEAD_DELIVERIES exact `stable_lead_ref` filter + `alwaysOutputData` + retry 3 × 30s.
- ACCESS_CONTROL retry 3 × 30s, fail closed, no continue-on-fail.
- Claim upsert retry 3 × 30s, fail closed.
- Normalize CONFIG passes `tg_delivered:*` / `tg_attempts:*`.
- Expand reuses Read CONFIG snapshot; no extra fallback Sheets call.
- Success CONFIG writes minimized to one recipient guard.
- Proof exemption: `PHASE_3E2_3_FINAL_EXACTLY_ONCE_PROOF` + `final-proof.example`.

Admin contour and access state unchanged; AI OFF; rollback workflow inactive. Live exactly-once proof PASS: claims=2, sendOk=2, stamps=2, five-poll resends=0. Gmail finalization now continues regular output after synthetic fake-ID failure; two CONFIG guards were reconciled without resend.


## 3F.2.1

Emit `source_display=Сайт i-seo.su` for website-form leads alongside `source_channel`. Do not alter parser 3.3 semantics.

### Phase 3G.1 patch note

Target: wire Approved Template Router/Renderer + recipient profile resolution into Operational Format/Expand path. Shared metadata → LEADS; personalized drafts → recipient store. Keep AI OFF; no client auto-send; preserve fail-closed delivery. **Historical:** live patch applied; seed repaired 3G.1.1. Libs: `runtime-libs/approved-template-*.mjs`, `reply-profile-lib.mjs`. Rollback stamp: `sm-reply-v2.1`.

### Phase 3G.2 Operational note

Operational.dev remains **45** nodes active — no structural expansion required for numbering. Consumer of profiles must resolve `reply_sender_name` + `reply_profile_number` from ACCESS_CONTROL; never Telegram display/username. Nickname «Мопс» never in customer copy (use Михаил for MOD_A). Contour: AI OFF · reminders OFF · Sales-Manager-v2 inactive · `LEADS` / `LEAD_EVENTS` · stats epoch 05.08.2026 Europe/Moscow.

### Phase 3G.2.2 Operational note

Operational.dev remains **45** nodes active — the ADMIN_A/MOD_A profile-wipe defect was isolated to Admin.dev's authorization/upsert path and did not affect Operational.dev's recipient personalization (regression-checked, `evidence/phase3g2-2/OPERATIONAL-PERSONALIZATION-REGRESSION-v1.md`). `Expand Delivery Recipients` gains a `resolver_version=iseo-reply-profile-resolver-v1.0` label field for traceability — no structural change. Contour unchanged: AI OFF · reminders OFF · Sales-Manager-v2 inactive.

### Phase 3H.4 Operational patch note

Same Operational.dev ID (45 nodes):

1. **Update Last Success / Runtime State:** write `gmail_poll_heartbeat` + mirror keys on **empty** scheduled polls (`iseo-gmail-poll-heartbeat-v1.0`).
2. Stamp `last_production_processed_*` on non-test processing success only.
3. Supersedes pre-3H.4 empty-poll `[]` no-write behavior that froze `/status` poll time.
4. Evidence: `evidence/phase3h4/` · `architecture/GMAIL-POLL-HEARTBEAT-CONTRACT-v1.md` · `implementation/SCHEDULED-POLL-OBSERVABILITY-v1.md`.

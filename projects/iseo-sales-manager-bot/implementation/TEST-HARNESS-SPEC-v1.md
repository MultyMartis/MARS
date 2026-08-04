# TEST HARNESS SPEC v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A  
**Source fixtures:** SANDBOX-TEST-PLAN-v1 F01–F21  
**Rule:** synthetic only — no real unread Gmail, no real clients, no production labels

---

## 1. MetaBOT Programmer validation gates

Before any sandbox apply / import:

| Gate | Pass criteria |
|------|---------------|
| G1 JSON parse | Workflow JSON parses |
| G2 Unique names | Node names unique |
| G3 Connections | All targets exist |
| G4 Credentials | Placeholders / names only — no secret values |
| G5 Sandbox side effects | Gmail mutate / prod Telegram / OpenRouter disabled or sandbox-bound |
| G6 No live recipients | No real manager/admin chat ids in committed artifacts |
| G7 No real workbook ids | Placeholders or sandbox ids only in committed artifacts |
| G8 AI OFF isolation | When `ai_enabled=false`, OpenRouter node not executed |
| G9 Incoming preserve | Error/TG-fail path does not remove incoming |
| G10 No PROCESSED on TG fail | Telegram fail never reaches Add Gmail PROCESSED |
| G11 same_message | Classifies `reprocessed`, never business `repeat` |
| G12 no-contact UX | `quality_status=bad`; empty reply; no «менеджер свяжется»; contact Q1 first |
| G13 quality no-dup | Quality label appears once; missing on `Не хватает:` |
| G14 history human | No `match=` / `prior=` / lead ids in Telegram |
| G15 mode RU | Без ИИ / С ИИ / ИИ не сработал, использован шаблон |
| G16 synthetic footer | Dev cards: `Тестовая заявка · PHASE 3B.3`; no hashtags |
| G17 health wording | No `readable_ref_ok` / `structural_ok_no_fetch` / `inactive_expected` |
| G18 admin RU config | Контур / Режим ИИ / Версия парсера / Версия сообщений |

---

## 2. Fixture matrix

Synthetic Gmail payloads use fake message ids `msg_synth_Fxx` and domains `example.com` / `example.ru` only.

| ID | Synthetic Gmail payload (summary) | Parser expect | Service | Quality | Duplicate | AI branch | Reply source | Sheets writes | Gmail labels | Telegram | Forbidden |
|----|-----------------------------------|---------------|---------|---------|-----------|-----------|--------------|---------------|--------------|----------|-----------|
| F01 | Phone only body | phone set; name empty | Other/Audit per text | needs_data/poor | new | OFF | template | RAW+CLEAN+DEDUP+EVENTS | PROCESSED+remove in on TG ok | card no-name | invent email |
| F02 | Email only | email primary | per text | needs_data+ | new | OFF | template | same | success labels | card | invent phone |
| F03 | Telegram @handle only | messenger | per text | needs_data+ | new | OFF | template | same | success | card | generic “telegram” as contact |
| F04 | Named audit + phone | name+phone | Audit | ok/needs_data | new | OFF | template | same | success | named card | |
| F05 | Unnamed audit + phone | phone; Audit signals | Audit | needs_data | new | OFF | template | same | success | no-name Audit | |
| F06 | SEO + site + email | site+email | SEO | ok/needs_data | new | OFF | template | same | success | site shown | |
| F07 | Direct keywords | — | Direct | any | new | OFF | template | same | success | Директ | |
| F08 | Site build keywords | — | Site | any | new | OFF | template | same | success | Сайт | |
| F09 | Vague “вопрос” | — | Other | needs_data+ | new | OFF | template | same | success | Другое | |
| F10 | Calculator payload flag | calc_detected | Audit/SEO per calc | any | new | OFF | template | RAW calc fields | success | | AI columns in RAW |
| F11 | Malformed / empty body | parse partial/failed | Other | unusable/error | new/error | OFF | template/error | RAW+ERRORS maybe | ERROR; incoming preserved if fail | no fake success | PROCESSED without CLEAN |
| F12 | Same `gmail_message_id` as prior | same id | — | — | **reprocessed** / same_message | OFF | template | CLEAN **update** | per gate | «Повторная обработка» | status=repeat |
| F13 | Same phone new message | new msg id | — | — | **repeat** / phone | OFF | template | CLEAN append + history | success | Повторный лид | site_only as repeat |
| F14 | Same site different contact | new contacts | — | — | **possible** / site_only | OFF | template | CLEAN append | success | card delivered | suppress lead |
| F15 | AI ON valid JSON | — | AI service | merged | new | ON success | ai | CLEAN ai stamps | success | Режим AI | second AI call |
| F16 | AI invalid JSON | — | det | det | new | ON fallback | ai_fallback_template | fallback stamps | success | fallback mode | publish invalid JSON |
| F17 | AI timeout | — | det | det | new | ON fallback | ai_fallback_template | fallback | success | fallback | hang without fallback |
| F18 | AI forbidden promise | — | det | det | new | ON fallback | ai_fallback_template | fallback | success | fallback | send price promise |
| F19 | Sheets CLEAN write fail | — | — | — | — | OFF | — | ERRORS; no fake CLEAN | ERROR; incoming preserved | **no** success card | success Telegram |
| F20 | Body with `<` `&` long text | escape | — | — | new | OFF | template | same | success | no entity crash | MarkdownV2 crash |
| F21 | CLEAN ok, Telegram fail | — | — | — | new | OFF | template | CLEAN+ERRORS | **ERROR label**; **no PROCESSED**; **incoming preserved** | fail | PROCESSED; remove incoming |

---

## 3. AI mode matrix

| Mode | Fixtures |
|------|----------|
| AI OFF (zero OpenRouter) | F01–F14, F19–F21 |
| AI ON | F15–F18 (+ spot F04/F06) |

Evidence required: n8n execution shows **0** HTTP OpenRouter calls on AI OFF runs.

**Phase 3B.2 acceptance note:** the prior `AI_DEADLINE` GAP is **CLOSED**. Expanded deterministic Russian unsafe-pattern detection rejected deadline, price, guarantee, and fabricated-fact cases; the Phase 3B.2 local harness result was **19 PASS / 0 FAIL / 0 GAP**.

---

## 4. Admin command fixtures

| Test | Expect |
|------|--------|
| Unknown | Exact `Неизвестная команда. Используйте /help.` |
| Non-admin | `Доступ запрещён.` |
| `/start` authorized | Contour + AI wording; points to `/help` |
| `/start` unauthorized | `Доступ запрещён.` (no config leak) |
| `/help` | Lists `/start`; omits `/test_lead`; canonical `/ai_status` (no `/aistatus` ads) |
| `/status` lead stamp | Shows `last_lead_success_at` Moscow time for latest delivered production lead |
| Attribution | Admin/Ops Telegram send: `appendAttribution=false` |
| Runtime update unit | Gmail-stub + gate success → writes `last_lead_success_at`; empty poll → poll only; fail → no success stamp |
| `/ai_on` `/ai_off` | CONFIG flip + LEAD_EVENTS audit |
| `/health` AI off | AI probe SKIPPED |
| `/config` | Shows `parser_version=sm-parser-v3.2`, `message_format_version=sm-msg-v2.1` when aligned |
| `/test_lead` prod | refused |
| `/test_lead` dev | sandbox rows only |

---

## 5. Pass criteria (sandbox exit)

1. F01–F21 Pass/Fail recorded.  
2. No client send path.  
3. RAW has no AI pretence columns.  
4. CLEAN stores `first_reply_text`.  
5. F12–F14 dedupe distinctions correct.  
6. F16–F18 fallback works.  
7. F21 label policy holds.  
8. Gates G1–G11 green.

---

## 6. Evidence location (Phase 3B+)

`projects/iseo-sales-manager-bot/evidence/phase-3-sandbox/` — create when tests run.

---

*Related: SANDBOX-TEST-PLAN-v1 · SANDBOX-APPLY-GATE-v1.*


## Phase 3B.4

Harness webhook injection remains valid for reply-shape and unauthorized tests. It is **not** a substitute for real Telegram Trigger acceptance evidence.


## Phase 3B.4.1

Alias harness (webhook → Normalize only) may verify `/aistatus` `/lasterror` `/aion` `/aioff` `/foobarunknown`. It is **not** a substitute for the ten real Telegram Trigger executions.

## Phase 3B.5

Normalize harness remains valid for polish reply-shape checks. Real Telegram Trigger `/help` post-polish is required to prove Trigger registration after Admin patch cycles. Full Trigger re-matrix is optional operator follow-up when Admin stays active.

## Phase 3D.1 — real form parser fixtures

Local pure-JS suite (no n8n required):

- `implementation/parser-fixtures/parse-lead-lib.mjs`
- `implementation/parser-fixtures/run-fixture-suite.mjs`
- Fixtures **F-AF01–F-AF12** (multiline/collapsed audit form, email/Telegram, NBSP, reorder, missing fields, malformed contact, legacy pre-parsed, special chars, quoted duplicate)
- Evidence: `evidence/phase3d1/PARSER-FIXTURE-ACCEPTANCE-v1.md`

## Phase 3D.3 — manager UX / lead-action fixtures (F-MU01–F-MU30)

Local pure-JS/unit harness covering `sm-msg-v2` formatting, inline keyboard, callback state machine, `/leads`, and lifecycle defaults. Synthetic lead ids and `SYNTHETIC_TEST` markers only — no real Telegram sends in the local run; live confirmation is a separate matrix (below).

| ID | Area | Case | Expect |
|----|------|------|--------|
| F-MU01 | Visual indicator | New lead title | 🟢 Новый лид |
| F-MU02 | Visual indicator | Repeat lead title | 🟡 Повторный лид |
| F-MU03 | Visual indicator | Possible-repeat title | 🟠 Возможный повтор |
| F-MU04 | Visual indicator | Reprocessed title | 🔵 Повторная обработка |
| F-MU05 | Copy field | `client_name` present | rendered as `<code>` |
| F-MU06 | Copy field | `phone` present | rendered as `<code>` |
| F-MU07 | Copy field | `email` present | rendered as `<code>` |
| F-MU08 | Copy field | `messenger` present | rendered as `<code>` |
| F-MU09 | Copy field | `site` present | rendered as `<code>` |
| F-MU10 | Reply copy block | Full reply text | single `<pre>` block; manager instruction line stays outside `<pre>` |
| F-MU11 | Inline keyboard | Actionable pending card | both buttons attached with `sm:p:`/`sm:s:` tokens |
| F-MU12 | Inline keyboard | Archive/service card | no buttons attached |
| F-MU13 | Callback | `pending→processed` | outcome `applied`; Sheets mutate true; `LEAD_EVENTS` `manager_marked_processed` |
| F-MU14 | Callback | repeat same processed click | outcome `idempotent`; no duplicate Sheets mutate |
| F-MU15 | Callback | `pending→spam` | outcome `applied`; Sheets mutate true |
| F-MU16 | Callback | repeat same spam click | outcome `idempotent` |
| F-MU17 | Callback | `processed→spam` after settle | outcome `conflict`; no Sheets status change; event recorded |
| F-MU18 | Callback | `spam→processed` after settle | outcome `conflict`; no Sheets status change |
| F-MU19 | Callback | unauthorized user | `Доступ запрещён.`; no Sheets mutation |
| F-MU20 | Callback | unknown/expired token | safe generic failure; no Sheets mutation |
| F-MU21 | Message edit | successful mutate | card edited, keyboard cleared |
| F-MU22 | Message edit | edit call fails | Sheets mutation kept; `Callback Edit Result` notice path used; not rolled back |
| F-MU23 | `/leads` | default (no arg) | 5 most recent CLEAN leads |
| F-MU24 | `/leads` | `/leads 3` | 3 most recent |
| F-MU25 | `/leads` | `/leads 10` | 10 most recent |
| F-MU26 | `/leads` | `/leads 7` (invalid) | rejected with usage message; no partial result |
| F-MU27 | `/leads` | synthetic rows present | `SYNTHETIC_TEST` rows excluded from result |
| F-MU28 | `/leads` | output cards | archive shape, no inline buttons |
| F-MU29 | Authorization | `manager_action_user_ids` empty | falls back to `admin_user_ids` |
| F-MU30 | CLEAN defaults | new lead first write | `lifecycle_status=pending`, `manager_action_token` generated, `message_format_version=sm-msg-v2` |

**Result:** 30/30 fixtures PASS plus 1 aggregate regression check (full `sm-msg-v1`-compatible field set still populated under `sm-msg-v2`) = **local harness 31/31 PASS**.

### Live acceptance matrix (Admin Telegram Trigger, operator-private)

| Check | Result |
|-------|--------|
| `/start` | PASS |
| `/help` | PASS |
| `/config` | PASS |
| `/leads` (3\|5\|10) | PASS |
| Callback processed (applied) | PASS |
| Callback idempotent re-click | PASS |
| Callback conflict (processed↔spam) | PASS |
| Callback unauthorized | PASS |

AI calls during live acceptance: **0**. Client auto-messages: **0**. New workflows: **0**.

## Phase 3D.3.1 — archive recovery + Sheets value safety

Local harness (Storage incoming `phase3d31-local/run-04-harness.mjs`, not committed): **29/29 PASS** covering default `/leads`→5, exact `3|5|10`, reject `7`/`03`/trailing garbage, fewer-than-requested honesty, newest-first unique selection, technical-retry collapse, multi-item capture passthrough, ordinals, lifecycle labels, formula-phone suppression, plus-phone text sanitize, copy-friendly fields, no buttons on done cards, synth exclusion, AI-OFF zero-provider, Admin/callback/Ops regression stubs.

Live Admin acceptance (`/leads 3|5|10|7`): **PASS** — multi-card Telegram delivery, formula suppressed, invalid count warning, contour gates unchanged (`evidence/phase3d31/`).

## Phase 3D.4 — enrollment + parser semantics fixtures (F-3D4-01–F-3D4-12)

Local harness covering role-aware start/help, Olya callback auth, parser v3.2 semantics, sm-msg-v2.1 emoji reduction. Synthetic identities and form bodies only.

| ID | Area | Case | Expect |
|----|------|------|--------|
| F-3D4-01 | Auth | Olya hash on manager list | callback allow |
| F-3D4-02 | Auth | Olya hash not on admin list | `/status` deny |
| F-3D4-03 | Start | manager-only `/start` | manager greeting shape |
| F-3D4-04 | Help | manager-only `/help` | manager help shape |
| F-3D4-05 | Parser | t.me in site field | messenger not site |
| F-3D4-06 | Parser | real domain in site | site populated |
| F-3D4-07 | Parser | «в тг» in comment | Telegram preference in summary |
| F-3D4-08 | Parser | `/free-audit/` page | normalized `free-audit` |
| F-3D4-09 | Formatter | v2.1 emoji density | max 2 emoji on standard card |
| F-3D4-10 | Callback | Olya processed synthetic | applied |
| F-3D4-11 | Callback | Olya spam synthetic | applied |
| F-3D4-12 | Regression | admin count 1, manager count 2 | PASS |

Combined with F-MU01–F-MU30 regression: **30/30 PASS** (manager UX suite unchanged).

### Live acceptance (Phase 3D.4)

| Check | Result |
|-------|--------|
| CONFIG enrollment | PASS |
| Live patch | PASS |
| Synthetic Olya callbacks | PASS |
| Olya live `/start` / `/help` | **PENDING** |

AI calls: **0**. Client messages: **0**. New workflows: **0**.


---

## Phase 3D.5 note

See `evidence/phase3d5/` for ACCESS_CONTROL / ACCESS_EVENTS, public auth routing, moderator registry Admin commands, and harness coverage (30+ checks). ACCESS_CONTROL is access SoT; do not edit workflow code to enroll moderators.


## Phase 3D.5.1 — Access registry population and SoT repair

- **ACCESS_CONTROL** is the primary authorization authority (Telegram user ID keyed; username informational only).
- `manager_action_user_ids` is legacy and is **not** an active moderator authority after registry acceptance.
- `admin_user_ids` remains recovery-only Admin bootstrap when ACCESS_CONTROL cannot be read technically.
- A revoked/blocked ACCESS_CONTROL row always overrides CONFIG allowlists.
- ACCESS_EVENTS append mapping must reference Prepare Access Upsert fields (never post-Upsert `` metadata).
- Evidence: `evidence/phase3d51/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3d51-access-registry-repair-v1.md`.

## Phase 3D.5.2 — Silence recovery harness

Required coverage includes: registry found/absent/empty/error/malformed/blocked/revoked; Admin bootstrap recovery; moderator/public; `/start` `/help` `/config` `/moderators` `/moderator_pending`; unknown command; bot `@suffix`; chat context survival; one-response invariant; callback auth/deny; AI OFF; Operational Gmail exactly-once; no new workflow; no `require('crypto')` in Admin Code nodes.

## Phase 3D.6 — status and notification suite
Required checks (31): public/pending/moderator/Admin/revoked/blocked `/my_status`; no registry row; registry read failure; **exact live Code-node mode** for `My Status` and `Finalize Access Notification` (`runOnceForAllItems` when using `$input.first()`); grant/revoke notification success paths; notification failure boundary (mutation persists); help includes `/my_status` for public/moderator/Admin; canonical underscores; ACCESS_CONTROL primary; revoked overrides legacy fallback; callback denied after revoke / allowed after restore; Admin/moderator/public `/start`; callback/archive/Admin-command/Operational exactly-once regression stubs; AI OFF zero-provider; zero client auto-messages; zero new workflows.

**Code-mode rule:** harness must execute against the exact live n8n Code-node `mode`. `runOnceForEachItem` code must not call `$input.first()`. Zero-item Code failures are deployment blockers. Role-specific command tests must include a real non-Admin path (operator Telegram acceptance is separate evidence).

**Result:** `evidence/phase3d6/HARNESS-RESULT.json` records **31/31 PASS** at Phase 3D.6.1 closeout. Live non-Admin `/my_status` acceptance is operator-confirmed. Direct grant/revoke notification delivery remains SAFE UNKNOWN unless independently evidenced.

---

## Phase 3D.7 harness

37 cases (fan-out, eligibility exclusions, idempotency, isolation, sync, commands, regressions). Local runner: STORAGE `phase3d7-local/run-04-harness.mjs` — required **37/37 PASS**.

## Phase 3D.8 button-repair harness

Required assertions: Format sets `telegram_has_buttons` only for actionable pending cards; both callback fields use `sm:p:`/`sm:s:` plus a 12-character opaque token; reply markup survives Expand and Restore; strict IF selects With Buttons; archive/service/non-pending cards select buttonless Send; repeated poll does not duplicate delivery; Admin callback parser accepts both actions; AI calls and client auto-messages remain zero.

## Phase 3D.8.1 callback/lifecycle harness — 34 cases

Required: early ack; processed/spam parse; FNV resolve + mismatch; admin/moderator auth; revoked/public/blocked deny; pending→processed/spam; CLEAN/EVENTS one transition; idempotent; conflict; two-copy resolve/edit; buttons removed; edit failure isolation; no mutation rollback; initiator success/partial/storage/malformed feedback; archive non-actionable; delivery once; second poll no dup; `/my_status` + `/delivery_users` regression stubs; AI OFF; client auto-messages=0; no new workflows. Local result: **34/34 PASS**.

## Phase 3D.8.2 actor attribution + revoked list — 49 cases

Required: Admin/moderator display resolution; username + generic fallbacks; callback profile cannot override ACCESS_CONTROL; revoked/public denied; snapshot once; processed/spam cards; multi-copy same label; HTML escape; no raw IDs/hashes on card; LEAD_EVENTS snapshot; name-change immutability; idempotent/conflict non-overwrite; pending+revoked empty-state matrix; public/blocked/Admin/active exclusions; stable code; `/moderators` active-only; one reply; Admin-only; underscores; regressions 35–49. Local runner: `implementation/harness/phase3d82-harness.mjs` — required **49/49 PASS**.

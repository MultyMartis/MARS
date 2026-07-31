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
| `/config` | Shows `parser_version=sm-parser-v3.1` when aligned |
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

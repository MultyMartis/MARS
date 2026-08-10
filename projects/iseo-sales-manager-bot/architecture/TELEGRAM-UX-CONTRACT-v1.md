
## Phase 3H.7.3.1 (2026-08-10)
- Verdict baseline: acceptance-card canonicalization + authoritative instance v1.1
- Root cause: callback status sync used reduced `buildFinalCard`; fixed to full canonical body
- Contract: `iseo-authoritative-card-instance-v1.1`
- Soak: new final 48h restarted (does not reuse 3H.7.3 T+0); Phase 3I.1 blocked; AI OFF
- Evidence: `evidence/phase3h731/`
<!-- Phase 3H.7.3 operator resurface production-parity repair 2026-08-10 -->
## Phase 3H.7.3 (current)

| Field | Value |
|-------|-------|
| **Phase** | 3H.7.3 — Operator resurface production-parity, contact error fix, multi-card sync hardening |
| **Verdict** | `COMPLETE — RESURFACE PARITY REPAIRED; OPERATOR ACCEPTANCE PENDING` |
| **Repairs** | Canonical renderer for resurface · formula-error contact filter · authoritative card registry · semantic ack ≠ sync warning |
| **Acceptance leads** | REAL_REOPEN_A/B/C pending · 12 parity cards · no new LEADS rows |
| **Runtime** | Ops **45** active · Admin **87** active · v2 inactive · AI **OFF** · reminders recipients=4 |
| **Soak** | 3H.7.2 interrupted · Fresh T+0 **2026-08-10 12:44 Europe/Moscow** · earliest T+48 **2026-08-12 12:44 Europe/Moscow** |
| **Evidence** | [evidence/phase3h73/](evidence/phase3h73/) |
| **Report** | [REPORT-iseo-sales-manager-bot-phase3h73-resurface-production-parity-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3h73-resurface-production-parity-v1.md) |
| **Gate** | Phase 3I.1 blocked until soak PASS + operator acceptance |

# TELEGRAM UX CONTRACT v1

**Product:** i-SEO Sales Manager Bot  
**Audience:** managers (Оля v1)  
**Format:** safe plain text **or** carefully escaped HTML — **not** fragile Markdown

> **Phase 3G.2:** For tone, Russian role/status labels, help/start wording, reply-profile surfaces, and fail-closed operator strings, use **[TELEGRAM-TEXT-CONTRACT-v2.md](TELEGRAM-TEXT-CONTRACT-v2.md)** as the text authority. This v1 document remains authoritative for **lead-card block layout** and historical UX deltas.

---

## 1. Goals

- One scannable card per processed lead.
- Human Russian labels only.
- Copy-ready first reply block.
- Clear new / repeat / reprocessed.
- No technical enums, ISO dumps, raw AI JSON, credentials, or internal stack traces.

---

## 2. Required blocks (order)

1. **Header** — Новый лид / Повторный лид / Повторная обработка
2. **Клиент**
3. **Контакты**
4. **Сайт**
5. **Услуга**
6. **Источник** (source + page + campaign if present)
7. **Кратко** (summary)
8. **Качество** (human label only — do not duplicate the label in a trailing comment)
9. **Не хватает** (missing fields; omit when empty)
10. **Следующий шаг** (manager_recommendation)

For complete leads (quality ok, contact present), prefer service-aware guidance:

- Audit → `Связаться с клиентом и уточнить детали аудита.`
- SEO → `Связаться с клиентом и уточнить задачи по продвижению.`
- Other → `Связаться с клиентом и уточнить задачу.`

Do **not** use tautological wording such as `Можно готовить следующий шаг.`
Preserve missing-data / no-contact guidance when fields are incomplete.
11. **Уточняющие вопросы**
12. **История** (only if repeat/possible/reprocessed; human Russian text only)
13. **Режим обработки** (Без ИИ / С ИИ / ИИ не сработал, использован шаблон)
14. **Готовый ответ клиенту** (copy-ready; or no-contact notice when reply cannot be formed)

Optional footer in **development synthetic** cards only: `Тестовая заявка · PHASE 3B.3`  
Production cards: **no** synthetic footer / hashtags.

---

## 3. Label maps

| Internal | Telegram |
|----------|----------|
| `new` | Новый лид |
| `repeat` | Повторный лид |
| `reprocessed` | Повторная обработка |
| `possible` | Возможный повтор (сайт) |
| `Audit` | Аудит |
| `SEO` | SEO |
| `Direct` | Директ |
| `Site` | Сайт |
| `Other` | Другое |
| `ok` | Данных достаточно |
| `needs_data` | Нужны уточнения |
| `poor` | Слабые данные |
| `unusable` / `bad` | Недостаточно для связи |
| `ai_off` / template | Без ИИ |
| `ai_on` / ai | С ИИ |
| `ai_fallback` / fallback | ИИ не сработал, использован шаблон |

Empty values → `—` (not `UNKNOWN`, not blank multi-newlines).

---

## 4. Formatting rules

- Prefer **plain text** with blank lines between blocks.
- If HTML: escape `<`, `>`, `&`; use `<b>` sparingly; no nested entities that Telegram rejects.
- Admin `/help` (Phase 3F.2.2): wrap only slash-commands in `<code>` via `cmdHtml`; keep placeholders like `<номер>` **outside** `cmdHtml` as `&lt;номер&gt;` so Telegram renders `<номер>`. Never substring-patch help lines.
- Do not use Markdown `*` `_` `` ` `` as primary (entity parse failures — MetaBOT lesson).
- Collapse multiple empty lines.
- Dates: `дд.мм.гггг чч:мм`.
- Reply block delimited:

```
──────── Ответ клиенту ────────

...text...

───────────────────────────────
Ответ клиенту автоматически не отправляется.
```

- No-contact / empty reply:

```
Готовый ответ не сформирован: нет контактных данных для связи.
Ответ клиенту автоматически не отправляется.
```

- Do not use raw Markdown fences.
- Do not expose match keys, lead IDs, dedupe keys, or technical enums in История.

---

## 5. Examples

### 5.1 AI OFF — new lead without name

```
Новый лид

Клиент: —
Контакты: +7… (телефон)
Сайт: —
Услуга: Аудит
Источник: форма /audit · utm: yandex / cpc / brand

Кратко: Заявка на аудит без имени и сайта; указан телефон.

Чего не хватает: имя; сайт
Качество: Нужны уточнения — нет имени и сайта
Следующий шаг: Уточнить имя и сайт перед КП; использовать вопросы ниже.

Уточняющие вопросы:
1) Как к вам обращаться?
2) Укажите, пожалуйста, адрес сайта.

Режим обработки: Без AI

——— Скопировать ответ клиенту ———
Здравствуйте!

Спасибо, ваша заявка получена (запрос по аудиту сайта).
Менеджер свяжется с вами, чтобы уточнить задачу.

С уважением,
команда i-SEO
——— Конец ответа ———
Отправляется только вручную. Бот клиенту не пишет.
```

### 5.2 AI ON — new lead with site

```
Новый лид

Клиент: Иван
Контакты: ivan@example.com (email)
Сайт: example.ru
Услуга: SEO
Источник: форма /seo

Кратко: Интерес к продвижению example.ru; нужен контакт для брифа.

Чего не хватает: телефон
Качество: Данные в порядке — можно начинать диалог
Следующий шаг: Подтвердить получение; уточнить регион и текущий трафик.

Уточняющие вопросы:
1) Есть ли удобный телефон для связи?

Режим обработки: AI

——— Скопировать ответ клиенту ———
Здравствуйте, Иван!

Спасибо, ваша заявка получена (запрос по SEO).
Специалист свяжется с вами, чтобы уточнить задачу.

С уважением,
команда i-SEO
——— Конец ответа ———
Отправляется только вручную. Бот клиенту не пишет.
```

### 5.3 Repeat lead

```
Повторный лид

Клиент: Мария
Контакты: +7… · @maria
Сайт: shop.ru
Услуга: Директ
Источник: письмо

Кратко: Повторный интерес к Директу по shop.ru.

Чего не хватает: —
Качество: Данные в порядке
Следующий шаг: Сверить прошлую переписку; не начинать с нуля.

Уточняющие вопросы: —

История:
Был контакт 12.03.2026 14:20 · услуга SEO · кратко: Запрос по продвижению shop.ru

Режим обработки: Без AI
…
```

### 5.4 AI fallback

```
Новый лид
…
Режим обработки: AI недоступен → шаблон
…
```

(Use deterministic summary/reply; no error stack in card. Details go to ERRORS tab.)

---

## 6. Forbidden in manager card

- Raw enums: `UNKNOWN`, `ok`, `Audit` as code, `ai_status=…`, `match=`, `prior=`
- Raw AI JSON
- OpenRouter / credential hints
- Full Gmail message id unless truncated support footer
- `#ERROR!`
- ISO-8601 history strings as the only history line
- Synthetic hashtags (`#leadmsgsyn`, `#lead_msg_syn`, `#lead_…`)
- “Менеджер свяжется с вами” when no usable contact exists
- Duplicate quality labels (`Качество: X — X`)

---

## 7. Destination

- Manager cards → `telegram_manager_chat_id`
- Admin command replies → admin chat / requesting user per Admin contract
- Never client Telegram/email auto-send

---

*Related: AI-OFF-ON-CONTRACT-v1 · LEAD-DATA-MODEL-v1 · ADMIN-COMMAND-CONTRACT-v1 · Phase 3B.3 evidence.*

---

## 8. Phase 3D.3 — `sm-msg-v2` (emoji indicators, copy blocks, inline actions)

**CONFIG `message_format_version` = `sm-msg-v2`.**

### 8.1 Emoji indicators

Primary indicator sits in the card title only; avoid stacking multiple emoji per line.

**Lead type:** 🟢 Новый лид · 🟡 Повторный лид · 🟠 Возможный повтор (сайт) · 🔵 Повторная обработка  
**Lifecycle:** 🕓 Ожидает обработки (pending) · ✅ Обработан (processed) · 🚫 Спам (spam)  
**System:** ✅ success · ⚠️ warning · ❌ error · ℹ️ info · ⚙️ service · 🤖 AI · 📊 stats · 📋 config · 📨 Gmail · 📁 archive

### 8.2 Copy-friendly fields and reply block (`parse_mode=HTML`)

- Contact fields (name / phone / email / messenger / site), when present, render as separate `<code>` inline blocks so managers can tap-to-copy a single value without selecting surrounding text.
- The prepared client reply renders as a single `<pre>` block placed after a manager-only instruction line — copying it yields **only** client-facing text (no internal labels leak into the copied string).
- Tap-to-copy on `<code>`/`<pre>` is a current Telegram mobile/desktop client behavior; long-press copy remains the fallback where tap-to-copy is unavailable.
- Truncation (long cards) prefers preserving manager-facing sections over the reply block.

### 8.3 Inline lifecycle buttons (lead cards only)

Actionable **pending** lead cards carry two inline buttons: **✅ Обработано** and **🚫 Спам** (Phase 3D.8.3 label polish; previously `✅ Отметить обработанным` / `🚫 Отметить как спам`). Callback data is an opaque per-lead token (`sm:p:<token12>` / `sm:s:<token12>`) — no PII, no raw `lead_id` in the visible button. Visible captions and callback actions are separate contracts. Completed-card headings remain **✅ Обработан** / **🚫 Спам** (do not rename the processed final state to the button caption). Archive, admin, and service cards carry **no** lifecycle buttons. After a successful action the source card message is edited (buttons cleared) rather than a new message sent; see [ADMIN-COMMAND-CONTRACT-v1.md](ADMIN-COMMAND-CONTRACT-v1.md) §7 for callback routing and idempotency.

### 8.4 Forbidden (unchanged, reasserted for 3D.3)

No opaque token collisions surfaced as PII; no raw `lead_id`/dedupe keys in button labels or answer toasts; no automatic client-facing send triggered by a manager button.

### 8.5 Phase 3D.3.1 — invalid contact suppression + archive multi-card

- Never render Sheets formula errors or placeholders (`#ERROR!`, `#VALUE!`, `#REF!`, `#N/A`, `Formula parse error`, `UNKNOWN`, bare `44`) as phone/email/messenger/site.
- Omit the invalid field; archive cards may show `⚠️ Контакт в архивной записи повреждён` when useful.
- `/leads` must emit **one Telegram message per selected archive card** with correct ordinals; do not collapse to the first item.
- Archive footer: `ℹ️ Архивная копия. Статус меняется только в исходной карточке.`

---

## 9. Phase 3D.4 — `sm-msg-v2.1` (reduced emoji density)

**CONFIG `message_format_version` = `sm-msg-v2.1`.**

Builds on §8 (`sm-msg-v2`) with **lower emoji density** on manager lead cards:

- Title lead-type emoji (🟢🟡🟠🔵) and lifecycle emoji (🕓✅🚫) **unchanged**.
- Section labels (Качество, Следующий шаг, Не хватает, …) render **without** prefix emoji.
- Archive footer may use a **single** ℹ️; no stacked section indicators.
- Target: **max 2** emoji on standard (non-archive) cards — title + lifecycle line.

Copy-friendly `<code>` fields, `<pre>` reply block, and inline lifecycle buttons unchanged from §8.

---

## 10. Phase 3D.4 — parser-driven card semantics (`sm-parser-v3.2`)

Parser upgrades affect card content (not layout):

- **`t.me/…` / `@handle` in site field** → classified as **messenger**, not site.
- **Contact method inference** from «Способ связи» + value shape.
- **Comment semantics** — «в тг» and equivalents reinforce Telegram preference.
- **Source page normalization** — `/free-audit/` → `free-audit` in «Источник» line.

See `evidence/phase3d4/` and `knowledge/WEBSITE-FORM-FORMATS-v1.md`.


---

## Phase 3D.5 UX

- Public welcome/help texts are informational only (no production/AI/lead/Admin leakage).
- Moderator start/help explain cards + irreversible status.
- Admin help includes **Пользователи** registry section.
- Callback deny: `Недостаточно прав для изменения статуса.`
- message_format_version: **sm-msg-v2.2**


## Phase 3D.5.1 — Access registry population and SoT repair

- **ACCESS_CONTROL** is the primary authorization authority (Telegram user ID keyed; username informational only).
- `manager_action_user_ids` is legacy and is **not** an active moderator authority after registry acceptance.
- `admin_user_ids` remains recovery-only Admin bootstrap when ACCESS_CONTROL cannot be read technically.
- A revoked/blocked ACCESS_CONTROL row always overrides CONFIG allowlists.
- ACCESS_EVENTS append mapping must reference Prepare Access Upsert fields (never post-Upsert `` metadata).
- Evidence: `evidence/phase3d51/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3d51-access-registry-repair-v1.md`.

## Phase 3D.5.2 — One-response invariant

Every Admin text command must produce exactly one Telegram reply. Silence after a received update is an incident. Service-unavailable and processing-failure copy must be operator-safe (no raw IDs, no stack traces).

## Phase 3D.6 — Personal access UX
- `/my_status` is available to public, pending, active moderator/Admin, revoked and blocked users; it never exposes another user’s identity or registry row.
- Show command names in HTML `<code>` tags, including `<code>/my_status</code>`, to preserve underscores.
- Active moderator text confirms card and callback capability but not Admin settings.
- Revoked text says public commands remain available; blocked text is only `Доступ к боту ограничен.`
- Grant notification: `Вам выданы права модератора Sales Manager.` followed by card-action rights and `/start`/`/help`.
- Revoke notification: `Ваши права модератора Sales Manager отозваны.` followed by retained `/start`, `/help`, `/my_status`.
- Successful `/my_status` after a role change proves ACCESS_CONTROL state; it does not by itself prove grant/revoke notification delivery.

---

## Phase 3D.7 — multi-recipient cards

- Every eligible active Admin/moderator receives the same manager-facing card in their **private** bot chat.
- Inline buttons remain only while `manager_status=pending`.
- Lifecycle actions synchronize all delivered copies; first valid transition wins.
- Public users never receive production lead cards.

## Phase 3D.8 — action-button payload repair

For an actionable pending card, Format must emit `telegram_has_buttons=true`, `telegram_callback_processed=sm:p:<token12>`, `telegram_callback_spam=sm:s:<token12>`, and preserve `telegram_reply_markup` through recipient expansion and claim restore. Archive `/leads` cards remain buttonless. This is a Format contract repair; Parser 3.2 is unchanged.

## Phase 3D.8.1 — live callback acknowledgement and multi-copy feedback

- Early `answerCallbackQuery`: valid action → `Обрабатываю…`; malformed → `Не удалось распознать действие.`; deny → `Недостаточно прав для изменения статуса.`
- Final durable texts: processed / spam / idempotent / conflict / not-found / storage / partial-copy (see evidence/phase3d8-1/).
- Final card status includes `Кем: <safe actor label>` + Moscow timestamp; buttons removed on all delivered copies.
- Multi-copy sync requires durable `LEAD_DELIVERIES` rows (`stable_lead_ref` + message refs).
- Operator two-role acceptance clicks closed Phase 3D.8.1 COMPLETE.

## Phase 3D.8.2 — actor attribution

- Actor label comes from ACCESS_CONTROL (`display_name`, then `@username`, else `сотрудник`).
- Optional combined form: `Display Name · @username` when concise and non-duplicative.
- Snapshot at apply time is stored in LEAD_EVENTS `detail` and shown identically on all synchronized card copies.
- Callback profile names must not override ACCESS_CONTROL attribution.

## Phase 3E.1 — `sm-msg-v2.3` + semantic site/reply

**CONFIG `message_format_version` = `sm-msg-v2.3`** (paired with `sm-parser-v3.3`) — superseded for new cards by 3E.2 below; historical rows remain readable.

- **Сайт** block reflects `website_state`: provided / explicitly absent / alternative contact / invalid / missing — messenger handles never under Сайт.
- First-reply block follows [FIRST-REPLY-RULES-v1.md](FIRST-REPLY-RULES-v1.md) (no unsupported facts; no auto-send).
- Pending buttons remain **`✅ Обработано`** / **`🚫 Спам`**; callbacks unchanged.
- Authority: [PARSER-3.3-CONTRACT-v1.md](PARSER-3.3-CONTRACT-v1.md) · [LEAD-SEMANTIC-MODEL-v1.md](LEAD-SEMANTIC-MODEL-v1.md).

## Phase 3E.2 — `sm-msg-v2.4` + First Reply Engine v2

**CONFIG `message_format_version` = `sm-msg-v2.4`** · **`first_reply_version` = `sm-reply-v2.0`**.

- Copy heading: `✉️ Ответ клиенту — нажмите, чтобы скопировать` with HTML-escaped `<pre>`; disclaimer outside.
- Test suppression / damaged-contact wording per [MANAGER-CARD-v2.4-CONTRACT-v1.md](MANAGER-CARD-v2.4-CONTRACT-v1.md).
- Known-information guard: [KNOWN-INFORMATION-GUARD-v1.md](KNOWN-INFORMATION-GUARD-v1.md).
- Engine: [FIRST-REPLY-ENGINE-v2.md](FIRST-REPLY-ENGINE-v2.md).
- Buttons/callbacks unchanged.

## Phase 3F.1 — pending-lead view and reminder texts (Admin.dev, read-only)

These are **command replies**, not lead cards — no lifecycle buttons, no `<pre>` copy block.

- `/pending_count` — one or two lines: total count, then a non-zero age-bucket summary (`до 2 часов: X · 2–24 часа: Y · старше суток: Z`). Zero state: `Необработанных заявок сейчас нет.`
- `/pending_leads [page] [test]` — numbered HTML-escaped entries (`N. <age> · <name>` / `<service> · <site>` / `<summary>` / `Черновик ответа: готов|нет`), footer `Страница P из PC · всего T`.
- `/reminder_status` — moderator sees a 4-line status/time/timezone summary; Admin sees the extended form (min count, test-inclusion, last window, last success, last pending count, last recipient count, last safe error).
- Reminder message (`formatReminderMessage`) — `⏰ Напоминание о заявках`, total count, over-24h count when present, oldest-age line, pointer to `/pending_leads`, and an "oldest first" nudge when any lead is over 24h old.
- All pending/reminder text reuses existing fallback vocabulary (`Без имени`, `Контакт не указан`, `Сайт не указан`, `Задача требует уточнения`) — no new placeholder terms invented.
- Same forbidden list as §6 applies: no raw enums, no lead ids, no Telegram/chat identifiers, no `#ERROR!`.

See `implementation/PENDING-COMMANDS-v1.md`, `implementation/REMINDER-CONFIG-COMMANDS-v1.md`, and `evidence/phase3f1/` for full acceptance detail.


## Phase 3G.1 UX

- Copy heading remains copy-to-clipboard customer block only.
- Manager guidance (`💡 Подсказка менеджеру`) **outside** `<pre>`.
- Per-recipient intro uses approved first name (ADMIN_A→Андрей, MOD_A→Михаил).
- Missing name: warning on card; no unsafe draft; not a delivery failure.
- Admin reply-profile commands; moderator `/my_reply_profile` view-only.
- No auto-send. Live UX acceptance: pending or in progress (historical 3G.1/3G.1.1 gate).

## Phase 3G.2 UX / text delta

- Profile addressing by immutable number (`reply_profile_number`); see [REPLY-PROFILE-NUMBERING-v1.md](REPLY-PROFILE-NUMBERING-v1.md).
- Text tone/labels/formats: [TELEGRAM-TEXT-CONTRACT-v2.md](TELEGRAM-TEXT-CONTRACT-v2.md).
- Help templates: [ROLE-AWARE-HELP-BUILDER-v2.md](../implementation/ROLE-AWARE-HELP-BUILDER-v2.md) — Admin includes profile section; moderator only `/my_reply_profile`.
- Command inventory: [TELEGRAM-COMMAND-REFERENCE-v1.md](../guides/TELEGRAM-COMMAND-REFERENCE-v1.md).


### Phase 3H.7 delta
See evidence/phase3h7 and LEAD-REOPEN-CONTRACT-v1.


## Terminal reopen action
Inline button `↩️ Вернуть в обработку` (`sm:r:`) on terminal original + archive cards.

## Phase 3H.7.2 note
Callback acknowledgement contract `iseo-lead-callback-ack-v1.0` deployed. Reopen ack is «Лид возвращён в обработку.». Aggregate no longer maps pending applied→processed. Operator-approved resurface of three genuine leads completed for acceptance; global reopen still does not fan out. Soak restarted; Phase 3I.1 blocked. See `evidence/phase3h72/`.


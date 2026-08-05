# HUMAN REPLY STYLE v1

**Product:** i-SEO Sales Manager Bot  
**Version:** `sm-human-v1.0`  
**Layered on:** First Reply Engine **`sm-reply-v2.1`** (unchanged in Phase 3E.2.3)
**Status:** IMPLEMENTED; **operator-accepted**; no redesign in Phase 3E.2.3
**Runtime lib:** `implementation/runtime-libs/first-reply-engine-v2.mjs`  
**AI:** OFF — deterministic templates only  
**Delivery:** manager draft for Оля (PER-0010) — **never** auto-sent to customer

---

## Purpose

Produce copy-ready first replies that read like a human manager wrote them — not like a parser narrating its own decisions. Human Reply Style v1 is a **presentation layer** on top of the existing guard rails and service branching in First Reply Engine v2.1.

**Documented architecture** (this file + runtime lib). **Live parity** depends on Operational.dev patch acceptance — treat harness PASS as implementation evidence, not operator sign-off.

---

## Principles (Оля draft voice)

1. **Natural greeting** — `Здравствуйте, <Имя>!` when name is usable; otherwise `Здравствуйте!`
2. **Acknowledge the real request** — mirror service + meaningful theme from comment; do not invent urgency or guarantees
3. **Ask only what is still unknown** — known-info guard suppresses questions silently (see [KNOWN-INFORMATION-GUARD-v1.md](KNOWN-INFORMATION-GUARD-v1.md))
4. **Never narrate internals** — no parser states, guard codes, form provenance, or «мы учли ваш комментарий»
5. **Compact question groups** — ≤3; numbered list only when >1 question
6. **No work-started / pricing / ranking promises** — same invariants as v2.0
7. **Closing block** — `С уважением,` / `команда i-SEO`
8. **Card disclaimer stays outside copy** — `Ответ клиенту автоматически не отправляется.`

---

## Silent known-info guard

When the Lead Semantic Model already contains a fact, the engine **drops** the matching question — it does **not** tell the customer that the fact was already known.

| Wrong (forbidden) | Right (silent) |
|---|---|
| «Адрес сайта уже указан, повторно присылать не нужно» | Acknowledge site in greeting; ask audit/SEO focus instead |
| «Текущий сайт не указан — это ожидаемо для задачи» | «Поняли, что вам нужен новый сайт» + business/feature questions |
| «Мы учли ваш комментарий по данным формы» | Natural paraphrase: «Поняли, что проблема связана со снижением конверсии в корзине» |

Suppression reason codes remain in `first_reply_reason_codes` for diagnostics only — **not** shown in customer copy or manager card body.

---

## Forbidden system phrases

Matched by `FORBIDDEN_PHRASE_PATTERNS` in runtime lib. Any hit → quality linter FAIL → `first_reply_ready=false`.

Representative patterns (not exhaustive):

- «адрес сайта уже указан» / «повторно присылать не нужно»
- «текущий сайт не указан» / «это ожидаемо для задачи»
- «адрес существующего сайта не нужен»
- «мы учли ваш комментарий» / «по данным формы»
- «система определила» / «поле отсутствует» / «недостающие поля»
- «контакт нормализован»
- Internal tokens: `website_state`, `resolved_service`, `parser`

Also forbidden: «напишем вам в Telegram» (auto-send implication).

Full linter contract: [FIRST-REPLY-QUALITY-LINTER-v1.md](FIRST-REPLY-QUALITY-LINTER-v1.md).

---

## Example branches (harness fixtures)

### Cart / conversion (meaningful audit comment)

**Input:** Audit form, site provided, comment «падает конверсия на корзине, нужна проверка»  
**Theme:** `conversion_cart`  
**Draft shape:** greeting → thanks for audit request + site → «Поняли, что проблема связана со снижением конверсии в корзине» → when/changes/analytics questions  
**Must NOT ask:** generic «приоритетные страницы» / «какой результат аудита»

### Vague audit

**Input:** Audit form, site provided, comment «нужно проверить сайт»  
**Theme:** `vague_service`  
**Draft shape:** natural focus question — «что сейчас беспокоит больше всего: технические ошибки, позиции…»

### Website development

**Input:** Development form, `website_state=explicitly_absent`, «Нужен новый сайт для компании»  
**Draft shape:** «Поняли, что вам нужен новый сайт» → business / features / examples  
**Must NOT say:** «текущий сайт не указан»

### Website development + SEO

**Input:** Development form, no site, «Нужен новый сайт и затем SEO продвижение»  
**Draft shape:** acknowledge both stages in one sentence → business, features, region  
**Must NOT ask:** current-site URL

### SEO (minimal comment)

**Input:** SEO form, site provided, comment «seo»  
**Draft shape:** thanks + site → region + priority products/services

### Telegram alternative contact

**Input:** comment or alt contact indicates Telegram preference  
**Draft shape:** «Учли, что вам удобнее общаться в Telegram» — **without** promising the bot will message first  
**Must NOT ask:** Telegram handle if already known

---

## Outputs (additive fields)

| Field | Value |
|-------|-------|
| `first_reply_version` | `sm-reply-v2.1` |
| `human_reply_style_version` | `sm-human-v1.0` |
| `meaningful_theme` | theme code from [MEANINGFUL-COMMENT-BRANCHING-v1.md](MEANINGFUL-COMMENT-BRANCHING-v1.md) |
| `quality_linter_ok` | boolean |
| `quality_linter_failures` | failure codes when blocked |

---

## Related

- [FIRST-REPLY-ENGINE-v2.md](FIRST-REPLY-ENGINE-v2.md)
- [MEANINGFUL-COMMENT-BRANCHING-v1.md](MEANINGFUL-COMMENT-BRANCHING-v1.md)
- [FIRST-REPLY-QUALITY-LINTER-v1.md](FIRST-REPLY-QUALITY-LINTER-v1.md)
- [KNOWN-INFORMATION-GUARD-v1.md](KNOWN-INFORMATION-GUARD-v1.md)
- Evidence: `evidence/phase3e2-1/HARNESS-RESULTS-v1.md` (64/64 PASS)

## Phase 3E.2.3 status note

This phase changes Sheets request economics and delivery safety only. Voice, branching, linter and manual-copy boundary remain unchanged. Final operator visual confirmation concerns the delivered proof card, not redesign approval.

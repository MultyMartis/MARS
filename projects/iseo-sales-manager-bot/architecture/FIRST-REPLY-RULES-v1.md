# FIRST REPLY RULES v1

**Product:** i-SEO Sales Manager Bot  
**Status:** **IMPLEMENTED** Phase 3E.1 (deterministic AI OFF templates in `sm-parser-v3.3` / processor)  
**Message card:** `sm-msg-v2.3`  
**Related:** [LEAD-SEMANTIC-MODEL-v1.md](LEAD-SEMANTIC-MODEL-v1.md) · research draft [FIRST-REPLY-CONSISTENCY-RULES-v1.md](../research/parser-3.3/FIRST-REPLY-CONSISTENCY-RULES-v1.md)

---

## Hard rules

1. Reply uses **resolved intent** only (precedence in Lead Semantic Model).
2. Do **not** mention site, name, budget, deadline, channel, or service **unless** present as resolved facts.
3. `website_state=explicitly_absent` must **not** become «укажите адрес сайта», if the task is site creation / no-site consultation.
4. Alternative contact (Telegram/WhatsApp) is a **contact channel**, never a website line.
5. On `intent_conflict=true` → neutral clarification ask; do not invent a winner service.
6. Manager-only notes, internal states, provenance, IPs, hashes → **never** in client copy.
7. AI OFF template is the production baseline; future AI ON must pass the same consistency checks and fall back on failure.
8. Reply is **copy-ready for managers only** — never auto-sent to clients.
9. Telegram card must still state that the reply is not sent automatically.

---

## Service-aware missing prompts (examples)

| Intent | Prefer asking (when missing) |
|--------|------------------------------|
| Audit | детали аудита / фокус страниц — **not** «есть ли сайт» if site `provided` |
| SEO | задачи продвижения — **not** re-ask known site |
| WebsiteDevelopment | тип бизнеса / функциональность — **not** «пришлите URL» when explicitly absent |
| Other / conflict | нейтральное уточнение задачи |

---

## Card coupling (`sm-msg-v2.3`)

- Block **Готовый ответ клиенту** = `first_reply_text` (HTML-escaped / `<pre>` as per formatter).
- Site block reflects `website_state` (provided / explicitly absent / alternative / invalid / missing) without leaking messenger under **Сайт**.
- Quality line uses human labels; do not dump enums.

---

## Regression anchors

Harness checks H19–H21, H25–H26, H41 (and P33 reply cases) in `implementation/harness/phase3e1-harness.mjs`.

# FIRST REPLY RULES v1

**Product:** i-SEO Sales Manager Bot  
**Status:** **EXTENDED** by Phase 3E.2.1 Human Reply Style v1 (`sm-reply-v2.1` / `sm-human-v1.0`)  
**Message card:** `sm-msg-v2.4`  
**Authoritative engine:** [FIRST-REPLY-ENGINE-v2.md](FIRST-REPLY-ENGINE-v2.md) · [HUMAN-REPLY-STYLE-v1.md](HUMAN-REPLY-STYLE-v1.md) · [KNOWN-INFORMATION-GUARD-v1.md](KNOWN-INFORMATION-GUARD-v1.md) · [FIRST-REPLY-QUALITY-LINTER-v1.md](FIRST-REPLY-QUALITY-LINTER-v1.md)  
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

## Card coupling (`sm-msg-v2.4`)

- Block **✉️ Ответ клиенту — нажмите, чтобы скопировать** = `first_reply_text` (HTML-escaped / `<pre>` as per formatter).
- Site block reflects `website_state` without leaking messenger under **Сайт** and without narrating guard logic to the customer.
- Missing-info labels are human-readable; internal reason codes stay machine-only.
- Damaged contact: one next-step + one suppression warning — no duplicate wording.

---

## Regression anchors

Harness Phase 3E.2.1: `implementation/harness/phase3e21-harness.mjs` (64 checks). Prior parser cases remain in `phase3e1-harness.mjs`.

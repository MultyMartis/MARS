# COMMENT SEMANTICS v1

**Phase:** 3D.4  
**Parser:** `sm-parser-v3.2`

---

## 1. Purpose

Use free-text «Комментарий» / «Сообщение» to reinforce contact preference when structured fields are ambiguous — especially **«в тг»** (Telegram preference).

---

## 2. Keyword patterns (case-insensitive, RU)

| Pattern | Effect |
|---------|--------|
| `в тг`, `в телеграм`, `в telegram`, `напишите в тг`, `свяжитесь в тг` | Prefer **messenger** (Telegram) for primary contact |
| `позвоните`, `лучше звонить`, `по телефону` | Prefer **phone** |
| `на почту`, `ответьте на email`, `пишите на` | Prefer **email** |
| `whatsapp`, `в вотсап` | Prefer **phone** (WhatsApp uses phone number) |

Keywords apply only when they do not contradict an explicit «Способ связи» value.

---

## 3. «в тг» preference rule

When comment contains «в тг» (or equivalent) **and**:

- contact field has `@handle` or `t.me/…` → classify as **Telegram messenger** (primary)
- contact field has phone only → keep phone; append summary note «Клиент просит связь в Telegram — уточнить @»
- contact field empty → set `missing_fields` to include messenger; quality `needs_data`

Do **not** invent a handle from comment text alone.

---

## 4. Summary integration

Detected preference may shorten `summary` / `manager_recommendation`:

- «Клиент просит связь в Telegram.»
- «Предпочитает звонок.»

Keep summary factual — no fabricated handles or numbers.

---

## 5. Synthetic example

**Input (synthetic form body):**

```text
Способ связи: телефон
Контакт: +7900…
Комментарий: лучше писать в тг @synth_client_01
```

**Parsed:**

| Field | Value |
|-------|-------|
| phone | +7900… (synthetic) |
| messenger | @synth_client_01 |
| contact_type | mixed |
| summary | … «Клиент просит связь в Telegram.» |

---

## 6. Acceptance

| Case | Result |
|------|--------|
| «в тг» + @ in comment | messenger extracted from comment adjunct |
| «в тг» without handle | needs_data; no invented handle |
| Explicit email method overrides «в тг» in comment | email wins |
| No comment | unchanged v3.1 behavior |

---

*Related: CONTACT-METHOD-INFERENCE-v1 · MESSENGER-SITE-SEMANTIC-FIX-v1.*

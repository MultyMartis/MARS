# CONTACT METHOD INFERENCE v1

**Phase:** 3D.4  
**Parser:** `sm-parser-v3.2`

---

## 1. Purpose

Deterministically map website-form «Способ связи» and «Контакт» fields to `phone` / `email` / `messenger` / `mixed` without inventing values.

---

## 2. Primary signals (priority order)

| Priority | Signal | Maps to |
|----------|--------|---------|
| 1 | Explicit «Способ связи» label | Declared method wins for the contact field |
| 2 | Value shape | phone / email / `@handle` / `t.me/…` grammar |
| 3 | Comment body keywords | «в тг», «telegram», «whatsapp», «позвоните» (see COMMENT-SEMANTICS-v1) |
| 4 | Field name fallback | «Телефон» → phone; «Email» → email |

First confident match wins; do not duplicate the same token across phone and messenger.

---

## 3. Inference table

| «Способ связи» (normalized) | «Контакт» example (synthetic) | `contact_type` | Field populated |
|-----------------------------|-------------------------------|----------------|-----------------|
| телефон / phone | `+7900…` (masked pattern) | phone | `phone` |
| email / почта | `user@example.com` | email | `email` |
| telegram / тг / в телеграм | `@synth_handle` | messenger | `messenger` |
| telegram / тг | `t.me/synth_user` | messenger | `messenger` |
| (empty) + email-shaped contact | `user@example.com` | email | `email` |
| (empty) + phone-shaped contact | `+7900…` | phone | `phone` |
| (empty) + `@handle` | `@synth_handle` | messenger | `messenger` |
| whatsapp | `+7900…` | phone | `phone` (+ note in summary if needed) |

---

## 4. Rejected placeholders

Never infer contact from:

- `44`, `UNKNOWN`, `#ERROR!`, `#VALUE!`, `#N/A`
- bare domain in contact field when site field empty (route to site inference instead)
- `t.me/…` in site field (route to messenger — MESSENGER-SITE-SEMANTIC-FIX-v1)

---

## 5. `primary_contact` selection

Best available in order: **phone → email → messenger** when multiple present; `mixed` when two+ usable with no clear primary from «Способ связи».

---

## 6. Acceptance

| Case | Result |
|------|--------|
| Explicit Telegram method + `@handle` | messenger populated; site empty |
| Empty method + email contact | email |
| Empty method + phone contact | phone |
| Conflicting method vs shape | explicit method wins; shape validated |
| Placeholder contact | field omitted; quality degraded appropriately |

---

*Related: MESSENGER-SITE-SEMANTIC-FIX-v1 · COMMENT-SEMANTICS-v1 · SUPPLIED-FORM-END-TO-END-v1.md.*

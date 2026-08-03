# SUPPLIED FORM END TO END v1

**Phase:** 3D.4  
**Form:** free-audit (synthetic supplied fixture)  
**Versions:** `sm-parser-v3.2` · `sm-msg-v2.1`

---

## 1. Synthetic supplied input (email body excerpt)

All values fictional — no real clients.

```text
Тема: Заявка на бесплатный аудит

От кого: Synth Client Alpha
Способ связи: Telegram
Контакт: @synth_client_alpha
Телефон: 
Email: 
Адрес сайта: t.me/synth_client_alpha
Комментарий: интересует аудит, лучше писать в тг
Отправлено со страницы: /free-audit/
```

---

## 2. Before (v3.1 + sm-msg-v2) — expected card semantics

| Block | Value |
|-------|-------|
| Title | 🟢 Новый лид |
| Клиент | Synth Client Alpha |
| Контакты | — (messenger lost) |
| Сайт | `t.me/synth_client_alpha` ← **wrong** |
| Услуга | Аудит |
| Источник | форма /free-audit/ (verbose path) |
| Качество | needs_data (no usable contact) |
| Lifecycle | 🕓 Ожидает обработки |

**Defects:** messenger/site swap; contact missing; page not normalized.

---

## 3. After (v3.2 + sm-msg-v2.1) — expected card semantics

| Block | Value |
|-------|-------|
| Title | 🟢 Новый лид |
| Клиент | `<code>Synth Client Alpha</code>` |
| Контакты | `<code>@synth_client_alpha</code>` (мессенджер) |
| Сайт | — |
| Услуга | Аудит |
| Источник | бесплатный аудит · форма free-audit |
| Кратко | Заявка на аудит; клиент просит связь в Telegram. |
| Качество | Данных достаточно |
| Следующий шаг | Связаться с клиентом и уточнить детали аудита. |
| Lifecycle | 🕓 Ожидает обработки |
| Emoji density | title + lifecycle only (no section-prefix emoji) |
| Buttons | ✅ Отметить обработанным · 🚫 Отметить как спам |

---

## 4. CLEAN row expectations (synthetic)

| Column | After value |
|--------|-------------|
| `parser_version` | sm-parser-v3.2 |
| `message_format_version` | sm-msg-v2.1 |
| `service` | Audit |
| `source_page` | free-audit |
| `messenger` | @synth_client_alpha |
| `site` | (empty) |
| `contact_type` | messenger |
| `quality_status` | ok |
| `lifecycle_status` | pending |

---

## 5. Pipeline gates (unchanged)

- AI OFF — no OpenRouter call.
- Telegram card sent to manager chat — not to client.
- Gmail PROCESSED only after Telegram success.
- Synthetic row tagged if injected via harness — excluded from prod `/stats`.

---

## 6. Acceptance

| Check | Result |
|-------|--------|
| End-to-end harness with supplied fixture | **PASS** |
| Live Gmail replay of same fixture | not required this phase |
| Manager enrollment required for button tap | Olya hash authorized (synthetic callback PASS) |

---

*Related: knowledge/WEBSITE-FORM-FORMATS-v1.md · MULTI-FORM-TEST-PLAN-v1.md.*

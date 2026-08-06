# AI_COMMENT Contract

**Status:** FROZEN DOCUMENTATION SEMANTICS / PHASE 0A  
**Runtime:** NOT IMPLEMENTED  
**Enablement:** Phase 2 (after Phase 1 SIMPLE)

---

## 1. Role

AI is an **optional commentary layer** only.

- No authority over facts, severity, actions, or production decisions.
- AI input is derived from the **normalized envelope**, never from raw monitor artifacts.
- AI output appears **after** the immutable SIMPLE fact block.
- AI failure must not block SIMPLE delivery.

---

## 2. Normalized safe AI input shape

```json
{
  "status": "ATTENTION",
  "summary_code": "ONBOARDING_REQUIRED",
  "baseline_count": 1737,
  "current_count": 1817,
  "added_urls": 80,
  "removed_urls": 0,
  "onboarding_needed_count": 4,
  "operator_action": "Проверить новые ветки каталога"
}
```

| Rule | Detail |
|------|--------|
| Source | Derived from normalized envelope only |
| Never receive | Raw monitor artifacts, raw paths, raw logs, credentials, chat IDs |
| Counts | Exact envelope integers only |

---

## 3. Allowed output

- One short optional commentary paragraph.
- Must not contradict SIMPLE facts.
- Must not introduce new numbers.
- Displayed after immutable SIMPLE block.

---

## 4. Prohibited AI behavior

AI is forbidden to:

- change status
- reinterpret severity
- change action
- add numbers
- alter counts
- infer undocumented causes
- claim the 1C import caused a change unless source facts explicitly say so
- recommend baseline refresh
- recommend production writes
- recommend automatic remediation
- claim the site is healthy when `site_status` is BLOCKED
- expose technical evidence
- invent next steps

---

## 5. Fallback / timeout / failure

| Condition | Behavior |
|-----------|----------|
| AI failure | Fall back immediately to SIMPLE |
| Timeout | Fall back immediately to SIMPLE |
| Malformed response | Fall back immediately to SIMPLE |
| Empty response | Fall back immediately to SIMPLE |
| Waiting | SIMPLE must **not** wait indefinitely for AI |

`ai_status` becomes `FAILED` (or remains `DISABLED` / `NOT_REQUESTED` as applicable). `site_status` unchanged. `delivery_status` for SIMPLE unchanged by AI outcome.

---

## 6. Sanitized examples

### Allowed commentary (illustrative)

> Кратко: зафиксирован ненулевой onboarding-сигнал по каталогу; действуйте по указанному action в блоке фактов.

### Forbidden commentary examples

- “Сайт в порядке” when status is BLOCKED
- “Обновите baseline” / “Сделайте FTP/DB правку”
- “1C точно вызвал +80” without explicit source fact
- Any pasted path, token, or chat id

---

## 7. Future enablement gate

AI_COMMENT may be enabled only after:

1. Phase 1 SIMPLE path proven in sandbox/internal.
2. Operator explicitly enables AI for Client Ops.
3. Provider credentials remain outside Git (n8n/host only) — MetaBOT pattern: `projects/metabot-seo-content-agent/integration-boundary.md`.
4. Prompt/output filters enforce this contract.

Phase 0A creates **no** OpenRouter credentials and performs **no** AI API calls.

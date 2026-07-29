# SOURCE SANITIZATION MANIFEST v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A  
**Status:** **Contract defined** · **Execution blocked** (no source exports present)

---

## 1. Policy

| Rule | Detail |
|------|--------|
| Git | Only sanitized artifacts under `projects/iseo-sales-manager-bot/baselines/` |
| Raw | Stay in `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\raw\` — never commit |
| XLSX | Never copy into Git; emit schema markdown with **synthetic** examples only |
| Secrets | Never invent fake usable secrets; use placeholders only |

---

## 2. Workflow JSON — remove / redact

| Class | Action |
|-------|--------|
| Authorization header values | Redact → placeholder or empty |
| API keys / tokens | Redact |
| Webhook URLs containing secrets | Redact path/query secrets |
| Credential ids (if policy requires) | Replace with type/name placeholders |
| Telegram chat ids (unnecessary) | `<MANAGER_CHAT_ID>` / `<ADMIN_CHAT_ID>` |
| Google document ids (unnecessary) | `<RAW_WORKBOOK_ID>` / `<CLEAN_WORKBOOK_ID>` |
| `instanceId` | Remove |
| `pinData` | Remove |
| Execution / staticData with PII | Remove |
| Personal lead data / customer examples | Remove or replace with synthetic |
| OpenRouter credential material | Never discuss; placeholder `<OPENROUTER_CREDENTIAL>` only |

---

## 3. Workflow JSON — preserve

| Element | Preserve |
|---------|----------|
| Node names | Yes |
| Node types | Yes |
| `typeVersion` | Yes |
| Positions | Yes |
| Connections | Yes |
| Expressions | Yes (scrub inline secrets if any) |
| Parameter structure | Yes |
| Credential type / name placeholders | Yes |
| Workflow settings | Yes |
| `active` state | Yes (as evidence) |
| Safe version metadata | Yes |

---

## 4. Placeholder vocabulary (mandatory)

| Placeholder | Meaning |
|-------------|---------|
| `<OPENROUTER_CREDENTIAL>` | OpenRouter credential binding |
| `<GMAIL_CREDENTIAL>` | Gmail credential binding |
| `<GOOGLE_SHEETS_CREDENTIAL>` | Sheets credential binding |
| `<TELEGRAM_CREDENTIAL>` | Telegram credential binding |
| `<RAW_WORKBOOK_ID>` | RAW workbook document id |
| `<CLEAN_WORKBOOK_ID>` | CLEAN workbook document id |
| `<MANAGER_CHAT_ID>` | Manager Telegram chat |
| `<ADMIN_CHAT_ID>` | Admin Telegram chat |
| `<INCOMING_GMAIL_LABEL_ID>` | Incoming leads label |
| `<PROCESSED_GMAIL_LABEL_ID>` | Processed label |
| `<ERROR_GMAIL_LABEL_ID>` | Error label |

---

## 5. Execution status (this wave)

| Step | Status |
|------|--------|
| Locate raw exports | **FAIL** — missing |
| Run sanitizer | **SKIPPED** |
| Produce `Sales-Manager-v*.sanitized.json` | **BLOCKED** |
| Produce XLSX schema baselines from real headers | **BLOCKED** |
| Contract documentation | **DONE** (this file) |

---

## 6. Post-drop procedure (operator / next wave)

1. Operator drops files into STORAGE `raw/`.
2. Sanitizer produces STORAGE `sanitized/` copies.
3. Security review: no secrets / PII / real workbook ids if policy redacts.
4. Promote allowlisted sanitized files into `baselines/`.
5. Generate V1/V2 comparison + node inventory + connection map from sanitized JSON.
6. Separate commit wave if required.

---

*Phase 3A does not fabricate workflow JSON from memory.*

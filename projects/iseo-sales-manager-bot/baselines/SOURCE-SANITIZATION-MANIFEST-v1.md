# SOURCE SANITIZATION MANIFEST v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A.1  
**Status:** **Executed** — sanitized baselines Git-eligible

---

## 1. Policy

| Rule | Detail |
|------|--------|
| Git | Only sanitized artifacts under `projects/iseo-sales-manager-bot/baselines/` |
| Raw | Remain in `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\raw\` |
| XLSX | Never copy into Git; emit schema markdown with synthetic examples only |
| Secrets | Never invent usable secrets; placeholders only |

---

## 2. Workflow sanitization records

| Raw filename | Raw SHA256 | Sanitized filename | Sanitized SHA256 | Git eligible |
|--------------|------------|--------------------|------------------|--------------|
| `Sales-Manager-v1 json.txt` | `05D923CA6A3CDD34E52D0A6D10FF4CAC53DBF7AF550AEA0BC97C2D537F598411` | `Sales-Manager-v1.sanitized.json` | `A1C9FD0607E9D7F6866CF491EFF7673070DC3BD3AE2703E6E65EF1212A915EB5` | **YES** |
| `Sales-Manager-v2 json.txt` | `F9C2E268C10BD10C45D168133602C9495600F65DDAA88A0F0C34B522C54267DF` | `Sales-Manager-v2.sanitized.json` | `AD90715FD14B6F8EF568BCBD69CC0F123D41FF024296AD3E54D3B9FD11AB821C` | **YES** |

### Sanitization actions (both)

- Workflow `id` → `<WORKFLOW_INSTANCE_ID>`
- `versionId` redacted
- Removed `pinData`, `meta` (and non-essential API blobs when present)
- Credential ids → `<CREDENTIAL_ID_REDACTED>`; names → type placeholders
- Inline `Authorization` headers → `Bearer <REDACTED_TOKEN>`
- Spreadsheet document ids → `<RAW_WORKBOOK_ID>` / `<CLEAN_WORKBOOK_ID>`
- Telegram chat id → `<MANAGER_CHAT_ID>`
- Gmail label ids → `<INCOMING_GMAIL_LABEL_ID>` / `<PROCESSED_GMAIL_LABEL_ID>` / `<ERROR_GMAIL_LABEL_ID>`
- Webhook ids → `<WEBHOOK_ID_REDACTED>`
- Email/phone-like strings scrubbed to synthetic tokens where matched

### Removed categories

Secret header values · credential ids · webhook ids · instance/meta blobs · pinData · real chat ids · private workbook ids · live label ids · personal lead data

### Preserved structural evidence

Node names · types · typeVersions · positions · connections · expressions · code logic · parameter structure · credential type placeholders · `active` · settings · safe tags

### Validation result

| Check | V1 | V2 |
|-------|----|----|
| Valid JSON | PASS | PASS |
| Unique node names / ids | PASS | PASS |
| Connection targets exist | PASS | PASS |
| Known / classified node types | PASS | PASS |
| Secret residue classes | none | none |
| PII residue classes | none | none |
| Required placeholders present | PASS | PASS |

---

## 3. Workbook handling

| Raw filename | Raw SHA256 | Sanitized Git artifact | Git eligible |
|--------------|------------|------------------------|--------------|
| `MetaBOT -Leads.DB.xlsx` | `FED01A145D4003FD9800834CA2771FD8BC07DC87ADA283E187FA172D63163DAA` | `RAW-SHEET-SCHEMA-BASELINE-v1.md` + quality findings | markdown **YES** / xlsx **NO** |
| `MetaBOT -Leads_Manager.DB.xlsx` | `AF565F1CC4E273A4B7D24660CDB22D0A628699C67C0F49694155D1A7101B6DB4` | `CLEAN-SHEET-SCHEMA-BASELINE-v1.md` + quality findings | markdown **YES** / xlsx **NO** |

---

## 4. Placeholder vocabulary

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
| `<WORKFLOW_INSTANCE_ID>` | Workflow instance id |

---

*Phase 3A.1 closes the execution gap left by the Phase 3A contract-only manifest.*

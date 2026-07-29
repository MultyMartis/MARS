# ADMIN SOURCE SELECTION v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A  
**Action:** identify closest MetaBOT Admin baseline — **do not copy yet**

---

## 1. Selected candidate

| Field | Value |
|-------|-------|
| **Candidate** | `SEO Content Agent Beta.v14 - Admin` |
| **Sanitized path** | `projects/metabot-seo-content-agent/exports/live-v14-evidence/2026-07-10/SEO-Content-Agent-Beta-v14-Admin.sanitized.json` |
| **Evidence date** | 2026-07-10 |
| **Size** | 68319 bytes |
| **active (export)** | true |
| **nodes_count** | 15 |
| **Entry** | Webhook (not Telegram Trigger) |

**Role:** pattern source for auth-ish routing, Sheets read, Telegram reply, health formatting — **not** a drop-in Sales Manager Admin.

---

## 2. Candidate node inventory (names only)

| Node | Type | Reuse for Sales Manager? |
|------|------|--------------------------|
| Webhook | `n8n-nodes-base.webhook` | Replace with Telegram Trigger (or keep webhook only if operator chooses bot webhook architecture) |
| Route Stop All Flow | IF | **Remove** — SEO emergency stop |
| Lookup Active Locks | Google Sheets | **Remove** |
| Prepare Cancelled Locks | Code | **Remove** |
| Cancel Active Locks | Google Sheets | **Remove** |
| Send Stop All Flow Success | Telegram | **Remove** |
| Route Locks | IF | **Remove** |
| Lookup Locks | Google Sheets | **Remove** |
| Format Locks Response | Code | **Remove** |
| Route Health | IF | **Reuse pattern** → part of command router |
| Health Check Active Jobs | Google Sheets | **Replace** with Sales Manager health probes |
| Health Check Memory | Google Sheets | **Remove** / replace (SEO memory table N/A) |
| Format Health Response | Code | **Reuse pattern** |
| Build Admin Response | Code | **Reuse pattern** (help/unknown/deny) |
| Send Admin Telegram | Telegram | **Reuse pattern** |

---

## 3. Reusable patterns (keep conceptually)

| Pattern | MetaBOT evidence | Sales Manager use |
|---------|------------------|-------------------|
| Command routing via IF/Switch cascade | Route Stop → Route Locks → Route Health → default Build | Expand to 10 commands + unknown |
| Sheets read for health | Health Check* | CONFIG / ERRORS / bounded CLEAN |
| Format then Telegram reply | Format* → Send Admin Telegram | Safe Telegram Reply |
| Default catch-all response | Build Admin Response | Unknown Command + Help |
| Authorization | **WEAK in this export** (SAFE UNKNOWN / incomplete) | **Must add** explicit `admin_user_ids` gate |

---

## 4. Nodes to remove (SEO-specific)

- All **locks** / `seo_active_jobs` / stop-all-flow paths.  
- Memory health against SEO memory sheet.  
- Any `/run`, `/outline`, `/text`, `/seoqa`, `/factcheck`, `/get` intake-user commands (belong to SEO Intake, not Admin Sales).  
- Content pipeline / lock cancellation side effects.

---

## 5. Authorization pattern (required new)

MetaBOT Admin sanitized export does **not** clearly show a dedicated allowlist gate node. For Sales Manager Admin.dev:

1. Normalize Command.  
2. Read Authorization Config (`admin_user_ids`).  
3. Check User Authorization IF.  
4. Deny: `Недостаточно прав.`  
5. Only then Route Command.

---

## 6. Health pattern (adapt)

Reuse: multi-check Sheets → Format Health Response → Telegram.  
Replace targets with HEALTHCHECK-CONTRACT-v1 probes.  
**Forbid** full-sheet scans / production lead appends / AI probe when AI OFF.

---

## 7. Telegram formatter

Reuse: Code builds text → Telegram send. Prefer plain text / safe HTML (MetaBOT Markdown lesson).

---

## 8. Sheets read/write pattern

Reuse Google Sheets v4.x nodes with documentId placeholders.  
CONFIG write only for allowlisted keys (`ai_on` / `ai_off`).  
Audit via LEAD_EVENTS.

---

## 9. Unknown-command path

MetaBOT falls through to Build Admin Response. Sales Manager requires **exact**:

```
Неизвестная команда. Используйте /help.
```

---

## 10. Required new Sales Manager commands

`/help` `/status` `/ai_status` `/ai_on` `/ai_off` `/health` `/stats` `/test_lead` `/last_error` `/config`

---

## 11. Copy decision

| Decision | Value |
|----------|-------|
| Copy JSON now? | **NO** (Phase 3A) |
| Preferred build mode Phase 3B | New Admin.dev graph **inspired by** candidate patterns OR clone-then-strip SEO nodes under sandbox charter |
| Max Admin.dev copies | **one** persistent |

---

## 12. SAFE UNKNOWN

- Whether live MetaBOT Admin still matches 2026-07-10 export.  
- One Telegram bot vs two for Sales Manager manager/admin.  
- Whether Sales Manager Admin should use Telegram Trigger vs webhook (operator decision in Phase 3B gate).

---

*Related: ADMIN-WORKFLOW-PATCH-SPEC-v1 · ADMIN-COMMAND-CONTRACT-v1.*

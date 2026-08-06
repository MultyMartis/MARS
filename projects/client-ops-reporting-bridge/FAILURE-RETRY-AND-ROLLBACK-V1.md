# Failure, Retry, and Rollback v1

**Status:** DESIGN ONLY / PHASE 0B  
**Implementation:** NOT STARTED

---

## 1. Critical rule

**Only source facts determine `site_status`.**

Infrastructure failures after a trustworthy envelope is created must **not** rewrite `site_status`. They affect publication/transfer/`delivery_status` / ops state only.

---

## 2. Failure catalog

| Failure | site_status effect | delivery_status effect | Retry allowed? | Retry owner | Max retry (design) | Evidence / log | Operator action | Rollback / disable |
|---------|--------------------|------------------------|----------------|-------------|--------------------|----------------|-----------------|--------------------|
| Source read failure | No authoritative site claim; treat as BLOCKED processing / no OK|ATTENTION|FAILED claim | NOT_ATTEMPTED | Yes (later) | Exporter | 3 discovery cycles | path basename + error class | Check Storage mount / permissions | Stop exporter; monitor untouched |
| Parse failure | BLOCKED (`SOURCE_ARTIFACT_MALFORMED`) if envelope built; else no publish | NOT_ATTEMPTED | No automatic “fix parse” | — | — | artifact name | Fix monitor artefacts under separate charter | N/A to baseline |
| Normalization failure / conflict | BLOCKED codes per algorithm | May still send BLOCKED SIMPLE if published | No reinterpret retry | — | — | reason_codes | Review source artefacts | Monitor untouched |
| Publication failure | Unchanged site facts in memory; latest not replaced | NOT_ATTEMPTED | Yes | Exporter | 5 | failed/ diagnostic | Check disk/ACL/lock | Disable exporter publish mode |
| File transfer failure (A) | Unchanged | NOT_ATTEMPTED / RETRYING | Yes | n8n poll / exporter republish same event | 5 | poll errors | Check mount | Disable poll |
| Webhook transfer failure (B) | Unchanged | NOT_ATTEMPTED / RETRYING | Yes | Exporter push | 5 backoff | HTTP class only | Check auth/network | Disable push |
| n8n validation failure | Unchanged (reject) | NOT_ATTEMPTED | No send | Producer may fix envelope | — | validation errors sanitized | Investigate exporter | Disable workflow intake |
| Dedupe state failure | Unchanged | Hold / manual | Cautious | Operator | — | store errors | Repair Data Store | Disable sends |
| Telegram delivery failure | **Unchanged** | FAILED or RETRYING | Yes if not SENT | n8n | 5 backoff | sanitized API metadata | Check bot/chat | Disable Telegram node/workflow |
| AI failure (future) | **Unchanged** | unchanged | AI only | n8n AI branch | 2 | ai_status=FAILED | Leave AI disabled | Disable AI branch |
| n8n outage | Unchanged | NOT_ATTEMPTED | Yes when up | Exporter/n8n | resume | outage window | Restore n8n | Workflow disabled state |
| Telegram outage | **Unchanged** | RETRYING/FAILED | Yes | n8n | 5 | outage | Wait/retry | Disable send |
| Storage unavailable | No new publish | NOT_ATTEMPTED | Yes | Exporter | 5 | mount errors | Restore Storage | Stop exporter |
| Stale lock | No publish | NOT_ATTEMPTED | After recovery | Operator + exporter | — | lock file age | Clear per protocol | — |
| Overlapping exporter runs | Second exits busy | — | Immediate no | — | — | busy code | Ensure single schedule | — |
| Partial file write | latest untouched | — | Yes after cleanup | Exporter | 3 | temp leftovers | Delete temps | — |
| Corrupt latest file | Prefer by-run truth | n8n should fail validation | Republish latest from by-run | Exporter/operator | 1 controlled | checksum mismatch | Restore from by-run | Disable poll until fixed |

---

## 3. Retry safety

| Rule | Detail |
|------|--------|
| Same `event_id` | All retries of same normalized observation |
| No duplicate after confirmed SENT | `DUPLICATE_ALREADY_SENT` suppresses Telegram |
| Delivery uncertainty | If send result unknown → manual review / `RETRY_ALLOWED` with caution |
| Backoff | Recommend 1m → 5m → 15m → 60m → 6h |
| Dead-letter | After max retries → manual-review record |
| No infinite loop | Hard max attempts; circuit break on repeated infra errors |

---

## 4. Ownership summary

| Phase | Owner of retry |
|-------|----------------|
| Discovery / normalize / publish | Future exporter |
| Intake validation | n8n (reject; no silent repair) |
| Telegram send | n8n |
| AI | n8n (future; non-blocking) |

---

## 5. Disable / rollback procedure

1. **Disable n8n workflow** (schedule and/or webhook).
2. **Stop exporter task** (when exists) — do not create/stop Task Scheduler entries in Phase 0B.
3. **Leave source monitor untouched.**
4. **Preserve last published envelope** (by-run + latest).
5. **Do not roll back baseline.**
6. **Do not modify SITE-002 production.**
7. **Restore previous workflow export** only through accepted MetaBOT apply/rollback procedure (sanitized evidence + operator HITL).

---

## 6. Source isolation checklist

- No writes into scheduled-monitor run folders.
- No baseline refresh.
- No 1C import trigger.
- No production FTP/SFTP/SSH/DB.

---

## 7. Relationship to delivery isolation

Telegram/AI/infra failures never convert:

- OK → FAILED site claim
- ATTENTION → OK
- BLOCKED → OK/ATTENTION

They only change delivery/ops fields.

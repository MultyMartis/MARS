# n8n Workflow Design v1

**Status:** DESIGN ONLY / PHASE 0B  
**Workflow JSON:** NOT CREATED  
**Live n8n access:** NOT AUTHORIZED by this task  
**Canonical working name:** `MARS Client Ops Reporting Bridge — SITE-002 Internal Telegram SIMPLE`

---

## 1. Workflow purpose

Future isolated n8n workflow that:

1. Intakes a sanitized `mars.client_ops.report` envelope (PROFILE A or B).
2. Independently validates schema/security/values.
3. Deduplicates by `event_id`.
4. Formats Telegram SIMPLE.
5. Sends to **internal operator** chat only.
6. Records `delivery_status` without mutating site facts.
7. Provides a future attachment point for optional AI_COMMENT (disabled in Phase 1).

---

## 2. Ownership

| Aspect | Owner |
|--------|-------|
| Workflow graph / credentials | MetaBOT / n8n operational lane (future), separate from SEO Worker |
| Envelope semantics | Shared Client Ops contract |
| Site facts | OCPilot / SITE (already normalized before intake) |
| Telegram transport | n8n Telegram credential + this workflow |

**Separate identity from MetaBOT SEO Worker is mandatory.** Do not bolt Client Ops delivery onto SEO Intake/Worker graphs.

---

## 3. Trigger options

### PROFILE A — File pull

| Option | Notes |
|--------|-------|
| Schedule-based file poll | Read `latest\site.post_1c_monitor.json` on interval |
| Filesystem trigger | Only if n8n edition supports it **and** operator accepts |
| Explicit promoted-file poll | Same as schedule poll with explicit path config |

**Recommendation:** **schedule-based explicit promoted-file poll** of `published\latest\site.post_1c_monitor.json`.

Rationale: portable across n8n setups; avoids fragile FS watchers; aligns with daily SITE-002 cadence; clear operator disable (turn off schedule).

Suggested poll interval (design): every **5–15 minutes** during validation; may relax later. Not created in Phase 0B.

### PROFILE B — Authenticated push

| Requirement | Rule |
|-------------|------|
| Trigger | Authenticated webhook |
| Unauthenticated | Reject |
| Content-Type | Require `application/json` |
| Size limit | Hard max (recommend **256 KiB** for MVP envelope) |
| Replay | Dedupe by `event_id` + optional request idempotency key |

**No webhook is created in Phase 0B.**

---

## 4. Logical stages (node-level, not exact node IDs)

1. **Trigger** — schedule poll (A) or webhook (B).
2. **Intake capture** — load JSON object; capture receive timestamp.
3. **Payload size/type validation** — object only; size gate.
4. **Schema gate** — `schema_name`, supported schema major.
5. **Security gate** — `contains_secrets==false`, `redacted==true`, path/secret heuristics on public fields.
6. **Status/value validation** — enums, integer metrics, action structure, timestamps, `event_id` format.
7. **Dedupe lookup** — Data Store by `event_id`.
8. **SIMPLE formatter** — deterministic template from envelope only.
9. **Route resolver** — Phase 1: internal operator destination only (credential reference).
10. **Telegram send** — dedicated Client Ops bot credential (recommended; not created here).
11. **Delivery-result capture** — sanitized metadata only.
12. **Dedupe state update** — mark SENT / FAILED / RETRYING.
13. **Failure branch** — dead-letter / manual-review path.
14. **Evidence/log branch** — ops logging without secrets.

Optional future:

15. **AI branch** — after SIMPLE success; disabled in Phase 1; failure must not affect SIMPLE.

---

## 5. Validation trust boundary

Exporter is **not** the sole trusted validator.

n8n must independently verify:

- JSON object
- `schema_name == mars.client_ops.report`
- supported schema major
- required fields
- allowed `normalized_status`
- field types
- integer metrics
- action structure
- security flags
- `event_id` format (UUID)
- payload size
- no unexpected runtime routing credentials inside payload
- timestamp parseability

n8n must **not** recompute source facts from raw monitor artifacts.

---

## 6. Normalization trust

- Trust site facts **as carried by a valid envelope**.
- Reject invalid/unsafe envelopes.
- Do not “fix” conflicting metrics inside n8n by guessing.

---

## 7. Routing config (Phase 1)

| Rule | Value |
|------|-------|
| Target | Internal operator Telegram chat only |
| Excluded | Client chat, public report, external customer routing, client-safe templates, Hub Gateway delivery |
| Credentials | n8n credential store only |
| Examples in docs | No real chat IDs |

---

## 8. SIMPLE formatting

- Follow `TELEGRAM-SIMPLE-TEMPLATES.md`.
- Facts only from envelope.
- Parse mode and escaping must be deterministic (MetaBOT lesson: entity parse failures).
- Prefer plain text or strictly escaped mode; do not pass raw `*`/`_` from uncontrolled fields.
- Display timezone: configurable; Phase 1 SITE-002 recommendation **`Europe/Moscow`** (not host locale inference).
- FAILED/BLOCKED delivery must not be suppressed.
- During validation period: OK always sends (consumer policy).

---

## 9. Telegram design

| Item | Design |
|------|--------|
| Bot | **Recommended:** dedicated Client Ops Telegram bot |
| Existence | Does **not** exist because of Phase 0B docs |
| Approval | Operator approval required before Phase 1 external-system work |
| Chat | Internal operator / approved test chat only |
| Secrets | Credential store only; never in workflow export committed to Git |
| Send failure | Sets `delivery_status` failure; **does not** change `site_status` |

---

## 10. Delivery status handling

| Outcome | delivery_status | site_status |
|---------|-----------------|-------------|
| Not yet attempted | `NOT_ATTEMPTED` | unchanged |
| API success confirmed | `SENT` | unchanged |
| Transient failure | `RETRYING` | unchanged |
| Terminal failure | `FAILED` | unchanged |

---

## 11. Retry

- Reuse same `event_id`.
- Do not resend after `DUPLICATE_ALREADY_SENT`.
- Cap retries (recommend max **5** with exponential backoff: 1m / 5m / 15m / 60m / 6h design band).
- Ambiguous Telegram response → manual review (`RETRY_ALLOWED` or hold).

---

## 12. Dead-letter / manual-review path

- Invalid schema / security reject → no Telegram; record manual-review.
- `CONFLICTING_EVENT_ID` → manual-review.
- Exhausted retries → dead-letter record with sanitized evidence.

---

## 13. Observability and audit evidence

Retain (sanitized):

- receive time
- event_id
- normalized_status / summary_code
- dedupe decision
- delivery_status
- attempt count
- workflow execution id (n8n)

Never commit raw tokens or chat IDs to Git reports.

---

## 14. Sandbox vs production separation

| Environment | Rule |
|-------------|------|
| Sandbox workflow | Separate workflow copy; test chat only |
| Production workflow | Explicit HITL activation gate |
| Credentials | Distinct credential objects where practical |

Follow MetaBOT n8n development rules: sanitized exports, operator approval, rollback plan.

---

## 15. Credential references (categories only)

- Telegram Bot credential (Client Ops)
- Webhook auth credential (PROFILE B only)
- No OpenRouter credential required for Phase 1

---

## 16. Rollback / disable

1. Disable workflow schedule / webhook.
2. Do not touch SITE-002 monitor.
3. Preserve last promoted envelope.
4. Restore prior workflow via accepted MetaBOT apply/rollback procedure only.

---

## 17. Future AI branch attachment point

After stage 10 success (SIMPLE sent or intentionally skipped by later OK policy):

- Build safe AI input from envelope only (`AI-COMMENT-CONTRACT.md`).
- On failure/timeout/empty → `ai_status=FAILED`; keep SIMPLE as delivered.
- Phase 1: branch **disabled** (`ai_status=DISABLED`).

---

## 18. Future multi-site template boundary

Parameterize `site_id` routing table later. Phase 1 hard-scopes SITE-002 internal path only. Do not assume all sites share SITE-002 artifact shapes without adapters (exporter-side).

---

## 19. Explicit non-existence statement

Phase 0B creates **no** n8n workflow, **no** webhook, **no** Telegram bot, and **no** credential objects.

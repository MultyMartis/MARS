# WORKSTREAM A — Durable Post-Telegram SENT Ledger

`D6_WORKSTREAM_A_ANALYZED`

## Current maturity

`PARTIALLY_PROVEN`

- Durable **intake** dedupe (claim insert) is proven (D1 sequential + D3 synthetic + D5R2A real-source).
- Durable **post-Telegram SENT** update is explicitly **DEFERRED** since D1.

## Evidence already proven

1. FIRST_SEEN path: Lookup → Classify → Claim Insert (`intake_state=FIRST_SEEN`, `delivery_state=PENDING`) → Respond 202 → Telegram.
2. Workflow has **two** Data Table nodes only (lookup + claim insert). No post-Telegram update node.
3. D5R2A: Telegram node success + sanitized `message_id=7`, while Data Table `delivery_state` remains `PENDING` (GET-only reconfirmed in D6).
4. Schema has `delivery_state` column but **no** `telegram_message_id` / delivery timestamp columns.
5. Producer classification treats HTTP 202 as **INTAKE_ACCEPTED**, not Telegram SENT (`telegram_delivery_known` remains false at producer boundary).

## Current exact lifecycle (observed fields)

```
NEW event_id (no DT row)
  → Dedupe Classify: FIRST_SEEN
  → Dedupe Claim Insert:
       intake_state = FIRST_SEEN
       delivery_state = PENDING
       event_status = <normalized_status>
       first_seen_at / last_seen_at set
  → Respond Accepted (HTTP 202)
  → Telegram send (side effect; not persisted to DT)
  → [END]  delivery_state may remain PENDING forever
```

Replay same fingerprint → DUPLICATE / HTTP 200 / no Telegram.
Same id different fingerprint → EVENT_ID_CONFLICT / HTTP 409 / original row retained.

## Column roles (15-column schema)

| Column | Role |
|--------|------|
| event_id, event_fingerprint | Identity / dedupe |
| site_id, schema_*, event_type, event_status | Intake snapshot |
| intake_state | Intake classification (FIRST_SEEN) |
| delivery_state | Intended delivery ledger — currently stuck at PENDING |
| first_seen_at, last_seen_at | Claim timestamps |
| duplicate_count, conflict_count | Reserved (not updated post-claim) |
| redaction_version, sandbox_marker | Policy / provenance markers |

## Gaps / failure modes

| Scenario | Current behavior | Risk |
|----------|------------------|------|
| Telegram succeeds; no DT update | PENDING remains | False “not delivered” / unsafe retry temptation |
| Telegram fails after insert | PENDING remains | Cannot distinguish fail vs success from DT alone |
| Telegram succeeds; persistence update fails (future) | Ambiguous | Needs reconciliation before retry |
| Partial execution after claim | PENDING indefinitely | Operator must use n8n execution + Telegram evidence |
| message_id not stored | Audit depends on execution payload / evidence packs | Weak durable audit |

## Minimum safe future state machine (design only)

```
UNSEEN
  → CLAIMED_PENDING     (intake_state=FIRST_SEEN, delivery_state=PENDING)
  → DELIVERY_ATTEMPTED  (optional intermediate; or fold into PENDING + attempt_count)
  → SENT                (Telegram success persisted; message_id + delivered_at)
  → FAILED_TERMINAL     (Telegram definitive failure; error class persisted)
  → FAILED_RETRYABLE    (only after policy E + reconciliation)
```

**Minimum durable fields for recovery/audit:**

- `delivery_state` ∈ {PENDING, SENT, FAILED, FAILED_RETRYABLE} (smallest useful set)
- `telegram_message_id` (sanitized numeric/string id only)
- `delivered_at` or `delivery_updated_at`
- Optional: `last_delivery_error_class` (no raw payload / token)

**Invariant:** `intake_state=FIRST_SEEN` must never be undone by delivery updates. Delivery is a separate axis.

**Recovery rule:** If `delivery_state=PENDING` after workflow success, GET-only reconcile against n8n execution Telegram node before any retry. Never auto-POST same event_id while PENDING without reconciliation.

## Decision

`D6_SENT_LEDGER_REQUIRED_BEFORE_UNATTENDED=YES`

### Why required

Unattended mode without a terminal delivery ledger cannot safely decide “already notified customer” vs “claimed but not delivered,” which is the primary duplicate-notification hazard.

### Can it wait for more manual one-shots?

Manual C1 one-shots can continue with operator evidence packs (as D5R2A did). It **cannot** wait if unattended authorization is the goal.

## Upstream / downstream

- Upstream: none among A–E (foundational)
- Downstream: **E** (retry), **D** (unattended), informs **C3** recovery

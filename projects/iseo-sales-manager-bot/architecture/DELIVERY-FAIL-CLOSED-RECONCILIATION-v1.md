# DELIVERY FAIL-CLOSED RECONCILIATION v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3E.2.1  
**Scope:** Operational.dev multi-recipient Telegram delivery + Gmail finalization boundary  
**Status:** IMPLEMENTED (harness models D01–D14 PASS); live patch acceptance **ATTENTION**

---

## Incident root cause (documented)

Observed failure chain (Phase 3D.7 class; re-validated in 3E.2.1 harness):

1. **Telegram sends succeed** for all recipients (Admin + moderators).
2. **Post-send persistence fails** — e.g. Google Sheets rate limit / quota on Stamp or Append path.
3. **`Append LEAD_EVENTS` / delivery ledger write blocked** → downstream Gmail finalize never reached.
4. **`CONFIG tg_delivered:<stable>:<recipient_ref>` never written** — business guard absent.
5. **Next poll:** Classify Duplicate treats lead as **`new`**; Expand fans out again → duplicate cards.

Contributing factors (prior forensic):

- Upsert Claim used `onError=continueRegularOutput` → fake success despite failed claim write.
- Stamp node `$input.first()` pairing threw after per-item sends.
- Gmail PROCESSED/remove-incoming skipped when Aggregate never ran.

Evidence: `evidence/phase3d7-1/DELIVERY-KEY-ROOT-CAUSE-v1.md`, `evidence/phase3d7-1/GMAIL-FINALIZATION-BOUNDARY-v1.md`.

---

## Fail-closed ledger read

Before any Telegram send expand, read LEAD_DELIVERIES (and related delivery context). Classify read outcome:

| State | Meaning | Send policy |
|-------|---------|-------------|
| `ledger_read_ok=true` | Usable rows or confirmed empty ledger | Proceed to per-recipient skip/claim logic |
| `ledger_read_error=true` | Quota / 429 / hard read failure with no usable rows | **Send zero cards** — fail closed |
| `reconciliation_required` | Prior `claimed` or `uncertain` rows for this lead/recipient | **No blind resend** — operator/reconcile path |

Harness: D01 (Fixture H ledger read error), D02 (Sheets quota).

**MARS honesty:** policy is documented + harness-mirrored; exact n8n node graph is external runtime truth.

---

## Claim must persist before send

**Change (3E.2.1):** Upsert Claim node **must not** use `continueRegularOutput` on failure.

| Before | After |
|--------|-------|
| Claim write fails silently → send proceeds | Claim write fails → block send for that recipient (`claim_upsert_error`) |
| Duplicate risk on retry | Send only after durable claim row (best-effort Sheets upsert) |

Harness: D03 — claim failure → zero cards.

---

## claimed / uncertain → no blind resend

Per-recipient delivery states:

| Status | Next poll behaviour |
|--------|---------------------|
| `delivered` | Skip send (primary ledger) |
| `claimed` | Do not resend; mark `reconciliation_required` if Telegram outcome unknown |
| `uncertain` | Same — reconcile before any new send |
| (missing) + CONFIG fallback hit | Skip send |

Harness: D04–D07, D08 (one moderator failure must not resend Admin).

Delivery key shape (unchanged):

`lead_delivery:<stable_lead_ref>:<opaque_recipient_ref>`

Forbidden in key: execution id, timestamp, username, display name, row number, Telegram message id.

---

## Secondary CONFIG guards

Primary: LEAD_DELIVERIES per-recipient row.

Secondary business guard (when ledger write lags or finalize path partial):

`tg_delivered:<stable_lead_ref>:<recipient_ref>`

Written on successful delivery/finalize path. Classify Duplicate consults this when ledger row missing but CONFIG proves prior delivery.

Harness: D05 — Gmail finalization failure must not resend already-delivered recipient when CONFIG fallback present.

---

## Append LEAD_EVENTS — continueRegularOutput

**Intentional asymmetry:** Append LEAD_EVENTS (audit trail) may use `onError=continueRegularOutput` so a **non-critical** append failure does not block Gmail PROCESSED / remove-incoming finalization.

Rationale: losing one event row is preferable to leaving mail intake-eligible and re-fan-out duplicate Telegram cards.

**Trade-off:** event log may be incomplete during quota pressure — ops must use LEAD_DELIVERIES + CONFIG guards as authoritative delivery truth.

---

## Google Sheets limitation — no atomic CAS

Google Sheets API **does not** provide compare-and-swap or transactional multi-row commit.

Implications:

- Claim → send → stamp is **best-effort sequential**, not atomic.
- Concurrent polls or partial failures can leave `claimed` without `delivered` — hence `reconciliation_required`, not blind resend.
- Rate limits (429 / quota) remain an operational risk; mitigated by fail-closed read + claim-before-send + CONFIG fallback + Gmail finalize decoupled from all moderator successes (admin-anchor policy per 3D.7.1).

**Not claimed:** exactly-once delivery under all Sheets failure modes — **at-most-once send** with reconcile path is the documented target.

---

## Gmail finalization boundary (recap)

After admin-anchor delivery + business storage:

1. Apply PROCESSED label.
2. Remove intake label.
3. Do **not** require every moderator delivery to succeed before Gmail finalize.
4. Gmail finalize failure must **not** trigger resend to recipients already marked delivered (ledger + CONFIG).

---

## Harness contract (D01–D14)

| ID | Policy |
|----|--------|
| D01–D02 | Ledger read error → zero sends |
| D03 | Claim failure → zero sends |
| D04 | Send OK + stamp fail → no resend |
| D05 | Gmail finalize fail → no resend delivered |
| D06 | Delivered skipped next poll |
| D07 | Claimed/uncertain reconciled |
| D08 | Per-recipient isolation |
| D09 | Stable key across polls |
| D10 | Incident marker suppressable |
| D11–D14 | RAW/CLEAN/delivery record integrity |

Results: `evidence/phase3e2-1/HARNESS-RESULTS-v1.md`.

---

## Related

- [LEAD-LIFECYCLE-v1.md](LEAD-LIFECYCLE-v1.md)
- [CONFIGURATION-MODEL-v1.md](CONFIGURATION-MODEL-v1.md)
- `implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md` — idempotency nodes
- `plans/ROLLBACK-PLAN-v1.md` — `tg_delivered:*` / `tg_attempts:*`

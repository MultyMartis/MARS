# REPORT — ISEO Operational.v3.dev PostgreSQL candidate

**Document:** `REPORT-iseo-operational-v3-postgres-candidate-v1.md`  
**Wave:** ISEO SALES MANAGER — POSTGRESQL CANDIDATE WORKFLOW V3 / INACTIVE BUILD / SHADOW DATA AUTHORITY  
**Worktree:** `X:\AI MARS\worktrees\mars-data-layer-iseo-operational-v3-01`  
**Branch:** `wave/mars-data-layer-iseo-operational-v3-01`  
**Date:** 2026-09-03

---

## 1. Verdict

**OPERATIONAL V3 POSTGRES CANDIDATE PASS — READY FOR CONTROLLED CUTOVER PREP**

Inactive PG candidate exists, production Sheets Operational.dev remains ACTIVE, PG tests (idempotency, status, outbox dry-run, cleanup) passed, registry registered as `candidate`, cutover not executed.

---

## 2. Old production

| Field | Value |
|---|---|
| Name | `i-SEO Sales Manager - Operational.dev` |
| ID | `xSnXPy8cEHoZw6xG` |
| Active | YES |
| SoT | Google Sheets |
| Modified this wave | No substantial modification |

---

## 3. New candidate

| Field | Value |
|---|---|
| Name | `i-SEO Sales Manager - Operational.v3.dev` |
| ID | `NH4uV145Amrgnmkm` |
| Active | NO |
| Runtime | PostgreSQL `app_iseo_sales` via `iseo_runtime` |
| Trigger | Manual inject only (no live Gmail poller) |
| Export | `projects/mars-data-layer/workflows/operational-v3-dev/Operational.v3.dev.n8n.json` |
| Export hash | `dcd9ddd595102aa8ec1e804ef08ea6efc6ef7d1bf21d37626c0eb3b4ad9b0601` |

---

## 4. Functional parity

See evidence `parity_matrix.md`. Business functions mapped; Sheets storage concepts replaced by PG tables/functions. Live Gmail Trigger parity intentionally deferred until cutover (single intake rule).

---

## 5. Data-path redesign

| Legacy Sheets concept | PG target |
|---|---|
| RAW | `inbound_events` |
| CLEAN | `leads` |
| DEDUP_INDEX | uniqueness / idempotency keys |
| LEAD_EVENTS | `lead_events` |
| LEAD_DELIVERIES | `deliveries` outbox |
| retry/defer | `jobs` + delivery retry |
| ERRORS | `errors` |

Migration: `0005_v3_runtime_functions.sql` (applied). Toolkit: closed ops in `toolkit/ops_iseo_sales.py` (no generic execute_sql product surface).

---

## 6. Gmail ingress

Normalize source identity → `register_inbound_event` (inside commit) → dedupe/new → upsert lead → durable events/deliveries → only then finalize Gmail. Candidate uses fixture inject + commit function; live poller not enabled.

---

## 7. Idempotency

Repeated same Gmail `source_id`: inbound=1, lead=1, delivery intent=1, create-event pattern=1. PASS.

---

## 8. Leads / upsert

`upsert_lead` via `process_gmail_inbound_commit`. Status transitions via `change_lead_status` (spam/processed tested). PASS.

---

## 9. Events

`append_lead_event` / commit-attached events. PASS.

---

## 10. Delivery / outbox

Enqueue on commit → claim → dry-run (NO Telegram API) → `mark_delivery_result`. PASS. Synthetic Telegram = 0.

---

## 11. Config

`get_active_config` reads non-secretish `config` keys. Secrets remain in n8n/env conventions. No full Sheets CONFIG polling on critical path.

---

## 12. Access

No ACCESS redesign. Candidate uses `access_rules` / recipient listing for outbox recipients. No Olya/admin/moderator status changes. No access test traffic.

---

## 13. Errors

`record_error` with correlation, execution id, workflow version, provider/class, retryable flag, sanitized context (`errors.context`). PASS.

---

## 14. Retry / defer

`enqueue_job` with future `available_at`; no Sheets Quota Defer Gate; no source hammer loops. PASS.

---

## 15. DB credential / security

| Item | Value |
|---|---|
| Credential | `ISEO Runtime PG (v3)` / `XCmmOgzZ1RWT4Fg3` |
| Role | `iseo_runtime` |
| Password exposed in Git/chat | NO |
| encryptionKey rotated | NO |
| Residual | `SECURITY REMEDIATION DEFERRED TO SEPARATE SERVER OPS WAVE` |

---

## 16. Test methodology

Fixtures + parameterized PG contracts as `iseo_runtime`; synthetic namespace `v3test_%`; cleanup after; shadow read smoke; no live Gmail; no Telegram sends.

---

## 17. Acceptance results

See `acceptance_matrix.md`. All required gates met for candidate acceptance (not cutover).

---

## 18. Malformed delivery residual

**Classification: `LEGACY INVALID ROW`** (webhook header dump in historical LEAD_DELIVERIES). Excluded permanently; not importer/schema blocker for v3.

---

## 19. Workflow registry

`mars_core.workflow_releases` entry: status=`candidate`, workflow id `NH4uV145Amrgnmkm`, export hash recorded. Not marked active.

---

## 20. Source export

Canonical export under `projects/mars-data-layer/workflows/operational-v3-dev/`. Orchestrator + migration + toolkit in Git.

---

## 21. Cutover plan

Design-only sequence documented in `cutover_plan.md`. **Not executed.**

---

## 22. Post-cutover rollback

PG-compatible rollback required; Sheets Operational.dev is not valid post-SoT rollback. Pin accepted v3 export as rollback release before cutover (`rollback_design.md`).

---

## 23. Sheets projection status

Not implemented. Future: PG authoritative → async Sheets projection. No PG→Sheets writes this wave.

---

## 24. Git

Wave branch `wave/mars-data-layer-iseo-operational-v3-01` from clean worktree off `origin/mars/canonical-post-recovery` @ `239bedc7`. Selective commit/push of allowlisted paths (no secrets). Primary dirty checkout not touched.

---

## 25. Remaining blockers (cutover prep — not candidate blockers)

1. Pin PG-compatible rollback release of accepted v3 export before activation.
2. Wire live Gmail Trigger only at cutover; keep single poller invariant.
3. Final Sheets→PG delta + reconcile.
4. Enable real Telegram send path (still via outbox) with controlled observe.
5. Separate server ops wave for prior n8n encryptionKey exposure remediation.
6. Optional quarantine of legacy malformed delivery row for metrics/projection.

---

## 26. Next gate

**Controlled cutover prep** (still no activate until explicit charter): rollback pin → delta plan freeze → dual-check active-state → human GO for cutover wave.

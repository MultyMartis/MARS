# WORKSTREAM C — Controlled Activation Lifecycle

`D6_WORKSTREAM_C_ANALYZED`

## Current maturity

`PARTIALLY_PROVEN`

Manual bounded lifecycle proven in D5R2A:

`inactive → activate → one POST → deactivate → active=false`

Empirical webhook behavior:

| Workflow state | Production webhook |
|----------------|--------------------|
| inactive | unavailable / HTTP 404 (D5R2) |
| active | available (D5R2A) |

Tooling: allowlisted activation client (`client-ops-n8n-activation-client.mjs`) — activate/deactivate only for workflow `tkM4H0G0gM3q9Foi`.

## Model comparison

### C1 — Permanently inactive; manual activate per controlled delivery

| Dimension | Assessment |
|-----------|------------|
| Attack surface | Lowest continuous exposure |
| Accidental webhook exposure | Only during explicit window |
| Reliability | Requires operator/orchestrator activate; proven |
| Race / concurrent events | Narrow window if deactivate always runs |
| Deactivation failure | Leaves active until emergency deactivate |
| Scheduler implications | Compatible with manual charters only |
| Fit today | **Current accepted containment model** |

### C2 — Permanently active; producer path guarded

| Dimension | Assessment |
|-----------|------------|
| Attack surface | Continuous webhook endpoint exposure |
| Protection | Relies on header auth + producer gates |
| Reliability | Highest availability |
| Risk | Any secret leak or auth bypass receives traffic while workflow can deliver Telegram |
| Fit today | **Not recommended** until SENT ledger + retry policy + stronger observability exist |

### C3 — Automated bounded activate → POST → deactivate transaction

| Dimension | Assessment |
|-----------|------------|
| Attack surface | Time-boxed |
| Reliability | Needs guaranteed finally-deactivate + health checks |
| Race windows | External POSTs possible while active; concurrency must stay 1 |
| Deactivation failure | Critical — needs alerting + emergency phrase |
| Fit | **Target for eventual unattended** after A/B/E prerequisites |

### C4 — Redesign intake so delivery workflow need not be continuously exposed

e.g. split intake accept queue from Telegram delivery; or private internal trigger.

| Dimension | Assessment |
|-----------|------------|
| Attack surface | Potentially best long-term |
| Cost | Larger redesign; not needed to unlock next phase |
| Fit | Deferred optional future |

## Recommendation

`D6_ACTIVATION_MODEL_RECOMMENDATION=HYBRID`

- **Near-term (now):** remain on **C1** for any further controlled deliveries (inactive default; temporary activate only under charter).
- **Unattended target:** **C3** with hard caps (concurrency=1, max activation window, always deactivate, alert on deactivate failure).
- **Reject C2** as default until security + ledger + concurrency proofs exist.
- **C4** remains a later option if C3 race windows prove unacceptable.

## Required before unattended?

**YES** (as a defined operational model, not necessarily permanent activation). Unattended without an explicit activation contract recreates D5R2’s inactive-404 failure or C2’s continuous exposure by accident.

## Upstream / downstream

- Upstream soft: **A** improves recovery after mid-window failures
- Downstream: **D**

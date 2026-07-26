# WORKSTREAM D — Eventual Unattended Monitor → Client Ops Architecture

`D6_WORKSTREAM_D_ANALYZED`

## Current maturity

`DESIGNED_NOT_IMPLEMENTED` (no automatic connection; D4 adapter live blocked; no watcher)

## Desired future path (design)

```
SITE-002 scheduled monitor (dedicated runtime @ 8bb6e8f0)
  → authoritative completed artifacts on Storage
  → adapter (firewall + mapping)
  → freshness / delivery_eligibility gate
  → deterministic event_id
  → durable dedupe
  → Client Ops delivery (bounded activation)
  → terminal delivery_state
  → containment + operator escalation
```

## Model comparison

### D1 — Monitor runner directly calls producer

- Coupling: high
- Dirty MAIN / runtime risk: high if runner pulls monorepo WIP
- Replay safety: weak unless ledger complete
- Scheduler independence: poor
- **Reject for near-term**

### D2 — Separate scheduled producer reads latest **completed** monitor artifact

- Coupling: low (artifact contract only)
- Source authority: explicit completed run directory (same as D5 path rules)
- Replay safety: event_id + DT dedupe + SENT ledger
- Failure recovery: producer retries independently of monitor
- Observability: separate producer run evidence
- Dirty MAIN avoidance: uses dedicated runtime for monitor; producer from controlled checkout / offline package
- Scheduler independence: two tasks; overlap policy required
- **Recommended next unattended architecture**

### D3 — Queue / outbox between monitor and Client Ops

- Best long-term durability / independent retries
- Heavier ops (new store, consumers)
- **Future evolution after D2 proves**

### D4 — n8n polls / triggers from Storage

- Moves orchestration into n8n
- Credential + filesystem authority complexity
- Harder to keep MAIN/runtime cleanliness guarantees
- **Not preferred**

### D5 — Other

Not required; D2 covers evidence-backed needs.

## Recommendation

`D6_UNATTENDED_ARCHITECTURE_RECOMMENDATION=D2`

With explicit future path D2 → D3 once SENT ledger + retry policy are production-safe.

## Prerequisites before any D2 live authorization

1. Workstream **A** terminal delivery ledger
2. Workstream **B** freshness separation
3. Workstream **C** HYBRID/C3 activation contract
4. Workstream **E** retry/concurrency policy
5. Runtime cleanliness + scheduler overlap lock
6. Security review pass for unattended secrets handling

## Decision flags

- Required before unattended: the **integration itself is the unattended goal** — must be last
- Can wait: **YES** (must wait)
- `CLIENT_OPS_AUTOMATIC_SITE002_CONNECTION_AUTHORIZED=NO` (unchanged)

## Upstream / downstream

- Upstream: **A, B, C, E**
- Downstream: none among A–E (terminal architecture goal)

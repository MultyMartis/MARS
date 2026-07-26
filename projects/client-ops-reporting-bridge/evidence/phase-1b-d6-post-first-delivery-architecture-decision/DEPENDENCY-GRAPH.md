# DEPENDENCY GRAPH — Phase 1B-D6

`D6_DEPENDENCY_GRAPH_COMPLETE`

## Directed edges (prerequisites → dependents)

```text
A (SENT ledger) ──────────────► E (retry/concurrency)
A (SENT ledger) ──────────────► D (unattended)
B (freshness) ────────────────► D (unattended)
B (freshness) ───────────────► E (retry of stale artifacts)
C (activation lifecycle) ─────► D (unattended)
E (retry policy) ─────────────► D (unattended)
A ─soft─► C3 recovery behavior (not blocking C1)
```

## Ranked implementation order (derived)

1. **A** — no upstream among A–E; blocks safe retry and unattended terminal state
2. **B** — orthogonal to A; blocks honest eligibility for unattended
3. **C** — formalize HYBRID/C3 before automation; can be design-heavy after A/B start
4. **E** — requires A (and B for stale rules)
5. **D** — requires A+B+C+E

## Edge rationale

| Edge | Why upstream is required |
|------|--------------------------|
| A → E | Without SENT vs PENDING, automatic retry cannot avoid duplicate Telegram |
| A → D | Unattended must know terminal delivery state for each event_id |
| B → D | Unattended must not treat aged ATTENTION as BLOCKED or silently send stale |
| B → E | Stale artifacts must never enter retry-as-fresh paths |
| C → D | Unattended needs explicit activate window contract (else 404 or permanent exposure) |
| E → D | Unattended failure recovery without retry policy is undefined / unsafe |
| A → C3 (soft) | Ledger enables reconcile if deactivate/POST races leave ambiguous state |

## Primary answer

**What must be fixed first before unattended authorization?**

**A — durable post-Telegram SENT ledger**, then **B**, then **C**, then **E**, then **D**.

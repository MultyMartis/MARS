# EAR Failure Models v1

**Purpose:** Document expected EAR and operator behavior when acquisition or snapshot quality fails in predictable ways.  
**Status:** architecture specification — **no** automated handling implementation.  
**Phase:** 2B  

---

## Philosophy

| Principle | Application |
|-----------|-------------|
| **Honesty over completeness** | Gaps belong in `safe-unknown`, not invented data |
| **Fail closed on publish** | Validation failure → no Publish |
| **No silent downgrade** | Quality level must match evidence; operator may **explicitly** downgrade |
| **Consumers do not fix acquisition** | Unblock = new Request → Acquire cycle |

---

## Failure catalog

### Missing evidence

| Aspect | Definition |
|--------|------------|
| **Condition** | Required section for declared quality level is absent and not documented |
| **Expected EAR behavior** | Validate **fails** OR operator explicitly lowers quality target before re-Validate; add `safe-unknown` entry if section intentionally skipped |
| **Publish** | **No** publish at overstated level |
| **Consumer** | Must not infer missing data from charter |

---

### Partial evidence

| Aspect | Definition |
|--------|------------|
| **Condition** | Some sections present; others incomplete; common in Mode 0/1 first cycles |
| **Expected EAR behavior** | Declare actual quality level (e.g. Level 1 with Level 3 requested → downgrade or reject); populate `safe-unknown` per gap; allow partial sequence `p1`, `p2` |
| **Publish** | Allowed at **honest** level with operator approval |
| **Consumer** | Halts phases blocked by `safe-unknown` per consumer guide |

---

### Contradictory evidence

| Aspect | Definition |
|--------|------------|
| **Condition** | Metadata claims conflict with manifest (e.g. version claim vs file proof) |
| **Expected EAR behavior** | Validate **fails** or marks contradiction in `safe-unknown` with both sources cited; **no** silent resolution |
| **Publish** | **No** publish until operator resolves or downgrades claims |
| **Consumer** | Must not treat conflicting claims as proven |

---

### Stale snapshot

| Aspect | Definition |
|--------|------------|
| **Condition** | `created_at` or acquisition window no longer acceptable for audit charter (SITE changed materially) |
| **Expected EAR behavior** | Document staleness in metadata if known; recommend new Acquire; do not refresh published package in place |
| **Publish** | Operator may withhold Publish if charter requires fresh evidence |
| **Consumer** | Treat as point-in-time; cite `snapshot_id`; request new cycle for “current” audit |

---

### Version mismatch

| Aspect | Definition |
|--------|------------|
| **Condition** | `snapshot_version` / `ear-opencart-snapshot-v1` incompatible with consumer intake rules |
| **Expected EAR behavior** | Validate fails; document required contract version |
| **Publish** | **No** publish to consumers on older contract without explicit consumer bump |
| **Consumer** | Reject intake; request EAR package at supported version |

---

### Failed validation

| Aspect | Definition |
|--------|------------|
| **Condition** | Checklist in [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md) not satisfied (secrets in package, quality inflation, missing `safe-unknown` on empty critical section) |
| **Expected EAR behavior** | Reject candidate; document reasons; remain operator-held |
| **Publish** | **Blocked** |
| **SAFE UNKNOWN** | Ambiguous checklist result → treat as failed validation until operator clarifies |

---

### Consumer misuse

| Aspect | Definition |
|--------|------------|
| **Condition** | Consumer uses unpublished candidate, live credentials, mutates snapshot, or upgrades quality without new `snapshot_id` |
| **Expected EAR behavior** | **None** at runtime (EAR not a consumer monitor) — document as charter violation in incident/report |
| **Operator** | Halt consumer run; enforce Publish-only intake; new acquisition if live access occurred |
| **EAR process response** | Clarify handoff docs; no automatic remediation |

---

## Failure → lifecycle mapping

| Failure | Typical stage | Next step |
|---------|---------------|-----------|
| Missing / partial | Validate | Re-Acquire or downgrade |
| Contradictory | Validate | Operator investigation |
| Stale | Consume or pre-Publish | New Request → Acquire |
| Version mismatch | Validate | Spec bump or re-package |
| Failed validation | Validate | Fix candidate or abandon |
| Consumer misuse | Consume | Operator incident; new snapshot if needed |

---

## SAFE UNKNOWN behavior (global)

When EAR or operator cannot determine:

| Situation | Behavior |
|-----------|----------|
| Evidence sufficiency for quality level | **SAFE UNKNOWN** → no publish at claimed level |
| Connector output integrity (future) | **SAFE UNKNOWN** → Validate fails until operator attests |
| Legal/compliance of retained bulk | Operator legal — not EAR |

Record in package `safe-unknown` section with `unblock_hint` where applicable per [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md).

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md) | Gates |
| [EAR-SNAPSHOT-PUBLISHING-v1.md](EAR-SNAPSHOT-PUBLISHING-v1.md) | No publish on fail |
| [EAR-OPENCART-CONSUMER-GUIDE-v1.md](EAR-OPENCART-CONSUMER-GUIDE-v1.md) | Consumer halt rules |

---

## Non-goals

- Automated retry connectors
- Self-healing snapshot repair
- Consumer-side EAR enforcement agents

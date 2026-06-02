# EAR Connector Failures v1

**Purpose:** Failure taxonomy for Mode 2 connectors — expected connector behavior and expected EAR behavior.  
**Status:** architecture specification only — **no** retry automation or code.  
**Phase:** 2D  
**Relation:** Complements [EAR-FAILURE-MODELS-v1.md](EAR-FAILURE-MODELS-v1.md) (workflow-level); this document is **connector-acquisition-specific**.

---

## Failure handling principles

1. **Fail closed on integrity** — Authentication, read-only violation, corrupt archive → no silent publish as complete.
2. **Partial is explicit** — Partial acquisition is `partial` status + warnings + `safe-unknown`, not success.
3. **No secret leakage in errors** — Error messages describe class and scope, not passwords.
4. **Operator authority** — Retry, scope change, or mode fallback (0/1) requires operator decision.
5. **Validation is gate** — Connectors do not bypass Validate stage.

---

## Failure catalog

### Authentication failure

| Aspect | Detail |
|--------|--------|
| **Examples** | Wrong password, expired key, MFA required, admin lockout |
| **Connector behavior** | Stop immediately; status `failed`; error `authentication_failed`; no evidence package or empty package marked failed |
| **EAR behavior** | Acquire stage fails; no Validate promotion; operator notified; log channel without credentials |
| **Snapshot impact** | None published; prior snapshot unchanged |
| **Recovery** | Operator fixes credentials externally; new Request/Acquire cycle |

---

### Connection failure

| Aspect | Detail |
|--------|--------|
| **Examples** | DNS failure, timeout to host, TLS mismatch, firewall block |
| **Connector behavior** | Stop; `connection_failed`; optional retry count **SAFE UNKNOWN** at runtime |
| **EAR behavior** | Acquire fails; suggest alternate channel (e.g. FTP vs SFTP) in operator guidance only |
| **Snapshot impact** | None |
| **Recovery** | Network fix or channel change; new cycle |

---

### Timeout

| Aspect | Detail |
|--------|--------|
| **Examples** | Manifest sweep exceeded max duration; large `image/` tree |
| **Connector behavior** | Stop or `partial` per scope policy; warning `incomplete_scope`; list completed prefixes |
| **EAR behavior** | If `partial`: Validate may allow degraded level with expanded `safe-unknown`; Publish requires operator acknowledgment |
| **Snapshot impact** | Partial manifest — consumers must not assume full tree |
| **Recovery** | Narrow scope, exclude globs, or ZIP offline intake |

---

### Partial acquisition

| Aspect | Detail |
|--------|--------|
| **Examples** | Some paths denied; one Hybrid leg failed; max size reached |
| **Connector behavior** | status `partial`; warnings enumerate gaps; Evidence Package contains completed artifacts only |
| **EAR behavior** | Validate maps available sections; mandatory `safe-unknown` entries; quality level capped |
| **Snapshot impact** | Publish allowed only if operator accepts degraded level per [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md) |
| **Recovery** | Second acquisition leg or new `snapshot_id` merge policy **SAFE UNKNOWN** |

---

### Contradictory evidence

| Aspect | Detail |
|--------|--------|
| **Examples** | Admin reports 3.0.3.7; `version.php` says 3.0.3.8; ZIP vs live SFTP mismatch |
| **Connector behavior** | warning `contradiction_detected`; do not resolve — pass both artifacts |
| **EAR behavior** | Validation records both in evidence index; `metadata` uses **Detected** vs **Claim** split; `safe-unknown` until operator resolves |
| **Snapshot impact** | Published with explicit contradiction flag — consumers halt version-dependent phases |
| **Recovery** | Operator determines truth source; re-acquire corroborating channel |

---

### Corrupt archive

| Aspect | Detail |
|--------|--------|
| **Examples** | Truncated zip, bad CRC, zip bomb detected, path traversal attempt |
| **Connector behavior** | Stop or quarantine; error `corrupt_artifact`; no extract to consumer paths |
| **EAR behavior** | Acquire fails; quarantine protocol per [EAR-STORAGE-MODEL-v1.md](EAR-STORAGE-MODEL-v1.md) conceptual |
| **Snapshot impact** | None |
| **Recovery** | New archive from operator; virus scan policy **SAFE UNKNOWN** |

---

### Missing metadata

| Aspect | Detail |
|--------|--------|
| **Examples** | Connector cannot read version files; admin session blocked |
| **Connector behavior** | `partial` or `success` with warnings `weak_evidence`; no fabricated metadata |
| **EAR behavior** | Validation leaves `metadata` minimal; populates `safe-unknown` |
| **Snapshot impact** | L0–L1 possible; OCPilot may block Run 5 phases |
| **Recovery** | Add connector leg (Hybrid) or operator manual drop Mode 0 |

---

### Version mismatch

| Aspect | Detail |
|--------|--------|
| **Examples** | Detected version ≠ charter baseline; fork markers unexpected |
| **Connector behavior** | warning `version_mismatch`; collect evidence anyway |
| **EAR behavior** | Do not auto-change `baseline_candidate`; flag consumer |
| **Snapshot impact** | Publish allowed with honesty — consumer selects baseline or stops |
| **Recovery** | Charter update or correct SITE target |

---

### Read-only violation

| Aspect | Detail |
|--------|--------|
| **Examples** | SFTP STOR attempted; admin save clicked; SQL UPDATE in script |
| **Connector behavior** | Immediate stop; error `read_only_violation`; status `failed` |
| **EAR behavior** | Halt acquisition; incident note in operational log; no publish |
| **Snapshot impact** | None from this session; operator assesses SITE side effects |
| **Recovery** | Operator confirms SITE state; separate remediation charter if needed — outside EAR v1 |

---

## Cross-reference: workflow failures

| Connector failure | Workflow stage | See also |
|-------------------|----------------|----------|
| Auth / connection | Acquire | [EAR-FAILURE-MODELS-v1.md](EAR-FAILURE-MODELS-v1.md) |
| Partial / contradiction | Validate | [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md) G2–G3 |
| Publish blocked | Publish | [EAR-SNAPSHOT-PUBLISHING-v1.md](EAR-SNAPSHOT-PUBLISHING-v1.md) |

---

## Expected operator actions (summary)

| Failure | Typical operator action |
|---------|-------------------------|
| Authentication | Fix secret ref; retry |
| Connection | Check VPN/firewall; try FTP or ZIP |
| Timeout | Reduce scope |
| Partial | Accept degraded publish or re-run leg |
| Contradiction | Investigate; re-acquire |
| Corrupt archive | Re-download backup |
| Missing metadata | Add channel |
| Version mismatch | Update charter/baseline |
| Read-only violation | Stop; site impact review |

---

## SAFE UNKNOWN

- Automatic retry backoff — runtime charter.
- Whether contradiction auto-resolves preferring file over admin — default: file preferred at validation unless operator override documented.

---

## Non-goals

- Incident ticketing integration or PagerDuty.

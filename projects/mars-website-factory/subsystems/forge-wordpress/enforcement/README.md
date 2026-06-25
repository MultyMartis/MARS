# Forge WordPress — FW-07C-0 Enforcement Foundation

**Phase:** FW-07C-0 (repository-only)
**Status:** IMPLEMENTED_AND_VALIDATED_IN_REPO
**Agent:** AG-WP-001

---

## Scope

FW-07C-0 implements the first **executable fail-closed** safety layer for Forge WordPress. It is a **pure validation foundation** — no WordPress runtime, database, FTP, WP-CLI, or filesystem mutation outside the repository.

Components:

| Component | Path | Role |
|-----------|------|------|
| Path validator | `src/path-validator.mjs` | Fail-closed path gate |
| Scope policy | `src/scope-policy.mjs` + `policies/forge-scope-policy-v1.json` | Environment admission |
| Operation registry | `src/operation-registry.mjs` | Canonical 42-op loader |
| Risk engine | `src/risk-engine.mjs` + `policies/forge-risk-policy-v1.json` | R0–R5 requirements |
| Kill switch | `src/kill-switch.mjs` | Repo-only state evaluator |
| Audit contract | `src/audit-event.mjs` | Safe audit object builder |
| Admission validator | `src/admission-validator.mjs` | Unified fail-closed gate |
| Reason codes | `src/reason-codes.mjs` | Stable denial vocabulary |

**Stubs (contract-only, no runtime execution):** snapshot manager, approval gate, dry-run runner — deferred to FW-07C-1+.

---

## Fail-closed model

Any missing, unknown, or unverified input → **DENY**. No warnings-only path. Admission output:

```json
{
  "admitted": false,
  "decision": "DENY",
  "reason_codes": ["FW_..."],
  "phase": "FW-07C-0"
}
```

---

## Protected roots

Defined in `policies/forge-protected-roots-v1.json`:

- `C:\`, `C:\Users`, `C:\Windows`, `C:\Program Files`, `C:\Program Files (x86)`
- `C:\MARS Phenix`, `C:\AI MARS`, `C:\AI MARS STORAGE`, `C:\this is backUP AI MARS 23.06.2026`
- `E:\`, `E:\MARS-Localhost` (protected parent; registered site descendants allowlisted separately)

---

## Runtime prohibition

FW-07C-0 **must not**:

- Touch `E:\MARS-Localhost` on disk
- Run WordPress, Laragon, Apache/Nginx/MySQL
- Use WP-CLI, DB connections, FTP/SFTP, remote requests
- Create runtime lock files or enable tokens on disk

Synthetic path strings in fixtures are **inert test data only**.

---

## Phase limitations (FW-07C-0)

| Environment | Policy |
|-------------|--------|
| `LOCAL_SYNTHETIC` | R0 only, after full validation |
| `LOCAL_PROJECT_RUNTIME` | DENY |
| `REMOTE_*` | DENY |

| Risk class | FW-07C-0 |
|------------|----------|
| R0 | Admission possible after validation |
| R1–R5 | DENY |

| Kill switch | Policy |
|-------------|--------|
| `GLOBAL_DISABLED` (default) | DENY ALL |
| `SITE_ENABLED_READ_ONLY` | R0 only if all other checks pass |
| `EMERGENCY_STOP` | DENY ALL |

**Runtime bindings:** 0 proven. Registry marks all operations `UNBOUND`. Test fixtures may use `TEST_ONLY_SYNTHETIC_BINDING` — not in production registry.

**Reparse points:** `requires_reparse_check = true` always. Real resolution deferred to FW-07C-1 runtime adapter. Status `UNKNOWN` → DENY.

---

## Test command

From repository root:

```bash
node projects/mars-website-factory/subsystems/forge-wordpress/enforcement/tests/run-all-enforcement-tests.mjs
```

Individual suites:

```bash
node .../tests/run-path-validator-tests.mjs
node .../tests/run-risk-engine-tests.mjs
node .../tests/run-admission-tests.mjs
```

---

## Validation vs runtime binding

| Layer | FW-07C-0 | FW-07C-1+ |
|-------|----------|-----------|
| Path policy | Executable (string-only) | + reparse adapter |
| Operation registry | Loaded from contracts | + proven bindings |
| Admission | Repo-only evaluator | Wired into harness |
| Audit | Object contract | Append-only JSONL on disk |

---

## Transition to FW-07C-1

FW-07C-1 is **LOCAL_SYNTHETIC_READ_ONLY_BINDING_VALIDATED** (2026-06-26). See [runtime/README.md](../runtime/README.md).

FW-07C-2 is **NOT ADMITTED**. Do not perform mutating runtime operations.

---

*FW-07C-0 enforcement foundation — repo-only, fail-closed.*

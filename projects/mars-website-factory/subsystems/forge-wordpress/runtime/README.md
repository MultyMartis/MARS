# Forge WordPress — FW-07C-1 Runtime Binding Layer

**Phase:** FW-07C-1 — Local Synthetic Runtime Binding Preflight  
**Status:** LOCAL_SYNTHETIC_READ_ONLY_BINDING_VALIDATED (when preflight passes)  
**Agent:** AG-WP-001

---

## Scope

FW-07C-1 binds **proven read-only R0 operations** to the `fws-0001` synthetic WordPress sandbox through the FW-07C-0 fail-closed admission layer.

This layer is **not** a mutating harness. It performs:

- Runtime authority validation
- Physical/reparse boundary validation
- Scoped in-memory admission tokens
- Read-only Node filesystem adapters
- Baseline mutation detection
- External audit receipts (outside runtime)

---

## Mandatory execution chain

```text
operation request
→ schema validation
→ kill switch
→ operation registry (binding)
→ risk engine (FW-07C-0)
→ scope policy (FW-07C-0)
→ logical path validator (FW-07C-0)
→ physical/reparse boundary validator
→ exact runtime binding
→ read-only adapter (requires admission token)
→ result validation
→ audit receipt (external path only)
```

**Direct adapter invocation is DENIED.** Use `executeRuntimeInspection()` only.

---

## Public API

| Entrypoint | Path |
|------------|------|
| Runtime inspection chain | `src/runtime-inspection-chain.mjs` → `executeRuntimeInspection()` |
| Reparse validator | `src/reparse-boundary-validator.mjs` |
| Baseline capture | `src/baseline-capture.mjs` |
| Binding registry | `bindings/fws-0001-readonly-bindings-v1.json` |

---

## Proven operations (FW-07C-1)

| operation_id | binding_decision |
|--------------|------------------|
| `wp.inspect.runtime` | BOUND_READ_ONLY_PROVEN |
| `wp.inspect.theme` | BOUND_READ_ONLY_PROVEN |
| `wp.inspect.plugin_state` | BOUND_READ_ONLY_PROVEN |
| `wp.inspect.routes` | BOUND_READ_ONLY_PROVEN |

All other candidate operations are **DEFER** or **REJECT**.

---

## Kill switch

| State | Behavior |
|-------|----------|
| `GLOBAL_DISABLED` | Default — DENY ALL |
| `SITE_ENABLED_READ_ONLY` | R0 read-only after full gate pass |
| `SITE_DISABLED` | DENY |
| `EMERGENCY_STOP` | DENY ALL |

No persistent runtime tokens. In-memory only.

---

## Runtime prohibition

- No writes inside `X:\MARS-Localhost`
- No WP-CLI, PHP execution, DB clients, network
- No shell execution for bound operations
- No audit files inside runtime site root

External receipts: `runtime/reports/fw07c1-x-runtime-preflight/` (repository path on `X:\AI MARS`)

---

## Test commands

```bash
node projects/mars-website-factory/subsystems/forge-wordpress/runtime/tests/run-all-fw07c1-tests.mjs
node projects/mars-website-factory/subsystems/forge-wordpress/enforcement/tests/run-all-enforcement-tests.mjs
node projects/mars-website-factory/subsystems/forge-wordpress/runtime/tests/run-runtime-preflight.mjs
```

---

## Transition

| Phase | Status |
|-------|--------|
| FW-07C-1 | Read-only synthetic binding validated |
| FW-07C-2 | **NOT ADMITTED** — requires separate additive charter |

Do **not** touch `shpigovsky` runtime. Do **not** perform WordPress writes.

---

*FW-07C-1 runtime binding — read-only synthetic preflight.*

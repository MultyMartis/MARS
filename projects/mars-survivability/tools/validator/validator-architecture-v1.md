# Scoped Operation Validator — Architecture (v1)

**Status:** **documented** — human-operated validation tooling foundation (G2).  
**Not:** runtime orchestration, autonomous security system, Cursor hook, policy engine, or enforcement product.

**Lane:** B (Survivability / Operational Hardening)  
**Implements (read-only alignment):** [agent-operation-risk-classes-v1.md](../../contracts/agent-operation-risk-classes-v1.md), [protected-zones-registry-v1.md](../../registries/protected-zones-registry-v1.md), [destructive-operations-policy-v1.md](../../contracts/destructive-operations-policy-v1.md)

---

## 1. Purpose

Provide the **first real validation tooling layer** for MARS survivability: a **read-only**, **human-invoked** CLI that evaluates a proposed shell command (and optional scope path) **before** an operator or AGENT executes it.

**Goals:**

- Reduce risk of destructive operations, unsafe scope, path drift, recursive delete, dangerous AGENT tasks, workspace chaos, and accidental repo damage.
- Encode deny-first semantics from enforcement docs into machine-checkable rules (registry + script).
- Produce structured reasoning for operator review — not silent auto-block.

---

## 2. Boundaries

| In scope | Out of scope |
|----------|--------------|
| CLI read-only pattern matching on command strings | Autonomous execution blocking |
| Rule registry (JSON) maintained by humans | Cursor/IDE hooks |
| Sandbox example inputs | Production workspace mutation |
| Report format documentation | Git commit/push automation |
| Operational test protocol | Snapshot creation automation |
| GitGuard tooling map (design) | Claim of deployed GitGuard product |

**Filesystem:** Validator **does not** read or write workspace files except loading its own registry and optional user-supplied paths for scope checks (path string analysis only).

**Invocation:** Operator runs `node scoped-operation-validator-v1.mjs` **manually** when reviewing a planned operation. **No** auto-run on agent start, **no** CI gate unless explicitly chartered later.

---

## 3. Non-goals

- **Not** a runtime orchestration layer or multi-agent router.
- **Not** an autonomous security or compliance product.
- **Not** a substitute for human judgment, scope lock, or snapshot discipline.
- **Not** proof that MARS enforces operations automatically — enforcement remains **human-operated** per [enforcement-rules-registry-v1.md](../../registries/enforcement-rules-registry-v1.md).
- **Not** integration with Triumph v4/v5 workspaces beyond path-tier rules in registry.

---

## 4. Human-operated nature

1. Operator (or reviewer) copies proposed command from AGENT plan or task header.
2. Operator runs validator with `--command` and optional `--scope` / `--risk-class`.
3. Operator reads decision + reasoning; may override with documented human approval.
4. Operator proceeds, revises scope, or halts per [operational-halt-protocol-v1.md](../../protocols/operational-halt-protocol-v1.md).

**AGENT must not** invoke validator autonomously unless task explicitly lists validator review as a human step completed by operator.

---

## 5. No autonomous enforcement

- Validator output is **advisory** for G2 — it does not intercept Shell tool calls.
- **DENY** means “do not proceed without human review” — not “blocked by system.”
- Future GitGuard may consume validator output; that is **planned**, not implemented.

---

## 6. Read-only validation

The validator:

- Loads [rules/validator-rules-registry-v1.json](rules/validator-rules-registry-v1.json).
- Matches command text against patterns (case-insensitive where configured).
- Compares scope path against `protected_paths` prefixes.
- Emits decision and explanation to stdout (and optional report file per [validator-report-format-v1.md](validator-report-format-v1.md)).

It **never** executes the input command, **never** deletes files, **never** runs git mutations.

---

## 7. Deny philosophy

Aligns with [destructive-operations-policy-v1.md](../../contracts/destructive-operations-policy-v1.md) and enforcement registry:

- **Uncertain → escalate** — default to **NEED_HUMAN** or **DENY**, never silent **ALLOW**.
- **Recursive delete, git clean, reset --hard, workspace wipe language → DENY** for AGENT-context review.
- **Protected zone touch without narrow scope → NEED_HUMAN** minimum.
- **Missing scope on mutation-adjacent command → NEED_HUMAN**.

---

## 8. Risk-class integration

Optional `--risk-class` (`SAFE` | `LOW` | `MEDIUM` | `HIGH` | `CRITICAL` | `FORBIDDEN`) adjusts escalation:

| Declared class | Validator behavior |
|----------------|-------------------|
| SAFE | Stricter pattern match still applies; protected-path writes still escalate |
| LOW–MEDIUM | Missing scope on write-like patterns → **NEED_HUMAN** |
| HIGH–CRITICAL | Any destructive pattern → **DENY**; borderline → **NEED_HUMAN** |
| FORBIDDEN | Any non-read-only command → **DENY** |

Source taxonomy: [agent-operation-risk-classes-v1.md](../../contracts/agent-operation-risk-classes-v1.md).

---

## 9. Protected-zone integration

Registry `protected_paths` mirrors [protected-zones-registry-v1.md](../../registries/protected-zones-registry-v1.md) P0–P3 and Q paths (prefix match).

| Trigger | Typical decision |
|---------|------------------|
| Scope under P0 (`governance/`, `registry/`, `AGENTS.md`, …) + write/delete language | **DENY** or **NEED_HUMAN** |
| Scope under `workspaces/_snapshots/` + delete | **DENY** |
| Scope under production `workspaces/*/` + recurse/cleanup | **DENY** |
| Scope under `_sandbox/` + recurse | **NEED_HUMAN** (quarantined cleanup policy A-03) |

---

## 10. Prompt-risk integration

Validator does **not** parse full chat prompts. Operators map prompt phrases using [safe-prompt-pattern-library-v1.md](../../guardrails/safe-prompt-pattern-library-v1.md), then test extracted shell fragments.

Registry sections `cleanup_language`, `dangerous_keywords` support overlap with unsafe prompt patterns (“start fresh”, “cleanup repo”, “recreate workspace”).

---

## 11. Future GitGuard relation

| G2 (now) | G3+ (planned, not claimed) |
|----------|----------------------------|
| Standalone CLI + JSON registry | Pre-agent hook **optional**, human-chartered |
| Human runs before risky step | Manifest + snapshot cross-check |
| Text report format | Structured JSON report files under `reports/` |
| Tooling map contract | Diff scanner, rollback map validator |

See [gitguard-tooling-map-v1.md](../../contracts/gitguard-tooling-map-v1.md).

---

## 12. Decision model: ALLOW / DENY / NEED_HUMAN

| Decision | Meaning | Operator action |
|----------|---------|-------------------|
| **ALLOW** | No rule matched; read-only or explicitly scoped safe pattern | May proceed if scope lock and risk class agree |
| **DENY** | Forbidden pattern, protected zone violation, or FORBIDDEN class | **Do not** execute; halt or redesign |
| **NEED_HUMAN** | Ambiguous scope, medium-risk write, sandbox recurse, or incomplete evidence | Require `APPROVED: <op> @ <paths>` before AGENT runs |

**Precedence:** **DENY** > **NEED_HUMAN** > **ALLOW**. Multiple matches aggregate highest severity.

---

## 13. Component layout

```
tools/validator/
├── validator-architecture-v1.md      ← this document
├── scoped-operation-validator-v1.mjs ← CLI (Node ESM)
├── validator-report-format-v1.md
├── rules/
│   └── validator-rules-registry-v1.json
├── examples/                       ← sandbox test strings only
└── reports/                        ← human-written reports (.gitkeep)
```

---

## 14. SAFE UNKNOWN

- Effectiveness against novel obfuscated commands — **UNKNOWN** until G3 fuzz review.
- False positive rate on legitimate gulp/npm scripts — **UNKNOWN** until operational test protocol runs.
- Whether registry stays in sync with protected-zones doc — **human maintenance** required.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | G2 — validator architecture v1 |

---

*End of Validator Architecture v1.*

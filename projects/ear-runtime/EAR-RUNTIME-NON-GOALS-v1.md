# EAR Runtime Non-Goals v1

**Type:** Anti–scope-creep guard for engineering program  
**Date:** 2026-06-02  
**Architecture non-goals (still apply):** [EAR-NON-GOALS-v1.md](../../shared/external-access-runtime/EAR-NON-GOALS-v1.md)

---

## Purpose

Prevent EAR Runtime from expanding into consumer products, deployment automation, or architecture rewrites during implementation pressure.

---

## Explicit non-goals

| Non-goal | Why |
|----------|-----|
| **Not a replacement for OCPilot** | OCPilot owns audit/analysis; Runtime owns acquisition only |
| **Not a replacement for WPilot** | WordPress engineering remains separate program |
| **Not a CMS manager** | No admin UI, catalog editing, or content CRUD |
| **Not a deployment platform** | No push-to-production, no site mutation |
| **Not autonomous site modification** | Read-only acquisition; Mode 3 / write connectors forbidden in v1 |
| **Not production automation** | No unattended cron/CI acquisition without explicit future charter |
| **Not a credential vault product** | `credential_ref` indirection only — secrets outside git |
| **Not governance enforcement as product** | No policy engine replacing human Validate/Publish |
| **Not architecture-by-code** | Connector code must not redefine snapshot levels or gates |
| **Not OCPilot Run 5 execution** | Consumer runs remain in OCPilot |
| **Not Website Factory operator** | Factory production rules stay in Factory domain |
| **Not MARS orchestration runtime** | No multi-agent scheduler or autonomous agent mesh |
| **Not hiding implementation in `shared/`** | Runtime code belongs under `projects/ear-runtime/runtime/` when built |
| **Not live PILOT execution by default** | Backlog + charter ≠ Execution Authorization |

---

## Technology non-goals (v1 — stack decided at Engineering Charter)

Engineering Charter **APPROVED** 2026-06-02 — Python, CLI-first, human-operated. See [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md), [R1-IMPLEMENTATION-DECISIONS-v1.md](R1-IMPLEMENTATION-DECISIONS-v1.md).

| Item | Status |
|------|--------|
| Primary language | **Python** — decided |
| Packaging (CLI vs library) | **CLI-first** — decided; packaging details **PARTIAL** |
| Python minor version pin | **PARTIAL** — charter cites 3.12+ in R1 Implementation Charter; not enforced in repo |
| Test framework | **SAFE UNKNOWN** — [R1-TEST-STRATEGY-v1.md](R1-TEST-STRATEGY-v1.md) defines tiers only |

Foundation code (R1.1/R1.2) exists under `runtime/` — **foundation only**, no connector.

---

## Relationship to architecture non-goals

Architecture already excludes: site audit logic, consumer repo merges, Mode 3 write access, orchestration platform. Runtime **inherits** those and adds **engineering-specific** exclusions above.

If a proposed feature fits a consumer or architecture doc better, **stop** — route to correct program or amendment charter.

---

## When something is allowed later

| Change type | Gate |
|-------------|------|
| New connector class (FTP, PMA, DB) | Architecture amendment + runtime charter |
| Mode 3 / write | Explicit future charter — **forbidden** v1 |
| WPilot connected path | Future runtime + architecture phase |
| Unattended production acquisition | Ops charter + security review |

---

## Truth statement

Listing a non-goal here does not imply any runtime feature exists. See [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md).

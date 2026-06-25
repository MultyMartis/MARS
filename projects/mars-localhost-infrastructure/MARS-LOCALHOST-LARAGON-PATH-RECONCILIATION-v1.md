# MARS Localhost — Laragon Path Reconciliation v1

**Document type:** Path reconciliation decision  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-01  
**Status:** **DECIDED**

---

## Decision

| Field | Value |
|-------|-------|
| **Actual install path** | `E:\MARS-Localhost\laragon` |
| **Previous preferred path (MLI-00)** | `E:\MARS-Localhost\runtime\laragon` |
| **Final canonical Laragon root** | `E:\MARS-Localhost\laragon` |
| **Migration** | **NONE** — existing install retained |

---

## Rationale

1. Operator installed Laragon at `E:\MARS-Localhost\laragon` before MLI-01 enablement.
2. Installation is **complete**: executable, `bin`, `etc`, `usr`, `www`, PHP, Apache, MySQL, Composer, Git.
3. Services **start and serve** PHP after MLI-01 configuration.
4. No conflicting data at `runtime\laragon`.
5. Moving install to `runtime\laragon` would add risk with **no operational benefit**.

---

## `runtime\laragon` placeholder

| Field | Value |
|-------|-------|
| **Path** | `E:\MARS-Localhost\runtime\laragon` |
| **State** | Empty directory |
| **Classification** | `DEPRECATED EMPTY PLACEHOLDER` |
| **Cleanup** | **Deferred** — operator-approved removal only |

---

## Compatibility consequences

| Area | Consequence |
|------|-------------|
| **MLI-00 directory standard** | Updated — `laragon\` at D: root is canonical |
| **MLI-00 placement decision** | Superseded path table; install status → **COMPLETE** |
| **MLI-01 enablement input** | Historical — referenced `runtime\laragon` as target |
| **D: README** | Updated to actual paths |
| **Forge WordPress / OCPilot** | Consumer pointers use `E:\MARS-Localhost\laragon` |

---

## Superseded documents (path sections only)

| Document | Change |
|----------|--------|
| [MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md](MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md) | `runtime\laragon\` → `laragon\` |
| [MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md](MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md) | Canonical path + status |
| [reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md) | Historical reference retained |

**Note:** MLI-00 reports are **not** rewritten as if the actual path was known in advance.

---

*Laragon path reconciliation v1 — MLI-01.*

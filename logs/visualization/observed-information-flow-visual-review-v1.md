# Observed Information Flow — Visual Review v1

**Date:** 2026-06-03  
**Lane:** B — MARS Visual Brain Refresh 2026-06  
**Upstream:** `logs/cleanup/discoveries/observed-information-flow-v1.md`

---

## Decision

**Useful** — implement as a **lightweight labelled note** on `infrastructure.canvas` (not a new canvas file, not master/orca).

---

## Rationale

| For visualization | Against separate canvas |
|-------------------|-------------------------|
| Flow is infrastructure-adjacent (intake → registry → archive) | New file would expand pack scope beyond refresh charter |
| Operators already open infrastructure for path/hybrid model | Master canvas is layer-oriented, not process-oriented |
| Single group + text avoids invented edges between programs | Program canvas must not imply orchestration edges |

---

## Implementation

- **Location:** `infrastructure.canvas` — group `n-inf-obs-flow-group` + node `n-inf-obs-flow`
- **Label:** `OBSERVED INFORMATION FLOW — NOT runtime · NOT architecture`
- **Content:** Documented chain with “steps may be skipped” disclaimer

**Not:** runtime subsystem, architecture layer, or mandatory pipeline.

---

## Alternative considered

Dedicated `observed-flow.canvas` — **rejected** (scope creep; no governance request for eighth canvas).

---

*Observed information flow visual review v1 — Task 6 evidence.*

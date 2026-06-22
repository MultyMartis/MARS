# Wave 1.2 Operator Decisions v1

**Date:** 2026-06-23  
**Machine-readable:** [`WAVE-1.2-OPERATOR-DECISIONS-v1.json`](WAVE-1.2-OPERATOR-DECISIONS-v1.json)

---

## W1.2-D1 — Wave 1.1

`APPROVED — IMPLEMENTED AND TESTED`

Checkpoint: `715402f` (`feat(ppc): wire search lifecycle entry points wave 1.1`)

---

## W1.2-D2 — Wave 1

`FINAL LOCKDOWN AUTHORIZED`

---

## W1.2-D3 — Wave 2

`BLOCKED UNTIL WAVE 1.2 OPERATOR REVIEW`

---

## W1.2-D4 — Existing legacy CLIs

Every existing executable Search PPC legacy entry point must be wrapped, gated, downgraded to diagnostic/read-only, or fail-closed with migration instructions. Documentation-only quarantine is insufficient.

---

## W1.2-D5 — Missing components

Components that do not exist may be classified `MISSING — CORRECTLY BLOCKED`. They do not need implementation during Wave 1.2.

---

## W1.2-D6 — Web-GPT boundary

- Repository: `IMPLEMENTED — REPOSITORY ENFORCEMENT`
- UI runtime: `UNAVAILABLE`
- Does not block Wave 2 when repository handoffs are validated

---

## W1.2-D7 — Corvonero

`FROZEN — READ-ONLY ENFORCEMENT TESTS ONLY`

---

## Wave status snapshot

| Wave | Status |
|------|--------|
| Wave 1.1 | `APPROVED — CHECKPOINTED` |
| Wave 1 | `FINAL LOCKDOWN IN PROGRESS` → operator review after 1.2 |
| Wave 1.2 | `IMPLEMENTED — OPERATOR REVIEW REQUIRED` |
| Wave 2 | `BLOCKED` |

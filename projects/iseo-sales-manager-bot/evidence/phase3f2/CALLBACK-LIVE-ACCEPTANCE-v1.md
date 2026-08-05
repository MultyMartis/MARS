# CALLBACK LIVE ACCEPTANCE v1 — Phase 3F.2

## What is confirmed

| Claim | Evidence | Status |
|---|---|---|
| Root cause of `unknown_lead` on a real, present lead is understood | Two independent token algorithms diverging, plus a write-order gap — [CALLBACK-NOT-FOUND-ROOT-CAUSE-v1.md](CALLBACK-NOT-FOUND-ROOT-CAUSE-v1.md) | **CONFIRMED** |
| Token generator (`computeActionToken`) now always uses canonical `fnvToken` | Source diff, `formatter-lib.mjs` | **CONFIRMED (code-level)** |
| Admin Handle Callback verifier aligned to the same canonical `fnvToken` | Forensic fact recorded in repair contract | **CONFIRMED (contract-level)**, not independently re-diffed against a live workflow export in this pass |
| Клиент A's existing card's embedded button token already equals the canonical `fnvToken(lead_id)` | Logical consequence of the token generator already being canonical when that card was formatted | **CONFIRMED by inference**, not by re-clicking the live button |

## What is NOT confirmed (honest gap)

| Claim | Status |
|---|---|
| A live re-click of Клиент A's "processed" button, post-repair, resolving successfully in production | **NOT PERFORMED in this evidence pass** — no new execution forensic (beyond exec `23320`, which predates the repair) was captured showing a successful post-repair callback |
| A fresh synthetic/regression callback probe against the repaired Admin Handle Callback node in the live n8n environment | **NOT PERFORMED** — this evidence pass documents the repair contract, it does not re-run a live click |

## Why this matters

Per charter, this evidence set must not invent a PASS for a live step that was not actually run. The token-unification fix is well-grounded in source (formatter-lib.mjs diff) and in forensic reasoning about why Клиент A's card should now resolve — but the actual button press has not been repeated and observed to succeed as of this evidence pass.

## Status

`PARTIAL — CODE-LEVEL FIX CONFIRMED; LIVE RE-CLICK CONFIRMATION PENDING OPERATOR`

*Related: [CALLBACK-LOOKUP-REPAIR-v1.md](CALLBACK-LOOKUP-REPAIR-v1.md), [EVGENIY-LIFECYCLE-RECONCILIATION-v1.md](EVGENIY-LIFECYCLE-RECONCILIATION-v1.md).*

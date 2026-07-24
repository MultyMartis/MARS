# Next-Phase Decision — Phase 1B-D0

## Selected next phase (exact)

**Phase 1B-D1 — Durable Dedupe Design and Inactive Sandbox Implementation**

## Why this precedes alternatives

| Candidate | Why not first |
|-----------|---------------|
| Runtime Producer Adapter Design and Offline Implementation | Needed, but posting without durable dedupe recreates B2 duplicate accepts with live Telegram risk |
| Controlled Manual Runtime Producer Connection | Unsafe while `DEDUPE_DEFERRED_SANDBOX` remains |

B2 proved duplicate `event_id` acceptance. C1 enabled Pattern B Telegram after accept. Therefore dedupe is the critical path before any runtime producer connection (stage-ordering **A**).

## Scope of D1 (PROPOSED charter shape)

- Design + inactive-sandbox implementation of durable dedupe (preferred: n8n Data Table).
- Prove upsert/lookup semantics with GET-only where possible; controlled inactive workflow mutation only under D1 charter.
- Keep workflow **inactive** unless a narrow temporary activation is explicitly chartered for dedupe tests **without** Telegram side effects if feasible.
- No producer runtime connection; no scheduler; no production activation; no Storage checkout creation unless separately authorized.

## Authorized future mutations (D1 only — not D0)

- Inactive workflow updates for dedupe nodes/logic under explicit D1 charter.
- Create Data Table via API under D1 charter if approved.
- Offline exporter changes **only if** dual-write ledger fallback is selected — prefer n8n-side first.

## Forbidden in D1 unless additional charter text

- Runtime producer connection.
- Scheduler creation.
- Production activation.
- Monitor changes.
- Secret value commits.
- Foreign WIP touches.

## Success criteria (D1)

- Durable dedupe store exists and is evidenced.
- Duplicate `event_id` no longer double-accepts toward Telegram send path.
- Conflict path fail-closed.
- Workflow returned inactive.
- Documentation + validators PASS.
- Security/secret/URL scans CLEAN.

## D0 implementation claim

**None.** D0 is decision-only.

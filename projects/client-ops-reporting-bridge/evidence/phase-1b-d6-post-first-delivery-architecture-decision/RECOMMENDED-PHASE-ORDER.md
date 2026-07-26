# RECOMMENDED PHASE ORDER — Phase 1B-D6

`D6_ROADMAP_DEFINED`

Hypothesis decision: `D6_PRIORITY_HYPOTHESIS_CONFIRMED`
Order: A → B → C → E → D

## D6-1 — Phase 1B-D6A — Durable Post-Telegram Delivery Ledger

- **Goal:** Design + offline implement durable SENT/FAILED update after Telegram; persist sanitized message_id; keep intake_state immutable.
- **Why now:** Proven delivery leaves PENDING; blocks all safe retry/unattended.
- **Mutation class:** Offline workflow compose / harness / docs first; any live apply requires separate charter.
- **Live/offline:** Offline first.
- **Prerequisites:** D6 decision accepted; containment active=false.
- **Exit gate:** Offline harness proves PENDING→SENT on Telegram success and PENDING→FAILED on Telegram failure; no live apply yet unless later charter.

## D6-2 — Phase 1B-D6B — Freshness Semantics Separation

- **Goal:** Separate `source_status` from `delivery_eligibility`; stop stale→BLOCKED rewrite.
- **Why now:** Unattended eligibility otherwise corrupts factual status.
- **Mutation class:** Offline normalizer/adapter/producer gates + tests.
- **Live/offline:** Offline.
- **Prerequisites:** D6-1 design stable enough to not store wrong status.
- **Exit gate:** Tests show aged ATTENTION remains ATTENTION with STALE_REVIEW_REQUIRED eligibility.

## D6-3 — Phase 1B-D6C — Controlled Activation Lifecycle Contract

- **Goal:** Formalize HYBRID ops: C1 default containment; C3 transaction spec for future automation (ready checks, finally-deactivate, emergency).
- **Why now:** Needed before any scheduled activate window.
- **Mutation class:** Docs + tooling hardening; no permanent activation.
- **Live/offline:** Mostly offline; any live activate only under future one-shot charter.
- **Prerequisites:** D6-1/D6-2 in progress or done.
- **Exit gate:** Written C3 state machine + failure handling accepted; still `active=false` by default.

## D6-4 — Phase 1B-D6E — Retry / Concurrency Policy Binding

- **Goal:** Encode failure-class matrix; keep concurrency=1; define reconcile-before-retry.
- **Why now:** Depends on durable delivery states.
- **Mutation class:** Producer policy offline; retries remain disabled until proven.
- **Live/offline:** Offline.
- **Prerequisites:** D6-1 ledger states live in design/impl; D6-2 eligibility rules.
- **Exit gate:** Policy tests; `max_retries` still 0 in production path until explicit later charter.

## D6-5 — Phase 1B-D6D — Unattended Architecture (D2) Design-to-Pilot Charter

- **Goal:** Separate scheduled producer reading completed monitor artifacts (D2); still not production-ready until pilot gates pass.
- **Why now:** Only after A–C–E.
- **Mutation class:** Design then tightly chartered pilot (not open production).
- **Live/offline:** Design offline first.
- **Prerequisites:** D6-1…D6-4 exit gates.
- **Exit gate:** Pilot charter with hard caps; `CLIENT_OPS_UNATTENDED_PRODUCTION_READY` still NO until pilot evidence accepted.

## Immediate next phase (do not start in D6)

**Phase 1B-D6A — Durable Post-Telegram Delivery Ledger Design and Offline Implementation**

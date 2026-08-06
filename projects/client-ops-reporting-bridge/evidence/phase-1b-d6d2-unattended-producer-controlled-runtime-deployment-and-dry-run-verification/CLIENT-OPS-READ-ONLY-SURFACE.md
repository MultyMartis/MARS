# CLIENT-OPS-READ-ONLY-SURFACE

- Transport: reused D6E2 allowlisted GET-only helpers for workflow / executions / Data Table schema / baseline event rows.
- Selected-event ledger GET: allowlisted Data Table path only; UUID-shaped event_id filter; no arbitrary URL.
- Mutation methods mechanically rejected via `assertGetOnlyAction` / `proveReadOnlyInvariant`.
- Used for prestate/poststate baseline and optional selected-event lookup.
- Stale path stopped before ledger GET in this run (`ledger_observation=null`); baseline GETs still executed.

Token: D6D2_CLIENT_OPS_READ_ONLY_SURFACE_ARMED

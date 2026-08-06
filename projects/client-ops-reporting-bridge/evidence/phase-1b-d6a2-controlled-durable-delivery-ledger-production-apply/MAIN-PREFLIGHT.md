# MAIN-PREFLIGHT

## Checks

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD at task start | `5c65ac8817e94ad146c7aee80d876b2290e65ef5` |
| HEAD at task end (foreign concurrent commits; not by D6A2) | `65ab3a973f94c51fccae03c9e48868b75293316b` |
| Client Ops evidence baseline commit (pre-D6/D6A) | `e9c9be59f643e66970930e31339431acb8077b55` |
| Staged snapshot | empty |
| Task index mutations | 0 |
| Git commits by task | 0 |
| Git pushes by task | 0 |

## Foreign WIP

Dirty MAIN contains unrelated `M` / `??` / `D` entries (iseo-report-hub, forge-wordpress, fp-0002, ocPilot, other Client Ops D5R phases, etc.). Treated as **foreign WIP — out of scope**. Not staged, restored, cleaned, or normalized.

## D6A implementation presence

Present under `projects/client-ops-reporting-bridge/`:

- `n8n/runners/lib/client-ops-delivery-ledger.mjs`
- `n8n/runners/lib/client-ops-delivery-ledger-compose.mjs`
- `n8n/harness/delivery-ledger-harness.mjs`
- `n8n/harness/delivery-ledger-cases/`
- `n8n/runners/validate-client-ops-d6a-delivery-ledger.mjs`

**Token:** `MAIN_INDEX_UNTOUCHED_BY_D6A2`

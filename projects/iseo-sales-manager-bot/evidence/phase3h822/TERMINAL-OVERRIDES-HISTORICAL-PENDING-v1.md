# TERMINAL OVERRIDES HISTORICAL PENDING v1

Harness cases 4–5 PASS.

| Scenario | Historical CLEAN | Later authoritative | Eligible |
|---|---|---|---|
| pending → spam | pending @ T1 | spam @ T2 | **false** |
| pending → processed | pending @ T1 | processed @ T2 | **false** |

Old first-row selector would keep pending if the pending row appeared first in sheet order. New selector uses latest authority timestamp across all statuses.

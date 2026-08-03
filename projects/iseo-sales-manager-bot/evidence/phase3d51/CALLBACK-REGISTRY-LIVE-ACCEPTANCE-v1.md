# CALLBACK REGISTRY LIVE ACCEPTANCE v1

| Actor | Callback | Expected |
|---|---|---|
| Андрей (admin/active) | processed | allowed |
| Оля (moderator/active) | processed/spam | allowed |
| Public | any | denied, no CLEAN mutation |
| Revoked moderator | any | denied; CONFIG cannot re-authorize |

Harness tests 21, 22, 29 PASS.

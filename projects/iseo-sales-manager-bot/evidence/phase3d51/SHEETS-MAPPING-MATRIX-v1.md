# SHEETS MAPPING MATRIX v1

| Workflow | Node | Tab | Operation | Header Match | Input Mode | Result |
|---|---|---|---|---|---|---|
| Admin.dev | Read ACCESS_CONTROL | ACCESS_CONTROL | read | PASS | — | PASS |
| Admin.dev | Upsert ACCESS_CONTROL | ACCESS_CONTROL | appendOrUpdate | PASS | RAW | PASS |
| Admin.dev | Append ACCESS_EVENTS | ACCESS_EVENTS | append | PASS | RAW + Prepare ref | PASS |
| Admin.dev | Read Authorization Config | CONFIG | read | PASS | — | PASS |
| Admin.dev | Prepare Access Upsert | — | code flatten | PASS | — | PASS |
| Admin.dev | Unknown Command (/moderators etc.) | ACCESS_CONTROL | read via prior node | PASS | — | PASS |
| Admin.dev | Config Summary | ACCESS_CONTROL | read counts | PASS | — | PASS |
| Admin.dev | Check User Authorization | ACCESS_CONTROL | auth SoT | PASS | — | PASS |
| Admin.dev | Handle Callback Action | — | registry-gated | PASS | — | PASS |

Operational.dev: unchanged this phase (authorization dependency not proven on Ops).

# Post-hardening backup manifest

Location: `...\runtime\backups\post-hardening\`

| Workflow | ID | Active | Nodes |
|---|---|---:|---:|
| Operational.dev | xSnXPy8cEHoZw6xG | true | 45 |
| Admin.dev | wLrLp4WQHm1VJmxz | true | 85 |
| Sales-Manager-v2 | h8I2Tl2yl4uzhUnB | false | 19 |

Rollback order: restore Admin raw → activate; restore Ops raw → activate; keep v2 inactive.

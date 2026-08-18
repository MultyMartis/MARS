# P18C evidence pack

No credentials. SMTP password was never requested, stored in Git, or written here.

| File | What it proves |
|------|----------------|
| `CURRENT-FORMS-MAIL-REALITY.json` | **P18C CURRENT FORMS / MAIL REALITY VERIFIED** (pre-change) |
| `DB-SCHEMA-BEFORE.json` | `fp02_form_leads` did not exist; activity log table existed |
| `LAYER-B-SNAPSHOTS.json` | exact-file SHA before upload |
| `SOURCE-PROD-PARITY.json` | **14/14 MATCH** |
| `POST-DEPLOY-QA.json` | schema v1, lead persist, duplicate, too-fast, QA cleanup, redaction, SMTP state |
| `DEPLOY-QA.json` | lint, parity, suppression ON, indexing closed |
| `SOURCE-SECRET-SCAN.json` | source files: no assigned mailbox secrets |
| `HTTP-SMOKE.json` | public apex still Craftum; WP inner privacy has lead form |
| `_p18c_01_intake.py` / `_p18c_02_deploy_qa.py` | operators for this wave (read secrets locally; do not print them) |

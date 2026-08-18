# Evidence — FP-0002 PROD-P18C-FU01 Admin menu exposure

| File | Role |
|------|------|
| `ADMIN-REALITY-BEFORE.json` | Production menu/hooks/users before fix |
| `ADMIN-MENU-BEFORE.md` | Operator-visible Site Settings list |
| `ROOT-CAUSE.md` | Parent slug mismatch proven |
| `_fu01_01_admin_reality.py` | Read-only intake |
| `_fu01_02_deploy_qa.py` | Exact-file snapshot, lint, deploy, QA |
| `LAYER-B-SNAPSHOTS.json` | Pre-change SHA + `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p18c-fu01-layer-b-pre\` |
| `SOURCE-PROD-PARITY.json` | 4/4 MATCH |
| `POST-DEPLOY-QA.json` | Menu after, settings render, leads, form, SMTP, indexing |
| `ADMIN-MENU-AFTER.md` | Visible list including Почта и формы |
| `SETTINGS-PAGE.md` | Field/password UX |
| `LEADS.md` | Заявки reachability |
| `RUNTIME.md` | SMTP / suppress / indexing |
| `HTTP-SMOKE.json` | Form still on inner origin; apex unchanged |
| `INDEXING.md` | CLOSED |
| `SECRET-REDACTION.md` | No secrets |
| `SOURCE-SECRET-SCAN.json` | Touched-file scan |
| `GIT-CHECKPOINT.json` | Isolated worktree commits (after git wave) |

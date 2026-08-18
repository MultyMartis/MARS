# Save / reload QA

**Required:** `MULTI-RECIPIENT ADMIN SAVE/RELOAD PASS`

Evidence: `POST-DEPLOY-QA.json` (`ok: true`, `ok_checks` all true).

| Case | Result |
|------|--------|
| 1 Existing one recipient loads | PASS — `client.leads@polygon-ws.ru` / `MetaCODE` |
| 2 Add recipient control | PASS — button + `data-fp02-recipients` + JS template. Second row appended client-side (no reload). Server accepts extra posted rows (case 3). |
| 3 Temporary second recipient save/reload | PASS — `fp02.fu02.qa@example.com` / `FU02-QA` persisted then shown on re-render |
| 4 Remove temporary row save/reload | PASS — QA address gone; original row remains 1:1 |
| 5 SMTP password remains CONFIGURED | PASS — YES throughout; blank password field; fingerprint of non-secret SMTP fields unchanged |

Validation extras:

- duplicate emails collapsed case-insensitively; first label kept
- blank rows dropped
- invalid non-empty email rejected; stored list unchanged

QA recipient cleaned. Original operator recipient restored.

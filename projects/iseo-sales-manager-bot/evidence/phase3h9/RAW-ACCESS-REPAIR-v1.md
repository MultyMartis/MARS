# RAW ACCESS REPAIR v1

Deployed on Admin.dev (100 nodes, same ID):

- Check User Authorization hash `CC1C76C24F1BABFF` — emits `deny_reply`
- Answer Callback Deny text expression uses `deny_reply`
- Handle Callback hash `E08EE34CF6EF1FA2` — unauthorized uses deny_reply; missing copy distinct
- Deny Reply hash `C636410485480E2E` — callback_denied = `Недостаточно прав.`

Permissions not broadened. Operational.dev untouched.

# ADMIN EXECUTION PATH FORENSIC v1

## Happy path (intended)

Telegram Trigger → Normalize Command → Read Authorization Config → **Collapse Authorization Context** → Read ACCESS_CONTROL → Check User Authorization → IF Authorized → Route Command → handler → Capture Admin Reply → Safe Telegram Reply

## Incident path (pre-repair)

1. Telegram Trigger — success (1 item)
2. Normalize Command — success (1 item)
3. Read Authorization Config — success (**33 items** = CONFIG rows)
4. Read ACCESS_CONTROL — success (**66 items** = 33× registry fan-out) **or** rate-limit error
5. Check User Authorization — **error** on `require('crypto')` / sha256 helper
6. No downstream reply node executed → **operator silence**

## Last successful node by failing exec

| Pattern | Last success before fail |
|---|---|
| crypto disallow | Normalize + both Sheets reads succeeded; fail at Check User Authorization |
| Sheets quota | Fail at Read ACCESS_CONTROL or Read Authorization Config |

## Post-repair path changes

- Collapse Authorization Context forces **one** command-context item before ACCESS_CONTROL
- Sheets nodes `onError=continueRegularOutput` + `alwaysOutputData`
- Check User Authorization always emits **one** normalized auth item (`registry_found`, `registry_read_ok`, bootstrap markers)
- Pure JS SHA-256 (no Node crypto module)

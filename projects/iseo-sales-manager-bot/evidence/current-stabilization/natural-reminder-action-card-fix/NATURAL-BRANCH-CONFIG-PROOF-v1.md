# NATURAL BRANCH CONFIG PROOF v1

## Requirement

Natural exact-lead branch must use the **same patched nodes** — not a parallel test-only route.

## Patched nodes on production path

| Node | Role on `sm:q:*` path | Patched |
|---|---|---|
| Handle Callback Action | resolver + callback field builder | unchanged (shared) |
| Edit Lead Card Message Pending | in-place pending card + keyboard | **YES — static KB** |
| Aggregate Card Sync Result | post-edit reply shaping | **YES — suppress** |
| Prepare Callback Answer | reply_text for Send path | **YES — honor suppress** |
| Capture Admin Reply | gate before Safe Reply | **YES — skip suppressed** |

## Connection proof (unchanged topology)

`Expand Card Sync Items` → `Edit Lead Card Message Pending` → `Aggregate Card Sync Result` → `Prepare Callback Answer` → `Capture Admin Reply` → `IF Telegram Has Buttons`

No alternate renderer added. No `/leads` branch modified.

## Deploy artifact

`forensic/post-deploy-verify.json` in STORAGE incoming folder confirms all six checks true on live GET after PUT.

Natural callback branch configuration **equals** patched branch.

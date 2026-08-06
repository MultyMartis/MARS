# RUNTIME-POSTSTATE

## Checkouts

| Runtime | Path | HEAD (pre envelope-fix commit) |
|---------|------|----------------------------------|
| Producer | `X:\AI MARS STORAGE\runtime-checkouts\client-ops-site-002-producer\repo` | `9c5d44aa` + local dispatcher patch applied |
| Monitor | `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` | `9c5d44aa` |

## State

| Item | Path |
|------|------|
| Dispatch markers | `...\runtime-state\client-ops-site-002-producer\state\import-completion-dispatch\` |
| Terminal cache | `...\runtime-state\client-ops-site-002-producer\import-terminals\mars-20260806-160514-5d2cdb3b\` |
| Completion artifact | `...\scheduled-monitors\post-1c\completion-dispatch\mars-20260806-160514-5d2cdb3b\` |

## Production PHP

Deployed under SITE-002:

- `storage/mars-tools/cron/mars_1c_import_wrapper.php` (v1.2.0 / D6G)
- `storage/mars-tools/cron/mars_1c_import_run_contract.php`
- Admin `tool/mars_1c_exchange` controller/model/view/language
- `column_left` menu patch

## Notes

- Beget scheduled HTTP gateway remains the scheduled import entrypoint; wrapper is shared with admin enqueue.
- Fixed-time producer script path now points at no-import watchdog only.

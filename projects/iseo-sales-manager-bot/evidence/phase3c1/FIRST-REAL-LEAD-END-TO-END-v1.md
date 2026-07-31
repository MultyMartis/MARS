# FIRST REAL LEAD END-TO-END v1

## Result

**NOT ACCEPTED** — operator website test was not processed end-to-end.

| Gate | Result |
|------|--------|
| Gmail eligible fetch count | **0** for production filter |
| Operational lead execution | **0** |
| RAW v2 row for this lead | **0** |
| CLEAN v2 row | **0** |
| DEDUP_INDEX | **0** |
| LEAD_EVENTS | **0** |
| Telegram manager card | **0** |
| Gmail PROCESSED after Telegram | **n/a** |
| Sales-Manager-v2 duplicate | **0** post-cutover executions |

## Required next operator action

1. Confirm Gmail filter/automation still applies the incoming leads label to website form mail.
2. Submit a **new** website test lead that remains in mailbox (not Trash) **with** the incoming label.
3. Confirm Telegram card + `/status` lead timestamp advance.

# ARCHIVE-LIVE-ACCEPTANCE-v1

Operator-private Admin harness (temporary webhook → Normalize; restored after).

| Test | Result |
|------|--------|
| `/leads 3` | PASS — 3 distinct cards, ordinals 1..3, formula suppressed |
| `/leads 5` | PASS — 5 distinct cards, ordinals 1..5 |
| `/leads 10` | PASS — 5 available unique leads, honest notice, ordinals 1..5 |
| `/leads 7` | PASS — invalid warning text |
| No lifecycle buttons | PASS |
| No n8n attribution | PASS (`appendAttribution=false`) |
| Not sent to manager group | PASS — operator private chat only |

`allPass=true` in local `ARCHIVE-LIVE-ACCEPTANCE.json` (Storage incoming; not committed).

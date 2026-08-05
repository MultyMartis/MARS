# SHEETS CALL BUDGET BEFORE / AFTER v1

| Case | BEFORE | AFTER live proof |
|---|---:|---:|
| Empty-poll CONFIG writes | 1 / 30s (~120/hour) | 0 |
| Schedule | implicit ~30s | `minutesInterval=2` |
| CONFIG reads | broad snapshot in amplified path | 1 |
| ACCESS_CONTROL reads | after earlier broad calls | 1 |
| LEAD_DELIVERIES returned items | ~52 full-tab | **1 bounded item** |
| Claims for two recipients | quota-prone / blocked | 2 |
| Telegram successful sends | blocked in 3E.2.2 proof | 2 |
| Delivered stamps | 0 in blocked proof | 2 |
| CONFIG fallback guards | absent after partial path | 2 reconciled |
| Five later poll sends | 0 while fail-closed | 0 after successful proof |

The final proof had no Sheets quota error. RAW=1 and CLEAN=1; DEDUP behavior remained unchanged.

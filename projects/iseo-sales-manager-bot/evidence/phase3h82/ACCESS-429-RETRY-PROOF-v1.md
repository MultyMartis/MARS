# ACCESS 429 RETRY PROOF v1

Isolated harness (`phase3h82-sheets-429-harness.mjs`), no production customer data.

| Case | Result |
|---|---|
| A. First ACCESS 429, retry succeeds | decision=`SENT`, pending=1, recipients=4, claims=4, successes=4 |
| B. Two sequential ACCESS 429s, later retry succeeds | same; claims generated once |

Harness 23/23 PASS. See `HARNESS-RESULTS.json` cases `A_one_429_then_success`, `B_two_429_then_success`.

Live Admin: ACCESS error → Classify → Wait → same ACCESS node. Build Claims still reads `$('Read ACCESS_CONTROL for Reminder')` after a successful retry.

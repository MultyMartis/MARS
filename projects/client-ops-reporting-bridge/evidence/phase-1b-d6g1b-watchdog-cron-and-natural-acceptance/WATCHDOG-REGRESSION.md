# Watchdog Regression

Offline sandbox via `/usr/local/bin/php8.3 mars_1c_d6g1a_offline_regression.php`:

```json
{
  "phase": "1B-D6G1A",
  "check": "offline-regression",
  "pass": true,
  "results": [
    {
      "id": "R_kill_true_enabled",
      "pass": true,
      "detail": []
    },
    {
      "id": "R_kill_false_blocks",
      "pass": true,
      "detail": []
    },
    {
      "id": "R_kill_alias_server_dispatch",
      "pass": true,
      "detail": []
    },
    {
      "id": "R_kill_default_true",
      "pass": true,
      "detail": []
    },
    {
      "id": "R_ui_blocked_label",
      "pass": true,
      "detail": []
    },
    {
      "id": "R12_kill_false_blocks_webhook",
      "pass": true,
      "detail": []
    },
    {
      "id": "R13_terminal_still_present",
      "pass": true,
      "detail": []
    },
    {
      "id": "R11_kill_true_eligible_not_blocked",
      "pass": true,
      "detail": []
    },
    {
      "id": "R15_recovery_idempotent_already",
      "pass": true,
      "detail": []
    },
    {
      "id": "R5_missing_creates_one",
      "pass": true,
      "detail": []
    },
    {
      "id": "R6_same_date_dedupes",
      "pass": true,
      "detail": []
    },
    {
      "id": "R7_next_day_new_event",
      "pass": true,
      "detail": []
    }
  ],
  "sandbox": "/tmp/mars-d6g1a-7b459147"
}
```

Covers: kill-switch true/false/alias/default; missing-date create; same-date dedupe; next-date new event; idempotent already-delivered.

No production fake missing-import day created. No forced NO_FRESH Telegram.

Gate: `D6G1B_WATCHDOG_REGRESSION_PASS`

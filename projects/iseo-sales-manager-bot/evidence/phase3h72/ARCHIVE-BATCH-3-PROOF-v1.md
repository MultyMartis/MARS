# ARCHIVE BATCH 3 PROOF

limit valid: true
all_keyboard_ok: true

First/middle/last keyboard contract independent of batch size.
```json
{
  "limit_valid": true,
  "items": [
    {
      "index": 1,
      "status": "processed",
      "has_reopen": true,
      "reopen_ok": {
        "inline_keyboard": [
          [
            {
              "text": "↩️ Вернуть в обработку",
              "callback_data": "sm:r:55606b75dd95"
            }
          ]
        ]
      }
    },
    {
      "index": 2,
      "status": "spam",
      "has_reopen": true,
      "reopen_ok": {
        "inline_keyboard": [
          [
            {
              "text": "↩️ Вернуть в обработку",
              "callback_data": "sm:r:546069e256e3"
            }
          ]
        ]
      }
    },
    {
      "index": 3,
      "status": "pending",
      "has_reopen": false,
      "reopen_ok": true
    }
  ],
  "all_keyboard_ok": true,
  "first": {
    "index": 1,
    "status": "processed",
    "has_reopen": true,
    "reopen_ok": {
      "inline_keyboard": [
        [
          {
            "text": "↩️ Вернуть в обработку",
            "callback_data": "sm:r:55606b75dd95"
          }
        ]
      ]
    }
  },
  "middle": {
    "index": 2,
    "status": "spam",
    "has_reopen": true,
    "reopen_ok": {
      "inline_keyboard": [
        [
          {
            "text": "↩️ Вернуть в обработку",
            "callback_data": "sm:r:546069e256e3"
          }
        ]
      ]
    }
  },
  "last": {
    "index": 3,
    "status": "pending",
    "has_reopen": false,
    "reopen_ok": true
  }
}
```

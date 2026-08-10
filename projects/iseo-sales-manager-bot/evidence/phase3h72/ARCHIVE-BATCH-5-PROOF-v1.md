# ARCHIVE BATCH 5 PROOF

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
              "callback_data": "sm:r:d3b306976bc5"
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
              "callback_data": "sm:r:d2b30504f277"
            }
          ]
        ]
      }
    },
    {
      "index": 3,
      "status": "spam",
      "has_reopen": true,
      "reopen_ok": {
        "inline_keyboard": [
          [
            {
              "text": "↩️ Вернуть в обработку",
              "callback_data": "sm:r:d5b309bd792a"
            }
          ]
        ]
      }
    },
    {
      "index": 4,
      "status": "spam",
      "has_reopen": true,
      "reopen_ok": {
        "inline_keyboard": [
          [
            {
              "text": "↩️ Вернуть в обработку",
              "callback_data": "sm:r:d4b3082affdd"
            }
          ]
        ]
      }
    },
    {
      "index": 5,
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
            "callback_data": "sm:r:d3b306976bc5"
          }
        ]
      ]
    }
  },
  "middle": {
    "index": 3,
    "status": "spam",
    "has_reopen": true,
    "reopen_ok": {
      "inline_keyboard": [
        [
          {
            "text": "↩️ Вернуть в обработку",
            "callback_data": "sm:r:d5b309bd792a"
          }
        ]
      ]
    }
  },
  "last": {
    "index": 5,
    "status": "pending",
    "has_reopen": false,
    "reopen_ok": true
  }
}
```

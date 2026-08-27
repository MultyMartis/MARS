# NATURAL-SEND-PATH-PROOF-v1

## Production wiring after deploy (Admin.dev `wLrLp4WQHm1VJmxz`)

| Node | Present | Disabled |
|------|---------|----------|
| Reminder Build Claims | yes | no |
| Merge Reminder Send Payload | yes | no |
| Switch Reminder Keyboard Size | yes | no |
| Send Reminder Telegram KB1…KB8 | yes | no |
| Send Reminder Telegram (ARCHIVED fixed-8) | yes | **yes** |
| Reminder Stamp | yes (downstream of KB*) | no |

## Edge proof

```
Merge Reminder Send Payload → Switch Reminder Keyboard Size
  → Send Reminder Telegram KB{n}  (n = rm_kb_n)
  → Reminder Stamp
```

Switch outputs (order): KB1 … KB8.

Example: KB5 → Reminder Stamp (proven on live workflow graph).

## Implication for next natural reminder

Natural scheduled Send Reminder uses **this same Switch + KB{n} path**, not the archived fixed-8 node.

With flatten fix: unused slots empty; Switch selects exact N; Telegram node emits only N buttons ⇒ **one All** when All is in the digest.

Harness: ADMIN_A acceptance exercised the exact Switch+KB path with live Telegram `reply_markup` All=1.

## Non-action

No production reminder claim was created for this proof.

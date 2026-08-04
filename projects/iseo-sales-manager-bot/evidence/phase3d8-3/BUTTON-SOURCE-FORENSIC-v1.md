# BUTTON SOURCE FORENSIC v1

## Question

Which active production sources create pending lead inline keyboards?

## Contour inspected (GET-only)

| Workflow | ID | Active | Nodes |
|----------|----|--------|------:|
| Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 59 |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 |

## Findings

| Source | Role | Old labels present? | Patch required? |
|--------|------|---------------------|-----------------|
| OPS Format Telegram Lead Card | Builds `telegram_reply_markup` + `telegram_has_buttons` + callback strings | Yes (`buildReplyMarkup`) | **Yes** — button `text` only |
| OPS Send Telegram Lead Card With Buttons | Live Telegram send with top-level `replyMarkup`/`inlineKeyboard` | Yes | **Yes** — button `text` only |
| OPS Send Telegram Lead Card | Plain send (no keyboard) | No | No |
| OPS IF Lead Has Action Buttons | Routes on `telegram_has_buttons` | N/A | No |
| Admin Edit Lead Card Message | Post-action edit (clear markup) | No action labels | No |
| Admin Recent Leads / `/leads` | Archive cards | Intentionally buttonless | No |
| Sales-Manager-v2 / v1 | Inactive / retired | Out of scope | No |

## Conclusion

Active original lead path is the only scope requiring label modification: **Format + Send With Buttons on Operational.dev**. Archive `/leads` cards remain non-actionable. Admin callback graph unchanged.

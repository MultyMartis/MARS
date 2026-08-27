# ADMIN-A-KEYBOARD-ACCEPTANCE-v1

## Constraints honored

- Recipient: ADMIN_A only
- No messages to MOD_B / Olya or other moderators
- No customer messages
- No reminder claim created
- No `last_window` mutation
- Not entered into production pending

## Result

| Metric | Value |
|--------|------:|
| Telegram message_id | 1142 |
| expected logical main buttons (visible) | 4 |
| actual main buttons | 4 |
| All logical expected | 1 |
| All actual | **1** |
| duplicate All | **0** |
| empty callback buttons | **0** |
| reminder claims created by test | **0** |
| last_window mutations by test | **0** |
| moderator test messages (non-ADMIN_A) | **0** |
| customer test messages | **0** |

## Buttons (wire)

1. Audit · 12  
2. Other · 4  
3. Older · 15  
4. All · 16  

SEO omitted because pending SEO count was 0 at test time (correct visibility rule).

## Live clicks (§17)

Not executed after acceptance send. Keyboard uniqueness + offline set sizes used as acceptance for this wave; operator may spot-click ADMIN_A message 1142 if visual confirmation desired.

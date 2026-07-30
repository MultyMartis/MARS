# COMMAND CANONICALIZATION AND ALIASES v1

## Canonical commands

`/help` `/status` `/ai_status` `/health` `/stats` `/last_error` `/config` `/foobar_unknown` `/ai_on` `/ai_off`

## Optional aliases → canonical

| Alias | Canonical |
|-------|-----------|
| /aistatus | /ai_status |
| /lasterror | /last_error |
| /aion | /ai_on |
| /aioff | /ai_off |
| /foobarunknown | /foobar_unknown |

## Normalize Command behavior

1. Trim leading/trailing whitespace
2. Lowercase command token safely
3. Strip optional `@bot_username` suffix
4. Map aliases to canonical values
5. Arguments never participate in privileged command matching
6. Router continues to use exact equals on canonical forms

## Hash

- Normalize Command hash before: `2C2655CBFE9BD1ED`
- Normalize Command hash after: `9C8C854B34B46BEA`

## Authorization

Authorization node and allowlist gate were **not** weakened.

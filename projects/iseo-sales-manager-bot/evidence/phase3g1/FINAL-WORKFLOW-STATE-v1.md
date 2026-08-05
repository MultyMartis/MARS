# FINAL WORKFLOW STATE — Phase 3G.1

**As of live patch wave (sanitized).**

| Workflow | ID | Active | Nodes | Notes |
|----------|-----|--------|------:|-------|
| Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | Template router enrich + Expand personalization + Format heading |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 84 | +2 nodes: reply-profile read + commands; Help lists profile cmds |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | — | unchanged; must stay inactive |

## Flags

- AI / OpenRouter: **OFF** (`OpenRouter AI` node disabled)
- Reminders: **OFF** (unchanged)
- Automatic customer messages: **0**
- Workflows created: **0**
- Access roles restored: **0** (Оля/Никита remain revoked)

## Patched Ops nodes

- Deterministic Lead Processor (approved-route enrich)
- Format Telegram Lead Card (heading)
- Expand Delivery Recipients (per-recipient render)
- Append or Update CLEAN v2 (shared reply metadata columns)
- Append / Upsert LEAD_DELIVERIES (personalized fields)

## Patched Admin nodes / additions

- Help (profile command list)
- Route Command (+6 reply-profile rules)
- Read ACCESS_CONTROL for Reply Profiles (**new**)
- Reply Profile Commands (**new**) → IF Access Registry Write

## Sheets

- ACCESS_CONTROL: additive reply-profile fields seeded for approved display names
- RECIPIENT_REPLIES: tab created (header init row may exist; treat as schema tab)

## Production activation

Deterministic approved templates are **deployed** on Operational.dev for new leads after this patch.  
**Operator visual acceptance still pending** before declaring full human sign-off.

# FINAL WORKFLOW STATE — Phase 3G.1.1

**As of profile seed repair + T1/T3 acceptance inject (sanitized).**

| Workflow | ID | Active | Nodes | Notes |
|----------|-----|--------|------:|-------|
| Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 | Narrow patch: `classifyProbableTest` early-return for `PHASE_3G11_TEMPLATE_ACCEPTANCE_HUMAN` |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 84 | Upsert ACCESS_CONTROL schema aligned with live Q–V profile columns |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | — | unchanged; must stay inactive |

## Flags

| Flag | Value |
|------|-------|
| AI / OpenRouter | **OFF** |
| Reminders | **OFF** |
| Automatic customer messages | 0 |
| Workflows created | 0 |
| Access roles changed | 0 |
| Sole Gmail intake | Operational.dev preserved |

## Sheets state

- ACCESS_CONTROL columns Q–V: **live headers + seeded values**
- TEST_LEADS: 2 acceptance mirror rows appended
- Production LEADS: 0 business acceptance rows claimed

## Profile state

- ADMIN_A → Андрей, enabled, active
- MOD_A → Михаил, enabled, active
- MOD_B_REVOKED → Оля, disabled, revoked
- MOD_C_REVOKED → Никита, disabled, revoked

## Operator gate

Deterministic templates + live profiles **deployed**. Operator visual acceptance of latest T1/T3 cards: **pending**.

# STARTING LIVE EVIDENCE v1 — Phase 3H.4

**Worktree base:** `origin/mars/canonical-post-recovery` @ `380cebd7`  
**Branch:** `agent/iseo-sm-phase3h4-soak-observability-repair`  
**Capture window:** pre-repair observability defects during active Phase 3H soak

## Live contour (starting)

| Workflow | ID | Active | Nodes |
|---|---|---:|---:|
| Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 85 |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 |

## Runtime posture

- AI: **OFF**
- Reminders: **ON** · 10:00 Europe/Moscow
- Active recipients: **3** (ADMIN_A, MOD_A, MOD_B — labels only)
- Revoked: Nikita (MOD_C_REVOKED label)
- Reporting: manual (`только вручную`)
- workflows_created: **0**

## Observed defects (pre-repair)

1. `/reminder_status` silent for Admin — executions **24194**, **24196** (`status=error`)
2. `/status` stale Gmail poll timestamp — `last_poll_success_at` frozen at **2026-08-05T10:34:00.459Z** (= 05.08.2026 13:34 МСК)
3. `/status` wrong last processed lead time — showed **22:23 МСК** from synthetic test delivery, not production lead `lead_19fd2052066e18b7`

## Soak state at discovery

- Soak attempt 1 started **06.08.2026 14:20 МСК** (Phase 3H)
- Polling was running; observability commands misreported live truth

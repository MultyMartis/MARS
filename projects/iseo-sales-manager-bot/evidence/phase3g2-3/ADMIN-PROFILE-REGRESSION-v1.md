# ADMIN PROFILE REGRESSION v1

**Phase:** 3G.2.3

---

## Expected ADMIN_A `/start`

Concise Admin start text remains:

- branding / contour readiness
- role: Администратор
- ИИ / напоминания state lines
- command hints including `/reply_profiles`
- **no** mandatory `Имя в ответах` line (Admin text contract unchanged)

Harness check #27 **PASS**. Live exec **24101** ADMIN_A `/start` success without stale-name defect class.

## Profile inventory unchanged

| # | Label | Name | Enabled | Access |
|---|-------|------|---------|--------|
| 1 | ADMIN_A | Андрей | true | active |
| 2 | MOD_B_REVOKED | Оля | false | revoked |
| 3 | MOD_A | Михаил | true | active |
| 4 | MOD_C_REVOKED | Никита | false | revoked |

No access changes. No renumbering. No restore of revoked users.

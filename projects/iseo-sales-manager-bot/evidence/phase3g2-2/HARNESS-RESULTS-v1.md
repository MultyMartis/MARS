# Harness results — Phase 3G.2.2

**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. New harness

`implementation/harness/phase3g22-harness.mjs` — unified resolver + anti-wipe + config formatting.

```json
{
  "ok": true,
  "passed": 53,
  "total": 53,
  "failed": [],
  "resolver_version": "iseo-reply-profile-resolver-v1.0"
}
```

**53/53 PASS.**

## 2. Coverage groups

| Group | Checks | Result |
|-------|--------|--------|
| Row/identity integrity after rehydrate (unique rows, no duplicates, numbers 1–4 present/unique) | #1–5 | PASS |
| Name restoration (Андрей, Михаил present after rehydrate) | #6–7 | PASS |
| Enabled-state restoration (ADMIN_A, MOD_A true; revoked disabled) | #8–10 | PASS |
| Resolver output completeness + fail-closed fallback rejection (nickname/display-name/username) | #11–14 | PASS |
| Command surfaces (`/reply_profiles`, `/reply_profile 1`/`3`, `/my_reply_profile`, `/start` line) | #15–21 | PASS |
| Resolver version consistency | #22, #29 | PASS |
| No blank active number/name; no false-disabled active profile | #23–25 | PASS |
| Config truth (parser/template/personalization versions, resolver version, Moscow stats formatting, reporting sync, active recipients=2) | #26–32 | PASS |
| AI/reminders OFF flags | #33–34 | PASS |
| No secrets in rendered command output | #35 | PASS |
| Profile mutation regression (`/reply_name_set`, `/reply_name_enable` still functional) | #36 | PASS |
| Access roles unchanged | #37 | PASS |
| Contour/production invariants (Operational/Admin active, v2 inactive, sole intake, zero workflow creation, zero lead loss/duplication) | #38–47 | PASS |
| Personalization draft correctness (Андрей/Михаил intro text, no «Мопс») | #48–50 | PASS |
| Fail-closed wiped-row resolution + rehydrate patch stable-identity keying | #51–52 | PASS |
| Name validation rejects `@username`-style input | #53 | PASS |

## 3. Regression harness (Phase 3G.2 baseline)

`implementation/harness/phase3g2-harness.mjs`:

```json
{
  "ok": true,
  "passed": 42,
  "total": 42,
  "failed": []
}
```

**42/42 PASS** — Phase 3G.2 numbering/text-contract baseline unaffected by the 3G.2.2 patch.

## 4. Combined result

| Harness | Result |
|---------|--------|
| `phase3g22-harness.mjs` | 53/53 PASS |
| `phase3g2-harness.mjs` (regression) | 42/42 PASS |
| Total offline checks this phase | 95/95 PASS |

## Result

- [x] New unified-resolver harness 53/53 PASS
- [x] Prior-phase regression harness 42/42 PASS
- [x] Zero failed checks across both harnesses

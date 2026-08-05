# Operational personalization regression

**Phase:** 3G.2.2
**Status:** FILLED — regression check, no functional change to Operational.dev
**Sanitized labels only:** ADMIN_A · MOD_A
**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. Purpose

Confirm that unifying the reply-profile resolver contract did not regress Operational.dev's recipient-personalization behaviour (the part of the system that actually builds client-facing draft copy on lead cards).

## 2. Check

| Check | Result |
|-------|--------|
| `Expand Delivery Recipients` still resolves `reply_sender_name` from ACCESS_CONTROL only (never Telegram display/username) | PASS |
| Resolver version stamped on Operational output matches Admin.dev's resolver version | PASS — `iseo-reply-profile-resolver-v1.0` on both sides |
| Personalized intro sentence still uses exactly the approved client name | PASS — «Меня зовут Андрей, компания INTLSEO.» / «Меня зовут Михаил, компания INTLSEO.» (harness checks #48–49) |
| Nickname «Мопс» never appears in personalized draft copy | PASS (harness check #50) |
| Node count for Operational.dev unchanged | PASS — 45 nodes active, no structural expansion required |
| `Parse Lead` version stamp unchanged by this phase | PASS — remains `sm-parser-v3.3` |
| Active personalized profiles delivered | 2 (ADMIN_A, MOD_A) |
| Revoked personalized profiles enabled for delivery | 0 |

## 3. Conclusion

Operational.dev required **no structural node changes** for the resolver unification — it already consumed ACCESS_CONTROL profile fields directly rather than through the same `Check User Authorization` code path that caused the Admin.dev wipe. The version-stamp addition (`iseo-reply-profile-resolver-v1.0`) is a labeling alignment, not a behavioural change. This phase's fix is scoped to Admin.dev's authorization/upsert path; Operational.dev's personalization output is regression-tested here and confirmed unaffected.

## Result

- [x] No regression in Operational.dev personalization behaviour
- [x] Resolver version now consistently labeled across both workflows
- [x] Active/revoked recipient counts verified (2 active, 0 revoked-enabled)

# Final workflow state — Phase 3G.2.2

**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

| Workflow | Active | Nodes | Notes |
|----------|--------|------:|-------|
| Operational.dev | true | **45** | sole Gmail intake; personalization regression-checked, no structural change |
| Admin.dev | true | **85** | same workflow patched in place — anti-wipe + rehydrate + unified resolver + config truth |
| Sales-Manager-v2 | false | — | unchanged, inactive |

## Admin.dev nodes touched this phase

| Node | Change |
|------|--------|
| Check User Authorization | anti-wipe projection — `reply_profile_*` fields now included in `rowFromSheet()` output; rehydrate applied |
| Reply Profile Commands | unified resolver v1.0 wiring; auto-rehydrate on profile-command paths |
| Config Summary | Moscow timestamp formatting; parser truth `sm-parser-v3.3`; resolver version line; reporting-sync honesty line; active-recipient count |
| Start | fail-closed reply-name line (no nickname fallback); rehydrate applied before formatting |
| Last-seen upsert (`/start` / `/my_status`) | profile fields now sourced from top-level Prepare output instead of the stripped context, preventing the wipe on write |

## Operational.dev

Unchanged node count (45). Version stamp added on `Expand Delivery Recipients`: `iseo-reply-profile-resolver-v1.0` — labeling alignment only, no structural change (see `OPERATIONAL-PERSONALIZATION-REGRESSION-v1.md`).

## Runtime library state

| File | Status |
|------|--------|
| `implementation/runtime-libs/reply-profile-resolver-v1.mjs` | new — unified resolver contract |
| `implementation/runtime-libs/reply-profile-lib.mjs` | updated — resolver version alias, unchanged validation rules |
| `implementation/runtime-libs/reply-profile-commands-v1.mjs` | updated — re-exports resolver + rehydrate helpers |
| `implementation/harness/phase3g22-harness.mjs` | new — 53/53 PASS |

AI OFF · reminders OFF · workflows created=0

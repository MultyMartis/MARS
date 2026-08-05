# Config truth forensic

**Phase:** 3G.2.2
**Status:** FILLED
**Sanitized labels only:** ADMIN_A · MOD_A
**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. Purpose

Compare what the CONFIG sheet key claimed against what the live Operational.dev `Parse Lead` node actually stamps, and correct any drift so `/config` displays truth rather than a stale cached value.

## 2. Finding

| Field | CONFIG sheet key (stale) | Live `Parse Lead` stamp | Verdict |
|-------|---------------------------|---------------------------|---------|
| Parser version | `sm-parser-v3.2` | `sm-parser-v3.3` | **CONFIG was stale** — display corrected to `sm-parser-v3.3` |
| Resolver version | not previously displayed | `iseo-reply-profile-resolver-v1.0` | New line added to `/config` |
| Reporting sync | not explicitly stated | no active reporting-sync nodes in Operational.dev | Display corrected to «выключена» (honest, not silently omitted) |
| Active recipients | not explicitly stated | 2 (ADMIN_A, MOD_A) | New line added to `/config` |

## 3. Root cause of the parser-version drift

The CONFIG sheet key was written at an earlier phase (`sm-parser-v3.2` was the live value at that time) and was never re-synced when Operational.dev's `Parse Lead` node was subsequently updated to `sm-parser-v3.3` in Phase 3E.1. No code re-reads and re-stamps this particular CONFIG cell automatically; it is a point-in-time snapshot that can go stale whenever the live parser version changes without a matching CONFIG write.

## 4. Reporting sync — honesty check

Operational.dev was inspected for active reporting-sync nodes. None are active. The `/config` summary is corrected to state this plainly (**выключена**) rather than implying reporting is live when it is not stated at all. This is a documentation/display correction, not a functional change to reporting.

## 5. Stats timestamp verification

| Input | Output |
|-------|--------|
| ISO `2026-08-05T13:02:57.000Z` | `05.08.2026 16:02 МСК` (Europe/Moscow, correctly offset) |

Verified programmatically with `Intl.DateTimeFormat('ru-RU', { timeZone: 'Europe/Moscow', ... })` — harness check #30 PASS.

## 6. Counters

| Counter | Value |
|---------|-------|
| config values verified | parser version, resolver version, reporting sync, active recipients, stats epoch |
| AI state | OFF |
| reminders state | OFF |

## Result

- [x] CONFIG stale parser-version key identified and corrected on display
- [x] Reporting-sync display corrected to honest «выключена»
- [x] Stats Moscow-time conversion verified
- [x] Resolver version now surfaced in `/config`

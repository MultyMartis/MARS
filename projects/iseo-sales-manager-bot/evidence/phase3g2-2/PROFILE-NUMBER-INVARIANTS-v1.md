# Profile number invariants — proof

**Phase:** 3G.2.2
**Status:** FILLED
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED
**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. Invariants under test

Numbering contract: `architecture/REPLY-PROFILE-NUMBERING-v1.md`. This evidence confirms the contract held **through** the wipe/rehydrate cycle, not only at initial seed time.

| Invariant | Result |
|-----------|--------|
| `reply_profile_number` immutable across the wipe event | PASS — all 4 rows retained their original number after wipe and after rehydrate |
| Numbers independent of Sheets row order | PASS (harness check #4) |
| Numbers independent of Telegram stable identity value | PASS (harness check #5, #52 — rehydrate keys strictly on stable identity, never invents a number) |
| No renumbering as a side effect of rehydrate | PASS — rehydrate only fills fields that are blank; a present `reply_profile_number` is never overwritten |
| No duplicate numbers after rehydrate | PASS (harness check #3, #5) |
| Revoked profiles (2, 4) remain disabled and ineligible after rehydrate | PASS (harness check #10) |

## 2. Counters

| Counter | Value |
|---------|------:|
| authoritative profile rows | 4 |
| duplicate profile rows | 0 |
| stable profile numbers | 4 |
| blank active profile numbers (after rehydrate contract) | 0 |
| blank active reply names (after rehydrate) | 0 |
| renumbered existing profiles | 0 |

## 3. Final numbering (unchanged seed, restored values)

| № | Label | Client name | Enabled | Access |
|---|-------|-------------|---------|--------|
| 1 | ADMIN_A | Андрей | true | active |
| 2 | MOD_B_REVOKED | Оля | false | revoked |
| 3 | MOD_A | Михаил | true | active |
| 4 | MOD_C_REVOKED | Никита | false | revoked |

## Result

- [x] Numbering invariants proven through the wipe/rehydrate cycle, not only at seed time
- [x] Zero renumbering, zero duplication

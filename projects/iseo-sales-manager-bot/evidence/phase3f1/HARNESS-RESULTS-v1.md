# HARNESS RESULTS v1 — Phase 3F.1

**Result:** PASS — 73/73

| ID | Description | OK |
|---|---|---|
| 1 | Pending lifecycle included | PASS |
| 2 | Processed excluded | PASS |
| 3 | Spam excluded | PASS |
| 4 | Test excluded by default | PASS |
| 5 | One logical lead counted once | PASS |
| 6 | Legacy compatibility pending | PASS |
| 7 | Missing timestamp safe | PASS |
| 8 | Age formatting | PASS |
| 9 | Oldest-first ordering | PASS |
| 10 | Pending count/list consistency | PASS |
| 11 | Pagination page 1 | PASS |
| 12 | Pagination later page | PASS |
| 13 | Invalid page clamped | PASS |
| 14 | HTML escaping | PASS |
| 15 | Telegram message length | PASS |
| 16 | Admin pending_count allowed | PASS |
| 17 | Moderator pending_count allowed | PASS |
| 18 | Revoked denied | PASS |
| 19 | Public denied | PASS |
| 20 | Admin config allowed | PASS |
| 21 | Moderator config denied | PASS |
| 22 | ACCESS_CONTROL read error fails closed (contract) | PASS |
| 23 | Active-recipient snapshot only | PASS |
| 24 | Disabled check sends zero | PASS |
| 25 | Outside-window check sends zero | PASS |
| 26 | Due window zero pending sends zero | PASS |
| 27 | Due window below min count sends zero | PASS |
| 28 | Due window pending sends two reminders | PASS |
| 29 | Revoked sends zero | PASS |
| 30 | Deterministic window key | PASS |
| 31 | Already completed window sends zero | PASS |
| 32 | Partial recipient success does not resend successful recipient | PASS |
| 33 | Ledger read error sends zero (contract) | PASS |
| 34 | Claim failure sends zero (contract) | PASS |
| 35 | Telegram success + stamp uncertainty does not blind resend (contract) | PASS |
| 36 | Three later schedule checks send zero duplicates | PASS |
| 37 | Timezone date boundary helper stable | PASS |
| 38 | Invalid time rejected | PASS |
| 39 | Invalid timezone rejected | PASS |
| 40 | Valid configuration readback | PASS |
| 41 | Restore 10:00 Europe/Moscow | PASS |
| 42 | Final enabled state OFF before acceptance | PASS |
| 43 | Processed lead disappears | PASS |
| 44 | Spam lead disappears | PASS |
| 45 | Repeated callback idempotent (contract) | PASS |
| 46 | Actor attribution unchanged (contract) | PASS |
| 47 | Original action buttons unchanged (contract) | PASS |
| 48 | Archive cards remain non-actionable (contract) | PASS |
| 49 | /my_status regression stub | PASS |
| 50 | /moderator_pending regression stub | PASS |
| 51 | /moderators regression stub | PASS |
| 52 | /leads regression stub | PASS |
| 53 | callback processed regression stub | PASS |
| 54 | callback spam regression stub | PASS |
| 55 | Operational exactly-once unaffected (no Ops patch) | PASS |
| 56 | Parser 3.3 unaffected | PASS |
| 57 | Human Reply Style unaffected | PASS |
| 58 | AI OFF | PASS |
| 59 | automatic client messages=0 | PASS |
| 60 | workflows created=0 | PASS |
| 61 | access changes=0 | PASS |
| 62 | real-client test messages=0 | PASS |
| 63 | destructive migrations=0 | PASS |
| X1 | business pending count snapshot=2+legacy+missingTs | PASS |
| X2 | test leads excluded=1 | PASS |
| X3 | count reply zero | PASS |
| X4 | count reply nonzero | PASS |
| X5 | reminder message useful | PASS |
| X6 | reminder status short | PASS |
| X7 | parse pending args page | PASS |
| X8 | parse pending args test | PASS |
| X9 | age format under 1h | PASS |
| X10 | age format days | PASS |

Business pending in fixture snapshot: 4
With tests: 5
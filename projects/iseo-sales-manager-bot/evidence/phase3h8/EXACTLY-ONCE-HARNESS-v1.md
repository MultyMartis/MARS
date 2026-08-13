# EXACTLY-ONCE HARNESS — Phase 3H.8

## Live selector proofs (pre-quota)
- Dry selector on `lead_clean_v2`: pending_count **≥ 1** (observed 8 non-test)
- ACCESS probe: staff active **4**

## Isolated Telegram harness (TEST-labelled)
Source: private `harness/tg-only.*.json`

| Check | Result |
|---|---|
| zero pending branch | PASS (`zero_pending`) |
| recipients | 4 |
| attempts | 4 |
| delivered | 4 |
| pass2 new sends | 0 |
| test window key | `pending-reminder-TEST:...` (cannot suppress production) |

Offline unit proofs also cover empty/wrong-sheet/test-filter cases.

Sheets-quota limited full ledger write loop; production claim ledger path unchanged and previously proven in Phase 3H.6.

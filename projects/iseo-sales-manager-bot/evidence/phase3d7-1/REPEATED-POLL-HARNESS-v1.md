# REPEATED POLL HARNESS v1

**Runner:** local pure simulation of Expand → Prepare Claims → Stamp → Aggregate  
**Result:** **26/26 PASS** (required ids 1–23 covered)

## Cases

1. one lead, four recipients — PASS  
2. first poll sends exactly four cards — PASS  
3. second poll sends zero cards — PASS  
4. third poll sends zero cards — PASS  
5. delivered rows persist — PASS  
6. stable key identical across polls / no forbidden key parts — PASS  
7. one moderator send failure does not resend Admin — PASS  
8. one moderator retry sends only that moderator — PASS  
9. workflow failure after Telegram success does not resend — PASS  
10. Gmail label failure does not resend delivered cards — PASS  
11. duplicate CLEAN row not created (`business_lead_count=1`) — PASS  
12. duplicate LEAD_DELIVERIES delivered rows not created — PASS  
13. claimed state blocks concurrent poll — PASS  
14. stale claimed state reconciliation — PASS  
15. recipient list unchanged — PASS  
16. recipient added after original delivery does not backfill historical lead — PASS  
17. revoked recipient excluded — PASS  
18. Admin anchor delivered — PASS  
19. Gmail finalization succeeds on admin anchor — PASS  
20. callback idempotency on duplicate cards (contract) — PASS  
21. AI OFF — PASS  
22. client auto-messages=0 — PASS  
23. no new workflows — PASS  

## Code hashes (post-patch)

| Node | Hash prefix |
|---|---|
| Expand | `B890B3D24C339FE7` |
| Prepare Claims | `691CE9CB88BE457A` |
| Stamp | `674C84E16D7F3FB4` |
| Aggregate | `3D1A8133C1228850` |

See `REPEATED-POLL-HARNESS-RESULT.json`.

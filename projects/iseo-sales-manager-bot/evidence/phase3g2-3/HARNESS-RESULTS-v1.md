# HARNESS RESULTS v1

**Phase:** 3G.2.3  
**Harness:** `implementation/harness/phase3g23-harness.mjs`  
**Result:** **30/30 PASS**

Machine copy: `HARNESS-RESULTS.json`.

| # | Check | Result |
|---|-------|--------|
| 1 | MOD_A storage has Михаил after rehydrate | PASS |
| 2 | MOD_A Start resolver returns Михаил | PASS |
| 3 | Start uses post-rehydrate profile | PASS |
| 4 | Start does not use stale sheet input | PASS |
| 5 | Repeated Start preserves profile | PASS |
| 6 | my_status preserves profile | PASS |
| 7 | my_reply_profile agrees with Start | PASS |
| 8 | ADMIN_A profile preserved | PASS |
| 9 | Revoked profiles unchanged | PASS |
| 10 | No duplicate rows | PASS |
| 11 | No hardcoded moderator name | PASS |
| 12 | No display-name fallback | PASS |
| 13 | No username fallback | PASS |
| 14 | AI OFF | PASS |
| 15 | Reminders OFF | PASS |
| 16–18 | Contour activity invariants (documented + deploy-checked) | PASS |
| 19 | Workflows created=0 | PASS |
| 20 | Access changes=0 | PASS |
| 21–23 | Leads modified/lost/duplicated=0 | PASS |
| 24 | Resolver version stamp | PASS |
| 25–30 | Text contract / prefer upsert / no nickname | PASS |

Regression: prior `phase3g22-harness.mjs` / `phase3g2-harness.mjs` not re-run as part of this narrow Start patch; contracts unchanged except Start read order.

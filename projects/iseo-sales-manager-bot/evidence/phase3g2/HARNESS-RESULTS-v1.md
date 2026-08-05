# Harness results — Phase 3G.2

**Phase:** 3G.2  
**Status:** FILLED  
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED  
**Forbidden in this file:** Telegram IDs, workbook IDs, secrets, emails, phones.

## Summary

| Metric | Value |
|--------|------:|
| total | 42 |
| passed | 42 |
| failed | 0 |

**Verdict:** offline harness **42/42 PASS**

## Checks (all PASS)

1. Numbers 1-4 assigned  
2. Numbers unique  
3. Stable across sort  
4. Not row index  
5. Not telegram id  
6. Duplicate rejected conceptually  
7. Next-number allocation  
8. Removed number not reused  
9. `/reply_profiles` content  
10. moderator denied text  
11. `/reply_profile 3`  
12. invalid profile  
13. name set ok  
14. mutation flag  
15. name validation  
16. multi-token rejected  
17. username rejected  
18. URL rejected  
19. emoji rejected  
20. name update readback  
21. revoked name update no access restore  
22. enable valid  
23. enable revoked denied  
24. enable missing name denied  
25. disable preserves name  
26. disable preserves role contract  
27. historical snapshots unchanged  
28. my_reply_profile  
29. admin help lines  
30. mod help role-safe  
31. parse int  
32. parse reject  
33. intro  
34. validation error text  
35. page size  
36. seed plan  
37. ready state  
38. disabled state  
39. AI OFF  
40. reminders OFF  
41. workflows created=0  
42. access roles unchanged  

Harness: `implementation/harness/phase3g2-harness.mjs`  
Source summary: Storage incoming `HARNESS-RESULTS.json`

## Result

- [x] 42/42 PASS

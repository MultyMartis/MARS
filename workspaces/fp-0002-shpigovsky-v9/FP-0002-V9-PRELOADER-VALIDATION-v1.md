# FP-0002 V9 — Preloader Validation v1

**Phase:** V9-03A  
**Automated:** PASS (markup once per page, JS init, fail-safe present)

| Scenario | Expected | Automated |
|----------|----------|-----------|
| First session load | Visible → clears on load | Structural PASS |
| Repeat session | Skipped | sessionStorage gate |
| Fail-safe 3s | Never stuck | JS constant present |
| noscript | Hidden | Markup present |
| BFCache | Immediate hide | JS handler present |
| Reduced motion | Short/no animation | CSS+JS PASS |

**Operator visual confirmation required** before V9-03 checkpoint.

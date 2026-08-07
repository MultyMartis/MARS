# Regression R1–R20

| ID | Result | Notes |
|----|--------|-------|
| R1 | FAIL/PARTIAL | Beget API AUTH_ERROR — watchdog cron not installed/confirmed |
| R2 | PASS (design) | Target timezone Europe/Moscow `0 9 * * *` proven as contour intent; import `0 8` proven |
| R3 | PASS | Watchdog code/gateway server-side; live HTTP invoke independent of workstation |
| R4 | PASS | Live TERMINAL_EXISTS NO_SEND |
| R5 | PASS | Offline missing-run create |
| R6 | PASS | Offline dedupe |
| R7 | PASS | Offline next-day |
| R8 | PASS | Completion poller Disabled |
| R9 | PASS | Producer Disabled |
| R10 | PASS | Runner self-hide; V2 trial popup_observed=false |
| R11 | PASS | Kill switch true eligible |
| R12 | PASS | Kill switch false blocks |
| R13 | PASS | Terminal unaffected |
| R14 | PASS | Watchdog respects kill switch |
| R15 | PASS | Idempotent already-delivered |
| R16 | PASS | Admin field deployed |
| R17 | PASS | Secrets absent from git/evidence |
| R18 | PASS | Workflow active |
| R19 | PASS | No production DT mutation from tests |
| R20 | PASS | Deploy hashes verified |

Overall gate `D6G1A_REGRESSION_PASS`: **PARTIAL** due R1 cron install.

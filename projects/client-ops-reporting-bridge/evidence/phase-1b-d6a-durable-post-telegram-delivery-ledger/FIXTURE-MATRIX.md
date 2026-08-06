# FIXTURE-MATRIX

Offline harness cases under `n8n/harness/delivery-ledger-cases/`.

| Case | ID | Expected | Result |
|------|----|----------|--------|
| 1 FIRST_SEEN + Telegram success | case1_first_seen_telegram_success | FIRST_SEEN / ATTENTION / PENDING→SENT / 1 Telegram | PASS |
| 2 FIRST_SEEN + Telegram definite failure | case2_first_seen_telegram_failure | FIRST_SEEN / ATTENTION / PENDING→FAILED / 1 attempt | PASS |
| 3 duplicate with SENT | case3_duplicate_with_sent | no Telegram / no regression | PASS |
| 4 duplicate with PENDING | case4_duplicate_with_pending | no Telegram replay / stays PENDING | PASS |
| 5 duplicate with FAILED | case5_duplicate_with_failed | no auto retry | PASS |
| 6 Telegram success + ledger write failure | case6_telegram_success_ledger_write_failure | Telegram once / PENDING / no resend | PASS |
| 7 finalizer double-call SENT | case7_finalizer_double_call_sent | idempotent SENT | PASS |
| 8 invalid SENT→FAILED | case8_sent_to_failed_rejected | reject / fail-closed | PASS |
| Extra: compose offline workflow | case_compose_offline_workflow | 20-node put validates | PASS |
| Extra: security metadata | case_security_no_secrets_in_metadata | sanitized class only | PASS |
| Extra: ambiguous leaves PENDING | case_ambiguous_leaves_pending | no finalize | PASS |

Historical live event is **not** used as a mutable fixture; sanitized offline event ids only.

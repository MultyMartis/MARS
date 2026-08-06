# Rollback Plan

1. Workflow: PUT prior Telegram expression / version `449a2c83…` (D6F1A) or intermediate `16fa9214…` if needed; keep active
2. Source: revert formatter / envelope / import_condition patches on canonical
3. Runtime: reset producer checkout to prior canonical commit
4. Do **not** delete Telegram messages or Data Table history
5. Secret rotation: N/A (not performed)

Token: `D6F1B_ROLLBACK_PLAN_READY`

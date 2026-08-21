# PARTIAL RECIPIENT RECOVERY

## Contract

At recovery for the same business window:

| Primary outcome | Recovery |
|-----------------|----------|
| A delivered | SKIP |
| B claimed-only / failed Telegram | retry/send |
| C no attempt | send |

## Proof

Harness case 3: recipients A/B/C with A=delivered, B=claimed → send B+C only.

Post-deliver marks `last_window` only when delivered count ≥ intended count (no premature COMPLETE).

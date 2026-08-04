# BUTTON LABEL REGRESSION v1

## Harness

1. Local offline harness `implementation/harness/phase3d83-harness.mjs` — **30/30 PASS** (`HARNESS-RESULT.json`).
2. Extended live-GET contour checks (Format/Send/Admin nodes) — **35/35 PASS** during patch session (not committed as secrets-dependent runner).

## Required checks (task matrix)

| # | Check | Result |
|---|-------|--------|
| 1 | pending processed label=`✅ Обработано` | PASS |
| 2 | pending spam label=`🚫 Спам` | PASS |
| 3 | processed callback data unchanged | PASS |
| 4 | spam callback data unchanged | PASS |
| 5 | button order unchanged | PASS |
| 6 | pending Admin copy has both buttons | PASS |
| 7 | pending moderator copy has both buttons | PASS |
| 8 | archive card has no buttons | PASS |
| 9 | processed final card says `✅ Обработан` | PASS |
| 10 | spam final card says `🚫 Спам` | PASS |
| 11 | processed feedback unchanged | PASS |
| 12 | spam feedback unchanged | PASS |
| 13–16 | Admin/moderator processed/spam paths present | PASS |
| 17 | actor attribution unchanged | PASS |
| 18 | multi-copy sync nodes present | PASS |
| 19 | buttons removed after action (edit node) | PASS |
| 20 | repeated callback idempotent contract | PASS |
| 21 | revoked denied | PASS |
| 22 | public denied | PASS |
| 23 | delivery exactly-once machinery | PASS |
| 24 | second poll / single schedule | PASS |
| 25 | `/moderator_pending` regression | PASS |
| 26 | `/moderators` active-only | PASS |
| 27 | `/my_status` present | PASS |
| 28 | AI OFF | PASS |
| 29 | client auto-messages=0 | PASS |
| 30 | workflows created=0 | PASS |

Additional: old long labels absent from Format/Send; final processed distinct from action button; node counts 45/59 stable.

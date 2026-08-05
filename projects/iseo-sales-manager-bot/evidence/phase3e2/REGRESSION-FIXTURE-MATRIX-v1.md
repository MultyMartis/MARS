# REGRESSION-FIXTURE-MATRIX-v1 — Phase 3E.2

| ID | Case | Expected |
|----|------|----------|
| H01 | Data contract | sm-reply-v2.0 / sm-msg-v2.4 |
| H02–H09 | Service replies | service-specific; no known re-asks |
| H10–H11 | Alt contact | Telegram not website |
| H12 | Test suppress | no draft |
| H13 | Damaged contact | not ready |
| H14–H17 | Known-info guards | suppress codes |
| H20–H21 | Greeting | name / fallback |
| H22–H27 | Copy UX / length / version | PASS |
| H28–H29 | Archive stored / legacy | PASS |
| H30–H35 | Parser 3.3 A–F | PASS |
| H36–H51 | Delivery/lifecycle/AI OFF contracts | PASS |
| H52 | Max length | ≤900 |

Local harness: **59/59 PASS**.

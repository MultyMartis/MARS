# LIVE ACCEPTANCE DEFECTS v1 — Phase 3F.2.1

## Operator defects (pre-repair)

| Command / surface | Observed | Expected |
|---|---|---|
| `/leads` | lifecycle pending; Услуга/Запрос `—` | processed; service+comment populated |
| `/lead_history 1` | «Команда не найдена» | human-readable history |
| Reporting `Лиды` | source `gmail_form`; reply `true`; last event machine code; historical positional/index garbage class (`27`) | human source; reply text; human event; no index leakage |
| Pending / reminders | PASS (zero pending; reminders OFF) | unchanged |

## Status after 3F.2.1

Defects repaired in Admin.dev + reporting resync. Operator visual acceptance **pending**.

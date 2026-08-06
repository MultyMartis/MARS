# LEADS / LEAD_EVENTS / CONFIG MATRIX v1

| Source | Role | Pre-repair | Post-repair |
|---|---|---|---|
| LEADS | Authoritative lead lifecycle | 1 prod processed @ 17:22 | unchanged |
| LEAD_EVENTS | Authoritative transitions | no extra processed event required for display | unchanged |
| CONFIG `last_production_processed_*` | Cache for `/status` | keys empty | ISO `2026-08-05T14:22:55.186Z` + lead id |
| CONFIG `last_lead_success_at` | Technical/synthetic delivery stamp | 22:23 source | retained; **not** used by `/status` production line |

## Precedence (contract iseo-last-production-processed-v1.0)

1. LEAD_EVENTS production processed (when attached)
2. LEADS processed timestamp
3. CONFIG `last_production_processed_at` cache
4. `нет данных`

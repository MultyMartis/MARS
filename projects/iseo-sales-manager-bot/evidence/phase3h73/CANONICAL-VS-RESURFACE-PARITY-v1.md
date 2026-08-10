# CANONICAL VS RESURFACE PARITY

Both paths use `iseo-canonical-lead-card-renderer-v1` / `formatLeadCard`.

| Field | Normal | Resurface |
|-------|--------|-----------|
| title | 🟢 Новый лид | 🟢 Новый лид |
| status pending | 🕓 Ожидает обработки | same |
| contact | phone/email via isValidContactValue | same |
| reply draft | approved template + personalization | same |
| keyboard | Обработано / Спам | same |
| delivery_reason | (none/initial) | operator_resurface (internal only) |

Human-visible structural parity: **PASS**

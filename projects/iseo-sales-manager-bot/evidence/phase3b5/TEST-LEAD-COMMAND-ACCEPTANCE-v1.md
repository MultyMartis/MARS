# TEST LEAD COMMAND ACCEPTANCE v1

## Decision

**DEFERRED** — full synthetic fixture from Admin.dev would require Execute Workflow / unsafe coupling to Operational.dev or a third workflow.

## Behaviour after polish

- Removed from visible `/help`
- Route retained (operator-only)
- Reply: `Команда временно недоступна до запуска рабочего контура.`
- Harness acceptance: **PASS**
- Deferred to Operational production acceptance / Phase 3C gate

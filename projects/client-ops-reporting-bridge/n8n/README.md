# Client Ops n8n locus

**Status:** PHASE 1B-B + B1 + B2 + C + C0R2 + C0S COMPLETE (real workflow inactive; Telegram not yet applied)
**Live n8n:** one workflow `MARS Client Ops Bridge — bzpm.ru` with native Header Auth bound; Phase 1B-B2 temporary activation used for POST matrix; Phase 1B-C1 applied Pattern B Telegram node (`Telegram Notify Accepted`) with credential `2bIC5376l7ElXb4B`; one sandbox delivery verified; returned `active=false`; executions=25

| Path | Role |
|------|------|
| `templates/` | Baseline inactive sandbox template (committed; historical blocked-auth create source) |
| `harness/` | Offline Node validator + cases + template gates |
| `runbooks/` | Pre-create / create design / apply-rollback |
| `experience-pack/` | Partial — create + auth-binding + POST + Telegram intake + semantics facts |
| `runners/` | Create / credential / auth-binding / activation / authenticated-POST / Telegram intake / semantics / C1 controlled-apply runners |
| `evidence/phase-1b-b-inactive-sandbox-create/` | Sanitized create/re-GET evidence |
| `evidence/phase-1b-b1-auth-binding/` | Sanitized auth-binding evidence |
| `evidence/phase-1b-b2-authenticated-post-validation/` | Sanitized POST matrix evidence |
| `evidence/phase-1b-c-telegram-bot-intake/` | Sanitized Telegram bot/credential intake evidence |
| `evidence/phase-1b-c0s-telegram-integration-semantics/` | Sanitized Pattern B semantics evidence |

See `../CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md`, `../PHASE-1B-B-INACTIVE-SANDBOX-WORKFLOW.md`, `../PHASE-1B-B1-NATIVE-WEBHOOK-AUTH-BINDING.md`, `../PHASE-1B-B2-AUTHENTICATED-SANDBOX-POST-VALIDATION.md`, `../PHASE-1B-C-TELEGRAM-BOT-INTAKE-AND-INTEGRATION-PREPARATION.md`, and `../PHASE-1B-C0S-TELEGRAM-INTEGRATION-SEMANTICS-VERIFICATION.md`.

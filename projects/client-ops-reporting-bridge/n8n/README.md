# Client Ops n8n locus

**Status:** PHASE 1B-B + PHASE 1B-B1 + PHASE 1B-B2 COMPLETE (workflow inactive)
**Live n8n:** one workflow `MARS Client Ops Bridge — bzpm.ru` with native Header Auth bound; Phase 1B-B2 temporary activation used for POST matrix; returned `active=false`

| Path | Role |
|------|------|
| `templates/` | Baseline inactive sandbox template (committed; historical blocked-auth create source) |
| `harness/` | Offline Node validator + cases + template gates |
| `runbooks/` | Pre-create / create design / apply-rollback |
| `experience-pack/` | Partial — create + auth-binding + POST validation facts captured |
| `runners/` | Create / credential / auth-binding / activation / authenticated-POST runners |
| `evidence/phase-1b-b-inactive-sandbox-create/` | Sanitized create/re-GET evidence |
| `evidence/phase-1b-b1-auth-binding/` | Sanitized auth-binding evidence |
| `evidence/phase-1b-b2-authenticated-post-validation/` | Sanitized POST matrix evidence |

See `../CLIENT-OPS-PROGRAMMER-CAPABILITY-EXTENSION.md`, `../PHASE-1B-B-INACTIVE-SANDBOX-WORKFLOW.md`, `../PHASE-1B-B1-NATIVE-WEBHOOK-AUTH-BINDING.md`, and `../PHASE-1B-B2-AUTHENTICATED-SANDBOX-POST-VALIDATION.md`.

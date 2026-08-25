# Reproduce Sales Manager For A New Project

This is a project-neutral playbook. It extracts reusable practice from the stable Sales Manager v2 baseline without copying client-specific data or assuming Sheets as target architecture.

For new projects, use **DATABASE-FIRST persistence**: PostgreSQL as system of record. Sheets may be an optional export/report layer only.

## Phase 0 — Charter

**Objective:** Define product scope, operator, channels, and non-goals.  
**Inputs:** Client need, manager workflow, escalation boundaries.  
**Outputs:** Written charter and authority hierarchy.  
**Gate:** Human accepts scope.  
**Failures:** Hidden CRM scope, unclear operator.  
**What not to do:** Start building workflows from vague chat memory.

## Phase 1 — Runtime Boundary

**Objective:** Choose execution runtime and ownership.  
**Inputs:** n8n host, credentials policy, deployment account.  
**Outputs:** Runtime authority document.  
**Gate:** One production runtime is named.  
**Failures:** Multiple active copies.  
**What not to do:** Claim Git docs execute the bot.

## Phase 2 — Data Model

**Objective:** Separate source, operational lead, events, errors, config, and dedupe.  
**Inputs:** Intake samples without committing PII.  
**Outputs:** PostgreSQL schema draft.  
**Gate:** RAW/source and CLEAN/normalized authority are distinct.  
**Failures:** Reconstructing source from normalized fields.  
**What not to do:** Use Sheets as system of record by default.

## Phase 3 — Intake Contract

**Objective:** Capture complete intake source.  
**Inputs:** Gmail/API/webhook capabilities.  
**Outputs:** Full fetch contract and fixtures.  
**Gate:** Full body captured before parse.  
**Failures:** Snippet-only ingestion.  
**What not to do:** Build source UX from previews.

## Phase 4 — Parser

**Objective:** Produce normalized operational fields while preserving source.  
**Inputs:** Representative safe samples.  
**Outputs:** Deterministic parser with version marker.  
**Gate:** RAW remains literal; CLEAN is useful.  
**Failures:** Parser overwrites source truth.  
**What not to do:** Add AI unless chartered and observable.

## Phase 5 — Identity And Dedupe

**Objective:** Prevent duplicate lead creation and resolve callbacks.  
**Inputs:** Message ids, source ids, lead id strategy.  
**Outputs:** Unique constraints and dedupe keys.  
**Gate:** Re-delivery is distinct from re-ingestion.  
**Failures:** Duplicate cards or duplicate leads.  
**What not to do:** Depend on broad table scans.

## Phase 6 — Manager Card

**Objective:** Create clear Telegram lead card.  
**Inputs:** CLEAN fields, Russian UX labels where needed.  
**Outputs:** Card template and action contract.  
**Gate:** Manager can act without internal noise.  
**Failures:** Too much debug data, missing actions.  
**What not to do:** Expose secrets, raw PII, or internal traces.

## Phase 7 — Lifecycle Actions

**Objective:** Implement minimal statuses.  
**Inputs:** Manager decisions.  
**Outputs:** Processed/spam callbacks and event log.  
**Gate:** Repeated callbacks are idempotent.  
**Failures:** Button races, unclear status.  
**What not to do:** Invent CRM stages prematurely.

## Phase 8 — Raw Source UX

**Objective:** Let manager view original request.  
**Inputs:** Stored source, callback identity.  
**Outputs:** Literal source response.  
**Gate:** No CLEAN substitution; no lifecycle mutation.  
**Failures:** Reconstructed source, IP leakage.  
**What not to do:** Use normalized fields as raw text.

## Phase 9 — Admin Surface

**Objective:** Provide operator commands and callback handling.  
**Inputs:** Authorized users, config keys.  
**Outputs:** Admin workflow/handlers.  
**Gate:** Unauthorized users are denied safely.  
**Failures:** Admin becomes hidden automation.  
**What not to do:** Auto-create task lists without product charter.

## Phase 10 — Reminders

**Objective:** Notify about still-actionable pending leads.  
**Inputs:** Timezone, weekday policy, lifecycle states.  
**Outputs:** Reminder scheduler and candidate query.  
**Gate:** Reminder does not mutate lifecycle.  
**Failures:** Spam/processed included, timezone drift.  
**What not to do:** Mark leads handled because reminder fired.

## Phase 11 — Observability

**Objective:** Make failures diagnosable.  
**Inputs:** Runtime logs, events, errors.  
**Outputs:** Events/errors model and runbook.  
**Gate:** Failure can be traced without secrets.  
**Failures:** Silent callback failures.  
**What not to do:** Store secrets or raw bodies in docs.

## Phase 12 — Security And Secrets

**Objective:** Keep credentials outside docs/code.  
**Inputs:** n8n credentials, secret manager, CONFIG keys.  
**Outputs:** Secret-reference map by name only.  
**Gate:** No secret values in Git.  
**Failures:** Token copied to doc/report.  
**What not to do:** Paste credentials for convenience.

## Phase 13 — Acceptance Fixtures

**Objective:** Validate without leaking PII.  
**Inputs:** Synthetic or sanitized samples.  
**Outputs:** Acceptance matrix and test evidence.  
**Gate:** Tests cover intake, card, actions, raw, reminders.  
**Failures:** Synthetic tests mislabeled as live.  
**What not to do:** Commit real lead bodies.

## Phase 14 — Cutover

**Objective:** Move from test to production safely.  
**Inputs:** Active workflow IDs, config, credentials, rollback.  
**Outputs:** Cutover report.  
**Gate:** One active production contour.  
**Failures:** Legacy copy remains active.  
**What not to do:** Big-bang without rollback.

## Phase 15 — Stable Freeze

**Objective:** Capture accepted baseline.  
**Inputs:** Evidence, workflow IDs, commit hash.  
**Outputs:** Stable baseline docs.  
**Gate:** Human accepts stable status.  
**Failures:** Pending observation claimed PASS.  
**What not to do:** Trigger natural reminders just to fill a matrix.

## Phase 16 — Operations

**Objective:** Run with minimal drift.  
**Inputs:** Runbooks, recovery guide, operator roster.  
**Outputs:** Operational routine.  
**Gate:** Incidents handled through evidence.  
**Failures:** Chat memory replaces docs.  
**What not to do:** Patch blindly during production incidents.

## Phase 17 — Successor Planning

**Objective:** Evolve without destabilizing baseline.  
**Inputs:** Roadmap, migration plan, deferred ideas.  
**Outputs:** Explicit new phase charter.  
**Gate:** Scope and rollback are approved.  
**Failures:** Roadmap treated as active runtime.  
**What not to do:** Mix future PostgreSQL design into current Sheets reality.


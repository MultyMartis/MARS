# MARS Agent Quality — OPERATIONAL INDEX

## Status

`active / minimal v1`

## Entry Points

| Surface | Use |
|---|---|
| `README.md` | Package purpose and exclusions |
| `contracts/agent-contract-v1.md` | Universal agent task contract |
| `templates/task-starter-v1.md` | Cursor/Web-GPT task starter |
| `gates/report-quality-gate-v1.md` | Minimal REPORT completeness gate |
| `templates/failure-record-template-v1.md` | Reusable failure record |
| `checklists/execution-guard-checklist-v1.md` | Practical preflight and halt checklist |
| `reports/aq-01-agent-quality-minimal-surface-v1.md` | AQ-01 execution report |

## Current Phase

`AQ-01 — minimal surface created`

## Core Run

Use AQ package to structure future agent tasks, Cursor prompts, REPORT review, failure records and quality gates.

Do not use it as proof of runtime enforcement.

AQ-01 is `HUMAN_INVOKED` and `NOT_AUTOMATED` unless a later task proves a concrete tool, hook, CI check, or runtime component exists in the repository.

## Owned Surfaces

AQ-01 owns only:

```text
projects/mars-agent-quality/
```

## External Boundaries

AQ-01 references but does not modify or supersede:

- `AGENTS.md`
- `.cursorrules`
- `governance/mars-x-drive-root-authority-v1.md`
- `projects/mars-survivability/`
- `projects/mars-website-factory/`
- `projects/mars-search-ppc-production/`

## Protected Zones

Do not edit protected zones through AQ-01 unless a separate task explicitly scopes the exact path list:

- `governance/`
- `registry/`
- `AGENTS.md`
- `.cursorrules`
- `web-gpt-sources/`
- `projects/mars-survivability/`
- `projects/mars-website-factory/`
- `projects/mars-search-ppc-production/`
- `workspaces/`
- `X:\AI MARS STORAGE\`
- `X:\MARS-Localhost\`

## Stop Conditions

Stop and report `SAFE UNKNOWN`, `NEED HUMAN APPROVAL`, or `SECURITY RISK` when:

- workspace is not `X:\AI MARS`;
- drive label is not `AI WS`;
- branch or task authority is unclear;
- requested paths escape approved scope;
- destructive operations are requested without separate charter;
- remote operations are requested without separate ROL charter;
- REPORT evidence is missing but a PASS claim is requested;
- foreign WIP would be staged, reverted, deleted, cleaned, or overwritten.

## Current Authorized Next Step

Use AQ-01 as a minimal reliability package for future scoped tasks.

No commit, push, remote operation, automated enforcement, runtime implementation, or cross-programme replacement is authorized by this index.

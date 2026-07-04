# Remote Operations Layer — OPERATIONAL INDEX

## Status

`MINIMAL_CHARTER`

## Maturity

`L2 STRUCTURED_CONTRACT` / not implemented runtime

## Entry Points

| Surface | Use |
|---|---|
| [`README.md`](README.md) | Purpose, scope, non-claims, relationships |
| [`contracts/remote-operations-charter-v1.md`](contracts/remote-operations-charter-v1.md) | Normative remote operations charter |
| [`templates/remote-task-starter-v1.md`](templates/remote-task-starter-v1.md) | Remote task starter template |
| [`gates/remote-report-gate-v1.md`](gates/remote-report-gate-v1.md) | Remote REPORT closeout gate |
| [`checklists/remote-preflight-checklist-v1.md`](checklists/remote-preflight-checklist-v1.md) | Remote preflight checklist |
| [`reports/master-11-rol-charter-minimal-surface-v1.md`](reports/master-11-rol-charter-minimal-surface-v1.md) | MASTER-11 execution report |

## Current Phase

`MASTER-11 — ROL charter minimal surface`

## Current Allowed Use

- Prepare remote task charters.
- Enforce checklist review before remote ops are proposed or performed.
- Classify remote evidence requirements and persistence expectations.
- Block unsafe remote tasks (missing identity, environment, approval, backup/rollback, or action class).

## Current Prohibited Use

- Direct remote connection from this package.
- Credential handling, storage, or pasting into chat.
- Automated remote mutation.
- Production changes without operator approval.
- Claiming ROL is a runtime, connector, credential vault, or production control plane.

## Core Run

1. Identify target system.
2. Classify environment: `prod` / `dev` / `stage` / `unknown`.
3. Verify operator approval.
4. Verify credentials are operator-managed and not requested into chat.
5. Require backup/rollback plan.
6. Use remote task starter.
7. Close with remote report gate.

If environment is `unknown` or action class is `UNKNOWN`, **block mutation**.

## Owned Surfaces

ROL owns only:

```text
projects/remote-operations-layer/
```

## External Boundaries

ROL references but does not modify or supersede:

- `AGENTS.md`
- `.cursorrules`
- `governance/` (including evidence persistence and maturity overlay)
- `projects/mars-agent-quality/`
- `projects/mars-survivability/`
- `projects/wpilot/`
- `projects/ocpilot/`
- `projects/metabot-seo-content-agent/`
- `shared/external-access-runtime/`
- `projects/ear-runtime/`

## Protected Zones

Do not edit protected zones through ROL tasks unless a separate task explicitly scopes the exact path list:

- `governance/`
- `registry/` (except explicit ROL registration tasks)
- `AGENTS.md`
- `.cursorrules`
- `web-gpt-sources/`
- `projects/wpilot/`
- `projects/ocpilot/`
- `projects/metabot-seo-content-agent/`
- `shared/external-access-runtime/`
- `projects/ear-runtime/`
- `workspaces/`
- `X:\AI MARS STORAGE\`
- `X:\MARS-Localhost\`

## Stop Conditions

Stop and report `SAFE UNKNOWN`, `NEED HUMAN APPROVAL`, or `SECURITY RISK` when:

- target system identity is unclear;
- environment is `unknown` and mutation is requested;
- action class is `UNKNOWN` and mutation is requested;
- operator approval is missing for remote mutation;
- credentials are requested into chat or agent context;
- backup/rollback plan is missing for write/destructive classes;
- production status is unknown for a live surface;
- evidence requirements cannot be met;
- foreign WIP would be staged, reverted, deleted, cleaned, or overwritten.

## Current Authorized Next Step

Use ROL as a minimal charter package for future remote-facing tasks.

No commit, push, remote connection, credential handling, automated remote mutation, runtime implementation, or programme replacement is authorized by this index alone.

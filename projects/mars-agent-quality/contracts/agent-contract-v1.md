# Agent Contract v1

**Status:** `MINIMAL_V1`  
**Mode:** `HUMAN_INVOKED` / `NOT_AUTOMATED`

## Purpose

Define a universal contract for MARS agent tasks without claiming runtime enforcement.

## Identity

Every agent task must state:

- task id;
- programme or project;
- parent chat / owner when known;
- lane;
- task type;
- operator authority source;
- target root.

## Authority Order

1. Current operator task prompt.
2. `AGENTS.md` and `.cursorrules`.
3. `governance/mars-x-drive-root-authority-v1.md`.
4. Programme OPERATIONAL-INDEX / lifecycle / registry.
5. AQ-01 contract and templates.
6. Referenced helper standards.

If authority conflicts cannot be resolved, stop with `SAFE_UNKNOWN` or `NEED HUMAN APPROVAL`.

## Capability Boundary

Agents may only perform actions allowed by the task scope, available tools, repository evidence, and current mode.

Do not claim:

- autonomous runtime;
- automatic policy enforcement;
- remote operational authority;
- production deployment;
- external system mutation;
- validator execution unless actually invoked.

## Scope Lock

Every task must list exact approved read/write paths.

Default write root for this package:

```text
X:\AI MARS\projects\mars-agent-quality\
```

Empty or ambiguous scope lock is invalid.

## Allowed Actions

Allowed only when listed by the task:

- read scoped files;
- create or edit scoped documentation files;
- run read-only validation commands;
- run task-specific validators;
- produce REPORT with evidence;
- propose staging list without staging.

## Prohibited Actions

- `git add .`
- `git add -A`
- `git commit -a`
- `git stash`
- `git reset`
- `git restore`
- `git clean`
- broad restore
- mass formatting
- cleanup
- moving unrelated files
- editing unrelated files
- recursive delete
- wildcard delete
- root-level operations on `X:\`
- mutation outside approved paths
- remote operations without ROL charter
- claiming runtime implementation without source evidence

## Preflight

Before mutation, verify:

```powershell
Get-Location
Get-Volume -DriveLetter X
git branch --show-current
git status --short
```

Required:

- workspace is `X:\AI MARS`;
- volume label is `AI WS`;
- branch matches task authority;
- git status is read;
- dirty/untracked tree is treated as foreign WIP.

Mismatch on workspace or volume identity means:

```text
STOP — X VOLUME IDENTITY OR WORKSPACE MISMATCH
```

## Evidence

Claims must be backed by task-appropriate evidence:

- file paths;
- git status;
- validation output;
- screenshots;
- checksums;
- receipts;
- logs;
- operator approvals;
- command outputs.

REPORT text alone is not evidence.

## Validation

Run only validation authorized by the task.

If validation is not run, say `SAFE_UNKNOWN` or `not run — out of scope`.

Do not substitute unrelated checks for required evidence.

## Git Discipline

Default:

- no staging;
- no commit;
- no push.

Commit or push only when explicitly requested by the operator.

Recommended staging lists may be shown, but not executed without approval.

## Foreign WIP Protection

Treat pre-existing modified and untracked files as foreign WIP.

Do not delete, move, restore, format, stage, or rewrite foreign WIP.

If foreign WIP blocks the task, stop and ask for operator decision.

## Stop Conditions

Stop when:

- scope is unclear;
- path escapes approved root;
- volume identity fails;
- protected zone mutation is requested without charter;
- destructive operation is requested without exact path list, dry-run, checkpoint, approval, rollback method, and evidence;
- external system mutation is requested without a task-specific authority;
- remote operations are requested without ROL charter;
- validation evidence is missing for a PASS claim;
- repository evidence does not support the requested implementation claim.

## Operator Approval

Operator approval is required for:

- destructive operations;
- remote operations;
- external system mutation;
- protected-zone writes;
- staging, commit, or push;
- maturity promotion;
- waivers of mandatory gates.

Approval must be explicit and scoped.

## SAFE UNKNOWN Usage

Use `SAFE_UNKNOWN` for bounded uncertainty.

Each entry must state:

- what is unknown;
- why it is unknown;
- what evidence would resolve it;
- what action is blocked or still allowed.

## Maturity Inflation Ban

The following are forbidden maturity jumps:

- Roadmap is not implementation proof.
- Report is not Git persistence proof.
- Build PASS is not Visual PASS.
- Cache is not checkpoint.
- Documented policy is not automatic enforcement.
- Validator source is not validator execution.
- Local draft is not registered programme truth.
- Remote Operations Layer mention is not remote operation authority.

## Post-Task Learning

After each non-trivial task, record:

- failure signals found;
- reusable rule candidates;
- missing evidence;
- stop conditions triggered;
- whether a failure record should be created.

Do not promote lessons into global governance without a separate charter.

# AQ Task Starter v1

**Status:** `MINIMAL_V1`
**Mode:** `HUMAN_INVOKED` / `NOT_AUTOMATED`

Use this template for future Cursor/Web-GPT tasks. Fill every field. Do not treat placeholders as authority.

```text
# TASK — <Task ID> — <short task name>

Task ID:
<AQ-XX | programme task id>

Programme:
<frontend | CMS | PPC | research | registry | filesystem | runtime | content | remote operations later | other>

Parent chat / owner:
<chat title/id or operator owner>

Lane:
<implementation | QA | research | registry | filesystem | runtime | content | remote-operations-proposed | other>

Task type:
<read-only audit | scoped implementation | report gate | failure record | validation | other>

Authority files:
- X:\AI MARS\AGENTS.md
- X:\AI MARS\.cursorrules
- X:\AI MARS\governance\mars-x-drive-root-authority-v1.md
- X:\AI MARS\projects\<programme>\OPERATIONAL-INDEX.md
- X:\AI MARS\projects\mars-agent-quality\contracts\agent-contract-v1.md

Scope:
<exact task goal and boundaries>

Out of scope:
- <explicit exclusions>
- Runtime implementation unless task explicitly charters it.
- Automatic enforcement unless source/tool evidence proves it.
- Remote operations unless a separate ROL charter is attached.

Approved write paths:
- X:\AI MARS\<exact approved path>
- X:\AI MARS\projects\<programme>\<exact approved path>

Protected zones:
- X:\AI MARS\governance\
- X:\AI MARS\registry\
- X:\AI MARS\AGENTS.md
- X:\AI MARS\.cursorrules
- X:\AI MARS\web-gpt-sources\
- X:\AI MARS\projects\mars-survivability\
- X:\AI MARS\projects\mars-website-factory\
- X:\AI MARS\projects\mars-search-ppc-production\
- X:\AI MARS\workspaces\
- X:\AI MARS STORAGE\
- X:\MARS-Localhost\

External systems:
<none | Figma | CMS | PPC platform | GitHub | remote host | other>
External mutation authorized:
<no | yes, exact authority and action>

Remote operations:
<not in scope | proposed only | requires separate ROL charter>

Risk class:
<SAFE | LOW RISK | MEDIUM RISK | HIGH RISK | CRITICAL | FORBIDDEN-for-agent-ops>

Allowed commands/actions:
- Get-Location
- Get-Volume -DriveLetter X
- git branch --show-current
- git status --short
- <task-specific read-only validation>
- <task-specific scoped file edits under approved write paths>

Prohibited commands/actions:
- git add .
- git add -A
- git commit -a
- git stash
- git reset
- git restore
- git clean
- broad restore
- mass formatting
- cleanup
- recursive delete
- wildcard delete
- moving unrelated files
- editing unrelated files
- mutation outside approved paths
- remote operations without ROL charter

Preflight:
Run:
Get-Location
Get-Volume -DriveLetter X
git branch --show-current
git status --short

Required:
- workspace = X:\AI MARS
- volume label = AI WS
- branch = <expected branch>
- git status read
- dirty/untracked tree preserved as foreign WIP

Validation:
- <exact validation command or read-only check>
- If not run, report SAFE_UNKNOWN with reason.

Git rules:
- no staging by default
- no commit unless explicitly requested
- no push unless explicitly requested
- recommended staging list may be shown but not executed

Stop conditions:
- workspace or volume mismatch
- scope ambiguity
- protected-zone write not explicitly approved
- destructive operation request without separate charter
- external system mutation not authorized
- remote operations requested without separate ROL charter
- evidence missing for PASS claim
- foreign WIP would be touched

REPORT requirements:
- task id
- scope executed
- files changed
- files created
- files deleted
- commands run
- validation evidence
- git status summary
- foreign WIP preservation
- UNKNOWN / SAFE_UNKNOWN
- risks
- operator approval required or not
- next step
- no commit unless authorized

Completion rule:
Stop after REPORT. Do not continue into next task, staging, commit, push, remote operation, or governance promotion without operator instruction.
```

## Programme Fit

This template is usable for frontend, CMS, PPC, research, registry, filesystem, runtime, content, and later remote operations tasks.

Remote operations remain `EXCLUDED` unless a separate Remote Operations Layer charter authorizes exact systems, credentials boundary, command class, rollback, evidence, and operator approval.

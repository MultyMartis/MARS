# Remote Task Starter v1

**Status:** `MINIMAL_CHARTER`
**Mode:** `HUMAN_INVOKED` / `NOT_AUTOMATED`

Use this template for any task that may touch remote or live external systems. Fill every field. Do not treat placeholders as authority.

Attach or reference:

- `projects/remote-operations-layer/contracts/remote-operations-charter-v1.md`
- `projects/remote-operations-layer/checklists/remote-preflight-checklist-v1.md`
- programme OPERATIONAL-INDEX when applicable (WPilot / OCPilot / MetaBOT / EAR / other)
- AQ task quality surfaces when used

```text
# TASK — <Task ID> — <Task name>

Task name:
<short human-readable name>

Task ID:
<ROL-XX | programme task id>

Target system:
<named system / site / host / workflow>

URL / host label (no secrets):
<public URL, host label, or panel label only>

Environment:
<prod | dev | stage | unknown>

Platform:
<hosting | FTP/SFTP | CMS admin | WordPress | OpenCart/ocStore | DB/phpMyAdmin | API | n8n/MetaBOT | remote files | other>

Requested action:
<exact action requested>

Action class:
<READ_ONLY | LOW_RISK_WRITE | CONFIG_CHANGE | CONTENT_CHANGE | CODE_CHANGE | DATA_CHANGE | DESTRUCTIVE_CHANGE | UNKNOWN>

Allowed scope:
- <exact path / object / panel / table / workflow / file set>
- <no broader scope>

Explicit forbidden scope:
- <what must not be touched>
- Credentials must not be pasted into chat.
- No mutation if environment or action class is UNKNOWN.
- No production change without operator approval.

Credentials boundary:
- Operator-managed only.
- Do not request secrets into chat.
- Do not store or commit credentials.
- ROL is not a credential vault.
- <token/path reference if programme already defines one; never include values>

Backup / rollback plan:
- Backup method:
- Backup location class:
- Rollback method:
- Rollback owner:
- If write/destructive and plan missing: BLOCK

Evidence to collect:
- What was inspected
- What was changed
- What was not changed
- Screenshots / logs / receipts (if any)
- Backup / rollback state
- Credential handling confirmation
- External state SAFE UNKNOWN if not verified

Operator approval status:
<approved | not approved | pending>
Approver:
Approval covers:
- target system
- environment
- action class
- allowed scope
- backup/rollback acceptance

Stop conditions:
- target identity incomplete
- environment UNKNOWN with mutation requested
- action class UNKNOWN with mutation requested
- operator approval missing for mutation
- credentials requested into chat
- backup/rollback missing for write/destructive classes
- unbounded scope
- SECURITY RISK detected

REPORT requirements:
- Use gates/remote-report-gate-v1.md
- List inspected / changed / not changed
- Evidence collected and classification
- Backup/rollback state
- Credential handling confirmation
- External state SAFE UNKNOWN if not verified
- Next action
- Whether operator approval was used
- No commit unless separately authorized

Authority files:
- X:\AI MARS\AGENTS.md
- X:\AI MARS\.cursorrules
- X:\AI MARS\projects\remote-operations-layer\OPERATIONAL-INDEX.md
- X:\AI MARS\projects\remote-operations-layer\contracts\remote-operations-charter-v1.md
- X:\AI MARS\projects\<programme>\OPERATIONAL-INDEX.md (when applicable)
```

## Blocking Reminder

If `Environment` is `unknown` or `Action class` is `UNKNOWN`, mutation is blocked.

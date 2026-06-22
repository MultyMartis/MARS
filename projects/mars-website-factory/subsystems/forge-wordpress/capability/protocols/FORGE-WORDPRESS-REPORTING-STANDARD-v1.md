# Forge WordPress Reporting Standard v1

**Document type:** Mandatory report format for Forge WordPress Cursor tasks  
**Version:** v1  
**Stage:** FW-04

---

## Report heading

Every Forge WordPress Cursor report **must** begin with:

```text
# REPORT — <TASK NAME>
```

Use the exact task name from the operator prompt.

---

## Mandatory sections

| Section | Content |
|---------|---------|
| **Result** | PASS / PARTIAL / FAIL / BLOCKED — one-line summary |
| **Preflight** | Branch, git status note, frontend approval, production check |
| **Inputs** | Authorities loaded; context tier manifest |
| **Scope** | Allowed write, read-only, forbidden — as declared |
| **Files created** | List with paths |
| **Files updated** | List with paths |
| **Validation** | Self-check + independent validator results |
| **Blockers** | Blocking issues or "none" |
| **SAFE UNKNOWN** | Unverified facts and verification path |
| **Git status** | Working tree note — no commit unless explicitly authorized |
| **Next authorized action** | Single clear next step |

---

## Implementation report additions

When task includes code implementation, also include:

| Section | Content |
|---------|---------|
| **Architecture decisions used** | WAD IDs, mode, theme/plugin boundary |
| **Standards used** | FW-S-* and skill IDs applied |
| **Security checks** | Escaping, nonces, capabilities, PHPCS summary |
| **Visual checks** | Parity status or deferred with reason |
| **Deviations from frontend** | Any documented deviation — or "none" |
| **Rollback notes** | How to revert if needed |

---

## Validator report format

```text
# REPORT — <VALIDATOR ID> — <PROJECT OR TASK>

## Verdict
PASS | FAIL | PASS WITH NON-BLOCKING FINDINGS

## Input artifacts reviewed
- <path>

## Blocking findings
- <id>: <description> — or "none"

## Non-blocking findings
- <id>: <description> — or "none"

## Independence
Separate pass: YES | NO
Implementer self-approved: FORBIDDEN for WV6/security

## Escalation
<operator action required> — or "none"
```

---

## Prohibited report patterns

- Claiming OPERATIONAL or production-ready without evidence
- Omitting SAFE UNKNOWN when facts are unverified
- Marking WV6 PASS without operator approval
- Marking handoff ACCEPTED without reviewer gate
- Hiding scope violations

---

## Related

- [FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md](FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md)
- [../../templates/FORGE-WORDPRESS-VALIDATION-REPORT-TEMPLATE-v1.md](../../templates/FORGE-WORDPRESS-VALIDATION-REPORT-TEMPLATE-v1.md)
- [../../../reporting-standard-v0.md](../../../reporting-standard-v0.md) — parent Factory reporting norms

---

*Reporting standard v1.*

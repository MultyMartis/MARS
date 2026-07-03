# Failure Record Template v1

**Status:** `MINIMAL_V1`  
**Mode:** `HUMAN_INVOKED` / `NOT_AUTOMATED`

Use this template for recurring agent-quality failures. Seed examples below are placeholders, not completed records.

```text
# FAILURE — <Failure ID> — <Failure name>

Failure ID:
<AQ-FR-000>

Failure name:
<short name>

Status:
<DRAFT | ACTIVE | SUPERSEDED | CLOSED | SAFE_UNKNOWN>

Affected systems:
- <programme / workspace / external system / agent class>

Trigger:
<what condition exposed the failure>

Failure:
<what went wrong>

Cause:
<known cause or SAFE_UNKNOWN>

Detection:
<how it was detected>

Impact:
<what was affected or could be affected>

Prevention:
<required prevention rule or check>

Required check:
<exact check to run or human review to perform>

Stop condition:
<when agent/operator must stop>

Evidence:
- <file path / git status / screenshot / checksum / receipt / command output>

Known examples:
- <incident / report / task id>

Affected agents:
- <Cursor | Web-GPT | specialized agent | human-invoked helper | SAFE_UNKNOWN>

Reusable rule:
<portable rule for future task starters or gates>

Related gates:
- <report-quality-gate-v1 | programme gate | operator approval>

Post-task learning:
<what should be reused, not generalized, or escalated>
```

## Seed Examples As Placeholders

These are candidate failure classes for future records. They are not complete records in AQ-01.

| Placeholder | Typical failure shape |
|---|---|
| Destructive filesystem action | Agent deletes, cleans, or rewrites outside scoped approval |
| False Green | PASS claimed from incomplete evidence |
| Text Hallucination | Agent invents repo facts, implementation status, or external results |
| Asset Identity Collision | Wrong brand-critical asset selected from mixed design source |
| Mixed Authority | Current task, programme index, and governance authority are blended incorrectly |
| Broad Git Staging | Agent stages unrelated foreign WIP |
| Invalid Semantic Resume | Agent resumes stale task context after scope changed |
| Build PASS Mistaken For Visual PASS | Technical build success reported as product/visual acceptance |
| Runtime Claims Without Evidence | Documentation or roadmap described as existing runtime |

## Use Rules

- Keep each failure record scoped and evidence-backed.
- Use `SAFE_UNKNOWN` instead of guessing cause or impact.
- Do not promote a placeholder into programme law without separate operator charter.
- Do not claim automatic detection unless a real tool and invocation evidence exist.

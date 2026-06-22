# Forge WordPress Cursor Task Template v1

**Document type:** Reusable Cursor task shell  
**Version:** v1  
**Stage:** FW-04

Copy this template for every Forge WordPress Cursor task. Replace `<PLACEHOLDER>` values.

---

```markdown
# TASK — <TASK NAME>

## TARGET FOLDER
`<absolute or repo-relative project path>`

## CURSOR MODE
Agent

## PROJECT ID
<project slug or NOT ASSIGNED for synthetic>

## CURRENT STAGE
<FWP-xx or capability phase — e.g. architecture, implementation, validation>

## OBJECTIVE
<One paragraph — what this task must produce>

## INPUT AUTHORITY
- <path> — <role>
- Specialist: capability/primary-specialist/FORGE-WORDPRESS-IMPLEMENTATION-SPECIALIST-v1.md
- Execution contract: capability/protocols/FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md
- Skill(s): capability/skills/<SKILL-FILE>

## ALLOWED WRITE SCOPE
- <path>/

## READ-ONLY SCOPE
- <approved frontend path>/
- projects/mars-website-factory/subsystems/forge-wordpress/

## FORBIDDEN SCOPE
- Production hosting
- Unrelated projects
- agents/registry.md
- WordPress core edits
- <project-specific forbidden paths>

## REQUIRED INPUTS
- [ ] Approved frontend / handoff manifest
- [ ] Project intake (if project-bound)
- [ ] Prior artifacts: <list>
- [ ] Operator approval for stage: <yes/no/N/A>

## REQUIRED OUTPUTS
- [ ] <artifact 1>
- [ ] <artifact 2>
- [ ] REPORT per FORGE-WORDPRESS-REPORTING-STANDARD-v1.md

## IMPLEMENTATION RULES
- Follow execution contract stages 1–10
- No implementation before approved plan (if applicable)
- No production commands
- Full files only — no silent fragments
- SAFE UNKNOWN for unverified facts

## VALIDATION
- Self: <skill or validator>
- Independent: <FW-V-xx if required>
- Operator gate: <yes/no — e.g. WV6>

## STOP CONDITIONS
- Frontend not approved
- Missing WAD / content model (when required)
- Scope violation
- Production target detected
- Blocking validator finding
- Secrets exposed

## GIT POLICY
- Preflight status required in report
- No commit unless explicitly authorized in this task

## REQUIRED REPORT
# REPORT — <TASK NAME>
(sections per FORGE-WORDPRESS-REPORTING-STANDARD-v1.md)
```

---

## Related

- [FORGE-WORDPRESS-PROMPT-PACK-v1.md](FORGE-WORDPRESS-PROMPT-PACK-v1.md)
- [../protocols/FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md](../protocols/FORGE-WORDPRESS-SPECIALIST-EXECUTION-CONTRACT-v1.md)

---

*Cursor task template v1.*

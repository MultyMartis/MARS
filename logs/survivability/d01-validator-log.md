# Validator Log — D-01 Drill

**Log id:** `validator-20260524-d01-drill`  
**Timestamp:** `2026-05-24T01:23:00Z`  
**Severity:** INFO  
**Operator:** cursor-agent-d01-drill  
**Lane:** B  
**Related task / chat:** D-01 Sandbox Survivability Drill

## Summary

First operational validator drill completed. Six cases run via CLI. ALLOW, NEED_HUMAN, and DENY decisions all verified. Full results in tool report.

## Evidence

- Tool: `projects/mars-survivability/tools/validator/scoped-operation-validator-v1.mjs`
- Report: `projects/mars-survivability/tools/validator/reports/d01-validator-results.md`
- Registry: `validator-rules-registry-v1.json`

## Actions taken

- Ran safe-example-02 (git status) → ALLOW
- Ran sandbox scoped write → NEED_HUMAN (PZ-14 parent zone)
- Ran dangerous examples 01–03 → DENY
- Ran governance write case → NEED_HUMAN

## Follow-up

- Document FP-01: sandbox writes inherit workspaces/ NEED_HUMAN
- Consider registry tuning for Q-tier sandbox exemption in future drill

## SAFE UNKNOWN

- No hook integration tested — CLI only

---

*End of validator log.*

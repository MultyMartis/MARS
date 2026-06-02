# Survivability Agent Handoff Checklist (v1)

**Status:** **documented** — paste block when opening new chat after drift or phase boundary.  
**Time target:** < 3 minutes

**Drift protocol:** [chat-context-drift-protocol-v1.md](../protocols/chat-context-drift-protocol-v1.md)

---

## Handoff block (copy to new chat)

```text
=== MARS AGENT HANDOFF v1 ===

Prior chat: <closed — reason: lane switch | workspace switch | summarization | incident | N phases>

CARRY FORWARD:
- Lane: <A|B>
- Workspace/domain: <absolute path>
- Git ref: <branch + short SHA or SAFE UNKNOWN>
- Snapshot id: <snap-... or none>
- Risk class of next work: <class>
- Open SAFE UNKNOWN: <list or none>

DO NOT CARRY (re-verify):
- Implicit cleanup authority
- Relative paths from old session
- "Almost done" without file list

NEXT TASK:
<paste fresh safe-agent-task-template-v1 block>

=== END HANDOFF ===
```

## Operator verification

- [ ] Fresh [safe-agent-task-template-v1.md](safe-agent-task-template-v1.md) pasted — not partial
- [ ] Prior snapshot id still valid or new snapshot planned
- [ ] No recovery-in-progress without quarantine manifest reference
- [ ] Chat named per lane/workspace/phase
- [ ] FORBIDDEN ops restated in new block

## Agent first response (expected)

- Restate allowed root in one sentence
- Confirm read-only location if shell used
- Refuse if handoff block incomplete

---

*End of Agent Handoff Checklist v1.*

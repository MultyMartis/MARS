# Chat Context Drift Protocol (v1)

**Status:** **documented** — human-operated discipline for long Cursor sessions on MARS.  
**Not:** session telemetry, automated drift detector, or summarization control product.

**Incident class:** [incident-analysis-cursor-agent-context-drift-v1.md](../reports/incident-analysis-cursor-agent-context-drift-v1.md)  
**Halt protocol:** [operational-halt-protocol-v1.md](operational-halt-protocol-v1.md)  
**Enforcement:** [enforcement-rules-registry-v1.md](../registries/enforcement-rules-registry-v1.md) §7

---

## 1. Purpose

Context drift is the **primary precursor** to destructive scope exit. This protocol defines detection signals, mandatory new-chat boundaries, and re-anchoring steps — **documentation only**, not IDE enforcement.

---

## 2. Drift mechanisms

### 2.1 Long-session degradation

| Signal | Effect |
|--------|--------|
| Many phases in one chat | Goal stack compresses; early constraints lost |
| Mixed audit + implement + recovery | Lane and mode blur |
| Terminal output scrollback loss | cwd and path history unreliable |

**Mitigation:** Checkpoint every major phase; consider new chat after N phases (see §5).

---

### 2.2 Summarization drift

| Signal | Effect |
|--------|--------|
| Cursor summary event | Scope lock, ALLOWED PATHS, snapshot id may drop |
| "Continuing from summary…" | Model retains task intent, loses path anchor |
| User assumes agent remembers lock | Invalid — restate mandatory |

**Mitigation:** After any summarization → **re-paste full safe task template** or **new chat**.

---

### 2.3 Lane confusion

| Signal | Effect |
|--------|--------|
| Lane B task touches `workspaces/*/src` | Governance vs implementation bleed |
| Lane A task edits `governance/` | Accidental policy mutation |
| Parallel chats same clone | Uncoordinated writes |

**Mitigation:** One lane + one workspace per AGENT chat; name: `Lane<A|B>-<target>-<phase>`.

---

### 2.4 Multi-project contamination

| Signal | Effect |
|--------|--------|
| Retrieval surfaces sibling project paths | Wrong workspace in plan |
| Shared partial names (`triumph`, `landing`) | v4/v5 mix |
| Repo-wide search in mutation task | Cross-project edits |

**Mitigation:** Absolute paths in ALLOWED PATHS; verify workspace slug in first agent response.

---

### 2.5 AGENT memory collapse

| Signal | Effect |
|--------|--------|
| Agent cites wrong file paths | Hallucinated or stale paths |
| Agent proposes ops on deleted paths | Stale context |
| Contradicts prior REPORT | State desync |

**Mitigation:** HALT; read-only `git status` + list dir; new chat with fresh template.

---

### 2.6 Path-anchor loss

| Signal | Effect |
|--------|--------|
| Relative paths without root | cwd-dependent expansion |
| "The workspace" without name | Ambiguous target |
| Recovery reframing | "Fix" → cleanup scope |

**Mitigation:** TARGET FOLDER restatement; halt if multiple candidates.

---

### 2.7 Recovery-loop drift

| Signal | Effect |
|--------|--------|
| Failed fix → "delete and retry" | F-10, X-09 |
| Second agent pass after incident | Amplifies damage |
| Cleanup after partial restore | Deletes evidence |

**Mitigation:** Quarantine protocol; human shell; **mandatory new chat** after incident.

---

## 3. Detection checklist (operator)

After any long session or ambiguous agent reply, verify:

- [ ] Scope lock still present in prompt context
- [ ] ALLOWED PATHS match actual work
- [ ] Lane matches paths (A → one workspace; B → docs/projects pack)
- [ ] cwd reported matches TARGET FOLDER
- [ ] No cleanup/fresh/wipe language accepted without paths
- [ ] Snapshot id still valid for in-progress MEDIUM+ work

If any fail → treat as **drift** → §4 or §5.

---

## 4. Re-anchoring (same chat — limited)

Allowed **once and only if** no incident and no summarization since last valid lock:

1. Operator pastes updated [safe-agent-task-template-v1.md](../templates/safe-agent-task-template-v1.md) in full  
2. Agent restates allowed root in one sentence  
3. Agent runs read-only location check  
4. Resume — **no destructive ops** until human confirms

If summarization occurred → prefer §5 new chat instead.

---

## 5. MANDATORY NEW CHAT

Start a **new** Cursor chat (fresh context) when:

| Trigger | Why |
|---------|-----|
| **After recovery incident** | Contamination narrative must not persist |
| **After lane switch** | A ↔ B discipline reset |
| **After workspace switch** | One workspace per session rule |
| **After summarization event** | Scope lock unreliable |
| **After >N major phases** | Default **N = 3** major phases (audit → implement → verify counts as 3) |
| **After filesystem incident** | Any unintended delete or quarantine |
| **After HALT L3+** | Escalation per operational-halt-protocol |
| **After guardrails policy change** | Re-read enforcement registry |

**Handoff:** Use [survivability-agent-handoff-checklist-v1.md](../templates/survivability-agent-handoff-checklist-v1.md).

---

## 6. Forbidden after drift detected

- Proceed with destructive shell  
- "Quick fix" without quarantine  
- Expand scope to "clean up"  
- Trust agent memory of paths  
- Skip snapshot because "we already did earlier in chat"

---

## 7. SAFE UNKNOWN

- Whether Cursor exposes reliable summarization markers to operator — **verify in UI**  
- Optimal N for major phases — default 3; tune from incident evidence  

---

## 8. Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — G1 chat context drift protocol |

---

*End of Chat Context Drift Protocol v1.*

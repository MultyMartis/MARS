# MARS Survivability Scorecard (v1)

**Status:** **documented** — qualitative audit as of 2026-05-23.  
**Method:** Repo evidence + incident class analysis; not automated metrics.  
**Ratings:** **LOW RISK** · **MEDIUM RISK** · **HIGH RISK** (lower is better for survivability).

---

## 1. Summary table

| Domain | Rating | Trend | One-line rationale |
|--------|--------|-------|-------------------|
| Filesystem survivability | **HIGH RISK** | ↓ after incident | No enforced protected zones or sandbox |
| Git survivability | **MEDIUM RISK** | → | Good culture docs; dirty tree + untracked assets common |
| Workspace isolation | **HIGH RISK** | → | Single clone, multi-chat, soft lane rules |
| Rollback readiness | **HIGH RISK** | → | No GitGuard; `_snapshots/` not standard |
| Snapshot discipline | **HIGH RISK** | → | Ad hoc; no manifest convention in use |
| Recovery speed | **MEDIUM RISK** | → | Git helps tracked files; emergency prompts unsafe |
| Prompt safety | **MEDIUM RISK** | ↑ | New destructive policy + scope lock templates |
| Agent safety | **HIGH RISK** | ↓ incident | AGENT + shell + drift = proven failure mode |
| Operational resilience | **MEDIUM RISK** | ↑ | Strong governance corpus; weak execution hooks |
| Chaos resistance | **HIGH RISK** | → | Recovery loops amplify damage |

**Overall survivability posture:** **HIGH RISK** for agent-driven filesystem work; **MEDIUM RISK** for human-only doc/governance work.

---

## 2. Filesystem survivability — **HIGH RISK**

**Evidence:**

- Agent can run recursive delete ([incident-analysis](incident-analysis-cursor-agent-context-drift-v1.md)).  
- `.cursorrules` prohibits delete but **not enforced**.  
- No `workspaces/_snapshots/` standard observed.  
- Monorepo size increases blast radius.

**Hardening:** destructive-operations-policy, safe-execution-layer, GitGuard G0–G2.

---

## 3. Git survivability — **MEDIUM RISK**

**Evidence:**

- [04-workflows__git-rules.md](../../../web-gpt-sources/04-workflows__git-rules.md) — milestone discipline.  
- Default no commit reduces accidental pushes.  
- Large dirty working trees (git status at audit start).  
- Untracked images/docs may exceed git recovery.

**Gaps:** agent `git clean` / `reset --hard` not blocked technically.

---

## 4. Workspace isolation — **HIGH RISK**

**Evidence:**

- [parallel-cursor-chat-work-mode-v0.md](../../../governance/parallel-cursor-chat-work-mode-v0.md) — discipline only.  
- Multiple `workspaces/triumph-*` versions coexist.  
- Lane A/B forbidden lists not machine-enforced.

---

## 5. Rollback readiness — **HIGH RISK**

**Evidence:**

- GitGuard **not implemented** ([mars-reality-index-v0.md](../../../governance/mars-reality-index-v0.md)).  
- WPilot documents rollback-first for plugin — separate system.  
- Factory failure-recovery governance exists — **doc only**.

---

## 6. Snapshot discipline — **HIGH RISK**

**Evidence:**

- No repo-wide snapshot manifest.  
- git-rules encourage milestone commits — **sparse** for WIP.  
- Design assets often untracked.

---

## 7. Recovery speed — **MEDIUM RISK**

**Strengths:** git checkout for tracked; documented Factory recovery modes.  
**Weaknesses:** emergency prompts favor fast delete-recreate; increases total recovery time after mistake.

---

## 8. Prompt safety — **MEDIUM RISK**

**Strengths:** AGENTS.md honesty; maintenance mode prune rules.  
**Weaknesses:** vague “cleanup” still usable; scope lock not mandatory until v1 survivability pack.  
**Improvement:** mars-survivability contracts/protocols added 2026-05-23.

---

## 9. Agent safety — **HIGH RISK**

**Evidence:** incident class; tool-safety-model not wired; Delete + Shell available in AGENT.

**Mitigation path:** GitGuard validator + Cursor hooks (future).

---

## 10. Operational resilience — **MEDIUM RISK**

**Strengths:**

- Phase S3–S8 survivability governance  
- operational-survivability, reality audit framework  
- Factory context-survivability layer  
- tools: governance-scanner, markdown-link-validator (read-mostly)

**Weaknesses:** documentation ≠ enforcement; operator load / fatigue documented.

---

## 11. Chaos resistance — **HIGH RISK**

**Failure modes:**

- Multi-chat + recovery loop + agent cleanup  
- rebuild-from-memory  
- governance expansion during emergency  

---

## 12. Scoring rubric (for v2)

| Rating | Criteria |
|--------|----------|
| LOW | Technical control + doc + verified drill |
| MEDIUM | Strong doc; partial manual discipline |
| HIGH | Known failure without control |

Future: score only after GitGuard G1 pilot + one restore drill.

---

## 13. Priority actions (from scorecard)

1. Mandate scope lock in AGENT prompts (immediate, zero code).  
2. Create `workspaces/_snapshots/` convention + first manual snapshot (G0).  
3. Pilot GitGuard rollback map for one workspace (G1).  
4. Evaluate Cursor shell hook for deny patterns (G3 — SAFE UNKNOWN feasibility).  
5. Never agent-recover from delete incident without human filesystem triage.

---

*End of MARS Survivability Scorecard v1.*

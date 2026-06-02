# Cursor Agent — Operational Risk Analysis (v1)

**Status:** **documented** — risk register for Cursor AGENT/ASK usage on MARS.  
**Date:** 2026-05-23

---

## 1. Executive summary

Cursor agents combine **full user OS privileges**, **non-deterministic reasoning**, and **session state loss** via summarization. MARS mitigates with **documentation** ([AGENTS.md](../../../AGENTS.md), [.cursorrules](../../../.cursorrules)) but lacks **technical enforcement**. Residual risk is **HIGH** for destructive filesystem operations without GitGuard phase G2+.

---

## 2. Context drift

| Aspect | Risk | Mitigation (v1 doc) |
|--------|------|---------------------|
| Summarization drops path literals | Wrong target directory | Scope lock re-anchor; CHECKPOINT.md |
| Goal persistence without constraints | “Cleanup” expands | destructive-operations-policy F-* |
| Confabulated file paths | Edit/delete wrong file | List-dir verify; SAFE UNKNOWN |
| Lost “do not touch” | Protected zone hit | protected-zones-registry |

**Severity:** **HIGH** — direct link to incident class.

---

## 3. Workspace confusion

| Scenario | Outcome |
|----------|---------|
| Multiple folders open | Edits outside MARS |
| Wrong workspace in @-mention | Partial rules |
| `workspaces/v4` vs `v5` coexist | Mixed partials |
| Project doc vs implementation path | Governance edit instead of src |

**Severity:** **HIGH** for Lane A production.

---

## 4. Cross-project contamination

- Single repo contains ORCA, Factory, wpilot, triumph, mars-survivability.  
- Broad grep + replace poisons unrelated packs.  
- Agent “helpfully” normalizes names across `projects/`.

**Mitigation:** scope lock; Lane B forbids routine `workspaces/*` edits.

**Severity:** **MEDIUM–HIGH**.

---

## 5. Indexed repo bleed

Cursor codebase index retrieves **semantically similar** content across the monorepo. Risk:

- Copy patterns from wrong project  
- Apply triumph-specific hacks to unrelated landing  
- Reference deprecated web-gpt-sources as current SoT  

**Mitigation:** cite SoT path in task; INDEX-first discipline.

**Severity:** **MEDIUM**.

---

## 6. Long-session degradation

| Hour mark | Typical degradation |
|-----------|----------------------|
| 0–2 | High adherence to rules |
| 2–4 | Summaries; omitted caveats |
| 4+ | Invented continuity; urgency bias |

**Mitigation:** new chat per phase; written checkpoint.

**Severity:** **HIGH** for destructive ops.

---

## 7. Undo / recovery instability

- Editor undo ≠ shell delete recovery  
- Git does not cover untracked assets (images, new pages)  
- Agent may run **second** destructive “fix”  

**Severity:** **HIGH** after first mistake.

---

## 8. AGENT vs ASK risk profile

| Dimension | ASK | AGENT |
|-----------|-----|-------|
| Filesystem write | No direct | Yes |
| Shell | No / limited | Yes |
| Delete tool | No | Yes |
| Speed | Slower | Faster |
| Blast radius | Low | **High** |
| Operator skill | Must self-execute | Must review each step |

**Rule:** ASK for planning destructive recovery; AGENT only with scope lock + snapshots.

---

## 9. When AGENT mode is forbidden (recommended)

| Condition | Action |
|-----------|--------|
| Post-incident recovery | Human-only or ASK plan |
| No scope lock in prompt | Refuse writes |
| Protected zone delete requested | Refuse |
| “Delete and recreate” task framing | Refuse; propose clone-first |
| Operator fatigue / long session | New chat or stop |
| Multi-chat active on same clone | Pause AGENT |
| Git dirty + untracked critical assets | No git clean; snapshot first |
| Governance baseline freeze task | Lane B read-mostly |

---

## 10. Dangerous prompt patterns

| Prompt | Why dangerous |
|--------|----------------|
| “Clean up the repo” | Unbounded delete |
| “Remove unused files” | Heuristic data loss |
| “Reset everything” | git + FS combo |
| “Make it like new” | Recreate workspace |
| “Fix quickly, you decide” | Transfers authority to model |
| “Continue where we left off” without artifacts | Drift |
| “Same as last time” without paths | Wrong project version |
| “Delete old attempts” | Multi-version loss |

**Safe alternative:** scoped list + operation class + snapshot ID.

---

## 11. Why “delete and recreate” is dangerous

1. **Untracked assets** die with folder  
2. **Partial implementations** lost that were not in git  
3. **Handoff knowledge** in local notes gone  
4. **Second-order bugs** in regen exceed first-order bugs  
5. **Time pressure** skips bootstrap audit ([reconstruction-bootstrap-governance.md](../../../projects/mars-website-factory/reconstruction-bootstrap-governance.md))

**Preferred:** clone-first, parity-first ([website-factory-safe-production-rules-v1.md](../protocols/website-factory-safe-production-rules-v1.md)).

---

## 12. Why filesystem assumptions fail

| Assumption | Reality |
|------------|---------|
| “Repo root is project” | Monorepo; many roots |
| “dist can be deleted safely” | May be only deploy artifact |
| “git will restore” | Untracked ignored |
| “path in chat is cwd” | Shell state diverges |
| “generated is disposable” | Sometimes only copy |
| “Windows path case-insensitive” | Tooling may differ |

---

## 13. Control matrix (target state)

| Control | Now | Target |
|---------|-----|--------|
| Scope lock convention | Partial | Mandatory |
| Protected registry | v1 doc | Hook warn |
| Pre-agent snapshot | Manual | GitGuard G1 |
| Validator | None | GitGuard G2 |
| Lane discipline | Doc | Chat naming + REVIEW |
| Incident reports | v1 | Recurring |

---

## 14. References

- [incident-analysis-cursor-agent-context-drift-v1.md](incident-analysis-cursor-agent-context-drift-v1.md)  
- [destructive-operations-policy-v1.md](../contracts/destructive-operations-policy-v1.md)  
- [safe-execution-layer-v1.md](../protocols/safe-execution-layer-v1.md)  
- [parallel-cursor-chat-work-mode-v0.md](../../../governance/parallel-cursor-chat-work-mode-v0.md)

---

*End of Cursor Agent Operational Risk Analysis v1.*

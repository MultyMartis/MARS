# Website Factory — Safe Production Rules (v1)

**Status:** **documented** — hardening rules for Factory / Forge / workspace delivery.  
**Scope:** `projects/mars-website-factory/`, `agents/mars-forge/`, `workspaces/*` landing implementations.  
**Not:** changes to Triumph v4/v5 workspaces in this audit pass.

**Builds on:** [reconstruction-bootstrap-governance.md](../../../projects/mars-website-factory/reconstruction-bootstrap-governance.md), [workspace-reset-governance.md](../../../projects/mars-website-factory/workspace-reset-governance.md), [failure-recovery-governance.md](../../../projects/mars-website-factory/failure-recovery-governance.md), [context-survivability-governance.md](../../../projects/mars-website-factory/context-survivability-governance.md).

---

## 1. Core principle

Under stress, Factory work fails when **recovery speed** is prioritized over **source fidelity**. These rules prioritize **parity and provenance** over agent improvisation.

---

## 2. No rebuild-from-memory

| Rule | Detail |
|------|--------|
| **R-WF-01** | After context compression or new chat, **do not** reconstruct HTML/CSS/JS from model memory. |
| **R-WF-02** | Rebuild only from: repo `src/`, design exports, handoff docs, screenshots **with** authority mapping. |
| **R-WF-03** | If source missing → **SAFE UNKNOWN** + HITL — not approximate regen. |

**Why:** Memory rebuild introduces silent drift; combined with delete-recreate it destroys auditable lineage.

---

## 3. Clone-first discipline

| Rule | Detail |
|------|--------|
| **R-WF-04** | New attempt → **copy** workspace or branch snapshot — do not mutate canonical tree in place during experiment. |
| **R-WF-05** | Prefer `workspaces/<project>-vN` lineage over in-place wipe. |
| **R-WF-06** | Document clone source SHA in handoff / REPORT. |

---

## 4. Parity-first recovery

| Rule | Detail |
|------|--------|
| **R-WF-07** | Recovery goal = **match last known good** (visual + structural), not “improve” design. |
| **R-WF-08** | Use [visual-reconciliation-layer.md](../../../projects/mars-website-factory/visual-reconciliation-layer.md) when comparing states. |
| **R-WF-09** | List **parity gaps** before any fix commits. |

---

## 5. No reinterpretation recovery

Forbidden in emergency:

- “While we're at it, refactor partials”  
- “Modernize the gulp pipeline”  
- “Simplify folder structure”  
- Changing design tokens without authority  

Allowed: minimal diff to restore parity with evidence.

---

## 6. No architecture rewrite during emergency

| Phase | Permitted work |
|-------|----------------|
| **Emergency** | Restore files, fix broken refs, regen from existing gulp |
| **Stabilization** | Scoped QA, checklist findings |
| **Evolution** | Architecture change only with explicit charter + non-emergency task |

Aligns with [operational-modes-model.md](../../../projects/mars-website-factory/operational-modes-model.md) recovery mode.

---

## 7. Stable-state freeze checkpoints

Before major change:

1. Record **freeze checkpoint**: date, git ref, scope, known gaps  
2. Store in project handoff or `CHECKPOINT.md` in workspace  
3. Agent tasks reference checkpoint ID  

**Unfreeze** only with written reason — [temporal-evolution-governance.md](../../../projects/mars-website-factory/temporal-evolution-governance.md).

---

## 8. Visual parity validation

- Compare hero, header, footer, first screen — not only “build passes”.  
- Use reference screenshots from `projects/<client>/design/` when present.  
- Record `VISUAL PARITY FINDINGS` in REPORT — not binary “done”.

---

## 9. Source-of-truth protection

| Layer | SoT |
|-------|-----|
| Implementation | `workspaces/<project>/src/` (Lane A) |
| Governance / methodology | `projects/mars-website-factory/` (Lane B) |
| Design authority | Project design folder + human sign-off |
| Generated | `dist/` — **never** SoT |

Agent must not delete `src/` to fix `dist/` issues.

---

## 10. dist survivability strategy

| Rule | Detail |
|------|--------|
| **R-WF-10** | `dist/` is regenerable — regen via gulp, not hand-edit ([.cursorrules](../../../.cursorrules)). |
| **R-WF-11** | Do not treat dist as backup; snapshot `src/` + assets. |
| **R-WF-12** | Before regen that deletes dist, ensure `src` parity checkpoint exists. |
| **R-WF-13** | Hosting handoff may require dist bundle — export copy to `_snapshots/` if deploy-critical. |

---

## 11. Backup-before-generator

Before running generators (exporter, mass page gen, template fill):

- [ ] Canonical schema/template validated  
- [ ] Input instance reviewed  
- [ ] Output dir is disposable or versioned  
- [ ] Prior output archived if non-reproducible  

ORCA exporter lessons apply to Factory mass outputs.

---

## 12. No mass-generation before canonical validation

| Rule | Detail |
|------|--------|
| **R-WF-14** | One page / one section proof → then batch. |
| **R-WF-15** | Validation summary artifact before full tree generation. |
| **R-WF-16** | Rollback map entry before batch (GitGuard G1). |

---

## 13. Agent mode restrictions (Factory)

| Situation | Mode |
|-----------|------|
| Visual parity restore | AGENT with scope lock + no delete |
| Workspace reset / cleanup | **Human shell** or ASK-only plan |
| Governance checklist | Lane B, doc paths only |
| “Start fresh” landing | **Forbidden** without clone-first + human charter |

Cross-ref: [destructive-operations-policy-v1.md](../contracts/destructive-operations-policy-v1.md).

---

## 14. Triumph lesson (documented)

Triumph V3/V4 history in Factory docs shows: bootstrap chaos, residue inheritance, and cleanup impulse caused drift. These rules codify **audit-before-cleanup** and **clone-first**.

**This audit did not modify** `workspaces/triumph-manipulator-landing-v4/` per task constraints.

---

## 15. SAFE UNKNOWN

- Automated visual diff tooling in CI — **not evidenced** for all workspaces.  
- Per-project gulp regen time and failure modes — operator-verified per workspace.

---

*End of Website Factory Safe Production Rules v1.*

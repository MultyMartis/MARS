# Website Factory Enforcement (v1)

**Status:** **documented** — normative enforcement contract for Factory / Forge / landing delivery.  
**Not:** automated visual diff CI, generator gate product, or changes to Triumph v4/v5 workspaces.

**Builds on:** [website-factory-safe-production-rules-v1.md](../protocols/website-factory-safe-production-rules-v1.md)  
**Enforcement registry:** [enforcement-rules-registry-v1.md](../registries/enforcement-rules-registry-v1.md)  
**Halt protocol:** [operational-halt-protocol-v1.md](../protocols/operational-halt-protocol-v1.md)

---

## 1. Enforcement principle

Factory enforcement prioritizes **source fidelity and provenance** over recovery speed. AGENT **must halt** when any rule below would be violated or when a task trades parity for improvisation.

---

## 2. No reinterpretation recovery

| Rule | AGENT | Enforcement |
|------|-------|-------------|
| **E-WF-01** | Do not "improve" design during emergency restore | HALT on refactor/modernize language |
| **E-WF-02** | Do not change partials structure without charter | Scope lock must list structural paths |
| **E-WF-03** | Do not change tokens/fonts without design authority | SAFE UNKNOWN if authority missing |

**Safer alternative:** Minimal diff to match last known good with evidence.

---

## 3. No visual rebuild from memory

| Rule | AGENT | Enforcement |
|------|-------|-------------|
| **E-WF-04** | Rebuild only from `src/`, handoff, design exports | HALT on memory-only reconstruction |
| **E-WF-05** | Post-summary → re-read files; do not infer CSS/HTML | Mandatory new chat + file reads |
| **E-WF-06** | Missing source → SAFE UNKNOWN + HITL | No approximate regen |

Cross-ref: R-WF-01–03 in [website-factory-safe-production-rules-v1.md](../protocols/website-factory-safe-production-rules-v1.md).

---

## 4. No generator before canonical validation

| Rule | AGENT | Enforcement |
|------|-------|-------------|
| **E-WF-07** | One page/section proof before batch | HALT on mass-gen without pilot artifact |
| **E-WF-08** | Schema/template validated before exporter/generator | SAFE UNKNOWN if schema unverified |
| **E-WF-09** | Validation summary artifact required before full tree | Reference ORCA validation pattern |

---

## 5. No mass-page rollout before pilot parity

| Rule | AGENT | Enforcement |
|------|-------|-------------|
| **E-WF-10** | Pilot page must pass visual + build parity | No batch until pilot REPORT signed |
| **E-WF-11** | Rollback map entry before batch | Snapshot or git ref documented |
| **E-WF-12** | Mass replace across pages = HIGH RISK | Snapshot + glob lock |

---

## 6. Mandatory reference freeze

Before major redesign or structural change:

| Checkpoint | Required |
|------------|----------|
| Git ref recorded | Yes |
| Freeze note in handoff / `CHECKPOINT.md` | Yes |
| Known gaps listed | Yes |
| Unfreeze reason | Written — human |

---

## 7. Canonical screenshot set

| Rule | Detail |
|------|--------|
| **E-WF-13** | Reference screenshots live in `projects/<client>/design/` when present |
| **E-WF-14** | Screenshot set versioned with freeze checkpoint |
| **E-WF-15** | Agent REPORT includes `VISUAL PARITY FINDINGS` — not binary done |

**SAFE UNKNOWN:** Automated pixel diff in CI — not evidenced for all workspaces.

---

## 8. Stable-state archive before redesign

| Rule | AGENT |
|------|-------|
| **E-WF-16** | Snapshot `src/` + critical assets to `_snapshots/` before redesign |
| **E-WF-17** | Do not redesign in place without archive |
| **E-WF-18** | dist export to snapshot if deploy-critical |

---

## 9. Typography / CLS / schema — after stable baseline

| Phase | Permitted |
|-------|-----------|
| **Emergency** | Restore broken refs only |
| **Stable baseline** | Typography, CLS, schema fixes with parity evidence |
| **Evolution** | Charter required |

**Rule:** No SEO/schema/perf optimization during emergency recovery — stabilization first.

---

## 10. Clone-first recovery

| Rule | Enforcement |
|------|-------------|
| **E-WF-19** | New attempt → copy workspace/branch — no in-place wipe |
| **E-WF-20** | Document clone source SHA in handoff |
| **E-WF-21** | HALT on "delete-recreate" / "start fresh landing" without clone path |

---

## 11. Visual parity gates

Before sign-off on restore or section delivery:

| Gate | Check |
|------|-------|
| Hero | Match reference or documented gap |
| Header / footer | Structural parity |
| First screen | Visual reconciliation |
| Build | Gulp/npm passes in scoped path |
| Links | No broken internal refs in scope |

**Tool:** [visual-reconciliation-layer.md](../../../projects/mars-website-factory/visual-reconciliation-layer.md)

---

## 12. Agent mode matrix

| Task | Mode | Snapshot |
|------|------|----------|
| Visual parity restore | AGENT + scope lock | Required |
| Workspace reset/cleanup | Human / ASK | N/A — refuse AGENT |
| Mass page generation | AGENT after pilot | Required |
| Emergency reinterpretation | **Forbidden** | — |

---

## 13. Violation handling

1. HALT agent session  
2. Quarantine if contamination suspected  
3. Restore from snapshot/git — parity diff  
4. Log to `logs/incidents/`  
5. Mandatory new chat  

---

## 14. Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — G1 Website Factory enforcement contract |

---

*End of Website Factory Enforcement v1.*

# GitGuard System Entry (v1)

**Status:** **documented** — registry entry and positioning for the **GitGuard** survivability concept.  
**Not:** runtime product, `projects/gitguard/` pack, CLI, Cursor hook, or automated enforcement engine.

**Evolution contract:** [gitguard-survivability-evolution-v1.md](../contracts/gitguard-survivability-evolution-v1.md)  
**Reality index:** [mars-reality-index-v0.md](../../../governance/mars-reality-index-v0.md)  
**Entity model:** [system-entity-model.md](../../../governance/system-entity-model.md)

---

## 1. System intent

**GitGuard** (conceptual) = human-operated **survivability helper** for MARS:

- Pre-agent filesystem/git snapshots  
- Protected-folder awareness  
- Rollback maps  
- Emergency restore playbooks  
- Pre-destructive verification  

**Mission:** Reduce blast radius of Cursor AGENT + full-privilege shell **before** technical hooks exist.

---

## 2. Survivability role in MARS

| Role | Detail |
|------|--------|
| **Snapshot discipline** | Manifest convention under `workspaces/_snapshots/` |
| **Policy awareness** | Reads [protected-zones-registry-v1.md](protected-zones-registry-v1.md) + [enforcement-rules-registry-v1.md](enforcement-rules-registry-v1.md) |
| **Rollback memory** | Human-maintained rollback map (future JSON) |
| **Incident support** | Diff audit reports; no autonomous recovery |
| **Bridge to G2–G4** | Validator (G2), helpers (G3), observability (G4) — **done**; hooks G3+ **planned** |

GitGuard **does not** replace git hosting, governance SoT, or operator judgment.

---

## 3. Operational boundaries

| In scope (documentation / future helper) | Out of scope |
|------------------------------------------|--------------|
| Snapshot manifest metadata | Autonomous agent |
| Deny-list validation (future) | Governance truth authoring |
| Rollback map entries | Registry engine / sync |
| Pre-destructive checklist | OS-level sandbox |
| Filesystem diff audit reports | Force-push automation |
| Cursor hook wrapper (future) | Mass cleanup orchestration |

**Current enforcement:** [enforcement-rules-registry-v1.md](enforcement-rules-registry-v1.md) — **human-operated**.

---

## 4. Future phases (aligned with evolution contract)

| Phase | Deliverable | Status |
|-------|-------------|--------|
| **G0** | Contracts, protected registry, manual snapshots, infra folders | **Done** |
| **G1** | Enforcement registry, halt/drift protocols, checklists, prompt library | **Done** |
| **G2** | Scoped operation validator (CLI + rules registry) | **Done** — human-invoked only |
| **G3** | Pre-execution helpers + advisory layer + human authority | **Done** — advisory only |
| **G3+** | Cursor hook integration | **Planned** — verify Cursor hook support; charter required |
| **G4** | Observability + drift detection (read-only tooling) | **Done** |
| **G5+** | Optional scheduled snapshots, rollback-map CLI validator | **Planned** — disk/retention policy |

Registration path when pack is created: [mars-future-system-entry-discipline-v0.md](../../../governance/mars-future-system-entry-discipline-v0.md).

---

## 5. Non-goals

GitGuard is **not**:

- A governance certification or compliance product  
- An automated policy engine that blocks without human review path  
- A replacement for `git` or backup appliances  
- Proof that MARS has a running multi-agent runtime  
- A license to bypass quarantine or halt protocols  
- A tool that deletes or cleans up on behalf of the operator  

---

## 6. Enforcement philosophy

1. **Default deny** for destructive AGENT operations — document first, automate later.  
2. **Human confirmation** remains authoritative; helpers **warn** and **assist**, not override.  
3. **Snapshot before mutation** for MEDIUM+ risk — incomplete snapshot = do not proceed.  
4. **No fake product claims** — status honesty per [AGENTS.md](../../../AGENTS.md).  
5. **Pilot before repo-wide hooks** — one workspace sandbox first (G3).  
6. **SAFE UNKNOWN** when implementation choice unset — do not invent runtime.

---

## 7. Related artefacts (G1)

| Document | Link |
|----------|------|
| Enforcement registry | [enforcement-rules-registry-v1.md](enforcement-rules-registry-v1.md) |
| Operational halt | [operational-halt-protocol-v1.md](../protocols/operational-halt-protocol-v1.md) |
| Chat drift | [chat-context-drift-protocol-v1.md](../protocols/chat-context-drift-protocol-v1.md) |
| Safe prompts | [safe-prompt-pattern-library-v1.md](../guardrails/safe-prompt-pattern-library-v1.md) |
| Destructive policy | [destructive-operations-policy-v1.md](../contracts/destructive-operations-policy-v1.md) |

---

## 8. Changelog

| Date | Change |
|------|--------|
| 2026-05-24 | v1 — G1 GitGuard registry entry (documentation positioning) |

---

*End of GitGuard System Entry v1.*

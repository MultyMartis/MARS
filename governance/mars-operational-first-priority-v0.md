# MARS — Operational-first priority shift

**Status:** **documented** — post-freeze priority declaration.  
**Date:** 2026-05-19.  
**Context:** [mars-governance-baseline-freeze-v0.md](mars-governance-baseline-freeze-v0.md); governance in [mars-lightweight-maintenance-mode-v0.md](mars-lightweight-maintenance-mode-v0.md).

**Is:** explicit **gravity shift** from governance expansion to operational delivery.  
**Is not:** deprecation of governance, runtime build mandate, or proof that listed systems are fully automated.

---

## 1. Priority statement

After Cycles 1–8, MARS **primary value** is **operational use** of documented systems — not further governance architecture.

| Mode | Posture |
|------|---------|
| **Governance** | **Maintenance** — freeze baseline, light hygiene |
| **Operational systems** | **Primary** — real workflows, packs, delivery, external bridges |

**Goal:** prevent **governance gravity** — where documentation work displaces production lanes.

---

## 2. Primary operational systems (ranked intent)

| Priority | System | Role | Canonical entry |
|----------|--------|------|-----------------|
| **1** | **ORCA** | Live PPC / operational doc corpus | [../projects/orca/OPERATIONAL-INDEX.md](../projects/orca/OPERATIONAL-INDEX.md) — FAST PATH |
| **2** | **MARS Website Factory** | Site production methodology + handoff | [../projects/mars-website-factory/OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) — Core Run |
| **3** | **Triumph v5** (manipulator landing programme) | Reference / battle-test delivery lane | [../projects/triumph-manipulator-landing/README.md](../projects/triumph-manipulator-landing/README.md), V3 charter |
| **4** | **MetaBOT** | External multi-workflow SEO/automation | [external-system-boundaries.md](external-system-boundaries.md), [external-systems-relationship-map-v0.md](external-systems-relationship-map-v0.md) |
| **5** | **WPilot** | Future WordPress bridge (documented boundary) | Factory handoff references; external map |
| **6** | **Future operational systems** | New packs/bridges per entry discipline | [mars-future-system-entry-discipline-v0.md](mars-future-system-entry-discipline-v0.md) |

**Supporting lanes (not primary gravity sinks):**

- **MARS Forge** — overlay on Factory/Gulp foundation; use [agents/mars-forge/AGENT.md](../agents/mars-forge/AGENT.md), not README checklist enumeration as daily default.
- **mars-runtime R1** — bounded experiments only.
- **continuity / IdeaBox** — optional human capture; not SoT.

---

## 3. What “operational-first” means in practice

| Do | Don't |
|----|-------|
| Start session from lane OPERATIONAL-INDEX | Start from governance/README full scan |
| Ship Factory/ORCA/Triumph task outcomes + REPORT | Author new governance triads for routine work |
| Fix registry row when id appears in delivery | Build registry engine or sync fiction |
| Use Forge/Gulp foundation map for frontend | Re-derive Gulp↔Forge relationship per task |
| Record milestones in lifecycle when **status** changes | Run Cycle 8-scale validation per feature |
| Treat MetaBOT/WPilot as **external** with boundaries | Merge external runtime into MARS core claims |

---

## 4. Governance role under maintenance mode

Governance remains **authoritative** for:

- Honesty ([AGENTS.md](../AGENTS.md))
- Boundaries and registry precedence
- Anti-mythology and survivability patterns (frozen catalogue)
- Entry discipline for new systems

Governance is **not** the default **work product** unless the chartered task **is** governance maintenance.

**Tier 0 still wins** on every session — then jump to **operational Tier 2** for the active lane.

---

## 5. Triumph v5 boundary (anti-mythology)

Triumph is **production-oriented delivery** and **methodology stress-test** — **not**:

- proof that Website Factory runtime exists in-repo  
- proof of autonomous deployment  
- substitute for ORCA live procedures  

Battle-test charter modes apply **only** when chartered — [operational-modes-model.md](../projects/mars-website-factory/operational-modes-model.md).

---

## 6. Decision heuristic

```
IF task_charter names operational lane (ORCA / Factory / Triumph / external bridge)
  THEN Tier 0 → lane OPERATIONAL-INDEX → execute → REPORT
ELSE IF task_charter names governance maintenance
  THEN Tier 0 → one governance row → minimal diff → REPORT
ELSE IF unclear
  THEN SAFE UNKNOWN — ask human which lane
```

---

## 7. Anti-patterns (governance gravity)

| Anti-pattern | Corrective |
|--------------|--------------|
| “Improve MARS” → new governance files | Improve **operational** outcome; governance only if drift proven |
| Factory Extended as first read | Core Run only |
| Meta-governance checklist for every page | Factory operational modes (light/standard/battle) |
| Triumph charter as default QA | Standard mode unless battle chartered |
| Parallel topology/reality/ontology maps | One row each per [mars-future-system-entry-discipline-v0.md](mars-future-system-entry-discipline-v0.md) |

---

*Operational-first — governance frozen, delivery primary.*

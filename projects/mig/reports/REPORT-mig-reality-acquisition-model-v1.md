# REPORT — MIG Reality Acquisition Model v1

**Date:** 2026-06-04  
**Task:** MIG Enhancement Charter — Reality Acquisition Model (documentation-only)  
**Lane:** B — MIG design / contracts

---

## Summary

Designed and documented the **MIG Reality Acquisition Model** as normative contract **[MIG-REALITY-ACQUISITION-MODEL-v1.md](../contracts/MIG-REALITY-ACQUISITION-MODEL-v1.md)**. The model defines four **Reality Layers** (R1 Human → R2 Browser Groundtruth → R3 Structured Search → R4 Intelligence), trust ordering, evidence reference discipline, conflict resolution, and **Human Review Mode** with the `evidence/` output package and required `review.md` sections.

**No runtime code** was added or changed.

---

## Deliverables

| Artifact | Path |
|----------|------|
| Normative contract | [contracts/MIG-REALITY-ACQUISITION-MODEL-v1.md](../contracts/MIG-REALITY-ACQUISITION-MODEL-v1.md) |
| This report | [reports/REPORT-mig-reality-acquisition-model-v1.md](REPORT-mig-reality-acquisition-model-v1.md) |

---

## Design decisions

1. **Two “R” namespaces** — MARS **R1** (MIG program) vs MIG **Reality Layer R1–R4** documented explicitly to avoid confusion with ORCA (MARS R2).
2. **R2 as primary automated mode** — Playwright/browser evidence is canonical for visual truth when R1 is absent; aligns with Enhancement Charter “browser evidence remains canonical acquisition source.”
3. **R3 for scale** — Maps to existing Search Acquisition / API paths; lower fidelity must surface in SAFE UNKNOWN.
4. **R4 bounded** — Session intelligence only; must cite R1–R3; never replaces capture; ORCA remains downstream interpreter.
5. **`evidence/review.md`** — Separate from `research_pack.review.md` (pack-level edit); Human Review Mode is capture-grade sign-off.

---

## Changed files

| File | Action |
|------|--------|
| `projects/mig/contracts/MIG-REALITY-ACQUISITION-MODEL-v1.md` | Created |
| `projects/mig/reports/REPORT-mig-reality-acquisition-model-v1.md` | Created |
| `projects/mig/OPERATIONAL-INDEX.md` | Updated (index entry) |
| `projects/mig/README.md` | Updated (structure table) |
| `projects/mig/system-overview.md` | Updated (cross-reference) |

---

## Project map updates

- **OPERATIONAL-INDEX.md** — new row **10i** Reality Acquisition Model.
- **README.md** — contracts row lists new SoT.
- **system-overview.md** — link under acquisition discipline.

**Registry:** No change to `registry/project-registry.md` (no new project; in-pack contract only).

---

## Alignment with existing docs

| Existing doc | Alignment |
|--------------|-----------|
| REPORT-mig-data-acquisition-architecture-v1 | Channels map to R1–R3; report remains channel topology; RAM v1 is trust stack |
| Pilot SERP checklist | Classified as **R1-first** workflow |
| mig-deep-research-architecture-v1 | **R4** channel with citation rules |
| v0.1 spine | Unchanged; R2 Playwright **planned**, not claimed as shipped |

---

## Git status

Documentation-only edits; **no commit** per project default.

---

## UNKNOWN / risks

| Signal | Detail |
|--------|--------|
| **SAFE UNKNOWN** | Playwright deployment topology (VPS pool, captcha, n8n ownership) not specified in repo — future implementation choice. |
| **Partial R2 today** | v0.1 website capture uses HTTP/DOM, not full browser — contract grades this as partial R2 with disclosure obligation. |
| **SECURITY RISK** | None introduced (docs only). |

---

## Next steps (optional, not executed)

- Reference RAM v1 from [mig-operational-runtime-architecture-v1.md](../contracts/mig-operational-runtime-architecture-v1.md) session tree when R2 lands.
- Add `reality_layers_present` to session manifest schema when runtime work is chartered.
- Pilot #1: produce first `evidence/review.md` under `incoming/mig/pilots/...` per §7 template.

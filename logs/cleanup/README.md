# MARS Cleanup Program — Permanent Audit Trail

**Status:** **operational** (human-maintained)  
**Created:** 2026-06-03 (MARS Ecosystem Integrity Census v1, Lane B)  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`45518bb` / `mars-v2-stable-baseline-2026-06`)

---

## Purpose

This tree holds **durable evidence** for ecosystem inventory, classification review, and **proposed** cleanup actions. It exists so that:

- Nothing discovered during a census **disappears silently**
- No deletions, archival moves, or reclassifications happen **without** a matching record here (or an explicit operator REPORT citing these paths)
- Future cleanup passes can **append** and cross-link, not overwrite history

**This is not:** an automated cleanup engine, policy enforcer, or registry SoT. Authoritative project identity remains `registry/project-registry.md`.

---

## Directory layout

| Path | Role |
|------|------|
| `discoveries/` | Raw and distilled findings from inventory passes (entities, gaps, conflicts) |
| `actions/` | Proposed actions only (`KEEP`, `RECLASSIFY`, `REGISTER`, `ARCHIVE`, `MERGE`, `INVESTIGATE`) — **no execution log** until a future pass explicitly performs work |
| `reclassifications/` | Records when an entity’s class or registry band changes (proposed or completed) |
| `archive-candidates/` | Entities flagged for archival review — **not** archived by default |
| `fixes/` | Reserved for future corrective work evidence (empty until fixes are chartered) |

---

## Canonical investigations

| Investigation | File |
|---------------|------|
| Ecosystem Integrity Census v1 | [MARS-ECOSYSTEM-INTEGRITY-CENSUS-v1.md](MARS-ECOSYSTEM-INTEGRITY-CENSUS-v1.md) |
| Cleanup Wave 1 summary | [MARS-CLEANUP-WAVE-1-SUMMARY-v1.md](MARS-CLEANUP-WAVE-1-SUMMARY-v1.md) |
| Cleanup Wave 1A summary | [MARS-CLEANUP-WAVE-1A-SUMMARY-v1.md](MARS-CLEANUP-WAVE-1A-SUMMARY-v1.md) |
| Wave 1A action registry | [actions/cleanup-wave-1a-registry-v1.md](actions/cleanup-wave-1a-registry-v1.md) |
| Cleanup Wave 2 Discovery | [MARS-CLEANUP-WAVE-2-DISCOVERY-v1.md](MARS-CLEANUP-WAVE-2-DISCOVERY-v1.md) |
| Cleanup Wave 2A summary | [MARS-CLEANUP-WAVE-2A-SUMMARY-v1.md](MARS-CLEANUP-WAVE-2A-SUMMARY-v1.md) |
| Wave 2A action registry | [actions/cleanup-wave-2a-registry-v1.md](actions/cleanup-wave-2a-registry-v1.md) |
| Cleanup Wave 2B summary | [MARS-CLEANUP-WAVE-2B-SUMMARY-v1.md](MARS-CLEANUP-WAVE-2B-SUMMARY-v1.md) |
| Wave 2B action registry | [actions/cleanup-wave-2b-registry-v1.md](actions/cleanup-wave-2b-registry-v1.md) |
| Observed information flow | [discoveries/observed-information-flow-v1.md](discoveries/observed-information-flow-v1.md) |
| Lifecycle alignment (2B) | [actions/lifecycle-alignment-v1.md](actions/lifecycle-alignment-v1.md) — Key Event History vs Tracking Mode; normal work ≠ mandatory append |
| Post-Cleanup Audit v1 | [MARS-POST-CLEANUP-AUDIT-v1.md](MARS-POST-CLEANUP-AUDIT-v1.md) |
| **Cleanup Program closeout** | [MARS-CLEANUP-PROGRAM-CLOSEOUT-2026-06.md](MARS-CLEANUP-PROGRAM-CLOSEOUT-2026-06.md) — status **COMPLETE** |
| Closeout registry | [cleanup-program-registry-closeout-v1.md](cleanup-program-registry-closeout-v1.md) |
| KC drift report (recommendations only) | [knowledge-center-drift-report-v1.md](knowledge-center-drift-report-v1.md) |

---

## Discipline

1. **Append-first** — Prefer new dated files (`YYYY-MM-DD-<topic>-vN.md`) over rewriting prior discovery files.
2. **Link SoT** — Cite `project_id`, `agent_id`, or canonical paths; do not duplicate full registry rows.
3. **No silent ops** — If cleanup is executed later, add a row under `actions/` or `fixes/` stating what changed, when, and who approved.
4. **SAFE UNKNOWN** — State unknowns explicitly; do not infer runtime or registration from folder names alone.

---

## Related governance

- `governance/registry-source-of-truth.md`
- `governance/ecosystem-topology-index.md`
- `governance/mars-reality-index-v0.md`
- `logs/lifecycle-log.md` (lifecycle **events**, not cleanup execution)

---

*Cleanup program structure — Census v1, Lane B.*

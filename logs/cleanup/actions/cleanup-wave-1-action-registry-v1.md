# Cleanup Wave 1 Action Registry v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 1  
**Rule:** Recommendations only — **KEEP · RECLASSIFY · ARCHIVE CANDIDATE · INVESTIGATE**  
**No execution** in Wave 1  
**Upstream:** Census v1 + Wave 1 task reviews (ISBD, Lifecycle Log, HomeGateway, Triumph map)

---

## Action vocabulary (Wave 1)

| Action | Meaning in this pass |
|--------|----------------------|
| **KEEP** | Current classification or location is correct; maintain |
| **RECLASSIFY** | Change documented class, band, or cross-links — not filesystem moves |
| **ARCHIVE CANDIDATE** | Flag for future archival review — **no move in Wave 1** |
| **INVESTIGATE** | Needs operator decision or deeper pass before action |

---

## Wave 1 finding registry

| ID | Entity / finding | Action | Rationale | Resulting state (if executed later) |
|----|------------------|--------|-----------|-------------------------------------|
| W1-001 | `logs/lifecycle-log.md` | **KEEP** | Active governance event SoT; under-maintained not obsolete | Remains append-only SoT |
| W1-002 | Lifecycle log gaps evt 0017–0021 | **INVESTIGATE** | Registry ahead of log per sync review | Human-gated backfill in Wave 2 |
| W1-003 | Lifecycle vs cleanup trail distinction | **RECLASSIFY** | Prevent conflation with `logs/cleanup/` | Operator docs clarify three log roles |
| W1-004 | ISBD `workspaces/isbd-care-landing/` | **RECLASSIFY** | De facto Factory execution case; not Program | Documented as client delivery execution case |
| W1-005 | ISBD registry gap | **INVESTIGATE** | Largest unregistered delivery; operator chooses Factory case row vs `project_id` | Traceable registration |
| W1-006 | ISBD canvas SAFE UNKNOWN node | **RECLASSIFY** | Contradicts live workspace | Canvas node reflects registered case |
| W1-007 | ISBD nested `.git` | **INVESTIGATE** | Monorepo boundary / backup scope | Policy documented |
| W1-008 | HomeGateway registry `planned` vs OPERATIONAL prose | **RECLASSIFY** | Overloaded "OPERATIONAL" term | Single clear band: planned doc pack |
| W1-009 | HomeGateway program maturity | **KEEP** | `planned / draft` — do not promote to active product | Honest maturity |
| W1-010 | HomeGateway workspace MVP v1 | **RECLASSIFY** | UI prototype — not shippable MVP product | Label: static UI prototype workspace |
| W1-011 | HomeGateway OPERATIONAL-INDEX workspace row | **INVESTIGATE** | Partially stale vs MVP v1 existence | Index aligned with reports |
| W1-012 | Triumph canonical workspace v6 | **KEEP** | Multi-source confirmation | v6 remains edit surface |
| W1-013 | Triumph v1–v4 workspaces | **ARCHIVE CANDIDATE** | Superseded / abandoned generations | Future cold storage after operator sign-off |
| W1-014 | Triumph v5 workspace | **ARCHIVE CANDIDATE** | Historical; v6 copied from v5 stable | Keep until ORCA docs retarget |
| W1-015 | ORCA calibration index → v5 paths | **RECLASSIFY** | Drift vs v6 canonical | Paths point to v6 |
| W1-016 | `triumph-manipulator-landing` single `project_id` vs 6 workspaces | **INVESTIGATE** | Version authority map missing in registry | Relationship map doc |
| W1-017 | Factory Triumph reference case (doc simulation) | **KEEP** | Distinct from workspace delivery | No merge with v6 workspace |
| W1-018 | `registry/project-registry.md` (all rows) | **KEEP** | SoT — reconcile prose only where flagged | Stable registry |
| W1-019 | `continuity/` IdeaBox | **KEEP** | Correctly excluded from registry | Unchanged |
| W1-020 | `seo-content-agent` legacy row | **KEEP** | Explicit legacy band | No new docs |
| W1-021 | `metabot-seo-content-agent` | **KEEP** | Canonical external system docs | Unchanged |
| W1-022 | GitGuard concept | **INVESTIGATE** | Entity model vs survivability denial of product | Operator band decision |
| W1-023 | MARS Bridge stub `incoming/mars-bridge/` | **KEEP** + **INVESTIGATE** | Stub correct location; charter TBD | Intake discipline |
| W1-024 | `incoming/*` drops | **INVESTIGATE** | Promote vs quarantine SOP | Intake policy |
| W1-025 | `web-gpt-sources/chat-migration/` | **ARCHIVE CANDIDATE** | Superseded by v1 state docs | Historical band |
| W1-026 | `projects/mig/archive/pre-pilot-gruzotaxi-krasnodar-v1/` | **ARCHIVE CANDIDATE** | Pre-pilot complete | Historical |
| W1-027 | `projects/orca/archive/stable-orca-after-triumph-battle-v1/` | **ARCHIVE CANDIDATE** | Parallel stable snapshot | Pointer doc first |
| W1-028 | `workspaces/_sandbox`, `_tmp`, `_quarantine` | **KEEP** + **INVESTIGATE** | Ops hygiene dirs | Retention policy |
| W1-029 | WPilot future agent roles | **INVESTIGATE** | Documented but no agent cards | Register only if activated |
| W1-030 | Integration registry empty rows | **INVESTIGATE** | Schema without instances | Populate when bridged |
| W1-031 | Factory block registry duplication | **INVESTIGATE** | v0 doc vs reference-v1 tables | Align without silent merge |
| W1-032 | `mars-core` example registry row | **RECLASSIFY** | Placeholder noise | Mark example or remove in Wave 2 |
| W1-033 | `continuity/registry/master-index.md` empty | **INVESTIGATE** | Manual nav not populated | Populate or deprecate |
| W1-034 | Structural coherence audit WPilot claim | **KEEP** + **RECLASSIFY** | Errata pointer — audit stale vs registry | Cross-link fix |
| W1-035 | Census proposed actions A-001–A-030 | **KEEP** | Superseded by this Wave 1 registry for lane B execution planning | Wave 1 SoT for actions |

---

## Summary counts

| Action | Count |
|--------|------:|
| **KEEP** | 10 |
| **RECLASSIFY** | 9 |
| **ARCHIVE CANDIDATE** | 8 |
| **INVESTIGATE** | 14 |

*(Some rows combine KEEP + INVESTIGATE as dual recommendation.)*

---

## Wave 1 execution status

**Wave 1:** proposal-only (read-only reviews).  
**Wave 1A (2026-06-03):** partial execution — see [cleanup-wave-1a-registry-v1.md](cleanup-wave-1a-registry-v1.md) and [../MARS-CLEANUP-WAVE-1A-SUMMARY-v1.md](../MARS-CLEANUP-WAVE-1A-SUMMARY-v1.md). **No** archive/delete.

---

## Cross-links

| Review | File |
|--------|------|
| ISBD | [reclassifications/isbd-classification-review-v1.md](../reclassifications/isbd-classification-review-v1.md) |
| Lifecycle Log | [discoveries/lifecycle-log-review-v1.md](../discoveries/lifecycle-log-review-v1.md) |
| HomeGateway | [reclassifications/homegateway-classification-review-v1.md](../reclassifications/homegateway-classification-review-v1.md) |
| Triumph map | [discoveries/triumph-version-map-v1.md](../discoveries/triumph-version-map-v1.md) |
| Census actions (prior) | [2026-06-03-ecosystem-census-proposed-actions-v1.md](2026-06-03-ecosystem-census-proposed-actions-v1.md) |

---

*Cleanup Wave 1 action registry v1 — recommendations only.*

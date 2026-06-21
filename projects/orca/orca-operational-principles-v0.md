# ORCA Operational Principles v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — Intelligence & Intake System layer principles (2026-05-21).

Supplements [starter-pack/orca-operational-principles-v1.md](starter-pack/orca-operational-principles-v1.md) (live PPC review) without replacing it.

## Scope of This Document

Principles for:

- Universal intake
- Project normalization
- Evidence and research
- Campaign mode separation
- Artifacts and Factory semantic lock
- Project memory

Does **not** expand MARS governance. Does **not** change Triumph export/validation CLIs.

## Core Principles

### 1 — Evidence-first

Decisions cite captured evidence or **SAFE UNKNOWN**. Raw files, AI drafts, and old snapshots are not default truth.

### 2 — HITL (human-in-the-loop)

Inventory, classification, normalization, approval, export import, and Factory build authority remain human. AI assists; humans sign off.

### 3 — SAFE UNKNOWN

Gaps are valid. Forbidden: guessing competitor budgets, conversion rates, or policy outcomes to fill templates.

### 4 — No fake autonomy

Do not describe intake, research, or export scripts as "agents," "orchestration," or "autonomous PPC" unless a future charter explicitly builds human-invoked tools with honest naming.

### 5 — No runtime mythology

Documentation in this layer is **operational architecture**, not proof of deployed services, crawlers, or registry engines.

### 6 — Normalized intelligence

Chaotic inputs become structured project folders and graded observations before strategy and export work.

### 7 — Approved artifacts only

`draft` ≠ operational truth. Commander import and Factory MODE 1 require `approved` or `production-ready` artifacts.

### 8 — Raw inputs ≠ operational truth

`incoming/` and `raw-inventory/` are traceability sources. Manifest + review bridge to truth.

### 9 — Modular mode packs

Search, RSYA, retarget, brand, local, experimental are **separate** operational shapes. Shared intake does not merge ad logic.

### 10 — Transport layer isolation

XLSX Commander exports and sheet patches are dumb transport — not semantic SoT (validated in Triumph flow).

### 11 — Semantic continuity

ORCA approved briefs and handoffs lock meaning through Website Factory MODE 1. Layout freedom; offer/intent/CTA/claims locked.

## Practical Gate Questions

Before citing ORCA output in export or Factory:

1. Is there an inventory manifest with operator-confirmed categories?
2. Is evidence graded (not default `unverified`)?
3. Is the artifact status `approved` or `production-ready`?
4. Is the campaign mode correct (Search ≠ RSYA)?
5. Are UNKNOWNs listed instead of invented?
6. Does Factory session use MODE 1 when content lock required?

## Layer Map (v0 foundation)

| Folder | Role |
|--------|------|
| `intake/` | Raw pack → manifest → normalize → distribute |
| `projects/` | Canonical per-project tree contract |
| `evidence/` | Classification vocabulary (with v1 strength docs) |
| `research/` | Human-operated intelligence collection |
| `intelligence/` | Factory lock, project memory, models |
| `campaign-modes/` | Mode separation architecture |
| `artifacts/` | Deliverable types and lifecycle |
| `moderation/` | Moderation incident registry (human log) |
| `orca-operational-principles-v0.md` | This file |

## Relationship to Validated Operations (2026-05-21)

**Evidence in repo** (not mythology):

- Triumph Manipulator Search pack — validation CLI, Commander export, full-cycle runs
- Commander import transport — human checklist
- Website Factory landing production — handoff continuity
- Raw pack ingestion precedent — `incoming/orca-triumph-raw-pack/`

v0 generalizes patterns Triumph already proves **without** mandating migration.

## Anti-Patterns

- Governance wave from intake docs.
- AGI-style "ORCA understands the market" language.
- Skipping manifest for expedited export.
- RSYA keywords copied from Search pack without mode review.

## Related Documents

- [orca-universal-intake-architecture-v0.md](intake/orca-universal-intake-architecture-v0.md)
- [project-structure-contract-v0.md](projects/project-structure-contract-v0.md)
- [project-md-contract-v0.md](projects/project-md-contract-v0.md)
- [inventory-manifest-schema-v0.md](intake/inventory-manifest-schema-v0.md)
- [evidence-classification-system-v0.md](evidence/evidence-classification-system-v0.md)
- [orca-campaign-mode-architecture-v0.md](campaign-modes/orca-campaign-mode-architecture-v0.md)
- [orca-website-factory-semantic-lock-v0.md](intelligence/orca-website-factory-semantic-lock-v0.md)
- [orca-factory-bridge-index-v0.md](intelligence/orca-factory-bridge-index-v0.md)
- [landing-route-registry-contract-v0.md](intelligence/landing-route-registry-contract-v0.md)
- [ppc-landing-qa-contract-v0.md](intelligence/ppc-landing-qa-contract-v0.md)
- [orca-artifact-system-v0.md](artifacts/orca-artifact-system-v0.md)
- [approval-gates-contract-v0.md](artifacts/approval-gates-contract-v0.md)
- [orca-research-layer-v0.md](research/orca-research-layer-v0.md)
- [competitor-snapshot-contract-v0.md](research/competitor-snapshot-contract-v0.md)
- [research-session-snapshot-contract-v0.md](research/research-session-snapshot-contract-v0.md)
- [moderation-incident-registry-v0.md](moderation/moderation-incident-registry-v0.md)
- [project-memory-system-v0.md](intelligence/project-memory-system-v0.md)
- [TRIUMPH-RELATIONSHIP-TO-INTELLIGENCE-v0.md](ppc/triumph-manipulator/TRIUMPH-RELATIONSHIP-TO-INTELLIGENCE-v0.md)
- [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) — § ORCA Intelligence Foundation v0

## Boundary

These principles guide **human-operated** ORCA Intelligence & Intake work. They do not create automation products, orchestration engines, or autonomous advertising systems.

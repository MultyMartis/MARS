# Website Factory Cross-Layer Artefact Registry v1

**Status:** **documented** — audit registry from 2026-06-22 cross-layer review.  
**Not:** automated catalogue sync.

**Purpose:** Classify found rules, contracts, and gaps; guide FP-0002 V6 and future pilots.

---

## Found artefact registry

| ID | Path | Layer | Purpose | Current status | Authority | Reusable for FP-0002 V6 | Conflict | Action |
| -- | ---- | ----- | ------- | -------------- | --------- | ---------------------- | -------- | ------ |
| R-001 | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` | SOURCE | Visual SoT | CANONICAL | Project JPG policy | Yes (only visual) | None | KEEP |
| R-002 | `workspaces/fp-0002-shpigovsky-v6/audit/jpg-visual-audit/FP-0002-V6-JPG-VISUAL-AUDIT.md` | AUDIT | Raw observations | ACTIVE | JPG | Yes | None | KEEP |
| R-003 | `workspaces/fp-0002-shpigovsky-v6/audit/jpg-visual-audit/review/FP-0002-V6-JPG-AUDIT-GROUNDING-REVIEW.md` | AUDIT | Grounding verdict PARTIAL | ACTIVE | JPG + audit | Yes | None | KEEP |
| R-004 | `workspaces/fp-0002-shpigovsky-v6/audit/jpg-visual-audit/review/FP-0002-V6-JPG-GROUNDED-STRUCTURE.json` | AUDIT | 11 sections + groups | ACTIVE | Grounding review | Yes | None | KEEP |
| R-005 | `projects/mars-website-factory/frontend-production-authority-order-v1.md` | OPERATOR RULE | OL-01–OL-07 hierarchy | CANONICAL | Factory | Yes (methodology) | None | KEEP |
| R-006 | `projects/mars-website-factory/frontend-precision-governance-v1.md` | NORMALIZATION | Spacing scales §2, normalization §1 | CANONICAL | Factory | Yes | None | KEEP |
| R-007 | `projects/mars-website-factory/frontend-section-spacing-rule-v1.md` | FOUNDATION | Same-bg / diff-bg rhythm | ACTIVE | Factory | Yes (method) | §4 FP-0002 v3 px | ADAPT — ignore §4 for V6 |
| R-008 | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` | LEGACY | v3 project SSOT | LEGACY | FP-0002 v3 | **No** (visual px) | V6 clean-room | DO NOT USE |
| R-009 | `projects/mars-website-factory/frontend-visual-foundation-contract-v1.md` | FOUNDATION | Demo page composition | ACTIVE | Factory | Yes (post-foundation shell) | Assumes Production Standards first | LINK — after G-OPF |
| R-010 | `projects/mars-website-factory/frontend-shell-first-start-protocol-v1.md` | IMPLEMENTATION | Shell-first gates | ACTIVE | Factory | Yes | Skips JPG foundation chain if read alone | LINK — via pipeline v1 |
| R-011 | `projects/mars-website-factory/layout-spec-law-v1.md` | SPECIFICATION | Zone/row before HTML | CANONICAL | Factory | Yes | None | KEEP |
| R-012 | `projects/mars-website-factory/group-decomposition-law-v1.md` | SPECIFICATION | GROUP-IDs before layout spec | CANONICAL | Factory | Yes | None | KEEP |
| R-013 | `projects/mars-website-factory/design-source-to-frontend-mapping-governance-v1.md` | EXTRACTION | Multi-source mapping | ACTIVE | Factory | Yes (method) | FIG-oriented examples | ADAPT — JPG-only path |
| R-014 | `projects/mars-website-factory/cadence-tier-model.md` | FOUNDATION | XS–XL rhythm vocabulary | ACTIVE | Factory | Yes | No px truth | KEEP |
| R-015 | `projects/mars-website-factory/canonical-vertical-cadence-system.md` | FOUNDATION | Narrative cadence | REFERENCE | Factory | Yes | None | LINK |
| R-016 | `workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md` | IMPLEMENTATION | Container/grid law | ACTIVE | Factory | Yes | None | LINK at SCSS |
| R-017 | `workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md` | IMPLEMENTATION | Inner zones | ACTIVE | Factory | Yes | None | LINK at SCSS |
| R-018 | `projects/mars-website-factory/pixel-fidelity-audit-rules-v1.md` | QA | Fidelity audit | ACTIVE | Factory | Yes | None | LINK |
| R-019 | `projects/mars-website-factory/operator-visual-approval-law-v1.md` | QA | Operator approval | CANONICAL | Factory | Yes | None | KEEP |
| R-020 | `projects/mars-website-factory/practical-value-normalization-contract-v1.md` | NORMALIZATION | Normalization contract | CANONICAL | Factory | Yes | New 2026-06-22 | PROMOTE |
| R-021 | `projects/mars-website-factory/site-wide-style-foundation-contract-v1.md` | FOUNDATION | Foundation template | CANONICAL | Factory | Yes | New 2026-06-22 | PROMOTE |
| R-022 | `projects/mars-website-factory/block-implementation-specification-contract-v1.md` | SPECIFICATION | Block spec template | CANONICAL | Factory | Yes | New 2026-06-22 | PROMOTE |
| R-023 | `projects/mars-website-factory/frontend-implementation-pipeline-v1.md` | UNKNOWN | Full gate chain | CANONICAL | Factory | Yes | New 2026-06-22 | PROMOTE |
| R-024 | `projects/mars-website-factory/workflow-map.md` | UNKNOWN | Legacy target flow | STALE | Factory | Partial | Omits foundation chain | SUPERSEDE — link pipeline v1 |
| R-025 | `projects/mars-website-factory/foundation-systems/README.md` | IMPLEMENTATION | Wave 2 SCSS tokens | REFERENCE | Factory | After foundation approved | Generic demo tokens | LINK — not V6 px source |
| R-026 | `projects/mars-website-factory/css-variable-first-law-v1.md` | PRODUCTION LAW | Token lookup before SCSS | **MANDATORY** | Factory | Yes | New 2026-06-22 | PROMOTE |
| R-027 | `projects/mars-website-factory/site-wide-style-foundation-contract-v1.md` §4 | PRODUCTION LAW | Single Base Container Law | **MANDATORY** | Factory | Yes | 2026-06-22 | STRENGTHEN |
| R-028 | `projects/mars-website-factory/site-wide-style-foundation-contract-v1.md` §6 | PRODUCTION LAW | Section Owns Its Rhythm Law | **MANDATORY** | Factory | Yes | 2026-06-22 | STRENGTHEN |
| R-029 | `workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md` WF-GRID-006 | IMPLEMENTATION | Single base container | **MANDATORY** | Factory | Yes | 2026-06-22 | STRENGTHEN |

---

## Evidence excerpts (key rules)

**OL-01 spacing (R-005):** Gap scale `5·10·20·30·40·50·70`; margin/padding `5·10·15·20·25·30·40·50·70·90`; map to **nearest** — arbitrary forbidden.

**Normalization (R-006 §1):** Design ≈64px → **70px**; ≈48px → **50px**; round toward scale.

**Section rhythm (R-007 §2.1):** Same-bg → single boundary padding; forbidden double-gap.

**Section rhythm ownership (R-028):** Major region spacing on layout shell — not first/last internal child.

**Single base container (R-027 / R-029):** One primary `.container` — no per-block duplicate geometry.

**Shell-first gap (R-010 §1):** Historically allowed Home-first; closed by foundation chain + layout spec.

**Grounding PARTIAL (R-003):** Header/Hero Y split SAFE UNKNOWN; `header_implementation_authorized: false`.

**Legacy conflict (R-008 vs V6):** v3 standards contain project px — **forbidden** as V6 visual authority per clean-room reports.

---

## Cross-layer connection matrix

| From layer | Required output | To layer | Required input | Contract exists | Enforced by workflow | Gap |
| ---------- | --------------- | -------- | -------------- | --------------- | -------------------- | --- |
| SOURCE | manifest + hash | AUDIT | source file | Partial (v6 purity gate) | v6 guard docs | Low |
| AUDIT | raw observations | GROUNDING | audit artefacts | Yes (grounding review) | Manual | Low |
| GROUNDING | grounded sections JSON | EXTRACTION | grounded map | **Was missing** | **Now** pipeline v1 | **Closed** |
| EXTRACTION | observed families | NORMALIZATION | extraction doc | **Was missing** | **Now** normalization contract | **Closed** |
| NORMALIZATION | traceability table | STYLE FOUNDATION | normalization + OL-01 | **Was missing** | **Now** foundation contract | **Closed** |
| STYLE FOUNDATION | approved tokens | BLOCK SPEC | foundation MD/JSON | **Was missing** | **Now** block spec contract | **Closed** |
| BLOCK SPEC | bindings | HTML | approved spec | layout-spec + block spec | pipeline v1 | Medium — layout spec per block still required |
| HTML | structure | SCSS | HTML review + foundation | pre-scss checklist | pipeline v1 | Low |
| SCSS | styles | VISUAL QA | build | QA entry + pixel rules + **CSS Variable First Law** | Existing | Low |
| VISUAL QA | verdict | CORRECTION | QA report | failure attribution model | Existing | Low |

**Primary historical gap:** JPG AUDIT → SITE-WIDE STYLE FOUNDATION (skipped extraction + normalization). **Repaired** by pipeline v1 + contracts (2026-06-22).

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-22 | v1 — Cross-layer audit registry |
| 2026-06-22 | v1.1 — R-026 CSS Variable First Law; SCSS→VQA matrix link |

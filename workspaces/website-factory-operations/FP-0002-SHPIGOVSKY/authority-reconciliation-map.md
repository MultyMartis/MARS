# FP-0002 V8 Phase 07B — Authority Reconciliation Map

**Date:** 2026-07-01  
**Phase:** 07B documentation and reconciliation  
**Baseline commit:** `eb47ebb4066252373e02d9e1095403d0ce6b6b22`  
**Baseline tag:** `fp-0002-v8-operator-approved-frontend-stable-01`

---

## Classification key

| Class | Meaning |
|-------|---------|
| **CURRENT_AUTHORITY** | Use for operational decisions in this phase |
| **SUPPORTING_EVIDENCE** | Valid evidence; subordinate to current authority |
| **HISTORICAL_CONTEXT** | Preserved; do not treat as current implementation truth |
| **SUPERSEDED** | Replaced by V8 baseline or later record |
| **UNKNOWN** | Insufficient evidence — triggers stop if required for write |

---

## FP-0002 project authority

| Source | Path | Class | Notes |
|--------|------|-------|-------|
| Operator-approved frontend baseline | [FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01.md](FP-0002-V8-OPERATOR-APPROVED-FRONTEND-BASELINE-01.md) | **CURRENT_AUTHORITY** | 10 pages; operator freeze |
| WordPress-ready facts | [FP-0002-V8-WORDPRESS-READY-BASELINE-v1.md](FP-0002-V8-WORDPRESS-READY-BASELINE-v1.md) | **CURRENT_AUTHORITY** | Concise CMS facts; expanded in handoff map |
| Project status | [PROJECT-STATUS.md](PROJECT-STATUS.md) | **CURRENT_AUTHORITY** | Update in 07B for phase pointer |
| Priority visual protocol | [FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md](FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md) | **CURRENT_AUTHORITY** | Active until operator retires |
| Page inventory (design) | [FP-0002-PAGE-INVENTORY-v1.md](FP-0002-PAGE-INVENTORY-v1.md) | **SUPPORTING_EVIDENCE** | PDF/design scope; not V8 route truth |
| Block inventory | [FP-0002-BLOCK-INVENTORY-v1.md](FP-0002-BLOCK-INVENTORY-v1.md) | **HISTORICAL_CONTEXT** | Pre-V8 consolidation naming |
| Production standards v3 | [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) | **SUPPORTING_EVIDENCE** | Excel intake §10–11 |
| Excel structure authority | `INCOMING/02_CONTENT/Предварит структура и спрос.xlsx` | **CURRENT_AUTHORITY** | Client site structure for 07C |
| O-Centre audit status | [FP-0002-OCENTRE-VISUAL-AUDIT-STATUS-v1.md](FP-0002-OCENTRE-VISUAL-AUDIT-STATUS-v1.md) | **HISTORICAL_CONTEXT** | Superseded by operator baseline closure |

---

## V8 workspace authority

| Source | Path | Class | Notes |
|--------|------|-------|-------|
| V8 README | `workspaces/fp-0002-shpigovsky-v8/README.md` | **CURRENT_AUTHORITY** | Workspace entry |
| V8 operational status | `workspaces/fp-0002-shpigovsky-v8/foundation/FP-0002-V8-OPERATIONAL-STATUS.md` | **CURRENT_AUTHORITY** | Some pre-07A rows stale; reconcile in 07B |
| V8 source tree | `workspaces/fp-0002-shpigovsky-v8/src/` | **CURRENT_AUTHORITY** | Implementation SoT |
| V8 build | `gulpfile.js`, `package.json` | **CURRENT_AUTHORITY** | Gulp clean build |
| V7 workspace | `workspaces/fp-0002-shpigovsky-v7/` | **HISTORICAL_CONTEXT** | Immutable fallback; static demo reference |
| V6 workspace | `workspaces/fp-0002-shpigovsky-v6/` | **SUPERSEDED** | Frozen fallback only |

---

## Website Factory authority

| Source | Path | Class | Notes |
|--------|------|-------|-------|
| WF operational index | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | **CURRENT_AUTHORITY** | Session router |
| Execution cases registry | `projects/mars-website-factory/execution-cases-registry-v1.md` | **CURRENT_AUTHORITY** | FP-0002 lane pointer |
| Implementation extraction discipline | `projects/mars-website-factory/implementation-extraction-discipline-v1.md` | **CURRENT_AUTHORITY** | Lessons promotion pattern |
| Universal button system law | `projects/mars-website-factory/universal-button-system-law-v1.md` | **CURRENT_AUTHORITY** | Aligns with V8 `.btn` model |
| Operator canonical source law | `projects/mars-website-factory/operator-canonical-source-law-v1.md` | **CURRENT_AUTHORITY** | Manual edits canonical |
| Universal style scale law | `projects/mars-website-factory/universal-style-scale-law-v1.md` | **SUPPORTING_EVIDENCE** | V6 pilot; V8 uses `--radius-main` exception |
| WF reference v1 | `workspaces/website-factory-reference-v1/` | **SUPPORTING_EVIDENCE** | Generic patterns; not FP-0002 visuals |
| Lessons learned (new) | `projects/mars-website-factory/operational-examples/WEBSITE-FACTORY-FP-0002-LESSONS-LEARNED-v1.md` | **CURRENT_AUTHORITY** | Created Phase 07B |

---

## Forge WordPress authority

| Source | Path | Class | Notes |
|--------|------|-------|-------|
| Forge WP operational index | `projects/mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md` | **CURRENT_AUTHORITY** | FW-06B intake waiting |
| Handoff contract | `projects/mars-website-factory/subsystems/forge-wordpress/contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md` | **CURRENT_AUTHORITY** | Generic contract |
| FP-0002 WP foundation | `projects/mars-website-factory/subsystems/forge-wordpress/projects/fp-0002/` | **SUPPORTING_EVIDENCE** | Local foundation only; no frontend integration |
| FP-0002 handoff map (new) | [FP-0002-V8-FORGE-WORDPRESS-HANDOFF-MAP-v1.md](FP-0002-V8-FORGE-WORDPRESS-HANDOFF-MAP-v1.md) | **CURRENT_AUTHORITY** | Project-specific expansion |

---

## Storage evidence

| Source | Path | Class | Notes |
|--------|------|-------|-------|
| 07B snapshot | `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\phase-07b-documentation-reconciliation\` | **SUPPORTING_EVIDENCE** | Not Git authority |
| 07A recovery pack | `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v8\FP-0002-V8-OPERATOR-APPROVED-FRONTEND-STABLE-01\` | **SUPPORTING_EVIDENCE** | Baseline build evidence |

---

## Reconciliation rules applied

1. **V8 approved source** overrides V6/V7 documentation claims about current pages.
2. **Baseline record** overrides stale operational status rows (e.g. O-Centre REJECTED vs baseline STABLE).
3. **Excel** is structure authority for client demo; **V8 dist** is frontend reality authority.
4. **Figma** (`Spig_v1.2.fig`) is design reference; does not override operator-approved implementation.
5. Historical paths (`C:\`, `D:\`, `E:\` MARS roots) — **HISTORICAL_CONTEXT** only.

---

*Phase 07B authority map — documentation reconciliation.*

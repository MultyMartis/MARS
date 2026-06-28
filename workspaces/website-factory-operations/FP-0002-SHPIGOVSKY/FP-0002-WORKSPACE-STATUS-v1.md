# FP-0002 — Workspace Status v1

**Document type:** Workspace lifecycle status — production cycle v2  
**Date:** 2026-06-14  
**Factory Project:** FP-0002 — Shpigovsky.ru

---

## Project

**FP-0002** — Shpigovsky.ru

---

## Current Phase

**C — Desktop Shell**

---

## Status

**READY TO START**

---

## Active Workspace

| Field | Value |
|-------|-------|
| Path | `workspaces/fp-0002-shpigovsky-frontend/` |
| Full path | `C:\AI MARS\workspaces\fp-0002-shpigovsky-frontend\` |
| Lifecycle | **ACTIVE** · **CANONICAL** · **PRODUCTION** |
| Starter base | `workspaces/triumph-manipulator-landing/` (canonical gulp-starter) |
| Created | 2026-06-14 (cycle v2 reset) |

---

## Archive Workspace

| Field | Value |
|-------|-------|
| Path | `C:\AI MARS STORAGE\website-factory\archive\fp-0002-shpigovsky-frontend-pre-v2\` |
| Lifecycle | **ARCHIVED** · **READ ONLY** · **REFERENCE ONLY** |
| Former phase | M2 Foundation Extraction (pre-v2 residue) |
| Marker | `ARCHIVED.md` in archive root |

---

## Design sources (canonical — not in workspace)

| Source | Path |
|--------|------|
| Design PDFs | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/` |
| Content / IA XLSX | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/02_CONTENT/Предварит структура и спрос.xlsx` |

Workspace **does not** duplicate intake; references operations pack only.

---

## Authority chain

| Layer | Document |
|-------|----------|
| A0 Source Discovery | [REPORTS/FP-0002-SOURCE-DISCOVERY-REPORT-v1.md](REPORTS/FP-0002-SOURCE-DISCOVERY-REPORT-v1.md) |
| A1 Design Audit | [REPORTS/FP-0002-DESIGN-AUDIT-v1.md](REPORTS/FP-0002-DESIGN-AUDIT-v1.md) |
| Design Approval Sheet | [REPORTS/FP-0002-DESIGN-APPROVAL-SHEET-v1.md](REPORTS/FP-0002-DESIGN-APPROVAL-SHEET-v1.md) |
| Operator Visual Approval Law | [operator-visual-approval-law-v1.md](../../../projects/mars-website-factory/operator-visual-approval-law-v1.md) |
| Production Roadmap v2 | [website-factory-production-roadmap-v2-draft.md](../../../projects/mars-website-factory/website-factory-production-roadmap-v2-draft.md) |
| Production Standards SSOT | [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) |
| Workspace Archive Rule | [workspace-reset-governance.md](../../../projects/mars-website-factory/workspace-reset-governance.md) §9 |

---

## Operator decisions (shell start)

| Decision | Value | Basis |
|----------|-------|-------|
| **D-021** | **Variant A** — Production Standards v3 authority for Desktop Shell | Recommended in Design Approval Sheet; consistent with **APPROVED** Production Standards v3 (Lead sign-off 2026-06-13) |

Shell builds per **Production Standards v3**, not PDF pixel tokens where conflicts remain open (D-007…D-011 deferred to UI Demo phase).

---

## Explicit exclusions (this cycle start)

| Item | Started |
|------|---------|
| FP-0002 Desktop Shell (header/footer per PDF + v3) | **NO** |
| FP-0002 UI Demo | **NO** |
| Home / PG-001 | **NO** |
| `src/assets/design/` intake copy | **NO** (sources stay in INCOMING) |

Starter template demo pages may exist from gulp-starter copy — **not** FP-0002 production deliverables.

---

## Next action

**Phase C — Desktop Shell** per [website-factory-production-roadmap-v2-draft.md](../../../projects/mars-website-factory/website-factory-production-roadmap-v2-draft.md) and [FP-0002-FRONTEND-START-SEQUENCE-v1.md](FP-0002-FRONTEND-START-SEQUENCE-v1.md).

---

## V7 / V8 transition (2026-06-28)

| Layer | Status |
|-------|--------|
| V7 workspace | `IMMUTABLE_STABLE_FALLBACK` — source frozen |
| V7 static demo | `fp-0002-v7-static-client-demo-stable-02` — deployed demo unchanged |
| V8 workspace | Bootstrap reconciliation complete; Git whitelist enabled |
| V8 baseline | Four-template authority `6eb493e9` |
| Browser parity | PASS (V7 reference dist vs V8 dist) |
| Component audit | COMPLETE |
| CF-003 Upper Navigation | COMPLETE (2026-06-28) |
| CF-004 Founder Quote | COMPLETE (2026-06-28) |
| CF-005 Specialists | COMPLETE (2026-06-28) |
| CF-006 Comfort gallery | COMPLETE (2026-06-28) |
| CF-007 Reviews | COMPLETE (2026-06-28) |
| Shared component audit | COMPLETE — next wave CF-008 FAQ (NOT AUTHORIZED) |
| About (`o-centre`) | DEFERRED in V8 |

---

## Changelog

| Version | Date | Notes |
|---------|------|-------|
| v1 | 2026-06-14 | Cycle v2 workspace reset; archive pre-v2; active workspace from gulp-starter |

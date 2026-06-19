# REPORT — WEBSITE FACTORY IMPLEMENTATION PASS 01

**Date:** 2026-06-17  
**Scope:** Production Modes Contract integration — **documentation only**.  
**Task:** WF-A01 — Production Modes Contract (Pass 01)  
**Honesty boundary:** No runtime, no automation, no new systems, no governance expansion, no WF-A02/A03 work.

---

## Executive Summary

Pass 01 внедрил **Production Modes Contract** в документационный слой Website Factory. Создан канонический SoT — `website-factory-production-modes-charter-v1.md`. Добавлены blocking intake gate, LOC-ZONE passport fields (`production_mode`, `mode_history[]`), QA router, трёхуровневая модель **BUILT / VERIFIED / PRODUCTION PASS**, anti-generative-fill policy для `PIXEL_PERFECT`, и deferred marker **WF-A03** в roadmap.

**Вердикт:** WF-A01 **complete (documentation)**. WF-A02 **not started**. WF-A03 **DEFERRED**.

---

## Production Modes Charter

**Created:** [projects/mars-website-factory/website-factory-production-modes-charter-v1.md](../projects/mars-website-factory/website-factory-production-modes-charter-v1.md)

Содержит:

| Section | Content |
|---------|---------|
| §2 | Canonical tokens `PIXEL_PERFECT`, `TEMPLATE_ART` |
| §3–4 | Per-mode definitions, SSOT, inputs, creativity, QA, acceptance, SAFE UNKNOWN |
| §5 | Mode Selection Rules — blocking gate |
| §6 | Mode Transition Rules + `mode_history[]` shape |
| §7 | Anti-Generative-Fill Policy (PIXEL_PERFECT) |
| §8 | QA Router documentation contract |
| §9 | Artifact lifecycle BUILT / VERIFIED / PRODUCTION PASS |
| §10–12 | Cross-surfaces, non-goals, roadmap linkage |

**Orthogonality:** Production mode × Forge mode × Operational modes — explicitly documented.

---

## Intake Gate Integration

Production Mode **MUST be declared** — undeclared → **SAFE UNKNOWN** → **STOP**.

| Surface | Change |
|---------|--------|
| [onboarding-flow-v1.md](../projects/mars-website-factory/onboarding-flow-v1.md) | Path B **step 0** — mode before charter |
| [website-factory-workflow-v0.md](../projects/mars-website-factory/website-factory-workflow-v0.md) | `WF_V0_S01_INTAKE` output + QA gate + STOP on undeclared |
| [website-factory-source-discovery-v1.md](../projects/mars-website-factory/website-factory-source-discovery-v1.md) | A0.5 mode branch; A0.6 REPORT; gate blocks undeclared |
| [initialization-governance.md](../projects/mars-website-factory/initialization-governance.md) | Production mode in Required Initialization State |
| [project-bootstrap-template-v0.md](../projects/mars-website-factory/project-bootstrap-template-v0.md) | Mandatory intake row |
| [first-operational-runbook-v0.md](../projects/mars-website-factory/first-operational-runbook-v0.md) | R01 ↔ S01 mode declare |
| [foundation-adoption-charter-v1.md](../projects/mars-website-factory/foundation-adoption-charter-v1.md) | Step 0 in new workspace workflow |
| [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) | Core Run row + wave banner |

---

## LOC-ZONE Integration

**Created:** [workspaces/website-factory-operations/FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md](../workspaces/website-factory-operations/FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md)

| Field | Contract |
|-------|----------|
| `production_mode` | `PIXEL_PERFECT` \| `TEMPLATE_ART` |
| `mode_declared_at` | ISO-8601 |
| `mode_declared_by` | operator ID |
| `mode_rationale` | evidence pointer |
| `mode_waivers` | optional |
| `mode_history[]` | append-only transition log |

**Updated passports / manifests:**

| Artifact | Mode |
|----------|------|
| [FP-0002-PROJECT-PASSPORT.md](../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PROJECT-PASSPORT.md) | `PIXEL_PERFECT` (retroactive 2026-06-17) |
| [MOC-01 FP-0001](../workspaces/website-factory-operations/projects/FP-0001-triumph-manipulator-landing/manifest/MOC-01-entry-anchor.md) | Current mode display: `TEMPLATE_ART` |
| [MOC-03 FP-0001](../workspaces/website-factory-operations/projects/FP-0001-triumph-manipulator-landing/manifest/MOC-03-scope.md) | `factory.production_mode` line |
| [LOC-ZONE README](../workspaces/website-factory-operations/README.md) | Passport fields pointer |

---

## PASS Taxonomy Reform

**Updated:** [frontend-qa-reporting-standard-v1.md](../projects/mars-website-factory/frontend-qa-reporting-standard-v1.md) §1.1 — **Layer F**

| Term | Definition |
|------|------------|
| **BUILT** | Artifact created (`npm run build` PASS) |
| **VERIFIED** | Checked per production mode rules |
| **PRODUCTION PASS** | Meets mode requirements — maps to FINAL VERDICT §6 |

**Conflict resolution:** Layer F is **orthogonal** to Layer A gate verdicts. Existing **FINAL VERDICT — PRODUCTION PASS** retained; now requires **VERIFIED** precedent. Migration table adds FP-0002 false-green mappings.

**Basis:** FP-0002 FAIL-001, FAIL-018; architecture alignment §7.2.

---

## Anti-Generative-Fill Policy

| Location | Content |
|----------|---------|
| Charter §7 | Canonical policy — forbidden actions, FP-0002 failure refs |
| [pixel-fidelity-audit-rules-v1.md](../projects/mars-website-factory/pixel-fidelity-audit-rules-v1.md) §0.4 | PF audit cross-ref |
| [design-source-to-frontend-mapping-governance-v1.md](../projects/mars-website-factory/design-source-to-frontend-mapping-governance-v1.md) | §7.2 copy-absent row + production mode header |

**Rule:** In `PIXEL_PERFECT` — missing data → **SAFE UNKNOWN** or **STOP** — never generate, infer, or substitute.

---

## QA Router

**Updated:** [operational-qa-entry-v1.md](../projects/mars-website-factory/operational-qa-entry-v1.md)

| Branch | When | Primary gates |
|--------|------|---------------|
| **PIXEL_PERFECT QA** | passport mode | PF-*, Mapping QA, render/text diff, Operator Visual |
| **TEMPLATE_ART QA** | passport mode | Blueprint, content, semantic matrix, block provenance; PF-* N/A |
| **STOP** | undeclared mode | — |

**Not implemented:** runtime router, automated checklist engine.

---

## Roadmap Updates

**Updated:** [roadmap.md](../projects/mars-website-factory/roadmap.md)

| ID | Status |
|----|--------|
| **WF-A01** | **Complete (Pass 01)** |
| **WF-A02** | **Planned** — Validation Architecture |
| **WF-A03** | **DEFERRED** — Pixel Factory Expansion |

**Also:** [website-factory-production-roadmap-v2-draft.md](../projects/mars-website-factory/website-factory-production-roadmap-v2-draft.md) — charter pointer in Related table.

---

## WF-A03 Deferred Marker

| Field | Value |
|-------|-------|
| **ID** | WF-A03 — Pixel Factory Expansion |
| **Status** | **DEFERRED** |
| **Basis** | AI Website Factory Research; Architecture Alignment; Production Modes Architecture; FP-0002 |
| **Start condition** | WF-A01 **and** WF-A02 complete |
| **Auto-start** | **Forbidden** |
| **Operator reminder** | After WF-A02: *«Перед началом Pixel Factory Expansion рекомендуется запустить отдельный Web-GPT Research Pass.»* |

**Explicit non-goals until WF-A03:** Vision Layer · Visual Diff Layer · Pixel QA Runtime · Screenshot Engine · Agent Runtime.

---

## Risks

| Risk | Mitigation (Pass 01) |
|------|----------------------|
| Operators skip step 0 | Blocking language in charter + workflow S01 + onboarding |
| False-green persists | Layer F BUILT ≠ VERIFIED in reporting standard |
| Mode / Forge conflation | Orthogonality table in charter |
| Retroactive mode wrong on FP-* | Evidence-cited retroactive rows; operator may amend |
| Doctrine vs operations drift | Passport SoT + MOC display-only rule |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Full AI Website Factory Research text in repo | **SAFE UNKNOWN** — external summary only |
| Automated render diff tooling | **SAFE UNKNOWN** — project-local optional |
| WF-A02 Validation Architecture scope | **Not defined in Pass 01** |
| Hybrid `page_mode_map` pilots | **Design only** — no pilot executed |
| Runtime mode enforcement | **Not claimed** — documentation contract only |
| OCPilot SITE-001 ↔ production mode crosswalk | **SAFE UNKNOWN** |

---

## Changed Files

| File | Change type |
|------|-------------|
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Modified |
| `projects/mars-website-factory/onboarding-flow-v1.md` | Modified |
| `projects/mars-website-factory/website-factory-workflow-v0.md` | Modified |
| `projects/mars-website-factory/website-factory-source-discovery-v1.md` | Modified |
| `projects/mars-website-factory/operational-qa-entry-v1.md` | Modified |
| `projects/mars-website-factory/frontend-qa-reporting-standard-v1.md` | Modified |
| `projects/mars-website-factory/initialization-governance.md` | Modified |
| `projects/mars-website-factory/project-bootstrap-template-v0.md` | Modified |
| `projects/mars-website-factory/pixel-fidelity-audit-rules-v1.md` | Modified |
| `projects/mars-website-factory/foundation-adoption-charter-v1.md` | Modified |
| `projects/mars-website-factory/design-source-to-frontend-mapping-governance-v1.md` | Modified |
| `projects/mars-website-factory/first-operational-runbook-v0.md` | Modified |
| `projects/mars-website-factory/roadmap.md` | Modified |
| `projects/mars-website-factory/website-factory-production-roadmap-v2-draft.md` | Modified |
| `workspaces/website-factory-operations/README.md` | Modified |
| `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PROJECT-PASSPORT.md` | Modified |
| `workspaces/website-factory-operations/projects/FP-0001-triumph-manipulator-landing/manifest/MOC-01-entry-anchor.md` | Modified |
| `workspaces/website-factory-operations/projects/FP-0001-triumph-manipulator-landing/manifest/MOC-03-scope.md` | Modified |

---

## New Files

| File |
|------|
| `projects/mars-website-factory/website-factory-production-modes-charter-v1.md` |
| `workspaces/website-factory-operations/FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md` |
| `reports/website-factory-production-modes-implementation-pass-01.md` |

---

## Updated Documents (summary)

18 modified + 3 new = **21** documentation artifacts touched.

**Not touched (by design):** runtime code, agents implementation, governance expansion waves, WF-A02, WF-A03 layers, FP-0002 frontend workspace, reference-v1 frozen doctrine bulk rewrite.

---

**STOP AFTER REPORT** — No further implementation. No Pixel Factory work. No Validation Architecture work.

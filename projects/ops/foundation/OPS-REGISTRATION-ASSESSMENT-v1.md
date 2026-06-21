# OPS — Registration Assessment v1

**Status:** **documented** — formal registration assessment only.  
**Program:** OPS — Business Operations Domain  
**Date:** 2026-06-04  
**Pass charter:** Governance registration assessment — **no registry edit**, **no topology edit**, **no lifecycle append**, **no `project_id` creation.  
**Parent:** [OPS-OPERATIONAL-MISSION-v1.md](OPS-OPERATIONAL-MISSION-v1.md) · [OPS-SYSTEM-POSITIONING-v1.md](OPS-SYSTEM-POSITIONING-v1.md) · [OPS-SUCCESS-CRITERIA-v1.md](OPS-SUCCESS-CRITERIA-v1.md)  
**Governance reference:** [mars-future-system-entry-discipline-v0.md](../../../governance/mars-future-system-entry-discipline-v0.md) · [registry-entry-minimal-standard.md](../../../governance/registry-entry-minimal-standard.md)

---

## 1. Purpose

Evaluate whether OPS should become a **registered MARS system** (`project_id` row + ecosystem visibility) based on foundation maturity, boundary clarity, and independence from peer systems — **without performing registration**.

---

## 2. Assessment matrix

For each dimension: **Assessment** (maturity band) · **Evidence** (repo paths) · **Risk** (if registered prematurely) · **Conclusion**.

| Dimension | Assessment | Evidence | Risk | Conclusion |
|-----------|------------|----------|------|------------|
| **Mission maturity** | **Strong** | [OPS-OPERATIONAL-MISSION-v1.md](OPS-OPERATIONAL-MISSION-v1.md); Phase 4 report §3 | Mission drift if registered before pilot proves operator value | **Ready for governance read** — mission is stable enough to justify a future row |
| **Boundary maturity** | **Strong** | [OPS-BOUNDARIES-v1.md](OPS-BOUNDARIES-v1.md) O-01–O-06, X-01–X-14; creep rules BR-01–BR-04 | Authority creep (CRM/accounting/legal) if boundaries not cited in registry note | **Ready** — exclusions are explicit and repeated in README |
| **Data model maturity** | **Strong (documented)** | [OPS-OPERATIONAL-DATA-MODEL-v1.md](OPS-OPERATIONAL-DATA-MODEL-v1.md); case/approval/deadline/status models | Shadow SoT if persistence is invented outside ATLAS discipline | **Ready at doc level** — implementation/persistence **not** evidenced |
| **Workflow maturity** | **Strong (documented)** | [OPS-WORKFLOW-ARCHITECTURE-v1.md](OPS-WORKFLOW-ARCHITECTURE-v1.md); WF-01–WF-06 under `projects/ops/workflows/` | False automation claims if registry row implies runtime | **Ready at doc level** — WF-01 pilot **not** executed |
| **Consumer maturity** | **Moderate** | [OPS-CONSUMER-MODEL-v1.md](OPS-CONSUMER-MODEL-v1.md); operator-centered norm | HomeGateway/ATLAS consumers assumed without contracts | **Partial** — primary consumer clear; integration consumers **SAFE UNKNOWN** |
| **Ecosystem positioning maturity** | **Strong** | [OPS-SYSTEM-POSITIONING-v1.md](OPS-SYSTEM-POSITIONING-v1.md); [OPS-ECOSYSTEM-RELATIONSHIPS-v1.md](OPS-ECOSYSTEM-RELATIONSHIPS-v1.md) | Duplicate lane if misclassified as ATLAS or HomeGateway extension | **Ready** — separate domain rationale is evidenced |
| **Operational usefulness** | **Unverified (human)** | MVP in [OPS-MVP-SCOPE-v1.md](OPS-MVP-SCOPE-v1.md); success criteria VC/DC/PR | Registry row without walkthrough invites mythology | **Not proven** — requires WF-01 pilot report |
| **Independence from ATLAS** | **Strong** | [OPS-ATLAS-RELATIONSHIP-v1.md](OPS-ATLAS-RELATIONSHIP-v1.md); consumer not SoT | OPS registered as “mini-ATLAS” | **Independent** — consumes ATLAS; does not replace |
| **Independence from HomeGateway** | **Strong** | README § HomeGateway; positioning §4.2 | Cockpit mistaken as workflow SoT | **Independent** — surface vs domain split documented |
| **Independence from MetaBOT** | **Strong** | Boundaries X-11; MVP O-10; ecosystem map | Live n8n integration implied by registry | **Independent** — human-attested evidence only |
| **Independence from ORCA** | **Strong** | Boundaries X-09; positioning PPC row | OPS owns PPC truth | **Independent** — citation-only in reports |
| **Independence from WPilot/OCPilot** | **Strong** | Boundaries X-12; README CMS rows | Storefront ops absorbed into OPS | **Independent** — operational reporting references only |

**Maturity legend:** **Strong** = normative docs complete and consistent · **Moderate** = documented with explicit UNKNOWNs · **Unverified** = requires human pilot or external evidence.

---

## 3. Registration options evaluated

| Option | Description | Fit |
|--------|-------------|-----|
| **A) Independent registered system** | `project_id` `ops` in [project-registry.md](../../../registry/project-registry.md) + topology + reality rows | **Best fit** if registration proceeds — matches `projects/ops/` pack pattern (ORCA, MIG class) |
| **B) Internal domain under another system** | Subordinate to ATLAS or HomeGateway | **Poor fit** — would blur identity SoT vs operational case lifecycle (positioning §2) |
| **C) Deferred / not registered** | Remain doc-only pack without ecosystem row | **Current state** — acceptable until pilot + entry discipline pass |

---

## 4. MARS entry discipline (seven items) — snapshot

Per [mars-future-system-entry-discipline-v0.md](../../../governance/mars-future-system-entry-discipline-v0.md):

| # | Requirement | OPS state (2026-06-04) |
|---|-------------|------------------------|
| 1 | Topology row | **Missing** — not in [ecosystem-topology-index.md](../../../governance/ecosystem-topology-index.md) |
| 2 | Reality row | **Missing** — not in [mars-reality-index-v0.md](../../../governance/mars-reality-index-v0.md) |
| 3 | Canonical entrypoint | **Present** — [README.md](../README.md) |
| 4 | OPERATIONAL-INDEX | **Present** — [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) (Core Run **27** rows — exceeds ≤10 session guideline) |
| 5 | Lifecycle append | **Missing** — no OPS registration event in `logs/lifecycle-log.md` |
| 6 | Lane assignment | **Implicit only** — Path B in-repo pack; not recorded in onboarding strategy |
| 7 | Registry row | **Missing** — no `ops` in project registry |

**Score:** **2/7 complete** for full ecosystem visibility. Documentation foundation is ahead of governance surfaces.

---

## 5. Comparative registry evidence

| Peer | Registration pattern | OPS analogy |
|------|---------------------|-------------|
| **ATLAS** | `atlas` row, topology, planned/foundation — [atlas-registration-v1.md](../../../logs/atlas/atlas-registration-v1.md) | OPS has comparable foundation depth; ATLAS registered **without** runtime |
| **ORCA** | `orca` active operational pack | OPS is operational doc-first; different domain (back-office vs PPC) |
| **GitGuard** | Registered **without** `project_id` | OPS is **not** survivability overlay — full pack justifies `project_id` if registered |
| **IdeaBox** | **Not** a project row | OPS is **not** optional incubation — scoped charter and MVP exist |

---

## 6. Blockers to registration (actionable)

| ID | Blocker | Severity |
|----|---------|----------|
| **B-01** | No WF-01 human pilot report (PR-01–PR-03 unverified) | **High** |
| **B-02** Entry discipline items 1, 2, 5, 6, 7 not done | **High** (for “ecosystem-visible” claim) |
| **B-03** ATLAS read/export consumer contract **SAFE UNKNOWN** | **Medium** |
| **B-04** Evidence storage location for monthly artifacts **SAFE UNKNOWN** | **Medium** |
| **B-05** OPERATIONAL-INDEX Core Run >10 rows — compression before scaling references | **Low–Medium** |

---

## 7. Final recommendation (registration action)

| Decision | Value |
|----------|-------|
| **Register in this pass?** | **No** |
| **Formal verdict** | **DEFER** |
| **Target posture after unblock** | **Independent registered system** (`project_id` `ops`, `status: planned`, phase **FOUNDATION** or **OPERATIONAL** doc-only) |
| **Recommended timing label** | **REGISTER AFTER PILOT** — not indefinite deferral |

### Reasoning

1. **Documentation foundation (Phases 1–4) is complete** — mission, boundaries, data model, workflows, consumers, success criteria, and ecosystem map provide sufficient material for a registry **note** and topology blurb.
2. **Operational usefulness is not evidenced** — no `REPORT-ops-wf01-pilot-v1.md` or equivalent; registering before pilot risks registry mythology per MARS honesty rules.
3. **Ecosystem visibility checklist is incomplete** — registering only the registry row without topology/reality/lifecycle in the same governance pass would recreate drift ATLAS registration avoided.
4. **Separate system (Option A) is correct** — Option B would misplace OPS under ATLAS or HomeGateway and weaken anti-duplication rules.

**Do not register until:** (a) at least one supervised WF-01 cycle recorded, and (b) a dedicated **registration execution pass** completes items 1–7 (charter separate from this assessment).

---

## 8. SAFE UNKNOWN

| Topic | Unknown | Verification |
|-------|---------|--------------|
| Preferred `status` at registration | `planned` vs `active` for doc-only pack | Human architect at registration pass |
| `related_entities` at registration | Agent cards deferred | Explicit “none” until cards chartered |
| HomeGateway OPS module | Display contract | HomeGateway integration charter |

---

*OPS Registration Assessment v1 — assessment only; no registry mutation.*

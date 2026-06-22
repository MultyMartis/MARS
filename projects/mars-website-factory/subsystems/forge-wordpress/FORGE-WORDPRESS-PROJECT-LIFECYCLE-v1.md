# Forge WordPress — Project Lifecycle v1

**Document type:** Project lifecycle methodology  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01

**Mapping:** Stages FWP-01–FWP-12 map to architecture layers L1–L10 — see [FORGE-WORDPRESS-ARCHITECTURE-v1.md](FORGE-WORDPRESS-ARCHITECTURE-v1.md).

**FW-01 honesty:** Stages FWP-06+ are **methodologically defined** — **not executable** until FW-05 pilot charter.

---

## Lifecycle diagram

```text
FWP-01 Intake
    ↓ [G1: handoff acknowledged]
FWP-02 Frontend Readiness Audit
    ↓ [G2: readiness PASS]
FWP-03 WordPress Architecture Decision
    ↓ [G3: WAD approved]
FWP-04 Content Model ──┐
FWP-05 Theme/Function  ├── parallel (design phase)
FWP-05b Admin UX ─────┘
    ↓ [G4: design package approved]
FWP-06 Implementation Specification
    ↓ [G5: spec approved — spec-first gate]
FWP-07 Local / DEV Implementation
    ↓ [G6: implementation complete — human review]
FWP-08 Automated Validation (WV)
    ↓ [G7: WV blockers cleared]
FWP-09 Visual and Admin QA
    ↓ [G8: operator acceptance]
FWP-10 Release Candidate Packaging
    ↓ [G9: manifest complete]
FWP-11 WPilot Handoff
    ↓ [G10: handoff accepted]
FWP-12 Post-Handoff Learning
```

*Note:* Original input merged FWP-05/06 naming — this v1 uses FWP-05 for parallel design, FWP-06 for consolidated spec (L7), FWP-07 for implementation (L8) for clarity.

---

## Stage registry

### FWP-01 — Intake

| Field | Value |
|-------|-------|
| **Inputs** | Factory frontend handoff; project passport; operator assignment |
| **Actions** | Register project in Forge WordPress artifact tree; verify Factory VL completion claim; assign mode candidate |
| **Outputs** | `PROJECT-INTAKE`; `FRONTEND-HANDOFF` acknowledgment |
| **Gate G1** | Handoff manifest signed; production mode known |
| **Blockers** | No handoff; VL6 not claimed; missing passport |
| **Responsibility** | Human operator + Forge WordPress Architect |
| **Prohibited shortcuts** | Skipping handoff checklist; starting audit without LOC-ZONE path |

---

### FWP-02 — Frontend Readiness Audit

| Field | Value |
|-------|-------|
| **Inputs** | Frontend package; Factory QA reports; build instructions |
| **Actions** | Reproduce build; inventory pages/blocks/assets; flag gaps |
| **Outputs** | `FRONTEND-READINESS-REPORT` |
| **Gate G2** | Readiness PASS or scoped waiver |
| **Blockers** | Broken build; missing critical pages (PIXEL_PERFECT); undeclared assets |
| **Responsibility** | Forge WordPress Architect |
| **Prohibited shortcuts** | Auditing from stale dist; fixing frontend in WP lane |

---

### FWP-03 — WordPress Architecture Decision

| Field | Value |
|-------|-------|
| **Inputs** | Readiness report; hosting notes; implementation modes doc |
| **Actions** | Produce WAD; score decision matrix; declare Mode A–D |
| **Outputs** | `WORDPRESS-ARCHITECTURE-DECISION` |
| **Gate G3** | Human-approved WAD |
| **Blockers** | Unresolved mode; Mode D without charter |
| **Responsibility** | Forge WordPress Architect — **human approval** |
| **Prohibited shortcuts** | Defaulting to builder; skipping matrix |

---

### FWP-04 — Content Model

| Field | Value |
|-------|-------|
| **Inputs** | WAD; IA; frontend block inventory |
| **Actions** | Define CPT, taxonomies, fields, relationships, REST policy |
| **Outputs** | `CONTENT-MODEL`; `CPT-TAXONOMY-MAP`; `ACF-SCHEMA` (conditional) |
| **Gate** | Part of G4 design package |
| **Blockers** | Conflicts with WAD; unnamed editorial roles |
| **Responsibility** | Content Modeler |
| **Prohibited shortcuts** | Copying theme structure into CPT without review |

---

### FWP-05 — Theme, Functionality, and Admin UX (design)

| Field | Value |
|-------|-------|
| **Inputs** | WAD; content model; frontend mapping |
| **Actions** | Theme architecture; plugin boundary; template map; admin UX map; plugin register |
| **Outputs** | `THEME-ARCHITECTURE`; `FUNCTIONALITY-BOUNDARY`; `TEMPLATE-MAP`; `BLOCK-TO-WP-MAPPING`; `ADMIN-UX-MAP`; `EDITABLE-REGIONS-MAP`; `PLUGIN-REGISTER` |
| **Gate G4** | Design package human-approved |
| **Blockers** | Missing editable-regions map; unapproved third-party plugins |
| **Responsibility** | Theme + Admin UX specialists |
| **Prohibited shortcuts** | Implementation before G4 |

---

### FWP-06 — Implementation Specification

| Field | Value |
|-------|-------|
| **Inputs** | All FWP-03–05 artifacts |
| **Actions** | Consolidate spec; define file tree; enqueue plan; validation plan |
| **Outputs** | `IMPLEMENTATION-SPEC`; `VALIDATION-PLAN` |
| **Gate G5** | **BLOCKING** spec approval — spec-first |
| **Blockers** | Incomplete artifacts; spec/code drift |
| **Responsibility** | Forge WordPress Architect |
| **Prohibited shortcuts** | **Any code before G5** |

---

### FWP-07 — Local / DEV Implementation

| Field | Value |
|-------|-------|
| **Inputs** | Approved spec; local WP environment |
| **Actions** | Implement theme, plugin, ACF JSON, assets integration |
| **Outputs** | Implementation branch; working local site |
| **Gate G6** | Human review of implementation vs spec |
| **Blockers** | Spec deviation; production access attempt |
| **Responsibility** | Theme Implementation Specialist (future agent) |
| **Prohibited shortcuts** | Production deploy; unreviewed plugin installs |
| **FW-01 status** | **NOT EXECUTABLE** |

---

### FWP-08 — Automated Validation

| Field | Value |
|-------|-------|
| **Inputs** | Implementation branch; validation plan |
| **Actions** | Run WV0–WV9 applicable layers |
| **Outputs** | Validation reports per layer |
| **Gate G7** | No WV blocking failures |
| **Blockers** | PHPCS fail; security fail; critical functional fail |
| **Responsibility** | WordPress Validator + tooling |
| **Prohibited shortcuts** | Skipping WV4 security |

---

### FWP-09 — Visual and Admin QA

| Field | Value |
|-------|-------|
| **Inputs** | Validated build; frontend reference |
| **Actions** | Visual parity review; admin walkthrough |
| **Outputs** | `VISUAL-QA-REPORT`; admin QA notes |
| **Gate G8** | Operator acceptance (PIXEL_PERFECT: mandatory visual sign-off) |
| **Blockers** | Unresolved parity failures; admin UX violations |
| **Responsibility** | Visual Parity Validator + human operator |
| **Prohibited shortcuts** | TECHNICAL PASS without operator approval |

---

### FWP-10 — Release Candidate Packaging

| Field | Value |
|-------|-------|
| **Inputs** | Accepted build; validation reports |
| **Actions** | Assemble release manifest; version tag; package theme/plugin ZIPs |
| **Outputs** | `RELEASE-MANIFEST` |
| **Gate G9** | Manifest completeness |
| **Blockers** | Missing validation evidence |
| **Responsibility** | Forge WordPress Architect |
| **Prohibited shortcuts** | Packaging with failing WV |

---

### FWP-11 — WPilot Handoff

| Field | Value |
|-------|-------|
| **Inputs** | Release candidate; handoff boundary checklist |
| **Actions** | Transfer package; document frozen/editable zones; WPilot briefing |
| **Outputs** | `WPILOT-HANDOFF` |
| **Gate G10** | WPilot Handoff Reviewer + operator acceptance |
| **Blockers** | Incomplete handoff contract; credential leakage |
| **Responsibility** | WPilot Handoff Reviewer (**HUMAN ONLY** final sign-off) |
| **Prohibited shortcuts** | Handoff without WV9 |

---

### FWP-12 — Post-Handoff Learning

| Field | Value |
|-------|-------|
| **Inputs** | Handoff outcome; WPilot feedback; pilot metrics |
| **Actions** | Lessons learned; research register update; methodology patches |
| **Outputs** | `LESSONS-LEARNED`; optional register entries |
| **Gate** | None blocking — continuous improvement |
| **Blockers** | N/A |
| **Responsibility** | Human operator |
| **Prohibited shortcuts** | Retrofit lessons without evidence |

---

## Related documents

- [FORGE-WORDPRESS-PROJECT-ARTIFACT-MODEL-v1.md](FORGE-WORDPRESS-PROJECT-ARTIFACT-MODEL-v1.md)
- [FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md)

---

*Project lifecycle v1 — gates documented; implementation not authorized.*

# Forge WordPress — Architecture v1

**Document type:** Subsystem architecture (methodology)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-01 — Architecture and Methodology  
**Lifecycle:** FOUNDATION (architecture documented; implementation **NOT STARTED**)

**Authority:** This document is MARS canonical architecture for Forge WordPress. Research Base v1 is evidence only — see [FORGE-WORDPRESS-RESEARCH-ADAPTATION-REGISTER-v1.md](FORGE-WORDPRESS-RESEARCH-ADAPTATION-REGISTER-v1.md).

**Honesty:** Architecture documentation ≠ operational capability ≠ runtime.

---

## 1. Purpose

Define the **layered architecture** of Forge WordPress as a human-supervised WordPress implementation subsystem between **Website Factory** (upstream frontend) and **WPilot** (downstream operations).

Forge WordPress transforms an **approved frontend package** into a **WordPress implementation package** through specification-first, sandbox-first, validation-gated work — without autonomous production control.

---

## 2. Architectural position

```text
Website Factory (VL0–VL6 frontend validation)
    → approved frontend handoff package
Forge WordPress (FWP lifecycle + WV0–WV9 validation)
    → WordPress implementation release candidate
WPilot (controlled operations on existing sites)
    → production/staging operations within chartered limits
```

**Orthogonal planes:**

| Plane | Scope |
|-------|--------|
| **Factory VL** | Upstream static frontend — ends at frontend handoff gate |
| **Forge FWP** | WordPress project lifecycle stages |
| **Forge WV** | WordPress-specific validation layers |
| **Human control** | Approval classes per [FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md](FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md) |

---

## 3. Layer model (canonical)

The preliminary layer list from Phase 1 input was reviewed and **adjusted** for MARS: **Implementation Planning** is elevated as a distinct gate-bearing layer; **Packaging** is merged with release-candidate semantics under validation/handoff; **Local/DEV Execution** is explicitly non-production.

```text
Forge WordPress
├── L1  Intake and Frontend Handoff
├── L2  Frontend Readiness Audit
├── L3  WordPress Architecture Decision
├── L4  Content Modeling
├── L5  Theme and Functionality Architecture
├── L6  Admin Experience Design
├── L7  Implementation Specification
├── L8  Local / DEV Implementation (future — chartered)
├── L9  Validation and QA
└── L10 WPilot Handoff
```

**Descent order:** L1 → L2 → L3 → L4/L5/L6 (parallel design) → L7 → L8 → L9 → L10. No layer skip without documented waiver.

---

## 4. Layer definitions

### L1 — Intake and Frontend Handoff

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Accept a WordPress-bound project into Forge WordPress only when Factory frontend handoff preconditions are met. |
| **Inputs** | Factory frontend handoff package; project passport; production mode (`PIXEL_PERFECT` \| `TEMPLATE_ART`); LOC-ZONE project folder reference. |
| **Outputs** | `PROJECT-INTAKE` record; `FRONTEND-HANDOFF` acknowledgment; assigned implementation mode candidate (Mode A–D). |
| **Authority** | Human operator + Forge WordPress Architect (methodology). |
| **Human gate** | **BLOCKING** — no WordPress work without signed handoff acknowledgment. |
| **Future automation** | Checklist validation of handoff manifest completeness (FUTURE SKILL). |
| **Forbidden** | Accepting incomplete frontend; bypassing Factory VL6; starting theme code. |
| **Dependent systems** | Website Factory; LOC-ZONE; [frontend-handoff-contract-v0.md](../../frontend-handoff-contract-v0.md) (upstream — FW-02 will formalize WP-specific contract). |

---

### L2 — Frontend Readiness Audit

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Verify the approved frontend package is sufficient for WordPress conversion (structure, assets, build reproducibility, editable-region candidates). |
| **Inputs** | Frontend dist/build; block inventory; design mapping artifacts; Factory QA reports (VL4–VL6). |
| **Outputs** | `FRONTEND-READINESS-REPORT`; editable-region candidates; block-to-surface preliminary map. |
| **Authority** | Forge WordPress Architect + Visual Parity Validator (review). |
| **Human gate** | **BLOCKING** on critical gaps (missing pages, broken build, undeclared production mode mismatch). |
| **Future automation** | Frontend package manifest diff vs template map (FUTURE SKILL). |
| **Forbidden** | Redesigning frontend; modifying Factory workspace without charter. |
| **Dependent systems** | Gulp Frontend Agent deliverables; Factory validation architecture (VL upstream only). |

---

### L3 — WordPress Architecture Decision

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Select implementation mode (A–D), classic/hybrid/block posture per section, theme vs plugin boundary, and tooling posture for the project. |
| **Inputs** | Frontend readiness report; hosting constraints; WPilot compatibility notes; research adaptation register. |
| **Outputs** | `WORDPRESS-ARCHITECTURE-DECISION` (WAD); mode declaration; risk register. |
| **Authority** | Human operator approval on WAD. |
| **Human gate** | **BLOCKING** — no content model or theme architecture without approved WAD. |
| **Future automation** | Decision matrix scoring assist (METHODOLOGY ONLY until FW-02 standards). |
| **Forbidden** | Defaulting all projects to block theme or page builders; Mode D without charter. |
| **Dependent systems** | [FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md](FORGE-WORDPRESS-IMPLEMENTATION-MODES-v1.md); [FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md](FORGE-WORDPRESS-ARCHITECTURAL-DECISIONS-v1.md). |

---

### L4 — Content Modeling

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Define portable content architecture independent of presentation theme. |
| **Inputs** | WAD; IA/blueprint artifacts; frontend block inventory; editorial requirements. |
| **Outputs** | `CONTENT-MODEL`; `CPT-TAXONOMY-MAP`; `ACF-SCHEMA` (when ACF mode selected); REST/capability notes. |
| **Authority** | Content Modeler role; human approval on content model. |
| **Human gate** | **BLOCKING** — content model errors are high-cost; require explicit sign-off. |
| **Future automation** | CPT/ACF scaffold generation from approved spec (FUTURE SKILL — post FW-05). |
| **Forbidden** | CPT in theme for portable content; undeclared meta without REST policy. |
| **Dependent systems** | ACF (preferred layer — see architectural decisions); core `register_post_type` when ACF-deferred. |

---

### L5 — Theme and Functionality Architecture

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Map presentation to theme; map business logic and portable registrations to functionality plugin boundary. |
| **Inputs** | WAD; content model; frontend HTML/CSS/JS structure; `BLOCK-TO-WP-MAPPING`. |
| **Outputs** | `THEME-ARCHITECTURE`; `FUNCTIONALITY-BOUNDARY`; `TEMPLATE-MAP`; `PLUGIN-REGISTER` (third-party). |
| **Authority** | Theme Implementation Specialist + human approval. |
| **Human gate** | **BLOCKING** before implementation spec. |
| **Future automation** | Template scaffold from mapping table (FUTURE SKILL). |
| **Forbidden** | Monolithic theme containing all CPT logic; unrestricted third-party plugins. |
| **Dependent systems** | Factory frontend assets; shared hosting constraints. |

---

### L6 — Admin Experience Design

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Design curated editor surface — what is editable, locked, or hidden. |
| **Inputs** | Content model; WAD; editable regions map; client editorial requirements. |
| **Outputs** | `ADMIN-UX-MAP`; `EDITABLE-REGIONS-MAP`; editor governance rules. |
| **Authority** | Admin UX Specialist; human operator approval for editorial freedom level. |
| **Human gate** | **BLOCKING** for client-facing projects before implementation. |
| **Future automation** | ACF location/rule generation from map (FUTURE SKILL). |
| **Forbidden** | Full-site editor freedom by default; exposing theme structure to casual editors. |
| **Dependent systems** | ACF; block locking; WPilot operational limits (downstream). |

---

### L7 — Implementation Specification

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Consolidate all design layers into a single implementation-ready specification before any code. |
| **Inputs** | All L3–L6 artifacts; validation plan skeleton. |
| **Outputs** | `IMPLEMENTATION-SPEC`; `VALIDATION-PLAN`. |
| **Authority** | Forge WordPress Architect; human approval **BLOCKING**. |
| **Human gate** | **BLOCKING** — spec-first gate (ADOPT from research). |
| **Future automation** | Spec completeness linter (FUTURE SKILL). |
| **Forbidden** | Code generation before approved spec; spec drift without version bump. |
| **Dependent systems** | Git; project artifact model. |

---

### L8 — Local / DEV Implementation

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Execute theme/plugin/code implementation in isolated local or DEV WordPress environment only. |
| **Inputs** | Approved implementation spec; version-controlled repo; local WP stack. |
| **Outputs** | Theme code; functionality plugin code; ACF JSON; built assets; implementation branch. |
| **Authority** | Theme Implementation Specialist (human-supervised); primary future agent candidate. |
| **Human gate** | **Approval required** for merge to main implementation branch; no production deploy. |
| **Future automation** | Cursor-assisted implementation under AGENTS.md + spec (FUTURE AGENT — post charter). |
| **Forbidden** | Production coding; direct live DB mutation; unreviewed plugin installs. |
| **Dependent systems** | Tooling architecture; Windows-compatible local stack; npm frontend build reuse. |

**FW-01 status:** Layer defined **methodologically only** — not executed.

---

### L9 — Validation and QA

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Prove implementation correctness, security, visual parity, and admin UX before release candidate. |
| **Inputs** | Implementation branch; frontend reference; validation plan. |
| **Outputs** | WV reports; `VISUAL-QA-REPORT`; security review notes; release readiness disposition. |
| **Authority** | Independent validators + human operator acceptance. |
| **Human gate** | **BLOCKING** for handoff — see WV0–WV9. |
| **Future automation** | PHPCS, Playwright, screenshot diff runners (FW-03 tooling design). |
| **Forbidden** | Skipping security layer; visual sign-off without operator review for PIXEL_PERFECT. |
| **Dependent systems** | [FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md); Factory operator visual approval law (upstream reference). |

---

### L10 — WPilot Handoff

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Package and transfer implementation to operations lane with frozen zones and operational contract. |
| **Inputs** | Release candidate; all validation reports; editable regions map; plugin register. |
| **Outputs** | `RELEASE-MANIFEST`; `WPILOT-HANDOFF` package; deployment instructions (for WPilot/operator — not autonomous). |
| **Authority** | WPilot Handoff Reviewer + human operator. |
| **Human gate** | **BLOCKING** — handoff without complete WV9 fails. |
| **Future automation** | Manifest generator from repo + reports (FUTURE SKILL). |
| **Forbidden** | WPilot scope creep into development; production credentials in package. |
| **Dependent systems** | [projects/wpilot/OPERATIONAL-INDEX.md](../../../wpilot/OPERATIONAL-INDEX.md); handoff boundaries doc. |

---

## 5. Cross-cutting concerns

| Concern | Handling |
|---------|----------|
| **Version control** | All implementation artifacts in Git — ADOPT |
| **Sandbox-first** | L8 runs only in local/DEV — ADOPT |
| **Spec-first** | L7 gate before L8 — ADOPT |
| **Human merge** | No autonomous production merge — ADOPT |
| **MARS Forge ≠ Forge WordPress** | Frontend overlay has no role in L4–L10 — MARS boundary |

---

## 6. Related documents

| Document | Role |
|----------|------|
| [FORGE-WORDPRESS-CAPABILITY-MODEL-v1.md](FORGE-WORDPRESS-CAPABILITY-MODEL-v1.md) | Capability mapping to layers |
| [FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md](FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md) | Stage gates FWP-01–FWP-12 |
| [FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md](FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md) | External boundaries |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation |

---

*Architecture v1 — FW-01. Methodology only. Not implementation authorization.*

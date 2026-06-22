# Forge WordPress Prompt Pack v1

**Document type:** Ready prompt starters  
**Version:** v1  
**Stage:** FW-04

**No project-specific data.** Replace `<TARGET>` and paths per active project.

---

## 1. Frontend inspection

```text
# TASK — Forge WordPress Frontend Package Inspection

TARGET FOLDER: <project-artifacts>/forge-wordpress/
CURSOR MODE: Agent
PROJECT ID: <slug>
CURRENT STAGE: FWP-02 Intake / Inspection

OBJECTIVE: Inspect approved frontend package and produce handoff completeness checklist.

INPUT AUTHORITY: FW-SK-01, FW-C-01 handoff contract
ALLOWED WRITE SCOPE: <project-artifacts>/forge-wordpress/inspection/
READ-ONLY SCOPE: <approved-frontend-path>/, subsystem docs
FORBIDDEN SCOPE: Production, unrelated WIP, frontend edits

STOP CONDITION: Frontend not operator-approved — STOP and report.

REQUIRED REPORT: # REPORT — Forge WordPress Frontend Package Inspection
```

---

## 2. WordPress architecture decision

```text
# TASK — Forge WordPress Architecture Decision (WAD)

TARGET FOLDER: <project-artifacts>/forge-wordpress/architecture/
CURSOR MODE: Agent
SKILL: FW-SK-02

OBJECTIVE: Produce WAD — mode, theme/plugin boundary, template strategy, validation approach.

REQUIRED INPUTS: Inspection report, project intake, implementation mode
HUMAN GATE: Operator approval before content model or implementation

STOP CONDITION: Missing inspection pass — STOP.

REQUIRED REPORT: # REPORT — Forge WordPress Architecture Decision
```

---

## 3. Content model design

```text
# TASK — Forge WordPress Content Model Design

TARGET FOLDER: <project-artifacts>/forge-wordpress/content-model/
SKILL: FW-SK-03

OBJECTIVE: Define content types, editable regions, and IA mapping.

REQUIRED INPUTS: Approved WAD, content evidence, frontend page inventory
HUMAN GATE: Operator approval before ACF/CPT implementation

REQUIRED REPORT: # REPORT — Forge WordPress Content Model Design
```

---

## 4. Theme architecture

```text
# TASK — Forge WordPress Theme Architecture

TARGET FOLDER: <project-artifacts>/forge-wordpress/architecture/
SKILL: FW-SK-05

OBJECTIVE: Define theme scaffold, template hierarchy, asset strategy, partials map.

REQUIRED INPUTS: Approved WAD, block-to-WP map draft
HUMAN GATE: Operator approval before code implementation

REQUIRED REPORT: # REPORT — Forge WordPress Theme Architecture
```

---

## 5. ACF design

```text
# TASK — Forge WordPress ACF Architecture

TARGET FOLDER: <project-artifacts>/forge-wordpress/acf/
SKILL: FW-SK-06

OBJECTIVE: Produce ACF field group schema and Local JSON plan.

REQUIRED INPUTS: Approved content model, editable regions map
HUMAN GATE: Operator approval before field registration code

REQUIRED REPORT: # REPORT — Forge WordPress ACF Architecture
```

---

## 6. Implementation specification

```text
# TASK — Forge WordPress Implementation Specification

TARGET FOLDER: <project-artifacts>/forge-wordpress/spec/
SKILL: FW-SK-09

OBJECTIVE: Consolidate WAD, maps, and plans into ordered implementation spec.

REQUIRED INPUTS: All approved design artifacts
HUMAN GATE: BLOCKING — no FW-SK-10 without approved spec

REQUIRED REPORT: # REPORT — Forge WordPress Implementation Specification
```

---

## 7. Theme implementation

```text
# TASK — Forge WordPress Theme Implementation

TARGET FOLDER: <wp-workspace>/wp-content/themes/<theme-slug>/
SKILL: FW-SK-10

OBJECTIVE: Implement approved theme per spec — foundation through interactions.

REQUIRED INPUTS: Approved implementation spec, read-only frontend
ALLOWED WRITE: Theme directory, functionality plugin, ACF JSON only
FORBIDDEN: Production, core edits, silent plugin installs

REQUIRED REPORT: # REPORT — Forge WordPress Theme Implementation
```

---

## 8. Validation

```text
# TASK — Forge WordPress Validation Pass

TARGET FOLDER: <project-artifacts>/validation/
SKILLS: FW-SK-11; Validators FW-V-01 through FW-V-04

OBJECTIVE: Run validation chain; produce independent validator reports.

INDEPENDENCE: Separate pass — implementer must not approve WV6/security

REQUIRED REPORT: # REPORT — Forge WordPress Validation Pass
```

---

## 9. Visual comparison

```text
# TASK — Forge WordPress Visual Parity Comparison

TARGET FOLDER: <project-artifacts>/validation/visual/
SKILL: FW-SK-12; Validator FW-V-05

OBJECTIVE: Compare local WordPress render to approved frontend baselines.

HUMAN GATE: Operator visual approval required for PASS

STOP CONDITION: Do not mark PASS without operator sign-off

REQUIRED REPORT: # REPORT — Forge WordPress Visual Parity Comparison
```

---

## 10. Release packaging

```text
# TASK — Forge WordPress Release Packaging

TARGET FOLDER: <project-artifacts>/release/
SKILL: FW-SK-13; Validator FW-V-07

OBJECTIVE: Build release manifest and staged package from validated artifacts.

REQUIRED INPUTS: Validation pass, implementation complete
FORBIDDEN: Include secrets, uploads, core, vendor without register

REQUIRED REPORT: # REPORT — Forge WordPress Release Packaging
```

---

## 11. WPilot handoff

```text
# TASK — Forge WordPress WPilot Handoff Preparation

TARGET FOLDER: <project-artifacts>/handoff/
SKILL: FW-SK-14; Validator FW-V-07

OBJECTIVE: Produce WPilot handoff artifact per FW-C-03 — no live deployment.

HUMAN GATE: Handoff reviewer acceptance

REQUIRED REPORT: # REPORT — Forge WordPress WPilot Handoff Preparation
```

---

## Related

- [FORGE-WORDPRESS-CURSOR-TASK-TEMPLATE-v1.md](FORGE-WORDPRESS-CURSOR-TASK-TEMPLATE-v1.md)
- [../skills/](../skills/)

---

*Prompt pack v1 — generic starters only.*

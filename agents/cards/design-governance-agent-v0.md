# Agent card — Design Governance Agent (v0)

**Documentation-first:** **`planned`** in MARS Agent Registry §4.1 — **governance** role for **Canonical Design Implementation Pack** authoring; **human-supervised** only. **Not** autonomous runtime, **not** frontend implementation, **not** design generation.

---

| Field | Value |
|--------|--------|
| **agent_id** | `design_governance_agent` |
| **display_name** | Design Governance Agent / Implementation Pack Generator |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [Design Governance Agent — full role + input contract](../design-governance-agent.md)
- [Design Governance Layer](../../projects/mars-website-factory/design-governance-layer.md)
- [Canonical Design Implementation Pack architecture](../../projects/mars-website-factory/canonical-implementation-pack-architecture.md)
- [Agent input contracts (governance)](../../governance/agent-input-contracts.md)
- [Design Handoff Contract v0](../../projects/mars-website-factory/design-handoff-contract-v0.md)
- [Frontend Handoff Contract v0](../../projects/mars-website-factory/frontend-handoff-contract-v0.md)
- [Block Registry v0](../../projects/mars-website-factory/block-registry-v0.md)
- [MARS Forge — semantic source lock](../mars-forge/semantic-source-lock.md) (optional alignment)
- [Agent registry §4.1](../registry.md)

---

## primary_responsibilities

- Author **`semantics/`**, **`implementation-pack/`**, and **`validation/`** under **`projects/<project>/design/vN/`** per architecture doc.
- Enforce **version isolation** and **`shared-assets/` ≠ semantics** discipline.
- Align pack with blueprint, design handoff, and block registry; **escalate** conflicts (**SAFE UNKNOWN**, quarantine).

---

## non_responsibilities

- HTML/SCSS/JS implementation (**Gulp Frontend Agent** lane).
- Generating raster/Figma comps (**design execution** lane).
- Automated enforcement or orchestration (**no** runtime claim).

---

## inputs_outputs_summary

Full **agent input contract** (required/forbidden outputs, validation, SAFE UNKNOWN): [../design-governance-agent.md](../design-governance-agent.md) §5.

---

## validation

- **`validation/`** artifacts in active pack (`semantic-qa.md`, `responsive-qa.md`, `freeze-checklist.md`).
- Cross-role: **Design QA** (fidelity), **Frontend QA** (build/viewport); **human** freeze sign-off.

---

## changelog

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-16 | Initial card stub; SoT prose in ../design-governance-agent.md |

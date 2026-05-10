# MARS Website Factory — design layer model

## Purpose

Translate **strategy** and **page blueprints** into **experiential structure** and **visual specifications** suitable for **frontend handoff**. This layer is **documentation-first**; no claim of an automated design pipeline in MARS.

## Sub-stages (planned agents)

1. **UX Structure Agent** — section order, responsive behavior **intent**, focus order at a high level.
2. **Wireframe Generator Agent** — low-fidelity layout artifacts (format: markdown diagrams, structured YAML layout, or design tool export — **TBD**).
3. **AI Designer Agent** — applies **Design System Rules** and brand inputs; produces **direction** and token references.
4. **Full Design Generator Agent** — high-fidelity output; **must** remain bounded by **HITL** before build.

## Artifacts

| Artifact | Description |
|----------|-------------|
| Wireframes | Page-level structure before visual polish |
| Design spec | Tokens, type, color, spacing, component states |
| Asset list | Images, icons, fonts — with license notes |
| Handoff bundle | What **frontend-production-model** needs (see [implementation-phase-1.md](implementation-phase-1.md) **Design artifact contract**) |

## QA

- **Design QA Agent** (planned) checks consistency with tokens and blueprint **block** list.
- **Human** approval gate before **Gulp Frontend Agent** work (**workflow-map.md**).

## SAFE UNKNOWN

- **Figma** (or other tool) as SoT — **not** assumed; may be file-based only.
- Automated **design-to-code** — **not** claimed.

# MARS — System Entity Model

**Status:** documented — minimal governance baseline.
**Scope:** entity classification for MARS documentation and human-supervised operational packs.
**Not:** runtime identity service, registry engine, deployment proof, or automated enforcement.

## Purpose

This baseline separates large operational systems, agents, overlays, workflows, tools, adapters, runtime components, and external systems so documentation does not imply automation or ownership that is not evidenced in the repository.

Use this model when adding or classifying new MARS documentation packs. It complements existing registry, naming, external-system, and adapter boundary rules; it does not replace their local authority.

## Entity Types

| Entity type | Meaning | Default location | Examples |
|-------------|---------|------------------|----------|
| **Program / Operational System** | Large human-supervised operational direction, product area, or ecosystem that may contain agents, workflows, contracts, tools, reports, and external-system procedures. | `projects/<system-id>/` | MARS Website Factory, ORCA, WPilot, GitGuard, MetaBOT SEO Content Agent |
| **Agent** | Execution role, specialist persona, or operational behavior unit followed by a human or Cursor session. A documented agent is not proof of an autonomous running process. | `agents/<agent-id>/` | `mars-forge-frontend-agent`, `wp-audit-agent`, `css-patch-agent`, `backup-rollback-agent` |
| **Overlay** | Specialized behavior extension over an existing agent or workflow. It inherits a foundation and adds scoped rules, QA, or execution discipline without becoming a separate system by default. | `agents/<overlay-id>/` or inside the parent agent pack, depending on existing convention. | MARS Forge as a frontend execution overlay over the Gulp Frontend Agent, per current repo evidence. |
| **Workflow** | Ordered human-supervised task chain, checklist, or runbook. A workflow document is not a workflow engine. | `workflows/**` or inside the related project/system pack. | Inspection workflow, QA workflow, export workflow, rollback planning workflow. |
| **Tool / Tool Adapter** | Helper, integration, or interface to an external system or local procedure. A tool may assist a step; an adapter maps interfaces or payloads and must not be described as the external system itself. | `tools/**` or the related project/system pack. Runtime experiments may have narrow adapter files under explicitly experimental locations. | Markdown validators, registry checkers, API shape adapters, report helpers. |
| **Runtime Component** | Explicit runtime experiment, contract, or component boundary. Runtime wording is allowed only when the path and evidence support it. | `mars-runtime/**` | R1 runtime sketches, adapter experiments, execution-boundary contracts. |
| **External System** | Real outside system that MARS may document, inspect, or interact with, but does not own. Its live configuration, credentials, schedules, uptime, and execution truth remain external. | Referenced from the related project/system pack; not owned by MARS layout. | WordPress, Beget, n8n, GitHub, Google Sheets, hosting providers, model vendors. |

## Classification Rules

- Not every AI-related thing is an agent.
- Large systems/programs may contain many agents, workflows, templates, tools, and external-system procedures.
- A folder in `projects/` may represent a system, not only a client project.
- A folder in `agents/` should normally represent an agent card, role, overlay, or behavior pack.
- Registry row does not prove runtime implementation.
- Documentation does not prove deployed automation.
- External system integration does not transfer ownership of that system to MARS.
- Human remains final authority for approvals, credentials, production changes, and interpretation of SAFE UNKNOWN.

## Boundary Notes

- Use **Program / Operational System** for large human-supervised directions such as WPilot or ORCA.
- Use **Agent** only for a role or behavior unit with a bounded operating posture.
- Use **Overlay** when the pack extends an existing agent or workflow instead of standing alone.
- Use **Workflow** for ordered procedures, including workflows stored inside a project pack.
- Use **Tool / Tool Adapter** for helpers and integrations; do not rename external products as MARS-owned tools.
- Use **Runtime Component** only for explicit runtime experiments or contracts, and keep the claim **BOUNDARY ONLY** unless implementation evidence exists.
- Use **External System** for WordPress, Beget, n8n, GitHub, Google Sheets, hosting, or other real systems outside this repository.

## SAFE UNKNOWN

- Whether a future entity should be promoted into a registry row is unknown until a human makes that registry edit.
- Whether an external system is live, configured, or safe to modify is unknown until the operator provides verified external evidence.
- Whether a documented workflow has been executed is unknown unless a report, artifact, or operator confirmation states the run and scope.

## Cross-References

- [canonical-terminology-registry.md](canonical-terminology-registry.md)
- [identity-and-naming-rules.md](identity-and-naming-rules.md)
- [external-system-boundaries.md](external-system-boundaries.md)
- [adapter-and-bridge-boundaries.md](adapter-and-bridge-boundaries.md)
- [registry-architecture.md](registry-architecture.md)

# ORCA Approval Gates Contract v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — HITL gate vocabulary across intake → export → launch.

**Not** automated policy engine. **Not** workflow orchestration.

## Purpose

Named gates prevent draft artifacts from becoming operational truth in Factory, Commander, or client delivery.

## Gate Definitions

| Gate | Unlocks | Typical prerequisites |
|------|---------|----------------------|
| `approved_for_research_use` | Citing snapshot in strategy drafts | Inventory + evidence grading for sources used |
| `approved_for_strategy` | Campaign architecture and intent tiers | Research snapshots reviewed; contradictions noted |
| `approved_for_keywords` | Keyword pack as SoT for export | Strategy gate; semantic QA |
| `approved_for_factory` | Website Factory MODE 1 handoff | Approved landing brief(s); semantic lock preconditions |
| `approved_for_commander_import` | XLSX / sheet patch import to Direct | Validation report human-reviewed; registry URLs verified |
| `approved_for_launch` | Live ads with production URLs | Landing QA `approved_for_ads`; moderation clear; launch checklist |
| `approved_for_client_pdf` | External PDF audit / strategy delivery | Client-appropriate redaction; evidence levels marked |
| `approved_for_archive` | Project freeze / handoff to archive | Operator confirms no active export work |

## Authority Model

| Actor | May set gates? |
|-------|----------------|
| Human operator | **Yes** — sole authority for all gates |
| AI / Cursor / ORCA helper | **No** — may propose; may not set `approved_for_launch` or any gate automatically |
| Export CLI | **No** — produces artifacts; does not approve |
| Validation CLI | **No** — reports findings; does not approve |

**Critical:** `approved_for_launch` requires explicit human sign-off in `approvals/` or `PROJECT.md` with date and operator note.

## Recording Gates

| Location | Content |
|----------|---------|
| `projects/orca/projects/<project-id>/approvals/<gate>-<date>.md` | Checklist + sign-off |
| `PROJECT.md` | Summary flags per [project-md-contract-v0.md](../projects/project-md-contract-v0.md) |
| Artifact front-matter | `status: approved` aligned with gate (see [orca-artifact-system-v0.md](orca-artifact-system-v0.md) |

## Gate Dependency (recommended order)

```
intake distributed
  → approved_for_research_use
  → approved_for_strategy
  → approved_for_keywords
  → approved_for_factory
  → (Factory build + ppc landing QA)
  → approved_for_commander_import
  → approved_for_launch
```

Parallel paths (e.g. client PDF) may branch — document exceptions in decision log.

## Anti-Patterns

- Validation CLI green → assumed launch approval (**forbidden**)
- Draft brief → Factory MODE 1 without `approved_for_factory`
- AI session end → auto-update `PROJECT.md` gates (**forbidden**)

## SAFE UNKNOWN

- Client verbal approval without written record — treat as not approved
- Partial keyword pack approval — document scope in approval file

## Related Documents

- [orca-artifact-system-v0.md](orca-artifact-system-v0.md)
- [project-md-contract-v0.md](../projects/project-md-contract-v0.md)
- [ppc-landing-qa-contract-v0.md](../intelligence/ppc-landing-qa-contract-v0.md)
- [orca-factory-bridge-index-v0.md](../intelligence/orca-factory-bridge-index-v0.md)

## Boundary

Gate **names and discipline** only. No runtime enforcement product.

# ORCA Moderation Incident Registry v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — human-maintained log of ad platform and policy friction.

Not connected to Yandex API. Not auto-scraped from moderation UI.

## Purpose

Capture rejections, warnings, and fixes so the same symbol, claim, or creative mistake is not repeated — linked to [project-memory-system-v0.md](../intelligence/project-memory-system-v0.md) `moderation_failures` category.

## Storage Locations

| Scope | Path |
|-------|------|
| Per-project | `projects/orca/projects/<project-id>/logs/moderation-incidents.md` |
| Per-project JSON | `projects/orca/projects/<project-id>/logs/moderation-incidents.json` |
| Pack-local (Triumph) | `ppc/triumph-manipulator/logs/moderation-incidents.md` until migrated |

## Incident Categories (artifact types stored)

| Category | Examples |
|----------|----------|
| `rejected_symbols` | Banned punctuation, emoji, trademark misuse |
| `rejected_claims` | Unsubstantiated speed/price/guarantee |
| `rejected_ads` | Full ad disapproval |
| `rejected_images` | Creative policy, text-on-image |
| `rejected_fastlinks` | Sitelink / extension rejection |
| `warning_screenshots` | UI warnings before hard reject |
| `commander_import_warnings` | Direct Commander import validation messages |
| `yandex_moderation_results` | Post-submit moderation outcomes |
| `workaround` | Operator-approved alternative wording or structure |
| `final_approved_version` | Path to creative that passed |

## Record Fields

| Field | Required | Description |
|-------|----------|-------------|
| `incident_id` | yes | Stable id (e.g. `mod-2026-05-21-001`) |
| `date` | yes | ISO date of incident or discovery |
| `project_id` | yes | Project slug |
| `campaign_mode` | yes | `search`, `rsya`, … |
| `platform` | yes | `yandex_direct`, `google_ads`, `other` |
| `artifact_ref` | yes | Ad id, export row, screenshot path, handoff ref |
| `issue` | yes | Short description of rejection / warning |
| `evidence` | yes | Screenshot path, platform message text, export snippet |
| `severity` | yes | `blocker` \| `warning` \| `informational` |
| `fix` | if known | What changed to resolve |
| `status` | yes | `open` \| `fixed` \| `waived` \| `archived` |
| `lesson_learned` | recommended | One-line rule for project memory |

## Project Memory Link

On `status: fixed` with `lesson_learned`:

1. Append to `logs/memory/` or `PROJECT-MEMORY.md` under `moderation_failures`.
2. Reference `incident_id` in memory entry.
3. Update `PROJECT.md` SAFE UNKNOWN if issue blocked a gate.

Do **not** duplicate full incident text in memory — link only.

## Workflow (human-operated)

1. Capture evidence at rejection (screenshot + message).
2. Log incident with `open` status.
3. Apply fix in draft artifact; re-export if needed.
4. Record `final_approved_version` path when passed.
5. Close incident; promote lesson to project memory.

## SAFE UNKNOWN

- Platform policy interpretation without official doc
- Whether competitor uses same claim legally
- Auto-moderation vs human review distinction

## Related Documents

- [project-memory-system-v0.md](../intelligence/project-memory-system-v0.md)
- [approval-gates-contract-v0.md](../artifacts/approval-gates-contract-v0.md)
- [evidence-classification-system-v0.md](../evidence/evidence-classification-system-v0.md)

## Boundary

Documentation registry contract only. No moderation bot, no policy engine, no guaranteed compliance.

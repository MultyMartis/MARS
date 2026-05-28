# ORCA Landing Route Registry Contract v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — single registry contract for landing URLs across ORCA, Website Factory, export, and validation.

Not a hosted registry service. Not auto-populated from crawlers.

## Purpose

One operator-maintained source for **which landing URL** each PPC route uses — so Search packs, Factory pages, exporter mapping, and validation CLI (when configured) do not diverge silently.

## Registry Formats (choose one per project)

| Format | Path (recommended) |
|--------|-------------------|
| JSON | `projects/orca/projects/<project-id>/landing-route-registry.json` |
| MD table | Section in `PROJECT.md` or `projects/orca/projects/<project-id>/LANDING-ROUTES.md` |

Triumph (legacy): may use pack-local docs until migrated — registry still recommended for new routes.

## Record Fields

| Field | Required | Description |
|-------|----------|-------------|
| `route_id` | yes | Stable slug (e.g. `page-01-manipulyator-5-tonn`) |
| `project_id` | yes | Canonical project slug |
| `url` | yes | **Final landing URL** used in ads / Commander (HTTPS, production or staging as declared) |
| `slug` | yes | Path segment(s) without domain |
| `page_type` | yes | `master` \| `capability` \| `use-case` \| `b2b` \| `geo` \| `other` |
| `intent_group` | yes | Intent tier / cluster label from strategy |
| `campaign_modes` | yes | Array: `search`, `rsya`, … — which modes may use this route |
| `status` | yes | `draft` \| `needs_fix` \| `approved_for_ads` \| `approved_for_launch` \| `archived` |
| `source_blueprint` | if exists | Path to ORCA landing brief or Triumph blueprint |
| `website_factory_page` | if exists | Workspace path or dist URL to built page |
| `ppc_export_usage` | if exists | Campaign / ad group refs in export JSON or XLSX |
| `SAFE UNKNOWN` | optional | Fields not yet verified |

## Critical Distinction: Landing URL ≠ Display URL

| Concept | Role | Where it lives |
|---------|------|----------------|
| **Landing URL** | User destination after click — **this registry** | `url` field |
| **Display URL** | Visible path in ad (Yandex display path) | **PPC export artifact** — ad extensions / ad row — **not** this registry |

**Rule:** Never copy display path into `url` without operator verification. Mismatch is a common Commander QA failure.

## Single Registry Rule

When `landing-route-registry.json` (or equivalent) **exists** for a project:

| Consumer | Must |
|----------|------|
| ORCA strategy / briefs | Reference `route_id` |
| Website Factory handoff | List `website_factory_page` + `route_id` |
| Triumph / generic exporter | Map ads to `route_id` → `url` from registry |
| Validation CLI | Validate continuity against registry when configured |
| `PROJECT.md` | Link to registry path |

If registry **does not exist**, consumers fall back to handoff docs and blueprints — mark **SAFE UNKNOWN** for route parity.

## Status Alignment

Landing route `status` should align with [ppc-landing-qa-contract-v0.md](ppc-landing-qa-contract-v0.md):

- `approved_for_ads` — passed PPC landing QA; eligible for ad URL assignment
- `approved_for_launch` — human launch gate (see [approval-gates-contract-v0.md](../artifacts/approval-gates-contract-v0.md))

## Example (JSON fragment)

```json
{
  "route_id": "page-01-manipulyator-5-tonn",
  "project_id": "triumph-manipulator-krasnodar",
  "url": "https://example.ru/manipulyator-5-tonn/",
  "slug": "/manipulyator-5-tonn/",
  "page_type": "capability",
  "intent_group": "S-tier-capability-5t",
  "campaign_modes": ["search"],
  "status": "approved_for_ads",
  "source_blueprint": "ppc/triumph-manipulator/landing-pages/01-capability-5t.md",
  "website_factory_page": "workspaces/triumph-manipulator-landing-v4/dist/manipulyator-5-tonn/",
  "ppc_export_usage": "triumph-s-tier-draft-v1:ad-group-5t"
}
```

## SAFE UNKNOWN

- Production domain not finalized
- Staging URL used temporarily
- Display URL path not yet chosen
- RSYA landing differs from Search — separate `route_id` required

## Related Documents

- [orca-website-factory-semantic-lock-v0.md](orca-website-factory-semantic-lock-v0.md)
- [ppc-landing-qa-contract-v0.md](ppc-landing-qa-contract-v0.md)
- [orca-factory-bridge-index-v0.md](orca-factory-bridge-index-v0.md)
- [project-md-contract-v0.md](../projects/project-md-contract-v0.md)

## Boundary

Human-operated registry contract only. No URL monitoring product, no automatic sync with ad platform.

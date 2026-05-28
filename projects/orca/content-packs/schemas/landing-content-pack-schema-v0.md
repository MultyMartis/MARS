# Landing Content Pack Schema v0

## Status

Human-readable schema contract. JSON reference: [content-pack-json-example-v0.json](content-pack-json-example-v0.json).

## Pack envelope

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `pack_id` | string | yes | Stable ID, e.g. `triumph-manipulyator-5-tonn-v0` |
| `pack_version` | string | yes | e.g. `v0.1` |
| `pack_type` | enum | yes | `capability` \| `use_case` \| `b2b` \| `geo` \| `master` |
| `project_ref` | string | yes | e.g. `triumph-manipulator-krasnodar` |
| `route_slug` | string | yes | e.g. `manipulyator-5-tonn` |
| `canonical_url` | string | yes | Production URL target |
| `locale` | string | yes | e.g. `ru-RU` |
| `artifact_state` | enum | yes | See [artifact-lifecycle-v0.md](../artifact-lifecycle-v0.md) |
| `content_mode` | enum | yes | `MODE_1` \| `MODE_2` |
| `semantic_lock` | enum | yes | `inactive` \| `active` |
| `created_at` | ISO date | yes | |
| `updated_at` | ISO date | yes | |
| `author_operator` | string | recommended | Human handle — not AI agent ID as authority |
| `source_artifacts[]` | path[] | recommended | ORCA research / blueprint paths |
| `approval_gates` | object | yes | See below |
| `ppc_continuity` | object | yes | See below |
| `seo_continuity` | object | optional | Title, description, robots default |
| `positioning_locks[]` | string[] | recommended | Global rules (single machine, no fleet, etc.) |
| `safe_unknowns[]` | object[] | optional | `{ field, note }` |
| `sections` | section[] | yes | Ordered 01–10 |

## `approval_gates` object

All booleans — **default false** until human sets:

```yaml
approved_for_factory: false
approved_for_client_export: false
approved_for_ads: false
approved_for_launch: false
```

## `ppc_continuity` object

| Field | Description |
|-------|-------------|
| `campaign_ref` | e.g. `triumph-s-tier-draft-v1` |
| `group_id` | e.g. `grp_fc01_5ton` |
| `group_label` | e.g. `01 — Манипулятор 5 тонн` |
| `display_path` | e.g. `manip-5-tonn` |
| `primary_intents[]` | Target queries |
| `ad_headline_1` | Locked headline |
| `ad_headline_2` | Locked headline |
| `ad_description` | Locked description |
| `callouts[]` | Extension callouts |
| `intent_continuity_rule` | Human-readable continuity check |

## `seo_continuity` object

| Field | Description |
|-------|-------------|
| `document_title` | `<title>` text |
| `meta_description` | |
| `h1` | Must align with hero |
| `robots_default` | e.g. `noindex,nofollow` for PPC landings |

## Markdown pack front-matter (authoring)

```yaml
---
pack_id: example-pack-v0
pack_version: v0.1
artifact_state: draft
content_mode: MODE_2
semantic_lock: inactive
---
```

## Boundary

Schema definition only. No validator implementation in v0.

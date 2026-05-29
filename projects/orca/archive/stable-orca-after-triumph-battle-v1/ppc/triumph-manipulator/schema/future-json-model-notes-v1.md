# Future JSON Model Notes v1

**Status:** Design notes only. **No** `.json` schema files, **no** validators, **no** sample instances in repo for Phase 2.

---

## Why JSON later

| Benefit | Notes |
|---------|-------|
| Machine validation | Phase 3 engine |
| Prompt constraints | Phase 5 — models emit JSON, not Excel |
| Exporter input | Phase 4 — typed graph |
| Diff/review | Git-friendly campaign drafts |

Markdown schemas in this folder remain the **human-readable contract**; JSON Schema is a **derived implementation artifact** in Phase 3+.

---

## Root document shape

```json
{
  "$schema": "https://mars.local/orca/ppc/triumph-manipulator/v1/document",
  "schema_version": "v1",
  "pack_ref": "triumph-manipulator",
  "project_label": "Triumph Krasnodar Search 2026-Q2",
  "meta": {
    "created_by": "human",
    "last_validated_at": null,
    "validation_passed": false
  },
  "campaigns": []
}
```

---

## Suggested file layout (future)

```
triumph-manipulator/
  schema/
    json/
      ppc-document-v1.schema.json      # JSON Schema — Phase 3
      validation-report-v1.schema.json
  instances/                           # gitignored or operator-local
    draft/
      campaign-main-v1.json
```

**Do not** commit production URLs or secrets in instances.

---

## Type mapping summary

| Markdown entity | JSON type | Notes |
|-----------------|-----------|-------|
| `Campaign` | object | `groups` array |
| `Group` | object | embed `keyword_cluster`, `landing_route`, `ad_list` |
| `Ad` | object | |
| `LandingRoute` | object | nested under group |
| `KeywordItem` | object | in `keywords[]` |
| `ValidationReport` | object | separate artifact |

Use `snake_case` field names matching markdown schemas exactly for 1:1 mapping.

---

## IDs and references

```json
{
  "entity_id": "grp_03_bytovka_v1",
  "parent_campaign_id": "camp_triumph_search_main_v1"
}
```

Foreign keys as strings — no UUID requirement in v1.

---

## Enums as JSON Schema

Example fragment (illustrative):

```json
{
  "campaign_type": {
    "type": "string",
    "enum": ["search"]
  },
  "landing_type": {
    "type": "string",
    "enum": ["master_hot", "use_case", "capability", "b2b", "intercity", "fallback"]
  }
}
```

RSYA/retargeting enums **omitted** until chartered.

---

## Validation integration

Phase 3 validator flow:

1. Parse JSON  
2. JSON Schema structural validate (ST-*)  
3. Rule engine for semantic/commercial (SE-*, CM-*, …) from [validation-schema-v1.md](validation-schema-v1.md)  
4. Emit `validation-report-v1.json`  

```json
{
  "schema_version": "v1",
  "validated_at": "2026-05-20T12:00:00Z",
  "passed": false,
  "findings": [
    {
      "id": "SY-01",
      "level": "error",
      "entity_id": "ad_grp03_a1_v1",
      "message": "headline_1 exceeds 56 characters"
    }
  ]
}
```

---

## Exporter integration

```json
{
  "input": "instances/draft/campaign-main-v1.json",
  "validation_report": "instances/draft/campaign-main-v1.validation.json",
  "template": "assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx",
  "output": "out/commander-export-v1.xlsx"
}
```

Exporter CLI **must not** accept unvalidated input when `require_validation: true`.

---

## Prompt system integration (Phase 5)

Prompts should:

- Request **single entity** or **full document** JSON output  
- Include doctrine refs by ID, not full pack dump  
- Forbid raw Excel and forbidden campaign types  

Example system constraint line:

> Output must validate against `ppc-document-v1` and set `search_only_scope: true`.

---

## n8n integration (Phase 6)

Human-triggered nodes only:

- Webhook → validate → notify operator  
- Approved JSON → export → email file  

**No** closed-loop launch.

---

## Versioning policy

| Change | Version bump |
|--------|--------------|
| New optional field | patch doc + optional JSON Schema |
| New required field | `v2` |
| New campaign type (RSYA) | new pack charter + `v2` |

---

## What not to put in JSON

- Governance metadata  
- Autonomous bid strategies  
- Orchestration DAG definitions  
- Fabricated API endpoints  

---

## SAFE UNKNOWN

- Whether to use JSON Schema draft 2020-12 vs OpenAPI fragment — decide in Phase 3.  
- Instance storage: repo vs operator disk vs external DB — operator choice.

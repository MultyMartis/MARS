# JSON Output Contract v1

**Role:** Binding discipline for **all** ORCA Triumph generation and repair prompts.

**Schema authority:** [orca-ppc-document-v1.schema.json](../schema/json/orca-ppc-document-v1.schema.json)  
**Report authority:** [validation-report-v1.schema.json](../schema/json/validation-report-v1.schema.json)

---

## Why JSON-first is critical

| JSON-first | Excel-first (forbidden) |
|------------|-------------------------|
| Single source of truth for intent graph | Rows hide mixed intents |
| Validation runs on structure before export | Errors discovered after import |
| Surgical repair by `entity_id` | Row diff chaos |
| Exporter stays dumb transport | Semantic logic leaks into export |
| Human-readable graph in editor | Formula / column drift |

Excel is **output transport** — [exporter/exporter-engine-overview-v1.md](../exporter/exporter-engine-overview-v1.md). Prompts that emit Excel train **wrong failure mode**.

---

## JSON-only output discipline

### Required behavior

1. **Single artifact per response** — one JSON object or one JSON array of patch ops unless operator requests separate review memo.  
2. **No markdown wrapping** — no ` ```json ` fences in machine-to-machine handoff (operator UI may use fences for readability).  
3. **No trailing commentary** — explanations go in `meta.notes` or separate human message if asked.  
4. **Valid UTF-8** — Cyrillic allowed; no mojibake escapes unless required.  
5. **Parseable** — strict JSON (double quotes, no comments, no trailing commas).

### Forbidden in generation output

- Prose paragraphs outside JSON  
- Excel TSV/CSV  
- “Here is a summary” before/after JSON  
- Mixed JSON + keyword tables in same response  
- Placeholder `...` or `etc.` inside JSON values  

---

## Root document requirements

Every full or merge-target document must include required root keys from schema:

| Field | Value / rule |
|-------|----------------|
| `schema_version` | Literal `"v1"` |
| `project_id` | Stable slug `^[a-z0-9][a-z0-9._-]*$` |
| `project_name` | Human-readable label |
| `market` | e.g. `yandex_direct_ru` |
| `geo` | `primary_region` required |
| `source_pack` | Literal `"triumph-manipulator"` |
| `search_only_scope` | `true` |
| `campaigns` | ≥ 1 campaign |
| `global_negatives` | Object with `keywords[]` |
| `landing_registry` | Entries for blueprints used |
| `validation_policy` | Per schema |
| `export_policy` | Per schema |
| `human_review` | Per schema — human-updated gates |

Reference instance: [schema/instances/triumph-s-tier-draft-v1.json](../schema/instances/triumph-s-tier-draft-v1.json).

---

## Entity ID requirements

| Rule | Detail |
|------|--------|
| Stability | Same entity keeps same `*_id` across repair passes |
| Uniqueness | No duplicate `campaign_id`, `group_id`, `ad_id` in document |
| Traceability | IDs readable by operator (`grp_s01_5ton` not `uuid-random`) |
| Parent linkage | Group references `campaign_id`; ad belongs to one group |
| Platform IDs | **Never** pretend Direct IDs exist pre-import |

---

## Deterministic structure

Prompts should emit keys in **consistent order** for human diff survivability:

```
schema_version → project_* → market → geo → source_pack → search_only_scope
→ campaigns[] (campaign_id → ... → groups[] → keyword_cluster → landing_route → ads[])
→ global_negatives → landing_registry → validation_policy → export_policy → human_review → meta
```

Within `ads[]`: `ad_id` → headlines → description → extensions → alignment → status.

**Arrays:** preserve logical order (tier sort S→A, group numbering).

---

## Fragment vs full document

| Mode | When | Shape |
|------|------|-------|
| **Full document** | Greenfield generation | Complete `OrcaPpcDocument` |
| **Fragment** | Add group, add ad | Object with path hint: `{ "_merge_path": "/campaigns/0/groups", "groups": [ {...} ] }` |
| **Patch** | Validation-fix | RFC6902-style ops array or `entity_replace` convention |

Fragments must still validate when merged — generation prompt must state merge target path.

---

## Validation expectations (post-generation)

Prompt output is **not** export-ready until:

1. Structural checklist or validator reports pass on ST/SY/SE/LM/CM/SV/EX  
2. `ValidationReport` emitted with `export_allowed` per policy  
3. Human review fields updated — [human-review-gates-v1.md](human-review-gates-v1.md)

Prompts must **not** claim `validation_passed: true` without actual validation run.

---

## ValidationReport output (fix / validate sessions)

When prompt assists validation summary (human-operated):

```json
{
  "schema_version": "v1",
  "report_id": "vr_{project_id}_{timestamp}",
  "document_ref": { "project_id": "..." },
  "rule_results": [],
  "export_allowed": false,
  "launch_allowed": false
}
```

`launch_allowed` is **always false** from AI — operator only in Direct.

---

## `draft_status` and human_review

| Field | Who sets |
|-------|----------|
| `ads[].status` | Generation default `draft`; operator may set `active` |
| `human_review.*` | **Human only** — prompts must not auto-approve export |
| `export_policy.approved` | Human after workbook review |

---

## SAFE UNKNOWN in JSON

Use explicit sentinels — not omission:

```json
"final_url": null,
"url_status": "SAFE_UNKNOWN",
"meta": { "notes": "URL pending operator CMS confirmation" }
```

Do not use fake placeholder domains (`example.com`) in export-bound documents.

---

## Contract violations (operator reject response)

Reject AI output if:

- JSON parse fails  
- `schema_version` ≠ `v1`  
- `search_only_scope` ≠ `true`  
- Excel or table keywords appear instead of `keyword_cluster`  
- Entity IDs renamed without approval  
- Prose mixed into JSON payload  

---

## Related docs

- [campaign-generation-prompts-v1.md](campaign-generation-prompts-v1.md)  
- [ad-generation-prompts-v1.md](ad-generation-prompts-v1.md)  
- [validation-fix-prompts-v1.md](validation-fix-prompts-v1.md)  
- [validation/validation-report-generation-v1.md](../validation/validation-report-generation-v1.md)

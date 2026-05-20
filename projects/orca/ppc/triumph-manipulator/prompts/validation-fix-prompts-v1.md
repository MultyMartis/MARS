# Validation-Fix Prompts v1

**Role:** Surgical repair prompts after validation — modify **entities**, not blind full regeneration.

**Input:** `OrcaPpcDocument` + `ValidationReport` per [validation-report-v1.schema.json](../schema/json/validation-report-v1.schema.json).

**Philosophy:** Validation finds defects; fix prompts patch `entity_ref` targets. Exporter does not repair semantics.

---

## Repair vs regenerate

| Situation | Action |
|-----------|--------|
| Single SY overflow on `ad.headline_1` | Fix prompt scoped to that ad field |
| SE intent mixing in one group | Split group OR remove offending keywords — **human approves split** |
| LM landing mismatch | Fix `landing_route` or ad copy — not entire campaign |
| 40+ unrelated FAILs | **STOP** — human architecture review; no mega-regen prompt |

**Default:** JSON Patch-style fragment or single-entity replacement — preserve `entity_id` unless ST rule requires new ID.

---

## Master validation-fix prompt pattern

```
TASK: Surgical ORCA validation repair.

INPUT:
1. OrcaPpcDocument JSON (current)
2. ValidationReport JSON (failures and warnings only)

OUTPUT: JSON only — one of:
- "patch": [ { "op": "replace", "path": "/campaigns/0/groups/1/ads/0/headline_1", "value": "..." } ]
- "entity_replace": { "entity_ref": {...}, "replacement": { ...partial entity... } }

RULES:
1. Address ONLY rule_ids listed in operator message or all status=fail items.
2. Do NOT regenerate unrelated campaigns, groups, or ads.
3. Do NOT change entity_id unless operator approves.
4. Do NOT invent capabilities to fix CM rules — use SAFE UNKNOWN or remove claim.
5. Do NOT convert Excel — document is SoT.
6. For warn-level items: fix only if operator says "fix warns"; else output "acknowledged_warns": [rule_id...].

After patch, list "resolved_rule_ids" and "remaining_unknowns".
```

---

## Fix class: FAIL (blocking)

Must resolve before `export_allowed`.

### ST / structural FAIL

```
rule_ids: ST-03 empty groups, ST-04 broken parent refs
ACTION: Add minimal valid child OR fix parent_id reference.
OUTPUT: smallest graph fragment fixing referential integrity.
Do not add filler keywords to pass ST-03.
```

### SY / symbol FAIL

```
rule_ids: SY-* headline/description/fastlink length
ACTION: Rewrite copy shorter — same intent, same primary phrase if possible.
FORBIDDEN: ellipsis truncation, dropping primary phrase without SE review.
OUTPUT: field-level replacement only.
```

### SE / semantic FAIL

```
rule_ids: SE-* intent mixing, generic phrases, phrase not in headline
ACTION:
- mixing: remove offending keywords OR propose group_split plan (JSON plan only, not auto-split)
- generic: replace with capability/use-case wording from intake
- phrase alignment: rewrite headline_1
OUTPUT: targeted entity fields + optional "operator_decision_required": true for splits.
```

### LM / landing FAIL

```
rule_ids: LM-* mismatch, missing URL
ACTION:
- If URL SAFE UNKNOWN: set human_review.block_export_reason — do not fake URL
- If copy mismatch: align ad to landing_route blueprint family
OUTPUT: landing_route and/or ad alignment fields.
```

### CM / commercial FAIL

```
rule_ids: CM-* untruthful capability, weak CTA
ACTION: Remove or soften unconfirmed claims; strengthen operational wording.
FORBIDDEN: invent specs to pass validation.
```

### SV / survivability FAIL

```
rule_ids: SV-* keyword dump, duplicate semantics
ACTION: prune keywords or merge groups (with operator_decision_required).
Never "fix" by hiding keywords in notes — remove from cluster.
```

### EX / export-mapping FAIL

```
Fix document/export_policy fields only — exporter does not run semantic repair.
See exporter/export-preconditions-v1.md.
```

---

## Fix class: WARN (non-blocking)

```
TASK: Fix WARN <rule_id> on <entity_ref> OR document acknowledgment.

If fixing:
- minimal change; preserve operator-readable names
If acknowledging:
- output { "rule_id": "SV-02", "acknowledged_by": "operator", "reason": "..." }
- do not change entity

Never auto-acknowledge WARNs without operator instruction in prompt.
```

---

## Prompt templates by failure theme

### Alignment repair

```
INPUT: SE failure "phrase not in headline" for entity_ref ad/...
OUTPUT: new headline_1 + alignment.phrase_in_headline: true
Keep description consistent. JSON only.
```

### Generic wording reduction

```
INPUT: CM/SE generic phrase list in report
OUTPUT: replace forbidden phrases using doctrine anti-generic list
Scan only affected text fields in entity_ref scope.
```

### Overflow repair

```
INPUT: SY failure with measured length
OUTPUT: shorter Russian copy, same meaning, under limit
Provide character_count in meta for operator verify.
```

### Landing mismatch repair

```
INPUT: LM failure ad vs landing_route
OUTPUT: either update continuation in description OR flag routing_type change with operator_decision_required
Do not change blueprint without intake confirmation.
```

---

## Repair loop discipline

```
validate → report → fix prompt → merge patch → re-validate
```

| Loop | Policy |
|------|--------|
| Max auto-assisted loops | 3 per session — then human review |
| Same rule_id repeats | STOP — architecture problem |
| Increasing entity count | STOP — anti-chaos violation |

---

## Forbidden repair behaviors

- Full document regen “to be safe”  
- Deleting validation report to bypass export gate  
- Silent truncation of headlines  
- Adding keywords to mask intent mixing  
- Auto-setting `human_review.approved_for_export: true`  
- Launching or calling exporter from fix prompt  

---

## Handoff after repair

1. Re-run validation (human checklist or future CLI)  
2. [human-review-gates-v1.md](human-review-gates-v1.md) before export  
3. Exporter only when `export_allowed` + human approval  

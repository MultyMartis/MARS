# Rule Execution Flow v1

**Role:** How rules are selected, ordered, executed, and aggregated into a `ValidationReport`.  
**Status:** Design contract only — no runtime.

---

## Execution model

The validation engine is a **deterministic, read-only rule runner**:

1. Load `OrcaPpcDocument` (JSON or normalized in-memory graph).  
2. Build entity index (`entity_id` → path in graph).  
3. For each **stage** in fixed order, run all rules in that stage’s registry order.  
4. Collect `rule_result` per rule (and per entity when rule is entity-scoped).  
5. Aggregate to `entity_results`, `blocking_errors`, `warnings`.  
6. Apply export gate policy → `export_allowed`.  
7. Emit `ValidationReport`; **do not** write back to source document.

**Forbidden behaviors:**

- Auto-launch, auto-pause, auto-bid  
- Silent string truncation to satisfy SY limits  
- Rewriting headlines/URLs without human-visible diff  
- Background daemon or scheduled re-validation without operator trigger  

---

## Stage order (fixed)

```
ST (+ NG)  →  SY  →  SE  →  LM  →  CM  →  SV  →  EX
```

Rationale:

| Order | Why |
|-------|-----|
| Structural first | Later rules assume resolvable IDs and required fields |
| Symbol before semantic | Length failures are cheap; avoid semantic work on invalid ads |
| Semantic before landing | Intent labels must exist before route matching |
| Landing before commercial | URL/type coherence before CTA/trust claims |
| Commercial before survivability | Group-level commercial coherence before campaign-scale chaos checks |
| Export mapping last | Mapping assumes document is semantically valid enough to export |

Within a stage, rules run in **numeric ID order** (e.g. SY-01 before SY-02).

---

## Rule invocation shape (logical)

Each rule receives:

| Input | Description |
|-------|-------------|
| `document` | Root PPC document |
| `entity_index` | Lookup for campaigns, groups, ads, routes |
| `rule_def` | Entry from [rule-registry-v1.md](rule-registry-v1.md) |
| `context` | Optional: `ruleset_ref`, `validator_version`, draft vs launch-ready mode |

Each rule returns:

```yaml
rule_id: SY-01
status: pass | fail | warn | not_checked | safe_unknown
severity: error | warn | info
entity_ref: { entity_kind, entity_id, field_path? }
message: human-readable finding
suggested_fix: optional, non-applied text
```

**`not_checked`:** Rule skipped because prerequisite failed (e.g. ad missing `headline_1` — SY-01 not_checked, ST-07 already failed).

---

## Entity-scoped vs document-scoped rules

| Scope | Examples | Execution |
|-------|----------|-----------|
| Document | ST-01, ST-02 | Once per document |
| Campaign | ST-03, NG-01, CM-04, SV-03 | Once per campaign |
| Group | SE-01, LM-02, SE-13 | Once per group |
| Ad | SY-01, SE-05, CM-05 | Once per ad |
| Cross-entity | LM-01, SE-09, NG-02 | Pass full graph or campaign slice |

Cross-entity rules still emit one `rule_result` per **finding** (multiple rows if multiple violations).

---

## Aggregation rules

### Per-entity rollup (`entity_results`)

For each `campaign`, `group`, `ad` touched by any rule:

1. Collect all `rule_results` referencing that `entity_id`.  
2. `entity_result.status` = worst of: `fail` > `warn` > `pass` > `not_checked`.  
3. `rule_ids` = list of rule IDs that fired non-pass on that entity.

### Summary counters (`summary`)

| Field | Meaning |
|-------|---------|
| `total_rules` | Rules attempted (excluding skipped prerequisites) |
| `passed` | `status` = pass |
| `warned` | `status` = warn |
| `failed` | `status` = fail |
| `not_checked` | Prerequisite skip |
| `safe_unknown_count` | `status` = safe_unknown |

### `validation_status` (document level)

| Condition | `validation_status` |
|-----------|---------------------|
| Any `fail` on severity `error` | `failed` |
| No errors, ≥1 warn or safe_unknown | `passed_with_warnings` |
| All executed rules pass | `passed` |
| Intake aborted (invalid JSON / missing root) | `incomplete` |

### `blocking_errors` and `warnings`

- `blocking_errors[]` ← all `rule_results` where `severity` = `error` and `status` = `fail`  
- `warnings[]` ← all where `severity` = `warn` and `status` in (`warn`, `fail` if warn-severity fail)

---

## Export gate (within execution flow)

After aggregation:

```
export_allowed =
  (validation_status != failed)
  AND (validation_status != incomplete)
  AND (blocking_errors is empty)
  AND NOT policy_block
```

`policy_block` examples (human-configurable in future):

- Document marked `draft_only`  
- `human_review_required` = true and no `operator_signoff` record (**future field**)  
- Any `safe_unknown` without explicit human clearance (default strict)

**Excel export** must check `export_allowed` before invoking exporter. Exporter does not re-run semantic rules.

---

## Human review hook (post-report)

```
ValidationReport emitted
    → operator reads blocking_errors / warnings
    → fixes document OR documents override for warns
    → re-run validation (recommended) OR sign off with notes
    → export if export_allowed
    → import Commander
    → launch_allowed set ONLY by human (see validation-report-generation-v1.md)
```

Re-validation is **operator-triggered**, not scheduled.

---

## Launch-ready mode (optional future flag)

When validating a document intended for launch (not draft exploration):

- Treat ST-10 (`intent_continuity_ack`) as **error** if false.  
- Treat SE-05/06 as **error** if `phrase_in_headline_1` / `phrase_in_description` false.  
- Treat CM-05 as **error** if mobile flags false.

Default validation mode for drafts: same rules, but operator may ignore non-blocking warns until promotion to launch-ready.

---

## Performance notes (for future implementation)

- Symbol checks: O(ads × fields) — run early, cache string lengths.  
- Duplicate H1 (SE-08/09): O(ads) hash per group/campaign — single pass after all ads loaded.  
- Landing rules: O(groups) with blueprint lookup table from [landing-pages/INDEX.md](../landing-pages/INDEX.md).

No requirement for parallel execution in v1; determinism beats speed.

---

## Related

- [validation-engine-overview-v1.md](validation-engine-overview-v1.md)  
- [validation-report-generation-v1.md](validation-report-generation-v1.md)  
- [rule-registry-v1.md](rule-registry-v1.md)

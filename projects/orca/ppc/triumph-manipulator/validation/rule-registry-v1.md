# Rule Registry v1

**Role:** Canonical catalog of validation rule IDs for Triumph Manipulator PPC v1.  
**Execution order:** [rule-execution-flow-v1.md](rule-execution-flow-v1.md)  
**Detail expansions:** symbol · semantic · landing · commercial · survivability docs in this folder.

**Prefix → class mapping:**

| Prefix | `rule_class` | Doc |
|--------|--------------|-----|
| ST-*, NG-* | structural | this file |
| SY-* | symbol | [symbol-validation-rules-v1.md](symbol-validation-rules-v1.md) |
| SE-* | semantic | [semantic-validation-rules-v1.md](semantic-validation-rules-v1.md) |
| LM-* | landing_mismatch | [landing-continuity-rules-v1.md](landing-continuity-rules-v1.md) |
| CM-* | commercial | [commercial-validation-rules-v1.md](commercial-validation-rules-v1.md) |
| SV-* | survivability | [survivability-validation-rules-v1.md](survivability-validation-rules-v1.md) |
| EX-* | export_mapping | this file (EX section) |

---

## Structural rules (ST-*)

### ST-01

| | |
|--|--|
| **rule_id** | ST-01 |
| **title** | Schema version v1 |
| **severity** | error |
| **target_entity** | document |
| **purpose** | Ensure validator and document share contract version |
| **failure_examples** | `schema_version: "v0"` or missing |
| **validation_logic_summary** | Root `schema_version` = `v1` |
| **recommended_operator_action** | Migrate document to v1 or fix typo |

### ST-02

| | |
|--|--|
| **rule_id** | ST-02 |
| **title** | Search-only scope enforced |
| **severity** | error |
| **target_entity** | document, campaign |
| **purpose** | Pack v1 is Yandex Search only |
| **failure_examples** | `search_only_scope: false`; RSYA campaign type |
| **validation_logic_summary** | Document and every campaign `search_only_scope` = true |
| **recommended_operator_action** | Remove non-search fields or split to future pack |

### ST-03

| | |
|--|--|
| **rule_id** | ST-03 |
| **title** | Campaign has at least one group |
| **severity** | error |
| **target_entity** | campaign |
| **purpose** | Non-empty campaign graph |
| **failure_examples** | `groups: []` |
| **validation_logic_summary** | `len(campaign.groups)` ≥ 1 |
| **recommended_operator_action** | Add group or remove empty campaign |

### ST-04

| | |
|--|--|
| **rule_id** | ST-04 |
| **title** | Group has at least one keyword |
| **severity** | error |
| **target_entity** | group |
| **purpose** | No empty ad groups |
| **failure_examples** | `keyword_cluster.keywords: []` |
| **validation_logic_summary** | ≥1 keyword in cluster |
| **recommended_operator_action** | Add keywords or pause group |

### ST-05

| | |
|--|--|
| **rule_id** | ST-05 |
| **title** | Group has at least one ad |
| **severity** | error |
| **target_entity** | group |
| **purpose** | No keyword-only groups for export |
| **failure_examples** | `ads: []` |
| **validation_logic_summary** | ≥1 ad in group |
| **recommended_operator_action** | Create ad from blueprint |

### ST-06

| | |
|--|--|
| **rule_id** | ST-06 |
| **title** | Parent references resolve |
| **severity** | error |
| **target_entity** | document |
| **purpose** | Referential integrity |
| **failure_examples** | `parent_group_id` points to missing group |
| **validation_logic_summary** | All FK ids exist in entity_index |
| **recommended_operator_action** | Fix ids or regenerate graph |

### ST-07

| | |
|--|--|
| **rule_id** | ST-07 |
| **title** | Required fields per entity schemas |
| **severity** | error |
| **target_entity** | campaign, group, ad |
| **purpose** | JSON Schema / markdown required fields present |
| **failure_examples** | Missing `landing_route`, `cta_semantics` |
| **validation_logic_summary** | Check against entity schema required tables |
| **recommended_operator_action** | Complete entity per schema docs |

### ST-08

| | |
|--|--|
| **rule_id** | ST-08 |
| **title** | Use-case classification when landing_type use_case |
| **severity** | error |
| **target_entity** | group |
| **purpose** | Routing schema coherence |
| **failure_examples** | `landing_type: use_case` without `use_case_classification` |
| **validation_logic_summary** | Iff use_case → classification set |
| **recommended_operator_action** | Set classification from landing-pages INDEX |

### ST-09

| | |
|--|--|
| **rule_id** | ST-09 |
| **title** | Capability classification when capability intent |
| **severity** | error |
| **target_entity** | group |
| **purpose** | Capability routing coherence |
| **failure_examples** | `intent_type: capability_exact` without capability class |
| **validation_logic_summary** | Iff capability intent → `capability_classification` set |
| **recommended_operator_action** | Set tonnage/class per blueprint |

### ST-10

| | |
|--|--|
| **rule_id** | ST-10 |
| **title** | Intent continuity ack (launch-ready) |
| **severity** | error |
| **target_entity** | group |
| **purpose** | Human confirmed landing continuity |
| **failure_examples** | `intent_continuity_ack: false` on export path |
| **validation_logic_summary** | Launch-ready groups require ack true |
| **recommended_operator_action** | Review blueprint; set ack |

### ST-11

| | |
|--|--|
| **rule_id** | ST-11 |
| **title** | No orphan ads or duplicate entity_id |
| **severity** | error |
| **target_entity** | document |
| **purpose** | Graph uniqueness |
| **failure_examples** | Duplicate `ad_id`; ad without parent group |
| **validation_logic_summary** | Global unique `entity_id`; every ad in exactly one group |
| **recommended_operator_action** | Regenerate ids; fix tree |

---

## Structural — negative keyword rules (NG-*)

### NG-01

| | |
|--|--|
| **rule_id** | NG-01 |
| **title** | Campaign global negatives include core blockers |
| **severity** | warn |
| **target_entity** | campaign |
| **purpose** | Junk traffic prevention |
| **failure_examples** | Missing вакансии, эвакуатор, купить |
| **validation_logic_summary** | Warn if core blocklist not subset of campaign_negatives |
| **recommended_operator_action** | Copy from triumph-s-tier-draft campaign_negatives |

### NG-02

| | |
|--|--|
| **rule_id** | NG-02 |
| **title** | Group negatives do not negate own intent |
| **severity** | error |
| **target_entity** | group |
| **purpose** | Prevent self-blocking |
| **failure_examples** | Group «5 тонн» with negative `5 тонн` |
| **validation_logic_summary** | Negative phrases must not match primary keyword stems |
| **recommended_operator_action** | Remove conflicting negative |

### NG-03

| | |
|--|--|
| **rule_id** | NG-03 |
| **title** | Campaign vs group negative conflicts documented |
| **severity** | info |
| **target_entity** | campaign, group |
| **purpose** | Traceability for operator |
| **failure_examples** | Overlapping negatives with different match types |
| **validation_logic_summary** | Info when campaign negative duplicates group negative |
| **recommended_operator_action** | Document in notes if intentional |

---

## Symbol rules (SY-*)

| rule_id | title | severity | target_entity |
|---------|-------|----------|---------------|
| SY-01 | Headline 1 ≤ 56 (spaces included) | error | ad |
| SY-02 | Headline 2 ≤ 30 if present | error | ad |
| SY-03 | Description ≤ 81 | error | ad |
| SY-04 | Fastlink title ≤ 30 | error | ad |
| SY-05 | Callout ≤ 25 | error | ad |
| SY-06 | Display URL path ≤ 20 per segment | error | ad |
| SY-07 | Truncation risk near limit | warn | ad |
| SY-08 | Excessive punctuation | warn | ad |
| SY-09 | Whitespace hygiene | warn | ad |
| SY-10 | Required text fields non-empty | error | ad |
| SY-11 | Extension counts within max | error | ad |
| SY-12 | Display domain vs landing host | warn | ad |

Full entries: [symbol-validation-rules-v1.md](symbol-validation-rules-v1.md).

---

## Semantic rules (SE-*)

| rule_id | title | severity | target_entity |
|---------|-------|----------|---------------|
| SE-01 | Single intent per group | error | group |
| SE-02 | Cross-intent risk not high | error | group |
| SE-03 | No employment/wrong-service keywords | error | group |
| SE-04 | No tier-X junk in launch | error | group |
| SE-05 | Phrase in headline 1 | error | ad |
| SE-06 | Phrase in description | error | ad |
| SE-07 | Anti-generic headline | error | ad |
| SE-08 | Duplicate H1 in group | warn | group |
| SE-09 | Duplicate H1 in campaign | warn | campaign |
| SE-10 | No generic SEO description | error | ad |
| SE-11 | No decorative fastlinks | error | ad |
| SE-12 | Primary keyword in cluster | error | ad, group |
| SE-13 | Keyword cluster size threshold | warn | group |
| SE-14 | Broad match without negatives | warn | group, campaign |
| SE-15 | Mixed intent in group | error | group |
| SE-16 | Weak CTA detection | warn | ad |

Full entries: [semantic-validation-rules-v1.md](semantic-validation-rules-v1.md).

---

## Landing mismatch rules (LM-*)

| rule_id | title | severity | target_entity |
|---------|-------|----------|---------------|
| LM-01 | Ad URL = group final URL | error | ad, group |
| LM-02 | landing_type matches classifications | error | group |
| LM-03 | Use-case vs capability mismatch | error | group, ad |
| LM-04 | B2B language needs B2B route | error | group, ad |
| LM-05 | Intercity promise needs intercity route | error | group, ad |
| LM-06 | Master fallback justified | **warn** | group |
| LM-07 | Capability claims vs blueprint | error | group, ad |
| LM-08 | Intent continuity ack | error | group |
| LM-09 | Fastlink URL continuity | warn | ad |

Full entries: [landing-continuity-rules-v1.md](landing-continuity-rules-v1.md).

---

## Commercial rules (CM-*)

| rule_id | title | severity | target_entity |
|---------|-------|----------|---------------|
| CM-01 | CTA fits intent tier | warn | ad |
| CM-02 | Capability truthfulness | error | ad |
| CM-03 | Trust line consistency | warn | ad, campaign |
| CM-04 | Geo consistency | warn | ad, campaign |
| CM-05 | Mobile readability flags | error | ad |
| CM-06 | No impossible promises | warn | ad |
| CM-07 | Search intent continuation | error | ad |
| CM-08 | Operational clarity | warn | ad |
| CM-09 | Payment claims match route | warn | ad |

Full entries: [commercial-validation-rules-v1.md](commercial-validation-rules-v1.md).

---

## Survivability rules (SV-*)

| rule_id | title | severity | target_entity |
|---------|-------|----------|---------------|
| SV-01 | Group count proportionate | warn | campaign |
| SV-02 | Human-readable names | warn | campaign, group |
| SV-03 | Mixed container justified | warn | campaign |
| SV-04 | Near-duplicate ad overload | warn | group |
| SV-05 | Export approval marker | info | document |
| SV-06 | Human review mandatory | error | document |
| SV-07 | No giant garbage groups | error | group |
| SV-08 | Draft vs active discipline | warn | group |
| SV-09 | Campaign negatives for launch | warn | campaign |

Full entries: [survivability-validation-rules-v1.md](survivability-validation-rules-v1.md).

---

## Export mapping rules (EX-*)

### EX-01

| | |
|--|--|
| **rule_id** | EX-01 |
| **title** | Validation report required before export |
| **severity** | error |
| **target_entity** | document |
| **purpose** | Enforce validate-before-export pipeline |
| **failure_examples** | Exporter invoked without `ValidationReport` |
| **validation_logic_summary** | Export step must reference report with `export_allowed: true` |
| **recommended_operator_action** | Run validation; fix blocking errors |

### EX-02

| | |
|--|--|
| **rule_id** | EX-02 |
| **title** | Internal-only fields not exported as primary columns |
| **severity** | error |
| **target_entity** | document |
| **purpose** | Dumb exporter — no semantic columns in Commander sheet |
| **failure_examples** | `semantic_intent` mapped to Campaign name |
| **validation_logic_summary** | Cross-check mapping table: internal fields → no export column |
| **recommended_operator_action** | Use Notes column only if operator opts in |

### EX-03

| | |
|--|--|
| **rule_id** | EX-03 |
| **title** | Required Commander columns mappable |
| **severity** | error |
| **target_entity** | campaign, group, ad |
| **purpose** | Prevent partial import |
| **failure_examples** | Missing `campaign_name`, `headline_1` for active ad row |
| **validation_logic_summary** | Every required export-mapping row has non-empty source |
| **recommended_operator_action** | Fill required fields per export-mapping-schema |

### EX-04

| | |
|--|--|
| **rule_id** | EX-04 |
| **title** | Active ads have landing URL for export |
| **severity** | error |
| **target_entity** | ad |
| **purpose** | Commander rows must click through |
| **failure_examples** | Active ad with empty `landing_url` |
| **validation_logic_summary** | For ads with `status: active`, `landing_url` non-empty valid URL |
| **recommended_operator_action** | Set URL from group route |

### EX-05

| | |
|--|--|
| **rule_id** | EX-05 |
| **title** | Match type and keyword fields exportable |
| **severity** | error |
| **target_entity** | group |
| **purpose** | Keyword sheet completeness |
| **failure_examples** | Keyword missing `phrase` or invalid `match_policy` |
| **validation_logic_summary** | Each active keyword has phrase + allowed match_policy enum |
| **recommended_operator_action** | Fix keyword_cluster rows |

### EX-06

| | |
|--|--|
| **rule_id** | EX-06 |
| **title** | Draft ads excluded or explicitly flagged |
| **severity** | warn |
| **target_entity** | ad |
| **purpose** | Avoid accidental export of drafts |
| **failure_examples** | All ads `draft` but export-ready flag set |
| **validation_logic_summary** | Warn if export-ready campaign has zero active ads |
| **recommended_operator_action** | Activate ads or demote campaign to draft |

---

## Ruleset versioning

| Field | Value |
|-------|-------|
| **ruleset_ref** | `triumph-manipulator-validation-v1` |
| **Aligned schema** | [validation-schema-v1.md](../schema/validation-schema-v1.md) |
| **Report contract** | [validation-report-v1.schema.json](../schema/json/validation-report-v1.schema.json) |

When rules change, bump ruleset_ref and regenerate golden reports (future).

---

## Count summary

| Class | Count |
|-------|-------|
| ST | 11 |
| NG | 3 |
| SY | 12 |
| SE | 16 |
| LM | 9 |
| CM | 9 |
| SV | 9 |
| EX | 6 |
| **Total** | **75** |

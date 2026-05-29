# Survivability Validation Rules v1 (SV-*)

**Class:** `survivability`  
**Goal:** Keep PPC structure **human-operable** in production — quality over quantity, anti-chaos, mandatory human review.

Doctrine alignment: [generation-logic-v0.md](../doctrine/generation-logic-v0.md) · ORCA survivability-first posture.

---

## Survivability principles

| Principle | Rule enforcement |
|-----------|------------------|
| Quality > quantity | Warn on oversized keyword dumps (see SE-13) |
| Human-readable naming | Group/campaign names must explain intent |
| Anti-chaos structure | No micro-spam groups; no duplicate-heavy ad sets |
| No broad semantic dumps | One intent per group (SE-01, SE-15) |
| Human review mandatory | SV-06 — export does not replace review |

---

## SV-01 — Group count proportionate

| Field | Value |
|-------|-------|
| **rule_id** | SV-01 |
| **title** | Group count proportionate to intent map |
| **severity** | warn |
| **target_entity** | campaign |
| **purpose** | Avoid micro-spam or single giant bucket |
| **failure_examples** | 80 groups for 8 intents; 1 group for entire S-tier map |
| **validation_logic_summary** | Compare `len(groups)` to intent map cardinality; warn if ratio >3x or <0.5x without `mixed_container` note |
| **recommended_operator_action** | Merge duplicates or split per intent-groups |

---

## SV-02 — Human-readable names

| Field | Value |
|-------|-------|
| **rule_id** | SV-02 |
| **title** | Group and campaign names human-readable |
| **severity** | warn |
| **target_entity** | campaign, group |
| **purpose** | Operator can navigate Commander without ORCA |
| **failure_examples** | `group_12`, `test`, `новая группа 2` |
| **validation_logic_summary** | Warn if name matches `/^(group_|ad_|test|новая)/i` or length <5 without tier prefix |
| **recommended_operator_action** | Use pattern `01 — Манипулятор 5 тонн` from draft fixture |

---

## SV-03 — Mixed container justification

| Field | Value |
|-------|-------|
| **rule_id** | SV-03 |
| **title** | Mixed container campaign documented |
| **severity** | warn |
| **target_entity** | campaign |
| **purpose** | `mixed_container` is allowed but must be conscious |
| **failure_examples** | `intent_classification: mixed_container` with no `routing_notes` |
| **validation_logic_summary** | Warn if mixed_container and empty campaign-level split justification |
| **recommended_operator_action** | Add notes or split campaigns by tier |

---

## SV-04 — Near-duplicate ad overload

| Field | Value |
|-------|-------|
| **rule_id** | SV-04 |
| **title** | No excessive near-duplicate ads per group |
| **severity** | warn |
| **target_entity** | group |
| **purpose** | >5 ads with minimal variation creates noise |
| **failure_examples** | 8 ads, same H1, minor word swaps |
| **validation_logic_summary** | Warn if `len(ads)` >5 AND >60% ads share normalized H1 |
| **recommended_operator_action** | Keep 2–3 distinct angles max per group |

---

## SV-05 — Export approval marker (future)

| Field | Value |
|-------|-------|
| **rule_id** | SV-05 |
| **title** | Human export approval when required |
| **severity** | info |
| **target_entity** | document |
| **purpose** | Remind operator of approval discipline |
| **failure_examples** | Future: `approved_for_export` false on launch run |
| **validation_logic_summary** | Info if field present and false; not_checked if field absent |
| **recommended_operator_action** | Set approval after review checklist |

---

## SV-06 — Human review mandatory

| Field | Value |
|-------|-------|
| **rule_id** | SV-06 |
| **title** | Human review required before treat-as-launch-ready |
| **severity** | error |
| **target_entity** | document |
| **purpose** | Validation never implies launch approval |
| **failure_examples** | Interpreting `export_allowed` as launch OK |
| **validation_logic_summary** | On launch-ready validation mode: require `human_review_required` flow completed (operator sign-off record — future field); always set `human_review_required` true when any warn |
| **recommended_operator_action** | Complete review checklist; never auto-launch |

---

## SV-07 — No giant garbage groups

| Field | Value |
|-------|-------|
| **rule_id** | SV-07 |
| **title** | Reject broad semantic dump groups |
| **severity** | error |
| **target_entity** | group |
| **purpose** | Block «аренда манипулятора» catch-all launch groups |
| **failure_examples** | Group with 30+ unrelated keywords and `intent_tier: S` |
| **validation_logic_summary** | Fail if keyword entropy high AND `intent_type` vague AND tier S/A |
| **recommended_operator_action** | Move to B or X; segment per intent-groups |

---

## SV-08 — Draft vs active discipline

| Field | Value |
|-------|-------|
| **rule_id** | SV-08 |
| **title** | Draft ads excluded from export validation pass |
| **severity** | warn |
| **target_entity** | group |
| **purpose** | Only validate active rows for export gate |
| **failure_examples** | Export includes `status: draft` ads with symbol errors |
| **validation_logic_summary** | Warn if any draft ad has errors when campaign marked export-ready |
| **recommended_operator_action** | Fix or exclude drafts before export |

---

## SV-09 — Anti-chaos campaign negatives

| Field | Value |
|-------|-------|
| **rule_id** | SV-09 |
| **title** | Campaign negatives present for launch |
| **severity** | warn |
| **target_entity** | campaign |
| **purpose** | Align with NG-01 survivability |
| **failure_examples** | Empty `campaign_negatives` on launch campaign |
| **validation_logic_summary** | Warn if core junk blockers missing (вакансии, купить, эвакуатор…) |
| **recommended_operator_action** | Copy blocklist from draft fixture campaign_negatives |

---

## Registry cross-reference

[rule-registry-v1.md](rule-registry-v1.md) · Negative rules NG-* in structural stage

# Landing Continuity Rules v1 (LM-*)

**Class:** `landing_mismatch`  
**Goal:** Ad promise must continue on landing page — correct blueprint family, URL coherence, honest fallback.

Blueprints: [landing-pages/INDEX.md](../landing-pages/INDEX.md) · routing: [landing-routing-schema-v1.md](../schema/landing-routing-schema-v1.md).

---

## Continuity doctrine

| Principle | Enforcement |
|-----------|-------------|
| Ad ↔ landing | User clicks expecting the **same task** they searched |
| Blueprint family | use_case / capability / b2b / intercity / master — no silent swap |
| Master fallback | **WARN** unless `fallback_reason` documents justification |
| Capability truth | Ad tonnage/boom must match blueprint class |

---

## LM-01 — Ad URL matches group route

| Field | Value |
|-------|-------|
| **rule_id** | LM-01 |
| **title** | Ad landing URL equals group final URL |
| **severity** | error |
| **target_entity** | ad + group (`landing_route`) |
| **purpose** | Single canonical URL per group unless override documented |
| **failure_examples** | Ad points to `/bytovka` while group route is `/manipulyator-5t` |
| **validation_logic_summary** | `ad.landing_url` = `group.landing_route.final_url` OR `landing_override` with reason in notes |
| **recommended_operator_action** | Align ad URL to group route or document override |

---

## LM-02 — Landing type matches classifications

| Field | Value |
|-------|-------|
| **rule_id** | LM-02 |
| **title** | landing_type matches group intent classifications |
| **severity** | error |
| **target_entity** | group (`landing_route`) |
| **purpose** | Schema coherence for routing rules |
| **failure_examples** | `intent_type: capability_exact` with `landing_type: use_case` without use_case classification |
| **validation_logic_summary** | Map `intent_type` → expected `landing_type`; verify `use_case_classification` / `capability_classification` per landing-routing-schema |
| **recommended_operator_action** | Fix `landing_route` or intent fields |

---

## LM-03 — Use-case vs capability mismatch

| Field | Value |
|-------|-------|
| **rule_id** | LM-03 |
| **title** | No use-case ad on capability-only page (or reverse) |
| **severity** | error |
| **target_entity** | group + ad |
| **purpose** | Prevent intent whiplash on landing |
| **failure_examples** | Ad «Перевозка бытовок» → capability 5t blueprint URL |
| **validation_logic_summary** | Compare ad semantic signals (H1, primary keyword) to `blueprint_id` family |
| **recommended_operator_action** | Assign blueprint from INDEX; rewrite ad or URL |

---

## LM-04 — B2B language without B2B route

| Field | Value |
|-------|-------|
| **rule_id** | LM-04 |
| **title** | B2B ad language requires B2B route |
| **severity** | error |
| **target_entity** | group + ad |
| **purpose** | Юрлица / безнал promises need B2B blueprint |
| **failure_examples** | «Безнал для юрлиц» in H1, route to generic master |
| **validation_logic_summary** | If ad or group has `b2b` signals → `landing_type` = b2b or blueprint `06-b2b-yurlica` |
| **recommended_operator_action** | Route to [06-b2b-yurlica.md](../landing-pages/06-b2b-yurlica.md) or remove B2B claim |

---

## LM-05 — Intercity promise without intercity route

| Field | Value |
|-------|-------|
| **rule_id** | LM-05 |
| **title** | Intercity promise requires intercity route |
| **severity** | error |
| **target_entity** | group + ad |
| **purpose** | Geo expansion honesty |
| **failure_examples** | «По краю и соседним городам» with Krasnodar-only URL |
| **validation_logic_summary** | Intercity phrases in copy → `landing_type: intercity` or blueprint `08-intercity-krai` |
| **recommended_operator_action** | Add intercity group or remove geo promise |

---

## LM-06 — Master fallback without justification

| Field | Value |
|-------|-------|
| **rule_id** | LM-06 |
| **title** | Master landing fallback must be justified |
| **severity** | warn |
| **target_entity** | group (`landing_route`) |
| **purpose** | Discourage lazy routing of exact-fit intents to master |
| **failure_examples** | S-tier capability group routed to `01-master-hot-general` with `fallback_allowed: true` and empty `fallback_reason` |
| **validation_logic_summary** | If `blueprint_id` = master OR `fallback_allowed` on specific intent → require non-empty `fallback_reason` / `routing_notes`; else **warn** |
| **recommended_operator_action** | Assign exact blueprint OR document why master is intentional (e.g. page not built yet) |

**Policy:** Fallback to master landing = **WARN** unless explicitly justified — not silent pass.

---

## LM-07 — Capability claims vs blueprint

| Field | Value |
|-------|-------|
| **rule_id** | LM-07 |
| **title** | Capability claims supported by blueprint class |
| **severity** | error |
| **target_entity** | ad + group |
| **purpose** | Ad must not promise tonnage/boom page cannot support |
| **failure_examples** | «6×6 вездеход» ad → 5t blueprint; «10 т» in callouts for 5t route |
| **validation_logic_summary** | Extract tonnage/boom from callouts/H1; match blueprint capability table |
| **recommended_operator_action** | Fix callouts or change blueprint |

---

## LM-08 — Intent continuity acknowledgment

| Field | Value |
|-------|-------|
| **rule_id** | LM-08 |
| **title** | Intent continuity ack for launch-ready groups |
| **severity** | error |
| **target_entity** | group (`landing_route.intent_continuity_ack`) |
| **purpose** | Operator confirms landing reviewed against ad |
| **failure_examples** | `intent_continuity_ack: false` on export-ready group (see draft fixture) |
| **validation_logic_summary** | Launch-ready: `intent_continuity_ack` = true |
| **recommended_operator_action** | Open blueprint checklist; set ack after visual review |

---

## LM-09 — Fastlink URL continuity

| Field | Value |
|-------|-------|
| **rule_id** | LM-09 |
| **title** | Fastlink URLs must not contradict primary intent |
| **severity** | warn |
| **target_entity** | ad (`fastlinks`) |
| **purpose** | Extensions are sub-intents, not random site areas |
| **failure_examples** | Primary 5t ad with fastlink only to unrelated service without `intent_role` note |
| **validation_logic_summary** | Warn if fastlink host/path intent family ≠ group intent and no `intent_role` |
| **recommended_operator_action** | Add `intent_role` or remove misleading fastlink |

---

## Registry cross-reference

[rule-registry-v1.md](rule-registry-v1.md)

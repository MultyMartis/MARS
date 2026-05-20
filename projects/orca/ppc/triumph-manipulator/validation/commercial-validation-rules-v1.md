# Commercial Validation Rules v1 (CM-*)

**Class:** `commercial`  
**Goal:** CTA clarity, honest capability/trust claims, mobile readability, search-intent continuation for Triumph manipulator service (Krasnodar).

---

## Commercial principles

| Principle | Validation focus |
|-----------|------------------|
| CTA clarity | User knows what happens next (call, calculate, order) |
| Capability truthfulness | Tonnage, boom, 6×6 claims match Triumph line |
| Practical trust | No impossible 24/7 / «лидер» without proof |
| Mobile readability | Short lines, scannable description |
| Operational clarity | Geo, payment (безнал), response path honest |
| Search intent continuation | Commercial promise matches query task |

---

## CM-01 — CTA fits intent tier

| Field | Value |
|-------|-------|
| **rule_id** | CM-01 |
| **title** | CTA semantics fit intent tier |
| **severity** | warn |
| **target_entity** | ad (`cta_semantics`) |
| **purpose** | B2B → calculate/call; hot capability → call; avoid hype |
| **failure_examples** | B2B group with `urgency_level: high` and «Заказать со скидкой» |
| **validation_logic_summary** | Map `intent_tier` + `intent_type` → allowed `primary_cta` set; warn on mismatch |
| **recommended_operator_action** | Set `call` or `calculate` per blueprint CTA |

---

## CM-02 — Capability truthfulness

| Field | Value |
|-------|-------|
| **rule_id** | CM-02 |
| **title** | Tonnage and boom claims plausible for Triumph |
| **severity** | error |
| **target_entity** | ad (callouts, H1, description) |
| **purpose** | Prevent false equipment promises |
| **failure_examples** | «Манипулятор 10 т» on 5t campaign; «стрела 25 м» when blueprint says 14 m |
| **validation_logic_summary** | Compare numeric claims to blueprint + doctrine machine line |
| **recommended_operator_action** | Correct numbers or change group to matching capability |

---

## CM-03 — Trust line consistency

| Field | Value |
|-------|-------|
| **rule_id** | CM-03 |
| **title** | Trust claims not self-contradictory |
| **severity** | warn |
| **target_entity** | ad + campaign |
| **purpose** | «Без посредников» and similar must be consistent |
| **failure_examples** | «Без посредников» in ad, «работаем через партнёров» in another ad same campaign |
| **validation_logic_summary** | Flag opposing trust phrases in same campaign |
| **recommended_operator_action** | Unify trust messaging per doctrine |

---

## CM-04 — Geo mention consistency

| Field | Value |
|-------|-------|
| **rule_id** | CM-04 |
| **title** | Geo in copy matches campaign geo |
| **severity** | warn |
| **target_entity** | ad + campaign |
| **purpose** | Avoid misleading geo targeting |
| **failure_examples** | Campaign geo Krasnodar, H1 «в Москве» |
| **validation_logic_summary** | Extract geo tokens from H1/H2; compare to `campaign.geo.primary_region` |
| **recommended_operator_action** | Fix copy or split intercity campaign |

---

## CM-05 — Mobile readability flags

| Field | Value |
|-------|-------|
| **rule_id** | CM-05 |
| **title** | Mobile-first readability confirmed (launch-ready) |
| **severity** | error |
| **target_entity** | ad (`mobile_first_readability`) |
| **purpose** | Enforce mobile SERP scannability |
| **failure_examples** | `h1_line_break_ok: false`; stuffed keywords; `estimated_mobile_grade: poor` |
| **validation_logic_summary** | Launch-ready: all required mobile flags true per ad-entity-schema |
| **recommended_operator_action** | Shorten H1 lines; fix description scan pattern |

---

## CM-06 — Practical trust — no impossible promises

| Field | Value |
|-------|-------|
| **rule_id** | CM-06 |
| **title** | No impossible operational promises |
| **severity** | warn |
| **target_entity** | ad |
| **purpose** | Survivability and brand trust |
| **failure_examples** | «24/7 без выходных» if not operationally true; «за 15 минут» without basis |
| **validation_logic_summary** | Match against promise blocklist unless `notes` documents truth |
| **recommended_operator_action** | Soften to verifiable wording («в день обращения») |

---

## CM-07 — Search intent continuation

| Field | Value |
|-------|-------|
| **rule_id** | CM-07 |
| **title** | Commercial copy continues search task |
| **severity** | error |
| **target_entity** | ad |
| **purpose** | User searching «манипулятор 5 тонн» must see rental/delivery task, not brand essay |
| **failure_examples** | Description only about company history; no task verb (заказать, подача, перевозка) |
| **validation_logic_summary** | Require task verb + intent noun in description for launch-ready |
| **recommended_operator_action** | Add task continuation: подача, перевозка, установка, расчёт |

---

## CM-08 — Operational clarity (contact path)

| Field | Value |
|-------|-------|
| **rule_id** | CM-08 |
| **title** | Operational next step clear |
| **severity** | warn |
| **target_entity** | ad (`cta_semantics`) |
| **purpose** | Mobile user knows how to convert |
| **failure_examples** | `primary_cta: call` but no phone path in doctrine notes and vague «Свяжитесь» |
| **validation_logic_summary** | Warn if CTA type set but `cta_phrase` empty or non-action |
| **recommended_operator_action** | Use «Позвонить», «Рассчитать стоимость» |

---

## CM-09 — Payment / B2B commercial honesty

| Field | Value |
|-------|-------|
| **rule_id** | CM-09 |
| **title** | Payment claims match route |
| **severity** | warn |
| **target_entity** | ad |
| **purpose** | Безнал / юрлица only when B2B path exists |
| **failure_examples** | «Безнал для юрлиц» on consumer-only landing |
| **validation_logic_summary** | Payment phrases require B2B blueprint or fastlink to B2B |
| **recommended_operator_action** | Add B2B route or remove payment claim |

---

## Registry cross-reference

[rule-registry-v1.md](rule-registry-v1.md)

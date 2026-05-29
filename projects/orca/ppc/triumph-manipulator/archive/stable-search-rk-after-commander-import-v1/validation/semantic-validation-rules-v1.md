# Semantic Validation Rules v1 (SE-*)

**Class:** `semantic`  
**Goal:** Intent purity, Yandex relevance behavior, anti-garbage — **no SEO-style fluff.**

Doctrine: [generation-logic-v0.md](../doctrine/generation-logic-v0.md), tiers: [intent-groups-v1.md](../research/intent-groups-v1.md).

---

## Anti-garbage doctrine (explicit)

**Forbidden patterns:**

- SEO fluff: «лучшие цены», «качественные услуги», «лидер рынка», «профессиональные услуги» without task anchor  
- Generic containers: one group mixing employment + rental + purchase intent  
- Broad semantic dumps: unrelated keywords in one cluster  
- Decorative fastlinks: «О компании», «Главная», «Наши услуги»  
- Keyword-stuffed descriptions that read like meta-descriptions  

**Required patterns (launch-ready):**

- One semantic intent per group  
- Primary query phrase in `headline_1` and `description` (bold-highlight doctrine)  
- Keywords align with group intent tier  

---

## SE-01 — Single intent per group

| Field | Value |
|-------|-------|
| **rule_id** | SE-01 |
| **title** | One semantic intent per group |
| **severity** | error |
| **target_entity** | group |
| **purpose** | Enforce «one group = one intent» |
| **failure_examples** | Group name «Манипулятор общий» with keywords for 5т, бытовки, и вакансии |
| **validation_logic_summary** | `intent_purity_markers.single_intent_confirmed` must be true |
| **recommended_operator_action** | Split into separate groups per [intent-groups-v1.md](../research/intent-groups-v1.md) |

---

## SE-02 — Cross-intent risk

| Field | Value |
|-------|-------|
| **rule_id** | SE-02 |
| **title** | Cross-intent risk not high |
| **severity** | error |
| **target_entity** | group |
| **purpose** | Block groups that will bleed budget across intents |
| **failure_examples** | `cross_intent_risk: high` with mixed capability + employment phrases |
| **validation_logic_summary** | `cross_intent_risk` ≠ `high` |
| **recommended_operator_action** | Re-segment cluster; move outliers to X-tier reject or negatives |

---

## SE-03 — Employment / wrong-service keywords

| Field | Value |
|-------|-------|
| **rule_id** | SE-03 |
| **title** | No employment or wrong-service terms in cluster |
| **severity** | error |
| **target_entity** | group (`keyword_cluster`) |
| **purpose** | Anti-garbage at keyword level |
| **failure_examples** | `вакансии водитель манипулятор`, `купить манипулятор б/у`, `эвакуатор краснодар` |
| **validation_logic_summary** | Fail if any keyword matches blocklist: вакансии, работа, резюме, купить (asset), ремонт, запчасти, эвакуатор |
| **recommended_operator_action** | Remove phrases; add campaign negatives |

---

## SE-04 — Tier-X junk exclusion

| Field | Value |
|-------|-------|
| **rule_id** | SE-04 |
| **title** | No tier-X junk intents in launch groups |
| **severity** | error |
| **target_entity** | group |
| **purpose** | Keep launch set to S/A/B architecture |
| **failure_examples** | Group `intent_tier: X` marked launch-ready; «манипулятор» broad only |
| **validation_logic_summary** | If `intent_tier` = X and group not explicitly `research_only` → error |
| **recommended_operator_action** | Move to reject list or pause; do not export |

---

## SE-05 — Phrase in headline 1

| Field | Value |
|-------|-------|
| **rule_id** | SE-05 |
| **title** | Primary phrase in headline 1 (launch-ready) |
| **severity** | error |
| **target_entity** | ad (`keyword_alignment.phrase_in_headline_1`) |
| **purpose** | Yandex bold-highlight — user sees query echoed |
| **failure_examples** | H1 «Надёжная техника на объекте» for query «манипулятор 5 тонн» |
| **validation_logic_summary** | For launch-ready ads: `phrase_in_headline_1` = true AND primary keyword token subset in H1 (case-insensitive, ё/е normalize) |
| **recommended_operator_action** | Rewrite H1 starting with primary phrase |

---

## SE-06 — Phrase in description

| Field | Value |
|-------|-------|
| **rule_id** | SE-06 |
| **title** | Primary phrase in description (launch-ready) |
| **severity** | error |
| **target_entity** | ad (`keyword_alignment.phrase_in_description`) |
| **purpose** | Continuation for bold highlight in body text |
| **failure_examples** | Description with only generic trust lines |
| **validation_logic_summary** | `phrase_in_description` = true; primary keyword stem in description |
| **recommended_operator_action** | Open description with task phrase + capability |

---

## SE-07 — Anti-generic headline

| Field | Value |
|-------|-------|
| **rule_id** | SE-07 |
| **title** | Headline not from forbidden vanity list |
| **severity** | error |
| **target_entity** | ad (`headline_1`) |
| **purpose** | Block non-converting generic ads |
| **failure_examples** | «Лучшие цены на манипулятор»; «Качественные услуги» |
| **validation_logic_summary** | Match H1 against forbidden list (validation-schema + doctrine); allow only if task anchor present in same string |
| **recommended_operator_action** | Replace with capability/use-case anchored H1 |

---

## SE-08 — Duplicate H1 within group

| Field | Value |
|-------|-------|
| **rule_id** | SE-08 |
| **title** | No duplicate headline_1 within group |
| **severity** | warn |
| **target_entity** | group (ads) |
| **purpose** | Avoid fake A/B with identical copy |
| **failure_examples** | Two ads same H1, different description only |
| **validation_logic_summary** | Normalize H1 (case, punctuation); warn on duplicate in same group |
| **recommended_operator_action** | Differentiate angle (geo, proof, CTA) or reduce ad count |

---

## SE-09 — Duplicate H1 across campaign

| Field | Value |
|-------|-------|
| **rule_id** | SE-09 |
| **title** | No duplicate headline_1 across groups (campaign) |
| **severity** | warn |
| **target_entity** | campaign |
| **purpose** | Prevent cannibalization and auction self-competition |
| **failure_examples** | Same H1 on 5т group and 6x6 group |
| **validation_logic_summary** | Campaign-wide H1 hash; warn on collision across groups |
| **recommended_operator_action** | Tie H1 to group-specific intent phrase |

---

## SE-10 — Generic wording in description

| Field | Value |
|-------|-------|
| **rule_id** | SE-10 |
| **title** | No generic SEO wording without anchor |
| **severity** | error |
| **target_entity** | ad (`description`) |
| **purpose** | Forbid meta-description style fluff |
| **failure_examples** | «Мы предлагаем качественные услуги по лучшим ценам» |
| **validation_logic_summary** | Block phrases: качественные услуги, лучшие цены, лидер рынка without nearby task noun (манипулятор, тоннаж, use-case) |
| **recommended_operator_action** | Replace with concrete capability + action |

---

## SE-11 — Decorative fastlinks

| Field | Value |
|-------|-------|
| **rule_id** | SE-11 |
| **title** | Fastlinks must continue intent |
| **severity** | error |
| **target_entity** | ad (`fastlinks`) |
| **purpose** | Extensions are qualifiers, not site nav |
| **failure_examples** | «О компании», «Главная», «Контакты» as only fastlinks |
| **validation_logic_summary** | Title match against decorative blocklist |
| **recommended_operator_action** | Use intent fastlinks from blueprint (use-case, B2B, capability) |

---

## SE-12 — Keyword alignment

| Field | Value |
|-------|-------|
| **rule_id** | SE-12 |
| **title** | Primary keyword declared and in cluster |
| **severity** | error |
| **target_entity** | ad + group |
| **purpose** | Traceability from ad to cluster |
| **failure_examples** | `primary_keyword` not in `keyword_cluster.keywords` |
| **validation_logic_summary** | `keyword_alignment.primary_keyword` phrase exists in group cluster with `is_primary` or exact phrase match |
| **recommended_operator_action** | Set primary flag on correct keyword row |

---

## SE-13 — Giant keyword dump

| Field | Value |
|-------|-------|
| **rule_id** | SE-13 |
| **title** | Keyword cluster size within operator threshold |
| **severity** | warn |
| **target_entity** | group |
| **purpose** | Survivability — avoid unmanageable groups |
| **failure_examples** | 40 phrases in one exact-fit capability group |
| **validation_logic_summary** | Warn if `len(keywords)` > threshold (default 15, configurable) |
| **recommended_operator_action** | Split by micro-intent or tighten match types |

---

## SE-14 — Broad match without negatives

| Field | Value |
|-------|-------|
| **rule_id** | SE-14 |
| **title** | Broad match overuse without negatives |
| **severity** | warn |
| **target_entity** | group + campaign |
| **purpose** | Reduce garbage traffic risk on Search |
| **failure_examples** | Many `broad` keywords, empty `group_negatives` and thin campaign negatives |
| **validation_logic_summary** | Warn if >30% keywords broad AND negatives count below doctrine minimum |
| **recommended_operator_action** | Add group negatives; prefer phrase/exact for S-tier |

---

## SE-15 — Mixed intent groups in campaign

| Field | Value |
|-------|-------|
| **rule_id** | SE-15 |
| **title** | Detect mixed intent types in single group |
| **severity** | error |
| **target_entity** | group |
| **purpose** | Explicit mixed-intent container detection |
| **failure_examples** | Keywords for «аренда» + «перевозка бытовки» + «5 тонн» without sub-segmentation |
| **validation_logic_summary** | NLP-light: cluster tags (capability, use_case, b2b) >1 dominant → fail unless `mixed_container` campaign with documented split plan |
| **recommended_operator_action** | Split groups per intent type |

---

## SE-16 — Weak CTA detection

| Field | Value |
|-------|-------|
| **rule_id** | SE-16 |
| **title** | CTA semantics present and non-vague |
| **severity** | warn |
| **target_entity** | ad (`cta_semantics`) |
| **purpose** | Commercial clarity for mobile SERP |
| **failure_examples** | `primary_cta` missing; `cta_phrase: "Узнать больше"` on hot intent |
| **validation_logic_summary** | Warn if `primary_cta` empty or vague phrase without call/calculate/order |
| **recommended_operator_action** | Set `call` or `calculate` per intent tier |

---

## Registry cross-reference

[rule-registry-v1.md](rule-registry-v1.md) · [validation-schema-v1.md](../schema/validation-schema-v1.md)

# Campaign Generation Prompts v1

**Role:** Prompt patterns that produce **Campaign / Group / keyword_cluster / landing_route / negatives** as JSON — not Excel, not bulk ads.

**Prerequisite:** Approved intake brief — [intake-prompt-patterns-v1.md](intake-prompt-patterns-v1.md).

---

## Generation target

Output must conform to:

- Root: `OrcaPpcDocument` per [orca-ppc-document-v1.schema.json](../schema/json/orca-ppc-document-v1.schema.json)  
- Entity model: [entity-model-overview-v1.md](../schema/entity-model-overview-v1.md)  
- Doctrine: [generation-logic-v0.md](../doctrine/generation-logic-v0.md)

**Minimum viable generation pass:** `campaigns[]` with `groups[]`, each group having `keyword_cluster`, `landing_route`, `group_negatives` — ads may be empty `[]` until ad-generation pass.

---

## Core generation principles (embed in every prompt)

1. **Search intent architecture first** — structure before volume.  
2. **One group = one semantic intent** — no mixed employment / buy / repair / order.  
3. **Campaign split** only when psychology, landing, or commercial stage materially differ.  
4. **Keyword clustering** by commercial meaning — not syntax overlap.  
5. **Landing routing** per group — blueprint ref + URL from intake truth.  
6. **Intent tiers** — prefer S/A from [research/intent-groups-v1.md](../research/intent-groups-v1.md).  
7. **Quality > quantity** — see [anti-chaos-prompting-rules-v1.md](anti-chaos-prompting-rules-v1.md).

---

## Prompt A — Full campaign skeleton

```
TASK: Generate ORCA Triumph campaign structure as JSON only.

INPUT: <attach intake brief JSON>

OUTPUT: OrcaPpcDocument fragment containing:
- schema_version "v1"
- project_id, project_name, market, geo, source_pack
- search_only_scope: true
- campaigns[] with groups[] ONLY (ads: [] empty per group)
- global_negatives from intake
- landing_registry entries for blueprints used
- validation_policy, export_policy, human_review stubs

FOR EACH GROUP include:
- group_id, group_name, semantic_intent, intent_tier, intent_type
- keyword_cluster (3–12 keywords max per group unless operator extends)
- group_negatives
- landing_route (blueprint_id, url, routing_type)

RULES:
- No Excel, no prose outside JSON.
- No invented capabilities beyond intake confirmed list.
- No tier-X junk segments unless intake overrides.
- cluster_rules_ack: true on each keyword_cluster.
- Stable entity_id pattern: camp_*, grp_*.

STOP after structure; do not generate ads in this pass.
```

---

## Prompt B — Campaign structure only (multi-campaign)

Use when intake defines distinct psychology splits:

```
Split campaigns ONLY for:
- General hot vs B2B vs capability vs use-case vs intercity
Do NOT micro-split without semantic reason.

Output: campaigns[] array with metadata per campaign:
campaign_id, campaign_name, intent_classification, routing_role, geo, campaign_negatives.
Each campaign: groups[] as in Prompt A.
```

---

## Prompt C — Group segmentation

```
Given semantic_intent list from operator or intake,
propose groups[] with:
- one-line semantic_intent
- intent_tier (S|A|B)
- intent_type enum aligned with pack (capability_exact, use_case, b2b, hot_general, intercity)

Reject merging intents that change landing or user psychology.
Output: JSON array of group stubs without keywords first.
Operator approves → then run keyword clustering prompt.
```

---

## Prompt D — Keyword clustering (per group)

```
INPUT: single group stub + intake exclusions

OUTPUT: keyword_cluster object only:
{
  "intent_summary": "...",
  "cluster_rules_ack": true,
  "keywords": [
    { "phrase": "...", "match_policy": "phrase", "status": "active", "is_primary": true }
  ]
}

RULES:
- Max 12 phrases per group (default); primary phrase = closest to group semantic_intent.
- Same commercial meaning only (e.g. заказать / вызвать — OK).
- FORBIDDEN in cluster: вакансии, ремонт, купить, unrelated equipment.
- No giant dumps; no single-word broad keywords.
- Phrases must be usable for Yandex phrase match and headline alignment later.
```

---

## Prompt E — Landing routing

```
INPUT: group semantic_intent + landing_availability from intake

OUTPUT: landing_route per group:
- blueprint_id (from landing-pages/)
- final_url (only if confirmed; else SAFE UNKNOWN blocks export later)
- routing_type: exact_fit | master_fallback
- continuation_note: how ad intent continues on page

RULE: master_fallback is WARN-level risk — flag in meta.notes, not silent default.
```

---

## Prompt F — Negatives (campaign + group)

```
OUTPUT:
- global_negatives.keywords (intake + pack defaults)
- campaign_negatives per campaign
- group_negatives for sensitive groups (e.g. employment bleed)

Match_type_default: phrase unless operator specifies.
Do not add negatives that block valid commercial queries for the group intent.
```

---

## Prompt G — Intent tier assignment

```
Map each group to intent_tier S/A/B using research/intent-groups-v1.md.
Document reject_list acknowledgments for tier X queries (not in clusters).

Output: JSON map { group_id: { intent_tier, rationale_short } }
Rationale in JSON field only — max 120 chars — for human audit.
```

---

## Entity ID conventions (generation prompts must enforce)

| Entity | Pattern | Example |
|--------|---------|---------|
| Campaign | `camp_{scope}_{tier}_v{n}` | `camp_triumph_search_s_tier_v1` |
| Group | `grp_{tier}{nn}_{slug}` | `grp_s01_5ton` |
| Keyword | implicit in cluster | `is_primary: true` on one phrase |

IDs stable across repair passes — fix prompts must not rename IDs without operator approval.

---

## Forbidden generation behaviors

| Forbidden | Why |
|-----------|-----|
| Excel / CSV / Commander columns | Transport is Phase 5 exporter |
| “Generate all possible keywords” | SV / SE survivability failure |
| Random campaign splits | Destroys operator readability |
| Groups without landing_route | LM validation blocked |
| `search_only_scope: false` | ST-02 error |
| Ads with headlines in structure pass | Separation of concerns; ad prompts separate |

---

## Handoff to ad generation

Campaign JSON is ready for ad prompts when:

- [ ] Every group has `semantic_intent`, `keyword_cluster`, `landing_route`  
- [ ] `human_review.intake_approved` or operator message confirms brief  
- [ ] Operator explicitly requests ad pass  

See [ad-generation-prompts-v1.md](ad-generation-prompts-v1.md).

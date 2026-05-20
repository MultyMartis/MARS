# Validation Schema v1

**Role:** Pre-export validation contract for the full PPC entity graph.  
**When:** After entity assembly, **before** Excel export ([direct-commander-foundation](../export/direct-commander-foundation-v0.md)).  
**Output (future):** `ValidationReport` artifact — pass/fail + findings; **no** silent auto-fix.  
**Today:** Human operator runs checklist manually against this doc.

---

## Validation pipeline position

```
Campaign + Groups + Ads + LandingRoutes
        ↓
   VALIDATION (this schema)
        ↓
   export only if launch-ready
        ↓
   Export mapping → Commander Excel
```

---

## Severity levels

| Level | Meaning | Export |
|-------|---------|--------|
| `error` | Must fix before export | **Block** |
| `warn` | Human may accept with note | Allow with `validation_override` flag (future) |
| `info` | Suggestion only | Allow |

---

## 1. Structural validation

**Goal:** Entity graph is complete and referentially coherent.

| ID | Check | Level |
|----|-------|-------|
| ST-01 | Root `schema_version` = `v1` | error |
| ST-02 | `search_only_scope` = true on all campaigns | error |
| ST-03 | Campaign has ≥1 group | error |
| ST-04 | Group has ≥1 keyword | error |
| ST-05 | Group has ≥1 ad | error |
| ST-06 | All `parent_*_id` references resolve | error |
| ST-07 | Required fields per entity schemas present | error |
| ST-08 | `use_case_classification` set iff `landing_type`=use_case | error |
| ST-09 | `capability_classification` set iff capability intent | error |
| ST-10 | `intent_continuity_ack` = true for launch-ready groups | error |
| ST-11 | No orphan ads or duplicate `entity_id` | error |

---

## 2. Symbol validation

**Goal:** Respect Yandex Direct field limits; avoid truncation surprises.

**Authority order:**  
1. [assets/direct-commander-template/](../assets/direct-commander-template/) annotations  
2. [ad-entity-schema-v1.md](ad-entity-schema-v1.md) contract table  
3. Live Direct UI at import (**SAFE UNKNOWN** if drift)

| ID | Check | Level |
|----|-------|-------|
| SY-01 | `headline_1` length ≤ 56 (spaces included) | error |
| SY-02 | `headline_2` length ≤ 30 if present | error |
| SY-03 | `description` length ≤ 81 | error |
| SY-04 | Each fastlink title ≤ 30 | error |
| SY-05 | Each callout ≤ 25 | error |
| SY-06 | Display URL path segments ≤ 20 | error |
| SY-07 | Truncation risk: word cut mid-token at limit−3 | warn |
| SY-08 | Excessive punctuation consuming budget | warn |
| SY-09 | Duplicate spaces / leading-trailing space | warn |

---

## 3. Semantic validation

**Goal:** Intent purity, relevance, anti-garbage, alignment.

| ID | Check | Level |
|----|-------|-------|
| SE-01 | One semantic intent per group (`intent_purity_markers.single_intent_confirmed`) | error |
| SE-02 | `cross_intent_risk` ≠ `high` | error |
| SE-03 | Keyword cluster: no employment / buy asset / repair terms | error |
| SE-04 | No mixed tier-X junk from [intent-groups](../research/intent-groups-v1.md) | error |
| SE-05 | `phrase_in_headline_1` = true for launch-ready ads | error |
| SE-06 | `phrase_in_description` = true for launch-ready ads | error |
| SE-07 | Anti-generic: H1 not from forbidden vanity list | error |
| SE-08 | Duplicate detection: same H1 across ads in group | warn |
| SE-09 | Duplicate detection: same H1 across groups (campaign) | warn |
| SE-10 | Generic wording: «качественные услуги», «лучшие цены» without anchor | error |
| SE-11 | Fastlinks not decorative (О компании, Главная) | error |
| SE-12 | Keyword alignment: primary keyword ∈ cluster | error |
| SE-13 | Giant keyword dump (>N keywords — operator threshold, default 15) | warn |
| SE-14 | Broad match overuse without negatives | warn |

### Forbidden primary headline patterns (non-exhaustive)

- Лучшие цены  
- Надёжная компания  
- Качественные услуги  
- Лидер рынка  
- Профессиональные услуги *(without task anchor)*

### Anti-garbage keyword signals

Fail if cluster dominated by:

- `вакансии`, `работа`, `резюме`  
- `купить` (asset purchase)  
- `ремонт`, `запчасти`  
- `эвакуатор` (wrong service)  
- `бесплатно`, `своими руками` (policy-dependent — warn)

---

## 4. Landing mismatch validation

**Goal:** Ad ↔ landing continuation integrity.

| ID | Check | Level |
|----|-------|-------|
| LM-01 | `ad.landing_url` = `group.landing_route.final_url` unless override documented | error |
| LM-02 | `landing_type` matches group classifications | error |
| LM-03 | Use-case ad on capability-only page (or reverse) | error |
| LM-04 | B2B ad language without B2B route | error |
| LM-05 | Intercity promise without intercity route | error |
| LM-06 | Specific intent forced to master fallback without `fallback_reason` | warn |
| LM-07 | Capability claims in ad not supported by blueprint class | error |

---

## 5. Commercial validation

**Goal:** CTA, capability, and trust claims are commercially coherent for Triumph.

| ID | Check | Level |
|----|-------|-------|
| CM-01 | `cta_semantics` fits intent tier (e.g. B2B → calculate/call, not hype) | warn |
| CM-02 | Tonnage/boom claims plausible for Triumph machine line | error |
| CM-03 | «Без посредников» / trust lines not contradicted elsewhere | warn |
| CM-04 | Geo mention consistent with campaign `geo` | warn |
| CM-05 | Mobile readability flags all true for launch-ready | error |
| CM-06 | Practical trust: no impossible promises (24/7 unless true) | warn |

---

## 6. Campaign / negative validation

| ID | Check | Level |
|----|-------|-------|
| NG-01 | Campaign global negatives include core junk blockers | warn if missing |
| NG-02 | Group negatives do not negate own intent keywords | error |
| NG-03 | Negative conflicts between campaign and group documented | info |

---

## 7. PPC survivability validation

**Goal:** Structure is operable by a human in production — anti-entropy.

| ID | Check | Level |
|----|-------|-------|
| SV-01 | Group count proportionate to intent map (no micro-spam) | warn |
| SV-02 | Group names human-readable | warn |
| SV-03 | `mixed_container` campaign without split justification | warn |
| SV-04 | >5 ads per group with near-duplicate copy | warn |
| SV-05 | Launch-ready without human `approved_for_export` status (future) | info |

---

## ValidationReport (future shape)

```yaml
schema_version: v1
validated_at: iso8601
campaign_ids: [string]
summary:
  errors: 0
  warnings: 0
findings:
  - { id: SE-05, level: error, entity_id: ad_x, message: "..." }
passed: boolean
```

**Rule:** `passed` = true only if `errors` = 0.

---

## Human supervision

Validation assists — it does **not**:

- Launch campaigns  
- Auto-pause ads  
- Rewrite copy without human visibility  

Operator may override `warn` with written reason in project notes (future field).

---

## Phase 3 implementation notes

Engine should:

- Load entity graph JSON  
- Run rules by ID  
- Emit `ValidationReport`  
- Never mutate entities silently  

Out of scope: ML quality scoring, autonomous bid advice.

---

## SAFE UNKNOWN

- Exact duplicate detection normalization (ё/е, punctuation) — define in Phase 3.  
- Platform moderation outcomes — human confirms post-import.

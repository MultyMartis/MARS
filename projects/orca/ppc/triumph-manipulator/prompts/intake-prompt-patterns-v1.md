# Intake Prompt Patterns v1

**Role:** Collect and normalize operator context **before** any campaign JSON is generated.  
**Output:** Intake brief (structured JSON sidecar recommended) — **not** ads or keywords at scale.

---

## Intake objective

Produce a **truth-bounded brief** that downstream generation prompts consume. Intake answers: *what may Triumph legitimately claim in search*, *where*, *for whom*, and *what is explicitly out of scope*.

---

## Required intake fields

| Field | Purpose | If unknown |
|-------|---------|------------|
| **niche** | Service category (manipulator / crane-truck, local B2B+B2C) | State niche; do not invent adjacent services |
| **geo** | Primary region, optional extended area | `SAFE UNKNOWN` for region IDs; use operator-confirmed labels |
| **capabilities** | Machine facts: tonnage, boom, 6×6, payment types | List only **confirmed** items; mark unconfirmed as `unknown` |
| **use_cases** | Bytovka, stroymaterialy, equipment, containers, etc. | Reference [landing-pages/INDEX.md](../landing-pages/INDEX.md) IDs when known |
| **landing_availability** | Which blueprint URLs exist and are launch-ready | `status: ready \| draft \| missing` per blueprint |
| **target_intent** | Tier focus (S/A first), hot vs qualification | Link to [research/intent-groups-v1.md](../research/intent-groups-v1.md) |
| **B2B_scope** | Legal entities, безнал, contracts | Do not claim B2B features without confirmation |
| **exclusions** | Global negatives, forbidden queries (jobs, repair, buy) | Inherit pack defaults; operator may extend |
| **priorities** | Launch order, budget sensitivity, mobile emphasis | Qualitative — no fake numeric targets |
| **launch_constraints** | Search-only, no RSYA, draft vs live, timeline | Enforce `search_only_scope: true` |

---

## Intake brief JSON sidecar (recommended shape)

Documentation contract — not a separate schema file in Phase 6:

```json
{
  "brief_version": "v1",
  "source_pack": "triumph-manipulator",
  "niche": "local manipulator rental — Krasnodar",
  "geo": {
    "primary_region": "Краснодар",
    "extended_notes": "SAFE UNKNOWN — operator to confirm край / межгород list"
  },
  "capabilities": {
    "confirmed": ["board_5t", "boom_14m", "bez_posrednikov"],
    "unknown": ["6x6_vezdekhod_availability"]
  },
  "use_cases": [
    { "id": "bytovka", "landing_blueprint": "02-use-case-bytovka", "ready": true }
  ],
  "landing_availability": [
    { "blueprint_id": "01-master-hot-general", "url": "SAFE UNKNOWN", "status": "draft" }
  ],
  "target_intent": {
    "priority_tiers": ["S", "A"],
    "reject_tier_x": true
  },
  "b2b_scope": {
    "enabled": true,
    "confirmed_features": ["bez_nal"],
    "unconfirmed": ["dogovor_postavki"]
  },
  "exclusions": {
    "global_negative_keywords": ["вакансии", "работа", "ремонт", "купить"]
  },
  "priorities": "Launch S-tier capability + use-case before broad hot master",
  "launch_constraints": {
    "search_only": true,
    "no_autolaunch": true,
    "draft_mode": true
  },
  "safe_unknowns": [
    "Exact intercity radius not confirmed"
  ]
}
```

---

## Master intake prompt pattern (operator → AI)

Use as Cursor session opener (paraphrase; keep constraints):

```
TASK: ORCA Triumph intake normalization only.

CONTEXT: triumph-manipulator pack. Search-only Yandex Direct.

COLLECT AND STRUCTURE:
- niche, geo, capabilities, use-cases, landing availability
- target intent tiers, B2B scope, exclusions, priorities, launch constraints

RULES:
1. Output JSON intake brief only (brief_version v1). No campaign entities yet.
2. For any unconfirmed business fact, use SAFE UNKNOWN — never invent capabilities.
3. Capabilities must be operator-confirmed or marked unknown.
4. Reference landing blueprint IDs from pack when cited.
5. Enforce search_only, no autolaunch in launch_constraints.
6. No keyword lists, no ads, no Excel.

If operator input is incomplete, list missing fields under safe_unknowns and ask targeted questions — do not fill with guesses.
```

---

## Anti-hallucination rules (intake-specific)

| Forbidden | Required instead |
|-----------|------------------|
| Inventing tonnage, boom length, fleet size | `capabilities.confirmed` vs `unknown` |
| Claiming URLs not provided | `landing_availability.status: missing` + SAFE UNKNOWN |
| Assuming 24/7, cheapest, nationwide | Omit or mark unknown |
| SEO-style market claims | Operational facts only |
| Expanding into evacuator, crane rental without charter | Explicit exclusion note |

**Doctrine:** Commercial truthfulness feeds CM-* validation later — intake errors become launch risk.

---

## Intake → generation handoff

Generation prompts **must** receive:

1. Approved intake brief JSON  
2. Explicit list of `safe_unknowns` (generation must not resolve unknowns silently)  
3. Operator sign-off line: `intake_approved: true` (human-set field)

Until `intake_approved`, campaign generation prompts are **out of scope**.

---

## Specialized intake sub-prompts

### A — Capability confirmation

```
List each capability claim as: confirmed | unknown | forbidden.
Sources allowed: operator message, landing blueprints, pack doctrine only.
Do not read live web unless operator attaches evidence.
```

### B — Landing inventory

```
For each use-case/capability in scope, map:
blueprint_id → url → status (ready|draft|missing).
Flag LM-risk if ad generation would reference missing URL.
```

### C — Intent tier selection

```
From research/intent-groups-v1.md, propose S/A segments for this launch.
Exclude tier X unless operator explicitly overrides with written reason.
```

---

## SAFE UNKNOWN handling

- Every `SAFE UNKNOWN` must appear in `safe_unknowns[]` with **what would verify it** (e.g. “operator confirms URL in CMS”).  
- Downstream prompts **must not** convert UNKNOWN to copy claims.  
- Validation-fix may not “fix” UNKNOWN by inventing facts — only structure or wording within known bounds.

---

## STOP cues (intake session)

- STOP when brief is complete enough for **one** campaign architecture pass  
- STOP after three clarification rounds — escalate to human, do not guess  
- Do not start campaign JSON in the same prompt as intake unless operator explicitly combines steps

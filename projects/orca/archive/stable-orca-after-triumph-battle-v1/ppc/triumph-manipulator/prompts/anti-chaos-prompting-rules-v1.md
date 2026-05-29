# Anti-Chaos Prompting Rules v1

**Role:** Hard constraints on prompt design and operator session behavior — **quality > quantity**.

Aligned with doctrine anti-garbage and validation survivability (SV-*, SE-*).

---

## Core rule

```
10 strong groups  >  100 garbage groups
3 truthful ads     >  50 generic ads
```

Any prompt that optimizes for volume is **invalid** for ORCA Triumph.

---

## Forbidden prompt outcomes

| Chaos pattern | Why forbidden | Detection |
|---------------|---------------|-----------|
| Giant keyword dumps | Destroys intent purity; SV fail | >12 keywords/group without charter |
| Generic ads | Low CTR, CM/SE fail | Forbidden phrase list in doctrine |
| Semantic duplication | Wasted spend, SE fail | Same intent in multiple groups |
| Hallucinated capabilities | Trust/legal risk; CM fail | Claims not in intake |
| Random campaign splitting | Operator unreadable | Micro-campaigns without psychology change |
| Uncontrolled expansion | Session never ends | “Also add…” loops without STOP |
| Excel-first generation | Bypasses validation | Any tabular ad/keyword output |
| “1000 ads” behavior | Spam production | Batch size limits violated |
| SEO-style fluff | Wrong discipline | Long descriptions, storytelling |
| Autonomous launch | Policy violation | Import/launch language in prompts |

---

## Prompt size and batch limits (default)

| Artifact | Default max per single prompt | Override |
|----------|------------------------------|----------|
| Groups per campaign | 15 | Operator written charter |
| Keywords per group | 12 | Same |
| Ads per group | 3 draft variants | Same |
| Campaigns per document | 5 | Architecture review |
| Fix targets per pass | All FAILs or ≤10 rule results | Operator choice |

Override must be **explicit in operator message** — model must not self-escalate limits.

---

## Semantic duplication prevention

Before adding a group, prompt must check:

1. Does an existing group share **commercial meaning**? → merge, don’t duplicate  
2. Does keyword differ only by morphology? → same cluster  
3. Does new group change landing psychology? → if no, same group  

**Prompt instruction snippet:**

```
Before proposing a new group, list existing group_id + semantic_intent and justify why a new group is required in ≤20 words.
If justification weak, do not create group.
```

---

## Generic wording blocklist (embed in ad prompts)

From doctrine — non-exhaustive; expand in validation:

- лучшие цены  
- высокое качество  
- надёжная компания  
- профессиональный подход  
- команда специалистов  
- лидер рынка  
- индивидуальный подход  
- полный спектр услуг  

Prefer: capability, use-case, geo, operational clarity.

---

## Capability truthfulness

```
INTAKE confirmed list = upper bound of all copy claims.
UNKNOWN capability → no ad claim; no callout; no fastlink.
```

**Forbidden prompt:** “Assume 6×6 available to make ads stronger.”

---

## Campaign splitting discipline

**Split when:**

- B2B vs B2C psychology differs  
- Landing family differs (master vs exact-fit use-case)  
- Intercity vs city-only geo intent  

**Do not split when:**

- Synonym variants of same intent  
- Artificial tiering for “more campaigns”  
- Single-word keyword differences  

---

## Excel-first rejection

If operator asks “fill Commander template”:

1. Refuse as primary output  
2. Offer JSON entity path → validation → export per Phase 5  
3. Excel only after G4 human review  

---

## Session STOP rules (anti-entropy)

| Signal | Action |
|--------|--------|
| 3 validation loops same rule | STOP — human architecture |
| Keyword count doubling | STOP — prune |
| Model proposes new pack scope | STOP — out of charter |
| “While we’re at it” expansion | STOP — new session charter |

Pack [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) STOP cues apply.

---

## Quality preservation in repair

Validation-fix prompts must **not**:

- Fix SV keyword dump by hiding keywords in `meta`  
- Fix SE mixing by renaming group only (same cluster)  
- Fix SY overflow by removing primary phrase without operator approval  

---

## Positive patterns (encouraged)

| Pattern | Benefit |
|---------|---------|
| S/A tier first launch | Survivability |
| One ad draft per group until validated | Focus |
| Primary phrase flagged in cluster | SE alignment |
| `draft` status default | Safe staging |
| Intake SAFE UNKNOWN | Honest export gate |

---

## Enforcement chain

```
anti-chaos prompt rules
    → JSON output contract
    → validation engine (SV/SE/CM)
    → human review gates
    → dumb exporter
```

Prompts are first line; validation is second; human is final.

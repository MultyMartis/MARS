# Human Review Gates v1

**Role:** Mandatory operator checkpoints between AI-assisted JSON production and **export / Commander import / launch**.

**Authority model:** Human is final authority — [generation-logic-v0.md](../doctrine/generation-logic-v0.md).

**Explicit prohibition:** **No auto-launch.** No prompt may trigger import, bidding, or campaign activation.

---

## Gate map

```
Intake approved (G0)
    → Structure approved (G1)
    → Copy approved (G2)
    → Validation accepted (G3)
    → Export approved (G4)
    → Commander import (G5 — human in UI)
    → Launch (G6 — human in Direct)
```

AI assists G0–G4 documentation only; **G5–G6 are human-only**.

---

## G0 — Intake approved

| Check | Pass criteria |
|-------|----------------|
| Capabilities | Only confirmed facts; UNKNOWNs listed |
| Landings | URLs ready or explicitly missing |
| Exclusions | Global negatives acknowledged |
| Scope | Search-only, Triumph pack |

**Field (recommended):** `human_review.intake_approved: true` + `intake_approved_by` + ISO date.

**Reject:** Regenerate intake brief — do not proceed to campaign JSON.

---

## G1 — Structure approved

| Check | Pass criteria |
|-------|----------------|
| Intent purity | One semantic intent per group |
| Campaign splits | Semantically justified |
| Keyword volume | No giant dumps (SV) |
| Landing routes | Every group has route + blueprint |
| Tier focus | S/A prioritized per charter |

**Reject semantics:** `structure_rejected: true`, `reject_reason` — return to campaign generation prompts, not ad pass.

---

## G2 — Copy approved

| Check | Pass criteria |
|-------|----------------|
| Headlines | Phrase alignment, non-generic |
| Truthfulness | CM capability claims verified |
| Mobile | Readable, practical CTA |
| Draft flag | Ads remain `draft` until operator promotes |

**Reject:** Targeted ad fix prompts per group — not full regen.

---

## G3 — Validation accepted

| Check | Pass criteria |
|-------|----------------|
| FAIL count | Zero blocking `fail` results |
| WARN | Each warn fixed **or** acknowledged with operator note |
| Report | `ValidationReport` stored alongside document |
| Export flag | `export_allowed: true` only when policy satisfied |

**Reject:** [validation-fix-prompts-v1.md](validation-fix-prompts-v1.md) loop — max 3 assisted loops then human architecture review.

**SAFE UNKNOWN:** If FAIL due to missing URL/fact — **block export**, do not AI-guess.

---

## G4 — Export approved (mandatory before Excel)

| Check | Pass criteria |
|-------|----------------|
| Document + report | Both inputs to exporter design |
| Workbook spot-check | Cyrillic, URLs, draft flags |
| Transport only | No semantic edits in Excel session |

**Field:** `human_review.approved_for_export: true`

**Forbidden:**

- Prompt “export and launch”  
- Autonomous exporter trigger without G4  
- Treating Excel as SoT edits (changes must round-trip to JSON first)

---

## G5 — Commander import (human)

Operator actions in Yandex Direct Commander:

- Import `.xlsx`  
- Resolve platform warnings  
- Map any manual adjustments back to JSON if SoT must stay aligned  

**AI role:** None — documentation support only.

---

## G6 — Launch (human)

- Bids, budget, schedule, geo fine-tuning in Direct  
- **launch_allowed** in validation schema is **never** set by AI  

---

## Approval / reject semantics

### Approve

```json
"human_review": {
  "intake_approved": true,
  "structure_approved": true,
  "copy_approved": true,
  "validation_accepted": true,
  "approved_for_export": true,
  "approved_by": "operator_handle",
  "approved_at": "2026-05-20T12:00:00Z",
  "notes": "S-tier draft ready for Commander transport"
}
```

Only operator (or explicit operator instruction in session) may set `true`.

### Reject

```json
"human_review": {
  "rejected": true,
  "reject_stage": "G2_copy",
  "reject_reason": "Generic headline on grp_s03",
  "rejected_at": "2026-05-20T12:00:00Z"
}
```

Reject clears downstream approvals (`approved_for_export: false`).

---

## Operator checkpoints (quick checklist)

**Before any export conversation:**

- [ ] I confirmed machine capabilities  
- [ ] I confirmed landing URLs  
- [ ] I read group names aloud — intents are pure  
- [ ] I reviewed validation FAIL/WARN list  
- [ ] I accept draft vs active ad status  
- [ ] I will import and launch myself in Direct  

---

## Auto-launch prohibition (absolute)

| Forbidden | Category |
|-----------|----------|
| “Launch campaign after export” | Autonomous launch |
| n8n scheduled import without human | Hidden automation |
| Prompt chaining that calls Direct API | Runtime not in pack |
| Setting `launch_allowed: true` via AI | Policy violation |

Future n8n may **notify** operator — not launch — [future-prompt-implementation-notes-v1.md](future-prompt-implementation-notes-v1.md).

---

## Relationship to validation engine

| Concept | Owner |
|---------|-------|
| `export_allowed` | Validation policy + zero blocking fails |
| `approved_for_export` | Human G4 |
| `launch_allowed` | Human G6 only — never AI |

See [validation/validation-engine-overview-v1.md](../validation/validation-engine-overview-v1.md).

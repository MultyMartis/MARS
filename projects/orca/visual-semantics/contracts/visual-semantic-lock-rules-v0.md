# Visual Semantic Lock Rules v0

Aligns with `orca-website-factory-semantic-lock-v0` — visual layer only.

## Lock types

| Lock | Visual semantics enforcement |
|------|------------------------------|
| One machine | `semantic_focus` includes `one_machine`; no fleet hero visuals |
| No fake hero price | no rate block in hero zones |
| Capability numbers | specs match pack + instance callouts |
| Trust sources | Яндекс + Авито in reviews section when required |
| Qualification | `qualification_mode` must match blueprint tier |
| Anti-evacuation | notice in hero OR explicit destructive waiver |

## Partial activation (Triumph zakaz)

From `semantic-lock-state-v1.md`:

| Domain | Status |
|--------|--------|
| One machine / specs | preserved |
| No fleet / fake price | preserved |
| Geo | preserved |
| Trust strip 4.9 in hero | **drifted** → operational — ambiguous |
| Hero qualification notice | **weakened** — destructive |
| Master hot handoff / pack | **missing** — artifact gap |

**Verdict:** semantic lock **partially active by doctrine**, not by full artifact trail.

## Visual lock on drift

| Drift class | Lock action |
|-------------|-------------|
| productive | document in pack; no revert during cleanup |
| destructive | block `approved_for_factory` |
| ambiguous | operator sign-off in pack |

## Operator activation checklist

1. Author master-hot handoff with visual semantics block
2. Create zakaz content pack with fields
3. `approved_for_factory: true` + human sign-off
4. Empty `drift_acceptance.destructive`
5. Register route in landing-route-registry — **UNKNOWN** without registry read

## Do not claim

- Factory auto-enforces visual locks
- HTML validation in validation-cli

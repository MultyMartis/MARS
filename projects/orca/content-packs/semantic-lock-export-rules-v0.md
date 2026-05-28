# Semantic Lock & Export Rules v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — binds content packs to export integrity and Website Factory MODE 1.

Extends [../intelligence/orca-website-factory-semantic-lock-v0.md](../intelligence/orca-website-factory-semantic-lock-v0.md) for the **content-packs** layer.

## Core rule

> **ORCA-approved landing content pack copy is locked at export and at Factory implementation when MODE 1 is active.**

Website Factory implements **visuals and frontend**. It does **not** rewrite ORCA-approved meaning.

## When semantic lock is active

All must be true:

1. Landing content pack `artifact_state` is `approved`, `factory-ready`, or `client-ready`
2. `content_mode: MODE_1` on pack envelope
3. Gate `approved_for_factory` recorded by **human operator**
4. Export or handoff references pack `pack_id` + `pack_version`

If any condition fails → **MODE 2** or provisional treatment.

## Locked at export (MODE 1)

These fields are **frozen** in DOCX and in Factory handoff:

| Domain | Examples |
|--------|----------|
| Headlines / H1 | Intent qualification strings (e.g. «5 тонн» + «Краснодар») |
| Capability numbers | Борт / стрела / вылет / кузов / мин. заказ |
| Positioning | Single-machine vs fleet framing |
| Negative space | Denied tasks, anti-evacuator filters |
| CTA hierarchy | Form vs call primary; messenger order |
| Price framing | «по задаче», no fake hourly rate |
| Trust claims | Review sources (e.g. Яндекс + Авито), rating text where approved |
| FAQ answers | No second machine, no invented tariffs |

## Allowed without lock breach

| Change | Layer |
|--------|--------|
| Layout, spacing, responsive | Factory presentation |
| Typography scale within brand | Factory |
| Iconography, imagery crop | Factory |
| `&nbsp;` and HTML typography fixes | Factory (no meaning change) |
| Component library extraction | Factory (no copy rewrite) |

## Export-specific rules

| Export type | Lock behavior |
|-------------|---------------|
| **DOCX** | Embeds `semantic_lock: active` in document header/footer metadata block |
| **Markdown** | Front-matter `semantic_lock: active` + section-level `locks[]` |
| **PDF (future)** | Must be generated from locked DOCX revision only |
| **Markdown → DOCX round-trip** | Operator must diff; AI must not silently “improve” copy |

## Indicators in exports

Exports should visibly mark:

- `MODE 1 — SEMANTIC LOCK ACTIVE`
- Per-section `🔒` or `semantic_lock: true` where subsection copy is frozen
- `SAFE UNKNOWN` markers preserved verbatim — not resolved by tooling

## MODE 2 rules

| Allowed | Forbidden |
|---------|-----------|
| Placeholder lorem or demo Russian | Shipping demo copy to production PPC URLs |
| Structural pack without final copy | Claiming MODE 1 continuity in QA reports |
| Factory exploration | Citing pack as approved SoT |

## Operator override

Explicit override requires:

- Dated note in `projects/orca/projects/<id>/approvals/`
- Updated `pack_version`
- Re-export DOCX if client-facing revision changed meaning

AI/Cursor **cannot** perform override.

## Violation handling

1. Stop Factory merge / deploy discussion  
2. Diff pack vs live HTML  
3. Restore from approved pack or bump version with operator sign-off  
4. Do not “fix” copy in HTML without pack update  

## Related

- [../artifacts/approval-gates-contract-v0.md](../artifacts/approval-gates-contract-v0.md)
- [artifact-lifecycle-v0.md](artifact-lifecycle-v0.md)
- [exporters/export-modes-v0.md](exporters/export-modes-v0.md)

## Boundary

Rules and vocabulary only — not automated enforcement.

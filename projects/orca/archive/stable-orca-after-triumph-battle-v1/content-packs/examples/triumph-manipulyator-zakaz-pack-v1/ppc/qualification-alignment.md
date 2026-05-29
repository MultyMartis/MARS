# PPC — Qualification alignment

## Blueprint requirement

Master hot = **PPC Qualification System** — filter junk within 5–10 sec.

## Qualification surfaces (as-built)

| Surface | Mechanism | Fold |
|---------|-----------|------|
| `hero__notice` | Anti-evacuation, мелкие бытовые | hero (bottom) — verify visibility |
| `hero__cargo` | Task type self-segmentation | hero lower |
| `tasks` denied block | Authoritative exclusions | below fold |
| FAQ Q6 | Short denied echo | below fold |
| Campaign negatives | купить, вакансии… | ads only |

## Continuity with instance rule

«Hero - заказ, подача, **квалификация задачи**»

| Element | Status |
|---------|--------|
| заказ | form + FAQ — **yes** |
| подача | lead, proof, steps — **yes** |
| квалификация | tasks + notice — **partial** if notice below fold |

## Calibration history

- G1 had `hero__notice` — noted removed in early G2 calibration
- **Current repo:** notice present — re-verify in mobile QA

## Forbidden drift

- Removing denied tasks section
- Removing anti-evacuation line entirely
- Adding «берём всё» broad claims

## Productive drift

- Cargo cards as interactive qualification
- Compact denied list vs prose walls

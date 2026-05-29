# Semantic Drift Rules v0

Human-operated classification for ORCA ↔ Factory ↔ PPC deltas.

## Definitions

| Term | Meaning |
|------|---------|
| **Source semantics** | ORCA blueprint, content pack, or signed handoff |
| **As-built semantics** | Shipped HTML copy + visible UI labels in workspace dist/src |
| **PPC surface** | Yandex ad headlines, descriptions, callouts, display path |
| **Lock** | Explicit 🔒 field in pack/handoff that blocks change without operator override |

## Decision tree

1. Does the change alter **locked** copy or claims? → If yes without override → **destructive**
2. Does the change break **ad ↔ hero** intent for the active ad variant? → **destructive** (PPC)
3. Does the change improve **qualification / CTA visibility** without breaking locks? → **productive**
4. Is it typography, spacing, grid only? → **neutral presentation**

## Destructive drift (examples from Triumph v0)

| Signal | Why destructive |
|--------|-----------------|
| Fleet framing («5–10 т», «свой автопарк») | Breaks one-machine positioning |
| Fake hero price («от XXXX ₽/час») | Breaks price honesty lock |
| Missing qualification line when blueprint requires it | Increases junk leads |
| H1 that contradicts primary ad for the launched variant | PPC continuity failure |
| Invented reviews / ratings | Trust lock violation |

## Productive evolution (examples from Triumph v0)

| Signal | Why productive |
|--------|----------------|
| Hero grid: copy left + **inline form** right | CTA visible without scroll; matches call+form strategy |
| Five spec bullets above fold | Capability-first; continues ad callouts (5 т / 3 т / 14 м) |
| Removal of v4 placeholder pricing | Restores honesty |
| `hero--v5` separated bg `<img>` + overlay | Reduces text-on-busy-photo clutter vs old composite hero |
| Cargo chips as tappable cards with micro-CTA | Task-first qualification; extends use-case chips |

## Ambiguous drift (requires operator tag)

| Signal | Notes |
|--------|-------|
| Trust strip: **4.9 ★ reviews** (ORCA) → **operational proof** (От 30 мин, безнал…) | May be productive for ops clarity; **weakens** immediate social proof — tag per ad variant |
| CTA wording: «Узнать стоимость перевозки» → «Рассчитать стоимость» | Same intent family; log as **minor lexical drift** |
| H1 «Аренда…» vs ad «Заказать…» (same group, different ads) | Not factory error — **multi-ad coverage** issue; pack should specify primary H1 strategy |

## Documentation requirement

Every drift finding must cite:

- Source path (blueprint / pack / handoff / JSON ad)
- As-built path (partial or built HTML)
- Classification: destructive | productive | neutral | ambiguous
- Operator action: fix | accept | defer | SAFE UNKNOWN

## No auto-verdict on performance

Drift rules judge **semantic and continuity** fit — not CTR or CR.

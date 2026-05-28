# Semantic Density Rules v0

## Definition

**Semantic density** = number of distinct **messages** (not words) competing in the same visual zone.

Semantic content can be correct while density is **destructive** — Triumph G0 hero proved this.

## Density warning model

| Level | Element budget (hero, single zone) | Action |
|-------|-----------------------------------|--------|
| `low` | ≤5 | OK for narrow intent |
| `medium` | 6–10 | Monitor CTA weight |
| `high` | 11–18 | Requires zoning (`hero_layout_mode`) |
| `overloaded` | 19+ | **Warning** — split zones or cut elements |
| `critical` | Multiple primary CTAs same zone | **Block** without operator override |

Field mapping: `visual_density` + `visual_noise_risk`.

## Triumph G0 failure (v4 index) — overloaded single zone

Competing in one hero block:

- 6× `hero__features` lines
- fake hourly rate
- fleet claim «5–10 т»
- «Свой автопарк»
- CTA without inline form
- visual placeholder competing with H1

**Class:** `overloaded` + `visual_noise_risk: critical` + wrong `semantic_focus`.

## Triumph G2 (v5 zakaz) — high but zoned

| Zone | Elements | Density |
|------|----------|---------|
| `hero__main` | H1, lead, 5 specs, form (5 fields) | high |
| `hero__lower` proof | 4 icons | medium |
| `hero__lower` cargo | 6×3 lines + micro-CTA | high |

**Total ~20+ messages before scroll** — acceptable for `master_hot` only with explicit pack flag `visual_density: high`.

## Destructive density patterns

1. **Same fact twice** — «мин. заказ 2 ч» in specs AND proof strip (Triumph: redundant).
2. **Six secondary CTAs** — cargo row competes with form submit (`cta_weight: secondary_noise`).
3. **Pricing in hero** — fake rate destroyed trust (removed in v5 — productive).
4. **Qualification + proof + cargo + specs in one row** — G0 pattern; forbidden.

## ORCA generation guardrails

When ORCA drafts hero content, flag if blueprint aggregate includes:

- 6+ features **and**
- pricing **and**
- proof **and**
- qualification **and**
- chips/cargo **and**
- primary + secondary CTA

→ recommend split: main = capability + CTA; lower = proof + qualification + chips (max 4–6).

## Pack fields

| Field | Use |
|-------|-----|
| `visual_density` | Overall tier |
| `visual_noise_risk` | Focal competition |
| `cargo_cards_max` | vNext — cap interactive chips (calibration proposed 4 mobile / 6 desktop) |

## SAFE UNKNOWN

Exact numeric thresholds per viewport — human sets tier from calibration, not formula.

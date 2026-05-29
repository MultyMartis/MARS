# Calibration — Destructive drift

**Source:** `projects/orca/visual-semantics/triumph-calibration/destructive-drift-findings-v1.md`

## Active

### D2 — Multi-ad H1 vs single landing H1

| Ad | Token |
|----|-------|
| A2 | **strong** — «Аренда» |
| A1 | **weak** — «Заказать» absent from H1 |

**Owner:** ORCA PPC + operator — not Factory-only.  
**Gate:** do not mark grp_fc12 fully continuity-verified until resolved.

## Historical (G0 — never restore)

- fake hero hourly rate
- fleet «5–10 т», «Свой автопарк»
- `hero_layout_mode: legacy_clutter`

## D1 — Qualification in hero (calibration update)

**Prior finding:** `hero__notice` removed in early G2 notes.  
**Repo snapshot 2026-05-28:** `hero__notice` **present** in `screen-01-hero.html`.

**Pack status:**

- If notice visible on mobile → downgrade D1 to **mitigated**
- If notice hidden by CSS → remains **destructive** until fix

Operator QA required.

## Ambiguous (not destructive without operator call)

- 4.9 ★ absent in hero (ops substitute)
- `intent_continuity_ack: false` — process honesty, not UX bug

## Launch gate (calibration opinion)

1. Resolve D2 H1 strategy
2. Confirm D1 visibility on mobile
3. Set `intent_continuity_ack: true` when signed

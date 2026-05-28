# Visual Semantics Principles v0

Evidence base: Triumph Manipulator calibration loop v1 (master hot).

## P1 — Semantic copy is necessary but insufficient

Blueprint `01-master-hot-general.md` specified correct **words**. v4 index hero still failed because Factory implemented **wrong visual hierarchy** (fleet, fake rate, 6 feature lines). v5 succeeded when **zoning and density** changed, not when semantics alone were «more correct».

## P2 — Capability must be scannable in <5 seconds

Doctrine and calibration agree: user must extract **5 т / 3 т / 14 м** without reading paragraphs. Implementation = compact spec list + dark overlay on photo — not six `hero__features` lines.

## P3 — One machine, one focal CTA color

MODE 1 locks forbid fleet framing and fake hero pricing. Visual semantics adds: **one primary red CTA** per viewport; secondary task CTAs use lower visual weight.

## P4 — Zone before volume

Master hot needs qualification density — but **in zones** (`hero__main` → `hero__aside` → `hero__lower`), not one flat pile. G2 v5 lower band is intentional separation; G0 failed because everything competed in one block.

## P5 — Trust mode is a product decision

Substituting operational proof for 4.9 ★ is not «wrong copy» — it is **`trust_mode` drift** that must be explicit. Factory must not silently choose; ORCA pack must set `trust_mode`.

## P6 — Mobile-critical overrides desktop layout

PPC instance `call-first` + mobile doctrine means `mobile_critical` can require **tel before form** even when desktop uses `grid_form_aside`. Triumph v5: **not yet aligned** — documented risk, not fixed in v0 docs.

## P7 — Productive drift should be preserved in packs

Inline form, cargo cards, bg overlay, specs-as-icons are **productive**. ORCA must encode them so future operators do not «restore» v4 anti-patterns during cleanup.

## P8 — Destructive drift blocks factory approval

Qualification line removal and multi-ad H1 mismatch are **destructive** until pack documents mitigation (restore notice, H1 strategy per ad variant).

## P9 — No fake conversion science

All mobile and trust effectiveness statements are **hypotheses** unless operator QA or measured data exists. Use **SAFE UNKNOWN**.

## P10 — Human-operated only

Visual semantics fields are reviewed by operators and calibration loops — **not** auto-scored by CLI, **not** enforced by governance engine.

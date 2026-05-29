# Semantic Density Control v1

**Purpose:** prevent destructive hero overload while allowing productive high-density layouts  
**Evidence:** `calibration/triumph-manipulator/ux-observations/hero-evolution-v1.md`, zakaz pack `visual-semantics/semantic-density.md`

---

## Definitions

| Term | Meaning |
|------|---------|
| **Semantic message** | Distinct claim user must parse (spec line, proof item, cargo card, CTA, notice) |
| **Destructive density** | High message count **without zoning** — user cannot extract intent in 5–10 s |
| **Productive density** | High message count **with zoning** — scan phases separated |

---

## Global budgets (default — override per pack with justification)

### Hero zone (first screen + `hero__lower`)

| Element | Max (zakaz-class) | Max (use-case) | Max (B2B/geo) |
|---------|-------------------|----------------|----------------|
| H1 + lead | 2 | 2 | 2 |
| Spec lines | 5 | 5 (or route-specific) | 4–5 |
| Primary CTA surfaces in hero | 1 dominant + 1 call | same | form + call doc CTA |
| Proof items in hero strip | 4 | 3 | 2–3 |
| Cargo cards | 6 (zakaz) | **4–5** | **3–4** |
| Qualification notice | 1 | 1 recommended | 1 |
| **Red accent buttons** (primary) | **≤2** visible in first viewport | ≤2 | ≤2 |
| **Simultaneous semantic messages** | ~22 (zakaz) — **zoned** | **≤16** | **≤14** |

### Page-level (full scroll)

| Element | Max |
|---------|-----|
| FAQ items (above fold pressure) | No hard max — but FAQ must not duplicate entire hero |
| Section H2 competing with hero H1 | 0 above hero |
| Fake pricing blocks | **0** |
| Fleet / autopark claims | **0** on MODE 1 routes |

---

## Field mapping in pack

| Pack field | Budget |
|------------|--------|
| `visual_density` | `low` / `medium` / `medium-high` / `high` |
| `cargo_cards_max` | Hard cap for hero cargo |
| `hero_interactive_max` | Forms + cargo micro-CTAs + modals in hero |
| `compactness_level` | `compact` = icon lines; `standard` = paragraphs discouraged in hero |

---

## Why v4 hero was destructive

**Source:** legacy `triumph-manipulator-landing` / v4 index hero (`screen-01-hero.html`).

| Failure | Mechanism |
|---------|-----------|
| Visual clutter | 6 `hero__features` lines + rate + CTA row — no focal point |
| Semantic overload | Fleet, НДС, hourly rental, geo in one band |
| Fake pricing | `от XXXX ₽/час` — trust destroyer; violates honesty lock |
| Wrong capability | «5-10 тонн» vs PPC 5 т / 3 т |
| Fleet framing | «Свой автопарк» — breaks one-machine doctrine |
| Weak CTA hierarchy | Generic «Оставить заявку» without inline qualification |
| Image competition | Large visual area without parameter clarity |

**Class:** `visual_density: high` + **unstructured** = **destructive**.

---

## Why v6 (zakaz / G2) is productive

**Source:** `workspaces/triumph-manipulator-landing-v6` zakaz stack (from V5 mailer MVP lineage).

| Success | Mechanism |
|---------|-----------|
| Focus hierarchy | H1 → lead → 5 specs → form aside |
| Zoning | `hero__main` / `hero__aside` / `hero__lower` |
| Capability-first | Specs match ad callouts immediately |
| Honest pricing | No fake hero rate — pricing in factors section |
| Task qualification | Cargo cards segment intent (with cap discipline) |
| Compactness | Icon spec list vs paragraph features |

**Class:** `visual_density: high` + **zoned** = **productive**.

**Remaining risk (G2):** lower band still dense (4 proof + 6 cargo) — mobile fold UNKNOWN until device QA.

---

## Reduction levers (productive drift — Factory may apply)

| Lever | Condition |
|-------|-----------|
| Cap cargo at 4 on ≤760px | Pack allows or `cargo_cards_max` |
| Merge redundant proof labels | No meaning change |
| Collapse proof strip on smallest breakpoints | Visual only |
| Move qualification to `hero__lower` top | Pack requires `qualification_line_required` |

---

## Forbidden «simplification»

| Action | Why forbidden |
|--------|---------------|
| Remove specs to «clean design» | Breaks PPC continuity |
| Remove denied tasks | Junk lead risk |
| Add 7th cargo without pack | Density breach |
| Add hero rate for «conversion» | Destructive pattern |

---

## Per-route density targets (generation)

| Route type | Target `visual_density` | Notes |
|------------|-------------------------|-------|
| Master hot (zakaz) | `high` (zoned) | Canonical — do not increase cargo without review |
| Capability (5t, vezdehod) | `medium-high` | Fewer cargo types |
| Use-case | `medium` | Stricter cargo cap |
| B2B (yurlic) | `medium` | Documents over cargo |
| Geo (kray) | `medium` | Avoid city list spam in hero |

---

## Operator checklist (quick)

- [ ] Count hero messages ≤ budget for route type
- [ ] ≤2 red primary buttons in first viewport
- [ ] No fake hero price
- [ ] Zones present (main / aside / lower)
- [ ] `cargo_cards_max` respected in copy draft
- [ ] Mobile critical elements listed — QA scheduled

---

## Related

- [visual-semantic-injection-rules-v1.md](visual-semantic-injection-rules-v1.md)
- [production-pack-readiness-checklist-v1.md](production-pack-readiness-checklist-v1.md)

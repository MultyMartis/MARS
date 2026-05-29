# Hero Hierarchy Model v0

## Zone model (v5 PPC — Triumph zakaz)

```text
.first-screen (bg + overlay)
  └── .hero.hero--v5
        └── .hero__shell
              ├── .hero__main          [scan path tier 1]
              │     ├── .hero__content   H1 → lead → specs
              │     └── .hero__aside     form (CTA column)
              └── .hero__lower         [scan path tier 2]
                    ├── .hero-proof--v5
                    └── .hero__cargo-block
```

Evidence: `current-hero-analysis-v1.md`, partial `v5-ppc/zakaz/screen-01-hero.html` (read-only cite).

## Scan path (desktop)

**Intended:** H1 → geo emphasis → lead → 5 specs → form H2 → submit  
**Secondary:** proof strip → cargo cards  
**Tertiary:** scroll to specs section image

## Why G0 (v4 index) failed

| Failure | Mechanism |
|---------|-----------|
| Overload | 6 feature lines + rate + CTA in one cognitive band |
| Visual competition | `hero__visual-note` vs headline |
| Weak CTA hierarchy | «Оставить заявку» without inline form |
| Fake pricing noise | `hero__rate` before qualification |
| Wrong capability | «5–10 тонн» vs ads |
| Fleet framing | «Свой автопарк» |
| Background conflict | Busy composite; no isolated machine read |

**Visual semantics diagnosis:** `hero_layout_mode: legacy_clutter`, `visual_density: overloaded`, `semantic_focus` violated.

## Why G1→G2 improved

| Improvement | Hierarchy effect |
|-------------|------------------|
| Isolated bg image + gradient | Machine readable; text wins |
| Separated `hero__lower` | Proof/cargo no longer fight H1 |
| Form-first aside | `cta_priority: form`, `cta_weight: primary_dominant` |
| Capability-first list | Specs match ad callouts <5 sec |
| Proof grouping | 4 ops icons — single strip rhythm |
| Specs promoted to anchors | Icons/lines vs paragraphs |
| No fake rate | Trust not undermined before CTA |
| Cargo as qualification | `use_case_fit` without duplicating H1 |

## Remaining weaknesses (G2)

| Issue | Field signal |
|-------|--------------|
| Lower band dense (4+6) | `visual_noise_risk: high` |
| No hero qualification line | `qualification_mode` gap |
| Form may stack below specs on mobile | `mobile_critical` risk |
| Six cargo CTAs | `cta_weight` borderline |

## `hero_priority` by route type

| Route | Recommended |
|-------|-------------|
| master_hot | `capability_first` |
| use_case | `capability_first` + cargo |
| b2b | `qualification_first` or B2B proof |
| price-heavy keyword groups | elevate pricing factors — not hero fake table |

## Hero v2 direction (requirements only)

See `next-evolution/hero-v2-operational-rules-v1.md` — restore qualification, hybrid trust, cap cargo, mobile CTA order.

## SAFE UNKNOWN

Optimal column ratio `1.06fr | 420px` on ultrawide — aesthetic, not calibrated.

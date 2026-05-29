# Cross-Negative Rules v1

**Scope:** Triumph Manipulator route family — Search PPC  
**Freeze:** PPC Exporter Production Baseline v1  
**Date:** 2026-05-29  
**Status:** **Mandatory** pre-export stage

---

## Route family (Triumph — 12 routes)

Cross-negative logic applies across these route slugs:

| # | Route slug | Registry-oriented id |
|---|------------|----------------------|
| 1 | `zakaz` | master hot |
| 2 | `5-tonn` | capability |
| 3 | `bytovki` | use-case |
| 4 | `konteynery` | use-case |
| 5 | `oborudovanie` | use-case |
| 6 | `armatura` | use-case |
| 7 | `kirpich-bloki` | use-case |
| 8 | `fbs-zhbi` | use-case |
| 9 | `stroymaterialy` | use-case |
| 10 | `vezdehod` | capability |
| 11 | `yurlic` | b2b |
| 12 | `kray` | geo |

Semantic family reference: [route-family-freeze-v1/ORCA-ROUTE-FAMILY-FREEZE-v1.md](../route-family-freeze-v1/ORCA-ROUTE-FAMILY-FREEZE-v1.md).

---

## ORCA obligations (mandatory)

Before marking export **READY**, ORCA **must**:

| # | Obligation |
|---|------------|
| 1 | **Build route intersections** — for each group, identify phrases/intents that belong to sibling routes |
| 2 | **Form cross-negative matrix** — group × sibling-route negative tokens (documented artifact or JSON block) |
| 3 | **Export group-level negatives** — negatives land on **group** scope in Commander export |
| 4 | **Reduce intra-campaign competition** — prevent groups from capturing sibling-route intent |

---

## Cross-negative matrix (conceptual)

For group **G** on route **R**, add negatives that block high-confidence sibling-route queries:

```
cross_negatives(G_R) = ⋃_{S ≠ R} intersection(intent(G_R), intent_family(S))
```

**Principles:**

- Negatives are **route-discriminators**, not global junk lists.  
- Prefer phrase-level negatives already in doctrine reject lists before inventing new ones.  
- Do not negate the group's own primary commercial phrases.  
- Logistics siblings (`bytovki`, `konteynery`, `oborudovanie`, …) cross-block generic manipulator rent queries that belong to `zakaz` or `5-tonn`, and vice versa per calibration.

---

## Example (illustrative — not exhaustive)

| Source group | Route | Example cross-negative on sibling intent |
|--------------|-------|---------------------------------------------|
| `grp_*_bytovki` | bytovki | `манипулятор 5 тонн`, `заказать манипулятор` (zakaz bleed) |
| `grp_*_5-tonn` | 5-tonn | `перевозка бытовок`, `доставка бытовок` |
| `grp_*_yurlic` | yurlic | consumer-only «аренда манипулятора» variants without B2B qualifier |
| `grp_*_kray` | kray | hyper-local service queries owned by `zakaz` |

Exact tokens live in JSON `group.negatives` / export mapping — matrix must be **reviewable** before export.

---

## Export readiness gate

| Gate | Requirement |
|------|-------------|
| Cross-negative matrix | Documented or machine-readable for the export run |
| Group negatives in XLSX | Present per Commander template negative columns |
| Human review | Operator confirms no over-negation of primary phrases |
| Hygiene | No legacy project tails — [COMMANDER-HYGIENE-AUDIT-v1.md](COMMANDER-HYGIENE-AUDIT-v1.md) |

**Export READY is blocked** if cross-negative stage skipped.

---

## Calibration evidence

Human session confirmed: cross negatives **improve routing quality** between sibling groups — see [COMMANDER-CALIBRATION-FINDINGS-v1.md](COMMANDER-CALIBRATION-FINDINGS-v1.md) finding #6.

---

## Boundaries

| In scope | Out of scope |
|----------|--------------|
| Cross-route negatives inside Triumph family | Account-level shared negative library automation |
| Group-scoped export | Campaign-wide negative sync product |
| Documentation + JSON/export obligation | Autonomous negative mining |

---

## SAFE UNKNOWN

- Optimal negative breadth per route after live search terms report — operator iterates post-launch (human-only).  
- Whether every group in current JSON instance has full cross-negative coverage — audit per export run.

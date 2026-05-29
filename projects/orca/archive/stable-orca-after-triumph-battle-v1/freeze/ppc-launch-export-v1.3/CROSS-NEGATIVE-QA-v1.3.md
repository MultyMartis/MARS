# Cross-Negative QA v1.3

**Date:** 2026-05-29  
**Rules:** [CROSS-NEGATIVE-RULES-v1.md](../ppc-exporter-production-baseline-v1/CROSS-NEGATIVE-RULES-v1.md)  
**Matrix module:** `tools/exporter-cli/cross-negative-matrix-v1.3.js`

---

## Automated QA result

| Check | Result |
|-------|--------|
| Group negatives present (first ad row / col 68) | **PASS** (12/12 groups) |
| No `грузотакси` legacy tails | **PASS** |
| No global `манипулятор` / `краснодар` / `край` as cross-negative | **PASS** (forbidden list enforced) |

---

## Matrix principles (frozen)

1. Each route has **discriminator tokens** (e.g. `бытовк*`, `контейнер*`, `арматур*`).  
2. Group **G** on route **R** receives: doctrine negatives from JSON **plus** all sibling-route tokens (**S ≠ R**).  
3. **5-tonn** and **zakaz** also receive consolidated hot-route block (capability / use-case bleed).  
4. **zakaz** does not export route-owned tokens that would choke broad hot intent — matrix uses discriminators only.  
5. **kray** contributes `межгород` only — not blanket «край» on other groups.

---

## Route discriminators

| Route | Tokens (exported on other groups) |
|-------|-----------------------------------|
| bytovki | `бытовк*` |
| konteynery | `контейнер*` |
| stroymaterialy | `стройматериал*` |
| oborudovanie | `оборудован*` |
| armatura | `арматур*` |
| kirpich-bloki | `кирпич*`, `блок*` |
| fbs-zhbi | `фбс`, `жби` |
| vezdehod | `вездеход`, `6х6`, `6x6` |
| yurlic | `юрлиц*`, `безнал`, `документ*` |
| kray | `межгород` |
| 5-tonn / zakaz | (no own discriminator — receive sibling union / hot block) |

**Cross count per group:** 15–21 tokens after merge with JSON doctrine negatives (e.g. `3 тонны`, `эвакуатор` on 5-tonn).

---

## Examples (5-tonn group)

Includes sibling route tokens such as: `бытовк*`, `контейнер*`, `арматур*`, `кирпич*`, `блок*`, `фбс`, `жби`, `оборудован*`, `вездеход`, `6х6`, `6x6`, `юрлиц*`, `безнал`, `документ*`, `межгород`, plus JSON doctrine negatives.

**bytovki group** blocks: `контейнер*`, `арматур*`, … (not `бытовк*` on itself).

---

## Human spot-check (required)

- [ ] No over-minus on primary commercial phrases per group  
- [ ] Sibling intent routes to correct landing after live query review  
- [ ] Campaign-level negatives unchanged (metadata row 9)

---

## SAFE UNKNOWN

Optimal negative breadth after 2–4 weeks search terms — operator iteration only; not automated in ORCA.

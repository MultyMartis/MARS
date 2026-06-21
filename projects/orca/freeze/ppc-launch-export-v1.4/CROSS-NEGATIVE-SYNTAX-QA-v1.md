# Cross-Negative Syntax QA v1

**Date:** 2026-05-29  
**Module:** `cross-negative-matrix-v1.4.js`  
**Rules baseline:** [CROSS-NEGATIVE-RULES-v1.md](../ppc-exporter-production-baseline-v1/CROSS-NEGATIVE-RULES-v1.md)

---

## Problem (v1.3)

Commander rejected group negatives containing `*`:

> «В минус-фразах можно использовать только буквы, цифры, пробел, операторы +, -, (, ), кавычки, квадратные скобки…»

**Source:** `cross-negative-matrix-v1.3.js` — route tokens like `бытовк*`, `контейнер*`, `арматур*`.

**Impact:** 12/12 groups failed syntax validation; import blocked or settings ignored.

---

## Fix (v1.4)

| Mechanism | Detail |
|-----------|--------|
| Wildcard ban | `COMMANDER_NEGATIVE_FORBIDDEN_RE` rejects `*` and regex-like chars |
| Stem expansion | `бытовк*` → `бытовка`, `бытовки`, `бытовку`, `бытовок` |
| Template phrases | Route discriminators as full phrases: `перевозка бытовок`, `доставка контейнеров`, … |
| Doctrine merge | JSON `group_negatives.keywords` unchanged (already valid phrases) |
| Validator gate | `validateNegativesCell()` in `_validate-launch-ready-v1.4.js` |

---

## Automated QA result

| Check | v1.3 | v1.4 |
|-------|------|------|
| Groups with `*` in col 68 | 12 | **0** |
| `commander_negative_syntax_pass` | FAIL | **PASS** |
| `no_legacy_gruzotaxi_negatives` | PASS | PASS |
| `group_negatives_present` | PASS | PASS |

**Verdict:** **PASS**

---

## Expansion map (reference)

| v1.3 token | v1.4 expanded forms |
|------------|---------------------|
| `бытовк*` | бытовка, бытовки, бытовку, бытовок |
| `контейнер*` | контейнер, контейнера, контейнеров, контейнеры |
| `стройматериал*` | стройматериал, стройматериалы, стройматериалов |
| `оборудован*` | оборудование, оборудования |
| `арматур*` | арматура, арматуры, арматуру |
| `кирпич*` | кирпич, кирпича, кирпичи |
| `блок*` | блок, блока, блоки, блоков |
| `юрлиц*` | юрлиц, юрлица |
| `документ*` | документы, документов |

Plain tokens (`фбс`, `жби`, `вездеход`, `6х6`, `безнал`, `межгород`) pass through unchanged.

---

## Template SoT alignment

Template v1 sample negatives use **phrase-level** forms without wildcards:

- Group 01: `-перевозка бытовок`
- Group 03: `-перевозка контейнеров`

v1.4 includes these phrase forms via `ROUTE_NEGATIVE_PHRASES` plus expanded stems for sibling-route coverage.

---

## Human spot-check (required)

- [ ] Commander import accepts all group negatives without error dialog  
- [ ] No over-minus on primary commercial phrases per group  
- [ ] Sibling intent routes correctly after 2–4 weeks search terms review  

---

## SAFE UNKNOWN

Optimal morphological coverage for Russian stems — operator may trim post-import based on search query report.

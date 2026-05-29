# Commander Import Findings v1

**Source:** Real Direct Commander import — Triumph Manipulator Search PPC  
**Artifact:** `triumph-sheet1-patch-launch-ready-v1.4.xlsx`  
**Date:** 2026-05-29 (import) · 2026-05-30 (freeze)  
**Type:** Human-operated battle record — **not** automated telemetry

---

## Import result: PASS

Direct Commander принял v1.4 XLSX без структурного отказа. Сущности импортированы в ожидаемых количествах.

---

## Pre-import gates (all PASS)

| Gate | Result |
|------|--------|
| `validation-cli` on JSON | PASS (345 rules) |
| Export v1.4 SUCCESS | PASS (84 rows) |
| `validate:launch-ready-v1.4` | PASS — Commander readiness **READY** |
| XLSX integrity reopen | PASS |
| Duplicate ads = 0 | PASS |
| URL QA (canonical `.html`) | PASS |
| Bid QA (400–600 ₽) | PASS |
| Cross-negative syntax (no `*`) | PASS |
| Campaign metadata fidelity | PASS (promotion URL = root) |

---

## Post-import verification

| Check | Result | Notes |
|-------|--------|-------|
| Groups count | 12 | Match |
| Ads count | 20 | Match — no duplicates per group |
| Keywords count | 64 | Match |
| Region | Краснодарский край | Match |
| Promotion URL | `https://manipulator-triumph.ru/` | Root, not route `.html` |
| Placement | Search | Match template |
| Group negatives | Imported | No syntax rejection after v1.4 fix |
| Landing URLs | `.html` canonical | Spot-check PASS |
| Fastlinks | `manipulator-triumph.ru/*.html` | Readable in UI |
| Bids on phrases | Visible | **After manual campaign strategy setup in UI** |

---

## Critical finding: bids require post-import strategy setup

**Observation:** Ставки на ключевых фразах **не отображались** сразу после импорта.

**Resolution:** Оператор вручную установил стратегию кампании («ручное управление ставками») в UI Direct Commander. После этого ставки из XLSX (col 54, 400–600 ₽) стали видимы.

**Implication:** XLSX transport layer **переносит bid values**, но Commander UI **требует explicit strategy activation** post-import. Закреплено в [CAMPAIGN-SETTINGS-LAYER-v1.md](CAMPAIGN-SETTINGS-LAYER-v1.md).

---

## Critical finding: strategy/budget/schedule not in XLSX

| Setting | XLSX | Commander UI |
|---------|------|--------------|
| Campaign type | Partial (metadata rows) | Confirm |
| Placement (Search) | Yes (R7C8) | Confirm |
| Manual bids strategy | Implied (col 53 = `-`) | **Must activate manually** |
| Weekly / daily budget | **Not in template** | **Set manually** |
| Ad schedule | **Not in template** | **Set manually** |
| Smart bidding | Out of scope | N/A |

---

## Cross-negative import

| Version | Result |
|---------|--------|
| v1.3 (wildcards `*`) | Commander syntax rejection — 12/12 groups failed |
| v1.4 (expanded stems + phrases) | **PASS** — all groups accepted |

Commander error message (v1.3):
> «В минус-фразах можно использовать только буквы, цифры, пробел, операторы +, -, (, ), кавычки, квадратные скобки…»

---

## Hygiene observations

- No legacy `gruzotaxi-triumph.ru` URLs in export  
- No stale template rows (last export row 99)  
- Campaign-level negatives (9 JSON entries) imported  
- Entity IDs cleared for new campaign mode  

---

## Not claimed

- Live ads serving  
- Budget spend or auction performance  
- Search terms report quality  
- Conversion tracking verification  

---

## Operator checklist (post-import — mandatory)

- [x] Import structural PASS  
- [x] Entity counts verified  
- [x] Campaign strategy set manually → bids visible  
- [ ] Budget set intentionally  
- [ ] Schedule set intentionally  
- [ ] Final operator sign-off before launch  
- [ ] Launch approved — **no**

---

## Related QA docs

- [../ppc-launch-export-v1.4/COMMANDER-IMPORT-CHECKLIST-v1.4.md](../ppc-launch-export-v1.4/COMMANDER-IMPORT-CHECKLIST-v1.4.md)  
- [../ppc-launch-export-v1.4/CROSS-NEGATIVE-SYNTAX-QA-v1.md](../ppc-launch-export-v1.4/CROSS-NEGATIVE-SYNTAX-QA-v1.md)  
- [../ppc-launch-export-v1.4/CAMPAIGN-FIDELITY-QA-v1.md](../ppc-launch-export-v1.4/CAMPAIGN-FIDELITY-QA-v1.md)

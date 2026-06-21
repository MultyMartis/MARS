# Commander Import Checklist v1.4

**Date:** 2026-05-29  
**Artifact:** `triumph-sheet1-patch-launch-ready-v1.4.xlsx`  
**Hygiene:** [COMMANDER-HYGIENE-AUDIT-v1.md](../ppc-exporter-production-baseline-v1/COMMANDER-HYGIENE-AUDIT-v1.md)

---

## Pre-import (machine)

- [x] `validation-cli` PASS on `triumph-s-tier-draft-v1.json`
- [x] Export v1.4 SUCCESS
- [x] `validate:launch-ready-v1.4` PASS
- [x] XLSX integrity reopen PASS
- [x] Duplicate ads = 0
- [x] URL QA PASS (canonical `.html`, no `gruzotaxi-triumph.ru`)
- [x] Bid QA PASS (400–600 ₽)
- [x] Cross-negative syntax PASS (no `*`)
- [x] Campaign metadata fidelity PASS (promotion URL root, placement search)

**Commander readiness (automated):** **READY**

---

## Import steps (human)

1. Open **Direct Commander** (desktop).  
2. **Импорт** → select `triumph-sheet1-patch-launch-ready-v1.4.xlsx`.  
3. Confirm template: Search (`Места показа: search`), **ручное управление ставками**.  
4. Confirm **Объект продвижения** = `https://manipulator-triumph.ru/` (not a route `.html`).  
5. New campaign mode — entity IDs cleared in export.  
6. After import, verify counts:

| Entity | Expected |
|--------|----------|
| Groups | 12 |
| Ads | 20 |
| Keywords | 64 |
| Region | Краснодарский край |

7. Confirm **минус-фразы на группу** import without syntax error (no `*` tokens).  
8. Spot-check **ставки** on phrases (400–600 ₽, variation per group).  
9. Spot-check **ссылки** and fastlinks (`manipulator-triumph.ru/*.html`).  
10. Set **бюджет / расписание** in Commander UI (not in XLSX).  
11. **Do not** enable campaign / ads until operator sign-off.

---

## Post-import (human — required)

- [ ] Campaign type + placement match template calibration  
- [ ] Promotion URL = site root  
- [ ] Bids visible on all 64 phrases  
- [ ] No duplicate ads per group  
- [ ] Group negatives active — no Commander syntax rejection  
- [ ] Schedule / budget intentional  
- [ ] Fastlink `||` encoding readable in UI  

---

## Explicit prohibitions

- **Do not** launch ads from this checklist alone  
- **Do not** push git from import session  
- **Do not** edit ad copy / URLs / phrases in Commander unless separate change request  

---

## Related QA docs

- [XLSX-LAUNCH-READY-v1.4.md](XLSX-LAUNCH-READY-v1.4.md)  
- [TEMPLATE-DIFF-AUDIT-v1.md](TEMPLATE-DIFF-AUDIT-v1.md)  
- [CAMPAIGN-FIDELITY-QA-v1.md](CAMPAIGN-FIDELITY-QA-v1.md)  
- [GROUP-FIDELITY-QA-v1.md](GROUP-FIDELITY-QA-v1.md)  
- [CROSS-NEGATIVE-SYNTAX-QA-v1.md](CROSS-NEGATIVE-SYNTAX-QA-v1.md)

---

## Audit record

| Field | Value |
|-------|-------|
| Export run | 2026-05-29 |
| Operator | _pending_ |
| Commander import | _pending_ |
| Launch approved | _no_ |

# Commander Import Checklist v1.3

**Date:** 2026-05-29  
**Artifact:** `triumph-sheet1-patch-launch-ready-v1.3.xlsx`  
**Hygiene:** [COMMANDER-HYGIENE-AUDIT-v1.md](../ppc-exporter-production-baseline-v1/COMMANDER-HYGIENE-AUDIT-v1.md)

---

## Pre-import (machine)

- [x] `validation-cli` PASS on `triumph-s-tier-draft-v1.json`
- [x] Export v1.3 SUCCESS
- [x] `validate:launch-ready-v1.3` PASS
- [x] XLSX integrity reopen PASS
- [x] Duplicate ads = 0
- [x] URL QA PASS (canonical `.html`, no `gruzotaxi-triumph.ru`)
- [x] Bid QA PASS
- [x] Cross-negative QA PASS

**Commander readiness (automated):** **READY**

---

## Import steps (human)

1. Open **Direct Commander** (desktop).  
2. **Импорт** → select `triumph-sheet1-patch-launch-ready-v1.3.xlsx`.  
3. Confirm template: Search, **ручное управление ставками**.  
4. New campaign mode — entity IDs cleared in export.  
5. After import, verify counts:

| Entity | Expected |
|--------|----------|
| Groups | 12 |
| Ads | 20 |
| Keywords | 64 |
| Region | Краснодарский край |

6. Spot-check **ставки** on phrases (400–600 ₽, variation per group).  
7. Spot-check **минус-фразы на группу** on each group.  
8. Spot-check **ссылки** and fastlinks (`manipulator-triumph.ru/*.html`).  
9. **Do not** enable campaign / ads until operator sign-off.

---

## Post-import (human — required)

- [ ] Bids visible on all 64 phrases  
- [ ] No duplicate ads per group  
- [ ] Group negatives active  
- [ ] Schedule / budget / account settings intentional  
- [ ] Fastlink `||` encoding readable in UI  

---

## Explicit prohibitions

- **Do not** launch ads from this checklist alone  
- **Do not** push git from import session  
- **Do not** edit ad copy / URLs in Commander unless separate change request  

---

## Related QA docs

- [LAUNCH-XLSX-EXPORT-v1.3.md](LAUNCH-XLSX-EXPORT-v1.3.md)  
- [BID-QA-v1.3.md](BID-QA-v1.3.md)  
- [CROSS-NEGATIVE-QA-v1.3.md](CROSS-NEGATIVE-QA-v1.3.md)

---

## Audit record

| Field | Value |
|-------|-------|
| Export run | 2026-05-29 |
| Operator | _pending_ |
| Commander import | _pending_ |
| Launch approved | _no_ |

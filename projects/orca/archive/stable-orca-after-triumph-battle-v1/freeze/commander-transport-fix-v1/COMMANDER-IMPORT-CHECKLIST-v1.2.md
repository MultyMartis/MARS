# COMMANDER IMPORT CHECKLIST v1.2

**Label:** `orca-commander-import-checklist-v1.2`  
**Date:** 2026-05-29  
**XLSX:** `tools/exporter-cli/output/triumph-sheet1-patch-full-cycle-v1.2.xlsx`  
**Pre-import QA:** `npm run validate:no-duplicate-ads-v1.2` must PASS

---

## Before import (local)

- [ ] Validation-cli report exists and export was not blocked
- [ ] `validate:no-duplicate-ads-v1.2` — all PASS
- [ ] Open XLSX in Excel — no repair dialog
- [ ] Spot-check row 16: ad row — headlines + URL, **empty phrase**
- [ ] Spot-check first keyword row in group: phrase filled, **empty headlines**
- [ ] ID columns empty on export rows (new-campaign mode)
- [ ] No rows below row 99

---

## Expected Commander counts (human verify)

| Entity | Expected |
|--------|----------|
| Groups | 12 |
| Ads | 20 |
| Keyword phrases | 64 |

---

## Post-import verify

- [ ] No duplicate ads per group (same headline triple + URL)
- [ ] `grp_fc12_zakaz` — 2 ads, homepage URL `https://manipulator-triumph.ru/`
- [ ] Region shows **Краснодарский край**
- [ ] No image/creative popup on search ads
- [ ] Fastlinks readable (may need manual polish for `||` encoding)

---

## If counts wrong

1. Do **not** edit JSON for transport bugs — fix exporter transport model.
2. Compare with [DUPLICATE-ADS-AUDIT-v1.md](../commander-url-sync-v1/DUPLICATE-ADS-AUDIT-v1.md).
3. Halt import if legacy `gruzotaxi-triumph.ru` URLs appear.

---

## Explicitly out of scope

- Do **not** launch campaigns from this checklist
- Do **not** treat transport QA as launch approval

# Sample run — Commander Import Feedback Fix v0.1

**Phase:** ORCA Commander Import Feedback Fix v0.1  
**NOT** production exporter · **NOT** Commander automation · human review required

---

## Prerequisites

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm install
```

Validation report must allow export (`export_allowed: true`).

---

## Command

```bash
npm run export:sheet1-patch:feedback
```

Or:

```bash
node sheet1-patch-export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  fixtures/validation-report.export-allowed.fixture.json \
  output/triumph-sheet1-patch-feedback-v0.1.xlsx
```

---

## Expected console output

- Label: `ORCA Commander Import Feedback Fix v0.1 — SUCCESS`
- `Metadata patched: campaigns.campaign_type, campaigns.campaign_negatives, campaigns.promotion_url`
- `Rows patched: 15`
- `Stale rows neutralized: 103` with `masked cells: 515` (approx.)
- `ZIP preserve check: PASS`
- `Integrity: INTEGRITY_OK`

---

## Spot-check in Excel

| Check | Row / cell | Expected |
|-------|------------|----------|
| Campaign type | Row 7 col 5 | `Единая перфоманс-кампания` |
| Minus phrases | Row 9 col 5 | `-вакансии -работа …` (from JSON) |
| Promotion URL | Row 11 col 5 | `https://triumph-krd.ru/manipulyator-5t` |
| Group 1 number | Row 16 col 6 | `1` |
| Group 2 number | Row 19 col 6 | `2` |
| Group 5 number | Row 29 col 6 | `5` |
| Group name | Row 16 col 5 | `01 — Манипулятор 5 тонн` |
| Status cols | Row 16 cols 56–57 | empty |
| Stale row | Row 31 cols 5, 8 | `-` (mask) |
| No autotarget | Row 16 col 8 | real phrase, not `---autotargeting` |

---

## Commander import trial (human)

1. Open XLSX in Excel — confirm no repair dialog  
2. Import via Direct Commander  
3. Compare group tree vs checklist in [commander-import-observations-v0.md](commander-import-observations-v0.md)  
4. Record results in operator notes (not automated)

---

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | Patch + metadata + cleanup + preserve + integrity passed |
| 1 | Blocked (precheck, patch, preserve, integrity) |

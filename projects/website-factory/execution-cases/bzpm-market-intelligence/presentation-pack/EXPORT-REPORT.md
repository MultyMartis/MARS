# EXPORT REPORT — BZPM MI Presentation Pack

**Generation date:** 2026-06-14  
**Generator:** `generate_bzpm_pack.py`  
**Authority:** BZPM-COMPETITOR-REGISTRY-v2.md · BZPM-MARKET-INTELLIGENCE-MASTER-REPORT-v1.md · BZPM-OPERATOR-INSIGHTS-v1.md  

---

## Generated Files

| # | File | Sheets | Charts | Tables |
| --- | --- | ---: | ---: | ---: |
| 01 | BZPM-MI-DASHBOARD.xlsx | 5 | 5 | 5 |
| 02 | BZPM-COMPETITOR-REGISTRY.xlsx | 1 | 0 | 1 |
| 03 | BZPM-CORE-RESEARCH-SET.xlsx | 4 | 0 | 4 |
| 04 | BZPM-OPERATOR-INSIGHTS.xlsx | 4 | 0 | 4 |
| 05 | BZPM-MANUAL-REVIEW-CHECKLIST.xlsx | 1 | 0 | 1 |
| 06 | BZPM-MI-PACKAGE-SUMMARY.xlsx | 1 | 0 | 0 |
| | **Total** | **16** | **5** | **15** |

Supporting files: `README.md`, `EXPORT-REPORT.md`, `generate_bzpm_pack.py`

---

## Workbook Structure

### BZPM-MI-DASHBOARD.xlsx
| Sheet | Content |
| --- | --- |
| 01_Overview | Key metrics, wave completion status |
| 02_Geography | Entity counts by geography + bar chart |
| 03_Tiers | Approved registry tier distribution + bar chart |
| 04_SERP | W3S visibility leaders + bar chart |
| 05_Program_Status | Status group pie chart + regional coverage bar chart |

### BZPM-COMPETITOR-REGISTRY.xlsx
| Sheet | Content |
| --- | --- |
| Full_Registry | 126 entities — ID, Company, Website, Tier, Geography, Coverage Zone, Type, Source Waves, Status |

### BZPM-CORE-RESEARCH-SET.xlsx
| Sheet | Rows | Content |
| --- | ---: | --- |
| 01_Approved_Registry | 46 | Approved COMP-BZPM entities |
| 02_Strong_Expansion | 21 | Strong expansion candidates |
| 03_Native_Benchmark_Group | 6 | W3Y operator benchmark list |
| 04_SERP_Leaders | 13 | Top SERP visibility entities |

### BZPM-OPERATOR-INSIGHTS.xlsx
| Sheet | Rows | Content |
| --- | ---: | --- |
| 01_Highlights | 7 | Operator highlight registry |
| 02_Patterns | 10 | Observed UX/catalog patterns |
| 03_FIM_Registry | 7 | Future investigation markers |
| 04_Benchmark_Group | 6 | Native benchmark group |

### BZPM-MANUAL-REVIEW-CHECKLIST.xlsx
| Sheet | Rows | Content |
| --- | ---: | --- |
| Review_Checklist | 33 | Tier A + Strong Expansion + Native Benchmark (deduplicated) |

### BZPM-MI-PACKAGE-SUMMARY.xlsx
| Sheet | Content |
| --- | --- |
| Executive_Summary | Client-facing market, geography, tier, key competitors, research coverage |

---

## Charts Created

All charts are in **BZPM-MI-DASHBOARD.xlsx**:

| # | Chart | Sheet | Type |
| ---: | --- | --- | --- |
| 1 | Entities by Geography | 02_Geography | Bar |
| 2 | Entities by Tier (Approved) | 03_Tiers | Bar |
| 3 | SERP Visibility Leaders | 04_SERP | Bar |
| 4 | Approved vs Expansion vs Deferred | 05_Program_Status | Pie |
| 5 | Regional Coverage | 05_Program_Status | Bar |

---

## Source Validation

### Registry v2 (TASK 3 table)

| Metric | Parsed | Expected (authority) | Match |
| --- | ---: | ---: | --- |
| Total canonical entities | 126 | 126 | ✓ |
| Approved | 46 | 46 | ✓ |
| Strong Expansion | 21 | 21 | ✓ |
| Possible Expansion | 22 | 22 | ✓ |
| Deferred | 26 | 26 | ✓ |
| Excluded | 11 | 11 | ✓ |

### Master Report v1 statistics cross-check

| Metric | Registry v2 | Master Report | Match |
| --- | ---: | ---: | --- |
| Approved registry | 46 | 46 | ✓ |
| Strong expansion | 21 | 21 | ✓ |
| Possible expansion | 22 | 22 | ✓ |
| Deferred pool | 26 | 26 | ✓ |
| Excluded pool | 11 | 11 | ✓ |
| Canonical entities | 126 | 126 | ✓ |

### Merge table (TASK 1) row count
126 data rows — consistent with TASK 3 registry table.

### Mismatches
**None detected** between parsed registry data and authority statistics in Registry v2 and Master Report v1.

### Notes (not mismatches)
- W2.5 historical deferred count (21) differs from W3X consolidated deferred pool (26) — expected; W3X includes expansion-queue deferrals (CAN-EXP-044…048) and W2.5 exclusions merged into deferred canon.
- Operator Manual Review Notes (2026-06-14) cited in W3Y but **not committed in-repo** (SAFE UNKNOWN per authority files).

---

## Export Summary

| Item | Value |
| --- | --- |
| Excel workbooks | 6 |
| Total worksheets | 16 |
| Total charts | 5 |
| Total Excel tables | 15 |
| Registry entities exported | 126 |
| Manual review checklist rows | 33 |
| Operator insight rows (all sheets) | 30 |
| Formatting applied | Headers, borders, zebra striping, freeze panes, auto-filter, conditional formatting (Core Research Set), data validation dropdowns (Checklist) |

**Packaging complete.** No W4 work initiated.

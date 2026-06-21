# BZPM MI Presentation Pack

**Program:** BZPM Market Intelligence  
**Stage:** Presentation & Packaging Layer  
**Status:** W3X + W3Y Approved  
**Generation date:** 2026-06-14  

---

## Purpose

Professional presentation package derived from approved BZPM Market Intelligence research. Suitable for:

1. **Internal BZPM research archive** — structured Excel artifacts alongside markdown authority files
2. **Executive review** — dashboard and package summary for management-facing review
3. **Website Factory reference** — reusable competitor and market context for future delivery work
4. **Catalog UX Intelligence foundation** — operator insights and benchmark group preserved for downstream waves

This pack is **packaging only**. It does not add research, modify registry conclusions, or perform intelligence extraction.

---

## Source Files (Authority)

| File | Role |
| --- | --- |
| `../BZPM-COMPETITOR-REGISTRY-v2.md` | Canonical entity registry (126 entities) |
| `../BZPM-MARKET-INTELLIGENCE-MASTER-REPORT-v1.md` | Master report baseline, SERP leaders, program state |
| `../BZPM-OPERATOR-INSIGHTS-v1.md` | W3Y operator highlights, patterns, FIM, benchmark group |

Repository markdown files have priority over chat or session memory.

---

## Generated Files

| File | Purpose |
| --- | --- |
| `BZPM-MI-DASHBOARD.xlsx` | Executive summary dashboard with charts |
| `BZPM-COMPETITOR-REGISTRY.xlsx` | Full competitor registry (all statuses) |
| `BZPM-CORE-RESEARCH-SET.xlsx` | Core approved, strong expansion, benchmark, SERP leaders |
| `BZPM-OPERATOR-INSIGHTS.xlsx` | Operator discoveries from W3Y |
| `BZPM-MANUAL-REVIEW-CHECKLIST.xlsx` | Operator review workspace with dropdowns |
| `BZPM-MI-PACKAGE-SUMMARY.xlsx` | Client-facing lightweight summary (no internal IDs) |

---

## Intended Use

### BZPM-MI-DASHBOARD.xlsx
Open for executive overview: entity counts, geography, tiers, SERP visibility, program status, regional coverage charts.

### BZPM-COMPETITOR-REGISTRY.xlsx
Filter and sort the full 126-entity universe. Use for registry lookups, status triage, and expansion queue review.

### BZPM-CORE-RESEARCH-SET.xlsx
Focus set for deep review: 46 approved entities, 21 strong expansion candidates, 6 native benchmark companies, SERP leaders.

### BZPM-OPERATOR-INSIGHTS.xlsx
Preserve W3Y operator observations — patterns, investigation markers, benchmark attention list.

### BZPM-MANUAL-REVIEW-CHECKLIST.xlsx
Working sheet for operator review of Tier A OEM, Strong Expansion, and Native Benchmark Group (33 unique companies). Dropdowns: Opened, Interesting, Keep (Yes/No); Priority (High/Medium/Low).

### BZPM-MI-PACKAGE-SUMMARY.xlsx
Share with BZPM management — market, geography, tier overview, key competitors, research coverage. No internal IDs or technical notes.

---

## Regeneration

```powershell
py presentation-pack/generate_bzpm_pack.py
```

Script: `generate_bzpm_pack.py` — parses authority markdown and rebuilds all workbooks.

---

## Scope Boundaries

- **In scope:** Formatting, filtering, charts, packaging existing approved data
- **Out of scope:** New research, registry edits, market conclusion changes, UX analysis, W4 work

---

## Related Documentation

- Export details: `EXPORT-REPORT.md`
- Registry authority: `../BZPM-COMPETITOR-REGISTRY-v2.md`
- Master report: `../BZPM-MARKET-INTELLIGENCE-MASTER-REPORT-v1.md`

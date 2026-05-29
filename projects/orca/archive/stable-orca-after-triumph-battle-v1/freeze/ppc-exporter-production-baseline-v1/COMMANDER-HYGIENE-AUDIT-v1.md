# Commander Hygiene Audit v1

**When:** Before export **READY** (after validation, with cross-negatives built)  
**Freeze:** PPC Exporter Production Baseline v1  
**Date:** 2026-05-29  
**Type:** Human-operated checklist — **not** automated enforcement product

---

## Purpose

Catch legacy and transport artifacts that pass schema validation but fail Commander import or pollute live structure.

Execute **every** item before treating XLSX as production-ready.

---

## Checklist

| # | Check | Pass criteria | Fail action |
|---|-------|---------------|-------------|
| H1 | **Legacy URLs** | No `gruzotaxi-triumph.ru`, no pre-sync slug paths, all URLs canonical `.html` on `manipulator-triumph.ru` | Halt — fix JSON per [commander-url-sync-v1](../commander-url-sync-v1/) |
| H2 | **Legacy negatives** | No old-project negative tails, no deprecated global lists | Remove / replace from JSON |
| H3 | **Old project tails** | No stale campaign names, group labels, or ID columns from prior accounts | Clear IDs for new-campaign export mode |
| H4 | **Old display paths** | Display URL = short slug only; no domain composite | Fix mapping / JSON |
| H5 | **Zero bids** | No `0` in bid columns | Apply [BID-MANAGEMENT-RULES-v1.md](BID-MANAGEMENT-RULES-v1.md) |
| H6 | **Wrong strategy artifacts** | No RSYA rows, retargeting cols, autotarget-only groups on Search manual template | Remove unsupported rows |
| H7 | **Duplicate ads** | `validate:no-duplicate-ads-v1.2` PASS; no keyword×ad multiplication | Fix exporter transport — do not patch XLSX by hand |
| H8 | **Invalid regions** | Region col = **Краснодарский край** on data rows (per full-cycle baseline) | Fix region mapping |
| H9 | **Stale sheet rows** | No data below last patched row (baseline: no rows below ~99) | Re-export from template v1 |
| H10 | **Image / creative pollution** | No image URLs on search text rows | Re-export v1.2 |
| H11 | **Fastlink encoding** | Fastlinks present; `||` encoding acceptable or flagged for human polish | Note in QA — not a block if import succeeds |
| H12 | **Cross-negatives present** | Group negatives exported per [CROSS-NEGATIVE-RULES-v1.md](CROSS-NEGATIVE-RULES-v1.md) | Block READY |

---

## Execution order

```
validation-cli PASS
    → cross-negative matrix built
    → hygiene audit (this doc) — all PASS
    → export v1.2
    → validate:no-duplicate-ads-v1.2 PASS
    → human Commander import checklist
```

---

## Evidence sources

| Topic | Reference |
|-------|-----------|
| URL sync | [commander-url-sync-v1/URL-EXPORT-VALIDATION-v1.md](../commander-url-sync-v1/URL-EXPORT-VALIDATION-v1.md) |
| Duplicate ads | [commander-transport-fix-v1/DUPLICATE-ADS-FIX-REPORT-v1.md](../commander-transport-fix-v1/DUPLICATE-ADS-FIX-REPORT-v1.md) |
| Import checklist | [commander-transport-fix-v1/COMMANDER-IMPORT-CHECKLIST-v1.2.md](../commander-transport-fix-v1/COMMANDER-IMPORT-CHECKLIST-v1.2.md) |
| Region fix | `tools/exporter-cli/commander-region-fix-v0.6.md` |

---

## Audit record (operator)

| Field | Value |
|-------|-------|
| Run date | |
| Operator | |
| JSON instance hash | |
| XLSX output path | |
| Failed checks (if any) | |
| Resolution | |

---

## Boundaries

- Hygiene audit ≠ launch approval  
- Automated scripts cover **subset** (duplicate ads, integrity reopen) — human still runs H1–H4, H10–H12  
- No claim of continuous monitoring — point-in-time pre-export only

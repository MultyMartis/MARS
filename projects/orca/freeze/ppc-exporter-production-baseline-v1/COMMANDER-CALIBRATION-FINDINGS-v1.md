# Commander Calibration Findings v1

**Source cycle:** ORCA → JSON → Exporter v1.2 → XLSX → Direct Commander → Human QA  
**Freeze:** PPC Exporter Production Baseline v1  
**Date:** 2026-05-29  
**Type:** Human calibration record — **not** automated telemetry

---

## Findings (frozen)

### 1. URL synchronization required

Canonical `.html` URLs on `https://manipulator-triumph.ru/` must match JSON, exporter fastlink table, and Commander import. Legacy slug URLs cause wrong landing routing.

**Upstream:** [commander-url-sync-v1](../commander-url-sync-v1/)  
**Gate:** Hygiene audit H1 — [COMMANDER-HYGIENE-AUDIT-v1.md](COMMANDER-HYGIENE-AUDIT-v1.md)

---

### 2. Duplicate ads — root cause: old transport model

Pre–v1.2 exporter multiplied keyword rows with ad rows, producing duplicate ads per group in Commander.

**Fix:** Transport split v1.2 — separate AD rows and KEYWORD rows.  
**Evidence:** [commander-transport-fix-v1/DUPLICATE-ADS-FIX-REPORT-v1.md](../commander-transport-fix-v1/DUPLICATE-ADS-FIX-REPORT-v1.md)  
**QA:** `npm run validate:no-duplicate-ads-v1.2` — **PASS**

---

### 3. Exporter v1.2 validated

Full-cycle export against `triumph-s-tier-draft-v1.json` with live validation report binding. Integrity reopen OK. Expected entity counts align with import checklist (12 groups · 20 ads · 64 phrases).

**Doc:** [EXPORTER-V1.2-APPROVAL-v1.md](EXPORTER-V1.2-APPROVAL-v1.md)

---

### 4. Commander import PASS

Human-operated Direct Commander import completed without structural rejection. Counts verified post-import per [COMMANDER-IMPORT-CHECKLIST-v1.2.md](../commander-transport-fix-v1/COMMANDER-IMPORT-CHECKLIST-v1.2.md).

**Not claimed:** live ads serving, budget spend, auction performance.

---

### 5. Human QA required

Post-import operator must confirm:

- Bids per [BID-MANAGEMENT-RULES-v1.md](BID-MANAGEMENT-RULES-v1.md)  
- Group negatives live  
- Schedule and account settings intentional  
- Fastlink readability (`||` encoding polish if needed)

ORCA/export path does **not** replace this step.

---

### 6. Cross negatives improve routing quality

Applying route-family cross-negative matrix reduced sibling-group intent bleed in human review. Mandatory before export READY — [CROSS-NEGATIVE-RULES-v1.md](CROSS-NEGATIVE-RULES-v1.md).

---

### 7. Template v1 approved

`triumph-manipulator-commander-template-v1.xlsx` promoted to Commander Search Manual Bids Template SoT — [COMMANDER-TEMPLATE-SOT-v1.md](COMMANDER-TEMPLATE-SOT-v1.md).

Supersedes v0 for all future Search PPC exports.

---

## Residual open items

| Item | Status |
|------|--------|
| Live SERP CPC calibration | **SAFE UNKNOWN** — market-dependent |
| Autobid / smart strategies | **Out of scope** — manual bids only |
| RSYA expansion | **Out of scope** — Search template v1 |
| Continuous drift monitoring | **Not implemented** — human re-audit on change |

---

## Related run artifacts

| Artifact | Path |
|----------|------|
| Full-cycle export summary (v0.6 era) | `ppc/triumph-manipulator/runs/full-cycle-v1/export-summary-v1.md` |
| v1.2 output (local, gitignored) | `tools/exporter-cli/output/triumph-sheet1-patch-full-cycle-v1.2.xlsx` |

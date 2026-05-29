# Exporter v1.2 Approval v1

**Component:** ORCA Commander Transport Split v1.2  
**Path:** `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/`  
**Freeze:** PPC Exporter Production Baseline v1  
**Date:** 2026-05-29  
**Status:** **APPROVED** for Triumph Search PPC production export path

---

## Approval summary

| Field | Value |
|-------|-------|
| **exporter_version** | `orca-exporter-cli-transport-split-v1.2` |
| **Label** | `ORCA Commander Transport Split v1.2` |
| **Entry script** | `sheet1-patch-export.js` |
| **Template base** | `triumph-manipulator-commander-template-v1.xlsx` |
| **Approval type** | Human-validated production baseline — **not** hosted service |

---

## What v1.2 fixes

| Issue (pre-v1.2) | v1.2 behavior |
|------------------|---------------|
| Keyword × ad row multiplication | Separate **AD** rows and **KEYWORD** rows |
| Duplicate ads in Commander | Eliminated — validated by post-export script |
| Col 1 «Доп. объявление группы» | `+` on 2nd+ ad in group; empty on keyword rows |

Design: [commander-transport-fix-v1/TRANSPORT-FIX-DESIGN-v1.md](../commander-transport-fix-v1/TRANSPORT-FIX-DESIGN-v1.md)

---

## Validation evidence

| Check | Command / artifact | Result |
|-------|-------------------|--------|
| No duplicate ads QA | `npm run validate:no-duplicate-ads-v1.2` | **PASS** |
| Full-cycle export | `npm run export:sheet1-patch:full-cycle-v1.2` | **SUCCESS** |
| XLSX integrity reopen | `xlsx-integrity-check.js` (in export flow) | **INTEGRITY_OK** |
| Entity counts | 12 groups · 20 ads · 64 phrases | Matches import checklist |
| Commander import | Human session | **PASS** — see calibration findings |

Report: [commander-transport-fix-v1/DUPLICATE-ADS-FIX-REPORT-v1.md](../commander-transport-fix-v1/DUPLICATE-ADS-FIX-REPORT-v1.md)

---

## Production commands (frozen reference)

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm run export:sheet1-patch:full-cycle-v1.2
npm run validate:no-duplicate-ads-v1.2
```

**Prerequisites:**

1. `validation-cli` report present — export not blocked  
2. Cross-negatives built — [CROSS-NEGATIVE-RULES-v1.md](CROSS-NEGATIVE-RULES-v1.md)  
3. Hygiene audit — [COMMANDER-HYGIENE-AUDIT-v1.md](COMMANDER-HYGIENE-AUDIT-v1.md)

---

## Governance rules

| Rule | Detail |
|------|--------|
| Exporter stays dumb transport | No PPC logic invention in export layer |
| JSON SoT | Meaning changes only in JSON + doctrine |
| Blocked export | Never hand-patch XLSX to bypass exporter — fix transport model |
| Template revision | Pin v1 — [COMMANDER-TEMPLATE-SOT-v1.md](COMMANDER-TEMPLATE-SOT-v1.md) |
| Output artifacts | `output/*.xlsx` gitignored — not committed SoT |

---

## Explicit non-approval (honesty)

| Not approved | Notes |
|--------------|-------|
| Autonomous launch | Human only |
| Bid optimization engine | [BID-MANAGEMENT-RULES-v1.md](BID-MANAGEMENT-RULES-v1.md) — human Commander |
| n8n / scheduled export | Future lane — isolated |
| Runtime orchestration | **Not in repo** |

---

## Supersedes

| Version | Status |
|---------|--------|
| Exporter prototype v0 / v0.x notes | Historical — do not use for new production exports |
| v1.1 full-cycle (pre-split) | Superseded by v1.2 for Commander import |
| **v1.2** | **Current production baseline** |

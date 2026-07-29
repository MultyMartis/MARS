# SOURCE GAP MANIFEST v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A  
**Date:** 2026-07-30  
**Verdict:** **SOURCE DROP REQUIRED** — exact JSON baseline generation **blocked**

---

## 1. Search scope (executed)

| Location | Result |
|----------|--------|
| `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\` | **Absent** before this phase; drop dirs created empty |
| `X:\AI MARS STORAGE\incoming\` (top-level + name filter) | No Sales-Manager / Leads.DB / Leads_Manager matches |
| `projects/iseo-sales-manager-bot/baselines/` | Did not exist before this phase |
| `projects/iseo-sales-manager-bot/` project-local inputs | No raw/sanitized workflow or XLSX |

**Not searched:** arbitrary disks, chat upload caches outside approved roots, deprecated C:/D:/E: MARS roots.

---

## 2. Expected sources — status

| # | Expected source | Status | Canonical role |
|---|-----------------|--------|----------------|
| 1 | Sales-Manager-v1 export | **MISSING** | Historical graph evidence |
| 2 | Sales-Manager-v2 export | **MISSING** | Primary Operational patch baseline |
| 3 | RAW workbook (`MetaBOT -Leads.DB.xlsx` or equiv.) | **MISSING** | Schema evidence only |
| 4 | CLEAN workbook (`MetaBOT -Leads_Manager.DB.xlsx` or equiv.) | **MISSING** | Schema evidence only |
| 5 | Telegram examples | **MISSING** | UX evidence (Phase 2 contracts used) |
| 6 | Phase 2 project documentation | **PRESENT** | Architecture authority for Phase 3A specs |
| 7 | MetaBOT Admin sanitized baseline | **PRESENT** (pattern source) | Admin patch pattern — not Sales Manager JSON |

---

## 3. Blocked artifacts

Do **not** invent. Regeneration requires operator drop + sanitization:

- `Sales-Manager-v1.sanitized.json`
- `Sales-Manager-v2.sanitized.json`
- Exact node-ID-level V1/V2 diff from live exports
- `RAW-SHEET-SCHEMA-BASELINE-v1.md` / `CLEAN-SHEET-SCHEMA-BASELINE-v1.md` from real XLSX headers
- `SHEET-DATA-QUALITY-FINDINGS-v1.md` from real row forensics

---

## 4. Required operator drop path

```
X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\raw\
```

Recommended filenames:

- `Sales-Manager-v1.json` (or `Sales-Manager-v1 json.txt`)
- `Sales-Manager-v2.json` (or `Sales-Manager-v2 json.txt`)
- `MetaBOT-Leads.DB.xlsx` (RAW)
- `MetaBOT-Leads_Manager.DB.xlsx` (CLEAN)

Sanitized staging:

```
X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\sanitized\
```

Repo promotion (sanitized only):

```
projects/iseo-sales-manager-bot/baselines/
```

---

## 5. What Phase 3A proceeds with

Implementation package under `implementation/` is derived from:

- Phase 2 architecture + plans (repo-evidenced);
- documented Sales-Manager-v2 **logical** source graph (OPERATIONAL-INDEX / N8N-CHANGE-PLAN);
- MetaBOT Programmer grammar + Admin sanitized pattern inventory.

**SAFE UNKNOWN until drop:** live node IDs, credential binding names, exact workbook document IDs, active-state parity, real header drift vs LEAD-DATA-MODEL-v1.

---

*No secrets, PII, or unsanitized JSON committed in this phase.*

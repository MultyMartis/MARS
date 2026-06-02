# Database Metadata — ocStore 3.0.3.8 (rs.2)

**Baseline:** `baselines/ocstore-3038-rs2/`  
**Generated:** 2026-05-30 (OCPilot Run 3.5)  
**Scope:** metadata only — **no** full database dump in `database/`

---

## Schema source

| Field | Value |
|-------|-------|
| Primary source | `files/install/opencart.sql` (promoted from canonical ZIP) |
| Source type | Vendor install seed SQL (pre-install bundle) |
| File size | 192 868 bytes |
| Location in baseline | `baselines/ocstore-3038-rs2/files/install/opencart.sql` |
| Copied to `database/` | **no** — metadata references install artifact only |

---

## Install SQL detected

| Observation | Value |
|-------------|-------|
| `CREATE TABLE` statements | 136 |
| `INSERT INTO` statements | 110 |
| Default table prefix | `oc_` (inferred from table names) |
| Table set delta vs 3039-rs1 | **0** tables unique to either version (same 136 table names) |

### Sample tables (first / last alphabetically in file)

- First observed: `oc_address`, `oc_googleshopping_target`, `oc_api`, …
- Last observed: … `oc_weight_class`, `oc_weight_class_description`, `oc_zone`, `oc_zone_to_geo_zone`

---

## Table observations

| Topic | Finding |
|-------|---------|
| Content type | Schema definitions + vendor default seed data for fresh install |
| Credential columns | Schema includes `password` columns and empty default `config_*` settings — typical OpenCart install SQL |
| Live customer data | **Not indicated** — seed/demo inserts only; no evidence of production export |
| ocStore-specific tables | **SAFE UNKNOWN** without upstream OpenCart 3.0.3.8 schema comparison |

---

## Known limitations

| Limitation | Impact |
|------------|--------|
| No dump in `database/` | DB layer comparison uses metadata + optional SQL file path in `files/install/` |
| No live DB connection | Table row counts, indexes, engine variants not verified at runtime |
| Prefix assumption | `oc_` inferred from SQL — site audits must confirm actual project prefix |
| Modifications / extensions | OCMOD and extensions may add tables on real sites — not reflected until site audit |
| SQL not diffed byte-by-byte vs 3039 | Sizes differ (192 868 vs 193 177 B); table **names** identical — content delta **SAFE UNKNOWN** |

---

## Usage

- Reference for **expected default schema shape** when comparing project sites.
- For full SQL text, read `files/install/opencart.sql` — do not treat as production backup.
- DB-layer audit claims without site evidence → **SAFE UNKNOWN** per [baseline-readiness-checklist.md](../../../baseline-readiness-checklist.md).

---

## SAFE UNKNOWN

- Exact row-level diff between 3038-rs2 and 3039-rs1 install SQL.
- ocStore-only tables vs upstream OpenCart 3.0.3.8 (no upstream baseline in repo).

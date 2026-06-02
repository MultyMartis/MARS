# Database Metadata — ocStore 3.0.3.9 (rs.1)

**Baseline:** `baselines/ocstore-3039-rs1/`  
**Generated:** 2026-05-30 (OCPilot Run 3.5)  
**Scope:** metadata only — **no** full database dump in `database/`

---

## Schema source

| Field | Value |
|-------|-------|
| Primary source | `files/install/opencart.sql` (promoted from canonical ZIP) |
| Source type | Vendor install seed SQL (pre-install bundle) |
| File size | 193 177 bytes |
| Location in baseline | `baselines/ocstore-3039-rs1/files/install/opencart.sql` |
| Copied to `database/` | **no** — metadata references install artifact only |

---

## Install SQL detected

| Observation | Value |
|-------------|-------|
| `CREATE TABLE` statements | 136 |
| `INSERT INTO` statements | 110 |
| Default table prefix | `oc_` (inferred from table names) |
| Table set delta vs 3038-rs2 | **0** unique table names — same 136 tables |

### Sample tables (first / last alphabetically in file)

- First observed: `oc_address`, `oc_googleshopping_target`, `oc_api`, …
- Last observed: … `oc_weight_class`, `oc_weight_class_description`, `oc_zone`, `oc_zone_to_geo_zone`

---

## Table observations

| Topic | Finding |
|-------|---------|
| Content type | Schema definitions + vendor default seed data for fresh install |
| Credential columns | Schema includes `password` columns and empty default `config_*` settings — typical OpenCart install SQL |
| Live customer data | **Not indicated** |
| ocStore-specific tables | **SAFE UNKNOWN** without upstream OpenCart 3.0.3.9 schema comparison |

---

## Known limitations

| Limitation | Impact |
|------------|--------|
| No dump in `database/` | DB layer comparison uses metadata + optional SQL path under `files/install/` |
| No live DB connection | Runtime schema state not verified |
| Prefix assumption | `oc_` inferred — confirm on each project site |
| Extension tables | Real sites may differ from install seed |
| SQL content delta vs 3038 | +309 bytes file size; table names identical — semantic diff **SAFE UNKNOWN** |

---

## Usage

- Reference for **expected default schema shape** when comparing project sites.
- For full SQL text, read `files/install/opencart.sql`.
- Do not import as production database without operator charter.

---

## SAFE UNKNOWN

- Exact INSERT/content differences vs 3038-rs2 install SQL.
- ocStore-only tables vs upstream OpenCart 3.0.3.9.

# PG17→PG18 COMPATIBILITY-v1

| Field | Value |
|---|---|
| Local validation | PostgreSQL **17.11** |
| Server foundation | PostgreSQL **18.0** (Debian 18.0-1.pgdg13+3) |
| Canonical migrations | roles/001 → core/0001–0002 → app_iseo_sales/0001–0004 |
| Apply result | SUCCESS (no SQL dialect/source changes required for PG18) |
| Extended suites | 02_constraints, 03_permissions, 04_extended, 05_inventory_and_explain PASS |
| Source fix in this wave | `05_inventory_and_explain.sql` — removed invalid `n.nspname` probe (test bug; fixed in Git) |
| Classification | **PG17→PG18 COMPATIBILITY = PASS** |

No PG18-specific migration patches were required on the server.

# MIGRATION-APPLY-v1

**Order:** roles/001 → core/0001 → core/0002 → app_iseo_sales/0001–0004

**Bootstrap role (name only):** `mars_admin`

**DDL role:** `mars_migrator` via `SET ROLE` (+ `GRANT CREATE ON DATABASE mars TO mars_migrator`)

**Result:** APPLY SUCCESS

**Object owner observed:** `mars_migrator`

```
 current_user | current_database |                                                      version                                                       
--------------+------------------+--------------------------------------------------------------------------------------------------------------------
 <redacted>   | <redacted>             | PostgreSQL 18.0 (Debian 18.0-1.pgdg13+3) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
(1 row)

DO
DO
DO
DO
GRANT ROLE
GRANT
SET
CREATE SCHEMA
CREATE SCHEMA
CREATE SCHEMA
COMMENT
COMMENT
COMMENT
REVOKE
REVOKE
REVOKE
GRANT
GRANT
GRANT
GRANT
GRANT
REVOKE
CREATE TABLE
COMMENT
CREATE TABLE
COMMENT
CREATE TABLE
CREATE TABLE
COMMENT
CREATE INDEX
CREATE INDEX
INSERT 0 2
INSERT 0 1
CREATE TABLE
COMMENT
CREATE TABLE
COMMENT
CREATE INDEX
CREATE TABLE
COMMENT
CREATE TABLE
COMMENT
CREATE TABLE
COMMENT
CREATE TABLE
COMMENT
CREATE TABLE
CREATE INDEX
COMMENT
CREATE TABLE
CREATE TABLE
ALTER TABLE
CREATE TABLE
COMMENT
CREATE TABLE
COMMENT
INSERT 0 1
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
CREATE INDEX
INSERT 0 1
SET
CREATE FUNCTION
COMMENT
CREATE FUNCTION
CREATE FUNCTION
CREATE FUNCTION
CREATE FUNCTION
CREATE FUNCTION
CREATE FUNCTION
CREATE FUNCTION
CREATE FUNCTION
REVOKE
REVOKE
REVOKE
REVOKE
REVOKE
REVOKE
REVOKE
REVOKE
REVOKE
GRANT
GRANT
GRANT
GRANT
GRANT
GRANT
GRANT
GRANT
GRANT
GRANT
GRANT
INSERT 0 1
GRANT
GRANT
REVOKE
REVOKE
GRANT
GRANT
GRANT
GRANT
GRANT
REVOKE
ALTER DEFAULT PRIVILEGES
ALTER DEFAULT PRIVILEGES
ALTER DEFAULT PRIVILEGES
INSERT 0 1
RESET
INSERT 0 1
  schema_name   |     version      |          applied_at           
----------------+------------------+-------------------------------
 app_iseo_sales | 0001_base_tables | 2026-09-03 07:35:46.58006+00
 app_iseo_sales | 0002_indexes     | 2026-09-03 07:35:46.593933+00
 app_iseo_sales | 0003_functions   | 2026-09-03 07:35:46.621672+00
 app_iseo_sales | 0004_grants      | 2026-09-03 07:35:46.631038+00
 <redacted>_core      | 0002_<redacted>_core   | 2026-09-03 07:35:46.51811+00
(5 rows)

     app_key     | status  
-----------------+---------
 app_iseo_sales  | planned
 app_seo_content | planned
(2 rows)

APPLY_EXIT=0

```

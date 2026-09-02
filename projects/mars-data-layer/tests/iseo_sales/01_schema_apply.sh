#!/usr/bin/env bash
# Apply iSEO Sales V1 schema + synthetic fixtures.
# Requires: DATABASE_URL, psql, bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
: "${DATABASE_URL:?Set DATABASE_URL to target PostgreSQL (e.g. postgresql://user@host:5432/mars)}"

PSQL=(psql "$DATABASE_URL" -v ON_ERROR_STOP=1)

echo "==> roles/001_create_roles.sql"
"${PSQL[@]}" -f "$ROOT/database/roles/001_create_roles.sql"

echo "==> core/0001_roles_and_schemas.sql"
"${PSQL[@]}" -f "$ROOT/database/core/migrations/0001_roles_and_schemas.sql"

echo "==> core/0002_mars_core.sql"
"${PSQL[@]}" -f "$ROOT/database/core/migrations/0002_mars_core.sql"

echo "==> app_iseo_sales/0001_base_tables.sql"
"${PSQL[@]}" -f "$ROOT/database/app_iseo_sales/migrations/0001_base_tables.sql"

echo "==> app_iseo_sales/0002_indexes.sql"
"${PSQL[@]}" -f "$ROOT/database/app_iseo_sales/migrations/0002_indexes.sql"

echo "==> app_iseo_sales/0003_functions.sql"
"${PSQL[@]}" -f "$ROOT/database/app_iseo_sales/migrations/0003_functions.sql"

echo "==> app_iseo_sales/0004_grants.sql"
"${PSQL[@]}" -f "$ROOT/database/app_iseo_sales/migrations/0004_grants.sql"

echo "==> fixtures/iseo_sales/synthetic_v1.sql"
"${PSQL[@]}" -f "$ROOT/fixtures/iseo_sales/synthetic_v1.sql"

echo "OK — schema + fixtures applied"

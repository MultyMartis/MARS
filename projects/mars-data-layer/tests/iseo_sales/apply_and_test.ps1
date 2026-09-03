# Platform-neutral local apply + test runner (Windows PowerShell)
# Uses psql from PATH or PG_BIN. Requires env.local.ps1 or DATABASE_URL/PG* vars.
# Does not rewrite test semantics — invokes the same SQL/sh artifacts.

param(
  [string]$ProjectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path,
  [switch]$SkipFixtures,
  [switch]$ResetFirst
)

$ErrorActionPreference = "Stop"

if (Test-Path "X:\AI MARS\local\mars-bot-data\env.local.ps1") {
  . "X:\AI MARS\local\mars-bot-data\env.local.ps1"
}

if (-not $env:PGHOST) { $env:PGHOST = "127.0.0.1" }
if (-not $env:PGPORT) { $env:PGPORT = "5433" }
if (-not $env:PGUSER) { $env:PGUSER = "mars_owner" }
if (-not $env:PGDATABASE) { $env:PGDATABASE = "mars" }

function Invoke-PsqlFile([string]$file) {
  Write-Host "==> $(Split-Path $file -Leaf)"
  & psql -h $env:PGHOST -p $env:PGPORT -U $env:PGUSER -d $env:PGDATABASE -v ON_ERROR_STOP=1 -f $file
  if ($LASTEXITCODE -ne 0) { throw "FAILED: $file (exit $LASTEXITCODE)" }
}

if ($ResetFirst) {
  & psql -h $env:PGHOST -p $env:PGPORT -U $env:PGUSER -d $env:PGDATABASE -v ON_ERROR_STOP=1 -c @"
DROP SCHEMA IF EXISTS app_iseo_sales CASCADE;
DROP SCHEMA IF EXISTS app_seo_content CASCADE;
DROP SCHEMA IF EXISTS mars_core CASCADE;
DROP ROLE IF EXISTS iseo_reader;
DROP ROLE IF EXISTS iseo_agent;
DROP ROLE IF EXISTS iseo_runtime;
DROP ROLE IF EXISTS mars_migrator;
"@
  if ($LASTEXITCODE -ne 0) { throw "reset failed" }
}

$files = @(
  "$ProjectRoot\database\roles\001_create_roles.sql",
  "$ProjectRoot\database\core\migrations\0001_roles_and_schemas.sql",
  "$ProjectRoot\database\core\migrations\0002_mars_core.sql",
  "$ProjectRoot\database\app_iseo_sales\migrations\0001_base_tables.sql",
  "$ProjectRoot\database\app_iseo_sales\migrations\0002_indexes.sql",
  "$ProjectRoot\database\app_iseo_sales\migrations\0003_functions.sql",
  "$ProjectRoot\database\app_iseo_sales\migrations\0004_grants.sql"
)
if (-not $SkipFixtures) {
  $files += "$ProjectRoot\fixtures\iseo_sales\synthetic_v1.sql"
}

foreach ($f in $files) { Invoke-PsqlFile $f }

Invoke-PsqlFile "$ProjectRoot\tests\iseo_sales\02_constraints.sql"
Invoke-PsqlFile "$ProjectRoot\tests\iseo_sales\03_permissions.sql"
Invoke-PsqlFile "$ProjectRoot\tests\iseo_sales\04_extended_local_validation.sql"

Write-Host "apply_and_test.ps1: PASS"

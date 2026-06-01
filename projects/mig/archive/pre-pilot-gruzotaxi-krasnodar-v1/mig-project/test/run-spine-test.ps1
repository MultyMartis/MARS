# Run MIG v0.1 session spine locally (without n8n)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Lib = Join-Path $Root "lib\session-spine\run-session-spine.js"
$Payload = Join-Path $PSScriptRoot "test-payload-fallback-v0.1.json"

if (-not $env:MIG_SESSION_ROOT) {
  $env:MIG_SESSION_ROOT = Join-Path $Root "sessions"
}

Write-Host "MIG_SESSION_ROOT=$env:MIG_SESSION_ROOT"
Write-Host "Running spine with payload: $Payload"

Get-Content $Payload -Raw | node $Lib --stdin

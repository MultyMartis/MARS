# MIG Task File Adapter v0.1 — process incoming/mig/requests/*.json
# Human-supervised: run after dropping request files.

$ErrorActionPreference = "Stop"
$MigRoot = Split-Path -Parent $PSScriptRoot
$RepoRoot = Split-Path -Parent (Split-Path -Parent $MigRoot)
$Adapter = Join-Path $MigRoot "lib\task-file-adapter\process-inbox.js"

if (-not $env:MIG_SESSION_ROOT) {
  $env:MIG_SESSION_ROOT = Join-Path $MigRoot "sessions"
}

if (-not $env:MIG_INBOX_ROOT) {
  $env:MIG_INBOX_ROOT = Join-Path $RepoRoot "incoming\mig"
}

Write-Host "MIG_INBOX_ROOT=$env:MIG_INBOX_ROOT"
Write-Host "MIG_SESSION_ROOT=$env:MIG_SESSION_ROOT"
Write-Host "Running Task File Adapter..."

node $Adapter @args

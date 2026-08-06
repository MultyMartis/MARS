#Requires -Version 5.1
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$StateRoot = 'X:\AI MARS STORAGE\runtime-state\client-ops-site-002-producer'
$Tools = 'X:\AI MARS STORAGE\runtime-checkouts\client-ops-site-002-producer\repo\projects\ocpilot\sites\site-002\tools'
$FetchPy = Join-Path $Tools 'site-002-d6g-fetch-pending-terminals.py'
$DispatchPs1 = Join-Path $Tools 'site-002-import-completion-dispatcher.ps1'
if (Test-Path -LiteralPath $FetchPy) {
  & py -3 $FetchPy
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
$pendingDir = Join-Path $StateRoot 'import-terminals\_pending'
if (-not (Test-Path -LiteralPath $pendingDir)) { exit 0 }
Get-ChildItem -LiteralPath $pendingDir -Filter '*.runid' -ErrorAction SilentlyContinue | ForEach-Object {
  $runId = [System.IO.Path]::GetFileNameWithoutExtension($_.Name)
  & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $DispatchPs1 -RunId $runId
  if ($LASTEXITCODE -eq 0) { Remove-Item -LiteralPath $_.FullName -Force -ErrorAction SilentlyContinue }
}
exit 0

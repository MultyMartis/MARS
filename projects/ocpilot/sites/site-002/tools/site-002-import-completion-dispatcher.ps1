#Requires -Version 5.1
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$ProducerRepo = 'X:\AI MARS STORAGE\runtime-checkouts\client-ops-site-002-producer\repo'
$StateRoot = 'X:\AI MARS STORAGE\runtime-state\client-ops-site-002-producer'
$MainRoot = 'X:\AI MARS'
$Mjs = Join-Path $ProducerRepo 'projects\client-ops-reporting-bridge\n8n\runners\run-site-002-import-completion-dispatch.mjs'
$RunId = $null
$Terminal = $null
for ($i = 0; $i -lt $args.Count; $i++) {
  if ($args[$i] -eq '-RunId' -and ($i + 1) -lt $args.Count) { $RunId = [string]$args[$i+1] }
  if ($args[$i] -eq '-Terminal' -and ($i + 1) -lt $args.Count) { $Terminal = [string]$args[$i+1] }
}
$nodeArgs = @($Mjs)
if ($RunId) { $nodeArgs += "--run-id=$RunId" }
if ($Terminal) { $nodeArgs += "--terminal=$Terminal" }
$env:MARS_MAIN_ROOT = $MainRoot
$env:MARS_PRODUCER_REPO = $ProducerRepo
$env:MARS_PRODUCER_STATE = $StateRoot
& node @nodeArgs
exit $LASTEXITCODE

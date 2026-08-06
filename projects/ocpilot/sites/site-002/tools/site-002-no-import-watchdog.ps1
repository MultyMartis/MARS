#Requires -Version 5.1
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$ProducerRepo = 'X:\AI MARS STORAGE\runtime-checkouts\client-ops-site-002-producer\repo'
$StateRoot = 'X:\AI MARS STORAGE\runtime-state\client-ops-site-002-producer'
$MainRoot = 'X:\AI MARS'
$Mjs = Join-Path $ProducerRepo 'projects\client-ops-reporting-bridge\n8n\runners\run-site-002-no-import-watchdog.mjs'
$env:MARS_MAIN_ROOT = $MainRoot
$env:MARS_PRODUCER_REPO = $ProducerRepo
$env:MARS_PRODUCER_STATE = $StateRoot
& node $Mjs
exit $LASTEXITCODE

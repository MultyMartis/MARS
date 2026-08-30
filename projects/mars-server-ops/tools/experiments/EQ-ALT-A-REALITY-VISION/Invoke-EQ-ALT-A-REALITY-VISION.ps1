#Requires -Version 5.1
<#
.SYNOPSIS
  EXP-A01b — Operator-guided offline EQVPS acceptance capture (VEESP ↔ EQVPS ↔ VEESP).

.DESCRIPTION
  Interactive PowerShell harness that remains usable when Cursor disconnects after
  switching v2rayN from VEESP RAW :8443 to EQVPS RAW :8443.

  Does NOT: mutate v2rayN config, switch VPN nodes, mutate servers, elevate, or
  require Cursor / ChatGPT during phases 2–6.

.PARAMETER DryValidate
  Safe local validation only. Exercises helpers, evidence I/O, and one transport
  suite. Does NOT prompt for EQVPS switch or real-app acceptance.

.EXAMPLE
  powershell.exe -NoProfile -ExecutionPolicy Bypass -File "X:\AI MARS\projects\mars-server-ops\tools\experiments\EXP-A01b\Invoke-EXP-A01b.ps1"
#>
[CmdletBinding()]
param(
    [switch]$DryValidate
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Continue'
try {
    # Improve Cyrillic display in a normal Windows console
    chcp 65001 | Out-Null
    [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
    $OutputEncoding = [System.Text.UTF8Encoding]::new($false)
} catch { }
$script:HarnessVersion = 'EQ-ALT-A-REALITY-VISION-1.0.0'

# --- EQ-ALT-A overlay (profile selection) ---
$script:AltAProfileName = 'MCA-ONE-EQ-ALT-A-REALITY-VISION'
$script:AltAImportUri = 'X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\eqvps-alt-a-reality-vision-2026-08-29\vless-share.uri.local'
$script:AltAPort = 9443
$script:AltAExpectedEgress = '95.216.126.173'
function Show-AltAProfileBanner {
    Write-Host ''
    Write-Host ('#' * 72) -ForegroundColor Magenta
    Write-Host 'EQ-ALT-A-REALITY-VISION / offline acceptance' -ForegroundColor Magenta
    Write-Host ("Profil v2rayN: {0}" -f $script:AltAProfileName) -ForegroundColor Magenta
    Write-Host ("Server port: {0} REALITY+Vision. Do NOT use/modify EQVPS :8443." -f $script:AltAPort) -ForegroundColor Magenta
    Write-Host ("Expected egress: {0}" -f $script:AltAExpectedEgress) -ForegroundColor Magenta
    Write-Host ("Import if missing: {0}" -f $script:AltAImportUri) -ForegroundColor Magenta
    Write-Host 'Harness does not switch VPN. Admin PowerShell NOT required.' -ForegroundColor Magenta
    Write-Host ('#' * 72) -ForegroundColor Magenta
    Write-Host ''
}
$script:ProxyUrl = 'http://127.0.0.1:10808'
$script:EvidenceRoot = 'X:\AI MARS\projects\mars-server-ops\evidence\EQVPS-TRANSPORT-ALTERNATIVES-WAVE-01'
$script:EnteredEqvpsPhase = $false
$script:SessionDir = $null
$script:Events = New-Object System.Collections.Generic.List[object]
$script:ManualRows = New-Object System.Collections.Generic.List[object]
$script:AbortRequested = $false
$script:DryAnswers = New-Object System.Collections.Queue
$script:IsDry = [bool]$DryValidate

# Stable non-.ru endpoints used in prior Server Ops transport evidence
$script:UrlEgress = 'https://api.ipify.org'
$script:UrlHttps = 'https://www.cloudflare.com/cdn-cgi/trace'
$script:UrlBody10MB = 'https://speed.cloudflare.com/__down?bytes=10000000'
$script:ExpectedBodyBytes = 10000000
$script:TimeoutShortSec = 25
$script:TimeoutBodySec = 120
$script:RepeatCount = 5

# ---------------------------------------------------------------------------
# Console / UX helpers
# ---------------------------------------------------------------------------
function Write-StageHeader {
    param([string]$Title)
    Write-Host ''
    Write-Host ('=' * 72) -ForegroundColor Cyan
    Write-Host $Title -ForegroundColor Cyan
    Write-Host ('=' * 72) -ForegroundColor Cyan
    Write-Host ''
}

function Write-WarnBox {
    param([string]$Message)
    Write-Host ''
    Write-Host ('!' * 72) -ForegroundColor Yellow
    Write-Host $Message -ForegroundColor Yellow
    Write-Host ('!' * 72) -ForegroundColor Yellow
    Write-Host ''
}

function Write-InstructionBlock {
    param(
        [string]$WhatToDo,
        [string]$WhatNotToChange,
        [string]$WhatToObserve,
        [string]$HowToConfirm
    )
    Write-Host 'ЧТО СДЕЛАТЬ:' -ForegroundColor White
    Write-Host $WhatToDo
    Write-Host ''
    Write-Host 'НЕ МЕНЯЙТЕ:' -ForegroundColor White
    Write-Host $WhatNotToChange
    Write-Host ''
    Write-Host 'ЧТО НАБЛЮДАТЬ:' -ForegroundColor White
    Write-Host $WhatToObserve
    Write-Host ''
    Write-Host 'КАК ПОДТВЕРДИТЬ:' -ForegroundColor White
    Write-Host $HowToConfirm
    Write-Host ''
}

function Add-SessionEvent {
    param(
        [string]$Code,
        [string]$Phase,
        [string]$Detail = ''
    )
    $row = [ordered]@{
        utc       = [datetime]::UtcNow.ToString('o')
        local     = (Get-Date).ToString('o')
        code      = $Code
        phase     = $Phase
        detail    = $Detail
    }
    $script:Events.Add([pscustomobject]$row) | Out-Null
}

function Save-EventsCsv {
    if (-not $script:SessionDir) { return }
    $path = Join-Path $script:SessionDir 'session-events.csv'
    $script:Events | Export-Csv -Path $path -NoTypeInformation -Encoding UTF8
}

function Save-ManualCsv {
    if (-not $script:SessionDir) { return }
    $path = Join-Path $script:SessionDir 'manual-acceptance.csv'
    if ($script:ManualRows.Count -eq 0) {
        'phase,app,question,answer,note,utc' | Set-Content -Path $path -Encoding UTF8
        return
    }
    $script:ManualRows | Export-Csv -Path $path -NoTypeInformation -Encoding UTF8
}

function Write-JsonFile {
    param(
        [string]$Path,
        [object]$Object
    )
    $json = $Object | ConvertTo-Json -Depth 12
    [System.IO.File]::WriteAllText($Path, $json, [System.Text.UTF8Encoding]::new($false))
}

function Wait-OperatorEnter {
    param([string]$Prompt = 'Нажмите ENTER, когда действие выполнено.')
    if ($script:IsDry) {
        Write-Host "[DRY] $Prompt" -ForegroundColor DarkGray
        Add-SessionEvent -Code 'DRY_AUTO_ENTER' -Phase 'DRY' -Detail $Prompt
        return
    }
    Write-Host $Prompt -ForegroundColor Green
    [void](Read-Host)
}

function Read-YNU {
    param(
        [Parameter(Mandatory)][string]$Prompt,
        [string[]]$Allowed = @('Y', 'N', 'U')
    )
    while ($true) {
        $raw = $null
        if ($script:IsDry) {
            if ($script:DryAnswers.Count -gt 0) {
                $raw = [string]$script:DryAnswers.Dequeue()
            } else {
                $raw = 'U'
            }
            Write-Host ("[DRY] {0} -> {1}" -f $Prompt, $raw) -ForegroundColor DarkGray
        } else {
            $raw = Read-Host $Prompt
        }
        if ($null -eq $raw) { $raw = '' }
        $val = $raw.Trim().ToUpperInvariant()
        if ($Allowed -contains $val) { return $val }
        Write-Host ("Неверный ввод '{0}'. Допустимо: {1}" -f $raw, ($Allowed -join '/')) -ForegroundColor Red
        if ($script:IsDry) {
            # Avoid infinite loop in dry mode on bad canned data
            return 'U'
        }
    }
}

function Read-YN {
    param([Parameter(Mandatory)][string]$Prompt)
    return (Read-YNU -Prompt $Prompt -Allowed @('Y', 'N'))
}

function Read-OptionalNote {
    param([string]$Prompt = 'Краткий комментарий (Enter = пусто):')
    if ($script:IsDry) {
        Write-Host "[DRY] $Prompt -> (empty)" -ForegroundColor DarkGray
        return ''
    }
    $n = Read-Host $Prompt
    if ($null -eq $n) { return '' }
    return $n.Trim()
}

function Add-ManualRow {
    param(
        [string]$Phase,
        [string]$App,
        [string]$Question,
        [string]$Answer,
        [string]$Note = ''
    )
    $script:ManualRows.Add([pscustomobject]@{
        phase    = $Phase
        app      = $App
        question = $Question
        answer   = $Answer
        note     = $Note
        utc      = [datetime]::UtcNow.ToString('o')
    }) | Out-Null
}

function Show-VeespRestoreWarning {
    Write-WarnBox @"
ВНИМАНИЕ:
Если сейчас выбран EQVPS, вручную верните VEESP RAW :8443 в v2rayN.

НЕ МЕНЯЙТЕ: TUN / System Proxy / routing / DNS / MTU / другие настройки.
Harness НЕ переключает VPN автоматически.
"@
}

# ---------------------------------------------------------------------------
# Safe process / network observation (no secret config parsing)
# ---------------------------------------------------------------------------
function Get-SafeProcessSnapshot {
    $names = @('v2rayN', 'v2rayN.exe', 'xray', 'xray.exe', 'wv2ray', 'v2ray')
    $rows = @()
    foreach ($n in $names) {
        try {
            Get-Process -Name ($n -replace '\.exe$', '') -ErrorAction SilentlyContinue | ForEach-Object {
                $startStr = 'UNKNOWN'
                $pathStr = 'UNKNOWN'
                try { $startStr = $_.StartTime.ToString('o') } catch { }
                try { $pathStr = $_.Path } catch { }
                $rows += [pscustomobject]@{
                    Name      = $_.ProcessName
                    Id        = $_.Id
                    StartTime = $startStr
                    Path      = $pathStr
                }
            }
        } catch { }
    }
    return $rows
}

function Get-ListenerInfo {
    param([int[]]$Ports)
    $out = @()
    foreach ($p in $Ports) {
        $found = $false
        $owners = @()
        try {
            $conns = Get-NetTCPConnection -LocalPort $p -State Listen -ErrorAction SilentlyContinue
            foreach ($c in @($conns)) {
                $found = $true
                $procName = 'UNKNOWN'
                try {
                    $procName = (Get-Process -Id $c.OwningProcess -ErrorAction SilentlyContinue).ProcessName
                } catch { }
                $owners += [pscustomobject]@{
                    LocalAddress = $c.LocalAddress
                    OwningPid    = $c.OwningProcess
                    ProcessName  = $procName
                }
            }
        } catch {
            # Fallback: netstat parse (safe metadata only)
            try {
                $ns = & netstat.exe -ano -p tcp 2>$null | Select-String -Pattern (":$p\s+")
                foreach ($line in @($ns)) {
                    if ($line -match "LISTENING\s+(\d+)$") {
                        $found = $true
                        $owningPid = [int]$Matches[1]
                        $pn = 'UNKNOWN'
                        try { $pn = (Get-Process -Id $owningPid -ErrorAction SilentlyContinue).ProcessName } catch { }
                        $owners += [pscustomobject]@{
                            LocalAddress = 'parsed-netstat'
                            OwningPid    = $owningPid
                            ProcessName  = $pn
                        }
                    }
                }
            } catch { }
        }
        $out += [pscustomobject]@{
            Port      = $p
            Listening = $found
            Owners    = $owners
            Note      = if ($p -eq 18088 -and -not $found) { 'expected_inactive_unless_isolated_probe' } else { '' }
        }
    }
    return $out
}

function Get-PrecheckObject {
    $os = Get-CimInstance Win32_OperatingSystem -ErrorAction SilentlyContinue
    $ifaces = @()
    try {
        Get-NetIPInterface -AddressFamily IPv4 -ErrorAction SilentlyContinue | ForEach-Object {
            $ifaces += [pscustomobject]@{
                InterfaceAlias = $_.InterfaceAlias
                ifIndex        = $_.ifIndex
                NlMtu          = $_.NlMtu
                ConnectionState = $_.ConnectionState
                Dhcp           = $_.Dhcp
            }
        }
    } catch { }

    $routes = @()
    try {
        Get-NetRoute -DestinationPrefix '0.0.0.0/0' -ErrorAction SilentlyContinue | ForEach-Object {
            $routes += [pscustomobject]@{
                InterfaceAlias = $_.InterfaceAlias
                NextHop        = $_.NextHop
                RouteMetric    = $_.RouteMetric
                ifIndex        = $_.ifIndex
            }
        }
    } catch { }

    $dns = @()
    try {
        Get-DnsClientServerAddress -AddressFamily IPv4 -ErrorAction SilentlyContinue | ForEach-Object {
            if ($_.ServerAddresses -and $_.ServerAddresses.Count -gt 0) {
                $dns += [pscustomobject]@{
                    InterfaceAlias = $_.InterfaceAlias
                    Servers        = @($_.ServerAddresses)
                }
            }
        }
    } catch { }

    $listeners = Get-ListenerInfo -Ports @(10808, 18088)
    $proxy10808 = @($listeners | Where-Object { $_.Port -eq 10808 })[0]
    $mixedOk = $false
    if ($proxy10808 -and $proxy10808.Listening) {
        $ownerNames = @($proxy10808.Owners | ForEach-Object { $_.ProcessName })
        if ($ownerNames -match '(?i)xray|v2ray') { $mixedOk = $true }
    }

    return [ordered]@{
        harness_version     = $script:HarnessVersion
        captured_utc        = [datetime]::UtcNow.ToString('o')
        captured_local      = (Get-Date).ToString('o')
        windows_caption     = if ($os) { $os.Caption } else { 'UNKNOWN' }
        windows_version     = if ($os) { $os.Version } else { [Environment]::OSVersion.Version.ToString() }
        windows_build       = if ($os) { $os.BuildNumber } else { 'UNKNOWN' }
        powershell_version  = $PSVersionTable.PSVersion.ToString()
        is_admin            = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
        interfaces_mtu      = $ifaces
        default_routes      = $routes
        dns_servers         = $dns
        processes           = @(Get-SafeProcessSnapshot)
        listeners           = $listeners
        mixed_proxy_10808   = [ordered]@{
            expected_url              = $script:ProxyUrl
            listening                 = [bool]($proxy10808 -and $proxy10808.Listening)
            owned_by_xray_or_v2ray    = $mixedOk
            note                      = if ($mixedOk) { '127.0.0.1:10808 appears to be live mixed proxy path' } else { '10808 not confirmed as xray/v2ray listener' }
        }
        port_18088_note     = 'Do not assume active; inactive is expected outside isolated probe'
        dry_validate        = $script:IsDry
    }
}

# ---------------------------------------------------------------------------
# Transport helpers (finite timeouts; never abort whole experiment)
# ---------------------------------------------------------------------------
function Invoke-CurlSafe {
    param(
        [Parameter(Mandatory)][string]$Url,
        [string]$Method = 'GET',
        [int]$TimeoutSec = 25,
        [string]$OutputFile = $null,
        [switch]$HeadOnly,
        [switch]$UseProxy
    )
    $started = Get-Date
    $result = [ordered]@{
        url            = $Url
        method         = if ($HeadOnly) { 'HEAD' } else { $Method }
        use_proxy      = [bool]$UseProxy
        proxy          = if ($UseProxy) { $script:ProxyUrl } else { $null }
        timeout_sec    = $TimeoutSec
        started_local  = $started.ToString('o')
        started_utc    = $started.ToUniversalTime().ToString('o')
        exit_code      = $null
        http_code      = $null
        size_download  = $null
        time_total     = $null
        errormsg       = $null
        body_sample    = $null
        ok             = $false
    }

    $tmpOut = $OutputFile
    $deleteTmp = $false
    if ([string]::IsNullOrWhiteSpace($tmpOut)) {
        $tmpOut = [System.IO.Path]::GetTempFileName()
        $deleteTmp = $true
    }

    $argList = New-Object System.Collections.Generic.List[string]
    [void]$argList.Add('-sS'); [void]$argList.Add('-L')
    [void]$argList.Add('--connect-timeout'); [void]$argList.Add([string][Math]::Min(15, $TimeoutSec))
    [void]$argList.Add('--max-time'); [void]$argList.Add([string]$TimeoutSec)
    [void]$argList.Add('-w'); [void]$argList.Add('HTTP_CODE=%{http_code}|SIZE=%{size_download}|TIME=%{time_total}')
    if ($HeadOnly) { [void]$argList.Add('-I') }
    if ($UseProxy) { [void]$argList.Add('-x'); [void]$argList.Add($script:ProxyUrl) }
    [void]$argList.Add('-o'); [void]$argList.Add($tmpOut)
    [void]$argList.Add($Url)

    $stderrText = ''
    $stdoutText = ''
    try {
        $psi = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName = 'curl.exe'
        $psi.Arguments = ($argList | ForEach-Object {
            if ($_ -match '[\s"]') { '"' + ($_ -replace '\\', '\\' -replace '"', '\"') + '"' } else { $_ }
        }) -join ' '
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError = $true
        $psi.UseShellExecute = $false
        $psi.CreateNoWindow = $true
        $proc = [System.Diagnostics.Process]::Start($psi)
        $stdoutText = $proc.StandardOutput.ReadToEnd()
        $stderrText = $proc.StandardError.ReadToEnd()
        $proc.WaitForExit()
        $result.exit_code = $proc.ExitCode
    } catch {
        $result.errormsg = $_.Exception.Message
        $result.ended_local = (Get-Date).ToString('o')
        if ($deleteTmp) {
            try { Remove-Item -LiteralPath $tmpOut -Force -ErrorAction SilentlyContinue } catch { }
        }
        return [pscustomobject]$result
    }

    if ($stdoutText -match 'HTTP_CODE=(\d+)\|SIZE=([\d\.]+)\|TIME=([\d\.]+)') {
        $result.http_code = $Matches[1]
        $result.size_download = $Matches[2]
        $result.time_total = $Matches[3]
    }
    if ($stderrText) {
        $result.errormsg = ($stderrText -replace '\r', '').Trim()
        if ($result.errormsg.Length -gt 500) {
            $result.errormsg = $result.errormsg.Substring(0, 500) + '...[truncated]'
        }
    }

    if ($deleteTmp -and (Test-Path -LiteralPath $tmpOut)) {
        try {
            $bytes = [System.IO.File]::ReadAllBytes($tmpOut)
            $sampleLen = [Math]::Min(120, $bytes.Length)
            if ($sampleLen -gt 0) {
                $text = [System.Text.Encoding]::UTF8.GetString($bytes, 0, $sampleLen)
                $text = ($text -replace '[^\x09\x0A\x0D\x20-\x7E]', '.')
                $result.body_sample = $text
            }
        } catch { }
        try { Remove-Item -LiteralPath $tmpOut -Force -ErrorAction SilentlyContinue } catch { }
    }

    $codeNum = 0
    [void][int]::TryParse([string]$result.http_code, [ref]$codeNum)
    $result.ok = ($result.exit_code -eq 0 -and $codeNum -ge 200 -and $codeNum -lt 400)
    $result.ended_local = (Get-Date).ToString('o')
    $result.duration_ms = [int]((Get-Date) - $started).TotalMilliseconds
    return [pscustomobject]$result
}

function Invoke-TransportSuite {
    param(
        [Parameter(Mandatory)][string]$Label,
        [Parameter(Mandatory)][string]$TextLogPath,
        [Parameter(Mandatory)][string]$JsonPath
    )
    $suite = [ordered]@{
        label          = $Label
        started_utc    = [datetime]::UtcNow.ToString('o')
        started_local  = (Get-Date).ToString('o')
        proxy_url      = $script:ProxyUrl
        tests          = [ordered]@{}
    }

    $log = New-Object System.Collections.Generic.List[string]
    $log.Add("=== TRANSPORT SUITE: $Label ===")
    $log.Add("UTC: $($suite.started_utc)")
    $log.Add("Proxy: $($script:ProxyUrl)")
    $log.Add('')

    Write-Host "Транспорт-тесты [$Label]..." -ForegroundColor White

    # A. Public egress (non-.ru)
    Write-Host '  A) public egress (api.ipify.org via proxy)...'
    $egress = Invoke-CurlSafe -Url $script:UrlEgress -TimeoutSec $script:TimeoutShortSec -UseProxy
    $suite.tests.egress = $egress
    $log.Add(('EGRESS ok={0} http={1} time={2} sample={3} err={4}' -f $egress.ok, $egress.http_code, $egress.time_total, $egress.body_sample, $egress.errormsg))
    Add-SessionEvent -Code 'TRANSPORT_EGRESS' -Phase $Label -Detail ("ok=$($egress.ok);http=$($egress.http_code)")

    # B. Ordinary HTTPS
    Write-Host '  B) ordinary HTTPS (cloudflare trace via proxy)...'
    $https = Invoke-CurlSafe -Url $script:UrlHttps -TimeoutSec $script:TimeoutShortSec -UseProxy
    $suite.tests.https = $https
    $log.Add(('HTTPS ok={0} http={1} time={2} err={3}' -f $https.ok, $https.http_code, $https.time_total, $https.errormsg))
    Add-SessionEvent -Code 'TRANSPORT_HTTPS' -Phase $Label -Detail ("ok=$($https.ok);http=$($https.http_code)")

    # C. Repeated HTTPS
    Write-Host ("  C) repeated HTTPS x{0}..." -f $script:RepeatCount)
    $reps = @()
    $pass = 0
    for ($i = 1; $i -le $script:RepeatCount; $i++) {
        $r = Invoke-CurlSafe -Url $script:UrlHttps -TimeoutSec $script:TimeoutShortSec -UseProxy
        $reps += $r
        if ($r.ok) { $pass++ }
        $log.Add(('REPEAT[{0}] ok={1} http={2} time={3}' -f $i, $r.ok, $r.http_code, $r.time_total))
    }
    $suite.tests.https_repeat = [ordered]@{
        count      = $script:RepeatCount
        pass_count = $pass
        results    = $reps
        ok         = ($pass -eq $script:RepeatCount)
    }
    Add-SessionEvent -Code 'TRANSPORT_HTTPS_REPEAT' -Phase $Label -Detail ("pass=$pass/$($script:RepeatCount)")

    # D. ~10 MB body
    Write-Host '  D) ~10 MB body transfer (Cloudflare speed via proxy)...'
    $bodyFile = Join-Path $script:SessionDir ("body-{0}.bin" -f ($Label -replace '[^\w\-]', '_'))
    $body = Invoke-CurlSafe -Url $script:UrlBody10MB -TimeoutSec $script:TimeoutBodySec -UseProxy -OutputFile $bodyFile
    $actualSize = $null
    if (Test-Path -LiteralPath $bodyFile) {
        try { $actualSize = (Get-Item -LiteralPath $bodyFile).Length } catch { }
        # Do not keep 10MB binary in evidence permanently — record size then delete
        try { Remove-Item -LiteralPath $bodyFile -Force -ErrorAction SilentlyContinue } catch { }
    }
    $bodyMeta = [ordered]@{
        url                 = $script:UrlBody10MB
        expected_bytes      = $script:ExpectedBodyBytes
        actual_bytes        = $actualSize
        curl                = $body
        size_match          = ($null -ne $actualSize -and $actualSize -eq $script:ExpectedBodyBytes)
        ok                  = ($body.ok -and $null -ne $actualSize -and $actualSize -eq $script:ExpectedBodyBytes)
    }
    $suite.tests.body_10mb = $bodyMeta
    $log.Add(('BODY10MB ok={0} http={1} bytes={2} time={3} err={4}' -f $bodyMeta.ok, $body.http_code, $actualSize, $body.time_total, $body.errormsg))
    Add-SessionEvent -Code 'TRANSPORT_BODY_10MB' -Phase $Label -Detail ("ok=$($bodyMeta.ok);bytes=$actualSize")

    $suite.ended_utc = [datetime]::UtcNow.ToString('o')
    $suite.ended_local = (Get-Date).ToString('o')
    $suite.summary = [ordered]@{
        egress_ok        = [bool]$egress.ok
        https_ok         = [bool]$https.ok
        https_repeat_ok  = [bool]$suite.tests.https_repeat.ok
        body_10mb_ok     = [bool]$bodyMeta.ok
    }

    $log.Add('')
    $log.Add(('SUMMARY egress={0} https={1} repeat={2} body10mb={3}' -f `
        $suite.summary.egress_ok, $suite.summary.https_ok, $suite.summary.https_repeat_ok, $suite.summary.body_10mb_ok))
    $log | Set-Content -Path $TextLogPath -Encoding UTF8
    Write-JsonFile -Path $JsonPath -Object $suite
    Save-EventsCsv

    Write-Host ("  Итог [{0}]: egress={1} https={2} repeat={3} body10mb={4}" -f `
        $Label, $suite.summary.egress_ok, $suite.summary.https_ok, $suite.summary.https_repeat_ok, $suite.summary.body_10mb_ok) `
        -ForegroundColor $(if ($suite.summary.egress_ok -and $suite.summary.https_ok) { 'Green' } else { 'Yellow' })

    return [pscustomobject]$suite
}

function Invoke-LightTransportRecheck {
    param(
        [Parameter(Mandatory)][string]$Label,
        [Parameter(Mandatory)][string]$JsonPath,
        [Parameter(Mandatory)][string]$TextLogPath
    )
    $suite = [ordered]@{
        label         = $Label
        started_utc   = [datetime]::UtcNow.ToString('o')
        started_local = (Get-Date).ToString('o')
        tests         = [ordered]@{}
    }
    $log = New-Object System.Collections.Generic.List[string]
    $log.Add("=== LIGHT TRANSPORT RECHECK: $Label ===")

    Write-Host "Повторный транспорт [$Label] (после app-тестов)..." -ForegroundColor White
    $egress = Invoke-CurlSafe -Url $script:UrlEgress -TimeoutSec $script:TimeoutShortSec -UseProxy
    $https = Invoke-CurlSafe -Url $script:UrlHttps -TimeoutSec $script:TimeoutShortSec -UseProxy
    $rep = Invoke-CurlSafe -Url $script:UrlHttps -TimeoutSec $script:TimeoutShortSec -UseProxy
    $bodyFile = Join-Path $script:SessionDir ("body-{0}.bin" -f ($Label -replace '[^\w\-]', '_'))
    $body = Invoke-CurlSafe -Url $script:UrlBody10MB -TimeoutSec $script:TimeoutBodySec -UseProxy -OutputFile $bodyFile
    $actualSize = $null
    if (Test-Path -LiteralPath $bodyFile) {
        try { $actualSize = (Get-Item -LiteralPath $bodyFile).Length } catch { }
        try { Remove-Item -LiteralPath $bodyFile -Force -ErrorAction SilentlyContinue } catch { }
    }
    $suite.tests.egress = $egress
    $suite.tests.https = $https
    $suite.tests.https_one_repeat = $rep
    $suite.tests.body_10mb = [ordered]@{
        expected_bytes = $script:ExpectedBodyBytes
        actual_bytes   = $actualSize
        curl           = $body
        ok             = ($body.ok -and $actualSize -eq $script:ExpectedBodyBytes)
    }
    $suite.summary = [ordered]@{
        egress_ok    = [bool]$egress.ok
        https_ok     = [bool]$https.ok
        repeat_ok    = [bool]$rep.ok
        body_10mb_ok = [bool]$suite.tests.body_10mb.ok
    }
    $suite.ended_utc = [datetime]::UtcNow.ToString('o')
    $log.Add(('egress={0} https={1} repeat={2} body={3}' -f $egress.ok, $https.ok, $rep.ok, $suite.tests.body_10mb.ok))
    $log | Set-Content -Path $TextLogPath -Encoding UTF8
    Write-JsonFile -Path $JsonPath -Object $suite
    Add-SessionEvent -Code 'TRANSPORT_POST_APP' -Phase $Label -Detail ("egress=$($egress.ok)")
    Save-EventsCsv
    return [pscustomobject]$suite
}

# ---------------------------------------------------------------------------
# Log capture (bounded, best-effort, no secrets)
# ---------------------------------------------------------------------------
function Get-ClientLogExtract {
    param([string]$OutV2ray, [string]$OutXray)
    $status = [ordered]@{
        v2rayn = 'NOT_AVAILABLE'
        xray   = 'NOT_AVAILABLE'
        notes  = @()
    }
    $candidates = @(
        (Join-Path $env:APPDATA 'v2rayN\guiLogs'),
        (Join-Path $env:LOCALAPPDATA 'v2rayN\guiLogs'),
        (Join-Path $env:APPDATA 'v2rayN'),
        (Join-Path $env:LOCALAPPDATA 'v2rayN')
    )
    $logFiles = @()
    foreach ($dir in $candidates) {
        if (Test-Path -LiteralPath $dir) {
            try {
                $logFiles += Get-ChildItem -LiteralPath $dir -File -ErrorAction SilentlyContinue |
                    Where-Object { $_.Extension -match '\.(txt|log)$' -or $_.Name -match 'log' } |
                    Sort-Object LastWriteTime -Descending |
                    Select-Object -First 3
            } catch { }
        }
    }
    if ($logFiles.Count -eq 0) {
        "LOG CAPTURE = NOT AVAILABLE`nNo accessible v2rayN/gui log files without elevation." |
            Set-Content -Path $OutV2ray -Encoding UTF8
        "LOG CAPTURE = NOT AVAILABLE" | Set-Content -Path $OutXray -Encoding UTF8
        return [pscustomobject]$status
    }

    $sb = New-Object System.Text.StringBuilder
    [void]$sb.AppendLine("Bounded extract (last ~200 lines per file). Secrets redacted.")
    [void]$sb.AppendLine("Captured UTC: $([datetime]::UtcNow.ToString('o'))")
    foreach ($f in ($logFiles | Select-Object -First 3)) {
        [void]$sb.AppendLine('')
        [void]$sb.AppendLine("--- FILE: $($f.FullName) | mtime=$($f.LastWriteTime.ToString('o')) ---")
        try {
            $lines = Get-Content -LiteralPath $f.FullName -Tail 200 -ErrorAction Stop
            foreach ($line in $lines) {
                $safe = $line
                $safe = [regex]::Replace($safe, '(?i)(uuid|id|password|passwd|token|secret|uri|vless://|vmess://|trojan://)\S+', '$1=[REDACTED]')
                $safe = [regex]::Replace($safe, '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', '[REDACTED-UUID]')
                [void]$sb.AppendLine($safe)
            }
            $status.v2rayn = 'PARTIAL'
        } catch {
            [void]$sb.AppendLine("read_error=$($_.Exception.Message)")
            $status.notes += $_.Exception.Message
        }
    }
    [System.IO.File]::WriteAllText($OutV2ray, $sb.ToString(), [System.Text.UTF8Encoding]::new($false))

    # Xray client log often co-located; if not found mark NOT_AVAILABLE
    $xrayCand = $logFiles | Where-Object { $_.Name -match '(?i)xray' } | Select-Object -First 1
    if ($xrayCand) {
        try {
            $xl = Get-Content -LiteralPath $xrayCand.FullName -Tail 200 -ErrorAction Stop
            $xs = ($xl | ForEach-Object {
                $s = $_
                $s = [regex]::Replace($s, '(?i)(uuid|id|password|passwd|token|secret|uri|vless://)\S+', '$1=[REDACTED]')
                $s = [regex]::Replace($s, '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', '[REDACTED-UUID]')
                $s
            }) -join "`n"
            Set-Content -Path $OutXray -Value $xs -Encoding UTF8
            $status.xray = 'PARTIAL'
        } catch {
            "LOG CAPTURE = NOT AVAILABLE`n$($_.Exception.Message)" | Set-Content -Path $OutXray -Encoding UTF8
        }
    } else {
        "LOG CAPTURE = NOT AVAILABLE`nNo distinct xray client log located safely." | Set-Content -Path $OutXray -Encoding UTF8
    }
    return [pscustomobject]$status
}

function Write-SessionReadme {
    param([string]$Path)
    $content = @"
# EXP-A01b session evidence

Harness: $($script:HarnessVersion)
Session directory: $($script:SessionDir)
DryValidate: $($script:IsDry)

## Purpose
Operator-guided offline acceptance capture:
VEESP baseline → EQVPS switch → transport + real apps → VEESP restore → recovery.

## Important
If the harness aborts (Ctrl+C / exception) after EQVPS phase started:

**Manually restore VEESP RAW :8443 in v2rayN.**

Do not change TUN / System Proxy / routing / DNS / MTU / other settings.
This harness never switches VPN automatically and never edits v2rayN config.

## Secrets policy
Evidence must not contain VLESS UUIDs, URIs, passwords, panel paths, tokens, or subscription links.
Log extracts are redacted best-effort.

## Files
- session-summary.json
- session-events.csv
- baseline-veesp.json / transport-veesp.txt
- eqvps.json / transport-eqvps.txt
- eqvps-post-app.json / transport-eqvps-post-app.txt (if reached)
- recovery-veesp.json / transport-recovery.txt
- manual-acceptance.csv
- process-snapshot.txt
- v2rayn-log-extract.txt
- xray-client-log-extract.txt
- COMPLETED.marker (only on full completion)

After completion with VEESP restored, return to Cursor and provide this directory path.
"@
    Set-Content -Path $Path -Value $content -Encoding UTF8
}

# ---------------------------------------------------------------------------
# Ctrl+C handling
# ---------------------------------------------------------------------------
$null = Register-EngineEvent -SourceIdentifier ConsoleBreak -Action {
    $script:AbortRequested = $true
} -ErrorAction SilentlyContinue

try {
    [Console]::TreatControlCAsInput = $false
} catch { }

# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
$summary = [ordered]@{
    experiment        = 'EXP-A01b'
    harness_version   = $script:HarnessVersion
    dry_validate      = $script:IsDry
    status            = 'STARTED'
    evidence_dir      = $null
    phases            = [ordered]@{}
    admin_required    = $false
    admin_used        = $false
    vpn_auto_switch   = $false
    v2rayn_config_writes = 0
    server_mutations  = 0
    secret_disclosure = 0
}

try {
    Write-StageHeader 'EXP-A01b — Offline EQVPS Acceptance Capture'
    if ($script:IsDry) {
        Write-Host 'MODE: DryValidate (без переключения VPN, без app-acceptance)' -ForegroundColor Yellow
        # Seed dry answers for any accidental prompt
        foreach ($a in @('Y','Y','Y','N','N','N','N','N','Y','Y','Y','Y','Y','Y','Y','Y','Y','U','Y','Y','Y','Y')) {
            $script:DryAnswers.Enqueue($a)
        }
    } else {
        Write-Host 'Этот PowerShell-сеанс — единственный обязательный контроллер теста.' -ForegroundColor White
        Write-Host 'Cursor может отключиться на EQVPS — это ожидаемо. Продолжайте здесь.' -ForegroundColor White
    }

    # Session dir
    $stamp = Get-Date -Format 'yyyy-MM-dd_HHmmss'
    $suffix = if ($script:IsDry) { 'dryvalidate' } else { 'live' }
    $script:SessionDir = Join-Path $script:EvidenceRoot ("{0}_{1}" -f $stamp, $suffix)
    New-Item -ItemType Directory -Force -Path $script:SessionDir | Out-Null
    $summary.evidence_dir = $script:SessionDir
    Write-Host ("Evidence: {0}" -f $script:SessionDir) -ForegroundColor Green
    Write-SessionReadme -Path (Join-Path $script:SessionDir 'README.md')
    Add-SessionEvent -Code 'SESSION_START' -Phase 'PHASE0' -Detail $script:SessionDir

    # ========================= PHASE 0 =========================
    Show-AltAProfileBanner
        Write-StageHeader 'PHASE 0 — PRECHECK'
    $precheck = Get-PrecheckObject
    Write-JsonFile -Path (Join-Path $script:SessionDir 'precheck.json') -Object $precheck
    $procSnap = @(Get-SafeProcessSnapshot)
    $procSnap | Format-Table -AutoSize | Out-String | Set-Content -Path (Join-Path $script:SessionDir 'process-snapshot.txt') -Encoding UTF8
    $logCap = Get-ClientLogExtract `
        -OutV2ray (Join-Path $script:SessionDir 'v2rayn-log-extract.txt') `
        -OutXray (Join-Path $script:SessionDir 'xray-client-log-extract.txt')
    $summary.phases.phase0_precheck = [ordered]@{
        mixed_proxy_10808_listening = $precheck.mixed_proxy_10808.listening
        mixed_proxy_owned_ok        = $precheck.mixed_proxy_10808.owned_by_xray_or_v2ray
        port_18088_listening        = @($precheck.listeners | Where-Object Port -eq 18088 | Select-Object -ExpandProperty Listening -First 1)
        is_admin                    = $precheck.is_admin
        log_capture                 = $logCap
    }
    Write-Host ("Proxy 127.0.0.1:10808 listening={0} xray/v2ray-owned={1}" -f `
        $precheck.mixed_proxy_10808.listening, $precheck.mixed_proxy_10808.owned_by_xray_or_v2ray)
    Write-Host ("Port 18088 listening={0} (inactive expected)" -f $summary.phases.phase0_precheck.port_18088_listening)
    Add-SessionEvent -Code 'PHASE0_DONE' -Phase 'PHASE0'
    Save-EventsCsv

    if ($script:IsDry) {
        # Dry path: run one transport suite, write stub artifacts, finalize
        Write-StageHeader 'DRYVALIDATE — TRANSPORT HELPER CHECK'
        $null = Invoke-TransportSuite -Label 'DRY_TRANSPORT' `
            -TextLogPath (Join-Path $script:SessionDir 'transport-veesp.txt') `
            -JsonPath (Join-Path $script:SessionDir 'baseline-veesp.json')

        # Minimal placeholder files so structure matches live session
        Write-JsonFile -Path (Join-Path $script:SessionDir 'eqvps.json') -Object @{ status = 'SKIPPED_DRYVALIDATE' }
        'SKIPPED_DRYVALIDATE' | Set-Content -Path (Join-Path $script:SessionDir 'transport-eqvps.txt') -Encoding UTF8
        Write-JsonFile -Path (Join-Path $script:SessionDir 'recovery-veesp.json') -Object @{ status = 'SKIPPED_DRYVALIDATE' }
        'SKIPPED_DRYVALIDATE' | Set-Content -Path (Join-Path $script:SessionDir 'transport-recovery.txt') -Encoding UTF8
        Save-ManualCsv

        $dryResult = [ordered]@{
            dry_validate              = $true
            powershell_syntax_ok      = $true
            evidence_dir_created      = (Test-Path -LiteralPath $script:SessionDir)
            transport_helper_ran      = $true
            csv_json_written          = $true
            admin_required            = $false
            admin_used                = [bool]$precheck.is_admin
            v2rayn_config_mutation    = 0
            server_mutation           = 0
            eqvps_switch_simulated    = $false
            app_acceptance_triggered  = $false
            result                    = 'PASS'
            evidence_dir              = $script:SessionDir
            completed_utc             = [datetime]::UtcNow.ToString('o')
        }
        Write-JsonFile -Path (Join-Path $script:SessionDir 'dry-validation-result.json') -Object $dryResult
        $summary.status = 'DRYVALIDATE_PASS'
        $summary.phases.dryvalidate = $dryResult
        Write-JsonFile -Path (Join-Path $script:SessionDir 'session-summary.json') -Object $summary
        Save-EventsCsv
        Write-StageHeader 'DRYVALIDATE — PASS'
        Write-Host ("Evidence: {0}" -f $script:SessionDir) -ForegroundColor Green
        Write-Host 'VPN не переключался. Можно запускать live-режим.' -ForegroundColor Green
        return
    }

    # ========================= PHASE 1 =========================
    Write-StageHeader 'PHASE 1 — VEESP BASELINE'
    Write-InstructionBlock `
        -WhatToDo "В v2rayN убедитесь, что выбран профиль VEESP RAW :8443 (активный рабочий узел)." `
        -WhatNotToChange "TUN, System Proxy, routing, DNS, MTU, UDP/443, браузерный proxy, Xray core, прочие настройки v2rayN." `
        -WhatToObserve "Интернет и Cursor сейчас работают как обычно (базовая линия)." `
        -HowToConfirm "Когда VEESP выбран — вернитесь сюда и нажмите ENTER."
    Wait-OperatorEnter
    Add-SessionEvent -Code 'VEESP_BASELINE_CONFIRMED' -Phase 'PHASE1'

    $veespTransport = Invoke-TransportSuite -Label 'VEESP_BASELINE' `
        -TextLogPath (Join-Path $script:SessionDir 'transport-veesp.txt') `
        -JsonPath (Join-Path $script:SessionDir 'baseline-veesp.json')

    Write-Host 'Короткая ручная приёмка VEESP (базовая линия):' -ForegroundColor White
    $vCursor = Read-YNU -Prompt 'Cursor сейчас работает? [Y/N/U]'
    $vChat = Read-YNU -Prompt 'ChatGPT: обычный prompt работает? [Y/N/U]'
    $vYt = Read-YNU -Prompt 'YouTube: реальное воспроизведение работает? [Y/N/U]'
    $vNote = Read-OptionalNote
    Add-ManualRow -Phase 'VEESP_BASELINE' -App 'Cursor' -Question 'works' -Answer $vCursor -Note $vNote
    Add-ManualRow -Phase 'VEESP_BASELINE' -App 'ChatGPT' -Question 'prompt_works' -Answer $vChat
    Add-ManualRow -Phase 'VEESP_BASELINE' -App 'YouTube' -Question 'playback_works' -Answer $vYt
    Save-ManualCsv
    $summary.phases.phase1_veesp_baseline = [ordered]@{
        transport = $veespTransport.summary
        manual    = @{ cursor = $vCursor; chatgpt = $vChat; youtube = $vYt }
    }
    Add-SessionEvent -Code 'PHASE1_DONE' -Phase 'PHASE1'
    Save-EventsCsv

    # ========================= PHASE 2 =========================
    Write-StageHeader 'ШАГ / PHASE 2 — ПЕРЕКЛЮЧИТЕ VPN НА MCA-ONE-EQ-ALT-A-REALITY-VISION (:9443)'
    Write-InstructionBlock `
        -WhatToDo @"
ВНИМАНИЕ EQ-ALT-A: профиль MCA-ONE-EQ-ALT-A-REALITY-VISION (не EQVPS :8443). Импорт при необходимости: vless-share.uri.local. В v2rayN ВРУЧНУЮ выберите профиль:
  VEESP RAW :8443  →  MCA-ONE-EQ-ALT-A-REALITY-VISION (:9443 REALITY+Vision)

После выбора подождите примерно 10 секунд стабилизации.
"@ `
        -WhatNotToChange @"
- TUN
- System Proxy
- routing
- DNS
- MTU
- правило UDP/443
- настройки браузерного proxy
- Xray core / версия
- любые другие настройки v2rayN
"@ `
        -WhatToObserve @"
Cursor может перестать работать / показать Reconnecting / Thinking.
Это ОЖИДАЕМО и является частью теста.
НЕ чините Cursor. Продолжайте в ЭТОМ окне PowerShell.
"@ `
        -HowToConfirm 'Когда EQVPS выбран и прошло ~10 секунд — вернитесь сюда и нажмите ENTER.'

    $script:EnteredEqvpsPhase = $true
    Wait-OperatorEnter
    Add-SessionEvent -Code 'EQVPS_SWITCH_CONFIRMED' -Phase 'PHASE2'
    Save-EventsCsv
    $summary.phases.phase2_switch = [ordered]@{
        code = 'EQVPS_SWITCH_CONFIRMED'
        utc  = [datetime]::UtcNow.ToString('o')
    }

    # ========================= PHASE 3 =========================
    Write-StageHeader 'PHASE 3 — EQVPS TRANSPORT CAPTURE'
    Write-Host 'Автоматические транспорт-тесты на EQVPS. Ошибки записываются, эксперимент продолжается.' -ForegroundColor White
    $eqvpsTransport = Invoke-TransportSuite -Label 'EQVPS' `
        -TextLogPath (Join-Path $script:SessionDir 'transport-eqvps.txt') `
        -JsonPath (Join-Path $script:SessionDir 'eqvps.json')
    $summary.phases.phase3_eqvps_transport = $eqvpsTransport.summary
    Add-SessionEvent -Code 'PHASE3_DONE' -Phase 'PHASE3'
    Save-EventsCsv

    # ========================= PHASE 4 =========================
    Write-StageHeader 'PHASE 4 — EQVPS REAL-APP MANUAL ACCEPTANCE'

    # TEST A — Cursor
    Write-StageHeader 'TEST A — CURSOR (EQVPS)'
    Write-InstructionBlock `
        -WhatToDo @"
Попробуйте обычную работу Cursor Agent:
1) Откройте/используйте существующую Agent-сессию.
2) Если Cursor ещё принимает ввод — отправьте осмысленный короткий запрос.
3) Понаблюдайте короткое разумное время (не чините сеть).
"@ `
        -WhatNotToChange 'Не переключайте VPN обратно на этом шаге. Не меняйте настройки v2rayN.' `
        -WhatToObserve 'Полный ответ / Reconnecting / Thinking / Taking longer / Agent stop retrying.' `
        -HowToConfirm 'Ответьте на вопросы ниже в этом окне (Y/N/U).'
    $cComplete = Read-YNU -Prompt 'Cursor дал полный usable ответ? [Y/N/U]'
    $cReconn = Read-YN -Prompt 'Был Reconnecting? [Y/N]'
    $cThink = Read-YN -Prompt 'Застрял на Thinking? [Y/N]'
    $cLonger = Read-YN -Prompt 'Показывал Taking longer than expected? [Y/N]'
    $cStop = Read-YN -Prompt 'Agent перестал retry? [Y/N]'
    $cNote = Read-OptionalNote -Prompt 'Комментарий по Cursor (Enter = пусто):'
    Add-ManualRow -Phase 'EQVPS' -App 'Cursor' -Question 'complete_usable_response' -Answer $cComplete -Note $cNote
    Add-ManualRow -Phase 'EQVPS' -App 'Cursor' -Question 'reconnecting' -Answer $cReconn
    Add-ManualRow -Phase 'EQVPS' -App 'Cursor' -Question 'stuck_thinking' -Answer $cThink
    Add-ManualRow -Phase 'EQVPS' -App 'Cursor' -Question 'taking_longer' -Answer $cLonger
    Add-ManualRow -Phase 'EQVPS' -App 'Cursor' -Question 'agent_stopped_retry' -Answer $cStop
    Save-ManualCsv

    # TEST B — ChatGPT
    Write-StageHeader 'TEST B — CHATGPT (EQVPS)'
    Write-InstructionBlock `
        -WhatToDo "Откройте ChatGPT в браузере как обычно. Проверьте UI, сессию, отправьте безобидный prompt, дождитесь полного ответа." `
        -WhatNotToChange 'Не меняйте VPN/proxy настройки. Не переключайте узел.' `
        -WhatToObserve 'Homepage/UI, отправка prompt, полный ответ.' `
        -HowToConfirm 'Ответьте Y/N/U на вопросы ниже.'
    $gHome = Read-YNU -Prompt 'ChatGPT Homepage/UI usable? [Y/N/U]'
    $gSub = Read-YNU -Prompt 'Prompt отправлен? [Y/N/U]'
    $gResp = Read-YNU -Prompt 'Полный ответ получен? [Y/N/U]'
    $gNote = Read-OptionalNote -Prompt 'Комментарий по ChatGPT (Enter = пусто):'
    Add-ManualRow -Phase 'EQVPS' -App 'ChatGPT' -Question 'homepage_ui' -Answer $gHome -Note $gNote
    Add-ManualRow -Phase 'EQVPS' -App 'ChatGPT' -Question 'prompt_submitted' -Answer $gSub
    Add-ManualRow -Phase 'EQVPS' -App 'ChatGPT' -Question 'complete_response' -Answer $gResp
    Save-ManualCsv

    # TEST C — YouTube
    Write-StageHeader 'TEST C — YOUTUBE (EQVPS)'
    Write-InstructionBlock `
        -WhatToDo "Откройте YouTube. Проверьте homepage, страницу видео, реальное воспроизведение (не только thumbnail)." `
        -WhatNotToChange 'Не меняйте VPN/proxy. Не переключайте узел.' `
        -WhatToObserve 'Homepage, video page, старт playback, устойчивость playback.' `
        -HowToConfirm 'Ответьте Y/N/U на вопросы ниже.'
    $yHome = Read-YNU -Prompt 'YouTube Homepage? [Y/N/U]'
    $yPage = Read-YNU -Prompt 'Video page? [Y/N/U]'
    $yStart = Read-YNU -Prompt 'Playback реально стартует? [Y/N/U]'
    $yStay = Read-YNU -Prompt 'Playback остаётся usable? [Y/N/U]'
    $yNote = Read-OptionalNote -Prompt 'Комментарий по YouTube (Enter = пусто):'
    Add-ManualRow -Phase 'EQVPS' -App 'YouTube' -Question 'homepage' -Answer $yHome -Note $yNote
    Add-ManualRow -Phase 'EQVPS' -App 'YouTube' -Question 'video_page' -Answer $yPage
    Add-ManualRow -Phase 'EQVPS' -App 'YouTube' -Question 'playback_starts' -Answer $yStart
    Add-ManualRow -Phase 'EQVPS' -App 'YouTube' -Question 'playback_usable' -Answer $yStay
    Save-ManualCsv

    # TEST D — Facebook (optional)
    Write-StageHeader 'TEST D — FACEBOOK CONTROL (опционально)'
    Write-Host 'Facebook — контрольный сайт. Можно пропустить: введите U.' -ForegroundColor White
    $fb = Read-YNU -Prompt 'Facebook usable? [Y/N/U] (U = не тестировал / skip)'
    $fbNote = Read-OptionalNote -Prompt 'Комментарий Facebook (Enter = пусто):'
    Add-ManualRow -Phase 'EQVPS' -App 'Facebook' -Question 'usable' -Answer $fb -Note $fbNote
    Save-ManualCsv

    $summary.phases.phase4_apps = [ordered]@{
        cursor   = @{ complete = $cComplete; reconnecting = $cReconn; thinking = $cThink; longer = $cLonger; stop_retry = $cStop }
        chatgpt  = @{ homepage = $gHome; submitted = $gSub; response = $gResp }
        youtube  = @{ homepage = $yHome; page = $yPage; start = $yStart; usable = $yStay }
        facebook = @{ usable = $fb }
    }
    Add-SessionEvent -Code 'PHASE4_DONE' -Phase 'PHASE4'
    Save-EventsCsv

    # Optional mid-EQVPS recheck
    Write-StageHeader 'EQVPS_TRANSPORT_POST_APP — повторный транспорт'
    $postApp = Invoke-LightTransportRecheck -Label 'EQVPS_TRANSPORT_POST_APP' `
        -JsonPath (Join-Path $script:SessionDir 'eqvps-post-app.json') `
        -TextLogPath (Join-Path $script:SessionDir 'transport-eqvps-post-app.txt')
    $summary.phases.eqvps_transport_post_app = $postApp.summary

    # ========================= PHASE 5 =========================
    Write-StageHeader 'ШАГ / PHASE 5 — ВЕРНИТЕ VPN НА VEESP RAW :8443'
    Write-InstructionBlock `
        -WhatToDo @"
В v2rayN ВРУЧНУЮ верните профиль:
  MCA-ONE-EQ-ALT-A-REALITY-VISION (:9443)  →  VEESP RAW :8443

Подождите короткое время на восстановление соединения.
"@ `
        -WhatNotToChange 'TUN, System Proxy, routing, DNS, MTU, UDP/443, браузерный proxy, Xray core, прочие настройки.' `
        -WhatToObserve 'Восстановление интернета / Cursor / обычных сайтов.' `
        -HowToConfirm 'Когда снова выбран VEESP — вернитесь сюда и нажмите ENTER.'
    Wait-OperatorEnter
    Add-SessionEvent -Code 'VEESP_RECOVERY_SWITCH_CONFIRMED' -Phase 'PHASE5'
    $script:EnteredEqvpsPhase = $false
    Save-EventsCsv
    $summary.phases.phase5_restore = [ordered]@{
        code = 'VEESP_RECOVERY_SWITCH_CONFIRMED'
        utc  = [datetime]::UtcNow.ToString('o')
    }

    # ========================= PHASE 6 =========================
    Write-StageHeader 'PHASE 6 — VEESP RECOVERY CONTROL'
    $recTransport = Invoke-TransportSuite -Label 'VEESP_RECOVERY' `
        -TextLogPath (Join-Path $script:SessionDir 'transport-recovery.txt') `
        -JsonPath (Join-Path $script:SessionDir 'recovery-veesp.json')

    Write-Host 'Ручная проверка восстановления на VEESP:' -ForegroundColor White
    $rCursor = Read-YNU -Prompt 'Cursor снова работает? [Y/N/U]'
    $rChat = Read-YNU -Prompt 'ChatGPT: актуальный prompt работает? [Y/N/U]'
    $rYt = Read-YNU -Prompt 'YouTube: реальное воспроизведение работает? [Y/N/U]'
    $rNote = Read-OptionalNote
    Add-ManualRow -Phase 'VEESP_RECOVERY' -App 'Cursor' -Question 'works_again' -Answer $rCursor -Note $rNote
    Add-ManualRow -Phase 'VEESP_RECOVERY' -App 'ChatGPT' -Question 'prompt_works' -Answer $rChat
    Add-ManualRow -Phase 'VEESP_RECOVERY' -App 'YouTube' -Question 'playback_works' -Answer $rYt
    Save-ManualCsv
    $summary.phases.phase6_recovery = [ordered]@{
        transport = $recTransport.summary
        manual    = @{ cursor = $rCursor; chatgpt = $rChat; youtube = $rYt }
    }
    Add-SessionEvent -Code 'PHASE6_DONE' -Phase 'PHASE6'
    Save-EventsCsv

    # Refresh process snapshot post-run
    @(Get-SafeProcessSnapshot) | Format-Table -AutoSize | Out-String |
        Add-Content -Path (Join-Path $script:SessionDir 'process-snapshot.txt') -Encoding UTF8

    # ========================= PHASE 7 =========================
    Write-StageHeader 'PHASE 7 — FINALIZE'
    Write-Host 'VPN сейчас должен быть на VEESP.' -ForegroundColor White
    $finalNet = Read-YNU -Prompt 'VEESP восстановлен и интернет работает? [Y/N/U]'
    Add-ManualRow -Phase 'FINAL' -App 'Network' -Question 'veesp_restored_internet_ok' -Answer $finalNet
    Save-ManualCsv

    $summary.status = 'COMPLETED'
    $summary.completed_utc = [datetime]::UtcNow.ToString('o')
    $summary.completed_local = (Get-Date).ToString('o')
    $summary.final_veesp_internet = $finalNet
    $summary.aba_matrix = [ordered]@{
        veesp_baseline = $summary.phases.phase1_veesp_baseline
        eqvps          = @{
            transport = $summary.phases.phase3_eqvps_transport
            apps      = $summary.phases.phase4_apps
            post_app  = $summary.phases.eqvps_transport_post_app
        }
        veesp_recovery = $summary.phases.phase6_recovery
    }
    Write-JsonFile -Path (Join-Path $script:SessionDir 'session-summary.json') -Object $summary
    Save-EventsCsv
    Save-ManualCsv
    'COMPLETED' | Set-Content -Path (Join-Path $script:SessionDir 'COMPLETED.marker') -Encoding UTF8
    Add-SessionEvent -Code 'SESSION_COMPLETED' -Phase 'PHASE7'
    Save-EventsCsv

    Write-StageHeader 'EXP-A01b ЗАВЕРШЁН'
    Write-Host ("Evidence:`n{0}" -f $script:SessionDir) -ForegroundColor Green
    Write-Host ''
    Write-Host 'Теперь можно вернуться в Cursor.' -ForegroundColor White
    Write-Host 'Передайте Cursor путь к этому evidence-каталогу.' -ForegroundColor White
    Write-Host ''
    Wait-OperatorEnter -Prompt 'Нажмите ENTER, чтобы закрыть harness.'
}
catch {
    $summary.status = 'ABORTED_OR_ERROR'
    $summary.error = $_.Exception.Message
    $summary.error_utc = [datetime]::UtcNow.ToString('o')
    try {
        if ($script:SessionDir) {
            Write-JsonFile -Path (Join-Path $script:SessionDir 'session-summary.json') -Object $summary
            Save-EventsCsv
            Save-ManualCsv
            Add-SessionEvent -Code 'SESSION_ERROR' -Phase 'ERROR' -Detail $_.Exception.Message
            Save-EventsCsv
        }
    } catch { }
    Write-Host ("ОШИБКА: {0}" -f $_.Exception.Message) -ForegroundColor Red
    if ($script:EnteredEqvpsPhase) {
        Show-VeespRestoreWarning
    }
    throw
}
finally {
    if ($script:EnteredEqvpsPhase) {
        Show-VeespRestoreWarning
    } elseif (-not $script:IsDry) {
        Write-Host ''
        Write-Host 'Напоминание: убедитесь, что в v2rayN снова выбран VEESP RAW :8443.' -ForegroundColor DarkYellow
    }
    try {
        if ($script:SessionDir) {
            Write-JsonFile -Path (Join-Path $script:SessionDir 'session-summary.json') -Object $summary
            Save-EventsCsv
            Save-ManualCsv
        }
    } catch { }
}

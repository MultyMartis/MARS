# Server B Direct Network Test (operator-assisted)
# Purpose: Measure workstation -> Server B with TUN/system proxy OFF.
# Does NOT: change network config, disable TUN, install software, or hard-code Server B IP.
#
# Invocation:
#   PowerShell -ExecutionPolicy Bypass -File "X:\AI MARS\projects\mars-server-ops\assets\SERVER-B-PLANNING\SERVER-B-DIRECT-NETWORK-TEST.ps1" -ServerIp "<SERVER_B_IP>"
#
# Preconditions (operator):
#   1. Turn OFF xray_tun / v2rayN TUN (and any system proxy intercepting ICMP/TCP tests).
#   2. Confirm Cursor/AI connectivity remains acceptable after TUN off (or run from a separate shell).
#   3. Use physical Ethernet if that is the intended production path.
#   4. Supply -ServerIp from local secret contour (secrets.local.md) - do not commit the IP.

param(
    [Parameter(Mandatory = $true)]
    [string]$ServerIp
)

$ErrorActionPreference = 'Continue'

function Test-IsIPv4Address {
    param([string]$Value)
    if ([string]::IsNullOrWhiteSpace($Value)) { return $false }
    if ($Value -notmatch '^(?:\d{1,3}\.){3}\d{1,3}$') { return $false }
    $octets = $Value.Split('.')
    foreach ($octet in $octets) {
        $n = 0
        if (-not [int]::TryParse($octet, [ref]$n)) { return $false }
        if ($n -lt 0 -or $n -gt 255) { return $false }
    }
    return $true
}

if ($ServerIp -eq '<SERVER_B_IP>' -or $ServerIp -match '[<>]' -or -not (Test-IsIPv4Address -Value $ServerIp)) {
    Write-Host "ERROR: Replace <SERVER_B_IP> with the actual Server B IPv4 from the local secret contour."
    Write-Host "Expected source: X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\secrets.local.md"
    Write-Host ("Received: {0}" -f $ServerIp)
    exit 1
}

Write-Host "=== MARS Server B Direct Network Test ==="
Write-Host ("Target: {0}" -f $ServerIp)
Write-Host ("Timestamp (UTC): {0}" -f [datetime]::UtcNow.ToString('o'))
Write-Host ("Timestamp (local): {0}" -f (Get-Date).ToString('o'))
Write-Host ""

Write-Host "=== Active adapters (physical + TUN indicators) ==="
$upAdapters = @(Get-NetAdapter | Where-Object { $_.Status -eq 'Up' })
$upAdapters |
    Select-Object Name, InterfaceDescription, Status, LinkSpeed, MacAddress |
    Format-Table -AutoSize

Write-Host "=== Adapter note ==="
Write-Host "Inspect Name, InterfaceDescription, and LinkSpeed to distinguish physical Ethernet from xray_tun / Wintun / TAP / TUN."
Write-Host "This script does NOT disable TUN. If a TUN adapter is Up, results may be distorted."
Write-Host ""

$tunLike = @(
    $upAdapters | Where-Object {
        $_.Name -match '(?i)tun|wintun|tap|xray|v2ray|wireguard|wg' -or
        $_.InterfaceDescription -match '(?i)tun|wintun|tap|xray|v2ray|wireguard|Meta'
    }
)
if ($tunLike.Count -gt 0) {
    Write-Host "WARNING: Possible TUN/VPN adapter(s) currently Up:"
    $tunLike | ForEach-Object {
        Write-Host ("  - {0} | {1} | {2}" -f $_.Name, $_.InterfaceDescription, $_.LinkSpeed)
    }
} else {
    Write-Host "No obvious TUN/Wintun/TAP adapter marked Up among active adapters."
}
Write-Host ""

Write-Host "=== Ping (-n 20) ==="
$pingOutput = & ping.exe $ServerIp -n 20 2>&1 | ForEach-Object { $_.ToString() }
$pingOutput | ForEach-Object { Write-Host $_ }
Write-Host ""

$pingLoss = $null
$pingMin = $null
$pingAvg = $null
$pingMax = $null
foreach ($line in $pingOutput) {
    if ($line -match 'Lost\s*=\s*(\d+)\s*\((\d+)%\s*loss\)') {
        $pingLoss = $Matches[2] + '%'
    }
    if ($line -match 'Minimum\s*=\s*(\d+)ms,\s*Maximum\s*=\s*(\d+)ms,\s*Average\s*=\s*(\d+)ms') {
        $pingMin = $Matches[1] + 'ms'
        $pingMax = $Matches[2] + 'ms'
        $pingAvg = $Matches[3] + 'ms'
    }
}

Write-Host "=== Traceroute ==="
& tracert.exe $ServerIp
Write-Host ""

Write-Host "=== Test-NetConnection TCP/22 ==="
$tnc = Test-NetConnection -ComputerName $ServerIp -Port 22
$tnc | Format-List ComputerName, RemoteAddress, RemotePort, InterfaceAlias, SourceAddress, PingSucceeded, TcpTestSucceeded
Write-Host ""

Write-Host "=== Final result summary ==="
Write-Host ("Timestamp (UTC): {0}" -f [datetime]::UtcNow.ToString('o'))
Write-Host ("Target: {0}" -f $ServerIp)
Write-Host ("Active Up adapters: {0}" -f $upAdapters.Count)
$upAdapters | ForEach-Object {
    Write-Host ("  - {0} | {1} | LinkSpeed={2}" -f $_.Name, $_.InterfaceDescription, $_.LinkSpeed)
}
Write-Host ("Ping loss: {0}" -f $(if ($pingLoss) { $pingLoss } else { '(see ping output above)' }))
Write-Host ("Ping min/avg/max: {0} / {1} / {2}" -f $(if ($pingMin) { $pingMin } else { 'n/a' }), $(if ($pingAvg) { $pingAvg } else { 'n/a' }), $(if ($pingMax) { $pingMax } else { 'n/a' }))
Write-Host ("TcpTestSucceeded (port 22): {0}" -f $tnc.TcpTestSucceeded)
Write-Host ("Test interface alias: {0}" -f $tnc.InterfaceAlias)
Write-Host "Record ping loss/RTT, hop count, TcpTestSucceeded, and whether TUN was OFF."
Write-Host "Do not paste secrets into Git evidence - sanitize IP if required by programme policy."
Write-Host "=== Done ==="
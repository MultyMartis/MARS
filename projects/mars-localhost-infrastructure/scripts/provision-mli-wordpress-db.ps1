#Requires -Version 5.1
<#
.SYNOPSIS
    Provision MLI WordPress database + least-privilege user (MySQL 8.4).
.DESCRIPTION
    Uses caching_sha2_password only. Reads DB_PASSWORD from runtime.env.
    No password output. Administrative connection via root@localhost.
.PARAMETER RuntimeEnv
    Path to runtime.env (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST required).
.PARAMETER AdminUser
    MySQL administrative user (default root).
.EXAMPLE
    .\provision-mli-wordpress-db.ps1 -RuntimeEnv 'C:\MARS Phenix\AI MARS\local\mli\fp-0002\runtime.env'
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$RuntimeEnv,
    [string]$AdminUser = 'root'
)

$ErrorActionPreference = 'Stop'
$Mysql = 'E:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\bin\mysql.exe'

function Get-EnvValue([string]$Path, [string]$Key) {
    foreach ($line in Get-Content -LiteralPath $Path) {
        if ($line -match "^\s*$Key\s*=\s*(.+)\s*$") {
            return $Matches[1].Trim().Trim('"').Trim("'")
        }
    }
    throw "Missing $Key in $Path"
}

$dbName = Get-EnvValue -Path $RuntimeEnv -Key 'DB_NAME'
$dbUser = Get-EnvValue -Path $RuntimeEnv -Key 'DB_USER'
$dbPass = Get-EnvValue -Path $RuntimeEnv -Key 'DB_PASSWORD'
$dbHost = Get-EnvValue -Path $RuntimeEnv -Key 'DB_HOST'
if (-not $dbHost) { $dbHost = '127.0.0.1' }

$sql = @"
CREATE DATABASE IF NOT EXISTS ``$dbName`` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER IF NOT EXISTS '$dbUser'@'$dbHost' IDENTIFIED WITH caching_sha2_password BY '$dbPass';
ALTER USER '$dbUser'@'$dbHost' IDENTIFIED WITH caching_sha2_password BY '$dbPass';
GRANT ALL PRIVILEGES ON ``$dbName``.* TO '$dbUser'@'$dbHost';
FLUSH PRIVILEGES;
"@

& $Mysql -u $AdminUser --batch -e $sql | Out-Null

$audit = & $Mysql -u $AdminUser --batch -e "SELECT User, Host, plugin FROM mysql.user WHERE User='$dbUser' AND Host='$dbHost';"
Write-Host "[MLI] Provisioned $dbUser@$dbHost -> $dbName"
Write-Host "[MLI] Plugin audit: $audit"

& $Mysql -h $dbHost -u $dbUser "-p$dbPass" -D $dbName -e 'SELECT 1 AS connection_ok;' | Out-Null
if ($LASTEXITCODE -ne 0) { throw 'Application connection test failed.' }
Write-Host '[MLI] Application connection test: PASS'

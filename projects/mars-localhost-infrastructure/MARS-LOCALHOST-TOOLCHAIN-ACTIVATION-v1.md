# MARS Localhost Toolchain Activation

## Status

OPERATIONAL — HUMAN-INVOKED — SESSION-ONLY

This document records the canonical workstation/runtime activation model for MARS Localhost Infrastructure (MLI).

This is not automatic global activation. This is not permanent PATH configuration. This is not a MARS autonomous runtime. It is a human-invoked workstation/runtime helper for approved local PHP, Composer, Node/npm, and project-local Gulp work.

## Canonical Roots

Active Brain:
`X:\AI MARS\`

Storage:
`X:\AI MARS STORAGE\`

Local Runtime:
`X:\MARS-Localhost\`

## Canonical Toolchain

PowerShell:
7.6.3 validated

Git:
2.54.0.windows.1 validated

Node.js:
`C:\Program Files\nodejs\node.exe`
v24.18.0

npm:
11.16.0

Gulp:
project-local only

PHP:
`X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe`
PHP 8.3.30

Composer:
`C:\ProgramData\ComposerSetup\bin\composer.phar`
Composer 2.10.1

Python:
`C:\Users\MetaCODE ONE\AppData\Local\Python\pythoncore-3.14-64\python.exe`
Python 3.14.6

Classification:
CURRENT / SHIM-RESOLVED / NORMALIZATION DEFERRED

## Activation Script

Path:

`X:\MARS-Localhost\tools\powershell\Activate-MarsToolchain.ps1`

Activate:

```powershell
. "X:\MARS-Localhost\tools\powershell\Activate-MarsToolchain.ps1"
```

Validate:

```powershell
php --version
composer --version
```

Rollback current session:

```powershell
Disable-MarsToolchain
```

Persistence:

PROCESS ONLY

The activation script does not change User PATH, Machine PATH, or PowerShell profile. It does not start Laragon services. It does not install packages.

## Gulp Policy

Use project-local dependencies only.

Preferred:

```powershell
npm run <existing-script>
```

Read-only task discovery:

```powershell
npx --no-install gulp --tasks-simple
```

No global Gulp installation.

Representative validated workspace:

`X:\AI MARS\workspaces\fp-0002-shpigovsky-v8\`

Validated:

- Gulp CLI 2.3.0
- Local Gulp 4.0.2

Node 24 classification:

NO EXPLICIT ENGINE
LOCAL TASK INSPECTION PASS
FULL BUILD VALIDATION NOT PART OF THIS WORKSTATION TASK

## Machine PATH Cleanup

Removed deprecated exact entry:

`E:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64`

Current classification:

DEPRECATED ROOT — REMOVED FROM MACHINE PATH

Canonical X: PHP was not added permanently.

Windows restart required:

NO

Cursor restart required after cleanup:

YES, to refresh inherited process environment.

Cursor restart is not claimed complete here; this documentation only records the cleanup state and restart requirement.

## Evidence

Storage evidence paths are external, out-of-Git evidence:

- `X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-BEFORE-PHP-CLEANUP-20260703-204105.txt`
- `X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-AFTER-PHP-CLEANUP-20260703-204105.txt`
- `X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-RESTORE-20260703-204105.ps1`
- `X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-REMOVE-PHP-20260703-204105.ps1`

Runtime files are external to Git and must not be represented as tracked MARS source.

## Failure Modes

- `php` unresolved before activation.
- Composer wrapper partial before PHP activation.
- Stale terminal inherited environment.
- Missing `X:` volume.
- Wrong volume label.
- Missing `php.exe`.
- Missing `composer.phar`.
- Execution policy blocking the script.
- Global Gulp accidentally used.

## Operational Rule

For PHP/Composer work in a fresh PowerShell terminal:

1. Confirm `X:` volume.
2. Dot-source the activator.
3. Run `php --version`.
4. Run `composer --version`.
5. Perform the approved task.
6. Optionally run `Disable-MarsToolchain`.

## Rollback

Session rollback:

```powershell
Disable-MarsToolchain
```

Machine PATH rollback evidence:

`X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-RESTORE-20260703-204105.ps1`

Machine PATH restore requires elevated PowerShell and explicit operator confirmation.

## Security Boundary

No credentials, tokens, account IDs, or secrets are stored in this documentation.

---

*Toolchain activation v1 -- MLI workstation/runtime helper; process-only and human-invoked.*

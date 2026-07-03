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

## Workstation PATH Normalization Closure

Status:

COMPLETE

Completed removals:

### User PATH

- `C:\Users\MetaCODE ONE\AppData\Roaming\npm`
- `C:\Users\MetaCODE ONE\AppData\Roaming\Composer\vendor\bin`

Reason:

Both directories were absent and no active global command shims depended on them.

### Machine PATH

Removed duplicate textual form:

`C:\Program Files\nodejs`

Retained canonical textual form:

`C:\Program Files\nodejs\`

Reason:

Both entries referenced the same Node installation in the same persisted Machine PATH scope.

### Retained Entries

User PATH:

`C:\Users\MetaCODE ONE\AppData\Local\Microsoft\WindowsApps`

Machine PATH:

- `C:\Program Files\Git\cmd`
- `C:\Program Files\nodejs\`
- `C:\ProgramData\ComposerSetup\bin`

### PHP Boundary

Deprecated E: PHP entry:

REMOVED

Canonical X: PHP in permanent User PATH:

NO

Canonical X: PHP in permanent Machine PATH:

NO

PHP activation model:

PROCESS ONLY / SESSION-ONLY

### Final Command Resolution

Git:

AVAILABLE

Node:

AVAILABLE

npm:

AVAILABLE

npx:

AVAILABLE

Composer wrapper:

AVAILABLE

Python:

SHIM-RESOLVED THROUGH WINDOWSAPPS

PHP before activator:

UNRESOLVED — EXPECTED

### Restart State

Windows restart required:

NO

Cursor restart required after cleanup:

YES

Post-restart validation:

OPERATOR-CONFIRMED

### Evidence Boundary

Storage evidence paths are external, out-of-Git evidence:

- `X:\AI MARS STORAGE\backups\workstation\environment\USER-PATH-BEFORE-STALE-ENTRY-CLEANUP-20260703-213858.txt`
- `X:\AI MARS STORAGE\backups\workstation\environment\USER-PATH-AFTER-STALE-ENTRY-CLEANUP-20260703-213858.txt`
- `X:\AI MARS STORAGE\backups\workstation\environment\USER-PATH-RESTORE-20260703-213858.ps1`
- `X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-BEFORE-NODE-DUPLICATE-CLEANUP-20260703-213858.txt`
- `X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-AFTER-NODE-DUPLICATE-CLEANUP-20260703-213858.txt`
- `X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-RESTORE-NODE-20260703-213858.ps1`
- `X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-REMOVE-NODE-DUPLICATE-20260703-213858.ps1`

Restore scripts require explicit operator action. Machine PATH restore requires elevation.

No credentials or secrets are stored in this PATH-normalization evidence.

### Remaining Deferred Item

Python normalization:

DEFERRED UNTIL A PYTHON-CRITICAL LANE REQUIRES IT

## Runtime Activator Backup

Status:

COMPLETE

Backup created:

2026-07-04T01:13:48+07:00

Backup root:

`X:\AI MARS STORAGE\backups\workstation\runtime-toolchain\MARS-TOOLCHAIN-ACTIVATOR-20260704-011348`

Source:

`X:\MARS-Localhost\tools\powershell\Activate-MarsToolchain.ps1`

`X:\MARS-Localhost\tools\powershell\README.md`

Backup contents:

- exact source copies;
- source receipt;
- backup manifest;
- SHA-256 checksums;
- restore guide;
- restore validation checklist.

Classification:

SANITIZED — RESTORABLE — OUT OF GIT

Source hashes:

Activate-MarsToolchain.ps1:

`3988AD57545207BA0A72717C139751413DF0867FF1E286D9101B9EAB98A8AD76`

README.md:

`A45582815EBA65C75BB663A43CC3558E42E22D6CA87C556EAD8CEC90B59FDA1A`

Restore policy:

- manual;
- exact two-file scope;
- checksum validation required;
- no automatic overwrite;
- no mirror;
- no delete;
- operator approval required when target differs.

Git documentation preserves authority and explanation.

Storage backup preserves the runtime file bytes.

Both are required for complete recovery.

## Current Backup Coverage

| Component | Status | Location |
|-----------|--------|----------|
| Cursor sanitized profile/config backup | COMPLETE | `X:\AI MARS STORAGE\backups\workstation\cursor\` |
| PATH checkpoints, cleanup evidence and rollback | COMPLETE | `X:\AI MARS STORAGE\backups\workstation\environment\` |
| Runtime toolchain activator and README | COMPLETE | `X:\AI MARS STORAGE\backups\workstation\runtime-toolchain\MARS-TOOLCHAIN-ACTIVATOR-20260704-011348` |
| Git documentation and reports | COMPLETE | `X:\AI MARS\` |

## Current Scope Closure

Cursor/workstation/toolchain current phase:

CLOSED FOR CURRENT SCOPE

Further workstation changes:

ONLY WHEN A CONCRETE PROJECT DEPENDENCY REQUIRES THEM

Python normalization:

DEFERRED UNTIL A PYTHON-CRITICAL LANE REQUIRES IT

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

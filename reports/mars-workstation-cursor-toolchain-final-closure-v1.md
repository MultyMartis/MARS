# REPORT — MARS WORKSTATION, CURSOR AND TOOLCHAIN FINAL CLOSURE

## 1. Result

COMPLETE

## 2. Closure Date

2026-07-04T01:13:48+07:00

## 3. Scope Completed

- Cursor user-data and account/profile metadata audit;
- MARS-CANONICAL profile creation and cross-window validation;
- sanitized Cursor backup;
- .cursorignore hardening;
- PHP/Composer/Gulp toolchain audit;
- session-only toolchain activation;
- deprecated E: PHP Machine PATH cleanup;
- stale npm and Composer User PATH cleanup;
- duplicate Node Machine PATH cleanup;
- persisted PATH validation;
- canonical MLI documentation;
- runtime activator backup.

## 4. Cursor State

Profile:

MARS-CANONICAL

Status:

OPERATIONALLY ACTIVE — UI CONFIRMED

Metadata:

SAFE UNKNOWN — UI CONFIRMED ONLY

Editor Window / Agents Window:

SHARED CANONICAL WORKSPACE — CONFIRMED

Working model:

Editor Window:
primary mutating interface

Agents Window:
read-only/bounded by default

Safety rule:

ONE MUTATING AGENT PER WORKING SCOPE

## 5. Backup Coverage

| Component | Status | Location | Restore Status |
|-----------|--------|----------|----------------|
| Cursor sanitized backup | COMPLETE | `X:\AI MARS STORAGE\backups\workstation\cursor\` | NOT YET RESTORE-TESTED |
| PATH evidence and rollback | COMPLETE | `X:\AI MARS STORAGE\backups\workstation\environment\` | CHECKPOINTED |
| Runtime activator backup | COMPLETE | `X:\AI MARS STORAGE\backups\workstation\runtime-toolchain\MARS-TOOLCHAIN-ACTIVATOR-20260704-011348` | RESTORE GUIDE INCLUDED |
| Git documentation | COMPLETE | `X:\AI MARS\` | COMMITTED AND PUSHED BY THIS TASK |

## 6. Runtime Activator Backup

Backup root:

`X:\AI MARS STORAGE\backups\workstation\runtime-toolchain\MARS-TOOLCHAIN-ACTIVATOR-20260704-011348`

Files:

- `source\Activate-MarsToolchain.ps1`;
- `source\README.md`;
- `inventory\SOURCE-RECEIPT.md`;
- `inventory\BACKUP-MANIFEST.md`;
- `inventory\CHECKSUMS-SHA256.txt`;
- `restore\RESTORE-GUIDE.md`;
- `restore\VALIDATION-CHECKLIST.md`.

Source hashes:

Activate-MarsToolchain.ps1:

`3988AD57545207BA0A72717C139751413DF0867FF1E286D9101B9EAB98A8AD76`

README.md:

`A45582815EBA65C75BB663A43CC3558E42E22D6CA87C556EAD8CEC90B59FDA1A`

Validation:

BACKUP COMPLETE AND RESTORABLE

## 7. Canonical Toolchain

PowerShell:
7.6.3

Git:
2.54.0.windows.1

Node:
v24.18.0

npm:
11.16.0

Gulp:
project-local only

PHP:
8.3.30

Composer:
2.10.1

Python:
3.14.6 / SHIM-RESOLVED / NORMALIZATION DEFERRED

Activation:

PROCESS ONLY / SESSION-ONLY

Persistent PHP PATH:

NOT USED

## 8. PATH State

Removed:

- deprecated E: PHP Machine PATH entry;
- stale npm User PATH entry;
- stale Composer User PATH entry;
- duplicate Node Machine PATH entry.

Retained:

- WindowsApps;
- Git;
- canonical Node path;
- ComposerSetup.

Windows restart:

NOT REQUIRED

## 9. Documentation and Git History

Prior commits:

`6d9eeec72e0fe2e370a3e561e5ca49b3495e71e9`

docs(mli): document canonical toolchain activation

`0d1ec543c1711c064fdb17ef27cba8b87656763b`

docs(mli): close workstation path normalization

The final runtime-backup documentation commit is created by this task.

## 10. Security and Boundaries

- no secrets backed up;
- no credentials;
- no account sessions;
- no chat history in canonical backup;
- no permanent PHP PATH;
- no global Gulp;
- no package installation;
- no foreign WIP mutation;
- no runtime binaries copied;
- no destructive synchronization;
- no writes outside approved X: roots.

## 11. Remaining SAFE UNKNOWN

- MARS-CANONICAL metadata is UI-confirmed, not machine-proven;
- Cursor backup has not been restore-tested;
- runtime activator backup has restore instructions but has not been restored in a destructive test;
- Python normalization is deferred.

## 12. Closure

Cursor backup:

COMPLETE

PATH evidence and rollback backup:

COMPLETE

Runtime activator backup:

COMPLETE

Documentation:

COMPLETE

Workstation PATH normalization:

CLOSED

Cursor/workstation/toolchain current phase:

CLOSED FOR CURRENT SCOPE

## 13. Future Trigger Conditions

Reopen this infrastructure lane only for:

- workstation replacement;
- disk migration;
- Cursor profile loss;
- Cursor version migration causing profile/config drift;
- PHP version change;
- Node version incompatibility;
- Composer model change;
- runtime activator restore;
- concrete Python-critical project;
- backup restore test.

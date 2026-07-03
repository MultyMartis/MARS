# REPORT — MARS LOCALHOST TOOLCHAIN ACTIVATION AND PATH CLEANUP

## Result

COMPLETE

## Runtime Tool

Script path:
`X:\MARS-Localhost\tools\powershell\Activate-MarsToolchain.ps1`

README path:
`X:\MARS-Localhost\tools\powershell\README.md`

Script SHA-256:
`3988AD57545207BA0A72717C139751413DF0867FF1E286D9101B9EAB98A8AD76`

README SHA-256:
`A45582815EBA65C75BB663A43CC3558E42E22D6CA87C556EAD8CEC90B59FDA1A`

## Validated Toolchain

- PHP 8.3.30
- Composer 2.10.1
- Node v24.18.0
- npm 11.16.0
- Gulp project-local 4.0.2

## Activation Model

PROCESS ONLY / SESSION-ONLY

## Machine PATH Cleanup

Removed exact deprecated E: PHP entry.

Other entries changed:

0

Windows restart required:

NO

## Evidence

- `X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-BEFORE-PHP-CLEANUP-20260703-204105.txt`
- `X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-AFTER-PHP-CLEANUP-20260703-204105.txt`
- `X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-RESTORE-20260703-204105.ps1`
- `X:\AI MARS STORAGE\backups\workstation\environment\MACHINE-PATH-REMOVE-PHP-20260703-204105.ps1`

## Cursor Indexing

Recorded `.cursorignore` exclusions:

- `.recovery-temp/`
- `.restore-test-temp/`
- `.tools/node-portable/`
- `.tools/node-runtime/`

## Boundaries

- No User PATH modification.
- No permanent X: PHP PATH.
- No global Gulp.
- No source build.
- No package installation.
- No secrets.
- No foreign WIP mutation.

## Git Scope

Task-owned files intended for commit:

- `.cursorignore`
- `projects/mars-localhost-infrastructure/MARS-LOCALHOST-TOOLCHAIN-ACTIVATION-v1.md`
- `projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md`
- `reports/mars-localhost-toolchain-activation-and-path-cleanup-v1.md`

---

*Scoped workstation/toolchain closure report -- runtime and storage evidence remain outside Git.*

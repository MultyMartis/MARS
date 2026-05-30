# SNAPSHOT-MANIFEST — Website Factory Legal + Blueprint Foundation v1

## Identity

| Field | Value |
|-------|--------|
| **Snapshot ID** | `snap-20260530-website-factory-legal-blueprint-foundation-v1` |
| **Timestamp (local)** | 2026-05-30 |
| **Purpose** | Rollback point before Website Factory brain polishing — Legal Pack v1 FROZEN + Blueprint / Block Registry foundation IN PROGRESS |
| **Snapshot path** | `workspaces/_snapshots/snap-20260530-website-factory-legal-blueprint-foundation-v1/` |
| **Operator** | APPROVED BY OPERATOR |

## Git baseline (at capture)

| Field | Value |
|-------|--------|
| **Baseline commit (HEAD)** | `d6b67ea6776e304775cd9be371cd4d480770f4f8` |
| **Branch** | `mars/post-cycle8-live-tests` |
| **Checkpoint commit** | Created by task — see checkpoint report |

## Build status

| Step | Result |
|------|--------|
| Pre-snapshot `npm run build` (live V6 workspace) | **PASS** (exit 0, Gulp `build` ~3.33s) |
| `dist/` in snapshot | **Excluded** — regenerate via `npm run build` after restore |

## Included payload

| Path | Files (at capture) |
|------|-------------------:|
| `website-factory-reference-v1/` | 95 |
| `triumph-manipulator-landing-v6/legal/` | 1 |
| `triumph-manipulator-landing-v6/legal-entity/` | 4 |
| `triumph-manipulator-landing-v6/src/pages/privacy-policy/` | 1 |
| `triumph-manipulator-landing-v6/src/pages/consent-personal-data/` | 1 |
| `triumph-manipulator-landing-v6/src/pages/user-agreement/` | 1 |
| `triumph-manipulator-landing-v6/src/pages/cookie-files-policy/` | 1 |
| `triumph-manipulator-landing-v6/src/partials/sections/legal/` | 9 |
| `triumph-manipulator-landing-v6/src/scss/` (legal scope) | 3 |
| **Total files** | **115** (+ manifest + report) |

## Excluded

| Path | Reason |
|------|--------|
| `node_modules/` | Reinstall via `npm install` |
| `dist/` | Regenerate via `npm run build` |
| `.cache/`, `logs/`, `tmp/`, `temp/` | Ephemeral |
| Triumph V6 non-legal workspace paths | Out of checkpoint scope (SMTP, PPC routes, visual polish) |

## Foundation state at capture

| System | Status |
|--------|--------|
| Legal Pack v1 | **FROZEN** |
| Legal Entity Discovery v1 | **ACCEPTED** |
| Site Type Registry v1 | **ACCEPTED** |
| Site Type Blueprints v1 | **IN PROGRESS** |
| Block Registry Alignment v1 | **IN PROGRESS** |
| Triumph V6 Legal Pilot (L1–L4) | **COMPLETE** |

## Verification (snapshot self-check)

| Check | Result |
|-------|--------|
| `node_modules/` in snapshot | **Absent** |
| `dist/` in snapshot | **Absent** |
| `.cache/`, `logs/`, `tmp/`, `temp/` in snapshot | **Absent** |
| Website Factory reference tree present | **PASS** (95 files) |
| Triumph V6 legal scope present | **PASS** (20 files) |

## Restore notes

1. Copy `website-factory-reference-v1/` to `workspaces/website-factory-reference-v1/` (selective merge or full replace per operator charter).
2. Copy `triumph-manipulator-landing-v6/` legal paths to live V6 workspace.
3. Run `npm install` and `npm run build` in `workspaces/triumph-manipulator-landing-v6/`.
4. Log restore in `logs/rollback-history/` if operational policy requires it.

**Primary restore source:** `workspaces/_snapshots/snap-20260530-website-factory-legal-blueprint-foundation-v1/`

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Live browser QA on legal pages | SAFE UNKNOWN |
| Production deploy authorization | SAFE UNKNOWN |
| CI automation for legal contract | FUTURE — not in scope |

## Sign-off

| Field | Value |
|-------|--------|
| **manifest completed** | 2026-05-30 |
| **operator sign-off** | Cursor agent (Website Factory Legal Blueprint Foundation Checkpoint v1) |

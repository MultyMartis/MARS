# FP-0002 — WPilot Local Installation v1

**Version:** v1.2 | **Date:** 2026-07-02 | **Stage:** FP-0002 DEV-runtime reconciliation

## Result

```text
WPilot installation:
INSTALLED AND ACTIVE (v0.3.0-rc5)

WPilot local read-only:
VALIDATED (8/8) post-reconciliation

WPilot writes:
DISABLED / NOT TESTED

Package:
metacode-wpilot-v0.3.0-rc5.zip (deploy-packages + local package cache)

Runtime:
http://shpigovsky.test/
```

## Reconciliation (2026-07-02)

Local Shpigovsky previously ran stale `metacode-wpilot-v0.3.0.zip` (22 files, pre-UX-01). Operator confirmed DEV `https://dev.gktriumph.ru/` is the visual/functional authority. Controlled replacement aligned local plugin files with **RC5** package identical to Brain source and DEV fingerprint.

| Check | Result |
|-------|--------|
| Stale package incident | `metacode-wpilot-v0.3.0.zip` — **superseded, preserved** |
| Canonical package | `metacode-wpilot-v0.3.0-rc5.zip` — SHA-256 `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577` |
| Brain ↔ RC5 equivalence | **EXACT** |
| Pre-replace checkpoint | `wpilot-pre-dev-runtime-reconciliation-20260702T161228Z` |
| Post-replace file count | 27 |
| Read-only REST | 8/8 PASS |
| Version collision | Header `0.3.0` on distinct builds — use build id `v0.3.0-rc5` |

Evidence: [wpilot-fp0002-dev-runtime-reconciliation-2026-07-02.md](../../../../wpilot/reports/wpilot-fp0002-dev-runtime-reconciliation-2026-07-02.md)

## Local bridge state

| Setting | Value |
|---------|-------|
| `bridge_enabled` | `true` |
| `dev_confirmed` | `true` |
| `write_enabled` | `false` |
| `emergency_disabled` | `false` |
| Token storage | `X:\AI MARS\local\tokens\wpilot-local-shpigovsky.token` (gitignored) |

## Evidence (initial install)

| Check | Result |
|-------|--------|
| Pre-repair checkpoint | `foundation-002a-pre-access-encoding-wpilot` |
| Initial (stale) package | `metacode-wpilot-v0.3.0.zip` — replaced 2026-07-02 |
| Plugin slug / version header | `metacode-wpilot` / `0.3.0` |
| MU-plugin | `mars-local-runtime.php` — **KEEP AS IS** |

## Boundaries (unchanged)

- No WPilot write proof in this task
- No production use
- Shpigovsky Forge admission: **V9-05C READ_ONLY** (see FP-0002-V9-05C-READ-ONLY-PROJECT-ADMISSION-RECEIPT-v1.md)
- No FW-07C-2
- WordPress implementation: **NOT STARTED**
- **Shpigovsky Core:** project foundation — no WPilot bridge duplication

---

*FP-0002 WPilot local installation — reconciled with DEV 2026-07-02.*

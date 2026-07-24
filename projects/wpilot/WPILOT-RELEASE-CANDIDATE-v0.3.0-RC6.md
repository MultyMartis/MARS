# WPilot Release Candidate — v0.3.0-RC6

**Classification:** Release candidate specification — RC6 production token-gating remediation after RC5.  
**Date:** 2026-07-24  
**Status:** Source + package built; **not** deployed to production in the remediation task.  
**Plugin slug:** `metacode-wpilot`  
**Maintenance class:** M1 (explicit remediation charter)

---

## Version

| Field | Value |
|-------|-------|
| **Release label** | `v0.3.0-RC6` |
| **Plugin version** | `0.3.0` (WordPress header unchanged vs RC5) |
| **Constants** | `RELEASE_CANDIDATE=RC6`, `RELEASE_LABEL=0.3.0-RC6` |
| **Schema version** | `0.2.0` |
| **Text domain** | `metacode-wpilot` |
| **REST namespace** | `wpilot/v1` |
| **Environment scope** | Packaging for authorized update gates; production deploy **not** auto-authorized |

---

## RC6 Delta (vs RC5)

| Area | Change |
|------|--------|
| **Token generation gate** | Uses `WPilot_Environment::can_manage_token()` — admin capability + not emergency; **no** `dev_confirmed` / `bridge_enabled` / `write_enabled` |
| **REST operational gate** | Unchanged — still `operational_readiness()` |
| **Write gate** | Unchanged — still requires `write_enabled` |
| **Token persistence** | `generate_token` / `revoke_token` write **partial** option updates only (stale-snapshot mitigation) |
| **Admin copy** | Token control / production prohibition updated to match corrected model |
| **`dev_confirmed` semantics** | Remains literal DEV/test assertion — **not** reinterpreted for production |

**Not in RC6 scope:** Sprint 3, new REST routes, schema bump, production deploy, weakening REST/write refusals, automatic production environment confirmation model.

---

## Package

| Field | Value |
|-------|-------|
| **ZIP path** | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.zip` |
| **Inventory** | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.inventory.json` |
| **Build helper** | `X:\AI MARS STORAGE\wpilot\deploy-packages\build-rc6-package.py` |
| **SHA-256** | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| **Size** | 55,771 bytes |
| **Root folder** | `metacode-wpilot/` |
| **File count** | **27** |
| **RC5 preserved** | `metacode-wpilot-v0.3.0-rc5.zip` (SHA-256 `43c71a561872a037f294a12d5194d0925e988392599f02c1eeb2d8b1c52e1577`) |

---

## Corrected readiness split

1. **Token creation readiness** — `can_manage_token()` + admin nonce.  
2. **REST operational readiness** — token + bridge + DEV confirmation + not emergency.  
3. **Write readiness** — REST readiness + `write_enabled` + mutation gates.

---

## Evidence

- [reports/REPORT-WPILOT-PRODUCTION-TOKEN-GATING-REMEDIATION.md](reports/REPORT-WPILOT-PRODUCTION-TOKEN-GATING-REMEDIATION.md)
- Tests: `tests/token-gating-remediation/run-token-gating-tests.php`
- Prior RC5: [WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md](WPILOT-RELEASE-CANDIDATE-v0.3.0-RC5.md) — historical; not rewritten

---

## Explicit exclusions

- No production update in this RC packaging task alone without site-ops update charter.
- No temporary production DEV assertion.
- No bridge enablement solely to mint a token.

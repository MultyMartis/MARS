# Forge WordPress — Pilot Tooling Profile v1

**Document type:** Minimum tooling profile for first pilot  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

**Not bound to FP-0002** — apply via FW-04 readiness checklist.

---

## 1. Required tools

| Tool | Purpose |
|------|---------|
| Git, Node, npm, Gulp | Frontend build |
| Local (or Laragon via MLI) | Default WP environment — [MLI consumer profile](../../../mars-localhost-infrastructure/MARS-LOCALHOST-CONSUMER-MODEL-v1.md) |
| PHP 8.1+, MySQL | Runtime |
| WP-CLI | WP operations |
| PHPCS + WPCS | WV2 |
| Playwright | WV5, WV6 |
| zip + checksum | WV9 |

---

## 2. Required environment

| Item | Specification |
|------|---------------|
| Profile | Laragon via MARS Localhost Infrastructure (`E:\MARS-Localhost`) |
| OS | Windows 10+ |
| Isolation | One site per pilot under `sites\wordpress\projects\` or `synthetic\` |
| Secrets | `C:\AI MARS\local\` only |
| MLI manifest | Required per [runtime manifest contract](../../../mars-localhost-infrastructure/MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md) |

---

## 3. Required validation

| WV | Minimum |
|----|---------|
| WV0 | Handoff complete |
| WV1 | WAD approved |
| WV2 | PHPCS pass (critical) |
| WV3 | Template + ACF sync |
| WV4 | FW-S-07 blockers |
| WV5 | Smoke paths |
| WV6 | Visual diff + operator approval (PIXEL_PERFECT) |
| WV7 | Admin UX map |
| WV8 | Baseline axe + Lighthouse advisory |
| WV9 | Package lint + handoff |

---

## 4. Optional tools

PHPStan, PHPUnit, WPScan, BackstopJS, Stylelint, WP Playground (lightweight checks).

---

## 5. Prohibited operations

- Production deploy  
- Production DB mutation  
- Autonomous plugin install on live  
- Ungoverned `search-replace` on remote  
- Agent self-registration  

---

## 6. Operator gates

G1–G10 per lifecycle — minimum G1, G3, G6 (visual), G9, G10 for release.

---

## 7. WPilot boundary

Forge delivers **Release Candidate** → WPilot **ChangeSet** on DEV → operator validates → staging/production per WPilot policy.

---

## 8. FW-04 readiness checklist

| # | Check | Evidence |
|---|-------|----------|
| 1 | Local (or fallback) installed | Capability audit |
| 2 | PHP + WP-CLI on PATH | Version output |
| 3 | PHPCS + WPCS project ruleset | `phpcs --config-show` |
| 4 | Playwright browsers installed | `npx playwright install` |
| 5 | Frontend PRODUCTION PASS | Factory VL reports |
| 6 | FRONTEND workspace build green | `npm run build` log |
| 7 | WORDPRESS workspace scaffold | Path exists |
| 8 | STORAGE baselines path writable | Operator confirm |
| 9 | Project passport + mode declared | INTAKE artifact |
| 10 | No production credentials in scope | Secret scan |
| 11 | WPilot DEV target identified (if handoff test) | WPilot registry |
| 12 | Human operator assigned | Charter |

**All 12 required** before FW-05 implementation start.

---

## Related

- [reports/FORGE-WORDPRESS-FW-04-PILOT-INTAKE-INPUT-v1.md](reports/FORGE-WORDPRESS-FW-04-PILOT-INTAKE-INPUT-v1.md)
- [FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md](FORGE-WORDPRESS-LOCAL-ENVIRONMENT-DECISION-v1.md)

---

*Pilot tooling profile v1.*

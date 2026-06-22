# FWS-0001 — WPilot Handoff Simulation v2

**Document type:** WPilot handoff simulation  
**Version:** v2  
**Date:** 2026-06-23  
**Stage:** FW-05R (pre-RC2)  
**Case:** FWS-0001  
**Contract:** FW-C-03

---

## Simulation status

**DRAFT** — prepared after FW-05R live validation; RC2 packaging run pending.

---

## Package intent (RC2)

| Component | Source |
|-----------|--------|
| Theme | `fws-synthetic` |
| Plugin | `fws-synthetic-core` |
| ACF JSON | `wp-content/acf-json/` |
| Dependencies | ACF Free ≥ 6.8.4 |

---

## Install sequence (simulated)

1. Upload theme + plugin zips to target DEV/staging (WPilot scope)
2. Activate ACF Free if not present
3. Activate `fws-synthetic-core`, then theme `fws-synthetic`
4. Import acf-json field groups (sync on save)
5. Assign front page (home), contacts page, primary menu
6. Flush permalinks
7. Verify routes: `/`, `/services/`, `/contacts/`

---

## Validation bundle reference

Live validation reports under `VALIDATION/reports/` — FW-05R suite.

| Validator | Verdict |
|-----------|---------|
| FW-V-01 | PASS |
| FW-V-02 | PASS WITH LIMITATIONS |
| FW-V-03 | PASS |
| FW-V-04 | PASS WITH LIMITATIONS |
| FW-V-05 | PASS WITH DEVIATIONS (WV6 pending) |
| FW-V-06 | PASS WITH LIMITATIONS |
| FW-V-07 | PASS WITH LIMITATIONS (RC2 pending) |

---

## Rollback

Pre-install backup: `D:\MARS-Localhost\backups\wordpress\synthetic\fws-0001\pre-forge-fw05r`

---

## Operator gates before real handoff

| Gate | Status |
|------|--------|
| WV6 visual approval | **PENDING** |
| RC2 zip + manifest | **PENDING** |
| WPilot intake charter | **Not started** — FW-06 scope |

---

## Boundaries

- Simulation only — no WPilot runtime claim
- FP-0002 not included
- No production credentials

---

## Related

- [FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md](../../../../projects/mars-website-factory/subsystems/forge-wordpress/contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md)
- [FWS-0001-FW-V-07-RELEASE-AND-HANDOFF-LIVE-v1.md](../../VALIDATION/reports/FWS-0001-FW-V-07-RELEASE-AND-HANDOFF-LIVE-v1.md)

---

*WPilot handoff simulation v2 — FWS-0001 (pre-RC2).*

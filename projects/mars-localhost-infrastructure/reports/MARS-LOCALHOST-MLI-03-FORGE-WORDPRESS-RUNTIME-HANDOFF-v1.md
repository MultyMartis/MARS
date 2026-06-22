# MARS Localhost MLI-03 — Forge WordPress Runtime Handoff v1

**Document type:** Forge WordPress consumer handoff  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Git baseline:** commit `4621388` on `mars/post-cycle8-live-tests`

---

## Purpose

Document what Forge WordPress (FW) may rely on after MLI-03 synthetic WordPress profile validation — without overstating operational readiness.

---

## Handoff status

| Consumer | MLI-03 handoff | Notes |
|----------|----------------|-------|
| **Forge WordPress** | **PARTIAL — WITH LIMITATIONS** | Synthetic runtime exists; full Profile A re-validation remains **FW-05R** |
| **FP-0002** | **OUT OF SCOPE** | Explicit charter required |
| **FW-05R** | **HOLD** | Pending MLI-03 profile matrix acceptance |

---

## Proven for consumer reference

| Asset | Location / identifier |
|-------|----------------------|
| WordPress runtime | `D:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` |
| WordPress version | 7.0 |
| Local domain | `fws-0001.test` |
| Database naming | `fws0001` (standard) |
| Backup baseline | `D:\MARS-Localhost\backups\wordpress\synthetic\fws-0001\baseline-001` |
| WP-CLI | 2.12.0 — core installed, verify-checksums PASS |
| HTTP smoke | Front-end, admin login, REST — 200 via Host header |
| Playwright | 3/4 PASS (HTTPS blocked on hosts) |

---

## Not yet proven (consumer must not assume)

| Gap | Impact |
|-----|--------|
| `fws-0001.test` hosts elevation pending | Direct URL, some HTTPS/Playwright paths |
| `mysqlcheck` not on PATH | Full WP-CLI `db check` |
| MySQL X Protocol on 33060 all interfaces | Non-WordPress exposure surface |
| Restore drill not executed | Disaster-recovery confidence |
| Custom Forge theme/plugin stack | FW-05R scope |

---

## Recommended consumer next steps

1. Run elevated `add-mli-host.ps1` to register `fws-0001.test`.
2. Re-run Playwright HTTPS scenario; attach artefacts to FW-05R intake.
3. Complete FW-05R synthetic validation charter before declaring Profile A operational.

---

## Related

- [MARS-LOCALHOST-CONSUMER-MODEL-v1.md](../MARS-LOCALHOST-CONSUMER-MODEL-v1.md)
- [MARS-LOCALHOST-MLI-03-WORDPRESS-PROFILE-VALIDATION-MATRIX-v1.md](MARS-LOCALHOST-MLI-03-WORDPRESS-PROFILE-VALIDATION-MATRIX-v1.md)
- Forge: [FORGE-WORDPRESS-CAPABILITY-READINESS-MATRIX-v1.md](../../mars-website-factory/subsystems/forge-wordpress/capability/FORGE-WORDPRESS-CAPABILITY-READINESS-MATRIX-v1.md)

---

*Forge WordPress runtime handoff v1 — MLI-03.*

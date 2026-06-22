# MARS Localhost Infrastructure — Roadmap

**Program:** MARS Localhost Infrastructure (MLI)  
**Version:** v1.1  
**Date:** 2026-06-22

---

## Stages

| ID | Name | Status | Notes |
|----|------|--------|-------|
| **MLI-00** | Infrastructure Foundation | **COMPLETE** | Identity, boundaries, D: tree, policies, consumer model |
| **MLI-01** | Laragon Enablement | **COMPLETE** | Laragon reconciled; smoke site; toolchain baseline |
| **MLI-02** | Shared Toolchain Hardening | **NEXT** | Composer keys, HTTPS, PHPCompatibility, Playwright, hosts |
| **MLI-03** | WordPress Runtime Profile Validation | PLANNED | Synthetic proof on Laragon (e.g. FWS-0001) |
| **MLI-04** | OpenCart Runtime Profile Validation | PLANNED | ocStore synthetic proof |
| **MLI-05** | Generic PHP Simulation Profile | PLANNED | Webhook/API sim baseline |
| **MLI-06** | Consumer Integration | PLANNED | Forge FW-05R, OCPilot local hooks |

---

## Current block

```text
MLI-00 — COMPLETE
MLI-01 — COMPLETE
MLI-02 — NEXT
Laragon: ENABLED at D:\MARS-Localhost\laragon
WordPress profile proven on Laragon: NO (MLI-03)
OpenCart profile proven on Laragon: NO (MLI-04)
```

---

## MLI-02 scope note

MLI-01 delivered partial WP-CLI/PHPCS enablement. MLI-02 remains **required** for hardening — not silently skipped.

---

## Honesty

- Do **not** declare full CMS runtime operational until MLI-03 and/or MLI-04 evidence exists.
- FW-05 Playground proof remains historical; full Profile A re-validation is **MLI-03 / FW-05R**.

---

## Related

- [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)
- [reports/MARS-LOCALHOST-MLI-02-SHARED-TOOLCHAIN-HARDENING-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-02-SHARED-TOOLCHAIN-HARDENING-INPUT-v1.md)

---

*MLI roadmap v1.1 — post MLI-01.*

# MARS Localhost Infrastructure — Roadmap

**Program:** MARS Localhost Infrastructure (MLI)  
**Version:** v1.2  
**Date:** 2026-06-22

---

## Stages

| ID | Name | Status | Notes |
|----|------|--------|-------|
| **MLI-00** | Infrastructure Foundation | **COMPLETE** | Identity, boundaries, D: tree, policies, consumer model |
| **MLI-01** | Laragon Enablement | **COMPLETE** | Laragon reconciled; smoke site; toolchain baseline |
| **MLI-02** | Shared Toolchain Hardening | **COMPLETE** | Hosts model, HTTPS, PHPCS, Playwright, tool registry |
| **MLI-03** | WordPress Runtime Profile | **NEXT** | Synthetic WordPress on Laragon |
| **MLI-04** | OpenCart Runtime Profile | PLANNED | ocStore synthetic proof |
| **MLI-05** | Generic PHP Simulation Profile | PLANNED | Webhook/API sim baseline |
| **MLI-06** | Consumer Integration | PLANNED | Forge FW-05R, OCPilot local hooks |

---

## Current block

```text
MLI-00 — COMPLETE
MLI-01 — COMPLETE
MLI-02 — COMPLETE
MLI-03 — NEXT
Laragon: ENABLED at D:\MARS-Localhost\laragon
Shared toolchain: HARDENED
WordPress profile proven on Laragon: NO (MLI-03)
OpenCart profile proven on Laragon: NO (MLI-04)
```

---

## Honesty

- Do **not** declare full CMS runtime operational until MLI-03 and/or MLI-04 evidence exists.
- FW-05R live synthetic validation: **HOLD** until MLI-03.

---

## Related

- [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)
- [reports/MARS-LOCALHOST-MLI-03-WORDPRESS-RUNTIME-PROFILE-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-03-WORDPRESS-RUNTIME-PROFILE-INPUT-v1.md)

---

*MLI roadmap v1.2 — post MLI-02.*

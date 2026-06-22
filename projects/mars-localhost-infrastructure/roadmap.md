# MARS Localhost Infrastructure — Roadmap

**Program:** MARS Localhost Infrastructure (MLI)  
**Version:** v1  
**Date:** 2026-06-22

---

## Stages

| ID | Name | Status | Notes |
|----|------|--------|-------|
| **MLI-00** | Infrastructure Foundation | **COMPLETE** | Identity, boundaries, D: tree, policies, consumer model |
| **MLI-01** | Laragon Enablement | **NEXT** | Operator install; document root; smoke test |
| **MLI-02** | Toolchain Enablement | PLANNED | Composer, WP-CLI, PHPCS, Playwright paths |
| **MLI-03** | WordPress Runtime Profile Validation | PLANNED | Synthetic proof on Laragon (e.g. FWS-0001 re-run) |
| **MLI-04** | OpenCart Runtime Profile Validation | PLANNED | ocStore synthetic proof |
| **MLI-05** | Generic PHP Simulation Profile | PLANNED | Webhook/API sim baseline |
| **MLI-06** | Consumer Integration | PLANNED | Forge FW-05R, OCPilot local hooks |

---

## Current block

```text
MLI-00 — COMPLETE
MLI-01 — NEXT
Runtime operational: NO
WordPress profile proven on Laragon: NO
OpenCart profile proven on Laragon: NO
```

---

## Honesty

- Do **not** declare MLI operational until MLI-03 and/or MLI-04 evidence exists.
- MLI-01 requires **operator-controlled** Laragon installation — not agent-autonomous.
- FW-05 Playground proof remains historical; full Profile A re-validation is **MLI-03 / FW-05R**.

---

## Related

- [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)
- [reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md)

---

*MLI roadmap v1.*

# MARS Localhost Infrastructure — Roadmap

**Program:** MARS Localhost Infrastructure (MLI)  
**Version:** v1.3  
**Date:** 2026-06-23

---

## Stages

| ID | Name | Status | Notes |
|----|------|--------|-------|
| **MLI-00** | Infrastructure Foundation | **COMPLETE** | Identity, boundaries, D: tree, policies, consumer model |
| **MLI-01** | Laragon Enablement | **COMPLETE** | Laragon reconciled; smoke site; toolchain baseline |
| **MLI-02** | Shared Toolchain Hardening | **COMPLETE** | Hosts model, HTTPS, PHPCS, Playwright, tool registry |
| **MLI-03** | WordPress Runtime Profile | **COMPLETE** | MLI-WP-SYN-001 / FWS-0001 synthetic WordPress |
| **MLI-04** | OpenCart Runtime Profile | **NEXT / PLANNED** | ocStore synthetic proof |
| **MLI-05** | Generic PHP Simulation Profile | PLANNED | Webhook/API sim baseline |
| **MLI-06** | Consumer Integration | PLANNED | Forge FW-05R, OCPilot local hooks |

---

## Current block

```text
MLI-00 — COMPLETE
MLI-01 — COMPLETE
MLI-02 — COMPLETE
MLI-03 — COMPLETE
MLI-04 — NEXT (OpenCart lane; not blocking Forge FW-05R)
Laragon: ENABLED at D:\MARS-Localhost\laragon
Shared toolchain: HARDENED
WordPress profile: PROVEN WITH LIMITATIONS (MLI-WP-SYN-001)
OpenCart profile proven on Laragon: NO (MLI-04)
```

---

## Consumer lanes (independent)

```text
WordPress consumer lane:
  MLI-03 → Forge WordPress FW-05R (authorized)

OpenCart consumer lane:
  MLI-04 → future OCPilot integration
```

MLI-04 is **not** required before FW-05R.

---

## Honesty

- WordPress synthetic runtime is **proven with limitations** — see [validation matrix](reports/MARS-LOCALHOST-MLI-03-WORDPRESS-PROFILE-VALIDATION-MATRIX-v1.md).
- FW-05R live synthetic validation: **COMPLETE** (2026-06-23) — operator WV6 pending for `fws-0001.test` hosts optional.

---

## Related

- [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)
- [MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md](MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md)
- [manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md)

---

*MLI roadmap v1.3 — post MLI-03.*

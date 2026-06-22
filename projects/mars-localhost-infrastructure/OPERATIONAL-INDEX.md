# MARS Localhost Infrastructure — Operational Index

**Status:** documented navigation only — **not** a service registry or automated router.  
**Lane:** Infrastructure — shared local execution  
**Domain root:** [README.md](README.md)  
**Lifecycle:** ENABLEMENT (MLI-01 **COMPLETE**)

---

## Current status

| Field | Value |
|-------|-------|
| **Stage** | MLI-01 **COMPLETE** |
| **Next** | **MLI-02 — Shared Toolchain Hardening** |
| **Laragon** | **YES** — `D:\MARS-Localhost\laragon` (v8.6.1) |
| **Smoke site** | `http://mli-smoke-001.test/` (hosts elevation may be required) |
| **Runtime operational (CMS profiles)** | **NO** — until MLI-03/MLI-04 validation |
| **Brain root** | `C:\AI MARS` |
| **Runtime root** | `D:\MARS-Localhost` |
| **FW-05R** | **HOLD** — pending MLI-03 WordPress profile |

---

## Foundation documents

| # | Document |
|---|----------|
| 1 | [MARS-LOCALHOST-INFRASTRUCTURE-IDENTITY-v1.md](MARS-LOCALHOST-INFRASTRUCTURE-IDENTITY-v1.md) |
| 2 | [MARS-LOCALHOST-PHYSICAL-BOUNDARY-CONTRACT-v1.md](MARS-LOCALHOST-PHYSICAL-BOUNDARY-CONTRACT-v1.md) |
| 3 | [MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md](MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md) |
| 4 | [MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md](MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md) |
| 5 | [MARS-LOCALHOST-DOMAIN-STANDARD-v1.md](MARS-LOCALHOST-DOMAIN-STANDARD-v1.md) |
| 6 | [MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md](MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md) |
| 7 | [MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md](MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md) |
| 8 | [MARS-LOCALHOST-CONSUMER-MODEL-v1.md](MARS-LOCALHOST-CONSUMER-MODEL-v1.md) |
| 9 | [MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md](MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md) |
| 10 | [MARS-LOCALHOST-BACKUP-AND-RESET-POLICY-v1.md](MARS-LOCALHOST-BACKUP-AND-RESET-POLICY-v1.md) |
| 11 | [MARS-LOCALHOST-SERVICE-CONTROL-POLICY-v1.md](MARS-LOCALHOST-SERVICE-CONTROL-POLICY-v1.md) |
| 12 | [MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md](MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md) |

---

## MLI-01 decisions and reports

| Item | Path |
|------|------|
| Path reconciliation | [MARS-LOCALHOST-LARAGON-PATH-RECONCILIATION-v1.md](MARS-LOCALHOST-LARAGON-PATH-RECONCILIATION-v1.md) |
| Document root | [MARS-LOCALHOST-DOCUMENT-ROOT-DECISION-v1.md](MARS-LOCALHOST-DOCUMENT-ROOT-DECISION-v1.md) |
| Vhost model | [MARS-LOCALHOST-LARAGON-VHOST-MODEL-v1.md](MARS-LOCALHOST-LARAGON-VHOST-MODEL-v1.md) |
| Service profile | [MARS-LOCALHOST-SERVICE-PROFILE-v1.md](MARS-LOCALHOST-SERVICE-PROFILE-v1.md) |
| CLI standard | [MARS-LOCALHOST-CLI-ENVIRONMENT-STANDARD-v1.md](MARS-LOCALHOST-CLI-ENVIRONMENT-STANDARD-v1.md) |
| Vhost registry | [registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md](registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md) |
| Installation audit | [reports/MARS-LOCALHOST-MLI-01-LARAGON-INSTALLATION-AUDIT-v1.md](reports/MARS-LOCALHOST-MLI-01-LARAGON-INSTALLATION-AUDIT-v1.md) |
| Service verification | [reports/MARS-LOCALHOST-MLI-01-SERVICE-CONTROL-VERIFICATION-v1.md](reports/MARS-LOCALHOST-MLI-01-SERVICE-CONTROL-VERIFICATION-v1.md) |
| Toolchain audit | [reports/MARS-LOCALHOST-MLI-01-TOOLCHAIN-AUDIT-v1.md](reports/MARS-LOCALHOST-MLI-01-TOOLCHAIN-AUDIT-v1.md) |
| Browser smoke | [reports/MARS-LOCALHOST-MLI-01-BROWSER-SMOKE-REPORT-v1.md](reports/MARS-LOCALHOST-MLI-01-BROWSER-SMOKE-REPORT-v1.md) |
| MLI-02 input | [reports/MARS-LOCALHOST-MLI-02-SHARED-TOOLCHAIN-HARDENING-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-02-SHARED-TOOLCHAIN-HARDENING-INPUT-v1.md) |

---

## Roadmap and manifests

| Item | Path |
|------|------|
| Roadmap | [roadmap.md](roadmap.md) |
| MLI-01 input (historical) | [reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-01-LARAGON-ENABLEMENT-INPUT-v1.md) |
| Runtime manifests | [manifests/](manifests/) |
| Smoke manifest | [manifests/MLI-SMOKE-001-RUNTIME-MANIFEST-v1.md](manifests/MLI-SMOKE-001-RUNTIME-MANIFEST-v1.md) |

---

## Consumers (pointers)

| Consumer | Pointer |
|----------|---------|
| Forge WordPress | [../mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md](../mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md) |
| OCPilot | [../ocpilot/OPERATIONAL-INDEX.md](../ocpilot/OPERATIONAL-INDEX.md) |
| Website Factory | [../mars-website-factory/OPERATIONAL-INDEX.md](../mars-website-factory/OPERATIONAL-INDEX.md) |

---

## Next authorized action

**MLI-02 — Shared Toolchain Hardening** — see input report. **Do not** start WordPress synthetic validation until MLI-03.

---

*Operational index — MLI-01 complete.*

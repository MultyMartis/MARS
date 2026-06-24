# MARS Localhost Infrastructure — Operational Index

**Status:** documented navigation only — **not** a service registry or automated router.  
**Lane:** Infrastructure — shared local execution  
**Domain root:** [README.md](README.md)  
**Lifecycle:** ENABLEMENT (MLI-03 **COMPLETE**)

---

## Current status

| Field | Value |
|-------|-------|
| **Stage** | MLI-03 **COMPLETE** |
| **Next** | **MLI-04 — OpenCart Runtime Profile** (parallel lane; Forge **FW-06** waiting) |
| **Laragon** | **YES** — `D:\MARS-Localhost\laragon` (v8.6.1) |
| **Shared toolchain** | **HARDENED** — see tool registry |
| **Smoke site** | `http://mli-smoke-001.test/` — **PASS** |
| **WordPress synthetic** | `http://fws-0001.test/` — MLI-WP-SYN-001 **POST-REBOOT VALIDATED** (MLI-03R.1) |
| **WordPress project FP-0002** | `http://shpigovsky.test/` — MLI-WP-FP0002-LOCAL **READY — POST-REBOOT VALIDATED** (MLI-03R.1) |
| **Runtime operational (WordPress)** | **YES** — synthetic profile with limitations |
| **Runtime operational (OpenCart)** | **NO** — until MLI-04 |
| **Brain root** | `C:\AI MARS` |
| **Runtime root** | `D:\MARS-Localhost` |
| **FW-05R** | **COMPLETE** — see [FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md](../mars-website-factory/subsystems/forge-wordpress/capability/reports/FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md) |

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
| 6b | [MARS-LOCALHOST-DATABASE-STANDARD-v1.md](MARS-LOCALHOST-DATABASE-STANDARD-v1.md) — provisioning (MLI-03R.1) |
| 7 | [MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md](MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md) |
| 8 | [MARS-LOCALHOST-CONSUMER-MODEL-v1.md](MARS-LOCALHOST-CONSUMER-MODEL-v1.md) |
| 9 | [MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md](MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md) |
| 10 | [MARS-LOCALHOST-BACKUP-AND-RESET-POLICY-v1.md](MARS-LOCALHOST-BACKUP-AND-RESET-POLICY-v1.md) |
| 11 | [MARS-LOCALHOST-SERVICE-CONTROL-POLICY-v1.md](MARS-LOCALHOST-SERVICE-CONTROL-POLICY-v1.md) |
| 12 | [MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md](MARS-LOCALHOST-LARAGON-PLACEMENT-DECISION-v1.md) |

---

## MLI-02 standards and reports

| Item | Path |
|------|------|
| Hosts management | [MARS-LOCALHOST-HOSTS-MANAGEMENT-STANDARD-v1.md](MARS-LOCALHOST-HOSTS-MANAGEMENT-STANDARD-v1.md) |
| Vhost provisioning | [MARS-LOCALHOST-VHOST-PROVISIONING-STANDARD-v1.md](MARS-LOCALHOST-VHOST-PROVISIONING-STANDARD-v1.md) |
| Local certificates | [MARS-LOCALHOST-LOCAL-CERTIFICATE-STANDARD-v1.md](MARS-LOCALHOST-LOCAL-CERTIFICATE-STANDARD-v1.md) |
| Composer | [MARS-LOCALHOST-COMPOSER-STANDARD-v1.md](MARS-LOCALHOST-COMPOSER-STANDARD-v1.md) |
| WP-CLI | [MARS-LOCALHOST-WPCLI-STANDARD-v1.md](MARS-LOCALHOST-WPCLI-STANDARD-v1.md) |
| PHPCS/WPCS | [MARS-LOCALHOST-PHPCS-WPCS-STANDARD-v1.md](MARS-LOCALHOST-PHPCS-WPCS-STANDARD-v1.md) |
| Node/npm | [MARS-LOCALHOST-NODE-AND-NPM-STANDARD-v1.md](MARS-LOCALHOST-NODE-AND-NPM-STANDARD-v1.md) |
| MySQL credentials | [MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md](MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md) |
| Smoke suite | [MARS-LOCALHOST-SMOKE-SUITE-v1.md](MARS-LOCALHOST-SMOKE-SUITE-v1.md) |
| Upgrade policy | [MARS-LOCALHOST-TOOLCHAIN-VERSION-AND-UPGRADE-POLICY-v1.md](MARS-LOCALHOST-TOOLCHAIN-VERSION-AND-UPGRADE-POLICY-v1.md) |
| Tool registry | [registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md](registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md) |
| MLI-02 toolchain audit | [reports/MARS-LOCALHOST-MLI-02-TOOLCHAIN-STATE-AUDIT-v1.md](reports/MARS-LOCALHOST-MLI-02-TOOLCHAIN-STATE-AUDIT-v1.md) |
| MLI-02 smoke report | [reports/MARS-LOCALHOST-MLI-02-SMOKE-SUITE-REPORT-v1.md](reports/MARS-LOCALHOST-MLI-02-SMOKE-SUITE-REPORT-v1.md) |
| MLI-03 input | [reports/MARS-LOCALHOST-MLI-03-WORDPRESS-RUNTIME-PROFILE-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-03-WORDPRESS-RUNTIME-PROFILE-INPUT-v1.md) |

---

## MLI-03 WordPress standards and reports

| Item | Path |
|------|------|
| WordPress runtime profile | [MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md](MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md) |
| Directory standard | [MARS-LOCALHOST-WORDPRESS-DIRECTORY-STANDARD-v1.md](MARS-LOCALHOST-WORDPRESS-DIRECTORY-STANDARD-v1.md) |
| Baseline configuration | [MARS-LOCALHOST-WORDPRESS-BASELINE-CONFIGURATION-STANDARD-v1.md](MARS-LOCALHOST-WORDPRESS-BASELINE-CONFIGURATION-STANDARD-v1.md) |
| Local guard (MU-plugin) | [MARS-LOCALHOST-WORDPRESS-LOCAL-GUARD-STANDARD-v1.md](MARS-LOCALHOST-WORDPRESS-LOCAL-GUARD-STANDARD-v1.md) |
| WordPress runtime registry | [registries/MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md](registries/MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md) |
| WP manifest | [manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md) |
| Validation matrix | [reports/MARS-LOCALHOST-MLI-03-WORDPRESS-PROFILE-VALIDATION-MATRIX-v1.md](reports/MARS-LOCALHOST-MLI-03-WORDPRESS-PROFILE-VALIDATION-MATRIX-v1.md) |
| Forge handoff | [reports/MARS-LOCALHOST-MLI-03-FORGE-WORDPRESS-RUNTIME-HANDOFF-v1.md](reports/MARS-LOCALHOST-MLI-03-FORGE-WORDPRESS-RUNTIME-HANDOFF-v1.md) |

---

## MLI-03R.2 duplicate MySQL process closure (2026-06-24)

| Item | Path |
|------|------|
| Process identity audit | [reports/MARS-LOCALHOST-MLI-03R2-MYSQL-PROCESS-IDENTITY-AUDIT-v1.md](reports/MARS-LOCALHOST-MLI-03R2-MYSQL-PROCESS-IDENTITY-AUDIT-v1.md) |
| Closure report | [reports/MARS-LOCALHOST-MLI-03R2-DUPLICATE-MYSQL-PROCESS-CLOSURE-v1.md](reports/MARS-LOCALHOST-MLI-03R2-DUPLICATE-MYSQL-PROCESS-CLOSURE-v1.md) |
| Post-reboot procedure | [reports/MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md](reports/MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md) |

**MySQL process state:** NORMAL — VERIFIED MULTI-PROCESS INTERNAL MODEL (single canonical server on `127.0.0.1:3306`).

---

## MLI-03R.1 post-reboot remediation (2026-06-24)

| Item | Path |
|------|------|
| Master incident report | [reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md](reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md) |
| Active config audit | [reports/MARS-LOCALHOST-MLI-03R1-ACTIVE-MYSQL-CONFIG-AUDIT-v1.md](reports/MARS-LOCALHOST-MLI-03R1-ACTIVE-MYSQL-CONFIG-AUDIT-v1.md) |
| Network hardening | [reports/MARS-LOCALHOST-MLI-03R1-MYSQL-POST-REBOOT-NETWORK-HARDENING-v1.md](reports/MARS-LOCALHOST-MLI-03R1-MYSQL-POST-REBOOT-NETWORK-HARDENING-v1.md) |
| Database provisioning standard | [MARS-LOCALHOST-DATABASE-STANDARD-v1.md](MARS-LOCALHOST-DATABASE-STANDARD-v1.md) |
| Provisioning script | [scripts/provision-mli-wordpress-db.ps1](scripts/provision-mli-wordpress-db.ps1) |

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
| WordPress manifest | [manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md) |

---

## Consumers (pointers)

| Consumer | Pointer |
|----------|---------|
| Forge WordPress | [../mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md](../mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md) |
| OCPilot | [../ocpilot/OPERATIONAL-INDEX.md](../ocpilot/OPERATIONAL-INDEX.md) |
| Website Factory | [../mars-website-factory/OPERATIONAL-INDEX.md](../mars-website-factory/OPERATIONAL-INDEX.md) |

---

## Next authorized action

**Forge WordPress FW-05R — Live Synthetic Runtime Validation** — **COMPLETE** (2026-06-23) — [FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md](../mars-website-factory/subsystems/forge-wordpress/capability/reports/FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md).

Parallel infrastructure lane: **MLI-04 — OpenCart Runtime Profile** (not blocking FW-05R).

---

*Operational index — MLI-03 complete.*

# MARS Localhost Infrastructure — Operational Index

**Status:** documented navigation only — **not** a service registry or automated router.  
**Lane:** Infrastructure — shared local execution  
**Domain root:** [README.md](README.md)  
**Lifecycle:** ENABLEMENT (MLI-03 **COMPLETE**)

---

## 1. Identity and authority

| Field | Value |
|-------|-------|
| **Canonical name** | MARS Localhost Infrastructure (MLI) |
| **Class** | Shared **universal** local development infrastructure — WordPress, OpenCart, PHP smoke sites, synthetic validation; **not** WordPress-only |
| **Production authority** | **NONE** — local operator-controlled execution only |
| **Brain root (governance)** | `C:\MARS Phenix\AI MARS` |
| **Runtime root (execution)** | `E:\MARS-Localhost` |
| **Bulk support** | `C:\MARS Phenix\AI MARS STORAGE` — optional archives; **not** live runtime root |

**Mandatory formulation** ([MARS-LOCALHOST-INFRASTRUCTURE-IDENTITY-v1.md](MARS-LOCALHOST-INFRASTRUCTURE-IDENTITY-v1.md)):

```text
C:\MARS Phenix\AI MARS governs.
E:\MARS-Localhost executes.
```

MLI is an **execution environment**. It is **not** the MARS brain, governance source, project registry, or Git authority.

| Field | Value |
|-------|-------|
| **Stage** | MLI-03 **COMPLETE** |
| **Next** | **MLI-04 — OpenCart Runtime Profile** (parallel lane; Forge **FW-06** waiting) |
| **FW-05R** | **COMPLETE** — [FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md](../mars-website-factory/subsystems/forge-wordpress/capability/reports/FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md) |

---

## 2. Recovery warning

**Post-incident reconciliation (2026-06-24):** MLI-03R.1–R.3 document MySQL 8.4 migration, wrong-datadir incident, Laragon `my.ini` authority, and cold-start persistence. **Do not** delete the historical `mysql-8.4` directory. **Do not** assume full Windows reboot validation is complete until operator retest per [MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md](reports/MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md).

**AG-WP-001 / WPilot bridge:** **not claimed** as live runtime in this index. Forge WordPress consumer validation references synthetic FWS-0001 only.

---

## 3. Architecture and roots

| Zone | Path | Role |
|------|------|------|
| **Brain** | `C:\MARS Phenix\AI MARS` | Governance, manifests, pointers, validation reports (Git) |
| **Runtime** | `E:\MARS-Localhost` | Laragon, CMS sites, databases, uploads, logs (**outside Git**) |
| **Laragon** | `E:\MARS-Localhost\laragon` (v8.6.1) | Service control — Laragon-generated `my.ini` is **active config authority** |
| **Canonical historical datadir** | `mysql-8.4.3` under Laragon data | Wrong-datadir incident remediated — see MLI-03R.1 |
| **Recovery script** | `E:\MARS-Localhost\tools\recover-mli-mysql-datadir.ps1` | Datadir recovery — active path on E:; historical D: references preserved in MLI-03R.* reports |

**Drive-letter note:** Historical `D:\MARS-Localhost` paths remain in MLI-03R.* incident evidence. Active operator runtime root confirmed on **`E:\MARS-Localhost`** (2026-06-25 post-cutover reconciliation).

---

## 4. Capability and consumers

| Capability | State |
|------------|-------|
| **Shared toolchain** | **HARDENED** — [registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md](registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md) |
| **Smoke site** | `http://mli-smoke-001.test/` — **PASS** |
| **WordPress synthetic (FWS-0001)** | `http://fws-0001.test/` — MLI-WP-SYN-001 **CURRENT SESSION RESTORED** (MLI-03R.3); FW-05R synthetic validation complete |
| **WordPress project FP-0002** | `http://shpigovsky.test/` — MLI-WP-FP0002-LOCAL **READY — CURRENT SESSION RESTORED** (MLI-03R.3) |
| **Runtime operational (WordPress)** | **YES** — synthetic + project profiles with documented limitations |
| **Runtime operational (OpenCart)** | **NO** — until MLI-04 |

**Forge consumer:** [../mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md](../mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md) — MLI provides runtime surface; Forge owns promotion semantics.

---

## 5. Chronological phase and checkpoint history

| Phase | Status | Key pointer |
|-------|--------|-------------|
| **MLI-01** | Complete | [reports/MARS-LOCALHOST-MLI-01-LARAGON-INSTALLATION-AUDIT-v1.md](reports/MARS-LOCALHOST-MLI-01-LARAGON-INSTALLATION-AUDIT-v1.md) |
| **MLI-02** | Complete | [reports/MARS-LOCALHOST-MLI-02-SMOKE-SUITE-REPORT-v1.md](reports/MARS-LOCALHOST-MLI-02-SMOKE-SUITE-REPORT-v1.md) |
| **MLI-03** | Complete | WordPress runtime profile — [MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md](MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md) |
| **MLI-03R.1** | Complete (2026-06-24) | MySQL 8.4 auth remediation — [reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md](reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md) |
| **MLI-03R.2** | Complete (2026-06-24) | Duplicate MySQL process closure — [reports/MARS-LOCALHOST-MLI-03R2-DUPLICATE-MYSQL-PROCESS-CLOSURE-v1.md](reports/MARS-LOCALHOST-MLI-03R2-DUPLICATE-MYSQL-PROCESS-CLOSURE-v1.md) |
| **MLI-03R.3** | Complete (2026-06-24) | Laragon cold-start datadir persistence — [reports/MARS-LOCALHOST-MLI-03R3-LARAGON-REBOOT-DATADIR-PERSISTENCE-v1.md](reports/MARS-LOCALHOST-MLI-03R3-LARAGON-REBOOT-DATADIR-PERSISTENCE-v1.md) |
| **MLI-04** | Planned | OpenCart runtime profile |

Forward commits (FP-0002 WordPress foundation): `11e9155`, `f003fe8`, `a5a7de0`, `266e2a8` — authority preserved in current HEAD documentation.

---

## 6. Current MySQL authority model

| Item | Authority |
|------|-----------|
| **Server** | Single canonical MySQL 8.4 on `127.0.0.1:3306` |
| **Process model** | Two `mysqld.exe` processes = **parent/child internal model** (NORMAL — verified MLI-03R.2) |
| **Authentication** | `caching_sha2_password` remains **valid** for MLI app users |
| **Active config** | Laragon-generated `my.ini` — see [reports/MARS-LOCALHOST-MLI-03R1-ACTIVE-MYSQL-CONFIG-AUDIT-v1.md](reports/MARS-LOCALHOST-MLI-03R1-ACTIVE-MYSQL-CONFIG-AUDIT-v1.md) |
| **Datadir** | Canonical `mysql-8.4.3`; old `mysql-8.4` directory **must not be deleted** |
| **Provisioning** | [MARS-LOCALHOST-DATABASE-STANDARD-v1.md](MARS-LOCALHOST-DATABASE-STANDARD-v1.md) · [scripts/provision-mli-wordpress-db.ps1](scripts/provision-mli-wordpress-db.ps1) |
| **Network hardening** | [reports/MARS-LOCALHOST-MLI-03R1-MYSQL-POST-REBOOT-NETWORK-HARDENING-v1.md](reports/MARS-LOCALHOST-MLI-03R1-MYSQL-POST-REBOOT-NETWORK-HARDENING-v1.md) |

---

## 7. Validation gates

| Gate | Status |
|------|--------|
| MLI-02 smoke suite | **PASS** |
| MLI-03 WordPress profile matrix | **PASS** — [reports/MARS-LOCALHOST-MLI-03-WORDPRESS-PROFILE-VALIDATION-MATRIX-v1.md](reports/MARS-LOCALHOST-MLI-03-WORDPRESS-PROFILE-VALIDATION-MATRIX-v1.md) |
| FW-05R live synthetic validation | **COMPLETE** (2026-06-23) |
| FWS-0001 synthetic (MLI-WP-SYN-001) | **VALIDATED** — manifest [manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md) |
| Laragon cold-start persistence | **PROVEN** (MLI-03R.3) |
| **Full Windows reboot** | **PENDING OPERATOR RETEST** — separate validation gate; **not proven** in this index |

---

## 8. Runtime consumers (pointers)

| Consumer | Pointer |
|----------|---------|
| Forge WordPress | [../mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md](../mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md) |
| OCPilot | [../ocpilot/OPERATIONAL-INDEX.md](../ocpilot/OPERATIONAL-INDEX.md) |
| Website Factory | [../mars-website-factory/OPERATIONAL-INDEX.md](../mars-website-factory/OPERATIONAL-INDEX.md) |

---

## 9. Risks and prohibitions

- **No production authority** — MLI is local-only; no client production access claimed.
- **No secrets in Git** — credentials in `local/mli/` env files or external storage only.
- **No automatic datadir deletion** — preserve `mysql-8.4` historical directory.
- **No conflation of governance and runtime** — manifests in Git point to runtime; runtime state stays on D:.
- **No AG-WP-001 runtime claim** without separate promotion evidence.

---

## 10. Deferred decisions

| Item | Status |
|------|--------|
| MLI-04 OpenCart runtime profile | Planned — parallel to Forge FW-06 |
| Physical drive-letter reconciliation (D: vs E:) | **Deferred** — historical paths unchanged in documentation |
| Full Windows reboot operator retest | **Pending** |
| MLI-04 blocking Forge | **No** — FW-05R complete; MLI-04 parallel |

**Next authorized action:** Parallel infrastructure lane **MLI-04 — OpenCart Runtime Profile** (not blocking FW-05R).

---

## 11. Evidence and report links

### Foundation documents

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

### MLI-02 standards and reports

| Item | Path |
|------|------|
| Tool registry | [registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md](registries/MARS-LOCALHOST-TOOL-REGISTRY-v1.md) |
| MLI-02 toolchain audit | [reports/MARS-LOCALHOST-MLI-02-TOOLCHAIN-STATE-AUDIT-v1.md](reports/MARS-LOCALHOST-MLI-02-TOOLCHAIN-STATE-AUDIT-v1.md) |
| MLI-02 smoke report | [reports/MARS-LOCALHOST-MLI-02-SMOKE-SUITE-REPORT-v1.md](reports/MARS-LOCALHOST-MLI-02-SMOKE-SUITE-REPORT-v1.md) |
| MLI-03 input | [reports/MARS-LOCALHOST-MLI-03-WORDPRESS-RUNTIME-PROFILE-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-03-WORDPRESS-RUNTIME-PROFILE-INPUT-v1.md) |

### MLI-03 WordPress standards and reports

| Item | Path |
|------|------|
| WordPress runtime profile | [MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md](MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md) |
| WordPress runtime registry | [registries/MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md](registries/MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md) |
| WP manifest (FWS-0001) | [manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md) |
| Validation matrix | [reports/MARS-LOCALHOST-MLI-03-WORDPRESS-PROFILE-VALIDATION-MATRIX-v1.md](reports/MARS-LOCALHOST-MLI-03-WORDPRESS-PROFILE-VALIDATION-MATRIX-v1.md) |
| Forge handoff | [reports/MARS-LOCALHOST-MLI-03-FORGE-WORDPRESS-RUNTIME-HANDOFF-v1.md](reports/MARS-LOCALHOST-MLI-03-FORGE-WORDPRESS-RUNTIME-HANDOFF-v1.md) |

### MLI-03R remediation reports

| Item | Path |
|------|------|
| MLI-03R.3 datadir persistence | [reports/MARS-LOCALHOST-MLI-03R3-LARAGON-REBOOT-DATADIR-PERSISTENCE-v1.md](reports/MARS-LOCALHOST-MLI-03R3-LARAGON-REBOOT-DATADIR-PERSISTENCE-v1.md) |
| MLI-03R.2 process closure | [reports/MARS-LOCALHOST-MLI-03R2-DUPLICATE-MYSQL-PROCESS-CLOSURE-v1.md](reports/MARS-LOCALHOST-MLI-03R2-DUPLICATE-MYSQL-PROCESS-CLOSURE-v1.md) |
| MLI-03R.1 auth remediation | [reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md](reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md) |
| Post-reboot procedure | [reports/MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md](reports/MARS-LOCALHOST-POST-REBOOT-VERIFICATION-PROCEDURE-v1.md) |

### Roadmap and manifests

| Item | Path |
|------|------|
| Roadmap | [roadmap.md](roadmap.md) |
| Smoke manifest | [manifests/MLI-SMOKE-001-RUNTIME-MANIFEST-v1.md](manifests/MLI-SMOKE-001-RUNTIME-MANIFEST-v1.md) |

---

*Operational index — MLI-03 complete; MLI-03R remediation reconciled (Wave 4).*

# MLI-WP-SYN-001 — Runtime Manifest v1

**Document type:** Runtime manifest (brain SoT)  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Contract:** [MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md](../MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md)

---

## Identity

| Field | Value |
|-------|-------|
| **Runtime ID** | MLI-WP-SYN-001 |
| **Project / synthetic ID** | FWS-0001 |
| **Runtime class** | synthetic |
| **Platform** | wordpress |
| **Current status** | `active` |
| **Production target** | **NONE** |

---

## Paths and URLs

| Field | Value |
|-------|-------|
| **MARS authority path** | `X:\AI MARS\projects\mars-localhost-infrastructure\manifests\MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md` |
| **Consumer authority pointer** | `workspaces/forge-wordpress-synthetic/FWS-0001/` (Forge handoff — not MLI SoT) |
| **Local runtime path** | `X:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` |
| **Local URL (HTTP)** | `http://fws-0001.test/` |
| **Local URL (HTTPS)** | `https://fws-0001.test/` |
| **Canonical URL** | `http://fws-0001.test/` |
| **Junction** | `X:\MARS-Localhost\laragon\www\fws-0001` |
| **Vhost registry** | [MARS-LOCALHOST-VHOST-REGISTRY-v1.md](../registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md) |
| **WordPress runtime registry** | [MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md](../registries/MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md) |

---

## Runtime stack

| Field | Value |
|-------|-------|
| **WordPress version** | 7.0 |
| **Locale** | ru_RU |
| **PHP version** | 8.3.30 |
| **DB ID** | `mars_wp_fws0001` |
| **DB user** | `mli_fws0001_app` (@127.0.0.1 / localhost only) |
| **DB version** | MySQL 8.4.3 |
| **DB host** | 127.0.0.1 |
| **Table prefix** | `mli_` |
| **Web server** | Apache 2.4.66 |
| **mod_rewrite** | enabled |
| **MySQL bind-address** | 127.0.0.1 (hardened) |
| **MySQL X Protocol** | disabled (`mysqlx=0`) |
| **WP-CLI** | 2.12.0 — `X:\MARS-Localhost\tools\wp-cli\` |

---

## Ownership

| Field | Value |
|-------|-------|
| **Runtime owner** | MARS Localhost Infrastructure (operator) |
| **Implementation owner** | forge-wordpress |
| **Operations owner** | Operator |
| **Production target** | **NONE** |

---

## Secrets and configuration

| Field | Value |
|-------|-------|
| **Secrets location** | `X:\AI MARS\local\mli\fws-0001\runtime.env` |
| **Secrets in manifest** | **Prohibited** — location only |
| **wp-config** | `X:\MARS-Localhost\sites\wordpress\synthetic\fws-0001\wp-config.php` |
| **Debug** | WP_DEBUG on; log on; display off (synthetic default) |

Configuration standard: [MARS-LOCALHOST-WORDPRESS-BASELINE-CONFIGURATION-STANDARD-v1.md](../MARS-LOCALHOST-WORDPRESS-BASELINE-CONFIGURATION-STANDARD-v1.md)

---

## Packages (current state — post FW-05R)

| Package | Status |
|---------|--------|
| WordPress core 7.0 ru_RU | installed |
| Default bundled theme | present |
| **Forge theme `fws-synthetic`** | **installed, active** |
| **Forge plugin `fws-synthetic-core`** | **installed, active** |
| ACF Free 6.8.4 | **installed, active** |

---

## Network validation

| Check | Result | Notes |
|-------|--------|-------|
| HTTP smoke | **PASS** (with Host header or hosts) | WordPress front/admin reachable |
| Hosts `mli-smoke-001.test` | **PASS** | Shared MLI managed block |
| Hosts `fws-0001.test` | **PENDING ELEVATION** | FW-05R closure 2026-06-23: `add-mli-host.ps1` exit 3; Host-header smoke PASS; direct URL NOT EXECUTED |
| HTTPS cert generated | **YES** | `laragon\etc\ssl\fws-0001.test.crt` |
| HTTPS smoke (Playwright) | **PASS WITH UNTRUSTED LOCAL CA** | `ignoreHTTPSErrors: true` — MLI-02 pattern |
| WP-CLI checksums | verify on consumer handoff | `wp core verify-checksums` |

---

## State

| Field | Value |
|-------|-------|
| **Backup state** | `pre-forge-fw05r` — `X:\MARS-Localhost\backups\wordpress\synthetic\fws-0001\pre-forge-fw05r` |
| **Rollback state** | pre-forge-fw05r available |
| **Last validation** | 2026-06-23 — FW-05R Forge live synthetic validation |
| **MLI-03R.1 post-reboot** | 2026-06-24 — `wp db check` PASS; HTTP 200; MySQL loopback restored — [report](../../reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md) |
| **MLI-03R.3 Laragon cold-start** | 2026-06-24 — datadir drift remediated; session + 2× cold-start **PASS** — [report](../../reports/MARS-LOCALHOST-MLI-03R3-LARAGON-REBOOT-DATADIR-PERSISTENCE-v1.md) |
| **Last validation report** | [FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md](../../mars-website-factory/subsystems/forge-wordpress/capability/reports/FORGE-WORDPRESS-FW-05R-LIVE-SYNTHETIC-VALIDATION-REPORT-v1.md) |

---

## Lifecycle notes

| Topic | Detail |
|-------|--------|
| **Purpose** | Synthetic WordPress capability proof for Forge FWS-0001 |
| **Data class** | Synthetic fixtures only — no client PII |
| **Reset** | Permitted after evidence archived per backup policy |
| **FW-05R** | Consumer validation **COMPLETE** (2026-06-23) — PROVEN WITH LIMITATIONS; WV6 pending; direct domain gate pending hosts elevation |
| **Forge consumer** | Implementation consumer only — MLI remains runtime provider |
| **FP-0002** | **Out of scope** — separate future `projects` runtime |

---

## Machine-readable skeleton (reference)

```json
{
  "runtime_id": "MLI-WP-SYN-001",
  "project_synthetic_id": "FWS-0001",
  "runtime_class": "synthetic",
  "platform": "wordpress",
  "mars_authority_path": "projects/mars-localhost-infrastructure/manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md",
  "local_runtime_path": "D:\\MARS-Localhost\\sites\\wordpress\\synthetic\\fws-0001",
  "local_url": "http://fws-0001.test",
  "local_url_https": "https://fws-0001.test",
  "database_id": "mars_wp_fws0001",
  "database_user": "mli_fws0001_app",
  "table_prefix": "mli_",
  "wordpress_version": "7.0",
  "locale": "ru_RU",
  "php_version": "8.3.30",
  "db_version": "MySQL 8.4.3",
  "web_server": "apache",
  "runtime_owner": "operator",
  "implementation_owner": "forge-wordpress",
  "operations_owner": "operator",
  "production_target": "NONE",
  "backup_state": "pre-forge-fw05r",
  "rollback_state": "pre-forge-fw05r",
  "secrets_location": "C:\\AI MARS\\local\\mli\\fws-0001\\runtime.env",
  "current_status": "active",
  "last_validation": "2026-06-23"
}
```

---

## Related

- [MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md](../MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md)
- [MARS-LOCALHOST-WORDPRESS-LOCAL-GUARD-STANDARD-v1.md](../MARS-LOCALHOST-WORDPRESS-LOCAL-GUARD-STANDARD-v1.md)
- [MARS-LOCALHOST-CONSUMER-MODEL-v1.md](../MARS-LOCALHOST-CONSUMER-MODEL-v1.md)

---

*Runtime manifest v1 — MLI-WP-SYN-001.*

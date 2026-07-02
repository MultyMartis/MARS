# MLI X-Drive WordPress Runtime Controlled Remediation — Receipt v1

**Date:** 2026-06-30  
**Task:** MLI X-DRIVE WORDPRESS RUNTIME CONTROLLED REMEDIATION  
**Authority:** `X:\MARS-Localhost\` (runtime) · `X:\AI MARS\` (governance)  
**Branch:** `mars/canonical-post-recovery` @ `880dc945ef03b38f1327228a0c9a4923d16de5af`

---

## Summary

Controlled remediation restored a functional X-native Laragon WordPress runtime after post-migration loss of MySQL datadir, Apache vhosts, and `www` junctions. Clean MySQL 8.4.3 datadir provisioned; approved SQL dumps imported; site mappings and vhosts recreated; HTTP and WP-CLI validation **PASS** via `Host` header tests.

---

## Checkpoint

| Field | Value |
|-------|-------|
| **Path** | `X:\MARS-Localhost\backups\runtime\MLI-X-REMEDIATION-PRECHANGE-20260630-003850` |
| **Scope** | `laragon\data`, `laragon\etc`, `laragon\www`, `laragon\usr\tpl`, `tools` |
| **Rollback** | Restore scoped surfaces from checkpoint; stop X Laragon; replace `httpd.conf` / `my.ini` from checkpoint if needed |

### SQL dump hashes (SHA-256)

| Dump | Hash |
|------|------|
| `mars_wp_fws0001.sql` | `AC672E8BE8DA9D46A032F90CC9B3D1AF24983A8684CFFA001438BC6739B71FD6` |
| `mars_wp_fp0002.sql` | `86371FAFAE8F566BF6F2AEB07274E1B4D49018A1AE03CFEC795E2DF52E0A0962` |

---

## Runtime restored

| Component | Path / state |
|-----------|--------------|
| **MySQL datadir** | `X:\MARS-Localhost\laragon\data\mysql-8.4.3\` (clean initialize-insecure + import) |
| **MySQL config** | `recover-mli-mysql-datadir.ps1 -Apply` + read-only `bin\my.ini` |
| **www junctions** | `fws-0001`, `shpigovsky`, `mli-smoke-001` → canonical `sites\` paths |
| **Apache vhosts** | `laragon\etc\apache2\sites-enabled\` (HTTP only; SSL deferred) |
| **Apache integration** | MLI includes appended to `bin\apache\...\conf\httpd.conf`; `mod_rewrite` enabled |

---

## Validation (2026-06-30 session)

| Site | HTTP `/` | HTTP `/wp-login.php` | WP-CLI | Theme | Core plugin |
|------|----------|----------------------|--------|-------|-------------|
| **FWS-0001** | 200 | 200 | PASS | `fws-synthetic` | `fws-synthetic-core` |
| **Shpigovsky** | 200 | 200 | PASS | `shpigovsky` | `shpigovsky-core` |
| **MLI smoke** | 200 | n/a | n/a | n/a | n/a |

**Stop/start persistence:** second cold start of MySQL + Apache repeated all HTTP checks **200**.

---

## Pending / operator follow-up

| Item | Status |
|------|--------|
| **Windows hosts** (`.test` domains) | **COMPLETE** (2026-07-02) — three entries added; receipt [MARS-LOCALHOST-MLI-HOSTS-REBOOT-PERSISTENCE-20260702-v1.md](MARS-LOCALHOST-MLI-HOSTS-REBOOT-PERSISTENCE-20260702-v1.md) |
| **Full Windows reboot** | **VERIFIED** (2026-07-02) — same receipt |
| **SSL certificates** | **Deferred** — not regenerated |
| **FW-07C-1 baseline** | **REVALIDATION_REQUIRED** — runtime rebuilt; Forge frozen baseline unchanged |
| **Canonical `runtime.env` on `X:\AI MARS\local\mli\`** | **Pending** — path absent; credentials reconciled from MLI-03R1 backup env files during import |

---

## Safety

- E-drive source: read-only vhost reference only  
- Old Laragon/MySQL: **NOT EXECUTED**  
- Old raw datadir: **NOT COPIED**  
- FP-0002 frontend / Forge contracts: **NOT CHANGED**

---

*Remediation receipt v1 — MLI X-drive controlled recovery 2026-06-30.*

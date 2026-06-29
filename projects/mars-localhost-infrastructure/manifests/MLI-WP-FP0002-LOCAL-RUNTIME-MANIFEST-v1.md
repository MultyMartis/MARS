# MLI-WP-FP0002-LOCAL — Runtime Manifest v1

**Document type:** WordPress runtime manifest  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** FW-06A / FW-06A.1 — **COMPLETE**

---

## Identity

| Field | Value |
|-------|-------|
| **Runtime ID** | MLI-WP-FP0002-LOCAL |
| **Project ID** | FP-0002 |
| **Project** | Шпиговский |
| **Platform** | WordPress |
| **Class** | `projects` / `local` |
| **Brain authority** | `X:\AI MARS` |
| **Physical root** | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky` |
| **Junction** | `X:\MARS-Localhost\laragon\www\shpigovsky` |
| **Local URL** | `http://shpigovsky.test` |
| **Database** | `mars_wp_fp0002` |
| **DB user** | `mli_shpigovsky_app` |
| **Table prefix** | `fp02_` |
| **Credentials class** | `X:\AI MARS\local\mli\fp-0002\runtime.env` |
| **Production target** | **NONE** |

---

## Stack (verified FW-06A)

| Component | Version |
|-----------|---------|
| WordPress | 7.0 (ru_RU) |
| PHP | 8.3.30 |
| MySQL | 8.4.3 |
| Apache | 2.4.66 |
| WP-CLI | 2.12.0 |

---

## WordPress state

| Field | Value |
|-------|-------|
| Site title | Шпиговский — локальная разработка |
| `blog_public` | `0` (discourage indexing) |
| Permalinks | `/%postname%/` |
| Timezone | `Europe/Moscow` |
| Active theme | `shpigovsky` (foundation) |
| Active plugins | `advanced-custom-fields` 6.8.4, `shpigovsky-core` 0.1.0 |
| MU-plugin | `mars-local-runtime.php` |
| WPilot | **NOT INSTALLED** |
| ACF | **ACF Free 6.8.4 active** — Pro workflow pending operator package |

---

## Frontend intake

| Field | Value |
|-------|-------|
| Theme integration | **LOCKED** |
| Frontend authority | **NOT ADMITTED** |
| Approved handoff | **PENDING** |
| Source workspace | `workspaces/fp-0002-shpigovsky-v6/` |

---

## Backup / reset

| Field | Value |
|-------|-------|
| Baseline | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\foundation-001` |
| Backup script | `mars-runtime\scripts\backup-runtime.ps1` |
| Reset script | `mars-runtime\scripts\reset-to-foundation.ps1` |
| Reset token | `RESET-FP-0002` |

---

## Validation (2026-06-23)

| Check | Result |
|-------|--------|
| WP-CLI `core is-installed` | **PASS** |
| Checksums | **PASS** |
| HTTP front (direct domain) | **200** |
| REST `/wp-json/` | **200** |
| Direct `shpigovsky.test` hosts | **PASS** (FW-06A.1 closure) |
| `mysqlcheck` / `wp db check` | **PASS** (FW-06A.1) |
| Playwright foundation smoke | **PASS** (FW-06A.1) |
| Outgoing mail | **SUPPRESSED** (MU-plugin) |
| Local admin notice | **VISIBLE** |

---

## MLI-03R.1 post-reboot validation (2026-06-24)

| Check | Result |
|-------|--------|
| MySQL `datadir` | `mysql-8.4.3` — **PROVEN** |
| Auth plugin (`mli_shpigovsky_app@127.0.0.1`) | `caching_sha2_password` |
| `wp db check` | **PASS** |
| HTTP smoke | **PASS** |
| Playwright foundation smoke | **PASS** (5/5) |
| Controlled MySQL restart | **PASS** |

```text
FP-0002 WordPress foundation:
READY — POST-REBOOT VALIDATED
```

Report: [MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md](../../reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md)

---

## MLI-03R.3 Laragon cold-start datadir persistence (2026-06-24)

| Check | Result |
|-------|--------|
| Post-Windows-reboot incident | **DETECTED** — wrong datadir `mysql-8.4` |
| Session recovery | **PASS** |
| Laragon cold-start ×2 | **PASS** — datadir `mysql-8.4.3` |
| `wp db check` | **PASS** |
| HTTP smoke | **PASS** |

```text
FP-0002 WordPress foundation:
READY — CURRENT SESSION RESTORED

Windows reboot persistence:
PENDING OPERATOR RETEST
```

Report: [MARS-LOCALHOST-MLI-03R3-LARAGON-REBOOT-DATADIR-PERSISTENCE-v1.md](../../reports/MARS-LOCALHOST-MLI-03R3-LARAGON-REBOOT-DATADIR-PERSISTENCE-v1.md)

---

## FW-06A.1 closure — direct domain

```text
Direct domain:
PASS

Evidence:
Operator browser verification + automated DNS/HTTP verification

Closure date:
2026-06-23
```

---

## Consumer relation

| Consumer | Role |
|----------|------|
| Forge WordPress | Project owner — theme/plugin source in brain workspace |
| MLI | Runtime provider |
| WPilot | **Not connected** |

---

## Forge documents

- [FP-0002-WORDPRESS-FOUNDATION-REPORT-v1.md](../../mars-website-factory/subsystems/forge-wordpress/projects/fp-0002/FP-0002-WORDPRESS-FOUNDATION-REPORT-v1.md)

---

*MLI-WP-FP0002-LOCAL manifest v1 — FW-06A / FW-06A.1 complete.*

# MARS Localhost — Database Naming Standard v1

**Document type:** Database naming standard  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-00

---

## Purpose

Predictable, collision-resistant database names for local MariaDB/MySQL instances shared across MLI consumers.

---

## Schema

```text
mars_{platform}_{identifier}
```

| Segment | Values | Notes |
|---------|--------|-------|
| **prefix** | `mars` | Fixed MLI namespace |
| **platform** | `wp`, `oc`, `php`, `oth` | CMS / runtime family |
| **identifier** | compact slug | lowercase, no hyphens in DB name |

### Platform codes

| Platform folder | Code |
|-----------------|------|
| `sites/wordpress/` | `wp` |
| `sites/opencart/` | `oc` |
| `sites/php/` | `php` |
| `sites/other/` | `oth` |

### Identifier normalization

| Folder slug | DB identifier |
|-------------|---------------|
| `fws-0001` | `fws0001` |
| `fp-0002` / `shpigovsky` | `fp0002` or `shpigovsky` (manifest picks one) |
| `bzpm` | `bzpm` |
| `ocs-0001` | `ocs0001` |
| `web-sim-0001` | `websim0001` |

---

## Examples

| Site | Database name |
|------|---------------|
| WordPress synthetic FWS-0001 | `mars_wp_fws0001` |
| WordPress project FP-0002 | `mars_wp_fp0002` |
| OpenCart project BZPM | `mars_oc_bzpm` |
| OpenCart site generic | `mars_oc_site001` |
| PHP synthetic sim | `mars_php_websim001` |

---

## Environment suffix (optional)

For multiple environments of same slug on one machine (rare):

```text
mars_wp_fp0002_dev
mars_wp_fp0002_sbx
```

Default local profile omits suffix unless manifest declares it.

---

## Dump naming

```text
{database_name}_{yyyyMMdd}_{HHmm}_{reason}.sql
```

| Example | Meaning |
|---------|---------|
| `mars_wp_fws0001_20260622_1430_baseline.sql` | Baseline before validation |
| `mars_oc_bzpm_20260622_1600_predump.sql` | Pre-migration dump |

**Location:** `X:\MARS-Localhost\databases\dumps\`  
**Optional archive:** `X:\AI MARS STORAGE\{consumer}\` for large retained dumps

---

## Baseline naming

```text
{baseline_id}__{database_name}.sql
```

Stored under `X:\MARS-Localhost\databases\baselines\` with manifest reference.

---

## Credentials policy

| Rule | Policy |
|------|--------|
| **Production credentials** | **Prohibited** in local `.env` by default |
| **Shared local user** | Operator-defined per MLI-01 (e.g. `mars_local`) — not in Git |
| **Password storage** | `X:\AI MARS\local\` or OS secret store — **never** in manifests or docs |
| **Manifest** | Records database **name** and **host/port** only |

---

## Accidental production connection

| ID | Guard |
|----|-------|
| **DB-01** | Local DB host must be `127.0.0.1` or `localhost` unless manifest charters tunnel |
| **DB-02** | Production hostnames forbidden in local `.env` |
| **DB-03** | `wp-config.php` / OpenCart `config.php` must use manifest database name |
| **DB-04** | Pre-flight check: grep configs for non-local hosts before import |

---

## Related

- [MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md](MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md)
- [MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md](MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md)

---

*Database naming standard v1 — MLI-00.*

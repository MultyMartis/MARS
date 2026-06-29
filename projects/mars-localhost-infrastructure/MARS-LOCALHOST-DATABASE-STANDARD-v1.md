# MARS Localhost — Database Provisioning Standard v1

**Document type:** MySQL database and application-user provisioning standard  
**Version:** v1  
**Date:** 2026-06-24  
**Stage:** MLI-03R.1 (post-reboot remediation)

---

## Purpose

Canonical rules for creating MLI WordPress (and future consumer) databases and least-privilege application accounts on **MySQL 8.4** under Laragon, with reboot-safe configuration and **no** reliance on deprecated `mysql_native_password`.

---

## Authority files

| Topic | Document |
|-------|----------|
| Naming | [MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md](MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md) |
| Credentials | [MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md](MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md) |
| Active MySQL config | `X:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\my.ini` (**authoritative** for `mysqld`) |
| MLI mirror copy | `X:\MARS-Localhost\laragon\data\my.ini` (operator reference; must stay in sync) |
| Provisioning helper | [scripts/provision-mli-wordpress-db.ps1](scripts/provision-mli-wordpress-db.ps1) |

---

## Active MySQL configuration (MLI-03R.1)

| Setting | Required value | Notes |
|---------|----------------|-------|
| `datadir` | `X:/MARS-Localhost/laragon/data/mysql-8.4.3` | MLI WordPress data lives here |
| `bind-address` | `127.0.0.1` | Classic protocol loopback only |
| `mysqlx` | `0` | X Protocol disabled |
| `mysql_native_password` | **Must remain DISABLED** | Do not enable plugin or use for new accounts |

**Reboot rule:** Laragon starts `mysqld` without `--defaults-file`; Windows MySQL reads `my.ini` from the **binary directory**. Laragon **regenerates** `bin\mysql\mysql-8.4.3-winx64\my.ini` at each MySQL start, deriving `datadir` from package family `mysql-8.4` (see `usr\packages.conf`). Edits to `laragon\data\my.ini` alone are **not** sufficient.

**MLI-03R.3 durable pinning (2026-06-24):**

| Layer | Path | Role |
|-------|------|------|
| User template | `laragon\usr\tpl\MySQL.my.ini.tpl` | Canonical `datadir`, `bind-address`, `mysqlx=0` for Laragon merge |
| Authoritative runtime | `laragon\bin\mysql\mysql-8.4.3-winx64\my.ini` | Loaded by `mysqld`; **ReadOnly** to block generator overwrite |
| Operator mirror | `laragon\data\my.ini` | Reference copy; must stay in sync |
| Recovery | `X:\MARS-Localhost\tools\recover-mli-mysql-datadir.ps1` | Audit; `-Apply` after MySQL stop |

Report: [MARS-LOCALHOST-MLI-03R3-LARAGON-REBOOT-DATADIR-PERSISTENCE-v1.md](reports/MARS-LOCALHOST-MLI-03R3-LARAGON-REBOOT-DATADIR-PERSISTENCE-v1.md)

**Windows reboot persistence:** Laragon cold-start **PROVEN** (MLI-03R.3); full OS reboot **PENDING OPERATOR RETEST**.

---

## Application account rules

| Rule | Value |
|------|-------|
| Authentication plugin | **`caching_sha2_password`** (explicit in `CREATE USER` / `ALTER USER`) |
| Host scope | `127.0.0.1` matching runtime `DB_HOST` (avoid `%` and external hosts) |
| Privileges | `GRANT ALL` on `{database}.*` only — no `*.*`, no `GRANT OPTION`, no admin privileges |
| Admin operations | `root@localhost` or documented MLI admin only — **never** application users |
| Password source | `X:\AI MARS\local\mli\{runtime}\runtime.env` — **never** Git, reports, or SQL in repo |
| Duplicate hosts | Do not create both `localhost` and `127.0.0.1` unless manifest requires; prefer **`127.0.0.1`** when `DB_HOST` is `127.0.0.1` |

### Forbidden

```sql
IDENTIFIED WITH mysql_native_password ...
default_authentication_plugin = mysql_native_password
CREATE USER ...@'%'
```

---

## Provisioning sequence

1. Confirm active `datadir` and `bind_address` via administrative connection.
2. Create database per naming standard.
3. Read password from approved `runtime.env` (or generate and write atomically to secrets + `wp-config.php`).
4. Create user with explicit `caching_sha2_password`.
5. Grant database-scoped privileges only.
6. `SELECT User, Host, plugin` audit (no `authentication_string`).
7. Connection test: `SELECT 1` and `SHOW TABLES` as application user.
8. `wp db check` for WordPress runtimes.
9. Controlled MySQL restart; repeat steps 1, 6–8.

---

## Post-restart validation checklist

| Check | Pass criteria |
|-------|---------------|
| `datadir` | `mysql-8.4.3` |
| `bind_address` | `127.0.0.1` |
| Port 3306 | `127.0.0.1` LISTEN only |
| Port 33060 | No listener |
| App plugin | `caching_sha2_password` |
| Cross-DB | Denied between FP-0002 and FWS-0001 users |

---

## Related

- [MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md](reports/MARS-LOCALHOST-MLI-03R1-MYSQL-8.4-AUTHENTICATION-REMEDIATION-v1.md)
- [MARS-LOCALHOST-WORDPRESS-BASELINE-CONFIGURATION-STANDARD-v1.md](MARS-LOCALHOST-WORDPRESS-BASELINE-CONFIGURATION-STANDARD-v1.md)

---

*Database provisioning standard v1 — MLI-03R.1.*

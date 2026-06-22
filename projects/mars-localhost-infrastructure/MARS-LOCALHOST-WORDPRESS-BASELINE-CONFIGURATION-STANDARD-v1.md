# MARS Localhost — WordPress Baseline Configuration Standard v1

**Document type:** WordPress baseline configuration standard  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Reference runtime:** MLI-WP-SYN-001 (FWS-0001)

---

## Purpose

Define the **baseline WordPress configuration** for all MLI WordPress runtimes: `wp-config.php` structure, constants, table prefix, locale, debug posture, URL policy, and secrets loading — without embedding secret values in documentation.

---

## Secrets loading pattern

Credentials and authentication keys live **outside** the site tree:

```text
C:\AI MARS\local\mli\{slug}\runtime.env
```

**Reference path (MLI-WP-SYN-001):**

```text
C:\AI MARS\local\mli\fws-0001\runtime.env
```

### wp-config.php contract

1. `wp-config.php` on D: defines non-secret constants and includes secrets loader.
2. Loader reads `runtime.env` from brain-side path (absolute path in wp-config — acceptable on local operator machine).
3. **No passwords** in Git, manifests, or MLI markdown.
4. If `runtime.env` missing, WordPress must **fail closed** (do not fall back to sample credentials).

### runtime.env expected keys (names only)

| Key | Purpose |
|-----|---------|
| `DB_NAME` | Database name per naming standard |
| `DB_USER` | Per-runtime application user |
| `DB_PASSWORD` | Local-only password — **not documented** |
| `DB_HOST` | `127.0.0.1` default |
| `AUTH_KEY` / `SECURE_AUTH_KEY` / etc. | WordPress salt keys |
| Optional `TABLE_PREFIX` | Override only if manifest declares non-default |

Generate salts:

```bat
wp config shuffle-salts
```

---

## Database block

| Constant | MLI-WP-SYN-001 value | Rule |
|----------|----------------------|------|
| `DB_NAME` | `mars_wp_fws0001` | Per [database naming standard](MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md) |
| `DB_USER` | `mli_fws0001_app` | Pattern: `mli_{slug_normalized}_app` |
| `DB_PASSWORD` | *(runtime.env)* | Never in docs |
| `DB_HOST` | `127.0.0.1` | **Required** local host |
| `DB_CHARSET` | `utf8mb4` | WordPress default |
| `DB_COLLATE` | `''` | Empty unless manifest specifies |

### Table prefix

| Runtime | Prefix | Rule |
|---------|--------|------|
| MLI-WP-SYN-001 | `mli_` | MLI namespace prefix for all MLI-provisioned WordPress runtimes |

**Rule WP-CFG-01:** Default table prefix for new MLI WordPress sites is `mli_` unless manifest documents exception.  
**Rule WP-CFG-02:** Do not use `wp_` on shared local MySQL — collision risk across runtimes.

WP-CLI create example (no password in command history — use env file):

```bat
wp config create --dbname=mars_wp_fws0001 --dbuser=mli_fws0001_app --dbhost=127.0.0.1 --dbprefix=mli_
```

---

## Core version and locale

| Setting | MLI-WP-SYN-001 |
|---------|----------------|
| **WordPress version** | 7.0 |
| **Locale** | `ru_RU` |
| **WPLANG** | `ru_RU` (in wp-config or via option) |

Install:

```bat
wp core download --version=7.0 --locale=ru_RU --force
wp core install --url=http://fws-0001.test --title="FWS-0001 Synthetic" --admin_user=mli_admin --admin_email=mli-local@localhost.test --skip-email
```

Use synthetic admin identity only — no real client email.

---

## URL constants

| Constant | Policy |
|----------|--------|
| `WP_HOME` | Set when manifest URL must be enforced |
| `WP_SITEURL` | Match `WP_HOME` unless subdirectory install (not default) |

**MLI-WP-SYN-001 canonical HTTP URL:** `http://fws-0001.test`

HTTPS cert exists; **no forced HTTP→HTTPS redirect** in MLI-03 baseline unless consumer adds it. When both schemes work, manifest records HTTP as canonical until charter updates.

---

## Debug and development constants

### Synthetic / sandboxes (default)

| Constant | Value | Notes |
|----------|-------|-------|
| `WP_DEBUG` | `true` | |
| `WP_DEBUG_LOG` | `true` | → `wp-content/debug.log` |
| `WP_DEBUG_DISPLAY` | `false` | |
| `SCRIPT_DEBUG` | `false` | Enable only for active theme dev |
| `SAVEQUERIES` | `false` | Enable temporarily for profiling |

### projects class (when client data present)

| Constant | Value | Notes |
|----------|-------|-------|
| `WP_DEBUG` | `true` | |
| `WP_DEBUG_LOG` | `true` | |
| `WP_DEBUG_DISPLAY` | `false` | **Required** when client data |
| `DISALLOW_FILE_EDIT` | `true` | Recommended |

---

## Security and update constants

| Constant | MLI default | Rationale |
|----------|-------------|-----------|
| `DISALLOW_FILE_EDIT` | `true` | Prevent admin file editor on shared local |
| `AUTOMATIC_UPDATER_DISABLED` | `true` | Operator-controlled core/plugin updates |
| `WP_AUTO_UPDATE_CORE` | `false` | Explicit update via WP-CLI |
| `FORCE_SSL_ADMIN` | `false` | Until HTTPS trust + hosts fully verified |
| `DISALLOW_FILE_MODS` | `false` | Consumer may need plugin install; set `true` for locked proof rigs |

---

## File system method

| Constant | Value |
|----------|-------|
| `FS_METHOD` | `direct` (local default when permissions allow) |

If direct writes fail, diagnose permissions on D: site root before switching to FTP constants (FTP **not** used in MLI baseline).

---

## Cron

| Topic | Policy |
|-------|--------|
| Default | WordPress pseudo-cron enabled for local |
| `DISABLE_WP_CRON` | `false` unless consumer documents alternate |
| System cron | Optional operator enhancement — not MLI-03 requirement |

---

## .htaccess and permalinks

| Requirement | Value |
|---------------|-------|
| **mod_rewrite** | **Enabled** in Apache |
| **Permalink structure** | `/%postname%/` recommended |
| **`.htaccess`** | Generated by WordPress in site root |

Verify:

```bat
wp rewrite structure '/%postname%/'
wp rewrite flush
```

---

## Apache / PHP alignment

Per [MARS-LOCALHOST-SERVICE-PROFILE-v1.md](MARS-LOCALHOST-SERVICE-PROFILE-v1.md):

| Component | Version |
|-----------|---------|
| PHP | 8.3.30 |
| Apache | 2.4.66 |
| MySQL | 8.4.3 |

Required PHP extensions for WordPress 7.0: mysqli, curl, gd, mbstring, zip, intl, xml, dom (verify via `php -m` after `activate-mli.cmd`).

---

## MySQL server hardening (MLI-03)

| Setting | MLI-03 state |
|---------|--------------|
| `bind-address` | **`127.0.0.1`** |
| Application user host | `localhost` / `127.0.0.1` only |
| Remote root | Not enabled for MLI profile |

---

## Options table baseline (post-install)

Verify via WP-CLI:

```bat
wp option get siteurl
wp option get home
wp option get WPLANG
wp option get blog_charset
```

Siteurl/home must match manifest local URL.

---

## Configuration anti-patterns

| Anti-pattern | Why forbidden |
|--------------|---------------|
| Production DB host in `DB_HOST` | Local guard violation |
| Production URL in `siteurl` | Cookie/leakage risk |
| Passwords in wp-config committed to Git | Secrets policy violation |
| Shared `wp_` prefix across runtimes | Table collision |
| `WP_DEBUG_DISPLAY true` with client data | Information disclosure |

See [MARS-LOCALHOST-WORDPRESS-LOCAL-GUARD-STANDARD-v1.md](MARS-LOCALHOST-WORDPRESS-LOCAL-GUARD-STANDARD-v1.md).

---

## Related

- [MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md](MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md)
- [MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md](MARS-LOCALHOST-DATA-AND-SECRETS-POLICY-v1.md)
- [MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md](MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md)

---

*WordPress baseline configuration standard v1 — MLI-03.*

# MARS Localhost — WordPress Runtime Profile v1

**Document type:** Platform runtime profile  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Platform:** WordPress  
**Reference runtime:** MLI-WP-SYN-001 (FWS-0001)

---

## Purpose

Define the **WordPress runtime profile** for MARS Localhost Infrastructure (MLI): how WordPress sites are classified, laid out on `E:\MARS-Localhost`, registered in the brain (`C:\AI MARS`), configured, validated, and consumed by Forge WordPress and related programs.

This profile **does not** ship Forge theme/plugin implementation. It establishes the **local execution substrate** only.

---

## Scope

| In scope | Out of scope |
|----------|--------------|
| Synthetic, projects, and sandboxes under `sites\wordpress\` | OpenCart/ocStore (MLI-04) |
| Local `.test` domains and vhosts | Production hosting or remote DEV |
| Per-runtime DB/user (local least-privilege) | Forge theme/plugin install (consumer step) |
| WP-CLI provisioning baseline | Client production data import without charter |
| Brain manifests and registries | WPilot remote operations |
| Local guards (no production) | Full FW-05R consumer validation (post-handoff) |

---

## Brain vs runtime (C: / D: rule)

| Zone | Role | WordPress content |
|------|------|-------------------|
| **`C:\AI MARS` (brain)** | Source of truth for manifests, standards, registries, validation reports | Pointers only — paths, URLs, database **names**, secrets **location** |
| **`E:\MARS-Localhost` (runtime)** | Executing files — core, uploads, caches, Laragon stack | WordPress tree, DB data, TLS material, dumps, logs |
| **`C:\AI MARS\local\mli\{slug}\`** | Runtime secrets outside Git | `runtime.env` — credentials; **never** in docs or manifests |

**Rule WP-RT-01:** Governance and manifest SoT live in brain; WordPress core and media live on D:.  
**Rule WP-RT-02:** `E:\MARS-Localhost` is **not** a Git repository for MARS.  
**Rule WP-RT-03:** Secrets never committed to Git or embedded in markdown.

See [MARS-LOCALHOST-PHYSICAL-BOUNDARY-CONTRACT-v1.md](MARS-LOCALHOST-PHYSICAL-BOUNDARY-CONTRACT-v1.md).

---

## Runtime classes

WordPress sites use the universal MLI classification under `sites\wordpress\{class}\{slug}\`:

| Class | Folder | Purpose | Manifest | Data |
|-------|--------|---------|----------|------|
| **synthetic** | `synthetic\` | Capability proof, smoke, toolchain validation | **Required** | Synthetic fixtures only |
| **projects** | `projects\` | Real project local pilot (e.g. FP-0002) | **Required** | Client data only with explicit charter |
| **sandboxes** | `sandboxes\` | Disposable experiments | Recommended | Minimal / synthetic preferred |

**Reference synthetic runtime:** `FWS-0001` → `MLI-WP-SYN-001` at `sites\wordpress\synthetic\fws-0001\`.

See [MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md](MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md).

---

## Directory layout

WordPress physical root:

```text
E:\MARS-Localhost\sites\wordpress\{class}\{slug}\
```

**Reference (MLI-WP-SYN-001):**

```text
E:\MARS-Localhost\sites\wordpress\synthetic\fws-0001\
├── index.php
├── wp-config.php              # loads secrets from brain-side runtime.env
├── wp-load.php
├── wp-admin\
├── wp-includes\
├── wp-content\
│   ├── plugins\
│   ├── themes\
│   ├── uploads\
│   └── ...
└── .htaccess                  # permalinks — requires mod_rewrite
```

Laragon junction (when used):

```text
E:\MARS-Localhost\laragon\www\fws-0001  →  sites\wordpress\synthetic\fws-0001
```

Full WordPress-specific rules: [MARS-LOCALHOST-WORDPRESS-DIRECTORY-STANDARD-v1.md](MARS-LOCALHOST-WORDPRESS-DIRECTORY-STANDARD-v1.md).

---

## Domain and vhost

| Field | MLI-WP-SYN-001 value |
|-------|----------------------|
| **Canonical slug** | `fws-0001` |
| **Canonical URL (HTTP)** | `http://fws-0001.test` |
| **HTTPS URL** | `https://fws-0001.test` (cert generated; untrusted local CA) |
| **Apache vhost** | `laragon\etc\apache2\sites-enabled\fws-0001.test.conf` |
| **SSL vhost** | `fws-0001.test-ssl.conf` |
| **mod_rewrite** | **Enabled** (WordPress permalinks) |

**Hosts status (MLI-03 verified):**

| Domain | Status |
|--------|--------|
| `mli-smoke-001.test` | **PASS** — managed block present |
| `fws-0001.test` | **PENDING ELEVATION** — FW-05R closure 2026-06-23: `add-mli-host.ps1` exit 3 from Cursor; Host-header smoke PASS |

Hosts management: [MARS-LOCALHOST-HOSTS-MANAGEMENT-STANDARD-v1.md](MARS-LOCALHOST-HOSTS-MANAGEMENT-STANDARD-v1.md).

---

## Database

| Field | MLI-WP-SYN-001 value |
|-------|----------------------|
| **Database name** | `mars_wp_fws0001` |
| **Application user** | `mli_fws0001_app` |
| **Host restriction** | `127.0.0.1` / `localhost` only |
| **MySQL version** | 8.4.3 |
| **bind-address** | **Hardened to `127.0.0.1`** (MLI-03) |
| **Table prefix** | `mli_` |

Naming: [MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md](MARS-LOCALHOST-DATABASE-NAMING-STANDARD-v1.md).  
Credentials policy: [MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md](MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md).

**No passwords** in documentation, manifests, or Git. Connection values live in:

```text
C:\AI MARS\local\mli\fws-0001\runtime.env
```

---

## Runtime stack

| Component | Version / value |
|-----------|-----------------|
| **WordPress core** | 7.0 |
| **Locale** | `ru_RU` |
| **PHP** | 8.3.30 (Laragon) |
| **Web server** | Apache 2.4.66 |
| **Database** | MySQL 8.4.3 |
| **WP-CLI** | 2.12.0 (`E:\MARS-Localhost\tools\wp-cli\`) |

Shared service profile: [MARS-LOCALHOST-SERVICE-PROFILE-v1.md](MARS-LOCALHOST-SERVICE-PROFILE-v1.md).

---

## WP-CLI

Activation before any WP-CLI command:

```bat
E:\MARS-Localhost\tools\activate-mli.cmd
cd /d E:\MARS-Localhost\sites\wordpress\synthetic\fws-0001
wp --info
wp core version
wp option get siteurl
```

**Policy:**

| Rule | Value |
|------|-------|
| PHP binding | Laragon PHP 8.3.30 via `activate-mli.cmd` |
| Target URLs | Local `.test` only |
| Production aliases | **Prohibited** |
| Remote operations | **Prohibited** |

Standard: [MARS-LOCALHOST-WPCLI-STANDARD-v1.md](MARS-LOCALHOST-WPCLI-STANDARD-v1.md).

**Typical provisioning sequence (operator / automation):**

1. `wp core download --locale=ru_RU`
2. Create DB/user (local only)
3. `wp config create` — table prefix `mli_`, load credentials from `runtime.env`
4. `wp core install` — synthetic admin/site meta only
5. `wp rewrite structure '/%postname%/'` + flush rules
6. Verify `wp core verify-checksums`

---

## wp-config baseline

WordPress configuration follows [MARS-LOCALHOST-WORDPRESS-BASELINE-CONFIGURATION-STANDARD-v1.md](MARS-LOCALHOST-WORDPRESS-BASELINE-CONFIGURATION-STANDARD-v1.md).

| Constant / setting | MLI-WP-SYN-001 |
|--------------------|----------------|
| `$table_prefix` | `mli_` |
| `DB_NAME` | `mars_wp_fws0001` |
| `DB_USER` | `mli_fws0001_app` |
| `DB_HOST` | `127.0.0.1` |
| `WPLANG` | `ru_RU` |
| Secrets source | `runtime.env` via guarded include |
| `WP_HOME` / `WP_SITEURL` | Match manifest URL (HTTP canonical until HTTPS redirect chartered) |

---

## Debug and environment

| Setting | Synthetic default | Rationale |
|---------|-------------------|-----------|
| `WP_DEBUG` | `true` | Surface issues during MLI proof |
| `WP_DEBUG_LOG` | `true` | Log to `wp-content/debug.log` on D: |
| `WP_DEBUG_DISPLAY` | `false` | Avoid leaking stack traces to browser in smoke |
| `SCRIPT_DEBUG` | `false` | Unless theme dev charter |
| `DISALLOW_FILE_EDIT` | `true` | Reduce accidental admin edits in shared local |
| `AUTOMATIC_UPDATER_DISABLED` | `true` | Operator-controlled updates only |

Logs stay on D: under site or `E:\MARS-Localhost\logs\applications\`. Do not commit debug logs to brain.

---

## Plugins and themes

| Topic | MLI-03 policy |
|-------|---------------|
| **Core** | WordPress 7.0 via WP-CLI |
| **Default theme** | Twenty Twenty-Five (bundled) unless consumer replaces |
| **Forge theme/plugin** | **NOT installed** in MLI-03 — Forge WordPress consumer step |
| **Third-party plugins** | Synthetic OSS only when validation requires; document in manifest |
| **Production packages** | **Prohibited** without explicit charter |

Consumer installs theme/plugin from `C:\AI MARS\workspaces\` after MLI handoff.

---

## Backup and reset

| Trigger | Action |
|---------|--------|
| Before toolchain upgrade | DB dump + optional files zip |
| Before destructive WP-CLI | Dump per naming standard |
| Synthetic reset | Drop DB, clear site tree, set manifest `planned` |

Locations:

```text
E:\MARS-Localhost\databases\dumps\
E:\MARS-Localhost\backups\wordpress\
```

Policy: [MARS-LOCALHOST-BACKUP-AND-RESET-POLICY-v1.md](MARS-LOCALHOST-BACKUP-AND-RESET-POLICY-v1.md).

Update manifest `backup_state` and `rollback_state` after baseline operations.

---

## Manifests and registries

| Artifact | Location |
|----------|----------|
| **Runtime manifest (SoT)** | [manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md](manifests/MLI-WP-SYN-001-RUNTIME-MANIFEST-v1.md) |
| **WordPress runtime registry** | [registries/MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md](registries/MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md) |
| **Vhost registry** | [registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md](registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md) |
| **Manifest contract** | [MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md](MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md) |

**Rules:**

- No sustained WordPress runtime without brain manifest.
- Manifest records database **name** and secrets **path** — never values.
- Registry row must agree with manifest slug, path, and domain.

---

## Validation

### HTTP smoke

| Check | Expected |
|-------|----------|
| URL | `http://fws-0001.test/` (or Host header if hosts pending) |
| HTTP status | **200** |
| WordPress install | Core reachable; admin login page or front page |

### HTTPS smoke (Playwright pattern — MLI-02 parity)

| Check | Expected |
|-------|----------|
| URL | `https://fws-0001.test/` |
| Certificate | Self-signed / untrusted local CA |
| Playwright | `ignoreHTTPSErrors: true` |
| Result | **PASS WITH UNTRUSTED LOCAL CA** when hosts entry present |

Fixture path: `E:\MARS-Localhost\tools\playwright-smoke\`.

### WP-CLI validation

```bat
wp core verify-checksums
wp db check
wp option get blogname
```

### PHPCS (when theme/plugin present)

```bat
phpcs --standard=E:\MARS-Localhost\tools\phpcs\rulesets\mars-wordpress.xml {path}
```

---

## Lifecycle

```text
planned → provisioning → active → (hold | archived)
```

| State | Meaning |
|-------|---------|
| **planned** | Manifest exists; D: path may be empty |
| **provisioning** | WP-CLI install in progress |
| **active** | Validation passed; consumer may attach |
| **hold** | Blocked (e.g. hosts elevation, failed smoke) |
| **archived** | Teardown complete; evidence retained in brain |

**MLI-WP-SYN-001 current status:** `active` (Forge FW-05R complete; hosts elevation pending for direct URL resolution).

### Post-validation closure (2026-06-23)

| Item | Result |
|------|--------|
| Direct DNS `fws-0001.test` | **PENDING ELEVATION** |
| Host-header HTTP smoke | **PASS** |
| Forge consumer state | **COMPLETE** — PROVEN WITH LIMITATIONS |
| MLI role | **Runtime provider** — unchanged |

### Reset (synthetic)

1. Archive validation report to `reports/`
2. Optional dump to `databases\dumps\`
3. `wp db drop` / MySQL drop database
4. Remove or empty site folder
5. Set manifest `archived` or `planned`

---

## Forge WordPress and WPilot relationship

### Forge WordPress

| Aspect | Detail |
|--------|--------|
| **Relationship** | **Consumer** of MLI WordPress runtime profile |
| **Owns** | Theme/plugin source, methodology, FWS/FP passports in `C:\AI MARS\workspaces\` |
| **Does not own** | `E:\MARS-Localhost` root, Laragon, shared toolchain |
| **MLI-03 delivers** | Synthetic runtime MLI-WP-SYN-001 — core only, no Forge packages |
| **Next consumer step** | Install Forge theme/plugin; run FW-05R validation |
| **FW-05R** | **HOLD** until MLI-03 evidence accepted; then consumer re-validation |

Pointer: [projects/mars-website-factory/subsystems/forge-wordpress/](../mars-website-factory/subsystems/forge-wordpress/)

### WPilot

| Aspect | Detail |
|--------|--------|
| **Relationship** | Remote DEV/production operator — **not** MLI local owner |
| **Uses** | May accept verified packages from Forge; operates `dev.gktriumph.ru` class hosts |
| **Boundary** | WPilot does **not** provision or govern `E:\MARS-Localhost` |
| **Production** | **NONE** for MLI-WP-SYN-001 |

See [MARS-LOCALHOST-CONSUMER-MODEL-v1.md](MARS-LOCALHOST-CONSUMER-MODEL-v1.md).

---

## Local guards

Production isolation rules: [MARS-LOCALHOST-WORDPRESS-LOCAL-GUARD-STANDARD-v1.md](MARS-LOCALHOST-WORDPRESS-LOCAL-GUARD-STANDARD-v1.md).

Summary:

| Guard | Policy |
|-------|--------|
| Production DB host | **Forbidden** in wp-config |
| Production URLs in `WP_HOME` | **Forbidden** unless mirror charter |
| Production credentials | **Forbidden** in `runtime.env` |
| MySQL exposure | `bind-address=127.0.0.1` |
| MySQL datadir | `mysql-8.4.3` — Laragon cold-start pinned MLI-03R.3; see [DATABASE-STANDARD](MARS-LOCALHOST-DATABASE-STANDARD-v1.md) |
| WP-CLI `@production` aliases | **Forbidden** |

---

## Production target

| Runtime | Production target |
|---------|-------------------|
| MLI-WP-SYN-001 | **NONE** |

No live production mirror, sync, or push configured for MLI-03 synthetic proof.

---

## Related standards

| Document | Topic |
|----------|-------|
| [MARS-LOCALHOST-WORDPRESS-DIRECTORY-STANDARD-v1.md](MARS-LOCALHOST-WORDPRESS-DIRECTORY-STANDARD-v1.md) | Folder layout |
| [MARS-LOCALHOST-WORDPRESS-BASELINE-CONFIGURATION-STANDARD-v1.md](MARS-LOCALHOST-WORDPRESS-BASELINE-CONFIGURATION-STANDARD-v1.md) | wp-config |
| [MARS-LOCALHOST-WORDPRESS-LOCAL-GUARD-STANDARD-v1.md](MARS-LOCALHOST-WORDPRESS-LOCAL-GUARD-STANDARD-v1.md) | Local-only guards |
| [MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md](MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md) | Universal D: layout |
| [MARS-LOCALHOST-PHPCS-WPCS-STANDARD-v1.md](MARS-LOCALHOST-PHPCS-WPCS-STANDARD-v1.md) | Coding standards |
| [reports/MARS-LOCALHOST-MLI-03-WORDPRESS-RUNTIME-PROFILE-INPUT-v1.md](reports/MARS-LOCALHOST-MLI-03-WORDPRESS-RUNTIME-PROFILE-INPUT-v1.md) | Stage input |

---

*WordPress runtime profile v1 — MLI-03.*

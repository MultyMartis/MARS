# Baseline Manifest — ocStore 3.0.3.9 (rs.1)

**Baseline folder:** `baselines/ocstore-3039-rs1/`  
**Canonical source:** `projects/ocpilot/incoming/baselines/opencart-3.0.3.9-rs.zip`  
**Generated:** 2026-05-30 (OCPilot Run 3)  
**Method:** ZIP entry listing via `System.IO.Compression` (no full tree extracted to repo)

---

## Archive identity

| Field | Value |
|-------|-------|
| Filename | `opencart-3.0.3.9-rs.zip` |
| Size | 17 081 441 bytes (~16.29 MB) |
| SHA256 | `925D120AE38ABB3B5C05636028F644403AEEA31CF97B1A73353FFBE19F39C7CA` |
| ZIP entries (total) | 4190 (3553 files + 637 directory entries) |
| Readable | yes |
| Password-protected | no |

---

## Structure chain

| Level | Path | Notes |
|-------|------|-------|
| **Archive Root** | `upload-3039-rs1/` | Sole top-level directory in ZIP |
| **Package Root** | `upload-3039-rs1/` | Single top-level dir rule applied |
| **OpenCart Root** | `upload-3039-rs1/` | Core markers present (see below) |

---

## Archive Root listing

Top-level entries inside ZIP:

```
upload-3039-rs1/
```

No stray top-level files outside the package directory.

---

## Package Root — direct children

| Entry | Type | Notes |
|-------|------|-------|
| `admin/` | directory | 1313 files under subtree |
| `catalog/` | directory | 616 files |
| `image/` | directory | 110 files |
| `install/` | directory | 117 files; includes `opencart.sql` |
| `system/` | directory | 1391 files |
| `index.php` | file | defines `VERSION` = `3.0.3.9` (verified via selective extract) |
| `config-dist.php` | file | 0 bytes in ZIP |
| `.htaccess.txt` | file | 1 |
| `php.ini` | file | 1 |
| `robots.txt` | file | 1 |
| `deleted-files.zip` | file | 1 084 625 bytes |

---

## OpenCart Root markers

Path prefix: `upload-3039-rs1/`

| Marker | Status |
|--------|--------|
| `admin/` | present |
| `catalog/` | present |
| `system/` | present |
| `image/` | present |
| `index.php` | present |
| `config.php` (package root) | **absent** — `config-dist.php` present instead (0 bytes) |

OpenCart Root confirmed at `upload-3039-rs1/` with pre-install layout (no populated root `config.php`).

---

## Key directories — file counts

Counts include files only (exclude directory entries), under Package Root:

| Path | File count |
|------|------------|
| `admin/` | 1313 |
| `catalog/` | 616 |
| `image/` | 110 |
| `install/` | 117 |
| `system/` | 1391 |
| Other top-level files | 6 |
| **Approx. total under Package Root** | **3553** |

---

## `system/` top-level children

```
.htaccess, config/, engine/, framework.php, helper/, library/, modification.xml,
startup.php, storage/, tweak.ocmod.xml, tweak-54fz.ocmod.xml
```

---

## Notable findings

| Finding | Detail |
|---------|--------|
| Platform signals | `ru-ru/` language paths: 348; ocStore OCMOD files `tweak.ocmod.xml`, `tweak-54fz.ocmod.xml` |
| Version signal | `index.php` and `admin/index.php`: `define('VERSION', '3.0.3.9')` |
| Pre-install bundle | `install/` directory present; no root `config.php` |
| Empty config templates | `config-dist.php`, `admin/config-dist.php` — 0 bytes in archive |
| Nested archive | `deleted-files.zip` inside package root |
| Install SQL | `install/opencart.sql` — 193 177 bytes (not promoted to repo) |
| Vendor delta vs 3038-rs2 | `wechat`-related vendor paths: 105 vs 29 in 3038-rs2 listing |
| Credential filename scan | No `.env`; no root `config.php` with secrets; vendor token/password paths are core/vendor code names only |
| Cache/session | Placeholder `index.html` stubs only (4 paths); not live cache data |
| Live-site artifacts | No evidence of populated uploads, session data, or operational logs in listing |

---

## SAFE UNKNOWN

- Complete file path list (full 3553-path inventory not embedded; regenerate from canonical ZIP if needed).
- Checksum per internal file — not computed in Run 3.
- Whether 0-byte `config-dist.php` is vendor-intentional or packaging defect.

# EAR Default Exclusions v1

**Type:** Acquisition exclusion policy — **no** implementation  
**Date:** 2026-06-01  
**Status:** **Approved** at Runtime Transition Freeze  
**Applies to:** Mode 2 connected acquisition, offline ZIP scope policies, manifest generation (R1–R3)

**Rule:** Paths below are **excluded by default** unless an explicit **Acquisition Request** documents inclusion with risk acceptance and manifest metadata.

---

## Policy principles

| Principle | Rationale |
|-----------|-----------|
| **Exclude ephemeral state** | Cache, sessions, temp files change constantly and inflate manifests without structural value |
| **Exclude logs** | May contain PII, tokens, or paths — security and noise |
| **Exclude upload trees by default** | Large binary bulk; rarely needed for Level 1 version proof |
| **Exclude backups** | Duplicates, stale copies, possible credential leaks in dumps |
| **Document exclusions in manifest** | Consumers must see what was intentionally omitted ([EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md)) |
| **Pilot may narrow further** | `allowed_paths` in sub-charter may be stricter; not broader without amendment |

---

## Approved default exclusion paths

Paths are relative to **site document root** unless noted. Match common OpenCart/ocStore layouts; operator may add site-specific globs at Request.

### Cache and image cache

| Path / pattern | Rationale |
|----------------|-----------|
| `image/cache/` | Thumbnail and resized image cache — regenerable; very large |
| `system/storage/cache/` | System cache (OC 3.x storage layout) |
| `cache/` | Legacy/alternate cache root if present |

### Logs

| Path / pattern | Rationale |
|----------------|-----------|
| `system/storage/logs/` | Application and error logs — sensitive, high churn |
| `logs/` | Alternate log location if present |

### Sessions

| Path / pattern | Rationale |
|----------------|-----------|
| `system/storage/session/` | Active session files — sensitive, ephemeral |

### Upload storage (default off)

| Path / pattern | Rationale |
|----------------|-----------|
| `system/storage/upload/` | User uploads and temp upload payloads — large; PII risk |

**Note:** Catalog `image/catalog/` is **not** in default exclusions — product images may be in scope for higher levels; for Level 1 SFTP pilots, charter may exclude bulk `image/` via pilot `excluded_paths` (PILOT-001 risk R-11).

### Temporary directories

| Path / pattern | Rationale |
|----------------|-----------|
| `tmp/` | Temporary files |
| `temp/` | Temporary files (alternate naming) |

### Backups

| Path / pattern | Rationale |
|----------------|-----------|
| `backup/` | Local backup trees — stale, large, may contain DB dumps with secrets |
| `backups/` | Alternate backup folder naming |

---

## Additional justified exclusions (runtime / ops only)

These paths are commonly present on hosted OpenCart installs and should **default exclude** unless Request explicitly needs them:

| Path / pattern | Rationale |
|----------------|-----------|
| `system/storage/modification/` | OCMod merged cache — derivable from source |
| `vqmod/vqcache/` | vQmod cache if present |
| `*.log` (any path) | Stray log files outside `logs/` |
| `.git/` | VCS metadata — not site runtime state |
| `node_modules/` | Accidental frontend tooling on host |
| `vendor/` (if duplicate of committed dep) | **SAFE UNKNOWN** — exclude if confirmed cache/vendor mirror only |

---

## Partial / selective inclusion patterns

| Pattern | Default | When to include (explicit Request) |
|---------|---------|-----------------------------------|
| `image/catalog/` bulk | In-scope for architecture | Level 1 may exclude via pilot policy — document in manifest |
| `image/cache/` | **Exclude** | Never default-include |
| Version proof files | **Include** | e.g. `index.php`, `admin/index.php`, `system/version.php` — CON-L1-A |
| `config.php` / `admin/config.php` | **Include with redaction plan** | Evidence quarantine — secrets stripped before publish |

---

## Connector and manifest requirements

| Requirement | Source alignment |
|-------------|------------------|
| Connector `scope.exclusions` lists defaults + pilot additions | [EAR-CONNECTOR-CONTRACT-v1.md](EAR-CONNECTOR-CONTRACT-v1.md) |
| `file-manifest` metadata records exclusion policy | [EAR-OPENCART-QUALITY-MAPPING-v1.md](EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| Wrong-root / cache bulk download risk | [EAR-OPENCART-RISK-MODEL-v1.md](EAR-OPENCART-RISK-MODEL-v1.md), PILOT-001 R-11 |

---

## PILOT-001 note

[IMPLEMENTATION-SUBCHARTER-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/IMPLEMENTATION-SUBCHARTER-v1.md) §4 `excluded_paths` remains **SAFE UNKNOWN** until operator sign-off. This document supplies **default** policy; pilot binding may add paths (e.g. large `image/` subtree policy) but must not silently **remove** security-critical exclusions (logs, sessions) without risk register entry.

---

## Non-goals

- This document does not define SFTP `LIST`/`RETR` behavior or glob implementation.
- Does not replace host-specific security review.
- Does not authorize downloading excluded paths for “convenience.”

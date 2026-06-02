# OCPilot — Baseline Sanitization Review

**Purpose:** document pre-promotion review of archive contents for allowed vs forbidden material before populating `baselines/<folder>/files/`.

**Run:** OCPilot Run 3.5 — Baseline Promotion  
**Date:** 2026-05-30  
**Method:** ZIP listing (Run 3) + promoted tree inspection + targeted filename/path scans — **not** full secret/malware scanning.

**Related:** [baseline-storage-model.md](baseline-storage-model.md), [quarantine-policy.md](quarantine-policy.md), [baseline-promotion-strategy.md](baseline-promotion-strategy.md)

---

## Review categories

| Category | Allowed in promoted baseline | Forbidden |
|----------|------------------------------|-----------|
| Vendor core | PHP, Twig, JS, CSS, images, language packs, OCMOD XML | — |
| Install bundle | `install/` including `opencart.sql` (vendor seed schema) | Live production DB dumps |
| Config templates | Empty or dist templates (`config-dist.php`) | Populated `config.php`, `admin/config.php` with credentials |
| Storage layout | `system/storage/` structure, vendor/, placeholder stubs | Live cache blobs, session payloads, upload user content |
| Credentials | — | `.env`, API keys, SMTP passwords in config files |
| Customer data | Demo/seed rows in install SQL only (vendor default) | Orders, customers, exports from live sites |
| Operational artifacts | — | Access logs, error logs from production, backup dumps |

---

## ocStore 3.0.3.8 (rs.2) — `opencart-3.0.3.8-rs.zip` → `baselines/ocstore-3038-rs2/files/`

### Archive identity

| Field | Value |
|-------|-------|
| SHA256 | `916CDFD62F5333487B14F5C94474C679D69CCD4EEED51638C167AC25A24E4C83` |
| Package root | `upload-3038-rs2/` |
| Files promoted | 4055 |

### Allowed content — findings

| Area | Finding |
|------|---------|
| Core directories | `admin/`, `catalog/`, `image/`, `install/`, `system/` present at promoted root |
| Language | `ru-ru/` paths present (ocStore locale pack) |
| OCMOD | `system/tweak.ocmod.xml`, `system/tweak-54fz.ocmod.xml` |
| Vendor | `system/storage/vendor/` — Composer dependencies (payment SDKs, Twig, Symfony, etc.) |
| Install SQL | `install/opencart.sql` — 192 868 bytes; 136 `CREATE TABLE`, 110 `INSERT` — vendor install seed |
| Image placeholders | Default catalog/demo image structure under `image/` |
| Cache/session dirs | Operational cache/session **directories** contain `index.html` stubs only at storage paths |

### Forbidden content — scan results

| Check | Result |
|-------|--------|
| Root `config.php` | **Absent** |
| `admin/config.php` | **Absent** |
| `.env` | **Absent** |
| Live cache payload | **Not detected** — paths matching `cache` are library/vendor source files (e.g. `system/library/cache/file.php`), not runtime cache entries |
| Live session data | **Not detected** — `system/storage/session/` has `.htaccess` + stub pattern; no session payload files |
| Customer/order exports | **Not detected** in file tree |
| Populated credentials in configs | **Not detected** — no populated config files |

### Anomalies (not blocking promotion)

| Item | Notes |
|------|-------|
| `config-dist.php`, `admin/config-dist.php` | **0 bytes** — packaging anomaly; documented in passport; not live credentials |
| `deleted-files.zip` | Nested vendor artifact (~1.19 MB) — promoted as-is; contents not fully inventoried |
| `install/opencart.sql` | Contains schema field names like `password`, empty default config keys — **vendor install seed**, not live secrets |
| Filename `opencart-*` | Archive naming vs ocStore content — platform classified from tree signals (Run 3) |

### Promotion decision

**PASS** — pre-install vendor bundle; no forbidden live-site artifacts detected in review scope. Full tree promoted to `files/` with OpenCart root at `files/` (no wrapper folder).

---

## ocStore 3.0.3.9 (rs.1) — `opencart-3.0.3.9-rs.zip` → `baselines/ocstore-3039-rs1/files/`

### Archive identity

| Field | Value |
|-------|-------|
| SHA256 | `925D120AE38ABB3B5C05636028F644403AEEA31CF97B1A73353FFBE19F39C7CA` |
| Package root | `upload-3039-rs1/` |
| Files promoted | 3553 |

### Allowed content — findings

| Area | Finding |
|------|---------|
| Core directories | Same OpenCart-root layout as 3038-rs2 |
| Language / OCMOD | Same ocStore signals (`ru-ru/`, `tweak*.ocmod.xml`) |
| Vendor | `system/storage/vendor/` — reduced file count vs 3038-rs2 (1291 vs 1809 vendor paths) — dependency refresh, not live data |
| Install SQL | `install/opencart.sql` — 193 177 bytes; 136 tables, 110 inserts — same table set as 3038-rs2 |
| WeChat integration paths | 96 paths vs 26 in 3038-rs2 — vendor extension files, allowed |

### Forbidden content — scan results

| Check | Result |
|-------|--------|
| Root `config.php` | **Absent** |
| `admin/config.php` | **Absent** |
| `.env` | **Absent** |
| Live cache/session | **Not detected** — same stub/library pattern as 3038-rs2 |
| Customer data / exports | **Not detected** |
| Populated credentials | **Not detected** |

### Anomalies (not blocking promotion)

| Item | Notes |
|------|-------|
| 0-byte `config-dist.php` | Same as 3038-rs2 |
| `deleted-files.zip` | ~1.08 MB — promoted; not fully inventoried |
| Install jQuery upgrade | `install/view/javascript/jquery/jquery-3.7.0.min.js` (3039) vs 2.1.1 (3038) — vendor installer assets only |

### Promotion decision

**PASS** — same pre-install vendor profile as 3038-rs2. Full tree promoted.

---

## Cross-baseline sanitization notes

| Topic | Conclusion |
|-------|------------|
| `install/opencart.sql` in `files/` | Retained as **vendor install artifact** inside promoted tree; **not** copied to `database/` as dump — see `database/database-metadata-v1.md` |
| SQL in `database/` folder | Metadata only per Run 3.5 scope |
| Re-scan after promotion | Post-promotion forbidden checks confirmed: no `config.php`, no `.env` at promoted roots |

---

## SAFE UNKNOWN

- Full malware or secret scanning — **not performed**.
- Complete inventory of `deleted-files.zip` interiors — **not performed**.
- Whether 0-byte `config-dist.php` is vendor-intentional — **SAFE UNKNOWN**.
- Semantic review of every `INSERT` row in install SQL — only structural/metadata review performed.
- Official ocStore download provenance — operator URL not recorded (Run 3).

# Versioned Baseline Passport — ocStore 3.0.3.9 (rs.1)

**Purpose:** standard identity record for baseline `baselines/ocstore-3039-rs1/`.

**Passport ID:** `ocstore-3039-rs1-passport-v1`  
**Created:** 2026-05-30 (OCPilot Run 3 — agent-assisted, human-supervised)

---

## Identity

| Field | Value |
|-------|-------|
| **Platform** | ocStore |
| **Version** | 3.0.3.9 (rs.1 — rs suffix from package folder `upload-3039-rs1/`) |
| **Source** | Operator-supplied archive `opencart-3.0.3.9-rs.zip` in `incoming/baselines/`; official download URL — **SAFE UNKNOWN** |
| **Acquisition Date** | 2026-05-30 |
| **Repo path** | `baselines/ocstore-3039-rs1/` |
| **Passport ID** | `ocstore-3039-rs1-passport-v1` |
| **Created by (operator)** | Operator archive drop; Run 3 intake (agent-assisted) |

---

## Readiness flags

| Field | Value |
|-------|-------|
| **Files Present** | yes — Run 3.5 promoted tree (3553 files); OpenCart root at `files/` (no wrapper folder) |
| **Database Metadata Present** | yes — `database/database-metadata-v1.md` (metadata only) |
| **Database Dump Present** | no — `install/opencart.sql` in `files/install/` only; not copied to `database/` |
| **Manifest Present** | yes — `manifest/baseline-manifest-v1.md` |
| **Notes Present** | no — `notes/` placeholder only |

Run 3.5 promotion complete — required readiness gate passes per [run-3.5-readiness-recheck.md](../../../run-3.5-readiness-recheck.md).

---

## Core Directories

Verified from archive listing (`opencart-3.0.3.9-rs.zip` → Package Root `upload-3039-rs1/`):

| Directory | Expected | Present in baseline |
|-----------|----------|---------------------|
| `admin/` | yes | yes (in archive) |
| `catalog/` | yes | yes (in archive) |
| `system/` | yes | yes (in archive) |
| `image/` (structure only) | yes | yes (in archive) |
| `storage/` or `system/storage/` | yes (OC 3.x) | yes — `system/storage/` (in archive) |
| `install/` | typical pre-install bundle | yes (in archive) |

---

## Known Differences

- ocStore distribution indicators (verified in archive listing): `ru-ru/` language pack (348 paths), `system/tweak.ocmod.xml`, `system/tweak-54fz.ocmod.xml`.
- Package folder name `upload-3039-rs1/` aligns with ocStore rs.1 build label (folder naming; not independently verified against ocstore.com release notes).
- Root `config.php` absent; `config-dist.php` present but **0 bytes** in archive — pre-install vendor layout; not a populated live config.
- Nested `deleted-files.zip` inside package root (~1.08 MB) — vendor artifact; purpose not fully verified.
- `system/storage/vendor/zoujingli/wechat-developer/` present (vendor library paths in listing) — count differs from 3038-rs2 archive.
- Differences vs upstream OpenCart 3.0.3.9 — **SAFE UNKNOWN** (no upstream OpenCart 3.0.3.9 baseline in repo for diff).

---

## Known Risks

| Risk | Mitigation |
|------|------------|
| Operator source not independently verified | Record SHA256 in manifest; operator may supply official URL/checksum later |
| `config-dist.php` / `admin/config-dist.php` are 0-byte entries | Treat as packaging anomaly; do not promote empty configs to `files/` without review |
| `install/opencart.sql` in archive | Schema reference only; do not commit as live dump without sanitization review |
| Filename says `opencart-*` but content is ocStore-shaped | Platform determined from tree signals + operator brief; documented as ocStore |

---

## Known Missing Areas

| Area | Status | Notes |
|------|--------|-------|
| Sanitized `files/` tree in repo | **acquired** (Run 3.5) | Promoted from canonical ZIP; see [baseline-promotion-strategy.md](../../../baseline-promotion-strategy.md) |
| `database/` schema metadata | **acquired** (Run 3.5) | `database/database-metadata-v1.md` — metadata only |
| Upstream OpenCart comparison baseline | not in repo | ocStore-vs-upstream deltas = SAFE UNKNOWN |
| Official source URL / vendor checksum | SAFE UNKNOWN | Operator may provide in Run 4+ |

---

## Files baseline (detail)

| Field | Value |
|-------|-------|
| Path in repo | `baselines/ocstore-3039-rs1/files/` — **3553 files (Run 3.5 promotion)** |
| Archive label (external) | `projects/ocpilot/incoming/baselines/opencart-3.0.3.9-rs.zip` |
| Checksum note | SHA256 `925D120AE38ABB3B5C05636028F644403AEEA31CF97B1A73353FFBE19F39C7CA` |
| Excluded from snapshot | Live `config.php` / `admin/config.php` (absent in archive); cache/session placeholder stubs only |

---

## Archive structure (verified Run 3)

| Level | Path |
|-------|------|
| Archive Root | `upload-3039-rs1/` (sole top-level entry) |
| Package Root | `upload-3039-rs1/` |
| OpenCart Root | `upload-3039-rs1/` |

---

## Database baseline (detail)

| Field | Value |
|-------|-------|
| Path in repo | `baselines/ocstore-3039-rs1/database/database-metadata-v1.md` |
| Content type | Metadata only — SQL remains at `files/install/opencart.sql` (193177 bytes) |
| Table prefix (default) | `oc_` (verified from install SQL table names) |
| Dump location | `files/install/opencart.sql` — not copied to `database/` |

---

## Manifest

| Field | Value |
|-------|-------|
| Path in repo | `baselines/ocstore-3039-rs1/manifest/` |
| Manifest filename | `baseline-manifest-v1.md` |
| Generation method | tool-assisted ZIP listing (PowerShell `System.IO.Compression`; no full repo extract) |

---

## Usage

| Field | Value |
|-------|-------|
| Intended for site comparison | yes — after readiness gate passes |
| Supersedes passport ID | — (first passport) |
| Comparison methodology | [baseline-comparison-methodology.md](../../../baseline-comparison-methodology.md) |

---

## Forbidden (reminder)

- `config.php`, `admin/config.php` with live values — not present in archive at package root
- Credentials, tokens, API keys — none detected in filename/metadata scan; **not** a full secret scan
- Customer data, order exports — not indicated in listing
- Unsanitized production dumps — not promoted

---

## SAFE UNKNOWN

- Official ocStore release page / mirror URL for this exact rs.1 build.
- Whether 0-byte `config-dist.php` entries are intentional vendor packaging or archive defect.
- Full ocStore-vs-upstream OpenCart file delta (requires upstream baseline or vendor release notes).
- Automated malware or secret scanning — **not** performed.
- rs.1 build identity beyond folder name and operator brief.

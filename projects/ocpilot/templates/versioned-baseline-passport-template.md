# Versioned Baseline Passport

**Purpose:** standard identity record for every versioned baseline under `baselines/<version-folder>/`.

**Store completed copies in:** `baselines/<version-folder>/passports/`  
**Naming suggestion:** `<version-folder>-passport-v1.md` (increment on supersession)

---

## Identity

| Field | Value |
|-------|-------|
| **Platform** | OpenCart / ocStore |
| **Version** | e.g. 3.0.3.7 / 4.0.x |
| **Source** | official download URL / ocStore build label / SAFE UNKNOWN |
| **Acquisition Date** | YYYY-MM-DD |
| **Repo path** | e.g. `baselines/opencart-3037/` |
| **Passport ID** | e.g. `opencart-3037-passport-v1` |
| **Created by (operator)** | |

---

## Readiness flags

| Field | Value |
|-------|-------|
| **Files Present** | yes / no / partial |
| **Database Metadata Present** | yes / no |
| **Database Dump Present** | yes (external) / yes (sanitized in repo) / no |
| **Manifest Present** | yes / no |
| **Notes Present** | yes / no |

If **Files Present = no** or **Manifest Present = no** when comparison is requested → baseline is **not ready**; see [baseline-readiness-checklist.md](../baseline-readiness-checklist.md).

---

## Core Directories

List directories expected in a clean install for this platform/version:

| Directory | Expected | Present in baseline |
|-----------|----------|---------------------|
| `admin/` | | |
| `catalog/` | | |
| `system/` | | |
| `image/` (structure only) | | |
| `storage/` or `system/storage/` (structure only) | | version-dependent |

Add ocStore-specific paths if applicable.

---

## Known Differences

Document how this baseline differs from upstream OpenCart (for ocStore) or from a previous baseline revision:

- 
- 

---

## Known Risks

| Risk | Mitigation |
|------|------------|
| Wrong version pinned | Re-verify against vendor release notes |
| Partial file tree | Do not use for full diff until complete |
| Schema metadata missing | Layer 1–2 file comparison only; DB layer = SAFE UNKNOWN |
| Mixed production files in upload | Re-sanitize before repo intake |

---

## Known Missing Areas

List intentionally excluded or not yet acquired areas:

| Area | Status | Notes |
|------|--------|-------|
| e.g. `image/catalog/` uploads | excluded — vendor default only | |
| e.g. sample products in DB | not included | |
| | | |

---

## Files baseline (detail)

| Field | Value |
|-------|-------|
| Path in repo | `baselines/<version-folder>/files/` |
| Archive label (external, if any) | |
| Checksum note (optional, no secrets) | |
| Excluded from snapshot | e.g. `image/cache/`, user uploads, `config.php` |

---

## Database baseline (detail)

| Field | Value |
|-------|-------|
| Path in repo | `baselines/<version-folder>/database/` |
| Content type | schema-only / metadata only / SAFE UNKNOWN |
| Table prefix (default) | e.g. `oc_` |
| Dump location | external only — unless explicitly approved sanitized copy |

---

## Manifest

| Field | Value |
|-------|-------|
| Path in repo | `baselines/<version-folder>/manifest/` |
| Manifest filename | |
| Generation method | manual / tool-assisted / SAFE UNKNOWN |

---

## Usage

| Field | Value |
|-------|-------|
| Intended for site comparison | yes / no |
| Supersedes passport ID | |
| Comparison methodology | [baseline-comparison-methodology.md](../baseline-comparison-methodology.md) |

---

## Forbidden (reminder)

- `config.php`, `admin/config.php` with live values
- Credentials, tokens, API keys
- Customer data, order exports
- Unsanitized production dumps

---

## SAFE UNKNOWN

- 

*(List anything not verified at passport creation time. Do not silently assume.)*

# ocStore 3.0.3.9 (rs.1) — Priority Baseline

**Purpose:** priority baseline folder for **real OCPilot target sites** running **ocStore 3.0.3.9 (rs.1)**.

## Status

- **READY** for file-level comparison after Run 3.5 baseline promotion ([run-3.5-readiness-recheck.md](../../run-3.5-readiness-recheck.md)).
- Canonical source remains `incoming/baselines/opencart-3.0.3.9-rs.zip` — promoted tree is reference working baseline only.
- If readiness checks fail after future changes, OCPilot **must request operator action** before comparison — **do not silently continue**.

## Folders

| Folder | Intended content |
|--------|------------------|
| `files/` | Sanitized vendor file tree for ocStore 3.0.3.9 (rs.1) |
| `database/` | Schema metadata or schema-only export labels — not live secrets |
| `notes/` | Version, source, exclusions, operator commentary |
| `manifest/` | File manifests, directory maps, checksum labels |
| `passports/` | Completed [versioned-baseline-passport-template.md](../../templates/versioned-baseline-passport-template.md) |
| `comparison-notes/` | Known ocStore differences vs upstream OpenCart or other ocStore builds |

## Rules

- **No secrets.** No credentials. No production customer data.
- **No raw production DB dumps** unless explicitly approved and sanitized.
- **Forbidden in repo:** `config.php`, `admin/config.php` (with real credentials), storage configs, tokens, API keys.
- Do **not** store live-site copies or hosting exports as «clean baseline» without intake review.

## Usage

Compare project sites against this baseline during read-only audits. See [baseline-readiness-checklist.md](../../baseline-readiness-checklist.md), [baseline-comparison-methodology.md](../../baseline-comparison-methodology.md), and [baseline-storage-model.md](../../baseline-storage-model.md).

# Clean OpenCart / ocStore Baseline Passport

**Purpose:** document a **reference** install stored under a **versioned** baseline folder in `baselines/`.

## Baseline identity

| Field | Value |
|-------|-------|
| Baseline ID | e.g. `opencart-3037-clean-v1` |
| Platform | OpenCart / ocStore |
| Version | e.g. 3.0.3.7 |
| Repo path | `baselines/<version-folder>/` e.g. `baselines/opencart-3037/` |
| Source | official download / ocStore build / SAFE UNKNOWN |
| Created date | |
| Created by (operator) | |

## Version folder checklist

| Version folder | Use when project site is |
|----------------|--------------------------|
| `opencart-230/` | OpenCart 2.3.x |
| `opencart-3037/` | OpenCart 3.0.3.7 |
| `opencart-4x/` | OpenCart 4.x |
| `ocstore-230/` | ocStore 2.3.x |
| `ocstore-3037/` | ocStore 3.0.3.7 |

If folder is empty → operator must provide baseline files/database metadata before comparison (Run 2).

## Files baseline

| Field | Value |
|-------|-------|
| Path in repo | `baselines/<version-folder>/files/` |
| Archive label (external) | |
| Checksum note (optional, no secrets) | |
| Excluded from snapshot | e.g. `image/cache/`, user uploads |

## Database baseline

| Field | Value |
|-------|-------|
| Path in repo | `baselines/<version-folder>/database/` |
| Content type | schema-only / sample data / metadata only |
| Table prefix | |
| Dump location | external only — no raw dumps in git unless approved and sanitized |

## Notes

| Field | Value |
|-------|-------|
| Path in repo | `baselines/<version-folder>/notes/` |
| PHP tested with | |
| Default extensions installed | none / list |
| Known deviations from vendor default | |

## Usage

| Field | Value |
|-------|-------|
| Intended for site comparison | yes |
| Supersedes baseline ID | |
| Legacy generic path used | no — prefer versioned folder |

## Forbidden

- `config.php`, `admin/config.php`, storage configs, credentials, tokens in repo.

## SAFE UNKNOWN

- 

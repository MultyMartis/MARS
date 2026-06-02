# OpenCart 4.x — Clean Baseline

**Purpose:** versioned reference folder for a **clean baseline** of **OpenCart 4.x** (major version line; pin exact minor in `notes/` when populated).

## Status

- Empty folder is **valid** at the current stage.
- If [baseline-readiness-checklist.md](../../baseline-readiness-checklist.md) required checks fail, OCPilot must ask the operator to provide baseline materials before using this baseline for comparison.

## Folders

| Folder | Intended content |
|--------|------------------|
| `files/` | Sanitized vendor file tree for OpenCart 4.x |
| `database/` | Schema metadata or schema-only export labels — not live secrets |
| `notes/` | Version, source, exclusions, operator commentary |
| `manifest/` | File manifests, directory maps, checksum labels |
| `passports/` | Completed [versioned-baseline-passport-template.md](../../templates/versioned-baseline-passport-template.md) |
| `comparison-notes/` | Known differences vs upstream (if applicable for this platform) |

## Rules

- Do **not** store secrets in this folder.
- Full raw DB dumps should **not** be committed unless explicitly approved and sanitized.
- **Forbidden in repo:** `config.php`, `admin/config.php`, storage configs, credentials, tokens, API keys.

## Usage

Compare project sites against this baseline during read-only audits. See [baseline-comparison-methodology.md](../../baseline-comparison-methodology.md), [baseline-storage-model.md](../../baseline-storage-model.md), and [templates/versioned-baseline-passport-template.md](../../templates/versioned-baseline-passport-template.md).

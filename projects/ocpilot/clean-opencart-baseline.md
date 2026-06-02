# Clean OpenCart Baseline

**Purpose:** отделить **чистый OpenCart / ocStore core** от **кастомизаций проектного сайта** (тема, модули, SQL-патчи, override).

## Why baseline is required

| Without baseline | With baseline |
|------------------|---------------|
| Custom code mistaken for core | Delta = project − clean |
| Risky «fix» of vendor files | Targeted rollback of custom only |
| Wrong catalog import assumptions | Import maps to known schema version |

## Versioned baselines (preferred)

Baselines live under `baselines/` — **one folder per pinned version**, not a single generic tree:

| Folder | Platform / version |
|--------|-------------------|
| `baselines/opencart-230/` | OpenCart 2.3.0 |
| `baselines/opencart-3037/` | OpenCart 3.0.3.7 |
| `baselines/opencart-4x/` | OpenCart 4.x |
| `baselines/ocstore-230/` | ocStore 2.3.0 |
| `baselines/ocstore-3037/` | ocStore 3.0.3.7 |

Each version folder contains:

| Component | Subfolder | Content |
|-----------|-----------|---------|
| Files | `files/` | Sanitized tree snapshot (no secrets); version-labeled |
| Database | `database/` | Schema/metadata snapshot labels — **not** live secrets in git |
| Notes | `notes/` | Version, build date, extensions excluded, operator notes, passport |

**Empty folder is valid** at current stage. If empty, OCPilot must ask the operator to provide baseline files and database metadata before using it for comparison.

**Legacy:** `baselines/clean-opencart/` remains as Phase 0 generic placeholder — not preferred for new work.

## Versioning rules

- Match project site OpenCart/ocStore version to the **correct versioned baseline folder**.
- New release line → new baseline folder or supersession note in `notes/`; do not silently overwrite old baseline.
- Passport: [templates/clean-baseline-passport-template.md](templates/clean-baseline-passport-template.md).

## Forbidden in baseline folders

- Secrets, credentials, tokens.
- `config.php`, `admin/config.php`, storage configs with live values.
- Full raw DB dumps in git unless explicitly approved and sanitized.

## Comparison workflow (project site)

1. Identify project OpenCart/ocStore version (read-only audit) → select matching `baselines/<version>/`.
2. Obtain project file tree evidence (FTP export metadata or path list in audit — not necessarily full binary in git).
3. Diff mentally or via tool: project vs `baselines/<version>/files/`.
4. Classify: **core** | **extension/vendor** | **project custom** | **SAFE UNKNOWN**.
5. DB: compare table prefix, extra tables, modified core tables — against baseline schema notes in `database/` and `notes/`.
6. Record deltas in [templates/inspection-report-template.md](templates/inspection-report-template.md) and site analysis folders under `sites/<slug>/`.

## When to consult baseline

- First read-only audit of a dealership site.
- Before catalog import planning (Run 6).
- Before theme/controller/ocMod change planning (Run 7).
- When investigating «is this bug core or custom?»

## Risks of confusing core vs custom

| Mistake | Consequence |
|---------|-------------|
| Edit `system/` core file | Breaks updates; hard rollback |
| Delete «unknown» file | May be payment/shipping module |
| Import against wrong schema | Broken categories, SEO URLs, attributes |
| Assume ocMod path = core | Silent behavior change |
| Compare against wrong version baseline | False delta, wrong rollback plan |

## Operator rule

If version or baseline match is uncertain → **SAFE UNKNOWN**; do not claim clean diff until evidence exists.

## Setup run

See OPERATIONAL-INDEX **Run 2** and [baselines/README.md](baselines/README.md).

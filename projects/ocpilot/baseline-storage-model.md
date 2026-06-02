# OCPilot — Baseline Storage Model

**Purpose:** define what belongs in a versioned baseline, what is forbidden, and why baseline is **reference material** — not a working project.

**Status:** documented model only; **no** runtime, **no** automation, **no** import of actual OpenCart files in this run.

---

## What a baseline is

A **versioned clean baseline** is a pinned, sanitized snapshot of a known OpenCart or ocStore release stored under `projects/ocpilot/baselines/<version-folder>/`.

It exists so OCPilot can compare:

```
Project Site  VS  Versioned Clean Baseline
```

and classify differences into:

- OpenCart core
- ocStore modifications
- third-party extensions
- theme modifications
- custom project code

Without confusing them.

---

## What belongs in a baseline

| Category | Allowed content | Typical location |
|----------|-----------------|------------------|
| Clean OpenCart files | Vendor file tree, no live config secrets | `files/` |
| Clean ocStore files | ocStore vendor tree, no live config secrets | `files/` |
| Sanitized file manifests | Path lists, checksum labels, directory inventories | `manifest/` |
| Directory maps | Structural maps of core directories | `manifest/` or `notes/` |
| Version notes | Source URL, build label, PHP compatibility | `notes/` |
| Schema metadata | Table list, column summaries, prefix label | `database/` |
| Table descriptions | Human-readable schema notes — not live data | `database/` |
| Comparison notes | Known deltas vs upstream, ocStore-specific paths | `comparison-notes/` |
| Baseline passport | Standard identity record per baseline | `passports/` |

---

## What is forbidden in a baseline

| Forbidden | Reason |
|-----------|--------|
| Credentials | Security; repo is not a secret store |
| `config.php` secrets | Live DB host, user, password, keys |
| `admin/config.php` secrets | Admin path and DB credentials |
| Production site files | Baseline must be **clean vendor**, not a clone of a live dealership |
| Customer data | Orders, accounts, PII — never in baseline |
| API tokens | Payment, shipping, CRM integrations |
| Hosting credentials | FTP, panel, SSH passwords |
| Unsanitized full DB dumps | Risk of secrets and PII in git |

If operator material contains any of the above → **strip before repo intake** or keep external with metadata-only reference in passport.

---

## Storage philosophy

### Baseline is reference material, not a working project

| Reference baseline | Working project site |
|--------------------|----------------------|
| Frozen vendor truth for one version | Live or exported dealership install |
| No `config.php` with real values | Has operational config (external to repo) |
| No customer/session/cache state | Has uploads, cache, logs, user data |
| Used for **comparison and classification** | Used for **audit target** under `sites/<slug>/` |
| Updated only when operator adds a new pinned version | Evolves with project customizations |

A baseline answers: *«What would a clean OpenCart 3.0.3.7 / ocStore 3.0.3.7 look like on disk and in schema?»*

It does **not** answer: *«How do I run this site in production?»*

### Why separation matters

- **Core vs custom:** Without a clean reference, project theme overrides and extension files are easily mistaken for vendor core.
- **Update safety:** Rollback and change planning require knowing which files are vendor-owned.
- **Version truth:** Comparing a 3.0.3.7 site against a 2.3.0 baseline produces false deltas.
- **ocStore vs OpenCart:** ocStore baselines include known distribution differences; OpenCart baselines do not.

### Empty folders are valid (current stage)

Placeholder baselines with only `.gitkeep` files are **valid** until Run 3 (First Baseline Acquisition). OCPilot must **not** silently assume comparison is possible — see [baseline-readiness-checklist.md](baseline-readiness-checklist.md).

---

## Versioned baseline folders

| Path | Platform / version |
|------|-------------------|
| `baselines/opencart-230/` | OpenCart 2.3.0 |
| `baselines/opencart-3037/` | OpenCart 3.0.3.7 |
| `baselines/opencart-4x/` | OpenCart 4.x |
| `baselines/ocstore-230/` | ocStore 2.3.0 |
| `baselines/ocstore-3037/` | ocStore 3.0.3.7 |

Each folder follows the same subfolder contract — see [baselines/README.md](baselines/README.md).

**Legacy:** `baselines/clean-opencart/` remains a Phase 0 generic placeholder; prefer versioned folders for new work.

---

## Subfolder contract

| Folder | Purpose |
|--------|---------|
| `files/` | Sanitized vendor file tree (OpenCart or ocStore core files) |
| `database/` | Schema metadata, table descriptions, prefix notes — not live dumps |
| `notes/` | Version notes, source, exclusions, operator commentary |
| `manifest/` | File manifests, directory maps, checksum labels |
| `passports/` | Completed [versioned-baseline-passport-template.md](templates/versioned-baseline-passport-template.md) per baseline revision |
| `comparison-notes/` | Documented known differences vs upstream OpenCart or between ocStore builds |

---

## Operator intake rules (future — Run 3)

1. Select correct version folder (platform + version match).
2. Sanitize: remove configs with secrets, uploads, cache, logs, customer data.
3. Fill passport in `passports/`.
4. Add manifest in `manifest/` when file tree is present.
5. Run [baseline-readiness-checklist.md](baseline-readiness-checklist.md) before declaring baseline usable.

---

## Related documents

| Doc | Role |
|-----|------|
| [templates/versioned-baseline-passport-template.md](templates/versioned-baseline-passport-template.md) | Standard passport |
| [baseline-comparison-methodology.md](baseline-comparison-methodology.md) | How to compare site vs baseline |
| [baseline-readiness-checklist.md](baseline-readiness-checklist.md) | Can this baseline be used? |
| [clean-opencart-baseline.md](clean-opencart-baseline.md) | Why baseline exists (Run 1.5) |
| [boundaries.md](boundaries.md) | Secrets and forbidden paths |

---

## SAFE UNKNOWN

- Exact file counts and checksums per version — until operator upload (Run 3).
- Whether ocStore 4.x baseline folder will be added — not defined in Run 2.
- Automated manifest generation — **not** claimed; human-operated intake only.

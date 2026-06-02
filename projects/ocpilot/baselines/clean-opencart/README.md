# Clean OpenCart Baseline (Legacy / Generic Placeholder)

**Status:** **legacy / generic placeholder** from Phase 0 — **not** the preferred baseline target.

**Preferred targets:** versioned folders under [../README.md](../README.md) — `opencart-230/`, `opencart-3037/`, `opencart-4x/`, `ocstore-230/`, `ocstore-3037/`.

**Run:** OPERATIONAL-INDEX #2 (planned).  
**Guide:** [clean-opencart-baseline.md](../../clean-opencart-baseline.md)

## Folders

| Folder | Intended content |
|--------|------------------|
| `files/` | Sanitized vendor file tree for one pinned OC version |
| `database/` | Schema metadata or schema-only export labels — external storage for full dumps |
| `notes/` | Version, source, exclusions, passport markdown |

## Phase 0 / Run 1.5 state

Placeholder `.gitkeep` only. For new work, populate a **versioned** baseline folder instead of treating this generic path as canonical.

## Comparison

Project sites under `sites/<slug>/` should be diffed against the **matching versioned** baseline during read-only audits (Run 4–5).

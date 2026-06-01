# MIG pre-pilot freeze — pre-pilot-gruzotaxi-krasnodar-v1

| Field | Value |
|-------|-------|
| **Freeze label** | `pre-pilot-gruzotaxi-krasnodar-v1` |
| **Created** | 2026-06-01 |
| **Purpose** | Baseline before first real MIG pilot on **грузотакси Краснодар** / проект **Триумф** |
| **Status** | MIG Runtime MVP verified locally before pilot (all five `verify-*.mjs` scripts exit 0) |
| **Pilot** | **Not executed** — no production request for this niche in `incoming/mig/requests/` |

## Contents

| Path | Description |
|------|-------------|
| [mig-project/](mig-project/) | Snapshot of `projects/mig/` at freeze time (source, contracts, lib, schemas, tools, tests, config, reports, workflows, examples, sessions) |
| [incoming-mig/](incoming-mig/) | Snapshot of `incoming/mig/` drop zone and registry |
| [MANIFEST.txt](MANIFEST.txt) | Full list of copied files (relative paths) |

## Exclusions (by design)

- `node_modules/`
- `projects/mig/archive/` (other freezes; this folder is the freeze root)
- `test/.verify-*` ephemeral verify output directories
- `.env` and obvious credential filenames (none present in tree at freeze)
- Git metadata

## Verification record (freeze day)

Operator ran from repo root:

```text
node projects/mig/tools/verify-competitor-discovery-v0.mjs
node projects/mig/tools/verify-multi-query-discovery-v0.mjs
node projects/mig/tools/verify-website-acquisition-v0.mjs
node projects/mig/tools/verify-landing-analysis-v0.mjs
node projects/mig/tools/verify-runtime-mvp-v0.mjs
```

All returned `"status": "ok"`.

## Restore note

This is a **local documentation/runtime baseline**, not a deployment artifact. To compare or restore files, copy from `mig-project/` or `incoming-mig/` into the live tree **only with explicit human approval** — do not overwrite active sessions or inbox state blindly.

## Related git checkpoint

Commit message (when applied): `MIG pre-pilot freeze before gruzotaxi Krasnodar test`

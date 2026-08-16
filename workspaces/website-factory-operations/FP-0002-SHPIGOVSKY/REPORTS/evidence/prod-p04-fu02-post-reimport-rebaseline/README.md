# Evidence — PROD-P04-FU02 Post-Reimport Production Rebaseline

**Date:** 2026-08-14  
**Wave:** PROD-P04-FU02  
**Mutations:** none (read-only production inspection + local evidence/docs)

## Required manifests

* `production-source-parity-manifest.json`
* `production-db-baseline.json`
* `pre-vs-post-reimport-diff.json`
* `migration-residue-map.json`
* `wpilot-state.json`
* `frontend-route-matrix.json`

## Supporting

* `access-revalidation.json`
* `runtime-identity.json`
* `environment-residue.json`
* `acf-json-reconcile.json`
* `wp-admin-rebaseline.json`
* `wp-admin-password-check.json` (match boolean only; no hash/password values)
* `imported-content-delta.json`
* `content-inventory.json`
* `recent-content-modified.json`
* `material-css-drift-review.json`
* `production-only-bak-review.json`
* `authority-transition.json`
* `session-summary.json`
* `safe-wp-config-metadata.json`

Helper scripts in this folder (`_run_rebaseline.py`, `_followup*.py`, `_password_check.py`) are local probe tools — not production mutators.

**Prior historical baseline:** `../prod-p04-fu01-filesystem-baseline/`

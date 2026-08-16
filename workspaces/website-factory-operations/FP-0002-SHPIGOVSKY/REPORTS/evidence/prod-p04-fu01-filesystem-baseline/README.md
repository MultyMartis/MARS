# PROD-P04-FU01 — Filesystem baseline evidence

**Date:** 2026-08-13  
**Mutations:** none (SSH/FTP READ + SHA only)

## Key artifacts

- `filesystem-read-proof.json` — auth + real WordPress root READ proven
- `safe-wp-config-metadata.json` — safe keys only (no passwords/salts)
- `production-source-parity-manifest.json` — theme + shpigovsky-core + ACF JSON + WPilot summary
- `theme-parity.json` / `shpigovsky-core-parity.json` / `acf-json-parity.json` / `wpilot-parity.json`
- `wpilot-upgrade-delta.json` — 0.3.0 → 0.3.2-RC1 delta; package replace safety
- `material-production-drift.json` — non-MATCH product drift
- `wordpress-core-identity.json`
- `_run_baseline.py` — read-only runner used this wave (no secrets embedded)

## Secret safety

No passwords, tokens, salts, or wp-config dumps in this folder.

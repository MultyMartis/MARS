# ISEO Sales — Cutover Prep Evidence Pack v1

**Wave:** Controlled Postgres cutover prep 01  
**Date:** 2026-09-03  
**Charter:** PREP ONLY — no production cutover, no SoT switch, no Admin.dev mutation

## Hard-stop end state (observed)

| Item | Required | Observed |
|------|----------|----------|
| Operational.dev | ACTIVE | YES `xSnXPy8cEHoZw6xG` |
| Operational.v3.dev | INACTIVE | YES `NH4uV145Amrgnmkm` |
| Operational.v3.rollback | INACTIVE | YES `favawMOzVwtFMdyH` |
| Sheets SoT | authoritative | YES |
| PostgreSQL | validated candidate / shadow | YES (`PG_CANDIDATE_VALIDATED`, `sheets_sot=true`) |

## Index

| Artifact | Purpose |
|----------|---------|
| `workflow_state.json` | Live n8n active/inactive + node credential type counts |
| `rollback_pin_proof.json` | PG-compatible rollback pin IDs/hashes |
| `workflow_releases_listing.txt` | `mars_core.workflow_releases` statuses |
| `register_*.sql` | Registry INSERT scripts (sanitized) |
| `delta_dry_run_summary.json` | Shadow refresh / delta dry-run vs prior apply |
| `malformed_delivery_exclusion.json` | LEGACY INVALID ROW exclusion |
| `in_flight_execution_policy.json` | Deterministic in-flight rules |
| `authority_state_model.json` | Authority progression + marker store |
| `authority_marker_update.txt` | `mars_core.apps.metadata` UPDATE proof |
| `backup_restore_gate_status.json` | Local / nightly / off-host / restore gates |
| `backup_restore_gate_probe.txt` | Host probe (paths/perms only) |
| `encryptionkey_residual_audit.json` | Cutover impact classification inputs |
| `credential_dependency_map.json` | v3 credential types (no secrets) |
| `admin_dev_dependency_inventory.json` | Admin Sheets R/W forensic |
| `cutover_topology_verdict.json` | A/B/C topology decision |
| `preflight_checklist.json` | Pre-cutover gates |
| `rollback_triggers.json` | Hard vs non-rollback observations |
| `AUTHORITY-STATE-v1.md` | Human-readable authority marker notes |

No secrets / PII in this pack.

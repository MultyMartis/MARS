# SITE-002 Source Artifact Inventory

| Artifact/field | Authority | Used by adapter | Security class |
|----------------|-----------|-----------------|----------------|
| monitor-classification.json | Primary classification | YES | MACHINE |
| changed-summary.json | Metric authority | YES | MACHINE |
| run-summary.json | Execution metadata / run_id | YES (allowlisted keys) | MACHINE |
| run_id | run-summary / folder name | YES identity | MACHINE |
| finished_at / observed_at | run / monitor | YES identity | MACHINE |
| classification | monitor (primary) | YES | MACHINE |
| baseline_url_count etc. | changed-summary | YES | MACHINE |
| artifact_paths | run-summary | STRIP always | PATH / SENSITIVE |
| run.log | debug | NEVER loaded | RAW_LOG |
| sitemap XML / URL lists | companions | NOT required for MVP adapter | PRESENTATION / URL |
| duration_human | presentation | STRIP | PRESENTATION |

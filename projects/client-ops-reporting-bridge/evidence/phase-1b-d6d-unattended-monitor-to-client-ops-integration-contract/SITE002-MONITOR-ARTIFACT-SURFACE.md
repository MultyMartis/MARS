# SITE002-MONITOR-ARTIFACT-SURFACE

Token: D6D_SITE002_MONITOR_ARTIFACT_SURFACE_MAPPED

- Entrypoint: site-002-prod-post-1c-catalog-onboarding-monitor-02.py
- Runner: site-002-post-1c-monitor-runner.ps1
- Scheduler action: powershell → runtime runner
- Output root: X:\\AI MARS STORAGE\\ocpilot\\project-sites\\site-002\\production\\scheduled-monitors\\post-1c\\<run_id>\\
- Machine JSON: run-summary.json, monitor-classification.json, changed-summary.json
- Completion: run directory + exit_code + finished_at; D6D adds run-complete.marker contract for producer intake
- Writes: Path.write_text (non-atomic); producer requires stabilization
- Classifications: NO_ACTION_REQUIRED / ONBOARDING_REQUIRED / HYGIENE_REVIEW_REQUIRED / FAILURE_REVIEW_REQUIRED

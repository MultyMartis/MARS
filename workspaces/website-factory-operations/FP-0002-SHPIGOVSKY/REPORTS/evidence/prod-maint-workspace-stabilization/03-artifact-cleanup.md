# Artifact cleanup decisions

## Removed (proven disposable)

| Item | Location | Reason |
|------|----------|--------|
| `_audit_extract_temp.cpython-314.pyc` | REPORTS/__pycache__/ (tracked) | Accidental tracked bytecode; covered by root .gitignore |

## Discarded with worktree retirement (not copied to canon)

| Item | Worktree | Class |
|------|----------|-------|
| `test-results/` | p18e-cd | TEMPORARY_JUNK |
| Intermediate PrivacyConsent WIP vs later canon | p18e-cd | SUPERSEDED |
| Re-intake `01-olya-admin-intake.json` drift | p18g-push-v2 | RUNTIME_ONLY |
| `_p18i_privacy_smoke.mjs` + `node_modules/` | p18i | TEMPORARY_JUNK |
| `05-git-receipt.json` | p23 | GENERATED_EVIDENCE (SHA already on remote) |

## Retained

- All canonical REPORTS / evidence under FP-0002-SHPIGOVSKY
- Local secrets under `X:\AI MARS\local\` and INCOMING/04_ACCESS (gitignored)
- Historical baselines and P18* reports

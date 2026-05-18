# WPilot Backup And Rollback Rules

**Status:** documented safety rules.

## Backup Confirmation

Before any write-like action, confirm:

- File backup exists.
- Database backup exists.
- Backup timestamp or recency is acceptable to the operator.
- Backup storage location is outside this repo.
- Restore owner is known.
- Restore method is understood at a high level.

Record only sanitized facts. Do not store backup archives, database dumps, or secret-bearing screenshots in the repo.

## Rollback Plan Requirements

Each approved change needs a rollback plan with:

- Exact target.
- Before state summary.
- Change action.
- Rollback action.
- Verification step.
- Stop conditions.
- Human owner.

Use [templates/rollback-plan-template.md](templates/rollback-plan-template.md).

## Safe Rollback Targets

Preferred MVP rollback targets:

- Revert a child theme CSS patch.
- Delete or draft a test page created during the run.
- Restore a copied test page to its before state.
- Remove a clearly labeled test file created only for the run.

## Disallowed MVP Rollback Dependencies

Do not depend on:

- Editing `wp-config.php`.
- Direct database writes.
- Plugin/theme/core updates.
- Production restore drills.
- Unverified hosting-panel actions.
- Any rollback that requires storing credentials in repo.

## Stop And Escalate

Stop and escalate to the human operator if:

- Backup cannot be confirmed.
- Rollback path depends on unknown permissions.
- A cache, builder, or theme option makes the target ownership unclear.
- File state changed outside the approved target.
- Site behavior differs from expectation after the test.

## SAFE UNKNOWN

Backup integrity, restore speed, Beget retention, and database restore behavior remain SAFE UNKNOWN until verified in the external system by the operator.

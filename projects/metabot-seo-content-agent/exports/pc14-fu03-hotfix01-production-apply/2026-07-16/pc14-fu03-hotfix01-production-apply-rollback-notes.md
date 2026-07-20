# PC14-FU03 HOTFIX01 Production Rollback Notes

## Scope
Production Worker only: `p4mqb4VuPcemIDlC` (`SEO Content Agent Beta.v14 - Worker`).

## Preferred rollback
1. PUT production from raw before backup:
   `local/pc14-fu03-hotfix01-production-apply-2026-07-16/rollback/worker-before-hotfix01.raw.json`
2. Confirm active=true after restore.
3. Confirm restore nodes again hard-require `$('Format Run Pipeline').all()`.
4. Confirm `Run Strict Surface Repair` remains enabled.
5. Confirm PC-07 Close Lock and TZ HOTFIX01 unchanged.

## Alternate
Replace jsCode on:
- Restore Format Run Items
- Restore Format Run Items After Lock
with pre-hotfix broken baseline (150-char hard-require).

## Do not
- Do not roll back Intake/Admin.
- Do not deactivate production during rollback unless separately chartered.
- Do not touch sandbox for production rollback.

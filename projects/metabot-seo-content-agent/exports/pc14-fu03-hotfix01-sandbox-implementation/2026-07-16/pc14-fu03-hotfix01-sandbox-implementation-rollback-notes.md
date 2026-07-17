# PC14-FU03 HOTFIX01 Sandbox Rollback Notes

## Scope
Sandbox only: `tVGWi7Ud3zz2eGKo` (`SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu03`).

## Preferred rollback
1. PUT sandbox from raw before export:
   `local/pc14-fu03-hotfix01-sandbox-implementation-2026-07-16/before/sandbox-worker.raw.json`
2. Confirm active=false after restore.
3. Confirm restore nodes again hard-require `$('Format Run Pipeline').all()`.

## Alternate
Replace jsCode on:
- Restore Format Run Items
- Restore Format Run Items After Lock
with pre-hotfix broken baseline.

## Do not
- Do not roll back production for this sandbox-only change.
- Do not activate sandbox during rollback verification unless separately chartered.

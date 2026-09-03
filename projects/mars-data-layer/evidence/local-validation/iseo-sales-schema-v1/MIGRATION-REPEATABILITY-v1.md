# MIGRATION-REPEATABILITY-v1

**Contract:** destroy/reset disposable DB only → recreate → apply from zero → SUCCESS again.

| Pass | Command | Result |
|------|---------|--------|
| 2 | `apply_and_test.ps1 -ResetFirst` | SUCCESS |
| 3 | `apply_and_test.ps1 -ResetFirst` | SUCCESS + `_repeatability-pass3.ok` |

**Conclusion:** no hidden manual DB state required. Source migrations alone reproduce the schema.

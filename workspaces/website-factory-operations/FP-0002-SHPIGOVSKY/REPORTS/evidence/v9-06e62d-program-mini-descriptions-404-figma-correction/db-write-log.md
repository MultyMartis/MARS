# DB write log — V9-06E62D

## Allowed writes
- Seeded treatment_program_short_description + _treatment_program_short_description on pages 1053/1054/1055/1056
- Temporary edit-test on 1053 (test string) then restored
- Temporary empty-field test on 1053 then restored
- Re-fix of 1053 after PowerShell escaping corruption during restore

## Final state
All four pages hold the former hardcoded Home direction texts.
Unrelated postmeta writes for this key: 0

## Idempotency
Second presence check: 4/4 rows present; non-empty values preserved on re-run path.

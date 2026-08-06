# Test fixture inventory

| Artifact | Classification | Action |
|---|---|---|
| TEST_LEADS ×2 (phase3g11 markers) | safe to delete from TEST contour | cleared |
| TEST_LEAD_EVENTS | empty / header-only | none |
| lead_clean_v2 synthetic rows (phase3b1) | legacy synthetic; not in LEADS SoT | preserve; excluded from reminder source after patch |
| LEAD_EVENTS synthetic phase3b1 | legacy | preserve; not counted by /stats epoch LEADS |
| PROFILE_EVENTS seed rows | sanitized evidence | preserve |
| REMINDER_DELIVERIES meta garbage | accidental schema contamination | repaired headers; data cleared |
| RECIPIENT_REPLIES meta garbage | accidental schema contamination | repaired headers; data cleared |
| reporting Лиды CLIENT_A | production | preserve |
| SAFE UNKNOWN | none requiring delete | — |

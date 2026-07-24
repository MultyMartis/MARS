# SITE-002 Status Mapping

| Source state | Client Ops status | Evidence | Fail behavior |
|--------------|-------------------|----------|---------------|
| NO_ACTION_REQUIRED | OK | tools README + normalizer | conflict/onboarding>0 to BLOCKED |
| ONBOARDING_REQUIRED | ATTENTION | tools README + normalizer | onboarding==0 to BLOCKED |
| HYGIENE_REVIEW_REQUIRED | ATTENTION | hardening report | — |
| FAILURE_REVIEW_REQUIRED | FAILED | tools README | also exit_code!=0 to FAILED |
| classification mismatch | BLOCKED | ARTIFACT-AUTHORITY | SOURCE_ARTIFACT_CONFLICT |
| unknown status | BLOCKED | D4 adapter | SOURCE_SCHEMA_UNSUPPORTED |
| incomplete/malformed | BLOCKED | D4 gate | never OK |

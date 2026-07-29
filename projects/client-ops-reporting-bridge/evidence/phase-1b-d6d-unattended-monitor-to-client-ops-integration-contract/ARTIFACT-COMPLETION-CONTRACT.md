# ARTIFACT-COMPLETION-CONTRACT

Token: D6D_ARTIFACT_COMPLETION_CONTRACT_DEFINED

Require: exists, schema, size>0, parse OK, run_id, observed_at, completion marker, terminal classification, stable hash/size, allowlisted root, not future beyond skew.
Reject: .tmp/.part, incomplete JSON, changing file, missing marker/fields, outside allowlist.

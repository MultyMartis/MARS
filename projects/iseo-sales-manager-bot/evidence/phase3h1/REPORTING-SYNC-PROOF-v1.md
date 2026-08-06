# Reporting sync proof

Model A — tests excluded / no automatic production reporting writes:

1. No reporting writer nodes on live Ops/Admin → new isolated test cannot auto-insert into production `Лиды`
2. Existing CLIENT_A reporting row remains the only production reporting lead row
3. TEST_LEADS cleanup did not touch reporting
4. Proof recorded via forensic HTTP reads (sanitized)

PASS for MANUAL classification.

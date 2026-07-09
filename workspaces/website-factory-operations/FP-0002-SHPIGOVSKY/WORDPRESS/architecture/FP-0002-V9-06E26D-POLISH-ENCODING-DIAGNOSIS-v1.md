# FP-0002 V9-06E26D-POLISH Encoding Diagnosis v1

- Likely cause: Stored taxonomy term name for default category (term_id=1) contains mojibake (UTF-8 Cyrillic misinterpreted and re-saved as box-drawing Unicode). Schema charset utf8mb4 is correct; issue is bad stored value, not connection/collation mismatch.
- Schema migration needed: **NO**
- DB charset: `utf8mb4` / `utf8mb4_unicode_ci`

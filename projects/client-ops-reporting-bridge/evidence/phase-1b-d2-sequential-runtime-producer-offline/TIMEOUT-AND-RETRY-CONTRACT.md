# Timeout and Retry Contract

connect_timeout_ms default 5000; request_timeout_ms default 30000; bounds 100..120000.
max_retries default 0; automatic retries disabled.
Ambiguous timeout → MANUAL_DEDUPE_CHECK_REQUIRED.

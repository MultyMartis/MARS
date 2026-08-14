# SHEETS 429 RETRY CONTRACT (evidence copy)

See canonical: [architecture/SHEETS-429-RETRY-CONTRACT-v1.md](../../architecture/SHEETS-429-RETRY-CONTRACT-v1.md)

Chosen policy: attempt 1 immediate; retries after ~5s / ~15s / ~30s; max 4 attempts; Retry-After 1–120s when sane; 429 only; fail closed; no infinite loop.

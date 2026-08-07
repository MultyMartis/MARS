# Security Review

- No webhook URL/secret/token printed in evidence
- Kill switch not exposed on public unauthenticated mutable endpoint
- Watchdog gateway remains token-gated
- Admin shows boolean UI label only
- Beget/SSH/FTP credentials not written to git
- Runtime `run-token.SECRET.txt` kept under Storage tmp only (not copied to evidence)

# SITE-002 Source Firewall

1. SITE-002 adapter firewall (site002_adapter_firewall.py) — allowlist; strip artifact_paths/duration_human; reject password/token/sql/stack/path carriers.
2. Generic producer firewall (producer_firewall.py).
3. Envelope security validator (Phase 1A).

Unknown keys: strip if harmless; reject if security-sensitive. run.log never loaded.

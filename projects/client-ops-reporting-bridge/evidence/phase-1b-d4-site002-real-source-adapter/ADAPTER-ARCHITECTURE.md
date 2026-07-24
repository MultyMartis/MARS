# Adapter Architecture

explicit SITE-002 artifact directory
  -> parse_source
  -> SITE-002 adapter firewall
  -> validate completeness
  -> normalize (Phase 1A)
  -> producer input + envelope
  -> producer offline transport (mock|fixture|disabled)

CLI: site002-adapter-dry-run --source <dir>

Forbidden: --latest, --watch, --live, --apply, --transport http, D3 phrases.

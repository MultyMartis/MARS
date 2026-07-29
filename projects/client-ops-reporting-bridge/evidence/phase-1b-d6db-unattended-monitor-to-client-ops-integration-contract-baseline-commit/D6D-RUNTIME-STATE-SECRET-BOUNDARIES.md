# D6D-RUNTIME-STATE-SECRET-BOUNDARIES

Cursor/lock/receipt/marker must contain no secrets.

State roots are local/outside Git. Secrets (n8n API key, Telegram token, webhook secret) never enter cursor/receipt/marker payloads.

# LIVE-ENDPOINT-ALLOWLIST

Approved host class: `n8n.ai-metacode.com` (exact).

Required:

- scheme `https`
- path starts with `/webhook/`
- no userinfo
- no query
- no fragment
- no localhost
- port absent or 443
- endpoint derived only from ignored `producer.local.json`
- no CLI `--url`
- no arbitrary URL posting

Evidence may record: scheme, host_approved, path_prefix_ok, port — never full URL.

# FIX-02 operator checklist — manual v2rayN profile (no URI import)

Do **NOT** import via VLESS share URI for this profile — URI import path mis-maps REALITY fields (PublicKey receives shortId).

Create a **new** profile in v2rayN UI:

- Display name: `MCA-ONE-EQ-ALT-A-REALITY-VISION-FIX02`
- Protocol: VLESS
- Address: `95.216.126.173`
- Port: `9443`
- UUID: from `client-secrets.local.json` (do not paste into chat)
- Encryption: `none`
- Flow: `xtls-rprx-vision`
- Network: `tcp` (v2rayN may show/store as `raw`)
- Security / Stream: `reality`
- SNI / serverName: `www.cloudflare.com`
- Fingerprint: `chrome`
- PublicKey: from `client-secrets.local.json` → `publicKey` (43-char url-safe base64; sha12 must be `e83743293573`)
- ShortId: `4fbd0c29e602e688`
- SpiderX: `/`

Validation gates:

1. Activate profile — must **not** show `Свойство PublicKey недопустимо`.
2. Only then test transport / TUN.

Alternate test path (already validated for startup):

- `fix02-direct-xray-client.local.json` + Xray 26.7.28 `run -test` = Configuration OK
- Isolated SOCKS `127.0.0.1:18088` transport currently **TIMEOUT** (config-valid; network path not cleared)

Do not touch EQVPS `:8443` or rotate REALITY keys.

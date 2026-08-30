# EQVPS-MICRO-IP — MCA Custom v2.1 endpoint DNS bootstrap fix (2026-08-28)

## Status

**Verdict:** `CUSTOM_V2_1_LOCAL_PASS`

Local-only corrected variant created. Active VEESP profile was not switched. No server mutation. No v2rayN DB/import. No git commit --trailer "Co-authored-by: Cursor <cursoragent@cursor.com>".

## Problem (evidence-based)

Custom v2 inherited the VEESP DNS/routing shell, including a direct-DNS endpoint bootstrap exemption for the stale VEESP hostname `wsp-cloud.com`, while the proxy endpoint was changed to `metacode-cloud.com`.

Result: `metacode-cloud.com` was not on the direct DNS bootstrap path; its DNS query could be sent through the proxy that cannot exist until that hostname resolves (DNS/proxy recursion).

## Source / Output

| Role | Path |
|------|------|
| Source | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-custom-config\MCA-ONE-PRIMARY-443-CUSTOM-v2.json` |
| Output | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-custom-config\MCA-ONE-PRIMARY-443-CUSTOM-v2.1.json` |

## Exact semantic change

Single line in `dns.servers[]` entry tagged `direct-dns-1` domains list:

- **before:** `"wsp-cloud.com"`
- **after:** `"metacode-cloud.com"`

Occurrence scan: exactly one quoted `"wsp-cloud.com"` existed in Custom v2 (line 94). It was the endpoint bootstrap exemption (not a `domain:` geosite-style rule). No other `wsp-cloud.com` occurrences. Proxy `address` / TLS `serverName` / XHTTP `host` already used `metacode-cloud.com` and were left untouched.

Line-level diff count between v2 and v2.1: **1**.

## Structural diff gate

| Gate | Result |
|------|--------|
| PROXY_OUTBOUND_IDENTICAL | YES |
| XHTTP_IDENTICAL | YES |
| TLS_IDENTICAL | YES |
| INBOUNDS_IDENTICAL | YES |
| TUN_IDENTICAL | YES |
| ROUTING_RULES_IDENTICAL | YES |
| ROUTING_RULE_ORDER_IDENTICAL | YES |
| DNS_SERVERS_IDENTICAL_EXCEPT_ENDPOINT_DOMAIN | YES |
| DIRECT_OUTBOUND_IDENTICAL | YES |
| BLOCK_OUTBOUND_IDENTICAL | YES |

## Bootstrap trace (v2.1 — `metacode-cloud.com`)

1. Hostname enters DNS subsystem (`dns-module`).
2. Matches `direct-dns-1` domains entry `metacode-cloud.com` (DoH `https://1.1.1.1/dns-query`, `skipFallback: true`).
3. DNS query uses the direct-DNS path and does **not** require the proxy outbound.
4. Hostname can resolve before the VLESS/TLS/XHTTP session is established.
5. Xray connects directly to `metacode-cloud.com:443`.
6. VLESS/TLS/XHTTP proxy becomes available.
7. Ordinary foreign catch-all traffic can then use `proxy`.

Stale bootstrap dependency: `wsp-cloud.com` removed from `direct-dns-1` — **gone** in v2.1.

## Local validation (isolated; did not use 10808)

Bundled Xray: `%LOCALAPPDATA%\v2rayN\bin\xray\xray.exe` with `XRAY_LOCATION_ASSET=%LOCALAPPDATA%\v2rayN\bin`.

| Check | Result |
|-------|--------|
| v2.1 full config `-test` | Geo assets OK; TUN private-namespace create denied while VEESP TUN already active (expected under concurrent VEESP; not a JSON syntax failure) |
| Isolated temp config (TUN removed, mixed port **18088**, api **18012**) `-test` | **Configuration OK** |
| Temporary mixed proxy | `127.0.0.1:18088` only |
| `curl -x http://127.0.0.1:18088 https://api.ipify.org` | **`95.216.126.173`** (exact match) |
| `https://www.google.com` | exit 0; HTML received (~84KB) |
| `https://www.youtube.com` | curl exit 56 (truncated receive) but YouTube HTML DOCTYPE received (~265KB) — content reachable under isolated test |

Isolated Xray was stopped after tests. Operator VEESP listener on `10808` left intact. Active profile not switched.

**Not claimed:** browser/TUN production PASS. Operator must import v2.1 into v2rayN for acceptance.

## Non-mutation confirmations

- Server mutation: **NO**
- v2rayN DB / active profile / import: **NO**
- EQVPS / VEESP live configs: **NO**
- Git commit: **NO**

## Raw evidence (local, not for commit unless separately chartered)

`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-custom-v2-1-bootstrap-raw-2026-08-28\`

Includes: `line-diff.txt`, `replacement-evidence.txt`, `structural-diff-gate.json`, `xray-*-config-test.txt`, `validation-summary.txt`, curl meta/heads.

## WHAT OPERATOR DOES NOW

1. Import: `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-custom-config\MCA-ONE-PRIMARY-443-CUSTOM-v2.1.json`
2. Remarks: `MCA-ONE-PRIMARY-443-CUSTOM-v2.1`
3. Activate manually
4. `curl.exe -sS -x http://127.0.0.1:10808 https://api.ipify.org` → expect `95.216.126.173`
5. Browser: ChatGPT, YouTube, Google, representative `.ru` site
6. Report exact results
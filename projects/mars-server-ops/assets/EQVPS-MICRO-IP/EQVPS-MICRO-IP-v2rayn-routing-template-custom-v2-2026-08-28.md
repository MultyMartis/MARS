# REPORT — MCA CUSTOM V2 FROM WORKING VEESP ROUTING

**Date:** 2026-08-28  
**Scope:** Local-only. Build MCA Custom Config v2 by cloning the **actual working VEESP/MCA-Gate v2rayN runtime** (routing/DNS/inbounds/direct/block) and replacing **only** outbound `tag=proxy` with the proven EQVPS VLESS+TLS+XHTTP outbound.  
**Mutations:** EQVPS / 3X-UI / Server A / DNS / UFW / SSH / AdminVPS / v2rayN upgrade / Xray upgrade / VEESP profile overwrite / auto-import into v2rayN DB — **NONE**.  
**Git:** no commit.

**Raw evidence (local, not in git):**  
`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-routing-template-raw-2026-08-28\`

**Custom v2 (local, not in git):**  
`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-custom-config\MCA-ONE-PRIMARY-443-CUSTOM-v2.json`

---

## Verdict

**READY_FOR_OPERATOR_CUSTOM_V2_TEST**

Local structural identity vs VEESP runtime: **PASS** (routing/DNS/inbounds/direct/block identical).  
Bundled Xray config validation: **PASS** (`Configuration OK`).  
Isolated live proxy on `127.0.0.1:18088`: **PASS** (`api.ipify.org` → `95.216.126.173`; Google/YouTube generate_204 → HTTP 204).  
Browser / system-proxy acceptance vs VEESP: **NOT RUN** — operator must import Custom v2 and compare.

---

## Working VEESP runtime

| Field | Value |
|-------|-------|
| **Captured path** | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-routing-template-raw-2026-08-28\veesp-working-runtime.json` |
| **Source** | `C:\Program Files\v2rayN\binConfigs\config.json` (copy only; original not overwritten) |
| **Capture timestamp** | 2026-08-28T22:22:56+07:00 (metadata refreshed in same wave) |
| **Active IndexId** | `4850651204958926275` (`guiNConfig.json`) |
| **Active profile proof** | outbound `proxy` → **`wsp-cloud.com:8443`**, `network=raw`, `security=tls` (matches known **MCA-Gate-TLS-MCA-ONE** / VEESP leg) |
| **metacode-cloud.com in runtime** | **NO** at capture time |
| **Xray PID (live v2rayN)** | `21480` (left running; not stopped) |
| **v2rayN** | **7.22.3** (`7.22.3+ccb0ffb3b6e15757a87ee1acd64a87fc5b9e8137`) |
| **Xray (bundled)** | **26.7.28** — `C:\Program Files\v2rayN\bin\xray\xray.exe` |

**Note:** `guiNDB.db` `ProfileItem` table was empty in this environment; address/port/network from live `config.json` is the authoritative activation proof. IndexId matches the prior documented MCA-Gate binding.

Sanitized copies (UUID redacted): `veesp-working-runtime.sanitized.json`, `MCA-ONE-PRIMARY-443-CUSTOM-v2.sanitized.json` under the raw evidence directory.

---

## Preserved behavior

### Inbounds

| Tag | Protocol | Listen | Port | Notes |
|-----|----------|--------|------|-------|
| `socks` | `mixed` | `127.0.0.1` | `10808` | UDP enabled; sniffing `http`/`tls` |
| `tun` | `tun` | — | — | Present in template (v2rayN TUN mode); sniffing enabled |
| `api` | `dokodemo-door` | `127.0.0.1` | `10812` | API inbound |

### Routing

- **domainStrategy:** `AsIs`
- **Rule count:** 18 (order preserved exactly)
- **RU / direct split (authoritative from captured runtime):**
  - `domain:ru`, Cyrillic РФ TLD, `domain:xn--` → **direct**
  - `domain:vk.com`, `cp.beget.com`, `kaspersky.com`, `bip.com` → **direct**
  - `geosite:category-ru` → **direct**
  - `geoip:ru` → **direct**
  - selected local apps (process list) → **direct**
  - `geoip:private` / `geosite:private` → **direct**
- **VPN / proxy:** catch-all `port: 0-65535` → **proxy** (foreign traffic)
- **Block:** UDP noise ports; multicast; **UDP/443** (QUIC) → **block**
- **DNS routing:** port 53 / TUN DNS / `direct-dns-*` / `dns-module` tags preserved

### DNS

- **hosts:** pinned resolvers for Google / Cloudflare / AliDNS / etc. (unchanged)
- **servers:**
  1. DoH `https://1.1.1.1/dns-query` for RU/related domains + `wsp-cloud.com` (`direct-dns-1`, skipFallback)
  2. DoH for `geosite:category-ru` + `geosite:private` (`direct-dns-2`, skipFallback)
  3. `8.8.8.8` for `full:dns.google`
  4. fallback `https://dns.google/dns-query`
- **tag:** present on DNS object (unchanged)

### Direct / block / dns outbounds

- Tags **`direct`**, **`block`**, **`dns`** byte-identical vs VEESP runtime
- Freedom / blackhole / DNS outbound settings unchanged
- Policy / stats / metrics / log top-level sections unchanged

---

## EQVPS replacement outbound

Replaced **only** outbound with `tag: proxy`.

| Field | Value |
|-------|-------|
| **protocol** | VLESS |
| **address / domain** | `metacode-cloud.com` |
| **port** | `443` |
| **TLS** | `security=tls`, SNI `metacode-cloud.com`, ALPN `h2,http/1.1`, fingerprint `chrome` |
| **XHTTP** | path `/x51a604f9239b1186`, host `metacode-cloud.com`, mode `auto` |
| **padding** | `xPaddingBytes: 100-1000` (top-level under `xhttpSettings`) |
| **scMax** | `scMaxBufferedPosts: 30`, `scMaxEachPostBytes: 1000000`, `scStreamUpServerSecs: 20-80` |
| **source** | `xhttp-client-forensic-raw-2026-08-28\standalone-primary-corrected.json` |
| **tag** | **`proxy`** (kept so all routing rules still target the same logical outbound) |

UUID / secrets: **not** reproduced in this git-safe document (present only in local JSON).

---

## Structural diff

| FIELD/SECTION | VEESP WORKING | MCA CUSTOM V2 | STATUS |
|---------------|---------------|---------------|--------|
| routing (all rules) | present | identical | **IDENTICAL** |
| dns | present | identical | **IDENTICAL** |
| inbounds | mixed+tun+api | identical | **IDENTICAL** |
| outbound `direct` | present | identical | **IDENTICAL** |
| outbound `block` | present | identical | **IDENTICAL** |
| outbound `dns` | present | identical | **IDENTICAL** |
| outbound `proxy` address | `wsp-cloud.com` | `metacode-cloud.com` | **REPLACED (intended)** |
| outbound `proxy` port | `8443` | `443` | **REPLACED (intended)** |
| outbound `proxy` network | `raw` | `xhttp` | **REPLACED (intended)** |
| outbound `proxy` TLS/XHTTP | VEESP raw/TLS | EQVPS XHTTP/TLS | **REPLACED (intended)** |
| log / policy / stats / metrics | present | identical | **IDENTICAL** |

**Classification:**

| Check | Result |
|-------|--------|
| ROUTING_IDENTICAL | **YES** |
| DNS_IDENTICAL | **YES** |
| INBOUNDS_IDENTICAL | **YES** |
| DIRECT_OUTBOUND_IDENTICAL | **YES** |
| BLOCK_OUTBOUND_IDENTICAL | **YES** |

No accidental routing/DNS drift.

---

## Routing semantic examples

Authoritative interpretation from **captured VEESP rule order** (geosite contents not expanded offline; foreign hosts fall through to catch-all **proxy** unless matched earlier):

| Target | Expected outbound | Basis |
|--------|-------------------|-------|
| `youtube.com` | **proxy** | catch-all rule port `0-65535` |
| `googlevideo.com` | **proxy** | catch-all |
| `ytimg.com` | **proxy** | catch-all |
| `google.com` | **proxy** | catch-all |
| `chatgpt.com` | **proxy** | catch-all |
| `openai.com` | **proxy** | catch-all |
| `api.ipify.org` | **proxy** | catch-all |
| representative `.ru` (`yandex.ru`, `mail.ru`, `vk.ru`) | **direct** | `domain:ru` |
| private / RFC1918 | **direct** | `geoip:private` |
| QUIC (`UDP/443`) | **block** | explicit UDP/443 block |

This matches the operator’s stated intent: foreign/non-RU via VPN; `.ru` / RU category via Goodline direct — **without changing rule semantics**.

---

## Local validation

| Step | Result |
|------|--------|
| `xray run -test` on Custom v2 | **PASS** — `Configuration OK` (Xray 26.7.28 + geo assets from `v2rayN\bin`) |
| Isolated temp inbound | `127.0.0.1:18088` (TUN stripped **only** in temp test copy; production Custom v2 retains TUN) |
| `curl -x http://127.0.0.1:18088 https://api.ipify.org` | **PASS** → `95.216.126.173` |
| Google `generate_204` via temp proxy | **PASS** → HTTP `204` |
| YouTube `generate_204` via temp proxy | **PASS** → HTTP `204` |
| Live v2rayN Xray PID 21480 | **untouched** after test stop |

Evidence files under raw dir: `xray-test-validation.txt`, `isolated-live-test.txt`, `structural-diff.json`, `routing-semantic-parse.json`.

---

## Server mutation

**NO**

## v2rayN mutation

**NO** (no DB write, no profile overwrite, no auto-import, no `binConfigs` write)

---

## Custom v2 path

`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-custom-config\MCA-ONE-PRIMARY-443-CUSTOM-v2.json`

---

## WHAT OPERATOR DOES NOW

1. v2rayN → **Servers → Add Custom Configuration**
2. Import:  
   `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-custom-config\MCA-ONE-PRIMARY-443-CUSTOM-v2.json`
3. Remarks: `MCA-ONE-PRIMARY-443-CUSTOM-v2`
4. Activate it (leave TUN/system-proxy settings as used with VEESP)
5. Test in **normal browser** (same session environment as VEESP): Google, YouTube, ChatGPT
6. Verify `.ru` direct behavior remains as before
7. Run:  
   `curl.exe -x http://127.0.0.1:10808 https://api.ipify.org`  
   Expect: `95.216.126.173`
8. Report: Google / YouTube / ChatGPT / `.ru` direct PASS|FAIL + ipify result

**Do not** build `:8443` Custom v2 yet.  
**Do not** delete or overwrite **MCA-Gate-TLS-MCA-ONE**.

Stop.

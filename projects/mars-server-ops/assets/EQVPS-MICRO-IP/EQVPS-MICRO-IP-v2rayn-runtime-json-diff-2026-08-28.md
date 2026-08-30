# REPORT — V2RAYN XHTTP RUNTIME JSON DIFF

**Date:** 2026-08-28  
**Scope:** Local read-only comparison; no server, DNS, UFW, 3X-UI, or v2rayN profile mutations performed.  
**Raw evidence:** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-runtime-json-diff-raw-2026-08-28\`

---

## Verdict

**V2RAYN_RUNTIME_JSON_MATCH = FAIL**

The **captured live runtime** `C:\Program Files\v2rayN\binConfigs\config.json` does **not** load MCA-ONE PRIMARY xhttp at all. It loads a different active profile (`MCA-Gate-TLS-MCA-ONE` → `wsp-cloud.com:8443`, network `raw`).

When MCA-ONE PRIMARY fields from the profile DB are **emulated** using v2rayN 7.22.3 serialization rules, the resulting outbound **passes** end-to-end on bundled Xray 26.5.9 (egress `95.216.126.173`). Padding nested under `xhttpSettings.extra` is **not** the failure mechanism on this client/core pair.

**Operator symptom explained:** `curl.exe -x http://127.0.0.1:10808 https://api.ipify.org` → schannel TLS handshake failure is consistent with traffic being proxied through the **wrong outbound** (MCA-Gate raw/TLS to `wsp-cloud.com:8443`), not the MCA-ONE xhttp path the operator inspected in the profile editor.

---

## Working standalone config

| Item | Value |
|------|-------|
| **Absolute path** | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\xhttp-client-forensic-raw-2026-08-28\standalone-primary-corrected.json` |
| **Client core** | Xray **26.5.9** (`C:\Users\MetaCODE ONE\AppData\Local\v2rayN\bin\xray\xray.exe`) |
| **Result** | **PASS** — `api.ipify.org` → **95.216.126.173**; Google/YouTube PASS (prior forensic run) |

**Active proxy outbound (semantic):**

- protocol: `vless`
- address / port: `metacode-cloud.com` / `443`
- network: `xhttp`
- security: `tls`
- tls: `serverName=metacode-cloud.com`, `fingerprint=chrome`, `alpn=[h2, http/1.1]`, `allowInsecure=false`
- xhttp: `path=/x51a604f9239b1186`, `host=metacode-cloud.com`, `mode=auto`
- **padding:** `xhttpSettings.xPaddingBytes = "100-1000"` (**top-level**, not under `extra`)
- also present: `scMaxBufferedPosts=30`, `scMaxEachPostBytes="1000000"`, `scStreamUpServerSecs="20-80"`, `remark`

---

## Actual v2rayN runtime config

| Item | Value |
|------|-------|
| **Install / data root** | `C:\Program Files\v2rayN\` (not `%LocalAppData%\v2rayN\`) |
| **v2rayN version** | **7.22.3 x64** |
| **Runtime config path** | `C:\Program Files\v2rayN\binConfigs\config.json` |
| **Xray core** | **26.5.9** (same bundled binary as above) |
| **Active IndexId** | `4850651204958926275` → **MCA-Gate-TLS-MCA-ONE** (`guiNConfig.json`) |
| **MCA-ONE PRIMARY IndexId (stored, not active)** | `5337955619831611283` |

**Captured runtime proxy outbound (semantic):**

- address / port: **`wsp-cloud.com` / `8443`**
- network: **`raw`**
- security: `tls`
- tls: `serverName=wsp-cloud.com`, `fingerprint=chrome`, `alpn=[http/1.1]` only
- **no xhttpSettings**

**Note:** MCA-ONE PRIMARY profile exists in `guiConfigs\guiNDB.db` with correct GUI fields (xhttp, path, host, TLS, XHTTP Extra). That profile was **not** what Xray was running at capture time.

**Derived MCA-ONE outbound (v2rayN 7.22.3 serialization emulation, not captured runtime):**  
`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-runtime-json-diff-raw-2026-08-28\v2rayn-derived-mca-one-primary-proxy-outbound-v2.json`  
Local probe with this outbound: **PASS** → `95.216.126.173`.

---

## Exact semantic diff

| FIELD | STANDALONE WORKING | V2RAYN DERIVED (MCA-ONE, if active) | V2RAYN RUNTIME CAPTURED |
|-------|-------------------|-------------------------------------|-------------------------|
| address | metacode-cloud.com | metacode-cloud.com | **wsp-cloud.com** |
| port | 443 | 443 | **8443** |
| protocol | vless | vless | vless |
| network | xhttp | xhttp | **raw** |
| security | tls | tls | tls |
| tls.serverName | metacode-cloud.com | metacode-cloud.com | **wsp-cloud.com** |
| tls.alpn | h2, http/1.1 | h2, http/1.1 | **http/1.1 only** |
| tls.fingerprint | chrome | chrome | chrome |
| tls.allowInsecure | false | *(omitted by v2rayN)* | false |
| xhttp.path | /x51a604f9239b1186 | /x51a604f9239b1186 | **absent** |
| xhttp.host | metacode-cloud.com | metacode-cloud.com | **absent** |
| xhttp.mode | auto | auto | **absent** |
| xhttp.xPaddingBytes | **"100-1000" (top-level)** | **absent** | **absent** |
| xhttp.extra.mode | absent | auto | absent |
| xhttp.extra.xPaddingBytes | absent | **"100-1000"** | absent |
| xhttp.scMaxBufferedPosts | 30 | absent | absent |
| xhttp.scMaxEachPostBytes | 1000000 | absent | absent |
| xhttp.scStreamUpServerSecs | 20-80 | absent | absent |
| outbound tag | absent | proxy | proxy |
| mux | absent | disabled | disabled |

Machine-readable table: `semantic-diff-table.json` in raw evidence directory.

---

## xPadding structure

| Form | Structure | Local Xray 26.5.9 probe |
|------|-----------|-------------------------|
| **Working standalone** | `"xhttpSettings": { "xPaddingBytes": "100-1000", ... }` | **PASS** |
| **v2rayN GUI Extra field** | stored as `{"mode":"auto","xPaddingBytes":"100-1000"}` in profile DB | — |
| **v2rayN 7.22.3 serialization** | `"xhttpSettings": { "extra": { "mode": "auto", "xPaddingBytes": "100-1000" } }` | **PASS** (derived outbound probe) |
| **extra-only padding variant** | `"extra": { "xPaddingBytes": "100-1000" }` only | **PASS** |
| **top-level padding only** | `"xPaddingBytes": "100-1000"` without scMax* fields | **PASS** |

**Compatibility conclusion (empirical, client 26.5.9 / server 26.7.28):**

- Both **top-level** `xPaddingBytes` and **`extra.xPaddingBytes`** work against this server when MCA-ONE endpoint fields are correct.
- v2rayN nests GUI “XHTTP Extra” under `xhttpSettings.extra` per upstream `V2rayOutboundService.cs` — this is **not** inherently incompatible here.
- Optional `scMax*` fields in the standalone file are **not required** for success (padding-only variant passes).
- Xray 26.5.9 **rejects** `allowInsecure: true` (feature removed); `false` or omission is fine.

---

## Root cause

**Primary (runtime evidence):** v2rayN is running **MCA-Gate-TLS-MCA-ONE**, not **MCA-ONE-PRIMARY-443**. The operator opened the MCA-ONE profile editor, but `guiNConfig.json` IndexId and `binConfigs\config.json` prove a different profile is active on port 10808. That mismatch alone explains standalone PASS vs v2rayN FAIL without any server-side change.

**Secondary (structural, non-blocking if MCA-ONE were active):** Working standalone uses top-level `xPaddingBytes` plus optional scMax* tuning; v2rayN would emit `extra.xPaddingBytes` and omit scMax* fields. Local probes show these differences do **not** break connectivity for MCA-ONE on Xray 26.5.9.

**Not supported as primary cause:** Subscription parser dropping padding (profile DB already contains XhttpExtra with padding); xhttp `extra` nesting alone; missing scMax* fields; v2rayN/Xray version upgrade requirement (for this specific failure mode).

---

## Minimal fix

**Do not change server, DNS, UFW, or 3X-UI.**

1. **Activate MCA-ONE-PRIMARY-443** in v2rayN so runtime matches the profile the operator edited (IndexId must become `5337955619831611283`).
2. After activation, verify `C:\Program Files\v2rayN\binConfigs\config.json` proxy outbound shows:
   - `metacode-cloud.com:443`
   - `streamSettings.network = xhttp`
   - `xhttpSettings.path = /x51a604f9239b1186`
   - `xhttpSettings.extra.xPaddingBytes = "100-1000"` (or top-level equivalent)
3. Retest curl via `127.0.0.1:10808`.

**If still failing after confirmed active MCA-ONE runtime JSON:** use a **Custom Config** profile or manual JSON with the proven standalone structure (top-level `xPaddingBytes`, optional scMax* fields) — no upgrade required based on current evidence.

**Not recommended as first step:** Rewriting GUI Extra to a different JSON shape (current shape already passes when emulated); v2rayN upgrade; server mutation.

---

## Server mutation required

**NO** — failure is explained by wrong local active profile and/or inactive MCA-ONE runtime, not by proven server-side misconfiguration.

---

## WHAT OPERATOR DOES NEXT

**One manual step:** In v2rayN, **set MCA-ONE-PRIMARY-443 as the active server** (double-click / “Set as active”), confirm `guiNConfig.json` IndexId changes to `5337955619831611283`, then run:

```powershell
curl.exe -x http://127.0.0.1:10808 https://api.ipify.org
```

Expected after correct activation: response body **`95.216.126.173`**. If not, open `C:\Program Files\v2rayN\binConfigs\config.json` and confirm the proxy outbound is MCA-ONE xhttp before any other change.

---

## Evidence index (raw, local)

| Artifact | Purpose |
|----------|---------|
| `standalone-primary-working.json` | Copy of working standalone config |
| `standalone-proxy-outbound-extract.json` | Redacted proxy outbound extract |
| `v2rayn-runtime-config-captured.json` | Live `binConfigs\config.json` at capture |
| `v2rayn-runtime-proxy-outbound-extract.json` | Captured proxy outbound (MCA-Gate) |
| `v2rayn-derived-mca-one-primary-proxy-outbound-v2.json` | v2rayN-accurate MCA-ONE emulation |
| `profile-mca-one-primary-db.json` | Redacted DB profile (no secrets) |
| `semantic-diff-table.json` | Three-way field comparison |
| `local-probe-results-summary.json` | Xray 26.5.9 padding-structure probes |

**Git status:** report and raw pack are local evidence only; **no commit** per task charter.

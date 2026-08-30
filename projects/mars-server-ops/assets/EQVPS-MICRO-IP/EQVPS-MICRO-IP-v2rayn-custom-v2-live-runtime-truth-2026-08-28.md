# REPORT — CUSTOM V2 LIVE RUNTIME TRUTH

**Date:** 2026-08-28  
**Scope:** Local forensic only. No EQVPS / 3X-UI / Server A / DNS / UFW / SSH mutation. No v2rayN DB writes, no profile edits, no config replacement, no process restart, no Git commit.  
**Raw evidence (local, not in git):**  
`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-custom-v2-live-runtime-raw-2026-08-28\`

---

## Verdict

**CUSTOM_V2_NOT_DRIVING_RUNTIME — ACTIVE PROFILE IS CUSTOM V1**

Despite the operator statement that `MCA-ONE-PRIMARY-443-CUSTOM-v2` was active, authoritative runtime evidence shows:

| Authority | Value |
|-----------|--------|
| `guiNConfig.json` **IndexId** | `4790694801484889455` |
| DB remarks for that IndexId | **`MCA-ONE-PRIMARY-443-CUSTOM`** (Custom **v1**, ConfigType=2) |
| Custom v2 IndexId (exists, not selected) | `5080872077167210504` → file `0c2eb3b0-9031-423f-b44d-8f026269019b.json` |
| Live `binConfigs\config.json` | **Byte-identical** to Custom **v1** source / stored GUID copy |
| Live size / mtime | **1676 bytes**, LastWrite **2026-08-28 21:58:07 +07** |
| Prepared Custom v2 | **9936 bytes**, mtime **22:24:16 +07** — **not** loaded into `binConfigs` |

At capture time, explicit proxy via `127.0.0.1:10808` returns **EQVPS** `95.216.126.173` (PASS for the config that is actually running — Custom v1).

The earlier operator `curl` **schannel (35)** at activation and the prior **Goodline egress under claimed Custom v2** are **not reproduced** by this live Custom-v2 runtime, because **Custom v2 is not what Xray is running**.

---

## 10808 owner

| Field | Value |
|-------|--------|
| **Process** | `xray.exe` |
| **PID** | `17148` |
| **Parent** | `v2rayN.exe` PID `13044` |
| **Creation** | 2026-08-28 23:06:39 +07 |
| **Listen** | `127.0.0.1:10808` (State=Listen) |
| **Command line** | Not readable in this session (blank via CIM/WMIC; likely ACL) |
| **Config reference (file evidence)** | `C:\Program Files\v2rayN\binConfigs\config.json` (sole runtime config path used by v2rayN for core) |

No second Xray / sing-box owner of 10808 observed.

---

## Live config

| Field | Value |
|-------|--------|
| **Path** | `C:\Program Files\v2rayN\binConfigs\config.json` |
| **Timestamp** | 2026-08-28T21:58:07+07:00 |
| **SHA256** | `C9F39E180A9CE529D91774404A5C32C714C44ED6032575586F7E6F8601C9A778` |
| **Prepared Custom v2 SHA256** | `0E4BACA8012A11CC460325A9E11C4B72FBBF3F3ECE91262034609C611B3AB7AF` |
| **Byte-identical to Custom v2** | **NO** |
| **Semantic-identical to Custom v2** | **NO** |
| **Byte-identical to Custom v1** (`MCA-ONE-PRIMARY-443-custom.json` / `guiConfigs\705c9f3f-….json`) | **YES** |

Capture timestamp: **2026-08-28T23:07:34+07:00** (after operator “ACTIVE” notice).

---

## Active live proxy outbound

(From live `binConfigs\config.json` — UUID redacted in evidence copies)

| Field | Live value |
|-------|------------|
| **tag** | `proxy` |
| **protocol** | VLESS |
| **destination** | `metacode-cloud.com` |
| **port** | `443` |
| **transport** | `xhttp` |
| **TLS/SNI** | `tls` / SNI `metacode-cloud.com` / ALPN `h2,http/1.1` / fingerprint `chrome` |
| **XHTTP** | path `/x51a604f9239b1186`, host `metacode-cloud.com`, mode `auto` |
| **xPaddingBytes** | `100-1000` (top-level under `xhttpSettings`) |
| **scMax*** | `scMaxBufferedPosts=30`, `scMaxEachPostBytes=1000000`, `scStreamUpServerSecs=20-80` |

This outbound matches the known-good EQVPS standalone / Custom v1 / Custom v2 **proxy** leg. It is **not** VEESP (`wsp-cloud.com:8443` / `raw`).

---

## Live routing for api.ipify.org

| Field | Live (Custom v1 runtime) | Prepared Custom v2 (not loaded) |
|-------|--------------------------|----------------------------------|
| **domainStrategy** | `AsIs` | `AsIs` |
| **rules** | **[] (empty)** | 18 rules (VEESP clone) |
| **Matched rule** | none — Xray default = **first outbound** | catch-all `port 0-65535` → `proxy` |
| **Outbound tag** | `proxy` (only outbound) | `proxy` |
| **Expected egress** | EQVPS `95.216.126.173` | EQVPS `95.216.126.173` |

**Live observed egress:** `95.216.126.173` — matches expectation for the **actually loaded** Custom v1 config.

---

## Live tests

| Test | Result | Detail |
|------|--------|--------|
| `curl -x 127.0.0.1:10808 https://api.ipify.org` | **PASS** | `95.216.126.173` |
| `curl -I -x … https://www.google.com` | **PASS** | CONNECT 200 + HTTP 200 |
| `curl -I -x … https://www.youtube.com` | **PASS** | CONNECT 200 + HTTP 200 |
| `generate_204` via proxy | **FAIL/flaky** | schannel (35) once in this session (not used as primary verdict) |
| `curl` **without** proxy `api.ipify.org` | **direct** | `46.181.159.198` (operator Goodline/home path) |
| Operator curl at “ACTIVE” notice | **schannel (35)** | Not reproduced on forensic retest against same live Custom v1 config |

Xray access logs: **not available** (`LogEnabled=false`). guiLogs dominated by repeated **Wintun `pnputil /remove-device` failures** (TUN teardown noise), not per-request outbound tags.

---

## Prepared vs live differences

| Item | Prepared CUSTOM-v2 | Live `binConfigs` | Status |
|------|--------------------|-------------------|--------|
| File size | 9936 | 1676 | **DIFFERENT** |
| SHA256 | `0E4BAC…B7AF` | `C9F39E…A778` | **DIFFERENT** |
| Identity | Custom v2 JSON | **Custom v1 JSON** | **WRONG PROFILE LOADED** |
| Inbounds | mixed 10808 + **tun** + api 10812 | mixed 10808 **only** | DIFFERENT |
| Outbounds | proxy + direct + block + dns | **proxy only** | DIFFERENT |
| Routing rules | 18 | **0** | DIFFERENT |
| DNS object | present (incl. `wsp-cloud.com` DoH pin) | absent | DIFFERENT |
| Proxy outbound EQVPS XHTTP | yes | yes (same leg) | SAME intent |
| `metacode-cloud.com` | present | present | present |
| `wsp-cloud.com` | present (DNS pin only) | absent | — |
| `95.216.126.173` / `178.173.250.69` | absent in JSON | absent | — |
| Stored on disk under `guiConfigs` | `0c2eb3b0-….json` == prepared | not copied to `binConfigs` | **v2 imported, not activated** |

---

## Why explicit proxy returned Goodline

**For this capture wave: NOT APPLICABLE / NOT REPRODUCED.**

- Live `10808` → **EQVPS**, not Goodline.
- Goodline IP `46.181.159.198` appears only on **non-proxied** curl.

**For the operator’s earlier claimed Custom-v2 → Goodline symptom: NOT PROVEN in this wave**, because Custom v2 was **never** the live `IndexId` / `binConfigs` payload during forensic capture.

Evidence-based statement for the **current** failure-to-load question:

> v2rayN is **not** running `MCA-ONE-PRIMARY-443-CUSTOM-v2`. It is running **`MCA-ONE-PRIMARY-443-CUSTOM` (v1)**. Custom v2 exists as an imported GUID file but was not selected into `guiNConfig.IndexId` and was not copied into `binConfigs\config.json` at the 23:06 core restart.

Likely operator confusion vectors (names are adjacent in the server list):

- `MCA-ONE-PRIMARY-443-CUSTOM`
- `MCA-ONE-PRIMARY-443-CUSTOM-v2`

---

## Meaning of -1 ms

| Evidence | Interpretation |
|----------|----------------|
| `ProfileExItem` rows | Only **MCA-Gate-TLS-MCA-ONE** has Delay=`2`; **no** Delay row for either Custom profile |
| Custom ConfigType=2 | Full JSON; v2rayN RealPing/tcping against a single VLESS server field is often **N/A** |
| Conclusion | **-1 ms is consistent with “latency test unsupported / unset” for Custom entries**, not proof of core failure by itself |

Primary failure proof remains egress / handshake behavior — not the -1 ms UI field.

---

## Server mutation

**NO**

## v2rayN mutation

**NO** (read-only copy of `binConfigs`, `guiConfigs`, DB shadow copy, logs)

---

## Root cause classification

**C. OLD_OR_OTHER_CONFIG_IS_RUNNING**

(Also fits **D. CUSTOM_CONFIG_NOT_DRIVING_10808** if “custom” is read as Custom **v2** specifically: v2 is imported but not driving 10808.)

| Candidate | Result |
|-----------|--------|
| A. CUSTOM_V2_SOURCE_LOADED_EXACTLY | **NO** |
| B. CUSTOM_V2_SOURCE_LOADED_WITH_V2RAYN_TRANSFORMS | **NO** (v2 not loaded) |
| C. OLD_OR_OTHER_CONFIG_IS_RUNNING | **YES** — Custom **v1** |
| D. CUSTOM_CONFIG_NOT_DRIVING_10808 | **YES for v2** — 10808 driven by v1 |
| E. MULTIPLE_CORES_OR_PORT_OWNERSHIP_CONFLICT | **NO** |
| F. INDETERMINATE | **NO** for “what is running now” |

**Not claimed:** serializer defect for Custom v2 (v2 never reached live `binConfigs` in this capture).  
**Not claimed:** EQVPS server failure (live Custom v1 proxy → EQVPS PASS).

---

## NEXT ACTION

**Exactly one:** In v2rayN, select **`MCA-ONE-PRIMARY-443-CUSTOM-v2`** (not `…-CUSTOM`), then confirm activation by **either**:

1. `guiNConfig.json` `IndexId` becomes **`5080872077167210504`**, and  
2. `binConfigs\config.json` size jumps to **~9936** / hash matches prepared Custom v2,

**or** report the new `curl -x http://127.0.0.1:10808 https://api.ipify.org` result after that confirmed switch.

Do **not** edit JSON, do **not** delete profiles, do **not** change the server. Re-run this forensic capture only after IndexId proves Custom v2.

Stop.

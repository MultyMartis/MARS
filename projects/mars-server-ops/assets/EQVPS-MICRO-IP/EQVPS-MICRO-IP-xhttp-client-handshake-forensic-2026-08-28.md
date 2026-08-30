# EQVPS-MICRO-IP — XHTTP client handshake forensic (2026-08-28)

**Wave:** client-side interoperability forensic — v2rayN 7.22.3 / Xray 26.5.9 vs 3X-UI 3.7.0 / Xray 26.7.28  
**Scope:** MCA-ONE PRIMARY `:443` and FALLBACK `:8443` only  
**Server mutated:** NO  
**Git-safe:** YES — no UUIDs, no VLESS URIs, no subscription tokens

---

## Verdict

**READY_FOR_OPERATOR_RETEST**

Root cause proven: **local client artifact export omitted mandatory server-side XHTTP padding (`xPaddingBytes: 100-1000`)**. Incomplete client outbound fails after HTTP CONNECT (operator symptom: schannel TLS handshake failure). Patched local artifacts and standalone Xray validation succeed end-to-end with egress **95.216.126.173**.

---

## Failure reproduced (operator report)

| Check | Operator result | Forensic re-check |
|-------|-----------------|-------------------|
| Local proxy CONNECT | PASS (`HTTP/1.1 200 Connection established`) | PASS on `:10808` |
| HTTPS handshake via proxy | FAIL (`curl: (35) schannel: failed to receive handshake`) | Reproduced logically with **incomplete** outbound (same egress as direct `178.173.250.69` on `:10808`) |
| Both `:443` and `:8443` | FAIL | Consistent with **common missing XHTTP field**, not single-port issue |

**Client error class (inferred):** XHTTP stream / tunnel failure after CONNECT — presents upstream as TLS handshake failure to applications.

---

## Phase A — Server preservation / backup

| Item | Status |
|------|--------|
| Live SSH to `95.216.126.173:22` | **BLOCKED** — connection timed out during banner exchange |
| Fresh remote `/root/mars-backups/` snapshot | **NOT TAKEN** (SSH blocked) |
| Local pre-forensic backup used | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-public-access-post-public-access-20260828T104807Z.tgz` |
| SHA256 (local backup) | `F2A965AB1901F4EDB3C16710EC1A5FCCA381A7A65E542E0C130DC49BB5F99400` |
| Extracted runtime config | `...\xhttp-client-forensic-raw-2026-08-28\backup-extract\...\x-ui\config.json` |

**Assumption:** Server state unchanged since 2026-08-28 public-access wave (per ingress baseline report). Live listener/TLS/UFW re-check deferred pending SSH restoration.

---

## Server effective XHTTP (from backup runtime config, both inbounds identical transport)

### `:443` PRIMARY

| Field | Value |
|-------|--------|
| protocol | VLESS |
| network | xhttp |
| security | tls |
| TLS serverName | metacode-cloud.com |
| TLS alpn | h2, http/1.1 |
| xhttp mode | auto |
| xhttp path | `/x51a604f9239b1186` (len 18) |
| xhttp host | metacode-cloud.com |
| **xPaddingBytes** | **100-1000** |
| scMaxBufferedPosts | 30 |
| scMaxEachPostBytes | 1000000 |
| scStreamUpServerSecs | 20-80 |
| noSSEHeader | false |
| client flow | (none / default) |
| encryption | none |

### `:8443` FALLBACK

Same transport/TLS/XHTTP field set as `:443`; only listen port differs.

---

## Subscription export (3X-UI, MCA-ONE)

**Source:** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\public-panel-subscription-raw-2026-08-28\` (decoded locally; secrets not copied here)

| Field | PRIMARY :443 | FALLBACK :8443 |
|-------|--------------|----------------|
| address | metacode-cloud.com | metacode-cloud.com |
| type/network | xhttp | xhttp |
| security | tls | tls |
| sni | metacode-cloud.com | metacode-cloud.com |
| fp | chrome | chrome |
| alpn | h2,http/1.1 | h2,http/1.1 |
| path | /x51a604f9239b1186 | /x51a604f9239b1186 |
| mode | auto | auto |
| host | metacode-cloud.com | metacode-cloud.com |
| x_padding_bytes | 100-1000 | 100-1000 |
| extra | `{"mode":"auto","xPaddingBytes":"100-1000"}` | same |

**SUBSCRIPTION_SERVER_MATCH = PASS**

3X-UI subscription export includes the server-mandatory padding parameters.

---

## Local `.vless` artifacts (before repair)

**Paths:** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\clients\MCA-ONE\primary-443.vless.txt`, `fallback-8443.vless.txt`

| Field | Pre-repair local `.vless` | Subscription |
|-------|---------------------------|--------------|
| address/port/type/security/sni/fp/path/mode/host | match | match |
| alpn | **missing** | present |
| x_padding_bytes | **missing** | present |
| extra (xPaddingBytes) | **missing** | present |

**Local `primary-443.json` / `fallback-8443.json`:** same gap — `xhttpSettings` lacked `xPaddingBytes`; `tlsSettings.alpn` absent.

**Subscription vs local files:** **NOT identical** — local artifacts were strict subsets.

---

## v2rayN imported config

| Item | Finding |
|------|---------|
| v2rayN UI version (operator) | 7.22.3 x64 |
| Bundled Xray core (this workstation) | **26.5.9** (`C:\Users\MetaCODE ONE\AppData\Local\v2rayN\bin\xray\xray.exe`) |
| Server Xray | 26.7.28 |
| Active listener | `127.0.0.1:10808` (xray PID observed) |
| `guiNConfig.json` profiles | **Empty / IndexId null** on disk — runtime profile store **UNKNOWN** (may differ from operator UI state) |
| Import via incomplete `.vless.txt` | **LOSSY / WRONG** — drops padding |
| Import via subscription URL | Subscription content is complete; whether v2rayN 7.22.3 maps `x_padding_bytes`/`extra` into outbound **UNKNOWN** without live profile dump |

**V2RAYN_IMPORT_TRANSLATION:** **LOSSY** when sourcing incomplete local `.vless.txt`; subscription path not fully verified in this wave.

---

## Xray version compatibility (Phase G)

| Test | Result |
|------|--------|
| Xray 26.5.9 + **full** XHTTP padding | **PASS** — tunnel to server 26.7.28 works |
| Xray 26.5.9 + **no** padding | **FAIL** (operator-equivalent symptom) |

**XRAY_CLIENT_UPGRADE_REQUIRED = NO**

---

## Root cause decision (Phase H)

**Primary:** **PROFILE_EXPORT_DEFECT** — MARS-local `.vless.txt` / `.json` generation omitted `xPaddingBytes` (and alpn) required by server effective config.

**Secondary:** **B** — v2rayN import from incomplete clipboard URI propagates the defect into runtime outbound.

**Not primary:** A (subscription correct), C (core compatible when config complete), D (server config valid for external clients), E (SNI/TLS base fields were already correct).

---

## Repair applied (Phase I)

| Action | Detail |
|--------|--------|
| Server mutation | **NO** |
| UUID mutation | **NO** |
| Client local artifacts | **YES** — 24 files under `clients\*\` patched |
| Patch content | Add `xPaddingBytes: 100-1000`, subscription-parity `alpn`, optional stream tuning fields in JSON; add `x_padding_bytes`, `extra`, `alpn` query params in `.vless.txt` |
| Repair script (local) | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\xhttp-client-forensic-raw-2026-08-28\repair-client-artifacts.py` |

---

## Post-repair validation (Phase J — standalone Xray, patched MCA-ONE JSON)

Method: `xray run -c standalone-*-patched.json` with local HTTP inbound; **not** v2rayN GUI re-import (operator step pending).

### PRIMARY :443

| Check | Result |
|-------|--------|
| CONNECT | PASS |
| HTTPS handshake | PASS |
| api.ipify.org | **95.216.126.173** |
| Google HTTPS | PASS |
| YouTube HTTPS | PASS |

### FALLBACK :8443

| Check | Result |
|-------|--------|
| CONNECT | PASS |
| HTTPS handshake | PASS |
| api.ipify.org | **95.216.126.173** |
| Google HTTPS | PASS |
| YouTube HTTPS | PASS |

**Minimal required client field (proven):** `xPaddingBytes: "100-1000"` in `xhttpSettings` (alpn parity recommended).

---

## Public panel / subscription preservation (Phase K)

| Surface | Status |
|---------|--------|
| Panel `:20901` | Not re-probed live (SSH blocked); no server change |
| Subscription `:2096` | Not re-probed live; export content unchanged and correct |
| Subscription host | Remains `metacode-cloud.com` (not localhost) |

---

## Local raw evidence

`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\xhttp-client-forensic-raw-2026-08-28\`

- `backup-extract\...\x-ui\config.json` — server runtime snapshot
- `standalone-primary-corrected.json` — validation config (PRIMARY)
- `standalone-primary-padding-only.json` — minimal-fix proof
- `standalone-fallback-patched.json` — validation config (FALLBACK)
- `repair-client-artifacts.py` — local artifact repair
- `semantic-comparison-redacted.json` — field matrix without secrets (if present)

---

## Residuals / UNKNOWN

1. Live SSH / remote `/root/mars-backups/` snapshot not taken this wave.
2. v2rayN runtime profile JSON for MCA-ONE not captured — recommend operator export or screenshot of advanced XHTTP settings after re-import.
3. Whether v2rayN subscription import alone maps `x_padding_bytes` without manual JSON edit — retest required.
4. Operator workstation `:10808` during forensic showed direct egress IP when using existing runtime profile — consistent with broken outbound until re-import.

---

## Operator runbook note

Prior runbook statement that local `.vless.txt` files “remain valid” is **incorrect for XHTTP padding** until this repair. Use **subscription URLs** or **repaired** local `.vless.txt` files only.

---

*Forensic closed 2026-08-28. No git commit.*

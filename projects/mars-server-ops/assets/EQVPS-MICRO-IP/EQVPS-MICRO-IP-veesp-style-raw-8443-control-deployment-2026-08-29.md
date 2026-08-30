# REPORT — EQVPS VEESP-STYLE RAW/TLS 8443 CONTROL

**Wave date:** 2026-08-29  
**Host:** `metacode-cloud.com` / `95.216.126.173`  
**Programme:** `projects/mars-server-ops/`  
**Classification:** Git-safe — no secrets, no UUID, no VLESS URI

---

## Verdict

**READY_FOR_OPERATOR_RAW_8443_TEST**

Server-side mutation complete; TLS and isolated local client test passed. Operator v2rayN acceptance is **not** yet proven — do **not** call production PASS until operator steps below succeed.

Isolated local probe (separate from operator v2rayN): **RAW_8443_LOCAL_PASS**

---

## Why this architecture

- **Working VEESP reference:** `MCA-Gate-TLS-MCA-ONE` on `wsp-cloud.com:8443` — VLESS + TLS + RAW/tcp — confirmed working with operator TUN, routing, DNS, ChatGPT, YouTube, Google.
- **XHTTP branch deferred:** Prior XHTTP client acceptance on EQVPS (Custom v1/v2/v2.1, capture scripts) is **not** the production path for this wave. XHTTP troubleshooting stops here for the primary objective.
- **Minimal changed variables:** Only TCP/8443 repurposed from XHTTP fallback to RAW/TLS. Goodline direct TCP/8443 reachability was already proven. VEESP itself uses 8443. Same transport family as the control model.

---

## Pre-change EQVPS

| Surface | Pre-mutation state |
|---------|-------------------|
| **443** | VLESS + TLS + XHTTP primary (`EQVPS-TLS-XHTTP-PRIMARY-443`) — **unchanged** |
| **8443** | VLESS + TLS + XHTTP fallback — **superseded by this wave** |
| **20901** | 3X-UI panel (HTTPS) — unchanged |
| **2096** | Subscription endpoint — unchanged |
| **22** | SSH — unchanged |

Baseline confirmed read-only before mutation: `x-ui` active, Xray 26.7.28, LE cert valid for `metacode-cloud.com`, UFW allows 22/443/8443/20901/2096.

---

## Backup

| Item | Value |
|------|-------|
| **Remote tarball** | `/root/mars-backups/eqvps-pre-raw-8443-20260828T180336Z.tgz` |
| **Local copy** | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-pre-raw-8443-20260828T180336Z\eqvps-pre-raw-8443-20260828T180336Z.tgz` |
| **SHA256** | `58cde04dd0a29b51b328c6d6f04a8dae41c851bf419b53f358fe26ff4497aa45` |
| **Contents** | `x-ui.db`, generated Xray config snapshot, inbound definitions, cert path metadata, listener/UFW/service state |
| **Rollback readiness** | **YES** — restore tarball per `EQVPS-MICRO-IP-ingress-restore-runbook-v1.md`; target state = exact previous 8443 VLESS/TLS/XHTTP fallback |

Rollback procedure (summary):

1. Stop `x-ui`; restore backed-up DB/config from tarball.
2. Restart `x-ui`; confirm `:8443` inbound shows XHTTP again in panel/runtime.
3. Re-validate listeners 22/443/8443/20901/2096 and UFW unchanged.

---

## Goodline / port evidence (Phase D)

Prior waves already proved direct Goodline TCP reachability to `95.216.126.173:8443`:

| Source report | Result |
|---------------|--------|
| `EQVPS-MICRO-IP-controlled-reboot-direct-port-gate-2026-08-27.md` | **DIRECT_8443 = PASS** (TUN OFF, Goodline path) |
| `EQVPS-MICRO-IP-goodline-ingress-stabilization-2026-08-28.md` | TCP `:8443` **PASS**; XHTTP `:8443` client baseline **PASS** |

No new operator network preflight required for this wave.

---

## 8443 mutation

### Before

VLESS + TLS + **XHTTP** (fallback inbound, remark `EQVPS-TLS-XHTTP-FALLBACK-8443` or equivalent)

### After

VLESS + TLS + **RAW** (network `tcp`, remark `EQVPS-TLS-RAW-8443`)

Implementation: edited existing inbound id **2** in 3X-UI SQLite (`/etc/x-ui/x-ui.db`); transport changed from `xhttp` to `tcp`; TLS settings preserved (existing LE cert paths, SNI `metacode-cloud.com`, ALPN `http/1.1`, fingerprint `chrome`). One new revocable client identity added: **MCA-ONE-RAW-8443** (new UUID — secret stored locally only).

**Not changed:** 443 XHTTP primary, 443 clients, panel, subscription, UFW 8443 rule, certificate files, DNS, SSH hardening.

---

## Server validation

| Check | Result |
|-------|--------|
| **x-ui** | active |
| **Xray** | active (26.7.28); benign OCSP warnings only |
| **22** | listening |
| **443** | listening; runtime `xhttp` + `tls` (unchanged) |
| **8443** | listening; runtime `tcp` + `tls` |
| **20901** | listening (panel) |
| **2096** | listening (subscription) |
| **UFW** | 8443/tcp allowed (unchanged rule) |
| **Accidental new ports** | none observed |
| **Restart loop** | none |

DB/runtime alignment post-mutation:

- `:443` → `EQVPS-TLS-XHTTP-PRIMARY-443` / `xhttp` / `tls`
- `:8443` → `EQVPS-TLS-RAW-8443` / `tcp` / `tls`

---

## TLS validation

Validated on server via OpenSSL client handshake:

| Target | SNI | Result |
|--------|-----|--------|
| `127.0.0.1:8443` | `metacode-cloud.com` | verify return code **0 (ok)** |
| `metacode-cloud.com:8443` | `metacode-cloud.com` | verify return code **0 (ok)** |

Certificate: Let's Encrypt, CN/SAN `metacode-cloud.com`, valid through 2026-11-25.

Note: VLESS RAW socket does not return HTTP; TLS handshake success is the correct transport check.

---

## MCA-ONE RAW client

| Field | Value |
|-------|-------|
| **remark** | MCA-ONE-RAW-8443 |
| **address** | metacode-cloud.com |
| **port** | 8443 |
| **protocol** | VLESS |
| **network** | tcp (RAW) |
| **security** | tls |
| **SNI** | metacode-cloud.com |
| **ALPN** | http/1.1 |
| **fingerprint** | chrome |
| **encryption** | none |
| **flow** | (empty) |
| **mux** | disabled |
| **allowInsecure** | false (default) |

UUID and full VLESS URI: **local only** — not in this report.

Import type target: ordinary **VLESS** profile in v2rayN 7.22.3 — **not** Custom Config.

---

## VEESP vs EQVPS comparison

| FIELD | VEESP (control) | EQVPS RAW | MATCH / EXPECTED DIFFERENCE |
|-------|-----------------|-----------|----------------------------|
| Server domain | wsp-cloud.com | metacode-cloud.com | **EXPECTED DIFFERENCE** |
| Server IP | 178.173.250.69 | 95.216.126.173 | **EXPECTED DIFFERENCE** |
| Client UUID | (VEESP UUID) | (new EQVPS UUID) | **EXPECTED DIFFERENCE** |
| Port | 8443 | 8443 | **MATCH** |
| Protocol | VLESS | VLESS | **MATCH** |
| Security | TLS | TLS | **MATCH** |
| Transport | RAW / tcp | RAW / tcp | **MATCH** |
| SNI | wsp-cloud.com | metacode-cloud.com | **MATCH (own domain)** |
| ALPN | http/1.1 | http/1.1 | **MATCH** |
| Fingerprint | chrome | chrome | **MATCH** |
| Flow | (empty) | (empty) | **MATCH** |
| Mux | disabled | disabled | **MATCH** |
| allowInsecure | false | false | **MATCH** |

No other intentional semantic differences.

---

## Isolated local test

Performed **without** modifying operator v2rayN, TUN, or `:10808` binding.

| Item | Value |
|------|-------|
| **Xray binary** | `C:\Program Files\v2rayN\bin\xray\xray.exe` (26.7.28) |
| **Config** | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\raw-8443-control-raw-2026-08-29\isolated-xray-18088.json` |
| **Proxy port** | `127.0.0.1:18088` (HTTP inbound) |
| **api.ipify.org** | **95.216.126.173** — PASS |
| **Google HTTPS** | HTTP **200** — PASS |
| **YouTube HTTPS** | HTTP **200** — PASS |
| **Verdict** | **RAW_8443_LOCAL_PASS** |

Evidence: `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\raw-8443-control-raw-2026-08-29\isolated-test-results.txt`

---

## Client artifact

**Full absolute path (local, secret-bearing):**

`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\clients\MCA-ONE\raw-8443.vless.txt`

Companion JSON:

`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\clients\MCA-ONE\raw-8443.json`

Existing XHTTP artifacts **not overwritten:**

- `primary-443.vless.txt` / `.json`
- `fallback-8443.vless.txt` / `.json`

Classification note (local):

`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\raw-8443-control-raw-2026-08-29\classification-note.local.md`

---

## Server mutation

**YES** — exact scope: TCP/8443 inbound only (XHTTP → RAW/TLS) + one new test client **MCA-ONE-RAW-8443**

## VEESP mutation

**NO**

## v2rayN mutation

**NO** — no `guiNDB.db` edit, no auto-import, no profile switch

---

## XHTTP status

| Leg | Status |
|-----|--------|
| **443 XHTTP primary** | **Preserved** — research/future transport; not operator-accepted production path |
| **8443 XHTTP fallback** | **Superseded** on server by RAW/TLS this wave |
| **Client acceptance** | **XHTTP CLIENT ACCEPTANCE DEFERRED** |
| **Current primary test path** | **RAW/TLS VEESP-STYLE CONTROL PATH** |

Historical Custom v1/v2/v2.1 artifacts and capture scripts retained as forensic evidence — not deleted.

---

## Raw / local evidence bundle

`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\raw-8443-control-raw-2026-08-29\`

Includes: backup output, mutate/validate logs, remote wave script, isolated test config/results.

---

## Git

**NO COMMIT** — this report only; foreign WIP preserved unstaged.

---

## WHAT OPERATOR DOES NOW

1. Keep working VEESP active until ready (`MCA-Gate-TLS-MCA-ONE`).

2. Import the **normal VLESS link** from:

   `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\clients\MCA-ONE\raw-8443.vless.txt`

   using ordinary v2rayN VLESS import (paste link or scan QR if generated locally).

3. Confirm v2rayN shows:

   - **Type:** VLESS (**NOT** Custom)
   - **Address:** metacode-cloud.com
   - **Port:** 8443
   - **Transport:** tcp / raw equivalent
   - **TLS:** tls

4. Set active profile: **MCA-ONE-RAW-8443**

5. Test immediately in normal browser:

   - ChatGPT
   - YouTube
   - Google

6. Test `.ru` direct behavior (should remain unchanged vs VEESP routing).

7. Run:

   ```powershell
   curl.exe -sS -x http://127.0.0.1:10808 https://api.ipify.org
   ```

   **Expected explicit proxy result:** `95.216.126.173`

8. If anything fails: return immediately to **MCA-Gate-TLS-MCA-ONE** (VEESP). Do **not** fall back to Custom Config during this acceptance test.

9. Report exact results back (pass/fail per site + curl output).

---

## Acceptance criteria reminder

**Server-side (this wave):** met — backup, rollback, services, listeners, TLS, client artifact, isolated local PASS.

**Operator-side (pending):**

1. v2rayN imports as ordinary VLESS
2. No Custom type
3. Explicit proxy ipify → `95.216.126.173`
4. ChatGPT / YouTube / Google work
5. `.ru` direct unchanged
6. Browsing feels operationally comparable to VEESP

**Do not scale** to MCA-PHONE / Unit-* until MCA-ONE RAW/8443 passes operator acceptance.

---

*EQVPS VEESP-style RAW/TLS 8443 control deployment · 2026-08-29 · READY_FOR_OPERATOR_RAW_8443_TEST · no secrets in Git.*

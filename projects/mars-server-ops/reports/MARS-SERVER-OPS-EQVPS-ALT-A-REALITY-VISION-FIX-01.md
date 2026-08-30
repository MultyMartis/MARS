# REPORT — MARS Server Ops EQ-ALT-A FIX-01 — REALITY Client PublicKey Repair

**Test ID:** `EQ-ALT-A-REALITY-VISION`  
**Wave:** EQ-ALT-A FIX-01  
**Node:** EQVPS Micro-IP / Helsinki `95.216.126.173`  
**Date:** 2026-08-29  
**Classification of this document:** safe (no secrets)

---

## 1. Executive verdict

**FIX-01 VERDICT: CLIENT PROFILE HYGIENE REPAIRED — KEYPAIR VALID — ISOLATED TRANSPORT STILL FAIL (TIMEOUT)**

| Item | Result |
|------|--------|
| Root cause of v2rayN `PublicKey` reject | **Original local share URI used CRLF EOL**; query/`pbk` payload itself is cryptographically valid |
| Server REALITY keypair | **VALID** |
| Client `pbk` vs server-derived public key | **MATCH** (`pub_sha12=e83743293573`) |
| shortId | **VALID / MATCH** |
| SNI / serverName | **VALID** (`www.cloudflare.com`) |
| flow / fingerprint | **VALID** (`xtls-rprx-vision` / `chrome`) |
| Local Xray `run -test` with corrected profile material | **PASS** |
| Corrected local share artifact | **CREATED** (LF-only) |
| Isolated workstation Xray → `:9443` retest | **FAIL** (`timeout`) |
| EQVPS `:8443` regression | **PASS** (untouched) |
| Server `:9443` mutation this wave | **0** |

**Primary principle held:** do not blame the network for a profile v2rayN cannot accept. Key material is valid; original share file EOL hygiene was defective; transport timeout persists **after** key validity is proven.

---

## 2. Failure classification

| Layer | Classification |
|-------|----------------|
| v2rayN import / `PublicKey` message | **CLIENT PROFILE ARTIFACT / IMPORT HYGIENE** (not network) |
| REALITY key material | **VALID** (not MISMATCH, not MALFORMED) |
| EQVPS network / Goodline path | **NOT YET CLEARED** — isolated transport still times out with valid keys |
| Application acceptance (Cursor/ChatGPT/YouTube) | **OUT OF SCOPE** this wave |

**Do not classify the v2rayN message as:** EQVPS network FAIL, REALITY transport FAIL, Goodline path FAIL, or application FAIL.

---

## 3. Original profile audit

Inspected (local-only, not printed):

`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\eqvps-alt-a-reality-vision-2026-08-29\vless-share.uri.local`

| Check | Finding |
|-------|---------|
| Scheme / host / port | `vless` / `95.216.126.173` / `9443` |
| Param set | `encryption,flow,security,sni,fp,pbk,sid,spx,type,headerType` present |
| `pbk` length / charset | 43 / URL-safe Base64 alphabet — **STRUCTURALLY_OK** |
| `pbk` whitespace / CR in field / quotes | none |
| `sid` | 16 hex chars — OK |
| `sni` | `www.cloudflare.com` |
| `flow` / `fp` | `xtls-rprx-vision` / `chrome` |
| File EOL | **CRLF** (`…VISION\r\n`) |
| Payload vs corrected (CR stripped) | **IDENTICAL** |

**Sanitized original defect:** `CRLF_EOL` on share URI file (not `pbk` mismatch, not private/public swap, not missing `pbk`).

Original bytes preserved as:

`…\vless-share.uri.local.ORIGINAL-BYTES.bak`

---

## 4. Server REALITY keypair verification

Live read of EQVPS `:9443` inbound (no private key exposed):

| Field | Observed |
|-------|----------|
| port | 9443 |
| protocol | vless |
| network | tcp |
| security | reality |
| dest | `www.cloudflare.com:443` |
| serverNames | `["www.cloudflare.com"]` |
| privateKey | present (len 43) — **[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]** |
| shortIds | 2 entries; nonempty len 16 hex |
| client UUID | present — **[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]** |
| client flow | `xtls-rprx-vision` |
| Xray server | `26.7.28` |
| listeners | `:9443` and `:8443` present |

**Server config structural status:** OK — no server mutation performed.

---

## 5. PublicKey derivation/validation

Method: server Xray native `xray x25519 -i <privateKey>` on EQVPS (version-compatible with installed `26.7.28`).

| Check | Result |
|-------|--------|
| Derived public key length | 43 |
| Derived `pub_sha12` | `e83743293573` |
| Local client `pub_sha12` | `e83743293573` |
| Classification | **MATCH** |
| Local Xray Windows `26.7.28` `run -test` | **PASS** (URL-safe nopad only; std Base64 / padded variants **FAIL** as expected) |

**Private key never printed.**

---

## 6. ShortId validation

| Check | Result |
|-------|--------|
| Form | hexadecimal |
| Length | 16 (supported) |
| Client vs server nonempty shortId | **MATCH** |
| Whitespace / quotes | none |
| URI param name | `sid` (correct for current clients) |

---

## 7. SNI / serverName validation

| Check | Result |
|-------|--------|
| Intended target | `www.cloudflare.com` |
| Present in serverNames | yes |
| Client SNI matches exactly | yes |
| Accidental `metacode-cloud.com` as REALITY SNI | **no** |
| Scheme / port suffix / whitespace | none |
| dest compatibility | `www.cloudflare.com:443` |

---

## 8. Flow / fingerprint validation

| Field | Client value | Status |
|-------|--------------|--------|
| flow | `xtls-rprx-vision` | OK |
| fingerprint / `fp` | `chrome` | OK |
| URI param names | `flow`, `fp`, `pbk`, `sid`, `sni`, `security=reality`, `type=tcp` | aligned with v2rayN 7.22.3 / Xray 26.7.28 expectations |

---

## 9. Root cause of v2rayN PublicKey error

**Exact root cause (evidence-based):**

1. **Cryptographic PublicKey material was not wrong.** Server private→public derivation **MATCH**es the client `pbk` (`e83743293573`). Xray accepts it.
2. **Original local share artifact was not byte-clean for import:** file ended with **CRLF**. After stripping CR, payload equals the corrected LF-only twin (including canonical `spx=%2F`).
3. Therefore the operator-facing v2rayN message **`Свойство PublicKey недопустимо, проверьте его`** is classified as a **client import/profile presentation failure** against a CRLF-bearing share file / import path — **not** as a server key mismatch and **not** as network failure.

**Not found:** private/public swap, missing `pbk`, illegal charset in `pbk`, wrong SNI, wrong flow, wrong shortId vs server.

**Operator action required for final UI confirmation:** import the corrected LF-only file (below). Do not switch VPN yet; report whether v2rayN still shows the PublicKey error.

---

## 10. Corrected local profile artifact

| Artifact | Path |
|----------|------|
| Corrected share URI (LF-only) | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\eqvps-alt-a-reality-vision-2026-08-29\vless-share-fixed.uri.local` |
| Corrected profile JSON (local) | `…\v2rayn-profile-fixed.local.json` |
| Safe metadata | `…\client-profile-validation-safe.md` |
| Original preserved | `…\vless-share.uri.local` + `…\vless-share.uri.local.ORIGINAL-BYTES.bak` |

Display name remains: **`MCA-ONE-EQ-ALT-A-REALITY-VISION`**.

Full share URI / UUID / private key: **not** written into this report.

---

## 11. v2rayN import readiness

| Item | Status |
|------|--------|
| Structural readiness | **YES** — key MATCH, Xray `-test` PASS, LF-only share |
| Automated UI import in this wave | **not executed** (no Program Files ACL edits; no destructive profile replace) |
| Expected outcome | v2rayN **should** accept `vless-share-fixed.uri.local` |

**Operator instruction (exact):**

1. Import **only** `vless-share-fixed.uri.local` (not the CRLF original).
2. Confirm profile name `MCA-ONE-EQ-ALT-A-REALITY-VISION`.
3. **Do NOT** switch system VPN / TUN yet.
4. Report whether PublicKey error still appears.
5. Do not delete the failed/partial profile entry if present — leave for evidence.

---

## 12. Isolated Xray client retest

Listener: `127.0.0.1:18088` → EQVPS `:9443` REALITY+Vision (same validated key material).

| Check | Result |
|-------|--------|
| Xray client starts | **YES** |
| Local SOCKS accepts dials | **YES** (log shows accepted `api.ipify.org:443` / `www.cloudflare.com:443`) |
| `api.ipify` via proxy | **FAIL** — `curl (28) Connection timed out ~30s` |
| Expected egress `95.216.126.173` | **not observed** |
| Ordinary HTTPS via proxy | **FAIL** (timeout) |
| Classification | **FAIL** |
| Error class | **timeout** (not `invalid publicKey`) |

Evidence: `…\fix01-isolated-transport-retest.json`

**Interpretation:** with a proven-valid Reality client config, the workstation still cannot complete the REALITY path to `:9443` within timeout. This is **post-key-validation transport/path behaviour**, not a PublicKey parse failure.

---

## 13. Reinterpretation of previous `:9443` timeout

| Question | Answer |
|----------|--------|
| Classification | **STILL VALID** (as path/transport evidence) **after** key proof |
| Why not INVALIDATED | Prep workstation probe already used JSON from `client-secrets.local.json` (valid `pbk`), not the CRLF share URI. FIX-01 retest with the same valid key material still times out. |
| Why not “blame network first” earlier | Parallel v2rayN import failure had to be separated; URI CRLF hygiene could block UI acceptance even while Xray JSON keys were already correct. |
| Residual | Timeout still does **not** by itself prove DPI vs routing vs middlebox; it only shows isolated Xray path failure with valid keys. |

---

## 14. Existing `:8443` regression check

| Check | Result |
|-------|--------|
| Listening | **yes** |
| TLS subject | `CN = metacode-cloud.com` |
| Mutation this wave | **0** |

---

## 15. Evidence paths

| Path | Role |
|------|------|
| `projects/mars-server-ops/reports/MARS-SERVER-OPS-EQVPS-ALT-A-REALITY-VISION-PREP.md` | Prep baseline |
| `projects/mars-server-ops/tools/experiments/EQ-ALT-A-REALITY-VISION/audit-client-pubkey-safe.py` | Safe URI audit |
| `projects/mars-server-ops/tools/experiments/EQ-ALT-A-REALITY-VISION/verify-server-keypair-fix01.py` | Server derive/compare |
| `projects/mars-server-ops/tools/experiments/EQ-ALT-A-REALITY-VISION/fix01-isolated-retest.py` | Isolated retest |
| `local/…/eqvps-alt-a-reality-vision-2026-08-29/vless-share-fixed.uri.local` | Corrected share |
| `local/…/client-profile-validation-safe.md` | Safe meta |
| `local/…/fix01-isolated-transport-retest.json` | Retest result |
| `local/…/keypair-verify-safe.json` | Match receipt (safe) |

---

## 16. Git / server / client mutation closeout

| Item | Status |
|------|--------|
| VEESP mutation | **0** |
| EQVPS `:8443` mutation | **0** |
| EQVPS `:9443` server mutation | **0** |
| Client configuration mutation | **0** except creation of corrected **local-only** artifacts under `eqvps-alt-a-reality-vision-2026-08-29\` |
| Secret disclosure in report/chat | **0** |
| commit | **0** |
| push | **0** |
| Foreign WIP | untouched / out of scope |

**STOP** — await operator v2rayN import confirmation of `vless-share-fixed.uri.local`. Do not jump to WireGuard; do not redesign REALITY; do not rotate server keys in this wave.

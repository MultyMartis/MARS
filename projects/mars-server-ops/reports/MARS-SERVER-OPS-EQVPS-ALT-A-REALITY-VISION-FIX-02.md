# REPORT — MARS Server Ops EQ-ALT-A FIX-02 — v2rayN Generated Config Forensics

**Test ID:** `EQ-ALT-A-REALITY-VISION`  
**Wave:** EQ-ALT-A FIX-02  
**Node:** EQVPS Micro-IP / Helsinki `95.216.126.173`  
**Date:** 2026-08-29  
**Classification of this document:** safe (no secrets)

---

## 1. Executive verdict

**FIX-02 VERDICT: PUBLICKEY FAILS AT V2RAYN IMPORT→STORAGE MAPPING — URI `pbk` VALID — DIRECT XRAY STARTUP PASS — TRANSPORT STILL TIMEOUT**

| Item | Result |
|------|--------|
| Exact layer where PublicKey first becomes invalid | **C → B:** v2rayN URI import / profile storage mapping (before clean runtime JSON) |
| Fixed URI `pbk` | **VALID** (`sha12_of_string=e83743293573`, decoded_len=32, base64url OK, LF-only) |
| v2rayN stored PublicKey | **MISMATCH** — expected `pbk` **absent** from DB; freelist shows PublicKey slot = **shortId hex16** `4fbd0c29e602e688` |
| Generated Xray runtime PublicKey (failed activation) | **Would be invalid** (same shortId-as-key); live `binConfigs/config.json` at forensics time was unrelated TLS profile |
| Xray 26.7.28 schema | JSON field `realitySettings.publicKey` (url-safe base64, 32 bytes); core errors name it **`password`** |
| Direct Xray client startup | **PASS** (`Configuration OK`) |
| Direct Xray isolated transport | **TIMEOUT** (config accepted; network path not cleared) |
| v2rayN conversion/import at fault | **YES** (URI import path) |
| Corrected client path | Manual v2rayN profile `MCA-ONE-EQ-ALT-A-REALITY-VISION-FIX02` + direct JSON |
| EQVPS `:8443` regression | **PASS** (TCP+TLS `CN=metacode-cloud.com`) |
| Server `:9443` mutation | **0** |

**Primary principle held:** PublicKey bytes were traced from server-derived expectation through URI → v2rayN DB freelist → Xray reject semantics. Network timeout is only meaningful **after** Xray accepts the config (direct path).

---

## 2. Reproduced failure

| Field | Value |
|------|--------|
| Source | `C:\Program Files\v2rayN\guiLogs\2026-08-29.txt` |
| Timestamps | `2026-08-29 19:24:45`, `19:48:28`, `19:48:32`, `19:48:43` (+07) |
| Sanitized line | `EQVPS-ALT-A-REALITY-VISION-MCA-ONE-EQ-ALT-A-REALITY-VISION: Свойство PublicKey недопустимо, проверьте его` |
| Log level | `INFO` (v2rayN UI/log wrapper) |
| Emitter | **Both layers:** Xray core fails REALITY build (`invalid "password": <value>`); v2rayN localizes/surfaces as PublicKey message |

Reproduced Xray-native equivalent with PublicKey=`4fbd0c29e602e688` (shortId):

`infra/conf: Failed to build REALITY config. > infra/conf: invalid "password": 4fbd0c29e602e688` (exit 23)

---

## 3. Config pipeline traced

```
SOURCE URI (fixed, LF)     → pbk VALID (sha12 e83743293573)
        ↓
IMPORTED v2rayN PROFILE    → FIRST MISMATCH (pbk not stored; PublicKey←sid)
        ↓
GENERATED Xray CONFIG      → inherits invalid PublicKey / fails start
        ↓
Xray STARTUP               → rejects REALITY (password/PublicKey invalid)
```

**WHERE does the first mismatch appear?**  
Between **source URI** and **v2rayN ProfileItem storage** (import/mapping). Not in URI crypto material; not in Xray 26.7.28 schema for a correct `publicKey`.

---

## 4. Fixed URI validation

Artifact: `…\eqvps-alt-a-reality-vision-2026-08-29\vless-share-fixed.uri.local`

| Check | Result |
|------|--------|
| UTF-8 BOM | none |
| EOL | LF-only (no CR) |
| Logical URI | one share line (+ trailing LF) |
| `pbk` present / duplicate | present ×1 |
| `pbk` CRLF / quotes / spaces / ZW | none |
| Alphabet | url-safe base64 (`A-Za-z0-9_-`) |
| strlen | 43 |
| decode | OK, **decoded_len=32** |
| round-trip base64url | equal |
| `sha12_of_string` | `e83743293573` (same method as FIX-01) |
| `sni` / `fp` / `flow` / `sid` | `www.cloudflare.com` / `chrome` / `xtls-rprx-vision` / hex16 OK |

---

## 5. v2rayN stored profile validation

| Item | Finding |
|------|---------|
| Storage | `C:\Program Files\v2rayN\guiConfigs\guiNDB.db` → table `ProfileItem` |
| Active rows at forensics | 3 TLS profiles only (Gate / `:8443` / `:24443`) — REALITY row **not active** |
| Residual evidence | SQLite freelist still contains deleted/temp row for remarks `EQVPS-ALT-A-REALITY-VISION-MCA-ONE-EQ-ALT-A-REALITY-VISION` |
| Subid | `TempRemoveSubId` (temp import path) |
| Expected `pbk` bytes in DB | **FALSE** (`pbk_in_db=false`) |
| Freelist PublicKey slot | `4fbd0c29e602e688` (= URI **sid**, not pbk) |
| Freelist ShortId slot | `/` (= spiderX) |
| Fingerprint `chrome` near row | **missing** |
| Flow | present in `ProtoExtra` as `xtls-rprx-vision` |
| Network stored | `raw` (v2rayN normalization of tcp) |
| StreamSecurity | `reality` |

**Conclusion:** import did **not** preserve `pbk`/`fp`; REALITY fields shifted so **shortId occupied PublicKey**.

Program Files ACL blocks agent DB insert (Users RX); live profile repair must be **operator UI manual** (see §14).

---

## 6. Generated Xray config validation

| Item | Finding |
|------|---------|
| Path | `C:\Program Files\v2rayN\binConfigs\config.json` |
| At forensics time | Active outbound = `wsp-cloud.com:8443` TLS (not REALITY) — after failed REALITY starts, UI remained on other profile |
| `publicKey` occurrences | 0 in that snapshot |
| Failed-start semantics | Simulated config with PublicKey=sid → Xray reject (above) |

No clean REALITY runtime JSON was left on disk from the failed activations; failure occurs at config build/start before a healthy REALITY outbound persists.

---

## 7. Xray 26.7.28 REALITY schema verification

Binary: `C:\Program Files\v2rayN\bin\xray\xray.exe` → **Xray 26.7.28** (`5ca6f4b`, windows/amd64).

| Expectation | Verified |
|-------------|----------|
| Client JSON path | `outbounds[].streamSettings.realitySettings` |
| Public key field name | **`publicKey`** |
| Core error alias | **`password`** (`invalid "password"` / `empty "password"`) |
| Encoding | URL-safe base64 **without** std padding |
| Decoded length | **32** bytes (X25519) |
| Std base64 / padded | **REJECT** |
| Quoted literal key | **REJECT** |
| Trailing CR alone in JSON string | still `Configuration OK` in `-test` (EOL-on-key alone ≠ this failure) |
| Empty / missing `publicKey` | **REJECT** (`empty "password"`) |

---

## 8. PublicKey byte-level validation

| Source | strlen | decoded_len | sha12_of_string | Notes |
|--------|--------|-------------|-----------------|-------|
| Server-derived / secrets `publicKey` | 43 | 32 | `e83743293573` | MATCH (FIX-01 retained) |
| Fixed URI `pbk` | 43 | 32 | `e83743293573` | MATCH + round-trip OK |
| v2rayN freelist PublicKey | 16 | n/a (hex, not pbk) | n/a | **MISMATCH** (is sid) |
| Direct test JSON | 43 | 32 | `e83743293573` | Xray `-test` PASS |

No manual byte “repair”; no private/public swap.

---

## 9. Four-representation comparison table

| # | Representation | strlen | decoded_len | hash fragment | encoding | vs expected |
|---|----------------|--------|-------------|---------------|----------|-------------|
| 1 | server-derived / secrets | 43 | 32 | `e83743293573` | base64url | baseline |
| 2 | fixed URI `pbk` | 43 | 32 | `e83743293573` | base64url | **MATCH** |
| 3 | v2rayN stored PublicKey | 16 | — | sid hex | hex shortId | **MISMATCH** |
| 4 | generated runtime (failed path) | 16 (inferred) | — | same sid | invalid as pk | **MISMATCH** |
| 4b | direct manual Xray JSON | 43 | 32 | `e83743293573` | base64url | **MATCH** |

---

## 10. UTF/BOM/EOL findings

| Artifact | BOM | CR | LF | Hidden Unicode in pbk |
|----------|-----|----|----|------------------------|
| `vless-share-fixed.uri.local` | no | no | yes | no |
| Freelist profile residual | n/a | n/a | n/a | pbk absent |
| Direct Xray JSON | no | present in pretty JSON whitespace only | yes | key clean |

FIX-01 CRLF-on-file remains a hygiene defect of the **original** share file, but is **not** sufficient as the sole root cause of the post-import PublicKey failure (LF-fixed import still left sid-in-PublicKey evidence).

---

## 11. v2rayN REALITY field mapping

| URI param | Expected ProfileItem / JSON | Observed on failed import residual |
|-----------|-----------------------------|-------------------------------------|
| `pbk` | `PublicKey` / `realitySettings.publicKey` | **not stored**; slot held **sid** |
| `sid` | `ShortId` | displaced (slot held `/`) |
| `spx` | `SpiderX` | displaced |
| `fp` | `Fingerprint` | **missing** (`chrome` absent) |
| `sni` | `Sni` / `serverName` | OK (`www.cloudflare.com`) |
| `flow` | `Flow` / users.flow | in ProtoExtra OK |
| `type=tcp` | Network | stored as `raw` (normal for v2rayN 7.x) |

**Do not call “generic v2rayN bug” beyond this evidence:** URI-import path for this REALITY share produced a field mis-map; direct Xray with correct JSON works.

---

## 12. Direct Xray client control

| Item | Result |
|------|--------|
| Config | `…\fix02-direct-xray-client.local.json` |
| Listener | `127.0.0.1:18088` SOCKS |
| `xray run -test` | **Configuration OK** |
| Process start + listen | **YES** |
| CASE | **A** — direct Xray accepts expected PublicKey ⇒ v2rayN import/generation path is leading client fault |

---

## 13. Root cause classification

| Layer | Classification |
|-------|----------------|
| A. Source URI artifact | **NOT ROOT** (valid after FIX-01 LF fix) |
| B. v2rayN imported profile storage | **PRIMARY FAULT** — PublicKey←shortId; pbk absent |
| C. v2rayN conversion/generation | **CONSEQUENTIAL** — would emit invalid `publicKey` |
| D. Generated Xray runtime JSON | Invalid when driven by B |
| E. Xray parser | **BEHAVING CORRECTLY** (rejects non-32-byte key) |
| F. Wrong schema assumption | **FALSE** — `publicKey` + url-safe 32-byte is correct |

Operator-facing Russian PublicKey message = **localized wrap of Xray `invalid "password"`**, not a separate crypto mismatch vs server.

---

## 14. Corrected client path

| Artifact | Path |
|----------|------|
| Manual checklist | `…\fix02-operator-manual-profile-checklist.md` |
| FIX02 share URI (LF; optional — **prefer manual**) | `…\vless-share-fix02.uri.local` |
| FIX02 profile field JSON | `…\v2rayn-profile-fix02.local.json` |
| Direct Xray client JSON | `…\fix02-direct-xray-client.local.json` |
| Safe forensics JSON | `…\fix02-forensics-safe.json` |

**Preferred activation:** create **new** v2rayN profile `MCA-ONE-EQ-ALT-A-REALITY-VISION-FIX02` via **manual fields** (not VLESS URI import).  
Verify PublicKey sha12 = `e83743293573` before enabling TUN.

Agent could not insert into live `guiNDB.db` (Program Files ACL RX for Users; no ACL mutation authorized).

---

## 15. Import/start validation

| Gate | Status |
|------|--------|
| Gate 1 — v2rayN import/store of URI path | **FAIL historically** (pbk not stored) |
| Gate 1 — manual FIX02 profile | **PENDING OPERATOR** (ACL blocked agent write) |
| Gate 2 — Xray start without PublicKey error | **PASS** for direct JSON; **PENDING** for repaired v2rayN profile |

---

## 16. Isolated transport result

| Check | Result |
|------|--------|
| Direct Xray starts / SOCKS listen | **YES** |
| `api.ipify` via SOCKS | **TIMEOUT** (curl exit 28, ~30s) |
| `cloudflare` via SOCKS | **TIMEOUT** |
| Expected egress `95.216.126.173` | **NOT OBSERVED** (no successful body) |
| Classification | **Valid network/transport evidence** *only for config-accepted client*; not a PublicKey problem |

`:9443` TCP connect from workstation = True (port reachable; REALITY/Vision path still times out).

---

## 17. Reclassification of FIX-01

| FIX-01 claim | FIX-02 status |
|--------------|---------------|
| “CRLF was the root cause” | **SUPERSEDED / INCOMPLETE** — hygiene issue only; LF import still produced invalid stored PublicKey |
| server keypair VALID/MATCH | **RETAINED** (`e83743293573`) |
| “v2rayN import should succeed” | **FALSE for Gate 2** — import≠runtime; storage mis-map |
| isolated timeout still valid | **RETAINED / STRENGTHENED** — timeout after **direct** Xray accepts PublicKey |
| Local Xray `-test` PASS with valid material | **RETAINED** |

---

## 18. Existing EQVPS `:8443` regression check

| Check | Result |
|------|--------|
| TCP `:8443` | True |
| TLS subject | `CN=metacode-cloud.com` |
| Mutation this wave | **0** |

---

## 19. Evidence paths

| Path | Role |
|------|------|
| `projects/mars-server-ops/reports/MARS-SERVER-OPS-EQVPS-ALT-A-REALITY-VISION-FIX-02.md` | This report |
| `projects/mars-server-ops/evidence/EQVPS-TRANSPORT-ALTERNATIVES-WAVE-01/EQ-ALT-A_2026-08-29_FIX02/` | Safe evidence copy |
| `local/…/eqvps-alt-a-reality-vision-2026-08-29/fix02-*` | Local forensics + direct client artifacts |
| `C:\Program Files\v2rayN\guiLogs\2026-08-29.txt` | Reproduced PublicKey lines |
| `C:\Program Files\v2rayN\guiConfigs\guiNDB.db` | Profile storage (+ freelist residual) |

---

## 20. Git/server/client mutation closeout

| Item | Value |
|------|--------|
| VEESP mutation | **0** |
| EQVPS `:8443` mutation | **0** |
| EQVPS `:9443` mutation | **0** |
| Client mutation | scoped local test/repaired artifacts + evidence copy only; no Program Files ACL change; no live DB insert |
| Secret disclosure | **0** |
| commit / push | **0** |
| Foreign WIP | present elsewhere — **out of scope** |

**STOP** — operator should create `MCA-ONE-EQ-ALT-A-REALITY-VISION-FIX02` manually and confirm Gate 2 (no PublicKey error) before TUN/app acceptance. Do not rotate server REALITY keys. Do not treat remaining timeout as PublicKey failure.

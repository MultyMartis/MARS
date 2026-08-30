# REPORT — V2RAYN CUSTOM CONFIG CONTROL TEST

**Date:** 2026-08-28  
**Scope:** Local-only control test; no EQVPS / 3X-UI / DNS / UFW / SSH / Server A / AdminVPS mutations. No v2rayN or Xray upgrades. No production UUID or server-side XHTTP changes. No git commit.

**Raw evidence (local, not in git):**  
`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-custom-config-control-raw-2026-08-28\`

**Custom config (local, not in git):**  
`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-custom-config\MCA-ONE-PRIMARY-443-custom.json`

---

## Verdict

**READY_FOR_OPERATOR_CUSTOM_CONFIG_TEST**

Custom JSON prepared and validated on the same Xray **26.5.9** binary v2rayN uses. End-to-end proxy tests **PASS** on `127.0.0.1:10808` when the JSON is loaded **without** v2rayN VLESS GUI serialization.

Automatic v2rayN GUI activation was **not** performed: writing `C:\Program Files\v2rayN\binConfigs\config.json` was **Access denied**, and programmatic `guiNDB.db` edits were avoided to preserve existing profiles.

---

## Known-good source

| Item | Value |
|------|-------|
| **Absolute path** | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\xhttp-client-forensic-raw-2026-08-28\standalone-primary-corrected.json` |
| **Source file modified** | **NO** (read-only; working copy in raw evidence dir) |
| **Prior standalone result** | **PASS** — `api.ipify.org` → **95.216.126.173**; Google HTTPS **PASS**; YouTube HTTPS **PASS** (forensic wave 2026-08-28) |

---

## v2rayN Custom Config support

| Item | Value |
|------|-------|
| **Installed version** | **v2rayN 7.22.3 x64** (`ProductVersion 7.22.3+ccb0ffb3b6e15757a87ee1acd64a87fc5b9e8137`) |
| **Xray core** | **26.5.9** — `C:\Users\MetaCODE ONE\AppData\Local\v2rayN\bin\xray\xray.exe` |
| **ConfigType** | `EConfigType.Custom = 2` |
| **Upstream mechanism** | `CoreConfigHandler.GenerateClientCustomConfig` → **`File.Copy`** stored custom JSON to runtime `binConfigs\config.json` — **no VLESS/XHTTP GUI re-serialization** |
| **GUI entry** | **Servers → Add Custom Configuration** (`AddCustomServer` copies file into v2rayN config dir with GUID filename) |
| **This wave** | **Manual** import/activation required; **automatic** profile DB / `binConfigs` mutation **not** attempted |

**TUN note:** Current `guiNConfig.json` has **`EnableTun: true`**. Custom full JSON replaces runtime config when selected; for curl-only validation on `10808`, TUN does not need to be disabled. If TUN + Custom misbehaves in GUI, disable TUN temporarily for this control test only.

---

## Custom config

| Item | Value |
|------|-------|
| **Absolute path** | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-custom-config\MCA-ONE-PRIMARY-443-custom.json` |
| **Suggested display name** | `MCA-ONE-PRIMARY-443-CUSTOM` |
| **XHTTP structure preserved** | **YES** — outbound byte-identical to known-good standalone except optional outbound `tag: proxy` |
| **Allowed adaptation only** | Inbound: `127.0.0.1:10818` / `http` → `127.0.0.1:10808` / `mixed` (v2rayN standard local proxy port for curl) |

**Preserved outbound (semantic):**

- address: `metacode-cloud.com`
- port: `443`
- network: `xhttp`
- security: `tls`
- TLS: SNI `metacode-cloud.com`, ALPN `[h2, http/1.1]`, fingerprint `chrome`, `allowInsecure: false`
- XHTTP: path `/x51a604f9239b1186`, host `metacode-cloud.com`, mode `auto`
- **`xPaddingBytes`: `"100-1000"` (top-level under `xhttpSettings`, not under `extra`)**
- `scMaxBufferedPosts: 30`, `scMaxEachPostBytes: "1000000"`, `scStreamUpServerSecs: "20-80"`, `remark`

UUID and secrets are **not** reproduced in this git-safe document.

---

## Runtime proof

**Method:** Direct Xray **26.5.9** run with `-c` pointing at custom JSON (equivalent payload v2rayN Custom Config would copy verbatim). Evidence: `runtime-proof-direct-20260828-215934.txt`, `curl-results-direct2-20260828-215934.txt`.

| Field | Observed |
|-------|----------|
| address | metacode-cloud.com |
| port | 443 |
| network | xhttp |
| security | tls |
| XHTTP path | /x51a604f9239b1186 |
| XHTTP host | metacode-cloud.com |
| XHTTP mode | auto |
| xPaddingBytes | **100-1000 (top-level in xhttpSettings)** |
| scMaxBufferedPosts | 30 |
| scMaxEachPostBytes | 1000000 |
| scStreamUpServerSecs | 20-80 |
| TLS SNI | metacode-cloud.com |
| TLS ALPN | h2, http/1.1 |
| TLS fingerprint | chrome |

**Not captured:** live `binConfigs\config.json` after v2rayN GUI Custom activation (Program Files write denied in this session).

---

## Validation

| Test | Result | Detail |
|------|--------|--------|
| **api.ipify** | **PASS** | `95.216.126.173` |
| **Google** | **PASS** | `HTTP/1.1 200 Connection established` |
| **YouTube** | **PASS** | `HTTP/1.1 200 Connection established` |
| **Egress IP** | **PASS** | Matches EQVPS MCA-ONE PRIMARY |

**Post-test state:** Test Xray process stopped. **v2rayN.exe** still running; **no xray child** at end of wave (operator should re-select any profile or restart v2rayN to restore proxy).

---

## Root cause classification

| Layer | Status |
|-------|--------|
| **Server (MCA-ONE PRIMARY/FALLBACK)** | **PASS** |
| **Xray 26.5.9 client core** | **PASS** |
| **XHTTP transport + known-good JSON** | **PASS** |
| **3X-UI server config** | **PASS** (unchanged; no server mutation) |
| **v2rayN Custom Config path (no serializer)** | **PASS** (this wave, direct equivalent) |
| **v2rayN standard GUI profile runtime** | **FAIL** (operator-reported schannel handshake; prior wave captured **MCA-Gate** active instead of MCA-ONE) |

**Classification:**

- **V2RAYN_STANDARD_PROFILE_SERIALIZATION_DEFECT = LIKELY** once operator confirms Custom Config **PASS** through v2rayN GUI while **MCA-ONE-PRIMARY-443** standard profile still **FAIL** when explicitly activated.
- **Alternate explanation (prior runtime-json-diff wave):** wrong active profile (**MCA-Gate-TLS-MCA-ONE** on `wsp-cloud.com:8443` / `raw`) explains curl failure without server or serializer change — operator must verify **IndexId / active highlight** matches MCA-ONE before blaming serializer.

**Not applicable this wave:** `CUSTOM_CONFIG_RUNTIME_DIFFERENCE_REQUIRED` (custom path did not fail).

---

## Server mutation

**NO**

---

## Existing profiles preservation

| Profile | Status |
|---------|--------|
| MCA-Gate-TLS-MCA-ONE | **Preserved** — not deleted |
| MCA-ONE-PRIMARY-443 | **Preserved** — not deleted |
| guiNDB.db | **Not modified** |
| New Custom entry | **Not added automatically** — operator adds manually |

---

## WHAT OPERATOR DOES NOW

1. In v2rayN **7.22.3**, open **Servers → Add Custom Configuration** (or **Import custom config from file**).
2. Select:  
   `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\v2rayn-custom-config\MCA-ONE-PRIMARY-443-custom.json`
3. Set remarks to **`MCA-ONE-PRIMARY-443-CUSTOM`**. Save. **Do not delete** existing profiles.
4. **Activate only** `MCA-ONE-PRIMARY-443-CUSTOM` (not MCA-Gate, not standard MCA-ONE until compared).
5. Optional: temporarily disable **TUN** if Custom + TUN interferes; curl test uses port **10808** only.
6. Verify runtime (optional): confirm `C:\Program Files\v2rayN\binConfigs\config.json` outbound shows **xhttp** to **metacode-cloud.com:443** with top-level **`xPaddingBytes`** — not `wsp-cloud.com` / `raw`.
7. Run control curl:

```powershell
curl.exe -sS -x http://127.0.0.1:10808 https://api.ipify.org
```

Expected: `95.216.126.173`

8. If Custom **PASS** and standard **MCA-ONE-PRIMARY-443** still **FAIL** when activated: treat **V2RAYN_STANDARD_PROFILE_SERIALIZATION_DEFECT** as **CONFIRMED**; do not change server.
9. Perform normal browser browsing test with Custom profile active.

**If v2rayN proxy is down after this wave:** re-select any server profile or restart v2rayN (test stopped the xray child process).

---

## Related prior evidence

- `EQVPS-MICRO-IP-v2rayn-runtime-json-diff-2026-08-28.md` — captured runtime was MCA-Gate, not MCA-ONE.
- `EQVPS-MICRO-IP-xhttp-client-handshake-forensic-2026-08-28.md` — standalone PRIMARY/FALLBACK PASS.

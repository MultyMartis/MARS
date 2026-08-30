# REPORT — MARS Server Ops FriendHosting Control Node Build 01 — PREP

**Date (UTC context):** 2026-08-29 / 2026-08-30 local  
**Wave:** FRIENDHOSTING-CONTROL-NODE-BUILD-01  
**Verdict:** **PREP_READY_FOR_OPERATOR_ACCEPTANCE**  
**Scope stop:** real-app acceptance NOT executed by agent (operator harness next)

---

## 1. Executive preparation verdict

FriendHosting Germany control node is prepared as a third independent VLESS+TLS+RAW/TCP `:8443` endpoint for controlled comparison against VEESP `:8443` and EQVPS `:8443`.

Server stack, TLS certificate, inbound, server-side validation, and isolated workstation transport all **PASS**. Offline acceptance harness is ready. Operator must import the local-only profile and run the harness; agent stops before VPN switch / real-app acceptance.

---

## 2. Node identity

| Field | Value |
|-------|--------|
| Provider | FriendHosting |
| Location | Germany |
| IPv4 | `92.42.99.126` |
| Hostname | `imart216311` |
| SSH | TCP/`3333` |
| OS | Ubuntu 24.04.4 LTS |
| Domain / SNI | `metacode-cloud.com` |
| DNS | operator-owned; points to `92.42.99.126` (not mutated this wave) |

---

## 3. Pre-build baseline

Captured before mutation:

- `:443` FREE, `:8443` FREE
- SSH `:3333` healthy
- Intake-01 direct gate already PASS/CLOSED CLEAN
- Fresh Ubuntu baseline consistent with intake evidence

Evidence: `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\build-01-control-node\pre-baseline-20260829T174340Z.json`

---

## 4. Backup / rollback anchor

**Status:** BACKUP + RESTORE STRATEGY CONFIRMED

| Item | Path |
|------|------|
| Remote checkpoint | `/root/mars-backups/friendhosting-prebuild-20260829T174340Z.tgz` |
| Local copy | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-prebuild-20260829T174340Z.tgz` |
| Local SHA256 | `24fbcf543d7c7deeb7d91d53435ed247ad7ddef7542624718d0e1191ef288368` |
| Rollback procedure | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\build-01-control-node\rollback-procedure-20260829T174340Z.md` |

Rollback intent: return toward Intake-01 clean pre-VPN baseline while preserving SSH `:3333`.

---

## 5. Package / build mutations

Scoped apt installs only (no Docker, no broad dist-upgrade):

- ca-certificates, curl, openssl, unzip, tar, sqlite3, ufw, certbot

Log: `...\build-01-control-node\packages-20260829T174340Z.log`

---

## 6. SSH safety

- Port remains **3333**
- Working password authentication path **preserved** (no key-only lock)
- UFW allow for `3333/tcp` set before enablement
- Post-build SSH still PASS

---

## 7. Firewall

UFW active, narrow policy:

- allow `3333/tcp` (SSH)
- allow `8443/tcp` (VPN)
- temporary `:80` used only for ACME HTTP-01, then removed
- panel not published publicly (localhost bind)

---

## 8. 3X-UI installation

| Item | Value |
|------|--------|
| Version | **3.7.0** |
| Panel listen | `127.0.0.1:20901` |
| Access model | SSH tunnel only |
| Credentials / base path | [LOCAL SECRET EXISTS — VALUE NOT EXPOSED] |

---

## 9. Xray installation / version

| Item | Value |
|------|--------|
| Observed bundled Xray | **26.7.28** |
| Client isolated binary used | `C:\Program Files\v2rayN\bin\xray\xray.exe` → **26.7.28** |

Parity note: EQVPS also reports Xray 26.7.28 / 3X-UI 3.7.0. VEESP historically differs (older server Xray in prior EXP-A01 evidence).

---

## 10. TLS certificate

| Item | Value |
|------|--------|
| Domain | `metacode-cloud.com` |
| Method | `certbot --standalone` HTTP-01 (temporary :80) |
| Permanent nginx | **not** installed |
| Paths | `/etc/letsencrypt/live/metacode-cloud.com/fullchain.pem` + `privkey.pem` |
| Verify return code | **0** |
| Private key | not exposed |

---

## 11. VLESS TLS RAW :8443 architecture

| Field | Value |
|-------|--------|
| Remark / inbound id concept | `FRIENDHOSTING-DE-RAW-8443` |
| Protocol | VLESS |
| Security | TLS |
| Network | RAW/TCP |
| Port | **8443** |
| SNI | `metacode-cloud.com` |
| ALPN | `http/1.1` (VEESP-equivalent control target) |
| Flow | empty |
| Mux | disabled on client profile |
| Sniffing | **disabled** (VEESP-like) |
| Reality / XHTTP / WS / WireGuard | **not** built |
| Second inbound | **not** built |

---

## 12. VEESP parity comparison

Intentional near-parity control (provider/IP/path as main variable):

| Aspect | FriendHosting Build 01 | VEESP (prior evidence) | EQVPS (prior evidence) |
|--------|------------------------|------------------------|-------------------------|
| VLESS+TLS+RAW `:8443` | YES | YES | YES |
| ALPN `http/1.1` | YES | YES | YES |
| Sniffing | OFF | OFF | ON (difference vs FH/VEESP) |
| Server Xray | 26.7.28 | older in EXP-A01 (e.g. 26.6.22 class) | 26.7.28 |
| 3X-UI | 3.7.0 | n/a / different history | 3.7.0 |
| Provider / IP / geo | FriendHosting DE `92.42.99.126` | VEESP | EQVPS |

Remaining differences vs VEESP are expected and documented; do not invent additional transports to “improve” parity.

---

## 13. Server-side validation

PASS:

- `x-ui` active
- `:8443` listening (`xray-linux-amd64`)
- External TCP `:8443` reachable from workstation
- TLS handshake / certificate verify = 0
- ALPN `http/1.1` present
- SSH `:3333` preserved

Note: plain HTTPS to `:8443` returns empty reply — expected for VLESS (not an HTTP origin).

---

## 14. Isolated client transport validation

Local temporary proxy: `127.0.0.1:18088` → FriendHosting `:8443`

| Check | Result |
|-------|--------|
| Local listen | PASS |
| `api.ipify.org` egress | **92.42.99.126** PASS |
| Ordinary HTTPS | PASS |
| ~10 MB body | **10485760** bytes PASS |

Evidence: `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\build-01-control-node\isolated-transport-result.json`

**Build issue resolved during PREP (not left open):**

1. Initial 3X-UI 3.7.0 inbound had empty runtime `clients[]` → auth impossible.  
2. Manual clients-table insert used `tg_id=""` (TEXT) while schema expects INTEGER → x-ui crash-looped restarting Xray → `:8443` vanished.  
3. Fix: set `tg_id=0`, sync inbound settings/clients, restore healthy `x-ui`/Xray. Isolated retest then PASS.

---

## 15. v2rayN client profile

| Item | Value |
|------|--------|
| Display name | **MCA-ONE-FRIENDHOSTING-DE-RAW-8443** |
| JSON | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\clients\MCA-ONE\friendhosting-de-raw-8443.json` |
| VLESS URI file | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\clients\MCA-ONE\friendhosting-de-raw-8443.vless.txt` |
| Secrets | [LOCAL SECRET EXISTS — VALUE NOT EXPOSED] |

Structural checks: address/domain, port 8443, TLS, SNI, ALPN `http/1.1`, flow empty, mux false, no Reality fields.

Import ≠ runtime success historically for Reality bugs; this profile is plain VLESS TLS RAW — use standard v2rayN import, then prove via harness.

---

## 16. Offline acceptance harness

| Item | Value |
|------|--------|
| Harness | `X:\AI MARS\projects\mars-server-ops\tools\experiments\FRIENDHOSTING-DE-RAW-8443\Invoke-FRIENDHOSTING-DE-RAW-8443.ps1` |
| Evidence root | `X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-DE-RAW-8443\` |
| DryValidate | PASS (`...\2026-08-30_010218_dryvalidate`) |
| Admin PowerShell | **NO** (not required) |
| Auto VPN switch | **NO** |

Phases (operator-guided):

0. Precheck  
1. VEESP baseline  
2. Manual select `MCA-ONE-FRIENDHOSTING-DE-RAW-8443`  
3. FriendHosting transport capture  
4. Real-app acceptance (Cursor / ChatGPT / YouTube / optional Facebook)  
5. Manual restore VEESP RAW `:8443`  
6. VEESP recovery control  
7. Evidence finalize  

---

## 17. Operator instructions

1. Import local profile **MCA-ONE-FRIENDHOSTING-DE-RAW-8443** from the local-only path above (do not paste URI into chat/Git).  
2. Keep TUN / System Proxy / routing / DNS / MTU / UDP-443 block unchanged vs current VEESP working baseline.  
3. Launch harness (one line):

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "X:\AI MARS\projects\mars-server-ops\tools\experiments\FRIENDHOSTING-DE-RAW-8443\Invoke-FRIENDHOSTING-DE-RAW-8443.ps1"
```

4. Follow on-screen phases. If Cursor dies after FriendHosting switch — continue in that PowerShell window.  
5. Always restore VEESP RAW `:8443` before ending.  
6. Return the session evidence directory path to Cursor after COMPLETED.marker.

Interpretation cases A/B/C remain as chartered — do not prejudge root cause.

---

## 18. Known differences vs VEESP

- Different provider / IP / network / location (primary experimental variable)
- Server Xray 26.7.28 vs historically older VEESP core in EXP-A01 evidence
- Panel stack is 3X-UI 3.7.0 (aligned with EQVPS, not necessarily identical to VEESP management path)
- Sniffing OFF on FriendHosting (VEESP-like; differs from EQVPS ON)

---

## 19. Risks / unresolved items

- Panel HTTP API from localhost returned 403/404 during build; client was finalized via DB+runtime config discipline — prefer SSH-tunnel panel for future edits.
- `tg_id` type mismatch can break Xray restart if clients rows are hand-edited incorrectly again.
- Real-app acceptance **not yet run** — transport PASS does not imply Cursor/ChatGPT/YouTube PASS.
- Foreign WIP in repo remains out of scope; do not stage/commit it.
- Unpushed commits may exist on canonical branch — this wave did not commit/push.

---

## 20. Evidence paths

| Kind | Path |
|------|------|
| Local build evidence | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\build-01-control-node\` |
| Local secrets / profile | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\` |
| Programme evidence root | `X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-DE-RAW-8443\` |
| Harness | `X:\AI MARS\projects\mars-server-ops\tools\experiments\FRIENDHOSTING-DE-RAW-8443\` |
| This report | `X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-FRIENDHOSTING-CONTROL-NODE-BUILD-01-PREP.md` |
| Intake reference | `X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-FRIENDHOSTING-INTAKE-01-DIRECT-443-GATE.md` |

---

## 21. Git / server mutation closeout

| Item | Status |
|------|--------|
| VEESP mutation | **0** |
| EQVPS mutation | **0** |
| FriendHosting SSH `:3333` preserved | **YES** |
| FriendHosting `:8443` created | **YES** |
| Secret disclosure in REPORT/chat/Git | **0** |
| commit | **0** |
| push | **0** |
| `git add .` / clean / reset | **0** |

Foreign WIP remains present and untouched.

**STOP.** Operator acceptance checkpoint is next; agent does not switch VPN or run real-app acceptance in this wave.

# REPORT — MARS Server Ops EXP-A01 — Live VEESP ↔ EQVPS Runtime Reconciliation

**Date (UTC acquisition window):** 2026-08-29 ≈ 08:25–08:40Z  
**Mode:** LIVE READ-ONLY / EVIDENCE-FIRST  
**Programme:** `projects/mars-server-ops/`  
**Evidence root (local, non-git):** `X:\AI MARS\local\infrastructure\EXP-A01-live-recon-2026-08-29\`  
**Prior wave:** `MARS-SERVER-OPS-EQVPS-AUDIT-01-EVIDENCE-ARCHITECTURE-RECONCILIATION.md`

---

## 1. Executive verdict

**Live `:8443` transport class on both nodes is VLESS + TLS + RAW/TCP (`network: tcp`, header `none`) with ALPN `http/1.1`.** AUDIT 01’s unresolved “VEESP may still be WebSocket” question is **closed against live effective config**: VEESP effective inbound is **RAW/tcp**, matching the operator client profile — Aug 25 “WS” intake is **STALE DOCUMENTATION**.

**Same-session transport health:** VEESP TUN and EQVPS isolated `:18088` both **PASS** egress + HTTPS + repeated HTTPS + 10 MB transfer. **EQVPS TUN real-app A/B was NOT completed** in this wave (Program Files `guiNConfig.json` write denied; UAC elevation failed/denied). Therefore **CASE A (provider/path strengthened by VEESP PASS / EQVPS FAIL under proven material equivalence) is NOT established**.

**Interpretation branch:** closest to **partial CASE B** (material-candidate live differences exist: sniffing on/off; Xray 26.6.22 vs 26.7.28; OS/kernel) **plus incomplete same-TUN real-app matrix**. Provider/IP/path hypothesis is **not proven** and is only **weakly** informed by transport equivalence.

### Executive answers (A–I)

| Q | Answer | Notes |
|---|--------|-------|
| **A.** VEESP sustained real-app acceptance this session? | **YES** (Cursor) / **PARTIALLY** (others) | Cursor Agent multi-turn on VEESP TUN egress `178.173.250.69` **PASS**. ChatGPT/YouTube **browser** playback/prompt **NOT TESTED** (HTTP fetch only). |
| **B.** EQVPS sustained real-app acceptance this session? | **NOT TESTED** (TUN) / transport **PASS** (isolated) | TUN profile switch blocked. Isolated `:18088` RAW transport **PASS**. |
| **C.** Live VEESP/EQVPS `:8443` materially equivalent? | **PARTIALLY** | Core VLESS/TLS/RAW/ALPN/flow-empty **EQUIVALENT**. Sniffing + Xray version **DIFFERENT — POSSIBLY MATERIAL**. |
| **D.** Material server config difference discovered? | **PARTIALLY** | No smoking-gun field mismatch on primary transport; sniffing + version remain candidates. |
| **E.** Material client-path inconsistency (`:10808` vs `:18088`)? | **PARTIALLY** historically / **BENIGN** now | `:10808` = live v2rayN mixed. `:18088` **not listening** at precheck; used only as temporary isolated EQVPS probe. |
| **F.** Evidence materially strengthen provider/IP/path hypothesis? | **NO** (not yet) | Need same-TUN Cursor/ChatGPT/YouTube matrix with EQVPS profile active. |
| **G.** Provider/path root cause proven? | **UNPROVEN** | — |
| **H.** FriendHosting justified as next independent control? | **NO** | Close TUN A/B + sniffing-equivalence first. |
| **I.** Single best next action? | **EXP-A01b / operator TUN switch** | Operator selects EQVPS RAW `:8443` in v2rayN UI (normal workflow), repeat Cursor≥3 + ChatGPT functional + YouTube playback, restore VEESP. Optionally EXP-A02 sniffing off on EQVPS under separate **mutation** charter. |

---

## 2. Scope / safety closeout

| Boundary | Status |
|----------|--------|
| Workspace `X:\AI MARS` | Confirmed |
| Volume `AI WS` | Confirmed (preflight) |
| Branch `mars/canonical-post-recovery` | Confirmed |
| Foreign WIP | Present (~1090 status lines) — **OUT OF SCOPE** |
| Git commit/push | **Not performed** |
| VEESP mutation | **0** (SSH observational + sudo read where needed) |
| EQVPS mutation | **0** |
| Client structural config mutation | **0** (IndexId write **attempted** → **ACCESS DENIED**; no successful change; IndexId remained VEESP) |
| FriendHosting provision | **Not performed** |
| Packet capture | **DEFERRED — REQUIRES NEXT EXPLICIT CHARTER** |
| Secrets in report | Redacted |

**STOP tokens:** none triggered for wrong volume/branch. Staged changes: empty.

---

## 3. Sources and live systems inspected

| System | Identity | Access |
|--------|----------|--------|
| VEESP | `178.173.250.69` / `wsp-cloud.com` / host `wsp-cloud` | root SSH (existing MCA-VPN-001 secrets contour) |
| EQVPS | `95.216.126.173` / `metacode-cloud.com` / host `metacode-cloud` | `marsops` Ed25519 + sudo for config/UFW |
| Windows client | Win10 build 19045; v2rayN 7.22.3; Xray 26.7.28 | Local observation |
| Docs | AUDIT 01, WEBGPT handoff, programme ACCESS-MODEL / OPERATIONAL-INDEX | Read-only |

---

## 4. VEESP live runtime model

| Field | Live value |
|-------|------------|
| OS | Ubuntu **22.04.5** LTS |
| Kernel | `5.15.0-187-generic` |
| Uptime (at capture) | ~12 days |
| x-ui | **active / enabled**; MainPID under `/usr/local/x-ui/x-ui` since 2026-08-17 |
| Xray | **26.6.22** (`b99c3e5`, go1.26.4) via `bin/xray-linux-amd64 -c bin/config.json` |
| Effective config | `/usr/local/x-ui/bin/config.json` (3X-UI generated) |
| `:8443` | VLESS, listen `0.0.0.0`, **tcp/RAW**, **tls**, ALPN `http/1.1`, `serverName` `wsp-cloud.com`, sniffing **disabled**, clients **7** (IDs redacted) |
| Other Xray | Reality `:46489`; api localhost |
| Also listening | x-ui `:5928`, sub `:2096`, Docker MTProto `:8445`, ssh `:22` |
| nginx | **not installed** |
| UFW | **inactive** |
| eth0 | `178.173.250.69/24`, **IPv6 present**, MTU **1500** |
| Sysctl (targeted) | `tcp_mtu_probing=0`, `cubic`, `fq_codel`, sack/timestamps/window_scaling=1, `ip_no_pmtu_disc=0` |
| Cert | LE YE2, CN/SAN `wsp-cloud.com`, 2026-08-13 → 2026-11-11; path `/root/cert/wsp-cloud.com/` |
| Routing | `domainStrategy: AsIs`; outbounds direct/blocked; access log `none` |
| DNS section | Not present / empty in sanitized dump |

---

## 5. EQVPS live runtime model

| Field | Live value |
|-------|------------|
| OS | Ubuntu **24.04.4** LTS |
| Kernel | `6.8.0-138-generic` |
| Uptime (at capture) | ~1d 16h |
| x-ui | **active**; same launch model under `/usr/local/x-ui` |
| Xray | **26.7.28** (`5ca6f4b`, go1.26.5) |
| Effective config | `/usr/local/x-ui/bin/config.json` (sudo required to read) |
| `:8443` | VLESS, `0.0.0.0`, **tcp/RAW**, **tls**, ALPN `http/1.1`, `serverName` `metacode-cloud.com`, sniffing **enabled**, clients **6**, fallbacks `[]` |
| Also live | `:443` XHTTP; `:24443` RAW/TLS A/B; panel `:20901`; sub `:2096` |
| nginx | **not installed** |
| UFW | **active**; 22/443/8443/20901/2096/24443 allowed |
| eth0 | `95.216.126.173/28`, link-local IPv6 only, MTU **1500** |
| Sysctl (targeted) | **Identical** to VEESP values above |
| Cert | LE YE2, CN/SAN `metacode-cloud.com`, 2026-08-27 → 2026-11-25; files under Let’s Encrypt live path in config |
| Routing/DNS | Same pattern: AsIs, direct/blocked; `dns: null` |

---

## 6. Documented vs live config drift

| Claim / source | Live | Classification |
|----------------|------|----------------|
| VEESP `:8443` = WebSocket (Aug 25 intake / AUDIT open Q) | **tcp/RAW** | **STALE DOCUMENTATION** / historical **CONFIG DRIFT** vs old intake |
| VEESP operator client RAW/TLS `:8443` | Matches live server | **ALIGNED** |
| EQVPS RAW `:8443` as documented in post-RAW waves | Matches live | **ALIGNED** |
| EQVPS Xray 26.7.28 | Live 26.7.28 | **ALIGNED** |
| VEESP Xray assumed same as client 26.7.28 | Live **26.6.22** | **CONFIG DRIFT** (version lag) — **POSSIBLY MATERIAL** |
| Both “equivalent enough” for provider blame (AUDIT E=NO) | Still incomplete real-app TUN matrix | Remains **NO** for provider conclusion |

---

## 7. Live VEESP ↔ EQVPS difference matrix

| Parameter | VEESP | EQVPS | Class |
|-----------|-------|-------|-------|
| OS | 22.04.5 | 24.04.4 | DIFFERENT — LIKELY IRRELEVANT (transport healthy both) |
| Kernel | 5.15 | 6.8 | DIFFERENT — LIKELY IRRELEVANT |
| eth0 MTU | 1500 | 1500 | IDENTICAL |
| IPv6 GUA | yes | no (link-local only) | DIFFERENT — LIKELY IRRELEVANT for this A/B |
| x-ui runtime model | 3X-UI + child Xray | same | EQUIVALENT |
| Xray version | 26.6.22 | 26.7.28 | DIFFERENT — POSSIBLY MATERIAL |
| `:8443` protocol | VLESS | VLESS | IDENTICAL |
| transport | tcp / none | tcp / none | IDENTICAL |
| security | tls | tls | IDENTICAL |
| ALPN | http/1.1 | http/1.1 | IDENTICAL |
| flow | empty/absent | empty/absent | EQUIVALENT |
| sniffing | **off** | **on** | DIFFERENT — POSSIBLY MATERIAL |
| fallbacks | absent | empty list | EQUIVALENT |
| routing/outbounds | AsIs / direct+blocked | same | EQUIVALENT |
| Xray DNS | none | null | EQUIVALENT |
| cert issuer | LE YE2 | LE YE2 | EQUIVALENT |
| nginx | absent | absent | IDENTICAL |
| UFW | inactive | active (8443 allowed) | DIFFERENT — LIKELY IRRELEVANT |
| Extra inbounds | Reality, Docker 8445 | 443 XHTTP, 24443 | DIFFERENT — LIKELY IRRELEVANT to `:8443` primary |
| TCP congestion / qdisc / MTU probing | cubic / fq_codel / 0 | same | IDENTICAL |

**Counted live differences (matrix rows marked DIFFERENT\*):** 8  
**Counted POSSIBLY MATERIAL:** 2 (sniffing; Xray version)  
**Counted clearly MATERIAL proof of app failure:** 0

---

## 8. Windows client precheck

| Item | Observed |
|------|----------|
| OS | Windows 10 Pro build **19045** |
| v2rayN | **7.22.3** (`C:\Program Files\v2rayN\v2rayN.exe`) |
| Active config path | `C:\Program Files\v2rayN\guiConfigs\` (LocalAppData copy **stale**) |
| Client Xray | **26.7.28** (PF bin) |
| TUN | **EnableTun=true**, Stack `system`, **MTU 1500**, adapter `xray_tun` Up |
| System Proxy | `ProxyEnable=0` (TUN path); ProxyServer remnant `127.0.0.1:10808` |
| Mixed proxy | **`:10808` LISTEN** owned by **xray** |
| Routing | V4 **Global** active (`IsActive=1`) |
| Active profile IndexId | `MCA-Gate-TLS-MCA-ONE` → `wsp-cloud.com:8443` RAW/TLS ALPN http/1.1 |
| Other profiles present | EQVPS RAW 8443; EQVPS RAW 24443 AB |
| Egress at precheck | **`178.173.250.69` (VEESP)** |

---

## 9. `:10808` / `:18088` reconciliation

| Port | Role this session | Verdict |
|------|-------------------|---------|
| **10808** | v2rayN mixed HTTP/SOCKS → active Xray core | **Intended production client path** |
| **18088** | Not listening at precheck; temporary isolated EQVPS RAW probe (pre-existing `isolated-xray-18088.json`) | **BENIGN at precheck**; **POSSIBLY MATERIAL historically** if earlier waves compared isolated probe to TUN apps without labeling |

Explicit `:10808` while on VEESP TUN: egress + HTTPS + 10 MB + YouTube HTTP **PASS**.

---

## 10. Same-session transport controls

| Test | VEESP TUN | EQVPS isolated `:18088` | EQVPS TUN |
|------|-----------|-------------------------|-----------|
| VPN egress | PASS `178.173.250.69` | PASS `95.216.126.173` | **NOT TESTED** |
| Ordinary HTTPS | PASS | PASS | NOT TESTED |
| Repeated HTTPS ×5 | PASS | PASS | NOT TESTED |
| ~10 MB body | PASS (~2.5s / ~1.8s) | PASS | NOT TESTED |

**CASE E (EQVPS transport fail) does not apply** for the isolated path.

---

## 11. Cursor real acceptance

| Node | Result | Evidence |
|------|--------|----------|
| VEESP `:8443` TUN | **PASS** | Sustained Agent session under confirmed VEESP egress; multi-step tool/SSH/report work without reconnect loop |
| EQVPS `:8443` TUN | **NOT TESTED** | Could not activate EQVPS profile (ACL/UAC) |

---

## 12. ChatGPT real acceptance

| Layer | VEESP | EQVPS |
|-------|-------|-------|
| Homepage (Invoke-WebRequest) | FAIL 403 (bot/WAF — not browser) | FAIL 403 (isolated) |
| LOGIN/SESSION | NOT TESTED | NOT TESTED |
| APP UI | NOT TESTED | NOT TESTED |
| PROMPT RESPONSE | NOT TESTED | NOT TESTED |
| **Final** | **NOT TESTED** (real app) | **NOT TESTED** |

Do **not** treat IWR 403 as VPN FAIL.

---

## 13. YouTube real acceptance

| Layer | VEESP TUN | EQVPS isolated |
|-------|-----------|----------------|
| Homepage HTTP | PASS | PASS |
| VIDEO PAGE | NOT TESTED | NOT TESTED |
| PLAYBACK | NOT TESTED | NOT TESTED |
| **Final** | **NOT TESTED** (playback) | **NOT TESTED** (playback) |

---

## 14. Facebook control

| Path | Result |
|------|--------|
| VEESP TUN IWR | FAIL (connection error) |
| EQVPS `:18088` IWR | PASS (200) |

Interesting but **not overinterpreted**: different path (TUN vs isolated HTTP proxy), possible regional/DNS/routing side-effects. **NOT** used to claim EQVPS app superiority.

---

## 15. Explicit proxy control

| Path | Result |
|------|--------|
| VEESP via `:10808` | PASS (egress VEESP, HTTPS, 10 MB, YouTube HTTP) |
| EQVPS via `:10808` under EQVPS TUN | **NOT TESTED** (no TUN switch) |
| EQVPS via `:18088` isolated | PASS (transport suite) |

---

## 16. Existing-log telemetry findings

- Both nodes: Xray **access log = none** → failed app connections **not visible** in access logs without config mutation.
- VEESP journal: routine TLS handshake noise on panel/sub ports; not app-specific.
- EQVPS journal as `marsops`: limited visibility; sudo journal empty for queried window.
- **Silent-at-server** for application failures remains plausible; packet capture deferred.

---

## 17. Same-session canonical acceptance matrix

| Row | VEESP `:8443` | EQVPS `:8443` |
|-----|---------------|---------------|
| VPN egress | PASS | PASS (isolated `:18088`) / NOT TESTED (TUN) |
| Ordinary HTTPS | PASS | PASS (isolated) |
| Repeated HTTPS | PASS | PASS (isolated) |
| 10 MB transfer | PASS | PASS (isolated) |
| Cursor prompt 1–3 / sustained | PASS | NOT TESTED |
| ChatGPT homepage (real browser) | NOT TESTED | NOT TESTED |
| ChatGPT functional prompt | NOT TESTED | NOT TESTED |
| YouTube homepage (HTTP) | PASS | PASS (isolated) |
| YouTube playback | NOT TESTED | NOT TESTED |
| Facebook control | FAIL (TUN IWR) | PASS (isolated IWR) |
| Explicit proxy control | PASS `:10808` | PASS `:18088` / NOT TESTED `:10808` |

---

## 18. Material differences

1. **Sniffing:** VEESP off / EQVPS on — **POSSIBLY MATERIAL** (routing metadata / DNS side-effects under TUN).  
2. **Xray server version:** 26.6.22 vs 26.7.28 — **POSSIBLY MATERIAL**; not auto-root-cause.  
3. **Incomplete same-TUN app matrix** — **MATERIAL gap in experiment**, not a server field.

---

## 19. Uncontrolled variables

- EQVPS tests used **isolated `:18088`**, not identical to v2rayN TUN/`10808` stack.  
- No real browser ChatGPT/YouTube playback automation.  
- Facebook asymmetry across path types.  
- Time-of-day / path state single window.  
- VEESP has extra Reality/Docker services; EQVPS has 443/24443.  
- Client IndexId switch requires admin ACL on Program Files.

---

## 20. Provider/path hypothesis update

| Hypothesis | Confidence after EXP-A01 |
|------------|--------------------------|
| EQVPS-specific server configuration issue | **MEDIUM** (sniffing/version candidates remain) |
| EQVPS provider/network issue | **LOW–MEDIUM** (transport PASS; apps unproven on TUN) |
| Hetzner/IP/ASN issue | **LOW** (unproven; no ASN proof in this wave) |
| Goodline↔EQVPS path issue | **LOW–MEDIUM** |
| application/CDN/backend interaction | **MEDIUM** (selective app class historically; not re-proven TUN) |
| Windows/v2rayN shared client issue | **LOW** (VEESP Cursor PASS on same client) |
| intermittent/time-dependent path issue | **MEDIUM** |

---

## 21. FriendHosting decision gate

**NO**

FriendHosting would discriminate **third-provider path** only after VEESP/EQVPS are shown **same-client TUN** PASS/FAIL with **material config equivalence** (or after an explicit sniffing/version equalization experiment). Buying FriendHosting now would **confound** remaining sniffing/version/TUN-path variables.

---

## 22. CONTRADICTIONS

- AUDIT/intake “VEESP `:8443` = WS” **contradicts** live effective **RAW/tcp**.  
- Historical “EQVPS transport fail” **contradicts** this session’s isolated RAW **PASS** (and prior RAW-era transport PASS notes).

---

## 23. STALE CONCLUSIONS

- Any conclusion that VEESP production `:8443` is WebSocket.  
- Any claim that `:18088` is currently a standing second client path (it was inactive until temporary probe).  
- Provider-blame readiness from AUDIT alone.

---

## 24. SUPERSEDED VERDICTS

- AUDIT open item “VEESP server transport class unresolved” → **SUPERSEDED: live = RAW/tcp**.  
- “Not equivalent enough for provider conclusion” → **RETAINED** (still true), but reason set updated (WS mystery closed; sniffing/version + TUN app matrix remain).

---

## 25. UNVERIFIED CLAIMS

- EQVPS TUN Cursor/ChatGPT/YouTube FAIL or PASS in this window.  
- Sniffing as actual cause.  
- Xray version delta as actual cause.  
- ASN/Hetzner ownership mapping.  
- FriendHosting Telehouse path behaviour.

---

## 26. Canonical facts after EXP-A01

1. VEESP live `:8443` = VLESS+TLS+RAW/tcp+ALPN http/1.1; sniffing off; Xray **26.6.22**.  
2. EQVPS live `:8443` = VLESS+TLS+RAW/tcp+ALPN http/1.1; sniffing on; Xray **26.7.28**.  
3. Targeted TCP sysctl set **identical**.  
4. nginx absent both; MTU 1500 both.  
5. Client active path = PF v2rayN 7.22.3 + TUN MTU 1500 + `:10808` + profile MCA-Gate (VEESP).  
6. VEESP TUN transport + Cursor sustained **PASS** this session.  
7. EQVPS isolated `:18088` transport **PASS**.  
8. EQVPS TUN app matrix **NOT TESTED** (switch blocked).  
9. Provider/path root cause **UNPROVEN**.  
10. FriendHosting **not** justified yet.

---

## 27. Remaining hypotheses

1. EQVPS sniffing-on interacts badly with TUN/DNS/routing for specific apps.  
2. Xray 26.7.28 server vs 26.6.22 behavioural delta.  
3. Provider/IP/path selective impairment **only under TUN real apps** (untested this wave).  
4. Client/profile mix-ups historically (`10808` vs `18088`).  
5. Intermittent upstream/CDN state.

---

## 28. Recommended next experiment

**EXP-A01b — Operator UI TUN A/B (no server mutation)**  
1. Operator selects `EQVPS-TLS-RAW-8443-…` in v2rayN (normal UI).  
2. Confirm egress `95.216.126.173`.  
3. Cursor ≥3 prompts + sustained; ChatGPT functional prompt; YouTube playback; optional Facebook.  
4. Switch back to VEESP; reconfirm egress.  
5. File matrix into amendment or EXP-A01b report.

**Then (mutation charter only):** EXP-A03 sniffing-off on EQVPS `:8443` A/B.  
**Only later:** FriendHosting third control.

---

## 29. Evidence path index

- `local\infrastructure\EXP-A01-live-recon-2026-08-29\veesp\` — host/Xray/config/cert/firewall  
- `...\eqvps\` — same + `12b_inbound_summary.json` + sudo firewall  
- `...\client\10_veesp_tun_transport.txt`  
- `...\client\12_eqvps_isolated_18088_transport.txt`  
- `...\client\14_veesp_explicit_10808.txt`  
- `...\client\04_sqlite_profiles_safe.json`  
- `...\client\19_tun_switch_blocker.txt`  
- `...\client\15_tun_ab_harness.log` (ACL denial)

---

## 30. Git/server/client mutation closeout

| Check | Value |
|-------|-------|
| Git mutation (commit/push) | **0** |
| Report file created under `projects/mars-server-ops/reports/` | **yes** (uncommitted; foreign WIP untouched) |
| VEESP mutation | **0** |
| EQVPS mutation | **0** |
| Client configuration mutation | **0** (no successful IndexId change) |
| Secret disclosure | **0** |

**Primary principle applied:** LIVE EQUIVALENCE FIRST — PROVIDER BLAME SECOND.

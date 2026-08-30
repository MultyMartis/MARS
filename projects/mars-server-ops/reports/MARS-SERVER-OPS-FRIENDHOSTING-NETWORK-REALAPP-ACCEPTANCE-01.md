# REPORT — FriendHosting Network & Real-App Acceptance 01

**Programme:** MARS Server Ops & VPS Forge  
**Wave:** FRIENDHOSTING-NETWORK-REALAPP-ACCEPTANCE-01  
**Date (local):** 2026-08-30  
**Mode:** READ-ONLY diagnostic + acceptance characterization  
**Active client profile (operator + evidence):** `MCA-ONE-FRIENDHOSTING-DE-RAW-8443`  
**Git:** no commit / no push  

**Mutations this wave:** VEESP = 0 · EQVPS = 0 · FriendHosting VPN/network = 0 · Windows network = 0 · secret disclosure in report artifacts = 0  

**Evidence class legend:** FACT · INFERENCE · UNPROVEN · OPERATOR-PROVIDED  

---

## 1. Executive verdict

FriendHosting Germany (`92.42.99.126`, VLESS+TLS+RAW `:8443`) is a **working third control node**.

| Layer | Verdict |
|-------|---------|
| **TRANSPORT ACCEPTANCE** | **PASS** |
| **REAL-APP ACCEPTANCE** (Cursor / ChatGPT / YouTube) | **PASS** |
| Cursor (this Agent diagnostic session) | **PASS** |
| ChatGPT | **OPERATOR PASS** |
| YouTube (incl. playback) | **OPERATOR PASS** |
| Google | **OPERATOR PASS** (+ transport HEAD 12/12) |
| Facebook | **NON-BLOCKING** (operator FAIL; raw HTTPS via proxy PASS) |
| Exact EQVPS root cause | **UNPROVEN** |
| Long-term FriendHosting stability | **NOT YET PROVEN** |

**Primary diagnostic conclusion:** under the same Windows/v2rayN/TUN/client-Xray stack that **fails real apps on EQVPS** and **passes on VEESP**, FriendHosting now **passes both transport and real apps**. This **further weakens** global-client / generic-architecture hypotheses and **strengthens** EQVPS-endpoint / provider / ASN / path / application-treatment hypotheses — **without proving** which EQVPS sub-cause is causal.

---

## 2. Exact active VPN/client state

| Item | Observed value | Class |
|------|----------------|-------|
| v2rayN process | running (PID observed) | FACT |
| xray process | running; owns `127.0.0.1:10808` Listen | FACT |
| v2rayN version | **7.22.3** (`7.22.3+ccb0ffb3…`) | FACT |
| client Xray | **26.7.28** (`go1.26.5 windows/amd64`) | FACT |
| mixed proxy | `127.0.0.1:10808` | FACT |
| System Proxy (WinINET ProxyEnable) | **0** (OFF) | FACT |
| TUN | `xray_tun` **Up** (Wintun Tunnel) | FACT |
| TUN IPv4/IPv6 NlMtu | **1500 / 1500** | FACT |
| TunMode.EnableTun | **true** | FACT |
| TunMode.Mtu (guiNConfig) | **1500** | FACT |
| TunMode.EnableIPv6Address | **false** | FACT |
| TunMode.Stack | `system` | FACT |
| Default route preference | `0.0.0.0/0` and `::/0` via `xray_tun` present | FACT |
| Profile in guiNDB | Remarks=`MCA-ONE-FRIENDHOSTING-DE-RAW-8443`; Address=`metacode-cloud.com`; Port=`8443`; Network=`raw`; StreamSecurity=`tls`; Sni=`metacode-cloud.com`; Alpn=`http/1.1`; Flow=empty | FACT |
| Egress via `:10808` | **92.42.99.126** (ipify / ifconfig.me / icanhazip / api64.ipify) | FACT |
| Egress without explicit proxy (TUN path) | **92.42.99.126** | FACT |
| Operator UI latency | ~**84 ms** | OPERATOR-PROVIDED |

**CLIENT ACTIVE PROFILE = CONFIRMED**

Confirmation basis: profile present in v2rayN DB with expected remarks/SNI/port; multi-endpoint egress equals FriendHosting IPv4; operator states this profile is active; working profile was **not** edited this wave.

---

## 3. FriendHosting node identity

| Field | Value |
|-------|-------|
| Provider (commercial) | FriendHosting |
| Hostname | `imart216311` |
| Public IPv4 | `92.42.99.126` |
| Public IPv6 (server) | `2a06:fcc0:a::15b/48` |
| Domain / SNI | `metacode-cloud.com` |
| SSH | TCP/`3333` (`sshd`) |
| VPN inbound | TCP/`8443` (`xray-linux-amd64`) |
| Public HTTPS panel front | TCP/`443` (`nginx`) → `127.0.0.1:20901` |
| 3X-UI listen | `127.0.0.1:20901` |
| OS | Ubuntu 24.04.4 LTS |
| Kernel | `6.8.0-138-generic` x86_64 |
| 3X-UI | **3.7.0** (prior build evidence; process `/usr/local/x-ui/x-ui` live) |
| Server Xray | **26.7.28** |
| Search domain (resolv) | `friendhosting.net` |

Listener ownership re-confirmed this wave (FACT):

- `:8443` → Xray  
- `:443` → nginx  
- `:3333` → sshd  
- `127.0.0.1:20901` → x-ui  

Also observed (FACT, not mutated): x-ui also listens on `*:2096` (subscription-related surface from prior build; out of scope).

---

## 4. Network ownership / ASN / prefix

| Item | Value | Class / source |
|------|-------|----------------|
| Announced prefix | **92.42.99.0/24** | FACT — [bgp.he.net/net/92.42.99.0/24](https://bgp.he.net/net/92.42.99.0/24), RIPE RDAP |
| Origin ASN | **AS47447** | FACT — HE / RIPE route `origin: AS47447` |
| ASN organization | **23M GmbH** (as-name TTM / 23M) | FACT — HE AS47447 |
| Prefix registrant | **Friendhosting LTD** | FACT — HE prefix registrant; RIPE `FRIENDHOSTING-MNT` |
| RIPE inetnum name | `BG-FRIENDHOSTING10-20240112` | FACT — [rdap.db.ripe.net/ip/92.42.99.126](https://rdap.db.ripe.net/ip/92.42.99.126) |
| RIPE country on inetnum | **DE** | FACT — RDAP |
| Matching RIPE delegation CC (HE) | **BG** | FACT — HE “Matching Delegations” |
| Org address (corporate) | Burgas, Bulgaria (Friendhosting LTD) | FACT — RDAP org entity |
| PTR | `imart216311.vds` | FACT — workstation Resolve-DnsName PTR |
| Relationship model | FriendHosting customer prefix announced via **23M GmbH AS47447** | INFERENCE from HE origin vs registrant split |
| 23M published upstreams | AS174, AS1299, AS3320, AS3356 (+ peering via AS6777) | FACT as published in AS47447 RIPE remarks (HE) |

**Interpretation (INFERENCE):** the IP is **not** a direct FriendHosting autonomous system in BGP; it is a FriendHosting-managed allocation riding **23M GmbH** transit/peering. This is **materially different** from EQVPS Helsinki on **Hetzner AS24940**.

---

## 5. Datacenter / geolocation evidence

| Evidence | Result | Class |
|----------|--------|-------|
| Cloudflare `/cdn-cgi/trace` via VPN egress | `ip=92.42.99.126`, `colo=FRA`, `loc=DE` | FACT (path/CDN view) |
| Commercial label | FriendHosting Germany | OPERATOR / prior reports |
| Third-party geo DBs (IPinfo-class) | often Frankfurt am Main, DE | INFERENCE / UNPROVEN as precise rack location |
| RIPE country DE vs org BG | country field DE; company registered BG | FACT (do not over-resolve) |

**Precise datacenter hall/rack = UNPROVEN.**  
**Strong working location signal = Germany / FRA-facing** (Cloudflare colo FRA + DE country fields).

---

## 6. Server network baseline

Captured via SSH read-only inventory (no sysctl/MTU/firewall changes):

| Item | Value |
|------|-------|
| NIC | `eth0` (altname `enp0s18`) |
| IPv4 | `92.42.99.126/24` |
| IPv4 default GW | `92.42.99.1` |
| IPv6 | `2a06:fcc0:a::15b/48` + link-local |
| IPv6 default | via `2a06:fcc0:a::1` |
| eth0 MTU | **1500** |
| qdisc | `fq_codel` on eth0 |
| tcp_congestion_control | `cubic` |
| default_qdisc | `fq_codel` |
| tcp_timestamps | 1 |
| tcp_window_scaling | 1 |
| tcp_ecn | 2 |
| ipv6 disable_all | 0 (IPv6 enabled) |
| Resolver | systemd-resolved stub `127.0.0.53`; search `friendhosting.net` |
| Server egress IPv4 | `92.42.99.126` |
| Server egress IPv6 | `2a06:fcc0:a::15b` |
| Offloads | TSO/GSO/GRO on (ethtool -k); informational only |

---

## 7. Goodline → FriendHosting direct gate recap

**Do not overwrite Intake-01 with TUN-on traceroute.**

While TUN was active this wave, `Find-NetRoute 92.42.99.126` and `tracert` collapsed to `xray_tun` / 1-hop illusion — **not** a valid direct-Goodline path measurement.

**Canonical Intake-01 FACTS (TUN OFF historically):**

| Gate | Result |
|------|--------|
| Ping | 20/20 PASS, 0% loss, ~89–90 ms |
| SSH `:3333` | PASS |
| TCP `:443` with known listener | 25/25 PASS, typical ~85–100 ms, one ~1083 ms outlier |
| Operator public IP then | `46.181.159.198` |

**Verdict:** direct Goodline reachability to FriendHosting was previously **PASS / CLOSED CLEAN**.

---

## 8. VPN egress validation

| Endpoint | Via `:10808` | Result |
|----------|--------------|--------|
| api.ipify.org | yes | `92.42.99.126` |
| ifconfig.me/ip | yes | `92.42.99.126` |
| icanhazip.com | yes | `92.42.99.126` |
| api64.ipify.org | yes | `92.42.99.126` (IPv4 literal) |
| api.ipify.org | no explicit proxy (TUN) | `92.42.99.126` |
| Cloudflare trace | yes | `ip=92.42.99.126`, `colo=FRA` |

**EGRESS = 92.42.99.126 (CONFIRMED).**

---

## 9. DNS behaviour

| Observation | Detail | Class |
|-------------|--------|-------|
| Ethernet DNS | `192.168.0.1` | FACT |
| xray_tun DNS servers shown | `fec0:0:0:ffff::1..3` (IPv6 family listing) | FACT |
| TUN IPv6 addressing | disabled in TunMode | FACT |
| `metacode-cloud.com` A | `92.42.99.126`; AAAA empty (workstation Resolve-DnsName) | FACT |
| nslookup @1.1.1.1 / @8.8.8.8 | A=`92.42.99.126` | FACT |
| Proxy-mediated name use | curl via `:10808` succeeds for google/youtube/chatgpt/cloudflare/example/facebook | FACT |
| Local Resolve-DnsName anomalies | some names returned unexpected A sets; facebook Resolve-DnsName failed while proxy HTTPS to facebook PASS | FACT |
| Interpretation | application traffic via mixed proxy/TUN uses **proxy/core DNS path**; raw Windows Resolve-DnsName is **not** authoritative proof of tunnel DNS | INFERENCE |
| `.ru` destinations | may be Goodline-direct per existing routing context — **not used** as VPN egress proof | prior context |

DNS was **not** changed.

---

## 10. IPv4 / IPv6 behaviour

| Path | Result |
|------|--------|
| Workstation IPv4 egress (proxy + TUN) | `92.42.99.126` |
| Workstation `curl -6` to api64 | fail (could not resolve / connect) |
| TunMode.EnableIPv6Address | **false** |
| Server has working IPv6 egress | yes (`2a06:fcc0:a::15b`) |
| Client using server IPv6 for app egress | **no evidence** |

**IPv4 egress:** FriendHosting IPv4  
**IPv6 egress (client apps):** none observed  
**IPv6 LEAK SUSPECTED = NO** (best evidence: IPv6 TUN address disabled + curl -6 failures + IPv4-only public egress). Residual absolute proof against all leak classes remains **UNPROVEN** without packet capture.

---

## 11. Route/path observations

### Goodline → FriendHosting (direct)

Intake-01: ~90 ms, stable TCP/SSH/443. Full ASN hop sequence from this workstation **not freshly captured** under TUN-off (mutation-avoidance).

### Workstation → Internet while VPN active

Default route via `xray_tun`. Cloudflare edge seen as **FRA**.

### FriendHosting vs EQVPS path family

| Node | Country signal | ASN family | Prior app result |
|------|----------------|------------|------------------|
| FriendHosting | DE / FRA | **AS47447 23M GmbH** (FriendHosting prefix) | **PASS** (this wave) |
| EQVPS Helsinki | FI / HEL (prior CF traces) | **AS24940 Hetzner** (95.216/16 class) | transport PASS / **apps FAIL** (EXP-A01b) |
| VEESP | prior control egress `178.173.250.69` | distinct from EQVPS Hetzner HEL | **PASS** |

**INFERENCE:** FriendHosting provides a **non-Hetzner-Helsinki** third control. App PASS here while EQVPS fails under same client **strengthens** provider/ASN/path/reputation interaction hypotheses for EQVPS.

Exact hop-by-hop Goodline→FRA vs Goodline→HEL comparison = **UNPROVEN** in this wave (TUN-on traceroute unusable; no looking-glass from Kemerovo executed).

---

## 12. MTU / PMTU findings

| Surface | MTU |
|---------|-----|
| Wintun / xray_tun NlMtu | 1500 |
| TunMode.Mtu | 1500 |
| FriendHosting eth0 | 1500 |

DF ping to `1.1.1.1` while TUN up:

- payload 1372–1472: PASS  
- 1480–1492: “needs fragmentation” / fail  

**However:** replies showed **TTL=64** and **&lt;1 ms** — consistent with **local TUN/stack ICMP behaviour**, **not** a clean underlay/VPN PMTU measurement across Goodline→Germany.

Large HTTPS bodies (1 / 10 / 25 MB) via `:10808` all **PASS** with no reset pattern.

**PMTU NOT PROVEN** for the real tunnel/underlay path.  
**No evidence** of black-hole MTU as a FriendHosting acceptance blocker.  
Hypothesis H9 (MTU as EQVPS root cause) remains **WEAKENED / LOW** given large-body PASS on both prior EQVPS transport and FriendHosting.

---

## 13. TLS / ALPN / HTTP protocol findings

### VPN server `:8443`

| Check | Result |
|-------|--------|
| SNI | `metacode-cloud.com` |
| Certificate CN | `metacode-cloud.com` |
| Chain | Let’s Encrypt (ISRG) |
| Verify | return code 0 (ok) |
| Protocol | **TLSv1.3** |
| Cipher | TLS_AES_128_GCM_SHA256 |
| ALPN | **http/1.1** |

### Through mixed proxy to public HTTPS

| Check | Result |
|-------|--------|
| CONNECT to google | HTTP/1.1 200 Connection established |
| ALPN offered/accepted (this Windows curl) | **http/1.1** |
| HTTP version (curl) | 1.1 |
| Alt-Svc | google advertised `h3` (HTTP/3 available at origin) |
| Cloudflare trace | `http=http/1.1`, `tls=TLSv1.2` (as reported by CF for this curl path) |
| Windows curl `--http2` / `--http3` | **unsupported** by installed libcurl |

**Do not claim HTTP/2 as root cause of anything.**  
Comparative note only: this client curl path is HTTP/1.1-capable and healthy through FriendHosting; browser apps (YouTube/ChatGPT/Cursor) may negotiate differently and still PASS (operator + this Agent).

---

## 14. Repeated transport/stability tests

Explicit proxy `127.0.0.1:10808` throughout.

| Suite | Result |
|-------|--------|
| HEAD google ×12 (2 s delay) | **12/12 PASS** (~0.48–0.59 s) |
| Keep-alive GET example.com ×8 | **8/8 PASS** |
| Extra TLS sessions to Cloudflare trace ×10 | **10/10 PASS** (~0.45–0.53 s; TLS ~0.37–0.44 s) |
| Medium body 1 MB ×5 | **5/5 PASS** (~1.04–1.09 s) |

**Failures / resets / EOF / sudden stalls in these suites: 0 observed.**

Stability over several minutes of sequential HTTPS: **healthy in this window**.

---

## 15. Transfer/throughput tests

| Transfer | HTTP | Size | Time (approx) | Throughput (curl speed) |
|----------|------|------|---------------|-------------------------|
| Small (jquery CDN) | 200 | 87533 | ~0.66 s | ~132 KB/s reported |
| 1 MB | 200 | 1000000 | ~1.04 s | ~0.96 MB/s |
| 10 MB | 200 | 10000000 | ~1.92 s | ~5.2 MB/s |
| 25 MB | 200 | 25000000 | ~4.06 s | ~6.2 MB/s |

**Medium/large body transfer = PASS.**  
No retries required; no mid-transfer collapses observed.

---

## 16. Cursor real-app acceptance

**Classification: CURSOR PASS**

This Agent task itself executed successfully through the active FriendHosting profile across **≥10 meaningful operation/tool cycles**, including:

1. Reading Server Ops indexes/reports  
2. Preflight / git status  
3. Client/TUN capture  
4. Multi-endpoint egress tests  
5. SSH read-only inventory  
6. Transport/stability suites  
7. DNS/IPv6/Facebook light checks  
8. TLS/ASN/web research  
9. Route/MTU probes  
10. Evidence + this report authoring  

**Not observed:** Reconnecting loops, endless Thinking, “taking longer” hang, tool-stream interrupt, unexpected agent stop, lost backend connectivity attributable to VPN.

This is stronger than a single chat turn: multi-cycle tool use remained healthy for the duration of the diagnostic.

---

## 17. ChatGPT / YouTube / Google operator evidence

| App | Evidence type | Result |
|-----|---------------|--------|
| Google | OPERATOR-PROVIDED + transport HEAD 12/12 | **PASS** |
| YouTube | OPERATOR-PROVIDED (actual use/playback) | **PASS** |
| ChatGPT | OPERATOR-PROVIDED | **PASS** |

Automated curl **does not** prove YouTube playback or ChatGPT UI usability; those remain operator real-app facts, consistent with Cursor PASS in this wave.

---

## 18. Facebook non-blocking observation

| Check | Result |
|-------|--------|
| Operator quick manual test | FAIL (non-blocking) |
| Local Resolve-DnsName | failed |
| HTTPS HEAD/GET via `:10808` | **HTTP 200** (GET ~445 KB) |

**NON-BLOCKING / NOT INVESTIGATED FURTHER.**  
Likely browser/app-specific or local-DNS quirk; raw proxy HTTPS reachability is present.

---

## 19. FriendHosting vs VEESP

| Dimension | VEESP (EXP-A01b control) | FriendHosting (this wave) |
|-----------|--------------------------|---------------------------|
| Role | Known PASS control | New third PASS control |
| Egress example | `178.173.250.69` | `92.42.99.126` |
| Transport | PASS | **PASS** |
| Cursor/ChatGPT/YouTube | PASS | **PASS** |
| Client stack | same family (v2rayN/TUN/Xray 26.7.28) | same observed versions |
| Architecture | VLESS TLS RAW `:8443` | VLESS TLS RAW `:8443` |
| Country/ASN | distinct from FriendHosting | DE / AS47447 23M + FriendHosting prefix |

**Conclusion:** FriendHosting behaves as a **second healthy control** alongside VEESP against the failing EQVPS case. FriendHosting is therefore a viable **backup/primary candidate** relative to EQVPS, subject to longer soak.

Material residual differences vs VEESP (versions/sniffing/exact provider) are **not** blocking acceptance here because apps PASS.

---

## 20. FriendHosting vs EQVPS

| Dimension | FriendHosting | EQVPS (EXP-A01b) |
|-----------|---------------|------------------|
| Provider/network | FriendHosting on **AS47447 23M** | EQVPS on **Hetzner AS24940** HEL class |
| Country | Germany / FRA signal | Finland / Helsinki |
| Public IP | `92.42.99.126` | `95.216.126.173` |
| OS | Ubuntu 24.04.4 | Ubuntu family (prior) |
| 3X-UI | 3.7.0 | prior live recon |
| Server Xray | **26.7.28** | **26.7.28** |
| Transport | VLESS+TLS+RAW `:8443` | VLESS+TLS+RAW `:8443` |
| SNI/domain | metacode-cloud.com | metacode-cloud.com (shared operator domain pattern) |
| ALPN | http/1.1 | http/1.1 class |
| flow | empty | empty class |
| sniffing | disabled (build charter) | historically **on** (prior recon; confound remains) |
| client v2rayN | 7.22.3 | same environment family |
| client Xray | 26.7.28 | 26.7.28 |
| TUN / MTU | on / 1500 | on / 1500 |
| Transport acceptance | **PASS** | **PASS** |
| Google | PASS | FAIL at app layer (A01b) |
| ChatGPT | PASS | FAIL |
| YouTube | PASS | FAIL |
| Cursor | **PASS** | FAIL |
| Observed latency | ~84 ms UI / ~90 ms direct gate | prior HEL path (different) |

**Diagnostic conclusion:** same client architecture can PASS FriendHosting and FAIL EQVPS. Therefore EQVPS failure is **not** explained by “Windows/v2rayN/TUN cannot do foreign VLESS RAW” in general. Leading remaining domain: **EQVPS/Hetzner/HEL endpoint × path × reputation × residual server-config knobs**.

---

## 21. Root-cause hypothesis update

| ID | Hypothesis | Update | Evidence (concise) |
|----|------------|--------|--------------------|
| H1 | global Windows/v2rayN/TUN failure | **WEAKENED** | FriendHosting + VEESP real-app PASS on same stack |
| H2 | client Xray 26.7.28 issue | **WEAKENED** | client 26.7.28 PASSes FriendHosting & VEESP |
| H3 | server Xray 26.7.28 generic issue | **WEAKENED** | FriendHosting server also 26.7.28 and PASSes apps |
| H4 | VLESS TLS RAW architecture generic issue | **WEAKENED** | third RAW `:8443` node PASSes |
| H5 | Goodline generic inability to use foreign VPS VPN | **WEAKENED** | FriendHosting direct gate + VPN apps PASS |
| H6 | EQVPS specific server config issue | **UNCHANGED** (still possible) | sniffing/version confounds remain; not isolated |
| H7 | EQVPS IP/prefix reputation/application treatment | **STRENGTHENED** | apps follow endpoint; FriendHosting different ASN/prefix PASSes |
| H8 | EQVPS/Hetzner/provider/network path interaction | **STRENGTHENED** | Hetzner HEL fail vs 23M/FriendHosting DE pass under same client |
| H9 | MTU/PMTU | **WEAKENED** | large bodies PASS; clean PMTU unproven but no FriendHosting symptom |
| H10 | DNS behaviour | **UNCHANGED / residual** | local Resolve quirks exist; proxy apps PASS |
| H11 | IPv6 | **WEAKENED** as FriendHosting/EQVPS differentiator | client IPv6 disabled; no leak signal |
| H12 | application/CDN-specific interaction | **STRENGTHENED** (with H7/H8) | transport PASS + app FAIL pattern historically EQVPS-specific |

**Most strengthened:** H7 + H8 (EQVPS endpoint/ASN/path/reputation/app treatment).  
**Most weakened:** H1–H5 (global client / generic RAW / Goodline-cannot).  
**Exact EQVPS root cause: UNPROVEN.**

---

## 22. FriendHosting transport verdict

**TRANSPORT ACCEPTANCE = PASS**

Basis: confirmed egress, HTTPS stability 30+/30 across suites, 1/10/25 MB transfers PASS, TLS to `:8443` valid, no reset pattern in window.

---

## 23. FriendHosting real-app verdict

**REAL-APP ACCEPTANCE = PASS**

Primary apps:

- Cursor = **PASS** (multi-cycle Agent diagnostic)  
- ChatGPT = **OPERATOR PASS**  
- YouTube = **OPERATOR PASS** (playback)  

Google supporting PASS. Facebook non-blocking.

---

## 24. Operational suitability

| Use case | Assessment |
|----------|------------|
| Everyday browser | Suitable in current window |
| ChatGPT | Suitable (operator) |
| Cursor | Suitable (this wave) |
| YouTube | Suitable including playback (operator) |
| Telegram/general Internet | Plausible by transport health; **not separately proven** |
| VPN backup/primary candidate | **Yes, as short-window acceptance candidate** |

| Metric | Comment |
|--------|---------|
| Latency | ~84–90 ms class — comfortable for interactive work |
| Stability (short window) | Excellent in tests |
| Throughput | Multi-MB/s class on 10–25 MB samples |
| Connection reliability | No failures in repeated suites |
| Operational simplicity | Same RAW `:8443` model as VEESP/EQVPS controls |
| Rollback readiness | Prior FriendHosting backups/rollback docs exist from build/nginx waves |

**Long-term reliability = NOT YET PROVEN** (hours/days soak not done).

---

## 25. Remaining unknowns

1. Multi-day/week FriendHosting soak stability.  
2. Exact Goodline→AS47447 hop graph vs Goodline→AS24940 HEL.  
3. Whether EQVPS sniffing-on vs FriendHosting sniffing-off is causal (still confound).  
4. IP-reputation scores / CDN treatment tables for `95.216.126.173` vs `92.42.99.126`.  
5. Browser-specific Facebook failure mechanism.  
6. True underlay PMTU (needs TUN-aware or TUN-off controlled test).  
7. Whether HTTP/2/3 browser negotiation differs materially (curl limited to HTTP/1.1 here).  
8. VEESP exact ASN/prefix forensic not re-run this wave.

---

## 26. Recommended next step

**STOP further FriendHosting mutation.** Use this node as the clean third control.

Recommended operator-facing next wave (choose one charter later):

1. **Soak / longitudinal acceptance** on FriendHosting (hours+) without config changes; or  
2. **EQVPS discrimination wave** that isolates Hetzner/HEL reputation/path vs residual EQVPS config (sniffing/version) — only with explicit mutation charter; or  
3. Keep VEESP + FriendHosting as dual PASS controls; treat EQVPS as failing endpoint under investigation.

Do **not** retune MTU/DNS/sysctl yet — no acceptance blocker supports it.

---

## 27. Evidence paths

Evidence directory:

`X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-DE-RAW-8443\NETWORK-ACCEPTANCE-01\2026-08-30_133528\`

Key files:

- `01-client-state.txt`  
- `03-egress.txt` / `03b-egress-no-explicit-proxy.txt`  
- `05-client-versions.txt`  
- `06-transport-stability.txt`  
- `07-server-inventory.txt`  
- `08-body-transfers.txt`  
- `09-dns-ipv6-facebook.txt`  
- `10-tls-http-protocol.txt`  
- `11-active-profile-safe.txt`  
- `12-route-tracert.txt`  
- `13-mtu-df-ping.txt`  
- `14-asn-rdap-summary.txt`  
- `15-latency-samples.txt`  
- `16-cursor-acceptance.txt`  

Report:

`X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-FRIENDHOSTING-NETWORK-REALAPP-ACCEPTANCE-01.md`

Prior related reports (unchanged this wave): Intake-01, Control-Node Build PREP, 3X-UI nginx public access, EXP-A01b EQVPS acceptance capture.

---

## 28. Mutation / Git closeout

| Item | Status |
|------|--------|
| VEESP mutation | **0** |
| EQVPS mutation | **0** |
| FriendHosting VPN profile / inbound / TLS / nginx / SSH / firewall / DNS | **0** |
| FriendHosting network/sysctl/MTU | **0** |
| Windows network / v2rayN routing / TUN MTU | **0** |
| Secret disclosure in Git report | **0** (UUID/URI/passwords/panel path not written) |
| Commit / push | **0** |
| Files created | evidence tree + this report under `projects/mars-server-ops/` |
| Foreign WIP | present elsewhere in tree; **out of scope**; not staged |
| Branch | `mars/canonical-post-recovery` |
| Preflight note | HEAD had unpushed commits vs `origin/mars/canonical-post-recovery` at session start — **not altered**; no commit created |

**STOP.**

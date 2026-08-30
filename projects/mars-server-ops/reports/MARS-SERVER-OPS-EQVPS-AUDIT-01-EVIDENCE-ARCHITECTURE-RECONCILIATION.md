# REPORT — MARS Server Ops / EQVPS Audit 01 — Evidence & Architecture Reconciliation

**Programme:** MARS Server Ops & VPS Forge  
**Task class:** READ-ONLY / EVIDENCE-FIRST AUDIT (AUDIT 01)  
**Generated:** 2026-08-29  
**Workspace:** `X:\AI MARS` · volume label **AI WS** · branch `mars/canonical-post-recovery`  
**Mutations in this task:** Git = 0 · Server = 0 · Client = 0 · Secret disclosure = 0  

**Report path:**  
`X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-EQVPS-AUDIT-01-EVIDENCE-ARCHITECTURE-RECONCILIATION.md`

**Evidence classes:** FACT · INFERENCE · HYPOTHESIS · UNPROVEN  

**Layer vocabulary (do not collapse):**  
SERVER-SIDE HEALTH · TRANSPORT HEALTH · CLIENT TRANSPORT HEALTH · REAL APPLICATION ACCEPTANCE · PRODUCTION ACCEPTANCE  

**Primary audit question:**  
Is EQVPS configured and tested close enough to the known-good VEESP control that we can reasonably attribute real-application behaviour differences to the provider / IP / network-path domain?

**Method priority:** falsify equivalence / config assumptions before blaming provider.

**Live remote verification in this audit:** **NOT PERFORMED** (repo + local evidence only).

---

## 1. Executive verdict

| # | Question | Answer | Short justification |
|---|----------|--------|---------------------|
| **A** | Is EQVPS server-side transport healthy? | **YES** | Listeners, LE TLS verify 0, runtime RAW/TLS `:8443` and cloned `:24443`, isolated Xray full-body transfers PASS (2026-08-29). |
| **B** | Has EQVPS passed universal real-application acceptance? | **NO** | No Git-safe matrix shows sustained Cursor Agent / YouTube playback / ChatGPT prompt PASS under v2rayN TUN. Operator acceptance still pending in last reports. |
| **C** | Is `:24443` proven better than `:8443`? | **NO** | Server TCP A/B identical (25/25 both). Isolated transfers both PASS. Operator Cursor/Firefox A/B **not filed** in MARS. Chat “24443 PASS” is **UNVERIFIED**. |
| **D** | Have we proven a provider / Hetzner / path root cause? | **NO** | Plausible class only. Isolated path transfers PASS; no causal proof; Hetzner FRA–HEL incident correlation ≠ causation. |
| **E** | Are VEESP and EQVPS currently equivalent enough for a provider/path conclusion without further controls? | **NO** | Protocol field match on client-claimed RAW/TLS `:8443` is strong, but **material differences remain** (server Xray version, OS, possibly VEESP server transport WS vs RAW, incomplete same-client real-app matrix, unfiled `:10808` vs `:18088`). |
| **F** | Is there a discovered server/client config error serious enough to explain current failures? | **PARTIALLY** | Historical **proven** client errors (wrong active profile; Custom v2 DNS bootstrap deadlock). **No** proven current EQVPS RAW server misconfiguration that explains isolated PASS + reported TUN app hangs. Remaining defect class **UNPROVEN**. |
| **G** | Single best next audit/experiment? | **EXP-A01** | Live read-only VEESP `:8443` inbound reconcile (WS vs RAW) **plus** same-session EQVPS RAW profile with `:10808` full-body vs `:18088` and a filed real-app matrix — before any FriendHosting purchase or provider-blame charter. |

**Central answer to the primary question:**  
**NO — not yet equivalent enough.** We can say EQVPS RAW **transport** looks healthy and **field-matched** to the *operator client’s* VEESP RAW profile. We **cannot** yet attribute real-app differences to provider/path, because (1) VEESP **server-side** transport class is unresolved vs Aug 25 intake, (2) server Xray versions differ, (3) real-app acceptance on EQVPS is not proven, (4) the discriminating `:10808` vs isolated probe was proposed but not evidenced as executed for RAW.

---

## 2. Audit scope

### In scope
- Reconstruct VEESP control, EQVPS current, Windows/v2rayN client models from MARS evidence.
- Build VEESP↔EQVPS difference matrix with materiality labels.
- Reconcile 443/XHTTP, 8443 RAW, 24443 A/B, acceptance layers, DNS/MTU/HTTP2/version hypotheses.
- Audit prior reasoning errors; design minimum next experiments (design only).

### Out of scope / not performed
- Fixing EQVPS, mutating servers/clients, purchasing FriendHosting.
- Live SSH/panel health check (would need separate operator-authorized charter).
- Staging/committing/pushing Git.
- Touching foreign WIP outside `projects/mars-server-ops/`.

### Preflight
| Check | Result |
|-------|--------|
| `Get-Location` | `X:\AI MARS` |
| Volume `X:` | **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| Foreign WIP | Present extensively (Website Factory / iSEO / etc.) — **OUT OF SCOPE** |
| Server Ops tree vs HEAD | Entire `projects/mars-server-ops/` appears **untracked** (`git ls-files` count **0**) |
| Unpushed commits on branch | Present (unrelated to this audit; **not** mutated) |

---

## 3. Evidence sources

### Index / reconstruction aid (not unquestioned truth)
- `...\reports\MARS-SERVER-OPS-WEBGPT-HANDOFF-01.md`

### Programme entry
- `...\OPERATIONAL-INDEX.md` — **STALE** vs EQVPS waves (AdminVPS-centric).
- Charter / inventory / secret / backup models under `projects\mars-server-ops\`.

### VEESP / MCA-VPN-001
- `LIVE-INTAKE-EVIDENCE-v1.md`, `SERVER-A-CURRENT-PASSPORT-v1.md`, `CURRENT-STATE-RECONCILIATION-v1.md`, topology / backup / incident / client-compat / legacy WS+nginx handoff.

### EQVPS (23 Git-safe asset reports, 2026-08-27 … 2026-08-29)
- All files under `assets\EQVPS-MICRO-IP\` (intake → bootstrap → firewall → port gate → DNS → ingress → Goodline XHTTP → client/forensic waves → RAW 8443 → full-transfer → 24443 → operator runbook).

### AdminVPS / Server B (context only)
- Phase 3E3 final verdict, direct gate, AdminVPS support pack, architecture freeze.

### Local contour (structure / pointers; secrets not exposed)
- `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\` — backups, raw evidence bundles referenced by reports, `secrets.local.md` / `operator-access.local.md` / `ssh\` → **[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]**.

### Storage
- `X:\AI MARS STORAGE\` exists; programme root `mars-server-ops\` **ABSENT** (per handoff; not re-created here).

### Root `OPERATIONAL-INDEX.md`
- **ABSENT** at repo root (programme index under Server Ops only).

---

## 4. Evidence quality / limitations

| Strength | Limitation |
|----------|------------|
| Multiple dated REPORT waves with backups/SHA256 | Programme tree currently **untracked** in Git — durability depends on disk + operator commit later |
| Isolated Xray tests separate from v2rayN DB | Real-app TUN results largely **operator-pending / not filed** |
| Client runtime JSON captures for VEESP | VEESP **server** intake is **4 days older** than EQVPS RAW waves |
| Explicit classification of layers in later reports | Early waves overstated “PRODUCTION STABLE” for XHTTP |
| Hetzner path **observed** in traceroute/DNS | Corporate ownership / ASN formal claim **UNPROVEN** in markdown |
| Local raw dirs referenced | Some local paths are cursorignore-filtered; audit relies on Git-safe reports + handoff metadata listing |

**Rule applied:** later reproducible operational evidence > narrative; a later REPORT that only repeats an assumption does not win.

---

## 5. VEESP canonical control model

### Identity (FACT)
| Field | Value | Evidence |
|-------|-------|----------|
| Asset | MCA-VPN-001 / Server A | passport / intake |
| Provider | VEESP (legacy/live label; panel not re-checked at intake) | passport |
| Domain | `wsp-cloud.com` | passport |
| IPv4 | `178.173.250.69` | EQVPS comparison reports (Git passport redacts as `<SERVER_IP>`) |
| OS | Ubuntu 22.04.5 LTS | live intake 2026-08-25 |
| Role | Production control VPN — **do not mutate** without charter | programme doctrine |

### Server-side intake 2026-08-25 (FACT)
| Item | Value |
|------|-------|
| Xray | **26.6.22** |
| 3X-UI semver | **SAFE UNKNOWN** (CLI did not return semver; legacy claim 3.4.1) |
| Panel | HTTPS `:5928` |
| Subscription listener | `:2096` |
| Inbound `:8443` | VLESS + TLS + **WebSocket** (`MCA-Gate-TLS`) |
| Inbound `:46489` | VLESS + Reality (`MCA-Gate-Reality`) |
| nginx | **not installed** / not in path |
| ufw | **inactive** |
| fail2ban | active (sshd) |
| Cert | LE under `/root/cert/wsp-cloud.com/`, expires 2026-11-11 |

### Client/control profile used during EQVPS waves 2026-08-28/29 (FACT as client runtime)
| Item | Value |
|------|-------|
| Profile remark | `MCA-Gate-TLS-MCA-ONE` |
| Address/port | `wsp-cloud.com:8443` |
| Transport | **RAW / tcp** |
| Security | TLS |
| ALPN | `http/1.1` |
| Fingerprint | chrome |
| Flow | empty |
| Mux | disabled |
| TUN | present (mixed `:10808` + TUN + api) |
| Operator-attested apps | ChatGPT / YouTube / Google / TUN used as working control |

### CONTRADICTION — transport class
| Source | Claim |
|--------|-------|
| Server intake 2026-08-25 | `:8443` = **WebSocket** |
| Client runtime 2026-08-28/29 | `:8443` = **RAW** |

**Canonical audit stance:** treat VEESP as **operator-working control**. Treat **current server-side** transport as **REQUIRES LIVE READ-ONLY RECONCILE**. Do **not** silently assume server was mutated to RAW.

### Application acceptance (VEESP)
| Layer | Status | Class |
|-------|--------|-------|
| Operator working path | Attested in EQVPS RAW control report | FACT as attestation |
| Fresh formal matrix in this audit | **NOT RE-RUN** | UNPROVEN for “fresh PASS” |

---

## 6. EQVPS canonical current model

### Identity (FACT)
| Field | Value |
|-------|-------|
| Provider label | EQVPS Micro-IP |
| Path observation | Consistent with **Hetzner Helsinki** infra (traceroute/DNS) — ownership not claimed |
| Location | Helsinki |
| IPv4 | `95.216.126.173` |
| Domain | `metacode-cloud.com` |
| OS | Ubuntu **24.04.4** LTS |
| 3X-UI | **3.7.0** |
| Xray | **26.7.28** |
| nginx in VPN path | **No** |

### Current inbounds (FACT — as of 2026-08-29 reports + runbook)

| Remark | Port | Role | Transport | Security | SNI | ALPN | Flow | Mux | Cert |
|--------|------|------|-----------|----------|-----|------|------|-----|------|
| `EQVPS-TLS-RAW-8443` | 8443 | **Production candidate** | RAW/tcp | TLS | metacode-cloud.com | http/1.1 | empty | disabled | LE metacode-cloud.com |
| `EQVPS-TLS-XHTTP-PRIMARY-443` | 443 | **Deferred / experimental** | XHTTP | TLS | metacode-cloud.com | (XHTTP era used h2+http/1.1 in client probes) | empty | disabled | same LE |
| `EQVPS-TLS-RAW-24443-AB` | 24443 | **A/B test** (not production fleet) | RAW/tcp | TLS | metacode-cloud.com | http/1.1 | empty | sniffing cloned from 8443 | same LE |

### Fleet (FACT)
- Six production RAW clients on `:8443` (`{Device}-RAW-8443`).
- One technical XHTTP test client on `:443` (`MARS-XHTTP-443-TEST`).
- One A/B client on `:24443` (`MCA-ONE-RAW-24443-AB`).
- Reality production ingress: **withdrawn**.

### Panel / management (FACT)
- Public panel HTTPS `:20901`, subscription `:2096` (paths secret-local).
- UFW allows 22 / 443 / 8443 / 20901 / 2096 / **24443** (24443 added for A/B).

### Material match to VEESP *client* profile (INFERENCE from reports)
On paper, EQVPS RAW `:8443` was deliberately field-matched to VEESP client RAW profile (port, VLESS, TLS, ALPN http/1.1, chrome FP, empty flow, mux off). **Expected differences:** domain, IP, UUID, server OS, Xray version, panel version, firewall posture.

---

## 7. Windows client canonical model

| Element | Evidenced value | Class |
|---------|-----------------|-------|
| OS | Windows 10 (operator workstation) | FACT (task / reports) |
| v2rayN | **7.22.3 x64** | FACT |
| Install root observed | `C:\Program Files\v2rayN\` | FACT |
| Xray (later RAW waves) | **26.7.28** under Program Files bin | FACT |
| Xray (some Aug 28 forensics) | **26.5.9** under LocalAppData probe path | FACT — note dual-path history |
| TUN | Wintun present in VEESP sessions | FACT |
| Mixed proxy | `127.0.0.1:10808` | FACT |
| MTU Ethernet | 1500 | FACT (full-transfer wave) |
| Routing shell (VEESP working) | `.ru` / category-ru / geoip:ru → direct; private → direct; UDP/443 → block; catch-all → proxy | FACT (differential report) |
| DNS shell (VEESP) | multi-server DoH; **VPN hostname** in `direct-dns-1` domains | FACT |

### Shared vs node-specific
| Shared (intended) | Node-specific |
|-------------------|---------------|
| Same PC, v2rayN, often same core, same TUN/MTU/routing *shell* | Active outbound host/port/transport/SNI/UUID; DNS exemption hostname must match **active** endpoint |

### Uncontrolled client variables flagged
1. **Wrong active profile** historically caused false EQVPS FAIL while VEESP runtime was active (runtime JSON diff).  
2. Custom configs temporarily diverged (v1 no DNS/TUN vs v2 full shell).  
3. Isolated probes used `:18088` / `:18089` — **not** identical to v2rayN `:10808` path.  
4. Operator remained on VEESP TUN during many server-side validations — correct for safety, but means app hangs were **not** reproduced in those sessions.

**Rule:** `.ru` sites are **invalid VPN egress proof** under this routing.

---

## 8. VEESP vs EQVPS configuration difference matrix

| Variable | VEESP | EQVPS | Classification |
|----------|-------|-------|----------------|
| Provider | VEESP | EQVPS Micro-IP | **MATERIAL** (under test) |
| Country / DC | SAFE UNKNOWN / NL research claims | Helsinki / Hetzner path observed | **MATERIAL** / path UNKNOWN detail |
| IPv4 | 178.173.250.69 | 95.216.126.173 | **MATERIAL** |
| Domain / SNI | wsp-cloud.com | metacode-cloud.com | **EXPECTED** (own identity) — **LIKELY IRRELEVANT** if TLS correct |
| Ubuntu | 22.04.5 | 24.04.4 | **POSSIBLY MATERIAL** |
| 3X-UI | SAFE UNKNOWN (~legacy 3.4.1) | 3.7.0 | **POSSIBLY MATERIAL** |
| Xray server | **26.6.22** | **26.7.28** | **POSSIBLY MATERIAL** (interaction class) |
| Client Xray | 26.7.28 (RAW waves) | same when testing EQVPS | **HELD** when same session |
| VLESS | yes | yes | MATCH |
| Flow | empty (client) | empty | MATCH |
| Transport (client claim) | RAW | RAW `:8443` | MATCH (client) |
| Transport (server intake) | **WS** (Aug 25) | RAW (Aug 29) | **MATERIAL UNKNOWN** until VEESP live reconcile |
| TLS | yes / LE | yes / LE | MATCH family |
| ALPN (client RAW) | http/1.1 | http/1.1 | MATCH |
| Port production | 8443 | 8443 | MATCH |
| Mux | disabled | disabled | MATCH |
| Sniffing | not deeply compared | cloned 8443→24443 | UNKNOWN detail |
| Routing (server) | NOT CHECKED live | NOT deeply exported in Git | UNKNOWN |
| DNS (server) | NOT CHECKED | systemd-resolved + Hetzner-range uplink | POSSIBLY MATERIAL |
| nginx | absent | absent | MATCH (absence) |
| Firewall | ufw inactive | UFW active (allowlist) | **POSSIBLY MATERIAL** (but ports proven open) |
| fail2ban | sshd | sshd | LIKELY IRRELEVANT to app hangs |
| IPv6 | present on VEESP eth0 | UFW IPv6 rules exist | UNKNOWN impact |
| MTU | not fully profiled | eth0 1500; client Ethernet 1500 | LIKELY IRRELEVANT as simple mismatch |
| Client profile | MCA-Gate-TLS-MCA-ONE | MCA-ONE-RAW-8443 | EXPECTED difference |
| TUN / Wintun / MTU 1500 | used | intended same | HELD when operator follows runbook |
| UDP/443 block | yes | yes (when VEESP shell used) | HELD |

**Count summary (this matrix):**  
- Compared rows: **28**  
- **MATERIAL** or **MATERIAL UNKNOWN**: **6** (provider, IP/path, OS, Xray version, unresolved VEESP server transport, possibly 3X-UI)  
- **POSSIBLY MATERIAL:** several (firewall posture, DNS uplink, kernel defaults)  
- **LIKELY IRRELEVANT / MATCH / HELD:** majority of VLESS field matches and client stack when controlled  

---

## 9. 443 / XHTTP reconciliation

| Topic | Finding | Class |
|-------|---------|-------|
| Why introduced | Reality `:443` FAIL on Goodline (`received real certificate`); need TLS path that already worked on `:8443` XHTTP | FACT |
| Architecture | VLESS + TLS + XHTTP; TLS in **Xray**; LE cert; **no nginx** | FACT |
| Early outcome | `XHTTP_443_PRIMARY_PASS` (2026-08-28 Goodline stabilization) | FACT (historical) |
| Client chase | Padding / import / Custom v1–v2; multiple false leads | FACT |
| Current status | **DEFERRED / NON-PRODUCTION**; one technical test client retained | FACT (runbook + cleanup) |
| Docs still implying current | `current-ingress-baseline-2026-08-28.md`, restore runbook baseline text | **STALE** |

**Final state label:** **SUPERSEDED as production path** · **RETAINED FOR TESTING** (443 inbound still listening) · **not CURRENT production candidate**.

---

## 10. 8443 RAW/TLS reconciliation

Layer verdicts for EQVPS `:8443` RAW (evidence-dated 2026-08-29 unless noted):

| Layer | Verdict | Evidence |
|-------|---------|----------|
| A. Listener/socket | **PASS** | listeners present; UFW allow |
| B. TLS | **PASS** | OpenSSL verify return 0 |
| C. Certificate | **PASS** | LE CN/SAN metacode-cloud.com |
| D. Xray inbound | **PASS** | runtime tcp+tls; remark EQVPS-TLS-RAW-8443 |
| E. Isolated client | **PASS** | `:18088` ipify/Google/YouTube |
| F. Egress | **PASS** | ipify → 95.216.126.173 |
| G. Large transfers | **PASS** | CF 1MB/10MB; YT/ChatGPT bodies |
| H. Windows explicit proxy `:10808` | **NOT TESTED** (proposed next; not filed for RAW) | full-transfer §13 |
| I. Windows TUN | **UNKNOWN / symptom reports** | hang class inferred; no filed PASS matrix |
| J. Browser real workload | **UNKNOWN / historically UNSTABLE reports** | not formalized PASS |
| K. ChatGPT real workload | **NOT TESTED** as prompt PASS | body transfer ≠ prompt |
| L. Cursor real workload | **NOT TESTED** as sustained Agent PASS | pending |
| M. YouTube playback | **NOT TESTED** | HTTP body ≠ playback |

**TRANSPORT HEALTH:** **PASS**  
**REAL APPLICATION ACCEPTANCE:** **NOT ACCEPTED / UNPROVEN**  
**PRODUCTION ACCEPTANCE:** **NO**

This matches the expected distinction in the audit charter — and is **supported**, not forced.

---

## 11. 24443 A/B reconciliation

| Question | Answer |
|----------|--------|
| Why created | Port A/B for middlebox / port-specific app hangs vs common factors |
| Diff vs 8443 | **Port only** (+ new inbound/client/UFW); stream/TLS/ALPN/FP/flow/sniffing cloned |
| Isolated result | **RAW_24443_LOCAL_PASS** (egress, YT body, CF 1/10 MB) |
| TCP A/B | 8443 25/25; 24443 25/25; VEESP 25/25 — **no connect anomaly** |
| Operator Cursor/Firefox | **WAITING** in report — **not filed in MARS** |
| ChatGPT/YouTube playback | **NOT TESTED** in MARS for 24443 TUN |

### About “8443 FAIL → 24443 PASS”
| Claim | Audit status |
|-------|--------------|
| Recorded as MARS PASS | **No** |
| Later invalidated in MARS | **No record** (nothing to supersede) |
| Chat-derived narrative | **UNVERIFIED** |

**If** an operator later saw a transient Cursor success, it must be filed with duration/quality before any PASS label. Current forensic stance: **insufficient evidence**; treating early PASS reasoning as **premature** (HYPOTHESIS risk), not as a MARS SUPERSEDED VERDICT.

**Current inbound state:** present for testing; **not** production fleet path.

---

## 12. Canonical application acceptance matrix

Legend: PASS / FAIL / UNSTABLE / UNKNOWN / NOT TESTED  

Sources keyed:  
V = VEESP operator attestation / client runtime · E8 = RAW 8443 isolated · E8f = full-transfer · E24 = 24443 report · R = runbook pending  

| Test | VEESP :8443 | EQVPS :8443 | EQVPS :24443 |
|------|-------------|-------------|--------------|
| api.ipify | PASS (attested egress 178.173.250.69) V | PASS E8/E8f | PASS E24 |
| ordinary HTTPS | PASS V | PASS E8 | PASS E24 (YT 200) |
| repeated TCP | PASS V (working path) | PASS E24 (25/25) | PASS E24 (25/25) |
| 1 MB body | UNKNOWN (not formalized) | PASS E8f | PASS E24 |
| 10 MB body | UNKNOWN | PASS E8f | PASS E24 |
| YouTube HTTP/full-body | UNKNOWN | PASS E8f | PASS E24 |
| YouTube homepage (browser) | PASS V (attested) | UNKNOWN / hang reports | NOT TESTED |
| YouTube actual playback | PASS V (attested) | NOT TESTED | NOT TESTED |
| ChatGPT homepage | PASS V | UNKNOWN / hang reports | NOT TESTED |
| ChatGPT login | UNKNOWN | NOT TESTED | NOT TESTED |
| ChatGPT actual prompt | PASS V (attested) | NOT TESTED | NOT TESTED |
| Facebook | UNKNOWN | NOT TESTED | NOT TESTED |
| Cursor simple request | PASS V (attested) | NOT TESTED | NOT TESTED (waiting) |
| Cursor sustained Agent | PASS V (attested) | NOT TESTED | NOT TESTED |
| Telegram | UNKNOWN | NOT TESTED | NOT TESTED |
| normal browser web | PASS V | UNKNOWN | NOT TESTED |

**Do not infer** missing app cells from curl PASS.

---

## 13. Browser / explicit-proxy findings

| Mode | What evidence shows |
|------|---------------------|
| TUN | VEESP TUN works as control. EQVPS TUN real-app **not proven PASS**; hang class reported/inferred. |
| HTTP proxy `:10808` | Custom v1 (XHTTP era): Google/YouTube **PASS** with egress EQVPS. Custom v2: FAIL (DNS deadlock). RAW era: `:10808` full-body compare **proposed, not filed**. |
| SOCKS vs HTTP | Mixed inbound documented; no separate SOCKS-only matrix. |

**Does explicit proxy evidence weaken “TUN itself is root cause”?**  
- **XHTTP-era Custom v1:** yes — explicit proxy worked without TUN → weakens TUN-global theory (**INFERENCE**, strong for that era).  
- **RAW-era:** **UNPROVEN** — the discriminating `:10808` vs `:18088` test was not evidenced as completed.  
- **VEESP TUN works:** rejects “TUN broken globally” (**FACT**).

**Conclusion class:** TUN-global broken = **REJECTED**. TUN/path-specific for EQVPS RAW = **STILL PLAUSIBLE / UNPROVEN**. Explicit-proxy falsification for RAW = **NOT YET DONE**.

---

## 14. DNS findings

| Item | Status |
|------|--------|
| v2rayN DNS mode (VEESP shell) | Multi-server DoH + tagged routing; VPN hostname exempt via `direct-dns-1` | FACT |
| Custom v2 bug | Stale `wsp-cloud.com` exemption → metacode DNS via proxy → deadlock | FACT |
| Custom v2.1 fix | Replace exemption with `metacode-cloud.com` → isolated PASS | FACT |
| Explains all RAW TUN hangs? | **No** — isolated RAW without that DNS shell also PASS; remaining hang class after RAW cutover still open | INFERENCE |
| DNS as sole current root | **NOT REJECTED**, but **not sole**; residual DNS/split issues **STILL PLAUSIBLE** under TUN | HYPOTHESIS |
| Hostnames resolving in browser under EQVPS TUN | Insufficient filed evidence | UNPROVEN |

**DNS REJECTED?** **No** — insufficient to reject residual DNS/split contributions under TUN.

---

## 15. MTU / PMTU findings

| Evidence | Result |
|----------|--------|
| Client Ethernet MTU | 1500 |
| EQVPS eth0 MTU | 1500 |
| DF probes 500–1472 | success; approx PMTU 1500 |
| Isolated 10 MB transfer | completes multi-MB/s despite some retrans counters |

**Simple local MTU mismatch / classic blackhole:** **REJECTED**  
**Complex path PMTU / loss under long-lived app flows:** **STILL PLAUSIBLE / WEAK** (retrans seen; transfers still completed in isolation)  
**Overall MTU hypothesis for “explains app hangs alone”:** **WEAK**

---

## 16. HTTP/2 compatibility findings

| Item | Status |
|------|--------|
| curl `--http2` on operator Windows | **SKIPPED** (unsupported in that wave) | FACT |
| Cursor HTTP/2 vs HTTP Compatibility Mode | Not found as a completed, filed A/B with PASS/FAIL in Git-safe corpus | UNPROVEN |
| HTTP/2-only root-cause theory | **WEAK / UNPROVEN** — cannot survive as primary without evidence |

**Current status:** **UNPROVEN**; do not treat as resolved or rejected.

---

## 17. Xray / v2rayN version findings

| Hypothesis | Assessment |
|------------|------------|
| Client-global Xray 26.7.28 regression | **WEAK / largely REJECTED** — same client works on VEESP control |
| Client-global v2rayN 7.22.3 regression | **WEAK** as global — VEESP works on same GUI |
| Server-version-specific interaction (26.6.22 vs 26.7.28) | **STILL PLAUSIBLE / UNPROVEN** — not falsified by VEESP success |
| Isolated EQVPS with client 26.7.28 | **PASS** — rejects “26.7.28 cannot speak to EQVPS RAW at all” |

**What VEESP success falsifies:** “this Windows stack cannot do VLESS/TLS/TUN at all.”  
**What it does not falsify:** EQVPS-specific profile serialization, DNS shell retarget, path/ASN/CDN behaviour, or server 26.7.28 quirks under long-lived app protocols.

---

## 18. Server-side architecture audit

Actively searched for config mistakes before provider blame:

| Area | Finding |
|------|---------|
| Bind/listen | Present on intended ports | FACT |
| Protocol/TLS/ALPN/SNI | Consistent with RAW cutover reports | FACT |
| Cert validity | verify 0; LE identity match | FACT |
| nginx | Absent — not a dual-terminator confusion for current RAW | FACT |
| Duplicate listeners | Not evidenced as conflict | — |
| Stale XHTTP on 8443 | Superseded by RAW mutation | FACT |
| Reality remnants | Withdrawn from production; orphan client cleaned | FACT |
| UI vs runtime | Post-mutation alignment documented for 443/8443 | FACT |
| Historical Reality flow mismatch | DB Vision vs generated null — contributed to Reality FAIL | FACT (historical) |
| Firewall | Ports allowed; direct Goodline TCP PASS | FACT |
| Proven current RAW misconfig explaining TUN app hangs | **None found in evidence** | FACT (absence) |

**Goal result:** no overlooked **proven** server RAW misconfiguration that replaces the need for client-path / provider discrimination. Historical client config errors **were** real and must not be forgotten.

---

## 19. Provider / IP / ASN / path hypothesis assessment

| Hypothesis | Support | Contradict | Missing | Confidence |
|------------|---------|------------|---------|------------|
| EQVPS provider quality | App symptoms reported; second node needed | Isolated transfers PASS | Formal SLA/abuse data | **LOW** |
| Hetzner HEL infra | Traceroute/DNS observations | Transfers PASS; no active incident on 2026-08-29 | Ownership claim | **LOW–MEDIUM** (infra presence MEDIUM; blame LOW) |
| IP reputation | None solid in Git | — | RBLs, abuse mail | **LOW** |
| ASN AS24940 | External claim | Not strongly in EQVPS md | WHOIS capture in Git | **LOW** |
| Goodline↔Hetzner path | Reality MITM-class FAIL; AdminVPS direct FAIL history; EQVPS retrans under load | EQVPS direct TCP 22/443/8443 PASS; isolated HTTPS PASS | App-layer path traces | **MEDIUM** as *class*, **LOW** as proven root |
| App/CDN/backend behaviour | Differential symptoms plausible | Incomplete matrix | Filed Cursor/YT/ChatGPT matrix | **MEDIUM** (leading unproven class) |

**PROVEN ROOT CAUSE:** **none**.

---

## 20. Hetzner incident assessment

| Question | Classification |
|----------|----------------|
| **INCIDENT EXISTENCE** (FRA–HEL backbone fault ~2026-08-21; updates ~2026-08-23; NBG1–FRA maintenance completed 2026-08-28) | **FACT** *as recorded research notes* in 24443 report — original status-page captures not inventoried in Git-safe tree |
| Active incident at 24443 provisioning (2026-08-29) | **None identified** (FACT as report) |
| **CAUSAL CONNECTION TO EQVPS app hangs** | **UNPROVEN** |
| Explains 8443 vs 24443 | **No** (TCP A/B identical) |

Temporal correlation ≠ causation.

---

## 21. FriendHosting experiment design review

**Status in MARS:** **NOT DOCUMENTED** as approved charter; **no** preflight metrics in programme tree/Storage.

### Intended design (operator-provided logic — experiment design only)
Germany / Frankfurt / Telehouse; near-equivalent Ubuntu 24.04 + 3X-UI 3.7.0 + Xray 26.7.28 + VLESS+TLS+RAW; same Windows client/routing/TUN/MTU; acceptance = Cursor sustained / YT playback / ChatGPT prompt / Facebook / transport controls.

### Validity as discriminator
**YES — conditionally valid**, **after** tighter VEESP↔EQVPS controls, because it holds client stack constant while changing provider/path.

### Variables that must be held constant / recorded
- Same v2rayN + Xray versions; same TUN/MTU/routing/DNS exemption retargeted to new hostname; same ALPN/flow/mux/port strategy.  
- Goodline **TUN-OFF** preflight on **assigned** IP (AdminVPS lesson).  
- Explicit `:10808` full-body + TUN real-app matrix.  
- Do **not** treat Looking Glass of a test IP as post-provision proof.  
- Record server Xray/3X-UI exact versions and whether VEESP remains untouched control.

**Do not purchase/provision from this audit alone.**

---

## 22. Previous reasoning errors

| # | What we concluded | Why too strong | What corrected it | New rule |
|---|-------------------|----------------|-------------------|----------|
| 1 | XHTTP padding / Extra JSON is root cause | Single structural diff treated as causal | Runtime showed wrong active profile; padding variants PASS | Confirm **active runtime JSON** before theorizing serialization bugs |
| 2 | Small HEAD/ipify = transport OK for apps | Collapsed layers | Full-transfer wave | Separate TRANSPORT vs REAL APP vs PRODUCTION |
| 3 | “PRODUCTION STABLE” XHTTP dual path | Early Goodline browsing success | Aug 29 RAW candidate + fleet | Date-stamp production claims; prefer later runbook |
| 4 | Copy VEESP routing shell identically | Ignored hostname-bound DNS exemption | v1–v2 differential | Retarget **endpoint-specific** DNS/routing when changing host |
| 5 | TUN is the broken thing (global) | Hangs under TUN | VEESP TUN works; Custom v1 explicit proxy worked | Reject global TUN; test TUN vs `:10808` separately |
| 6 | 24443 better than 8443 (chat) | One anecdote / insufficient reps | MARS: ready-for-test only; TCP A/B identical | No PASS without repeated sustained real-app evidence |
| 7 | Provider/Hetzner is root | Symptom + Helsinki path | Isolated PASS; no causal chain | Falsify config/client controls first |
| 8 | curl YouTube body = playback PASS | Wrong acceptance definition | Explicit layer vocabulary | Playback/prompt/Agent are separate rows |
| 9 | OPERATIONAL-INDEX = current truth | Stale AdminVPS wait state | EQVPS full stack exists | Prefer dated asset reports over stale index |

---

## 23. CONTRADICTIONS

| # | A | B | Canonical reading | Confidence |
|---|---|---|-------------------|------------|
| 1 | Index: wait AdminVPS; no 3X-UI | EQVPS has full stack | Index **STALE** | HIGH |
| 2 | Inventory/domain intent AdminVPS | Domain on EQVPS | EQVPS owns operational domain | HIGH |
| 3 | XHTTP “PRODUCTION STABLE” | RAW production candidate | Prefer Aug 29 runbook | HIGH |
| 4 | VEESP server WS | VEESP client RAW | **LIVE RECONCILE REQUIRED** | MEDIUM–HIGH |
| 5 | Reality primary | Reality withdrawn | Not production | HIGH |
| 6 | Padding = root | Wrong profile + DNS deadlock | Multi-cause evolution | HIGH |
| 7 | Chat: 24443 Cursor PASS | MARS: waiting for operator | UNVERIFIED chat | HIGH (absence) |
| 8 | Restore runbook “current” XHTTP | RAW candidate | Procedure OK; baseline stale | HIGH |

---

## 24. STALE CONCLUSIONS

1. `OPERATIONAL-INDEX.md` next-action = AdminVPS support / no Phase 4A.  
2. `SERVER-INVENTORY` without EQVPS row / AdminVPS as active second-node story.  
3. `EQVPS-MICRO-IP-current-ingress-baseline-2026-08-28.md` as **current** architecture.  
4. XHTTP fleet as production device set.  
5. Ingress restore runbook implied dual-XHTTP production baseline.  
6. Reality as EQVPS production primary.  
7. Assumption Server Ops tree is already on `origin` history (currently untracked on disk).  
8. Any claim that `:10808` RAW full-body was already proven equivalent to `:18088`.

---

## 25. SUPERSEDED VERDICTS

| Verdict | Superseded by |
|---------|---------------|
| UpCloud procurement | AdminVPS decision |
| Reality as EQVPS production primary | Goodline FAIL → XHTTP; Reality remains withdrawn |
| XHTTP 8443 production fallback | RAW 8443 control deployment |
| XHTTP as production fleet path | RAW cleanup + operator runbook |
| “Identical VEESP shell copy” for EQVPS Custom | DNS exemption retarget requirement |
| AdminVPS as DNS target for metacode-cloud.com | EQVPS DNS binding |

**Not a MARS superseded verdict:** “24443 Cursor PASS” — never recorded as PASS here.

---

## 26. UNVERIFIED CLAIMS

1. FriendHosting Looking Glass metrics / Telehouse selection / order state.  
2. AS24940 formal ownership claim for EQVPS IP.  
3. VEESP DC = Amsterdam.  
4. Fresh full VEESP application acceptance matrix.  
5. Cursor PASS on EQVPS 24443 (and any invalidation).  
6. Sustained Cursor Agent PASS on EQVPS RAW 8443.  
7. ChatGPT prompt / YouTube playback PASS on EQVPS via TUN.  
8. Hetzner incident **caused** EQVPS failures.  
9. Exact current VEESP **server** inbound = RAW.  
10. AdminVPS host still paid/alive.  
11. `:10808` RAW full-body results.  
12. Cursor HTTP Compatibility Mode A/B outcome.  
13. Facebook control results on any EQVPS path.

---

## 27. Held-constant / different / unknown variables

### HELD CONSTANT (when operator follows intended RAW A/B)
Windows PC · v2rayN 7.22.3 · client Xray 26.7.28 (RAW waves) · TUN/Wintun · MTU 1500 · RU/direct split · UDP/443 block · catch-all proxy · mux off · flow empty · ALPN http/1.1 · port 8443 · VLESS+TLS  

### DIFFERENT (evidenced)
Provider · IP · ASN/path · domain/SNI/cert identity · Ubuntu major · Xray **server** version · 3X-UI version · ufw posture · panel ports · presence of XHTTP/24443 extras · UUID  

### UNKNOWN / UNRESOLVED
VEESP server transport class now · VEESP 3X-UI semver · server routing/DNS internals both sides · whether operator filed RAW TUN matrix · residual DNS under TUN for EQVPS RAW profile · CDN/app-specific behaviour · FriendHosting existence  

### Before claiming provider/path causation, eliminate or control
1. Live VEESP server inbound = RAW (or document WS still serving with client raw — if that works, record it).  
2. Same client core + routing + DNS exemption hostname for EQVPS.  
3. Filed `:10808` vs `:18088` full-body.  
4. Filed real-app matrix (Cursor sustained, YT playback, ChatGPT prompt) with repetition.  
5. Preferably same server Xray version **or** explicit version A/B.  
6. Only then introduce a third provider (FriendHosting) as path discriminator.

---

## 28. Canonical current facts

1. Server Ops is documentation + chartered human execution — **not** autonomous.  
2. VEESP/`wsp-cloud.com`/`178.173.250.69` is the operator **control** path.  
3. EQVPS/`metacode-cloud.com`/`95.216.126.173` runs Ubuntu 24.04.4 + 3X-UI 3.7.0 + Xray 26.7.28.  
4. EQVPS production **candidate** = VLESS+TLS+RAW `:8443`.  
5. EQVPS XHTTP `:443` = deferred; Reality ≠ production; `:24443` = A/B only.  
6. EQVPS isolated RAW full-transfer = **PASS**.  
7. EQVPS real-app TUN acceptance = **not proven PASS**.  
8. `:24443` not proven better than `:8443`.  
9. Provider/Hetzner root cause = **not proven**.  
10. VEESP↔EQVPS equivalence for provider conclusions = **insufficient**.  
11. Historical client errors (wrong profile; DNS bootstrap) were real.  
12. Programme OPERATIONAL-INDEX is stale relative to EQVPS.  
13. No FriendHosting evidence in MARS.  
14. Secrets remain local — not disclosed in this report.  
15. `projects/mars-server-ops/` currently untracked vs HEAD.

---

## 29. Remaining hypotheses

| ID | Hypothesis | Status |
|----|------------|--------|
| H1 | v2rayN TUN/routing/DNS/split-tunnel specific to EQVPS profile | **LEADING / UNPROVEN** |
| H2 | App/CDN long-lived session behaviour on Goodline↔HEL path | **LEADING / UNPROVEN** |
| H3 | Server Xray 26.7.28 vs VEESP 26.6.22 interaction | **STILL PLAUSIBLE** |
| H4 | Residual DNS under TUN for EQVPS hostname | **STILL PLAUSIBLE** |
| H5 | Provider/IP/ASN quality | **STILL PLAUSIBLE / LOW proof** |
| H6 | Port-specific middlebox (8443 vs 24443) | **WEAK** after TCP A/B; awaits operator app A/B |
| H7 | Simple MTU blackhole | **REJECTED** |
| H8 | TUN globally broken | **REJECTED** |
| H9 | Invalid LE cert / closed port | **REJECTED** for current RAW |
| H10 | HTTP/2-only Cursor issue | **WEAK / UNPROVEN** |
| H11 | Hetzner FRA–HEL incident causation | **UNPROVEN** |

**ROOT CAUSE:** **NOT PROVEN.**

---

## 30. Minimum next experiments

### EXP-A01 — Live read-only VEESP inbound reconcile + EQVPS same-session controls
- **QUESTION:** Is VEESP server `:8443` WS or RAW, and does EQVPS RAW fail the same apps on the same client when VEESP PASS?  
- **HYPOTHESIS:** Unresolved VEESP server transport and missing same-session matrix block provider inference.  
- **CONTROL:** VEESP untouched except read-only; no EQVPS architecture change.  
- **ONE PRIMARY VARIABLE:** Observation/recording of live configs + filed results (not a mutation variable).  
- **PROCEDURE:** Chartered read-only SSH/panel inspect VEESP inbound stream; activate EQVPS `MCA-ONE-RAW-8443`; run `:10808` full-body suite; run browser/Cursor/YT playback/ChatGPT prompt checklist; switch back to VEESP; repeat checklist.  
- **PASS CRITERIA:** Written matrix with dates; VEESP transport class recorded.  
- **FAIL CRITERIA:** Incomplete matrix or config mutate without charter.  
- **MEANS:** Enables or blocks provider-path claims.  
- **DOES NOT PROVE:** FriendHosting outcome; ASN ownership.

### EXP-A02 — `:10808` vs `:18088` full-body differential (EQVPS RAW)
- **QUESTION:** Does v2rayN mixed proxy stall where isolated Xray passes?  
- **HYPOTHESIS:** Defect is inside v2rayN profile/routing/DNS, not server RAW.  
- **CONTROL:** Isolated `:18088` baseline already PASS.  
- **ONE PRIMARY VARIABLE:** Proxy path (v2rayN `:10808` vs standalone).  
- **PROCEDURE:** Same URLs/byte targets as full-transfer wave via both proxies; EQVPS RAW profile active.  
- **PASS/FAIL:** Comparable bytes/times vs stall/timeout.  
- **MEANS:** Localizes to v2rayN vs server.  
- **DOES NOT PROVE:** TUN-specific issues if only `:10808` tested.

### EXP-A03 — Operator 8443 vs 24443 real-app A/B (filed)
- **QUESTION:** Is there port-specific real-app behaviour?  
- **HYPOTHESIS:** Port middlebox (currently weak).  
- **CONTROL:** Same client stack; only profile port/inbound.  
- **ONE PRIMARY VARIABLE:** Destination port 8443 vs 24443.  
- **PROCEDURE:** As in 24443 report operator section; ≥2 repetitions; record duration.  
- **PASS CRITERIA:** Sustained difference replicated.  
- **FAIL CRITERIA:** Identical FAIL/PASS both ports.  
- **MEANS:** Accept/reject port hypothesis.  
- **DOES NOT PROVE:** Provider root cause alone.

### EXP-A04 — DNS exemption / routing shell audit for RAW profile
- **QUESTION:** Does ordinary VLESS import of RAW inherit correct `metacode-cloud.com` DNS exemption under TUN?  
- **HYPOTHESIS:** Residual DNS bootstrap/split issue.  
- **CONTROL:** Capture runtime `config.json` while EQVPS RAW active.  
- **ONE PRIMARY VARIABLE:** Presence/absence of metacode in direct-dns domains.  
- **PROCEDURE:** Activate profile; dump runtime DNS/routing (no secrets); curl ipify; browser tests.  
- **MEANS:** Confirms or clears DNS class for RAW.  
- **DOES NOT PROVE:** CDN behaviour.

### EXP-A05 — FriendHosting near-equivalent control (design only; later charter)
- **QUESTION:** Does an alternate Frankfurt provider path pass the same real-app matrix with the same client stack?  
- **HYPOTHESIS:** Provider/path domain.  
- **CONTROL:** After EXP-A01–A04; VEESP remains control; EQVPS unchanged.  
- **ONE PRIMARY VARIABLE:** Provider/path (hold Xray/UI/client versions).  
- **PROCEDURE:** TUN-OFF preflight on assigned IP → provision equivalent stack → same acceptance matrix.  
- **MEANS:** Strengthens/weakens EQVPS/Hetzner path hypothesis.  
- **DOES NOT PROVE:** Exact ASN mechanism; does not replace A01–A04.

**Preferred order:** A01 → A02 → A04 → A03 → (only then) A05.  
**Count proposed:** **5** high-value experiments (within 3–7).

---

## 31. Recommended next audit wave

**AUDIT 02 (suggested charter title):**  
`FULL SERVER OPS / EQVPS AUDIT 02 — LIVE READ-ONLY RECONCILE + FILED ACCEPTANCE MATRIX`

Contents: execute EXP-A01/A02/A04 under explicit operator approval; update OPERATIONAL-INDEX + SERVER-INVENTORY; decide AdminVPS disposition; decide whether FriendHosting charter is justified; optionally git-commit Server Ops tree as separate wave.

**Do not** start provider-blame or purchase waves before AUDIT 02 evidence.

---

## 32. Evidence path index

### This report
- `X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-EQVPS-AUDIT-01-EVIDENCE-ARCHITECTURE-RECONCILIATION.md`

### Prior handoff
- `X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-WEBGPT-HANDOFF-01.md`

### Programme
- `X:\AI MARS\projects\mars-server-ops\OPERATIONAL-INDEX.md` *(stale)*  
- Charter / inventory / access / secret / backup / change-risk / storage / service-map / VPS selection pack

### MCA-VPN-001
- `...\assets\MCA-VPN-001\LIVE-INTAKE-EVIDENCE-v1.md`  
- `...\SERVER-A-CURRENT-PASSPORT-v1.md`  
- `...\CURRENT-STATE-RECONCILIATION-v1.md`  
- `...\NETWORK-TOPOLOGY-v1.md` · `BACKUP-STATE-v1.md` · `INCIDENT-HISTORY-v1.md` · `CLIENT-COMPATIBILITY-v1.md`  
- `...\legacy\WS-TLS-NGINX-LEGACY-VPN-FULL-HANDOFF.md`

### EQVPS (primary)
- `...\EQVPS-MICRO-IP-operator-client-runbook-v1.md`  
- `...\EQVPS-MICRO-IP-veesp-style-raw-8443-control-deployment-2026-08-29.md`  
- `...\EQVPS-MICRO-IP-raw-full-transfer-and-client-registry-cleanup-2026-08-29.md`  
- `...\EQVPS-MICRO-IP-RAW-24443-port-ab-2026-08-29.md`  
- `...\EQVPS-MICRO-IP-v2rayn-runtime-json-diff-2026-08-28.md`  
- `...\EQVPS-MICRO-IP-v2rayn-v1-v2-differential-root-cause-2026-08-28.md`  
- `...\EQVPS-MICRO-IP-custom-v2-1-endpoint-bootstrap-fix-2026-08-28.md`  
- `...\EQVPS-MICRO-IP-goodline-ingress-stabilization-2026-08-28.md`  
- `...\EQVPS-MICRO-IP-current-ingress-baseline-2026-08-28.md` *(stale as current)*  
- Plus remaining Aug 27–28 intake/bootstrap/firewall/DNS/ingress/client/public-panel/xhttp forensic reports in same folder

### Local (non-secret structure; values not exposed)
- `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\`  
- `...\raw-8443-control-raw-2026-08-29\` · `...\raw-full-transfer-diagnostic-raw-2026-08-29\` · `...\raw-24443-ab-2026-08-29\`  
- `secrets.local.md` / `operator-access.local.md` / `ssh\` — **[LOCAL SECRET EXISTS — VALUE NOT EXPOSED]**

---

## 33. Git / mutation closeout

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| This report created | YES (under `projects/mars-server-ops/reports/`) |
| Server Ops tree tracking | Appears **fully untracked** vs HEAD |
| Foreign WIP | Untouched |
| Staged by this task | **NONE** |
| Commit | **NOT DONE** |
| Push | **NOT DONE** |
| Server mutation | **0** |
| Client mutation | **0** |
| Secret disclosure | **0** |
| Live remote verification | **NOT PERFORMED** |
| Experiments executed | **0** (design only) |

**Git mutation = 0 · Server mutation = 0 · Client mutation = 0 · Secret disclosure = 0**

---

*End of REPORT — AUDIT 01 · DISPROVE ASSUMPTIONS BEFORE BLAMING THE PROVIDER · CURRENT TRUTH OVER HISTORICAL CONVENIENCE.*

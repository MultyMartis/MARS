# EQVPS-MICRO-IP — DNS Binding + Ingress Architecture

**Date:** 2026-08-27 (operator local / wave closeout 2026-08-28 Asia/Bangkok)  
**Wave:** MARS Server Ops — EQVPS-MICRO-IP DNS binding verification + ingress architecture decision  
**Asset:** EQVPS Micro-IP (`metacode-cloud`) · public IPv4 `95.216.126.173`  
**Domain:** `metacode-cloud.com` (registrar / DNS: Beget)  
**Verdict:** **READY_FOR_INGRESS_DEPLOYMENT**

**This wave is documentation / verification / architecture only.**

| Forbidden in this wave | Status |
|------------------------|--------|
| Xray / 3X-UI / nginx / Docker / certbot install | **NOT DONE** |
| Certificate issuance | **NOT DONE** |
| UFW / fail2ban / SSH mutation | **NOT DONE** |
| Beget DNS mutation / PTR / hostname change | **NOT DONE** |
| Persistent listeners / open 80/443/8443 | **NOT DONE** |
| Reboot / apt update/upgrade/install | **NOT DONE** |
| Server A / AdminVPS mutation | **NOT DONE** |
| Git commit | **NOT DONE** |

**Companion charter (NEXT phase only — not executed):**  
[EQVPS-MICRO-IP-ingress-deployment-charter-v1.md](./EQVPS-MICRO-IP-ingress-deployment-charter-v1.md)

**Raw DNS evidence (gitignored / local):**  
`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\dns-architecture-raw-2026-08-27\`

**Prior EQVPS evidence:**

- [read-only intake](./EQVPS-MICRO-IP-read-only-intake-2026-08-27.md)
- [SSH bootstrap](./EQVPS-MICRO-IP-controlled-ssh-bootstrap-2026-08-27.md)
- [base OS security + firewall](./EQVPS-MICRO-IP-base-os-security-firewall-2026-08-27.md)
- [controlled reboot + direct port gate](./EQVPS-MICRO-IP-controlled-reboot-direct-port-gate-2026-08-27.md)

---

## 1. Verdict criteria checklist

| Criterion | Result |
|-----------|--------|
| Authoritative A: `metacode-cloud.com` → `95.216.126.173` | **PASS** |
| Authoritative A: `www.metacode-cloud.com` → `95.216.126.173` | **PASS** |
| No conflicting A / unexpected AAAA that blocks deploy | **PASS** |
| Public recursive propagation sufficiently confirmed | **PASS** (`DNS_PROPAGATION=PASS`) |
| EQVPS resolves apex + www to self IPv4 | **PASS** |
| Hostname remains `metacode-cloud` | **PASS** |
| Primary ingress architecture selected | **PASS** |
| Fallback architecture selected | **PASS** |
| Port map selected | **PASS** |
| Panel model selected | **PASS** |
| Certificate strategy selected | **PASS** |
| Rollback requirements defined | **PASS** |
| Remote application mutations this wave | **0** |

**Verdict:** **READY_FOR_INGRESS_DEPLOYMENT**

---

## 2. Phase A — Authoritative DNS

### Nameservers (NS)

| Host | Role |
|------|------|
| `ns1.beget.com` | Authoritative (SOA primary) |
| `ns2.beget.com` | Authoritative |
| `ns1.beget.pro` | Authoritative |
| `ns2.beget.pro` | Authoritative |

SOA (via recursive NS lookup): primary `ns1.beget.com`, hostmaster `hostmaster.beget.com`, serial `1787850014`, TTL observed **300**.

### Authoritative A answers

Queried **directly** against all four Beget NS (`Resolve-DnsName … -Server <ns> -DnsOnly`):

| Name | Type | Answer | TTL | Consistency |
|------|------|--------|-----|-------------|
| `metacode-cloud.com` | A | `95.216.126.173` | 300 | Identical on all 4 NS |
| `www.metacode-cloud.com` | A | `95.216.126.173` | 300 | Identical on all 4 NS |

### AAAA

| Name | Authoritative AAAA |
|------|--------------------|
| apex | **NONE observed** (empty answers from all 4 NS) |
| www | **NONE observed** |

### Mail-related records (observed, intentionally unchanged)

Read-only observation against `ns1.beget.com` (not mutated):

| Record class | State |
|--------------|-------|
| MX | **PRESENT** (Beget mail) — leave unchanged |
| TXT / SPF | **PRESENT** (Beget) — leave unchanged |
| `autoconfig` CNAME | **PRESENT** — leave unchanged |
| `autodiscover` CNAME | **PRESENT** — leave unchanged |

**Conflicting A records:** **NONE** → not `BLOCKED_FOR_DEPLOYMENT`.

---

## 3. Phase B — Public recursive DNS

| Resolver | apex A | www A | Notes |
|----------|--------|-------|-------|
| System (Windows) | `95.216.126.173` | `95.216.126.173` | TTL observed **600** (cache/resolver view) |
| `1.1.1.1` | `95.216.126.173` | `95.216.126.173` | TTL ~299 |
| `8.8.8.8` | `95.216.126.173` | `95.216.126.173` | TTL ~299 |
| `nslookup` cross-check | same | same | Confirms recursive answers |

**DNS_PROPAGATION = PASS**

No partial/stale conflicting answers observed on the queried resolvers.

---

## 4. Phase C — EQVPS server-side DNS

Access: `marsops` @ `95.216.126.173:22` with dedicated Ed25519 key (path under local secret contour; **no secrets in this file**).

| Check | Result |
|-------|--------|
| `hostname` / `hostnamectl --static` | `metacode-cloud` |
| `getent ahostsv4 metacode-cloud.com` | `95.216.126.173` |
| `getent ahostsv4 www.metacode-cloud.com` | `95.216.126.173` |
| `resolvectl query metacode-cloud.com` | `95.216.126.173` (eth0) |
| `resolvectl query www.metacode-cloud.com` | `95.216.126.173` (eth0) |
| Listeners on 443 / 8443 | **NONE** (only `:22`) |
| Hostname change | **NOT PERFORMED** |

`sudo ufw status` required password in this non-interactive session; UFW baseline reused from prior wave evidence (**active**, inbound **22/tcp only**).

---

## 5. Phase D — Domain / port relationship

| Fact | Classification |
|------|----------------|
| Prior Goodline TUN-OFF `DIRECT_22` | **PASS** (prior wave) |
| Prior Goodline TUN-OFF `DIRECT_443` | **PASS** (prior wave) |
| Prior Goodline TUN-OFF `DIRECT_8443` | **PASS** (prior wave) |
| Temp listeners / temp UFW | **CLEANED** in prior wave |
| HTTP/HTTPS expected to work now | **NO** — no app listener; UFW still 22-only |
| Re-open 443/8443 for this wave | **NOT DONE** (evidence not stale for architecture) |

---

## 6. Phase E — MARS architecture research (read-only)

### Server A (MCA-VPN-001) — production control evidence

Sources: `SERVER-A-CURRENT-PASSPORT-v1.md`, live intake, network topology.

| Item | Live / documented fact |
|------|------------------------|
| Domain | `wsp-cloud.com` (independent from EQVPS) |
| Stack | 3X-UI native + Xray; **nginx absent** |
| Working operator path | VLESS + TLS + WebSocket on **TCP/8443** |
| Reality | Listener **PRESENT** on high port (`46489`); client connectivity **NOT VERIFIED** |
| Panel | HTTPS on high port **5928** (public) |
| Subscription | Listener **2096** (public) |
| UFW | **inactive** on A (weaker than EQVPS baseline) |
| Mutation this wave | **NONE** |

### AdminVPS Server B — contrast

| Item | Fact |
|------|------|
| Direct Goodline path to assigned IP | **FAILED** (Phase 3E / 3E3) — IP rejected for direct entry |
| Host health | **PASS**; SSH via existing VPN path worked |
| App stack | **NOT installed** |
| Historical planning hostname/domain intent | `metacode-cloud.com` appeared in Server B planning |
| Current public DNS for `metacode-cloud.com` | Now authoritative to **EQVPS** `95.216.126.173` |

**Residual note:** AdminVPS Server B is **not** the current public DNS target for this domain. Do not mutate AdminVPS or Server A in the next ingress wave unless separately chartered.

### Architecture Freeze v1 (Server B planning) — relevant decisions reused by analogy

| Freeze item | Stance for EQVPS |
|-------------|------------------|
| nginx initial | **NOT REQUIRED** unless later charter proves need |
| 3X-UI native / systemd | **RETAIN** |
| Docker for core VPN | **NOT REQUIRED** |
| Reality classification | Not deprecated; validate independently |
| Initial WS preference | **SUPERSEDED as primary** for EQVPS by 2026 anti-DPI dual-stack decision below — retained as **compatibility alternate** inside TLS fallback family |

---

## 7. Phase F — Ingress architecture decision (2026)

### Evaluated families

| ID | Family | Decision |
|----|--------|----------|
| A | VLESS + REALITY on TCP/443 alone | Rejected as sole long-term design |
| B | VLESS + TLS + XHTTP on TCP/443 alone | Rejected as sole design |
| C | VLESS + TLS + WebSocket on 443/8443 alone | Rejected as sole primary (still useful as compatibility path) |
| D | **REALITY primary + TLS/XHTTP fallback** | **SELECTED** |
| E | Other (gRPC-only, Hysteria, sing-box, etc.) | **NOT selected** — insufficient MARS operational evidence for first EQVPS production cut |

### Selected design (family D)

| Role | Transport | Port | Notes |
|------|-----------|------|-------|
| **PRIMARY** | **VLESS + REALITY** (+ Vision if supported by chosen Xray/3X-UI at install time) | **TCP/443** | Anti-DPI first line; blends with HTTPS; proven direct reachability on this IP |
| **FALLBACK** | **VLESS + TLS + XHTTP** | **TCP/8443** | Modern TLS transport; uses real cert for `metacode-cloud.com` |
| **COMPATIBILITY ALTERNATE** (only if XHTTP client friction) | VLESS + TLS + WebSocket | **TCP/8443** (same fallback port; not simultaneous conflicting inbounds without redesign) | Operator-proven on Server A; use only if XHTTP fails client validation |

### Why

1. **Russian DPI / filtering reality (2026):** Reality remains the stronger *initial* public camouflage strategy versus bare WS fingerprinting; EQVPS already has **DIRECT_443=PASS** from operator Goodline.
2. **Proven path diversity:** Direct **443** and **8443** both PASS — enables primary/fallback without inventing exotic ports.
3. **Do not rely on Reality forever:** TLS+XHTTP fallback provides a managed second path using the newly bound domain.
4. **Do not freeze on legacy WS:** Server A WS works, but EQVPS should prefer XHTTP for new TLS ingress; WS remains documented compatibility escape hatch.
5. **nginx:** Not required for first production — Server A proves Xray can terminate TLS/WS without nginx; Reality needs no local website. Add nginx only under a later charter if a real public site or advanced masking is required.
6. **Operational simplicity:** One panel (3X-UI), two client profiles (primary/fallback), manual profile switch (same as Architecture Freeze client strategy).
7. **Changeability:** Transports are inbound configs — can be altered without rebuilding the VPS if backup/restore of 3X-UI DB + Xray config is disciplined.

### Explicit non-goals for first ingress deploy

- Automatic multi-hop / balancer failover  
- Public marketing website on this host  
- Semantic DNS (`vpn.*`, `proxy.*`, `xray.*`)  
- Cloning Server A panel/subscription public exposure model  

---

## 8. Phase G — Domain role

| Role | Decision for `metacode-cloud.com` |
|------|-----------------------------------|
| Operational server reference name | **YES** (matches hostname `metacode-cloud`) |
| ACME / TLS certificate name | **YES** — primary cert identity for TLS fallback |
| TLS SNI for TLS+XHTTP (8443) | **YES** — use apex (and optionally `www` SAN) |
| REALITY dest / camouflage SNI | **NO — SEPARATE** — do **not** point Reality `dest`/`serverNames` at `metacode-cloud.com`; choose popular external camouflage targets at deploy time and record them in local secrets / evidence (not Git) |
| Neutral HTTPS brochure site | **DEFERRED** — not required for VPN ingress |
| Panel hostname | **NO public hostname** initially — localhost + SSH tunnel |
| Subscription hostname | Prefer tunnel initially; optional later neutral subdomain |

### Subdomain recommendation

| Item | Decision |
|------|----------|
| Required now | **NO** — apex + www A records are sufficient for TLS fallback + ops reference |
| Later optional neutral names (DNS **not** created this wave) | `edge`, `node`, `app`, `cdn`, `gateway`, `service` — only if public subscription or secondary surface needs isolation |
| Forbidden names | `vpn`, `proxy`, `xray`, `vless`, `reality`, `panel`, `sub` as obvious semantics |

`www` remains mail/ops-neutral A twin; not a VPN brand surface.

---

## 9. Phase H — 3X-UI control-plane model

| Surface | Decision |
|---------|----------|
| Panel bind | **`127.0.0.1` only** (high local port chosen at install; random `webBasePath`) |
| Public panel port (Server A style 5928) | **REJECTED** for initial EQVPS |
| Access method | **SSH local port-forward** (`ssh -L …`) from operator workstation |
| Reverse proxy / public TLS for panel | **NOT in first wave** — complexity without proportional benefit while SSH is hardened |
| Subscription public listener (Server A style 2096) | **DEFERRED** — prefer panel export / tunnel-served subscription until client ops require public sub URL |
| If public subscription later | Separate charter: TLS on neutral path, rate limits, fail2ban consideration, non-semantic URL |

**Default preference honored:** minimize public management-plane exposure relative to Server A.

---

## 10. Phase I — Port allocation plan (proposed)

| Port | Bind | Purpose | UFW now | UFW next phase |
|------|------|---------|---------|----------------|
| **22/tcp** | `0.0.0.0` / `::` | SSH (`marsops` key-only) | **ALLOW** | **KEEP ALLOW** |
| **443/tcp** | public | PRIMARY — VLESS + REALITY | DENY (no rule) | **ALLOW after listener ready** |
| **8443/tcp** | public | FALLBACK — VLESS + TLS + XHTTP | DENY | **ALLOW after listener + cert ready** |
| **80/tcp** | public | ACME HTTP-01 **temporary only** if chosen | DENY | Temporary allow **only** during cert issuance, then remove |
| Panel (e.g. `2053` or install-chosen) | **127.0.0.1** | 3X-UI admin | N/A (local) | **DO NOT UFW-publish** |
| Subscription | **127.0.0.1** initially | sub JSON/URI | N/A | **DO NOT UFW-publish** initially |
| Reality high-ephemeral ports (Server A 46489 style) | — | **NOT used** for primary — primary is 443 | — | Avoid extra public ports |

---

## 11. Phase J — TLS / ACME decision

| Question | Decision |
|----------|----------|
| Certificate required for first production deploy? | **YES — required before enabling TLS fallback on 8443** |
| Required for Reality primary on 443? | **NO** (Reality uses camouflage TLS; local LE cert not required for Reality itself) |
| Immediate issuance this wave? | **NO** — deferred to NEXT charter |
| Challenge strategy (NEXT) | **Prefer DNS-01 at Beget** (no long-lived :80; no fight with Reality on :443) |
| Alternate challenge | **HTTP-01 on :80** only as time-boxed step **before** Reality claims :443, then close :80 |
| TLS-ALPN-01 on :443 | **AVOID** once Reality owns 443 |
| Cert name | `metacode-cloud.com` (+ optional `www.metacode-cloud.com` SAN) |
| nginx for ACME | **NOT required** if using certbot standalone/DNS plugin or 3X-UI built-in ACME carefully |

**NEXT phase recommendation:** obtain cert **before or in parallel with** TLS inbound creation; bind TLS+XHTTP to 8443 using that cert; keep Reality on 443 without depending on the LE cert.

---

## 12. Phase K — Backup / rollback requirements (for NEXT deploy)

Programme rule: **a backup is not operationally complete until a restore strategy exists.**

### Pre-install checkpoint (required)

| Artifact | Location class |
|----------|----------------|
| `sshd` effective config evidence | Config / baseline |
| UFW status verbose + rules numbered | Config |
| fail2ban jail status | Config |
| `dpkg-query -W` bounded package snapshot | Metadata |
| `uname -a`, hostname, IP | Metadata |
| Provider snapshot (if EQVPS offers) | Layer 1 provider |

### Post-install / pre-exposure backup (required)

| Artifact | Notes |
|----------|-------|
| 3X-UI SQLite DB | Class F — **secret** |
| Xray config as managed by 3X-UI | Class F — **secret** |
| Panel settings (port, base path, cert paths) | Secret-adjacent |
| Let's Encrypt / cert files + private keys | Class E — **never Git** |
| systemd unit drops for x-ui | Config |
| Install version metadata (3X-UI, Xray) | Manifest |

Off-server copy under `X:\AI MARS STORAGE\` per Server Ops storage model (operator path); Git holds only sanitized pointers/manifests.

### Rollback triggers

- Client tunnel FAIL on both primary and fallback after smoke window  
- Direct Goodline gate regression on 22/443/8443  
- Panel lockout without SSH recovery path  
- Unexpected public exposure of panel/subscription  

### Rollback steps (conceptual)

1. UFW: remove 443/8443 allows → return to **22-only**.  
2. Stop/disable x-ui (and thus Xray) if unstable.  
3. Restore pre-install UFW/sshd/fail2ban from checkpoint if mutated incorrectly.  
4. Restore 3X-UI DB/config from post-install backup if config corruption.  
5. Provider snapshot restore only under explicit destructive/DR charter.  
6. Server A remains untouched fallback for operator connectivity.

---

## 13. Phase L — Security / exposure review (proposed end-state after NEXT)

| Surface | Classification |
|---------|----------------|
| SSH 22 | **REQUIRED** — already hardened |
| 443 Reality | **REQUIRED** public ingress |
| 8443 TLS+XHTTP | **REQUIRED** public fallback ingress |
| Panel | **LOCALHOST ONLY** |
| Subscription | **LOCALHOST ONLY** initially |
| Port 80 | **CLOSED** except time-boxed ACME |
| fail2ban | Keep sshd; evaluate later for any public HTTP surface |
| Privilege | Prefer existing `marsops` sudo for admin; avoid new password SSH |
| Updates | **Controlled** — no unattended bulk upgrade during first VPN bring-up |
| Attack surface vs Server A | **NARROWER** management plane; similar or smaller data plane (2 ports vs A’s many) |

---

## 14. Residuals

| Residual | Severity | Notes |
|----------|----------|-------|
| No swap on EQVPS | Known / accepted | Monitor memory after 3X-UI |
| AdminVPS Server B still exists; domain no longer points there | Ops clarity | Do not assume Server B owns `metacode-cloud.com` |
| OPERATIONAL-INDEX still describes Server B / AdminVPS as active planning locus | Doc drift | Update index in a later housekeeping wave — **not** blocking ingress charter |
| Reality camouflage target selection | Pending deploy | Choose at install; keep out of Git |
| XHTTP vs WS client validation | Pending deploy | Charter includes decision gate |
| Public subscription URL | Deferred | Explicit later charter |
| Provider snapshot availability on EQVPS | SAFE UNKNOWN | Confirm at NEXT preflight |

---

## 15. Remote mutation accounting

| Class | Count |
|-------|-------|
| `REMOTE_APPLICATION_MUTATIONS` | **0** |
| `REMOTE_DNS_MUTATIONS` | **0** |
| `REMOTE_FIREWALL_MUTATIONS` | **0** |
| `REMOTE_SSH_MUTATIONS` | **0** |
| Packages installed | **0** |
| Reboots | **0** |

Remote actions limited to **read-only** SSH evidence (`hostname`, `getent`, `resolvectl`, `ss`).

---

## 16. MARS files

| Path | Action |
|------|--------|
| `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-dns-binding-ingress-architecture-2026-08-27.md` | **CREATED** |
| `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-ingress-deployment-charter-v1.md` | **CREATED** |
| `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\dns-architecture-raw-2026-08-27\` | **CREATED** (local raw evidence) |

---

## 17. Git

| Item | Value |
|------|-------|
| Branch | `mars/canonical-post-recovery` |
| Commit | **NONE** |
| Staging | **NONE** (do not stage foreign WIP) |

---

*EQVPS-MICRO-IP DNS binding + ingress architecture · verification + decision only · deployment not executed.*

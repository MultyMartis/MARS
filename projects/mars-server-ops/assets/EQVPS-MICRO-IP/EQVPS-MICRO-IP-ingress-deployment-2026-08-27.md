# EQVPS-MICRO-IP — 3X-UI / Xray Ingress Deployment

**Date:** 2026-08-27  
**Wave:** MARS Server Ops — EQVPS-MICRO-IP first controlled production ingress  
**Host:** `metacode-cloud` · `95.216.126.173` · Ubuntu 24.04.4 LTS  
**Domain:** `metacode-cloud.com`  
**Verdict:** **PASS_WITH_RESIDUALS**

**Charter:** `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-ingress-deployment-charter-v1.md`  
**Architecture:** `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-dns-binding-ingress-architecture-2026-08-27.md`  
**Restore runbook:** `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-ingress-restore-runbook-v1.md`

**Raw evidence (local / not Git):** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\ingress-deployment-raw-2026-08-27\`  
**Secrets contour (local / not Git):** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\secrets.local.md`  
**Local backup copy (local / not Git):** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-ingress-postinstall-20260827T175740Z.tgz`

**No secrets in this document** (no UUIDs, private keys, panel passwords, Reality private key, cert private key).

---

## 1. Verdict rationale

Usable production ingress is **active** via **VLESS + TLS + XHTTP on TCP/8443** with a Let’s Encrypt certificate for `metacode-cloud.com`, localhost-only 3X-UI, hardened SSH preserved, and UFW limited to 22/443/8443.

**Residual:** VLESS + REALITY on TCP/443 is correctly configured and **passes on-server** (loopback + public-IP hairpin), but **fails from the operator workstation path** (Goodline / TUN-OFF) with `REALITY: received real certificate (potential MITM or redirection)`. Same Xray **26.7.28** client used for both tests.

---

## 2. Installed software / provenance

| Item | Value |
|------|-------|
| 3X-UI | **v3.7.0** (upstream MHSanaei/3x-ui release 2026-08-24) |
| Install method | Official `install.sh`, non-interactive, pinned `v3.7.0` |
| Release asset SHA256 (recorded at install) | `0f8dd7baef3458f6591574e24814f322cf7f5e1e27f0a594683745e50be84ec5` |
| Xray core | **26.7.28** (`/usr/local/x-ui/bin/xray-linux-amd64`, go1.26.5 linux/amd64) |
| Panel binary path | `/usr/local/x-ui/` |
| DB | `/etc/x-ui/x-ui.db` (sqlite) |
| certbot | **2.9.0** (Ubuntu package) |
| Docker / nginx | **NOT installed** |

---

## 3. Control plane

| Check | Result |
|-------|--------|
| Panel bind | `127.0.0.1:20901` only |
| Subscription bind | `127.0.0.1:2096` only (corrected from installer default public bind) |
| Public UFW for panel/sub | **NO** |
| SSH tunnel reachability | **PASS** — `direct-tcpip` to `127.0.0.1:20901` returns HTTP from panel (`404` on `/` without webBasePath; expected) |
| `PUBLIC_PANEL_EXPOSURE` | **NO** |

Access model: workstation → SSH (`marsops@95.216.126.173:22`) → `127.0.0.1:20901` + panel `webBasePath` (stored only in local secrets).

---

## 4. Primary ingress — VLESS + REALITY :443

| Field | Value |
|-------|-------|
| Protocol | VLESS |
| Security | REALITY |
| Port | 443/tcp |
| Flow (intended) | `xtls-rprx-vision` (stored in DB clients; 3X-UI 3.7.0 may omit `flow` from generated `config.json` — residual) |
| Camouflage dest | `www.cloudflare.com:443` |
| serverNames | `www.cloudflare.com` |
| Listener | `*:443` (xray under x-ui) |
| UFW | `443/tcp ALLOW` — comment `MARS XRAY REALITY PRIMARY` |

### Validation matrix (PRIMARY)

| Gate | Result | Evidence summary |
|------|--------|------------------|
| PRIMARY_TCP_443 | **PASS** | Workstation `Test-NetConnection` True |
| PRIMARY_XRAY_CONFIG | **PASS** | Reality inbound present; matched x25519 pair verified via `xray x25519 -i` |
| PRIMARY_CLIENT_CONNECT (server loopback) | **PASS** | SOCKS→ipify egress `95.216.126.173` |
| PRIMARY_CLIENT_CONNECT (server hairpin to public IP) | **PASS** | Same egress via `95.216.126.173:443` |
| PRIMARY_CLIENT_CONNECT (operator workstation) | **FAIL** | Xray 26.7.28: Reality auth fails → real Cloudflare cert |
| PRIMARY_EGRESS (workstation) | **FAIL** | Blocked by client connect failure |
| PRIMARY_DNS / PRIMARY_BROWSING (workstation) | **FAIL** | Not reached |

**Interpretation:** Server Reality stack is operational. Failure is on the **external client path** (likely DPI / TLS middlebox behavior on the operator link), not a broken keypair or dead listener.

---

## 5. TLS certificate

| Field | Value |
|-------|-------|
| Domain | `metacode-cloud.com` |
| Issuer | Let’s Encrypt (CN=YE2) |
| Method | **HTTP-01** via `certbot --standalone` on port 80 |
| Paths | `/etc/letsencrypt/live/metacode-cloud.com/fullchain.pem` + `privkey.pem` |
| Validity | notBefore 2026-08-27 · notAfter **2026-11-25** |
| Port 80 UFW | Temporary `MARS TEMP ACME HTTP-01` → **deleted immediately** after success |
| Host listener :80 after ACME | **NONE** (`ss` empty; curl to :80 from server fails) |
| Workstation TCP/80 quirk | Some Windows probes report connect success despite no host listener / UFW deny — **residual observation only**; host state is closed |

DNS-01 at Beget was **not** automated (no established safe Beget API path in this wave).

---

## 6. Fallback ingress — VLESS + TLS + XHTTP :8443

| Field | Value |
|-------|-------|
| Selected transport | **XHTTP** (`XHTTP_SELECTED`) |
| Compatibility WS | Not used (`TLS_WS_COMPATIBILITY_FALLBACK` = inactive) |
| Reason XHTTP OK | Xray 26.7.28 accepts XHTTP probe; 3X-UI 3.7.0 manages inbound; operator client 26.7.28 works |
| TLS | Real cert for `metacode-cloud.com` |
| Listener | `*:8443` |
| UFW | `8443/tcp ALLOW` — comment `MARS XRAY TLS FALLBACK` |

### Validation matrix (FALLBACK)

| Gate | Result | Evidence summary |
|------|--------|------------------|
| FALLBACK_TCP_8443 | **PASS** | Workstation TCP True |
| FALLBACK_TLS | **PASS** | TLS handshake; leaf CN=`metacode-cloud.com`; expiry 2026-11-25 |
| FALLBACK_CLIENT_CONNECT | **PASS** | Xray 26.7.28 SOCKS tunnel established |
| FALLBACK_EGRESS | **PASS** | `api.ipify.org` → `95.216.126.173` |
| FALLBACK_DNS / browsing | **PASS** | HTTPS via tunnel to Cloudflare trace OK |

---

## 7. Final public exposure

### Listeners (public / management)

| Bind | Role |
|------|------|
| `0.0.0.0:22` / `[::]:22` | SSH |
| `*:443` | Xray REALITY primary |
| `*:8443` | Xray TLS+XHTTP fallback |
| `127.0.0.1:20901` | 3X-UI panel |
| `127.0.0.1:2096` | 3X-UI subscription (localhost) |
| `127.0.0.1:62789` | x-ui internal API tunnel (localhost) |

### UFW inbound (final)

| Rule | Comment |
|------|---------|
| 22/tcp | MARS SSH |
| 443/tcp | MARS XRAY REALITY PRIMARY |
| 8443/tcp | MARS XRAY TLS FALLBACK |

Default: deny incoming / allow outgoing. Port 80: **no allow rule**.

---

## 8. Security preservation

| Control | State |
|---------|-------|
| SSH | Port 22; root/password/KbdInteractive disabled; Pubkey yes; MaxAuthTries 3; X11 no — **unchanged hardening** |
| UFW | Active; only 22/443/8443 |
| fail2ban | Active; sshd jail active |
| DNS | Functional (`resolvectl` eth0) |
| NTP | `NTPSynchronized=yes` |
| Hostname / PTR / Beget mail | **NOT mutated** |
| Server A / AdminVPS | **NOT mutated** |
| Reboot | **NOT performed** |

---

## 9. Backups

| Item | Path |
|------|------|
| Pre-install | `/root/mars-backups/eqvps-ingress-preinstall-20260827T172605Z/` (+ `.tgz`) |
| Post-install | `/root/mars-backups/eqvps-ingress-postinstall-20260827T175740Z/` (+ `.tgz`) |
| Post-install SHA256 | `02f66631dfc3055f2ba6b57a5538cd3454baa943a8826b860d65415e079b80ab` |
| Local tgz copy | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\backups\eqvps-ingress-postinstall-20260827T175740Z.tgz` |

Post-install contents include: `/etc/x-ui` (incl. `x-ui.db`), xray `config.json`, systemd unit, ssh/ufw/fail2ban trees, UFW/ss status, cert leaf + key copies under `certs-meta/`, version metadata.

Restore procedure: see restore runbook (linked above).

---

## 10. Rollback (defined, not destructively exercised)

Triggers: broken listeners, unintended public panel, cert/config corruption, need to withdraw ingress.

High-level sequence (preserve SSH/22 always):

1. Remove UFW 443/8443 allows if withdrawing public ingress.  
2. `systemctl stop x-ui` (optional disable).  
3. Restore `/etc/x-ui` + certs from postinstall or preinstall tarball.  
4. `systemctl start x-ui`; validate `ss` + UFW.  
5. Retain Server A as operator connectivity fallback (**read-only** — not modified this wave).

---

## 11. Residuals

1. **External REALITY client FAIL** on operator Goodline/TUN-OFF path despite server-side PASS.  
2. **3X-UI may omit Vision `flow` in generated `config.json`** even when DB clients have it — monitor / durable inject strategy if Reality must be Vision-strict under panel regen.  
3. Workstation **TCP/80 connect quirk** vs host closed :80 — no host listener; no UFW allow.  
4. Panel warning “not secure with SSL” is expected for localhost-only HTTP behind SSH tunnel.  
5. certbot renew timer installed by package — renewals must not leave :80 permanently open (standalone renew needs time-boxed UFW if used).  
6. Foreign WIP elsewhere in monorepo preserved; **no commit**.

---

## 12. Remote mutations (this wave)

- Installed 3X-UI v3.7.0 + bundled Xray 26.7.28  
- Locked panel/sub to localhost  
- Created REALITY inbound :443 + UFW 443  
- Installed certbot; issued LE cert via temporary UFW 80  
- Created VLESS TLS XHTTP inbound :8443 + UFW 8443  
- Created `/root/mars-backups/eqvps-ingress-*` checkpoints  

---

## 13. Explicit non-mutations

Public panel; public subscription; nginx; Docker; SSH port/hardening rollback; root/password SSH; hostname; PTR; Beget mail records; Server A; AdminVPS; fail2ban removal; UFW disable; swap; GPT repair; cloud-init; open-vm-tools removal; reboot; git commit.

---

## 14. Git

| Item | Value |
|------|-------|
| Branch | `mars/canonical-post-recovery` |
| Commit | **NONE** |
| Staged by this wave | **NONE** |
| Foreign WIP | Preserved (untouched) |

---

## 15. Recommended next phase (do not execute here)

**EQVPS-MICRO-IP Reality path remediation / alternate-network validation** — confirm whether external REALITY failure is ISP-path-specific (test from a non-Goodline egress), then optionally harden Vision `flow` persistence under 3X-UI regen; keep TLS+XHTTP :8443 as production fallback. Optionally schedule certbot renew procedure that never leaves :80 permanently open.

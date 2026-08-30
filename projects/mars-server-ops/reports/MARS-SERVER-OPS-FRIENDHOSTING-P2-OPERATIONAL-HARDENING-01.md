# REPORT — MARS Server Ops FriendHosting P2 Operational Hardening 01

**Date (UTC):** 2026-08-30  
**Wave:** FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01 (+ interrupted-run recovery)  
**Target:** FRIENDHOSTING-DE / FriendHosting Germany / `92.42.99.126` / `metacode-cloud.com` / SSH `:3333`  
**P2 FINAL:** **PARTIAL**  
**Interrupted-run recovery:** **RECOVERED**  
**Critical server health before resume:** **PASS**

---

## 1. Executive verdict

P2 operational hardening was interrupted by a Cursor/session disconnect mid-wave. Recovery reconstructed actual state, reused the validated post-Plus pre-hardening backup, did **not** replay completed SSH hardening, finished remaining phases with **minimal mutation**, and left the working VLESS `:8443` architecture unchanged.

| Gate | Result |
|------|--------|
| Pre-resume health (SSH / nginx / panel localhost / Xray / DNS / TLS live / VPN egress) | **PASS** |
| Backup + SHA-256 match + restore strategy | **PASS / CONFIRMED** |
| Key-based SSH (operator `marsops` + root) | **PASS** |
| PasswordAuthentication | **no** |
| PermitRootLogin | **prohibit-password / without-password** |
| UFW intended allow 3333/443/8443 + deny 20901/2096 | **PASS** |
| fail2ban `sshd` jail + port **3333** drop-in | **PASS** |
| Swap `/swapfile` 2 GiB + fstab | **PASS** |
| `:2096` public hardening (UFW deny, **no** x-ui restart) | **HARDENED** |
| Live TLS `:443` / `:8443` | **PASS** (valid until **2026-11-27**) |
| `certbot renew --dry-run` | **FAIL** (standalone HTTP-01 needs **:80**; UFW denies :80) |
| VPN egress / HTTPS smoke | **PASS** (`92.42.99.126`) |
| Cursor smoke | **UNPROVEN** in this recovery wave |
| FriendHosting VPN architecture mutation | **0** |
| Reboot | **0** |

**Why PARTIAL (not FAIL):** transport, VPN, SSH, UFW, fail2ban, swap, and panel exposure controls work. The residual is **TLS auto-renew readiness under current UFW** — live certificates are healthy; simulated renewal cannot complete until ACME path is reconciled with the firewall (follow-up charter).

---

## 2. Interrupted-run recovery

### What happened

- Cursor/Agent session lost connectivity while P2 was in progress.
- Operator reported general Internet and FriendHosting VPN stable; exact stop phase unknown at resume time.
- Recovery **did not** restart the charter from phase 1.

### Already completed before interruption (do not repeat)

1. Pre-hardening baseline  
2. Fresh post-Plus / pre-hardening backup  
3. Backup hash validation (remote/local SHA-256 match)  
4. Restore strategy confirmation  
5. SSH audit  
6. Key-based operator SSH (`marsops` + pubkey)  
7. SSH auth hardening (KEY-ONLY drop-in)  
8. `:2096` **analysis** (case: not required by local VLESS profile)

### Partial / incomplete before interruption

- **`:2096` hardening** — STARTED / INCOMPLETE. Prior runner restarted `x-ui`, then SSH transport died (`SSH_DEAD_AFTER_XUI_RESTART`). UFW deny for `:2096` had **not** been applied.
- Firewall reconciliation, fail2ban validation, swap, TLS dry-run, logging, systemd boot readiness, package marker, post-hardening regression — **NOT STARTED** or incomplete relative to final gates.

### Ambiguous mutation found

- SSH already **KEY-ONLY**. Password bootstrap failed with `BadAuthenticationType: publickey`. Local encrypted key backup unlocked with passphrase literal `""`; working unencrypted `marsops_ed25519` restored for operator use. Both installed pubkeys remain on server. **No further SSH auth mutation** in recovery.
- `systemctl is-enabled ssh` was **disabled** while service **active** — boot readiness risk; fixed with `systemctl enable ssh` (no reboot).

### Resumed in recovery (first incomplete safe phases)

1. Live health gate — **PASS**  
2. Independent key SSH sessions (root + marsops) — **PASS**  
3. `:2096` hardening via **`ufw deny 2096/tcp` (+ deny `20901/tcp`)** — **no x-ui restart**, no listen rewrite  
4. Firewall reconciliation — allow 3333/443/8443; default deny  
5. fail2ban — ensure `/etc/fail2ban/jail.d/00-mars-server-ops-ssh.conf` `port = 3333`; reload  
6. Swap — create `/swapfile` **2048 MiB**, `chmod 600`, `mkswap`, `swapon`, fstab  
7. TLS — classify timer + dry-run (dry-run **FAIL**, see §10)  
8. Logging — `journald` `SystemMaxUse=200M`  
9. Systemd — enable `ssh`; verify nginx / x-ui / fail2ban enabled+active  
10. Post-hardening regression — critical services **PASS**

### Not repeated

- Operator account creation  
- SSH drop-in rewrite (already PASS)  
- Backup recreation (validated archive reused)  
- x-ui restart for `:2096`  
- Any VLESS / Xray / UUID / `:8443` architecture change  

### Evidence roots

- Evidence: `X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01\`  
- Tools: `X:\AI MARS\projects\mars-server-ops\tools\friendhosting-p2\`  
- Local contour (out of Git): `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\`

---

## 3. Phase matrix (forensic + recovery)

| # | Phase | Status |
|---|-------|--------|
| 1 | Pre-hardening baseline | **COMPLETED** |
| 2 | Fresh post-Plus backup | **COMPLETED** |
| 3 | Backup/hash validation | **COMPLETED** |
| 4 | Restore strategy | **COMPLETED** |
| 5 | SSH audit | **COMPLETED** |
| 6 | Key-based operator SSH | **COMPLETED** |
| 7 | SSH auth hardening | **COMPLETED** |
| 8 | Listener audit | **COMPLETED** (recovery final-state capture) |
| 9 | `:2096` analysis | **COMPLETED** |
| 10 | `:2096` hardening | **COMPLETED** in recovery (UFW deny) |
| 11 | Firewall reconciliation | **COMPLETED** |
| 12 | fail2ban | **COMPLETED** |
| 13 | swap/OOM resilience | **COMPLETED** |
| 14 | TLS renewal readiness | **PARTIAL** — timer OK; dry-run **FAIL** |
| 15 | Logging/rotation | **COMPLETED** (journald cap); x-ui logrotate optional |
| 16 | systemd/boot recovery | **COMPLETED** (`ssh` enabled; no reboot) |
| 17 | Package/security audit | **PARTIAL** — light marker only; no reboot |
| 18 | Post-hardening regression | **COMPLETED** for critical path; Cursor smoke **UNPROVEN** |

---

## 4. Backup gate

| Field | Value |
|-------|--------|
| Remote | `/root/mars-backups/friendhosting-plus-p2-pre-hardening-20260830T085016Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-plus-p2-pre-hardening-20260830T085016Z.tgz` |
| Size | **80689274** bytes |
| SHA-256 | `596469e821d4c4cf2dae8156032c7dc1a79b8702cde4495cd9643cebc125b9da` |
| SHA-256 match | **YES** |
| Restore strategy | **CONFIRMED** (see evidence `RESTORE-STRATEGY.md`) |
| Duplicate backup created in recovery? | **NO** |

Also retained (earlier wave): CURRENT-STATE / pre-panel-reboot archive `20260830T073335Z` remains a prior restore anchor.

---

## 5. SSH final state

| Item | State |
|------|--------|
| Port | **3333** |
| PasswordAuthentication | **no** |
| PubkeyAuthentication | **yes** |
| PermitRootLogin | **prohibit-password** (effective `without-password`) |
| Operator account | `marsops` (sudo group) |
| Independent key login root | **PASS** |
| Independent key login marsops | **PASS** |
| Drop-in | `/etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf` |
| Lockout protection | Working key session proven before any further auth change; recovery did not disable remaining access |

---

## 6. Listeners and `:2096`

| Listener | Bind | Intended exposure |
|----------|------|-------------------|
| sshd | `*:3333` | Public (UFW allow) |
| nginx | `*:443` | Public (UFW allow) |
| Xray | `*:8443` | Public (UFW allow) |
| 3X-UI panel | `127.0.0.1:20901` | Localhost only — **NOT EXPOSED** |
| 3X-UI sub | `*:2096` | Process still listens; **UFW DENY** |

**`:2096` method:** Case A (not required by local client profile). Hardened with UFW only. **No** x-ui restart in recovery (prior restart caused SSH death).

**Note:** Workstation TCP/HTTP probes to `:2096` may still succeed via VPN hairpin / local path ambiguity. Authority for public exposure is **UFW DENY + default deny**. Internet-facing intent = blocked.

---

## 7. Firewall (UFW)

```
Default: deny (incoming), allow (outgoing)
ALLOW: 3333/tcp, 443/tcp, 8443/tcp
DENY:  2096/tcp, 20901/tcp
```

Public ports intended: **3333, 443, 8443** only.

---

## 8. fail2ban

| Item | State |
|------|--------|
| Installed / enabled / active | **yes** |
| Jail `sshd` | **active** |
| Drop-in | `/etc/fail2ban/jail.d/00-mars-server-ops-ssh.conf` with `port = 3333` |
| Filter backend | systemd (`sshd.service`) |

---

## 9. Swap

| Item | State |
|------|--------|
| Path | `/swapfile` |
| Size | **2 GiB** |
| Permissions | `-rw-------` root:root |
| Active | **yes** |
| fstab | `/swapfile none swap sw 0 0` |
| Second swap created? | **NO** |

---

## 10. TLS renewal readiness

| Item | State |
|------|--------|
| Live cert `metacode-cloud.com` | **PASS** — notAfter **Nov 27 16:46:34 2026 GMT** |
| TLS handshake `:443` / `:8443` | **PASS** |
| `certbot.timer` | **enabled** + **active** |
| Renewal config authenticator | **standalone** |
| `certbot renew --dry-run` | **FAIL** — LE cannot fetch HTTP-01 on **:80** (timeout / firewall) |
| Port 80 listener | **absent** |
| UFW :80 | **not allowed** (intentional under harden defaults) |

**Classification:** **TIMER PRESENT; LIVE CERTS HEALTHY; AUTO-RENEW UNDER CURRENT UFW = NOT READY**.

**Do not** blindly open `:80` or change VLESS TLS material in this wave. Follow-up charter should pick one of: temporary UFW allow `:80` around renew (hooks), nginx/webroot HTTP-01 with controlled `:80`, or DNS-01.

Initial recovery dry-run hit `TimeoutError` / leftover certbot lock; final dry-run after lock clear produced the authentic FAIL above (`R1-tls-final.txt`).

---

## 11. Logging / boot recovery

| Item | State |
|------|--------|
| journald `SystemMaxUse` | **200M** |
| `ssh.service` enabled | **yes** (was disabled → enabled) |
| nginx / x-ui / fail2ban | enabled + active |
| Reboot performed | **0** |

---

## 12. Post-hardening regression

| Check | Result |
|-------|--------|
| SSH `:3333` | **PASS** |
| Key-based SSH | **PASS** |
| nginx `:443` | **PASS** |
| 3X-UI `127.0.0.1:20901` | **PASS** (localhost bind) |
| Public `:20901` | **NOT EXPOSED** (bind + UFW) |
| Xray `:8443` | **PASS** |
| VPN egress | `92.42.99.126` |
| VPN HTTPS smoke | **PASS** |
| Cursor smoke | **UNPROVEN** |
| UFW | intended |
| fail2ban | intended |
| swap | intended |
| `:2096` | UFW hardened; process listen residual |
| TLS renewal | classified **NOT READY** (dry-run FAIL) |

---

## 13. Mutations this wave (recovery continue)

| Area | Mutation |
|------|----------|
| `:2096` / panel | `ufw deny 2096/tcp`; `ufw deny 20901/tcp`; **no** x-ui restart |
| Firewall | ensure allow 3333/443/8443; default deny |
| fail2ban | ensure ssh jail port **3333** drop-in; reload |
| swap | create 2 GiB `/swapfile` + fstab |
| logging | journald SystemMaxUse=200M |
| systemd | `systemctl enable ssh` |
| VLESS / Xray / UUID / nginx panel path | **unchanged** |
| VEESP / EQVPS | **0** |
| Windows network | **0** |

---

## 14. Boundaries confirmed

- VEESP mutation = **0**  
- EQVPS mutation = **0**  
- FriendHosting VPN architecture mutation = **0**  
- FriendHosting reboot = **0**  
- Windows network mutation = **0**  
- Secret disclosure = **0** (no passwords, private keys, UUID/URI, panel path, or TLS private keys in this report)  
- Foreign WIP mutation = **0**  
- commit/push = **0**

---

## 15. NEXT

1. **TLS ACME under UFW** — separate narrow charter: make `certbot renew` succeed without weakening SSH/VPN (preferred: renew hooks or nginx/webroot + controlled `:80`, or DNS-01).  
2. Optional: decide whether to stop x-ui `*:2096` listen entirely (deeper than UFW) — only with charter; avoid x-ui restart without SSH lockout plan.  
3. Cursor smoke through VPN — operator prove separately.  
4. Do **not** treat node as `PRODUCTION_ACCEPTED` until soak (P6) + backup restore drill (P1) per inventory doctrine.  
5. No commit/push unless operator requests selective staging of allowlisted report/index paths.

---

## 16. References

- Prior disk wave: [MARS-SERVER-OPS-FRIENDHOSTING-PLUS-DISK-EXPANSION-01.md](MARS-SERVER-OPS-FRIENDHOSTING-PLUS-DISK-EXPANSION-01.md)  
- Evidence summary: `evidence/FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01/00-summary.json`  
- Final state: `evidence/.../R1-final-state.txt`  
- TLS dry-run: `evidence/.../R1-tls-final.txt`

---

*FriendHosting P2 Operational Hardening 01 · interrupted-run recovery · 2026-08-30 · PARTIAL*

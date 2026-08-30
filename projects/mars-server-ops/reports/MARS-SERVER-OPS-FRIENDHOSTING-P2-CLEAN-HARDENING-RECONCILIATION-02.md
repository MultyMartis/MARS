# REPORT — MARS Server Ops FriendHosting P2 Clean Hardening Reconciliation 02

**Date (UTC):** 2026-08-30  
**Wave:** FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02  
**Target:** FRIENDHOSTING-DE / FriendHosting Germany / `92.42.99.126` / `metacode-cloud.com` / SSH `:3333`  
**Administration path:** **VEESP** (workstation egress `178.173.250.69`) — FriendHosting not used as Windows VPN during this wave  
**P2 FINAL:** **PASS**

---

## 1. Executive verdict

Independent clean reconciliation from **live FriendHosting state** (not a replay of the interrupted P2 runner) confirms prior hardening still holds, creates a **new** hardened-state backup, and closes the remaining ACME gap: `certbot renew --dry-run` now **PASS** via nginx **webroot** HTTP-01 on `:80`.

| Gate | Result |
|------|--------|
| Independent VEESP control path | **PASS** (egress VEESP; FH administered over public IP) |
| Live pre-mutation health | **PASS** |
| Fresh backup + SHA-256 match + restore strategy | **PASS / CONFIRMED** |
| SSH key login root + marsops `:3333` | **PASS** |
| PasswordAuthentication | **DISABLED** |
| Root password remote login | **PROHIBITED** (`prohibit-password` / `without-password`) |
| marsops sudo | **PASS** |
| UFW default deny; allow 3333/443/8443/**80**; deny 20901/2096 | **PASS** |
| `:2096` | **UFW-DENIED ACCEPTED BOUNDARY** (listen `*:2096`, public HTTP timeout) |
| fail2ban `sshd` port **3333** | **PASS** |
| Swap `/swapfile` 2 GiB + fstab | **PASS** |
| Live TLS `:443` / `:8443` | **PASS** (notAfter **2026-11-27**) |
| `certbot renew --dry-run` | **PASS** (webroot) |
| Deploy/reload hook | **CONFIGURED** (nginx reload + x-ui restart on real renew) |
| VLESS `:8443` architecture mutation | **0** |
| Reboot / disk / VEESP / EQVPS mutation | **0** |
| FriendHosting client VPN smoke (workstation profile switch) | **PENDING OPERATOR** (intentional STOP) |

---

## 2. Why clean reconciliation was opened

Earlier P2 was interrupted around x-ui/`:2096` work; a recovery wave reconstructed state and left P2 **PARTIAL** because TLS renew dry-run failed under standalone HTTP-01 with UFW blocking `:80`.

This wave is a **new clean audit** from actual live authority:

- Do **not** replay old mutation scripts blindly.
- Do **not** roll back successful hardening merely to recreate baseline.
- First prove live truth; then close remaining gaps (primarily ACME).

Historical report retained: [MARS-SERVER-OPS-FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01.md](MARS-SERVER-OPS-FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01.md).

---

## 3. Independent VEESP administration path

| Check | Evidence |
|-------|----------|
| Workstation public egress | `178.173.250.69` (VEESP / MCA-VPN-001) |
| Default route | `xray_tun` present (VEESP VPN) |
| FriendHosting profile on Windows | **Not switched** during hardening |
| SSH/admin target | `92.42.99.126:3333` over independent path |

Intentional separation: **VEESP = control path**, **FriendHosting = hardened target**.

---

## 4. Live-state audit

Captured before mutation (`A1-live-audit.txt`).

| Area | Live truth |
|------|------------|
| Hostname | `imart216311` |
| OS | Ubuntu **24.04.4** LTS |
| Kernel | `6.8.0-138-generic` |
| Uptime (audit) | ~1h55 |
| vCPU | **2** |
| RAM | **~1.9 GiB** |
| Swap | **/swapfile 2 GiB** active, mode `600`, fstab present |
| Disk | `/dev/sda1` ext4 **~19G**, ~**14G** free (~29% used) |
| Listeners | `:3333` sshd; `:443` nginx; `:8443` xray; `127.0.0.1:20901` x-ui; `*:2096` x-ui; later `:80` nginx (post-ACME) |
| Services | ssh/nginx/x-ui/fail2ban **active+enabled**; certbot.timer **active+enabled** |
| UFW | active; default deny in; allow 3333/443/8443; deny 2096/20901 (then +allow 80) |
| SSH | Port 3333; PasswordAuthentication **no**; PermitRootLogin **prohibit-password**; pubkey yes |
| fail2ban | jails `sshd` (port 3333) + `3x-ipl` |
| TLS | certbot **2.9.0**; lineage `metacode-cloud.com`; valid to **2026-11-27**; was **standalone** |
| journald | `SystemMaxUse=200M` (~38.8M used) |
| nginx logrotate | daily, rotate 14 |
| Server egress | `92.42.99.126` |

---

## 5. Critical pre-mutation health

| Check | Result |
|-------|--------|
| SSH `:3333` | **PASS** |
| nginx `:443` TLS | **PASS** |
| Panel reverse proxy (secret path not disclosed) | **PASS** |
| 3X-UI localhost `:20901` | **PASS** (`127.0.0.1:20901`) |
| Xray `:8443` TLS | **PASS** |
| DNS `metacode-cloud.com` → `92.42.99.126` | **PASS** |
| Public `:20901` / `:2096` HTTP | **Timeout** (blocked) |
| Password SSH | **REJECTED** (`publickey` only) |

**Health gate:** **PASS** → mutation authorized for backup + ACME only.

---

## 6. Fresh hardened-state backup

| Field | Value |
|-------|-------|
| Stamp | `20260830T102110Z` |
| Remote | `/root/mars-backups/friendhosting-p2-clean-hardened-state-20260830T102110Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-p2-clean-hardened-state-20260830T102110Z.tgz` |
| Size | ~80.7 MiB |
| SHA-256 | `bb9a07045cc610c52275895cf4679881699906df24284e147f059486098d243c` |
| SHA match | **YES** |
| Members | etc-ssh, etc-nginx, etc-letsencrypt, etc-ufw, fail2ban, usr-local-x-ui, x-ui-db, fstab, systemd/package/meta snapshots |

Prior P2 pre-hardening archive `20260830T085016Z` remains historical; this wave did **not** rely on it as the sole restore anchor.

---

## 7. Restore strategy

**CONFIRMED** — see evidence `B1-RESTORE-STRATEGY.md` and local twin  
`...\backups\friendhosting-p2-clean-hardened-state-20260830T102110Z-RESTORE-STRATEGY.md`.

Human-operated: verify SHA → extract to staging → review diffs → scoped restore → `nginx -t` / reload → careful `x-ui` restart → validate SSH/TLS/UFW/VPN listeners.

Not a full DR drill in this wave.

---

## 8. SSH current truth

| Fact | Value |
|------|-------|
| Port | **3333** |
| root key login | **PASS** (retained for recovery) |
| marsops key login | **PASS** |
| marsops groups | `sudo`, `users` |
| PasswordAuthentication | **no** |
| PermitRootLogin | **prohibit-password** / effective **without-password** |
| Password probe | `BadAuthenticationType` — allowed types `publickey` |

No unnecessary SSH rewrite performed.

---

## 9. SSH final posture

Acceptable MARS posture retained:

- Key-based `:3333`
- `marsops` operational account + sudo **PASS**
- Password auth **DISABLED**
- Root password remote login **PROHIBITED**
- Root key recovery access **retained** (intentional)

No further theoretical tightening.

---

## 10. UFW / public surface

**Final intended public surface:**

| Port | Policy |
|------|--------|
| **3333/tcp** | ALLOW (SSH) |
| **443/tcp** | ALLOW (nginx TLS / panel reverse proxy) |
| **8443/tcp** | ALLOW (Xray VLESS) |
| **80/tcp** | ALLOW (ACME HTTP-01 + HTTPS redirect only) |
| **2096/tcp** | DENY |
| **20901/tcp** | DENY |
| Default incoming | **deny** |

IPv4 + IPv6 rules aligned. `:80` is minimal ACME/redirect — **not** panel exposure.

---

## 11. `:2096` decision

| Question | Finding |
|----------|---------|
| Owner | x-ui subscription HTTP service |
| Required by local VLESS profile / MARS operator | **No** (prior analysis; not reopened for listen rewrite) |
| Process listen | still `*:2096` |
| Public reachability | HTTP **Timeout** |
| x-ui restart to rebind | **Not done** (prior interruption risk; unnecessary) |

**Classification:** **B — PROCESS LISTENS BUT UFW DENY — ACCEPTED HARDENED BOUNDARY**

---

## 12. fail2ban

| Item | Status |
|------|--------|
| Service | active + enabled |
| `sshd` jail | enabled; **port = 3333**; backend systemd |
| Banned (audit) | 0 |
| Extra | `3x-ipl` jail present (x-ui) |

No reinstall; no self-ban.

---

## 13. swap / OOM

| Item | Status |
|------|--------|
| `/swapfile` | **2 GiB**, `rw-------` root |
| Active | **yes** |
| fstab | `/swapfile none swap sw 0 0` |
| Extra swappiness tuning | **none** |

Left unchanged.

---

## 14. TLS / ACME initial state

| Item | Pre-fix |
|------|----------|
| Live cert | **VALID** to 2026-11-27 |
| Authenticator | **standalone** |
| Challenge | http-01 |
| Problem | UFW denied `:80` → `certbot renew --dry-run` **FAIL** historically |
| Consumers | nginx `:443` + Xray via LE live paths (`oneTimeLoading: false`) |

---

## 15. TLS renewal fix

Mutations (narrow):

1. nginx site `metacode-cloud-acme80` — serve `/.well-known/acme-challenge/` from `/var/www/letsencrypt`; elsewhere **301 → HTTPS**.
2. `ufw allow 80/tcp` (ACME).
3. Renewal conf: `authenticator = webroot`, `webroot_path = /var/www/letsencrypt`, `[[webroot_map]]`.
4. Deploy hook `mars-reload-tls-consumers.sh`: `nginx -t` + reload; `systemctl restart x-ui` on **real** renewals.

**Not used:** manual recurring port-opening; DNS-01; VLESS/UUID/inbound changes.

---

## 16. certbot dry-run

```text
Simulating renewal of an existing certificate for metacode-cloud.com
Congratulations, all simulated renewals succeeded
DRY_EXIT:0
```

| Field | Value |
|-------|--------|
| Exit | **0 / PASS** |
| Authenticator | **webroot** |
| External challenge probe | HTTP **200** on probe file |
| `:80` root | **301** to HTTPS |
| Non-challenge path | **404** for missing challenge (expected) |

---

## 17. Certificate consumer reload / hooks

| Consumer | Path | Hook action |
|----------|------|-------------|
| nginx | LE `fullchain.pem` / `privkey.pem` | **reload** |
| Xray (via x-ui) | same LE paths | **restart x-ui** on deploy |

Dry-run does not exercise deploy hooks. Hook is installed for automated renewals. No x-ui restart executed in this wave for ACME dry-run (avoids prior SSH-drop risk during admin session).

---

## 18. Logging / rotation

| Item | Status |
|------|--------|
| journald `SystemMaxUse=200M` | **PASS** (~38.8M used) |
| nginx logrotate | present (daily / 14) |
| fail2ban / auth / x-ui rotate | standard packages + `mars-x-ui` logrotate present |
| Unbounded log risk on 20G disk | **not observed** |

No further logging mutation.

---

## 19. systemd / recovery

| Unit | active | enabled |
|------|--------|---------|
| ssh | yes | yes |
| nginx | yes | yes |
| x-ui | yes | yes |
| fail2ban | yes | yes |
| certbot.timer | yes | yes |

Xray lifecycle owned by **x-ui**. **No reboot** this wave — boot survival classified **PASS from unit enablement + prior historical reboot evidence**, not re-proven by reboot here.

---

## 20. Security package state

| Item | Status |
|------|--------|
| `apt list --upgradable` | **0 packages** (header-only listing) |
| `reboot-required` | **no** |
| Broad dist-upgrade | **not performed** |
| Pending security maintenance | None queued at verification time; continue normal apt hygiene under separate charter |

---

## 21. Final service regression

| Check | Result |
|-------|--------|
| SSH root key | **PASS** |
| SSH marsops key | **PASS** |
| marsops sudo | **PASS** |
| Password SSH | **DISABLED** |
| nginx `:443` | **PASS** |
| Panel reverse proxy | **PASS** (path secret) |
| 3X-UI `:20901` localhost | **PASS** |
| Public `:20901` | **BLOCKED** |
| `:2096` | **UFW-DENIED ACCEPTED BOUNDARY** |
| Xray `:8443` | **PASS** |
| TLS `:443` / `:8443` | **PASS** |
| UFW | **PASS** |
| fail2ban | **PASS** |
| swap | **PASS** |
| certbot dry-run | **PASS** |

---

## 22. Outstanding operator FriendHosting VPN smoke

**STOP checkpoint for operator:**

Server-side P2 hardening is complete. **Remain on VEESP** until ready.

Then manually switch v2rayN to profile:

`MCA-ONE-FRIENDHOSTING-DE-RAW-8443`

Suggested smoke (operator):

1. Confirm TUN on FriendHosting profile.
2. Check egress ≈ `92.42.99.126`.
3. Cursor / ChatGPT / YouTube HTTPS smoke as in prior acceptance doctrine.
4. Do **not** change server UFW/SSH/x-ui during client smoke.

This wave intentionally did **not** auto-switch Windows VPN.

---

## 23. Relationship to interrupted P2 run

| Topic | Stance |
|-------|--------|
| Old report | **Historical evidence only** — not deleted/rewritten |
| This report | **New** clean reconciliation authority |
| Successful prior hardening | **Preserved** (SSH/UFW/fail2ban/swap/2096 deny) |
| Replay | **Not** a continuation of interrupted runner |
| Residual closed | ACME dry-run under UFW |

---

## 24. Final P2 verdict

**P2 HARDENING = PASS**

All critical gates including `certbot renew --dry-run` succeeded. Client-side FriendHosting VPN smoke remains an **operator** post-STOP item and does not reopen server P2.

---

## 25. Next-wave decision

Do **not** execute now. Roadmap after operator VPN smoke:

1. **P3** — FRIENDHOSTING PER-DEVICE VLESS IDENTITY MODEL 01  
2. **P4** — FRIENDHOSTING RESERVE RAW/TLS `:24443`  
3. **P5** — backup automation + lightweight monitoring  
4. **P6** — multi-day soak / promotion  

Node remains **CONTROL / OPERATIONAL-CANDIDATE** (not `PRODUCTION_ACCEPTED`) until soak + fuller DR discipline.

---

## 26. Evidence paths

| Locus | Path |
|-------|------|
| Git-safe evidence | `projects/mars-server-ops/evidence/FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02/` |
| Tools | `projects/mars-server-ops/tools/friendhosting-p2/p2-clean-recon-02-*.py` |
| Local contour (secret-bearing) | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\` |
| Local mutate OUT | `...\p2-clean-recon-02-mutate-20260830T102110Z\` |
| Local audit OUT | `...\p2-clean-recon-02-20260830T101402Z\` |

---

## 27. Inventory / local-contour updates

- [SERVER-INVENTORY-v1.md](../SERVER-INVENTORY-v1.md) — FRIENDHOSTING-DE P2 → **PASS**; backup stamp `20260830T102110Z`; ACME webroot.  
- [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) — Core Run next → operator VPN smoke then **P3**.  
- Local backups twin under `FRIENDHOSTING-GERMANY\backups\` (out of Git).

---

## 28. Git / mutation closeout

| Item | Value |
|------|-------|
| commit/push | **0** |
| Foreign WIP mutation | **0** |
| VEESP server mutation | **0** |
| EQVPS mutation | **0** |
| FriendHosting VPN `:8443` architecture mutation | **0** |
| FriendHosting disk mutation | **0** |
| FriendHosting reboot | **0** |
| Windows network mutation during hardening | **0** |
| Secret disclosure in this report | **0** (panel path / UUID / keys omitted) |

**STOP.**

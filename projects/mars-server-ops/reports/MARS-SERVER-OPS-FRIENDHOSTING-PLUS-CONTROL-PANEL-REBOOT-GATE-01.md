# REPORT — MARS Server Ops FriendHosting Plus Control-Panel Reboot Gate 01

**Date (UTC):** 2026-08-30  
**Wave:** FRIENDHOSTING-PLUS-CONTROL-PANEL-REBOOT-GATE-01  
**Target:** FRIENDHOSTING-DE / FriendHosting Germany / `92.42.99.126` / `metacode-cloud.com`  
**Gate status:** **COMPLETE**  
**Verdict:** **PLUS CPU/RAM ACTIVATION = PASS** · disk expansion **PENDING PROVIDER-SIDE** by design · services/VPN **PASS**

---

## 1. Executive verdict

Operator pressed FriendHosting control-panel **Reboot** (order `#216311`). Guest now presents **2 vCPU** and **~1.9 Gi RAM** versus pre-reboot **1 vCPU / ~961 MiB**. Public IPv4 unchanged. Critical listeners returned without manual service start. VPN smoke via existing profile **PASS**. Disk remains **10 GiB** — expected; expansion is a separate support-side procedure.

| Gate | Result |
|------|--------|
| Panel reboot (boot time changed) | **PASS** |
| PLUS CPU/RAM activation | **PASS** |
| Disk expansion | **PENDING PROVIDER-SIDE WORK** |
| Services / TLS / UFW / VPN | **PASS** |
| Lifecycle | **CONTROL / OPERATIONAL-CANDIDATE** (unchanged) |

**NEXT:** **FRIENDHOSTING PLUS DISK EXPANSION 01** — coordinate with FriendHosting support via existing ticket (expect 10–20 min downtime). Do **not** grow partition/filesystem in this wave.

---

## 2. FriendHosting provider instruction

| Rule | Binding | This wave |
|------|---------|-----------|
| CPU/RAM apply only after panel **Reboot** | YES | Operator used panel Reboot |
| `systemctl reboot` / SSH reboot insufficient | YES | **Not used** (OS reboot = 0) |
| Disk expansion separate support procedure | YES | Not performed |
| Disk downtime ~10–20 min | noted | Future wave |
| Support window 09:00–23:30 UTC+2 | noted | Future wave |

---

## 3. Pre-reboot hardware

Captured `20260830T073335Z` (boot still `2026-08-29 14:07:19` UTC, uptime ~17h26m):

| Field | Value |
|-------|--------|
| Hostname | `imart216311` |
| OS / kernel | Ubuntu 24.04.4 LTS / `6.8.0-138-generic` |
| IPv4 / egress | `92.42.99.126` |
| MTU | 1500 |
| vCPU | **1** |
| RAM | **961Mi** (~984556 kB class) |
| Swap | none |
| `/dev/sda` | **10 GiB** (10737418240 B) |
| Root FS | ext4 ~8.7G / ~6.1G avail |

---

## 4. Fresh backup

| Item | Value |
|------|--------|
| Class | CURRENT-STATE PRE-PANEL-REBOOT |
| Remote dir | `/root/mars-backups/friendhosting-plus-pre-panel-reboot-20260830T073335Z` |
| Remote archive | `/root/mars-backups/friendhosting-plus-pre-panel-reboot-20260830T073335Z.tgz` |
| Local archive | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-plus-pre-panel-reboot-20260830T073335Z.tgz` |
| Local size | **80613337** bytes (~76.9 MiB) |
| Covered | 3X-UI/`x-ui` + DB, Xray under `/usr/local/x-ui`, nginx, Let's Encrypt, UFW, SSH, systemd cats, package inventory, hardware/network baselines |

Secret-bearing — local copy **out of Git**.

---

## 5. Backup validation / hash

| Check | Result |
|-------|--------|
| Archive exists (remote + local) | PASS |
| Non-zero size | PASS |
| `tar` list/read test | PASS |
| Remote SHA-256 | `04344ea5fb7d90086360753060197a2e2371f063f0efbef60bd713efe96ff002` |
| Local SHA-256 | `04344ea5fb7d90086360753060197a2e2371f063f0efbef60bd713efe96ff002` |
| Hash match | **YES** |
| Components | x-ui, x-ui.db, nginx, letsencrypt, ssh, ufw, baseline, systemd — **YES** |

Backup was confirmed **before** asking the operator to reboot.

---

## 6. Restore strategy

**Classification: BACKUP + RESTORE STRATEGY CONFIRMED**

Canonical steps:  
`X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-PLUS-CONTROL-PANEL-REBOOT-GATE-01\RESTORE-STRATEGY.md`

Order: verify SHA → extract → stop nginx/x-ui (keep ssh) → restore x-ui / nginx / ACME / UFW (review SSH) → `daemon-reload` → start x-ui → nginx → verify 3333/443/8443/20901 → TLS → VPN profile smoke → panel via nginx.

---

## 7. Operator control-panel reboot

| Item | Value |
|------|--------|
| Operator confirmation | **REBOOT COMPLETE** |
| Method | FriendHosting panel → order **#216311** → Server Management → **Reboot** |
| SSH / `systemctl reboot` | **not used** |
| Pre boot | `2026-08-29 14:07:19` UTC |
| Post boot (`uptime -s`) | **`2026-08-30 07:54:59` UTC** |
| Post uptime at recon | ~3 min (`20260830T075804Z`) |
| Current journal boot 0 | `2026-08-30 07:55:03` UTC (`6aec78f2…`) |
| Prior journal boot -1 | `2026-08-29 14:07:23` → `2026-08-30 07:54:46` UTC |

**Panel reboot: PASS** (new boot, uptime reset).

---

## 8. Post-reboot identity

| Field | Post (`20260830T075804Z`) |
|-------|---------------------------|
| Hostname | `imart216311` (unchanged) |
| Public IPv4 | **`92.42.99.126/24`** on `eth0` (unchanged) |
| Server egress | **`92.42.99.126`** |
| Default IPv4 | `via 92.42.99.1 dev eth0` |
| Default IPv6 | `via 2a06:fcc0:a::1` |
| MTU | **1500** (`eth0`, MAC `bc:24:11:45:ff:a6`) |
| Boot time changed | **YES** |

Network identity survived the panel reboot.

---

## 9. CPU activation

| | Pre | Post |
|--|-----|------|
| `nproc` | 1 | **2** |
| Online CPUs | cpu0 | **cpu0, cpu1** |
| Model | Common KVM processor | **Common KVM processor** |
| Topology | 1 socket × 1 core | **1 socket × 2 cores × 1 thread** |
| Hypervisor | KVM | KVM |

**CPU activation: PASS** (1 → 2 vCPU).

---

## 10. RAM activation

| | Pre | Post |
|--|-----|------|
| `free -h` Mem total | 961Mi | **1.9Gi** |
| MemTotal | ~984556 kB class | **2014852 kB (~1968 MiB)** |
| Swap | none | **none** (`SwapTotal: 0 kB`) |

**RAM activation: PASS** (~961 MiB → ~1.9 Gi). Swap not created (forbidden this wave).

**PLUS CPU/RAM ACTIVATION = PASS.**

---

## 11. Disk state

| Field | Post |
|-------|------|
| `/dev/sda` QEMU HARDDISK | **10737418240 B = 10 GiB** (unchanged) |
| Partition table | GPT; `sda1` root still **9662610944 B** |
| Root FS `/` ext4 | **8.7G** size, **3.0G** used, **5.8G** avail, **34%** |
| Unallocated trailing capacity | **none** visible (disk end = partition end) |

**DISK EXPANSION = PENDING PROVIDER-SIDE WORK.** Unchanged 10 GiB is **not** a CPU/RAM failure.

---

## 12. Why disk is intentionally still separate

FriendHosting states CPU/RAM apply after panel Reboot; disk expansion is a **support-side** procedure with ~10–20 min downtime and a ticket. Guest `growpart` / `resize2fs` were **not** run. A 10 GiB virtual disk after this reboot is the expected CASE until support expands the block device.

---

## 13. Service reboot survival

No manual `systemctl start` this wave. Post-reboot listeners and units:

| Endpoint | Result |
|----------|--------|
| sshd `:3333` | **PASS** (`ssh.service` + `ssh.socket` **active**) |
| nginx `:443` | **PASS** (`nginx.service` **enabled/active**) |
| Xray `:8443` | **PASS** (Xray **26.7.28** under x-ui) |
| 3X-UI `127.0.0.1:20901` | **PASS** (`x-ui.service` **enabled/active**) |
| Failed critical units | **none** |

Note (record only): `ssh.service` reports **disabled** while `ssh.socket` is **enabled** (Ubuntu socket activation). Listener `:3333` recovered without intervention. **Not mutated.**

**Service reboot survival: PASS.**

---

## 14. Firewall state

UFW **active**; default deny incoming / allow outgoing.

Intended public allows (unchanged):

- `3333/tcp` (MARS SSH)
- `443/tcp` (MARS 3X-UI nginx TLS)
- `8443/tcp` (MARS XRAY VLESS TLS RAW)

plus IPv6 twins. `20901` not in UFW allow list.

**Firewall: PASS.** Residual `:2096` — see §19.

---

## 15. TLS / domain

| Check | Result |
|-------|--------|
| DNS A `metacode-cloud.com` | **92.42.99.126** |
| nginx `:443` TLS (workstation) | **PASS** |
| Xray `:8443` TLS (workstation) | **PASS** |
| `openssl verify` | **OK** · **EXIT:0** |
| Cert | CN/SAN `metacode-cloud.com`, Let's Encrypt, 2026-08-29 → 2026-11-27 |

**TLS: PASS.**

---

## 16. VPN smoke

Profile **MCA-ONE-FRIENDHOSTING-DE-RAW-8443** — **not edited**.

| Check | Result |
|-------|--------|
| Proxy | `http://127.0.0.1:10808` |
| ipify | **92.42.99.126** |
| ifconfig.me | **92.42.99.126** |
| Google `generate_204` | **204** |
| OVH 1 MiB body | **PASS** (1048576 bytes) |

**VPN egress: 92.42.99.126**  
**VPN smoke: PASS** (post-reboot smoke only; not a long-term soak).

---

## 17. Cursor smoke

This wave continued through SSH reconnection, multi-command capture, TLS probes, and VPN HTTPS after the panel reboot while FriendHosting was the active path.

**CURSOR POST-REBOOT SMOKE = PASS.** Long-term soak **not** claimed.

---

## 18. Resource headroom

Post-reboot guest: **2 vCPU**, **~1.9 Gi RAM**, **10 GiB disk**, no swap.

| Near-term role | Headroom |
|----------------|----------|
| Xray `:8443` | **GOOD** |
| 3X-UI localhost | **GOOD** |
| nginx `:443` | **GOOD** |
| backup jobs | **GOOD** (root ~5.8G free; disk still 10 GiB) |
| monitoring | **GOOD** |
| multiple client identities | **GOOD** |
| reserve inbound | **ADEQUATE / GOOD** |
| n8n / PostgreSQL co-host | **Do not assume** — RAM/disk still not a multi-app host |

**Overall headroom for intended VPN control role: GOOD.** Disk remains the binding constraint until provider expansion.

---

## 19. Known `:2096` residual

**PRESENT** after panel reboot (`*:2096` x-ui subscription listener). UFW does not list `2096/tcp`. Pre-existing 3X-UI default bind residual.

**NOT MUTATED** this wave.

---

## 20. Provider disk-expansion next step

Recommend wave: **FRIENDHOSTING PLUS DISK EXPANSION 01**

1. Confirm/reuse current backup (or refresh if material drift).  
2. Coordinate exact time with FriendHosting support via **existing ticket**.  
3. Expect **10–20 min** downtime; support window **09:00–23:30 UTC+2**.  
4. Provider expands virtual disk.  
5. Reconnect after provider work.  
6. Inspect block-device / partition / filesystem.  
7. Only then decide whether guest-side filesystem growth is necessary.  
8. Validate SSH / nginx / Xray / 3X-UI / TLS / VPN afterward.

**Not performed in this invocation.**

---

## 21. Inventory update

Updated: `X:\AI MARS\projects\mars-server-ops\SERVER-INVENTORY-v1.md`

| Fact | Recorded |
|------|----------|
| Lifecycle | CONTROL / OPERATIONAL-CANDIDATE |
| CPU/RAM tariff activation | **PASS** (2 vCPU / ~1.9 Gi) |
| Disk expansion | **provider-side pending** (10 GiB unchanged) |
| Backup anchor | remote + local CURRENT-STATE `…20260830T073335Z.tgz` |
| Restore readiness | **CONFIRMED** (strategy written; restore drill not re-run) |
| Reboot-survival | **PASS** |

---

## 22. Evidence paths

| Path | Role |
|------|------|
| `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\plus-control-panel-reboot-gate-20260830T073335Z\` | Pre-reboot capture |
| `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\plus-control-panel-reboot-post-20260830T075804Z\` | Post-reboot capture + VPN/TLS |
| `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-plus-pre-panel-reboot-20260830T073335Z.tgz` | Secret-bearing local backup |
| `/root/mars-backups/friendhosting-plus-pre-panel-reboot-20260830T073335Z.tgz` | Remote backup |
| `X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-PLUS-CONTROL-PANEL-REBOOT-GATE-01\` | Sanitized evidence + restore strategy |
| This report | Gate closeout |

---

## 23. Mutation / Git closeout

| Item | Value |
|------|--------|
| VEESP mutation | 0 |
| EQVPS mutation | 0 |
| FriendHosting config mutation | 0 |
| FriendHosting OS reboot | 0 |
| FriendHosting control-panel reboot | **1** (operator) |
| FriendHosting disk resize | 0 |
| FriendHosting hardening mutation | 0 |
| Windows network mutation | 0 |
| Secret disclosure | 0 |
| Foreign WIP mutation | 0 |
| commit / push | 0 |

---

*FriendHosting Plus control-panel reboot gate 01 · 2026-08-30 · STOP.*

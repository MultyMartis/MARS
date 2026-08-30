# REPORT — MARS Server Ops FriendHosting Plus Post-Upgrade Reconciliation 01

**Date (UTC):** 2026-08-30  
**Wave:** FRIENDHOSTING-PLUS-POST-UPGRADE-RECONCILIATION-01  
**Target:** FRIENDHOSTING-DE / FriendHosting Germany / `92.42.99.126` / `metacode-cloud.com`  
**Mode:** READ-ONLY guest verification (no service, firewall, network, or filesystem mutation)  
**Verdict:** **PARTIAL** — critical services survived; **Plus hardware increase NOT presented** to the guest

---

## 1. Executive verdict

Operator reports tariff upgrade **Start → Plus** in the FriendHosting panel. Live guest inspection shows **unchanged** compute/memory/disk versus the 2026-08-29 pre-build baseline:

| Resource | Pre-upgrade (build pre-baseline) | Post-upgrade (this wave) |
|----------|----------------------------------|---------------------------|
| vCPU | 1 | **1** |
| RAM | ~961 MiB | **~961 MiB (984556 kB)** |
| Virtual disk `/dev/sda` | 10G class | **10 GiB (10737418240 B)** |
| Root FS `/` | ext4 ~8.7G | **ext4 ~8.7G / 8.6G findmnt** |

**Storage expansion:** **NOT PRESENTED** (CASE 3).  
**Services / VPN / SSH / TLS:** **PASS**.  
**Lifecycle:** remains **CONTROL / OPERATIONAL-CANDIDATE** (not PRODUCTION_ACCEPTED).  
**NEXT:** **C — PLUS RECONCILIATION FAIL** (resource presentation) → resolve provider/panel vs guest mismatch before P1 backup/hardening.

---

## 2. Upgrade context

| Item | Value |
|------|--------|
| Stable ID | FRIENDHOSTING-DE |
| Provider | FriendHosting |
| Location | Germany |
| Commercial tier (operator claim) | **Plus** |
| Prior local tier label | Start VDS (`node-identity.local.md`) |
| Provider panel exact Plus SKU specs in MARS | **NOT PERSISTED** → `PROVIDER PANEL SPEC = OPERATOR-OBSERVED / EXACT VALUE NOT YET PERSISTED` |
| Expected IPv4 | `92.42.99.126` |
| Domain | `metacode-cloud.com` |
| Pre-wave lifecycle | CONTROL / OPERATIONAL-CANDIDATE |
| Pre-wave acceptance | TRANSPORT PASS · REAL_WORKLOAD PASS · soak NOT YET PROVEN |

---

## 3. VM identity

| Field | Observed |
|-------|----------|
| Hostname | `imart216311` |
| OS | Ubuntu 24.04.4 LTS (noble) |
| Kernel | `6.8.0-138-generic` `#138-Ubuntu` x86_64 |
| Virtualization | KVM / QEMU (`systemd-detect-virt=kvm`; product `Standard PC (i440FX + PIIX, 1996)`) |
| machine-id sha256 | `e3f4488386654dbb5fb5bfcc6da64ab4df7b4aff8debab872e5c682a6860ff84` (hash only) |
| SSH | TCP/`3333` (`sshd` via `ssh.service` ACTIVE) |

Identity matches prior FriendHosting control-node evidence. No hostname/IP/OS class change observed.

---

## 4. Reboot / hot-resize evidence

| Evidence | Value |
|----------|--------|
| Boot time | `2026-08-29 14:07:19` UTC |
| Uptime at recon | ~17h06m (`2026-08-30 07:13` UTC) |
| `journalctl --list-boots` current boot | since `2026-08-29 14:07:23` UTC |
| `dmesg` resize/hotplug hits | **empty** (no useful resize lines in filtered tail) |
| Online CPU topology | only `cpu0` present under `/sys/devices/system/cpu` |

**Reboot caused by Plus upgrade:** **NO** (current boot predates this reconciliation day; no evidence of reboot for the tariff change during this session window).  
**Hot-add of CPU/RAM/disk:** **UNPROVEN / NOT OBSERVED** — guest still shows prior sizes.  
**VM migration:** **UNPROVEN** (insufficient evidence; MAC `bc:24:11:45:ff:a6` / IP unchanged).

---

## 5. CPU before / after

| | Before (2026-08-29 pre-baseline) | After (this wave) |
|--|----------------------------------|-------------------|
| `nproc` | 1 | **1** |
| CPU(s) | 1 | **1** |
| Model | Common KVM processor | **Common KVM processor** |
| Topology | 1 socket × 1 core × 1 thread | **same** |
| Hypervisor | KVM | **KVM** |
| Load average | ~0.00 | **0.01 0.02 0.00** |

**CPU reconciliation:** guest-visible CPU **unchanged**. No Plus vCPU increase presented.

---

## 6. RAM before / after

| | Before | After |
|--|--------|-------|
| `free -h` Mem total | 961Mi | **961Mi** |
| MemTotal | (baseline free text) | **984556 kB** |
| MemAvailable | — | **578104 kB (~564Mi available)** |
| Used (approx) | 286Mi | **~396Mi** |

**RAM reconciliation:** guest-visible RAM **unchanged** (~1 GiB class).

---

## 7. Swap

| Field | Value |
|-------|--------|
| Swap total | **0B** |
| Swap used | **0B** |
| `swapon --show` | empty |
| `/proc/swaps` | empty |

**Swap:** none. Do **not** create in this wave. Swap review belongs in later **P2 hardening / capacity** work if Plus capacity eventually appears.

---

## 8. Disk / block-device state

| Field | Value |
|-------|--------|
| Disk | `/dev/sda` QEMU HARDDISK |
| Virtual disk size | **10737418240 B = 10 GiB** |
| Partition table | GPT |
| `sda1` (root) | **9662610944 B ≈ 9.0 GiB** part, FSTYPE ext4, mount `/` |
| `sda15` | ESP vfat `/boot/efi` ~106M |
| `sda16` | `/boot` ext4 ~913M |

`parted -s /dev/sda unit B print` (read-only) confirms disk end **10737418240B** and root partition ending at disk end — **no unallocated trailing capacity** visible inside the guest.

---

## 9. Partition / filesystem state

| Field | Value |
|-------|--------|
| Root FS type | ext4 |
| `df -hT` `/` | **8.7G** size, **2.6G** used, **6.1G** avail, **30%** |
| `findmnt` size/avail | **8.6G / 6.1G / 30%** |
| `df -B1 /` | size **9283444736**, avail **6513876992** |

Partition and filesystem are consistent with each other for the current 10G virtual disk. There is **no** enlarged parent disk waiting for `growpart`/`resize2fs` inside the guest.

---

## 10. Storage expansion verdict

**CASE 3 — PROVIDER UPGRADE NOT FULLY PRESENTED**

| Check | Result |
|-------|--------|
| A. Virtual block device enlarged? | **NO** (still 10 GiB) |
| B. Partition enlarged? | **NO** |
| C. Filesystem enlarged? | **NO** |
| D. Free space comfortable for current stack? | **YES for current footprint** (~6.1G free) |

**Storage expansion:** **NOT PRESENTED**  
**Filesystem resize this wave:** **0** (forbidden / not indicated)

---

## 11. Network identity

| Field | Value |
|-------|--------|
| Public IPv4 | **92.42.99.126/24** on `eth0` |
| IPv6 | `2a06:fcc0:a::15b/48` + link-local |
| Domain A | `metacode-cloud.com` → **92.42.99.126** |
| Server egress (curl ipify/ifconfig) | **92.42.99.126** |
| MAJOR IP change? | **NO** |

---

## 12. Routes / MTU

| Field | Value |
|-------|--------|
| Default IPv4 | `via 92.42.99.1 dev eth0` |
| Default IPv6 | `via 2a06:fcc0:a::1` |
| MTU | **1500** (`eth0` / `fq_codel`) |
| DNS | systemd-resolved stub; uplink **8.8.8.8**; search `friendhosting.net` |

No route/MTU/DNS mutation performed.

---

## 13. Listener / service state

| Endpoint | Process | State |
|----------|---------|--------|
| `0.0.0.0:3333` / `[::]:3333` | sshd | **ACTIVE** |
| `0.0.0.0:443` / `[::]:443` | nginx | **ACTIVE** |
| `*:8443` | xray-linux-amd64 | **ACTIVE** (under x-ui) |
| `127.0.0.1:20901` | x-ui 3.7.0 | **ACTIVE** (localhost bind) |
| `*:2096` | x-ui subscription HTTP | **LISTEN** (see firewall residual) |

| Unit | Result |
|------|--------|
| `ssh.service` | **ACTIVE** |
| `nginx.service` | **ACTIVE** |
| `x-ui.service` | **ACTIVE** (Xray **26.7.28** child) |
| FAILED/DEGRADED critical units | **none observed** |

Panel control-plane path remains nginx `:443` → localhost panel (secret path **not** disclosed here). nginx `/` returns expected **404** (no site root content).

---

## 14. Firewall state

| Field | Value |
|-------|--------|
| UFW | **active**; default deny incoming / allow outgoing |
| Allowed public | **3333/tcp**, **443/tcp**, **8443/tcp** (+ v6 twins) |
| `20901` in UFW allow list | **NO** |
| Host self-test `92.42.99.126:20901` | **Connection refused** (localhost-only bind) |
| Host self-test `127.0.0.1:20901` | OPEN |

**Residual / unexpected surface:** workstation HTTP to `92.42.99.126:2096` returned `HTTP/1.0 404` from x-ui subscription listener despite UFW not listing `2096/tcp`. Treat as **pre-existing 3X-UI default bind residual**, not proven as introduced by Plus upgrade. **Do not harden in this wave** — schedule for P2 / dedicated firewall-bind wave. Intended public surface remains 3333/443/8443.

---

## 15. DNS / TLS

| Check | Result |
|-------|--------|
| DNS A `metacode-cloud.com` | **92.42.99.126** |
| Public TLS `:443` | **PASS** — CN/SAN `metacode-cloud.com`, Let's Encrypt, verify passed, TLS1.3 |
| Public TLS `:8443` | **PASS** — same cert family; local openssl verify return **0**; ALPN `http/1.1` observed |
| Cert validity window | 2026-08-29 → 2026-11-27 |

---

## 16. VPN transport smoke

| Check | Result |
|-------|--------|
| Explicit proxy | `http://127.0.0.1:10808` |
| Egress ipify | **92.42.99.126** |
| Egress ifconfig.me | **92.42.99.126** |
| HTTPS (google generate_204) | **204** |
| Medium body (OVH 1MiB via proxy) | **PASS** (1048576 bytes) |
| Cloudflare speed `__down` | 403 (endpoint policy; not treated as VPN fail) |
| Profile mutation | **0** |

**VPN transport smoke:** **PASS** (post-upgrade smoke only; not a new full acceptance campaign).

---

## 17. Cursor workload smoke

This reconciliation completed multiple meaningful local + SSH read operations without reconnect loop / interrupted tool flow.

**CURSOR POST-UPGRADE SMOKE = PASS**  
Does **not** promote long-term soak / PRODUCTION_ACCEPTED.

---

## 18. Resource headroom

Based on **actual** guest resources (not panel marketing):

| Workload near-term | Fit |
|--------------------|-----|
| Xray + 3X-UI + nginx + SSH | Fits; load idle |
| Backup jobs (light) | Marginal but feasible with ~6G free disk / ~0.5G avail RAM |
| Lightweight monitoring | Possible if sparse |
| Additional VPN identities / reserve inbound | Possible at small scale |
| PostgreSQL / n8n co-host | **Do not assume** — still ~1 GiB RAM / 1 vCPU |

**HEADROOM:** **ADEQUATE** for current VPN control role only; **LOW** if assuming multi-app host. Plus upgrade **did not** improve guest headroom yet.

---

## 19. Inventory update

Updated:

- `X:\AI MARS\projects\mars-server-ops\SERVER-INVENTORY-v1.md`  
- Local safe metadata under `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\`

Recorded: tariff claim Plus; guest vCPU/RAM/disk unchanged; swap none; reconciliation PARTIAL; lifecycle still OPERATIONAL-CANDIDATE.

---

## 20. Remaining actions

1. Operator: persist **exact Plus panel SKU numbers** (vCPU/RAM/disk claimed) into local contour.  
2. Provider/control action: determine why guest still sees Start-class resources (panel-only change vs need reboot/hotplug vs wrong VM).  
3. After guest shows enlarged disk/CPU/RAM: if disk enlarged but FS not claimed → dedicated expansion wave (**B** path).  
4. Only after resources match Plus truth: **P1 PRE-HARDENING BACKUP + RESTORE ANCHOR**.  
5. Later P2: bind/close `2096` public residual; swap review; hardening — **not this wave**.

**Do not** expand filesystem, reboot, or harden under this charter.

---

## 21. Evidence paths

| Kind | Path |
|------|------|
| Local recon dump | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\plus-post-upgrade-recon-20260830T071328Z\` |
| Recon orchestrator | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\run-plus-post-upgrade-recon.py` |
| Pre-upgrade baseline | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\build-01-control-node\pre-baseline-20260829T174340Z.json` |
| This report | `X:\AI MARS\projects\mars-server-ops\reports\MARS-SERVER-OPS-FRIENDHOSTING-PLUS-POST-UPGRADE-RECONCILIATION-01.md` |

Secrets / UUID / panel path / passwords: **not** stored in this report.

---

## 22. Mutation / Git closeout

| Control | Value |
|---------|--------|
| VEESP mutation | **0** |
| EQVPS mutation | **0** |
| FriendHosting service mutation | **0** |
| FriendHosting network mutation | **0** |
| FriendHosting filesystem resize | **0** |
| Windows network mutation | **0** |
| Secret disclosure | **0** |
| Foreign WIP mutation | **0** |
| commit / push | **0** |

Foreign WIP under other programmes left untouched. Unpushed commits may already exist on `mars/canonical-post-recovery` from unrelated work — this wave adds **no** commit.

---

## NEXT-WAVE DECISION

**C. PLUS RECONCILIATION FAIL**  
→ resolve provider/resource presentation issue before further FriendHosting work (P1 backup/hardening deferred until guest-visible Plus capacity is proven).

---

*FriendHosting Plus post-upgrade reconciliation 01 · 2026-08-30 · STOP.*

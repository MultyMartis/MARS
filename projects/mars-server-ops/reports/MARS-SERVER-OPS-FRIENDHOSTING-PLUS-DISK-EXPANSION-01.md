# REPORT — MARS Server Ops FriendHosting Plus Disk Expansion 01

**Date (UTC):** 2026-08-30  
**Wave:** FRIENDHOSTING-PLUS-DISK-EXPANSION-01  
**Capture ts:** `20260830T083148Z`  
**Target:** FRIENDHOSTING-DE / FriendHosting Germany / `92.42.99.126` / `metacode-cloud.com`  
**Verdict:** **PASS**  
**Storage case:** **A — FULLY AUTO-EXPANDED**  
**Guest storage mutation:** **NONE** (not required)

---

## 1. Executive verdict

Provider-side disk expansion is **guest-visible** and **complete**. Ubuntu sees `/dev/sda` at **20 GiB**; root partition `/dev/sda1` and ext4 already consume the enlarged capacity. No `growpart` / `resize2fs` was required. Plus compute (**2 vCPU / ~1.9 GiB**) unchanged. SSH / nginx / 3X-UI / Xray / TLS / VPN regression **PASS**. Residual `*:2096` remains **PRESENT** and was **not** mutated.

| Gate | Result |
|------|--------|
| Provider disk work | **CONFIRMED** (operator ticket + guest geometry) |
| Backup / restore readiness | **CONFIRMED** |
| Storage case | **A** |
| Guest partition growth | **NOT REQUIRED** |
| Guest filesystem growth | **NOT REQUIRED** |
| Service / VPN regression | **PASS** |
| Lifecycle | **CONTROL / OPERATIONAL-CANDIDATE** (unchanged) |

**NEXT:** **FRIENDHOSTING P2 OPERATIONAL HARDENING** (separate charter). Hardening **not** executed in this wave.

---

## 2. Provider work confirmation

| Item | Evidence |
|------|----------|
| Operator ticket | Support replied «Начинаю работы.» then «Готово.» |
| Provider claim | Disk expansion completed by FriendHosting |
| Guest proof | `/dev/sda` **21474836480** B (**20 GiB**) vs prior **10737418240** B (**10 GiB**) |
| Rescan | **Not needed** (new size visible without SCSI rescan) |
| Provider work status | **CONFIRMED** |

---

## 3. Pre-provider storage baseline

From prior Plus panel-reboot gate / recon (before provider disk work):

| Field | Value |
|-------|--------|
| Virtual disk `/dev/sda` | **10 GiB** (10737418240 B) |
| Root partition `sda1` | ≈ **9 GiB** |
| Root filesystem ext4 | ≈ **8.7 GiB** |
| Free (approx) | ≈ **5.8–6.1 GiB** class |

---

## 4. Backup / restore gate

| Check | Result |
|-------|--------|
| Local archive | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-plus-pre-panel-reboot-20260830T073335Z.tgz` |
| Local size | **80613337** bytes |
| Local SHA-256 | `04344ea5fb7d90086360753060197a2e2371f063f0efbef60bd713efe96ff002` |
| Remote archive | `/root/mars-backups/friendhosting-plus-pre-panel-reboot-20260830T073335Z.tgz` |
| Remote SHA-256 | `04344ea5fb7d90086360753060197a2e2371f063f0efbef60bd713efe96ff002` |
| Hash match remote/local/expected | **YES** |
| `tar` readability (local + remote list) | **PASS** |
| Restore strategy | **CONFIRMED** — `projects/mars-server-ops/evidence/FRIENDHOSTING-PLUS-CONTROL-PANEL-REBOOT-GATE-01/RESTORE-STRATEGY.md` |

Gate satisfied **before** any storage mutation decision. Mutation ultimately **not** performed.

---

## 5. Post-provider block-device state

| Field | Value |
|-------|--------|
| `blockdev --getsize64 /dev/sda` | **21474836480** B |
| Human | **20 GiB** |
| `lsblk` | `sda` **20G** disk |
| Layout | GPT: `sda1` (root), `sda14` (4M), `sda15` (`/boot/efi` 106M vfat), `sda16` (`/boot` 913M ext4) |

Provider enlargement **visible** to the guest.

---

## 6. Partition state

| Field | Value |
|-------|--------|
| Root partition | `/dev/sda1` |
| `blockdev --getsize64 /dev/sda1` | **20398997504** B |
| Human (`lsblk`) | **19G** |
| Mount | `/` |

Partition already larger than the pre-provider ~9 GiB baseline.

---

## 7. Filesystem state

| Field | Value |
|-------|--------|
| Type | **ext4** on `/dev/sda1` |
| Block size | **4096** |
| Block count | **4980224** |
| Filesystem size | **20398997504** B (= partition size) |
| Free blocks | **4044623** → **16566775808** B free (~15.43 GiB) |
| Filesystem state | **clean** |
| `df -hT /` | Size **19G** · Used **3.0G** · Avail **16G** · **16%** |
| `findmnt /` | Size **18.3G** · Used **2.9G** · Avail **15.4G** · **16%** |

Filesystem already matches partition capacity (no resize pending).

---

## 8. Storage case classification

**CASE A — FULLY AUTO-EXPANDED**

| Layer | Grown vs pre-provider? |
|-------|------------------------|
| `/dev/sda` | **YES** (10 → 20 GiB) |
| `/dev/sda1` | **YES** (~9 Gi → ~19 Gi) |
| ext4 | **YES** (~8.7G → ~19G / 18.3G findmnt) |

No guest-side storage mutation required.

---

## 9. Guest-side mutation, if any

| Action | Result |
|--------|--------|
| SCSI / block rescan | **NOT PERFORMED** (size already visible) |
| `growpart` | **NOT REQUIRED** / not run |
| `resize2fs` | **NOT REQUIRED** / not run |
| Partition table rewrite | **0** |
| Format / delete / fdisk destructive | **0** |
| Reboot | **0** |

FriendHosting storage mutation this wave: **none** (inspection-only).

---

## 10. Final storage capacity

| Metric | BEFORE provider | AFTER (guest) |
|--------|-----------------|---------------|
| Virtual disk | 10 GiB (10737418240 B) | **20 GiB (21474836480 B)** |
| Root partition | ≈ 9 GiB | **20398997504 B (~19 Gi)** |
| Root ext4 | ≈ 8.7 GiB | **20398997504 B** (`df` **19G** / `findmnt` **18.3G**) |
| Used | (prior ~2–3G class) | **~3.0G** (`df`) / **2.9G** (`findmnt`) |
| Free / avail | ≈ 5.8–6.1 GiB | **~16G** (`df`) / **15.4G** (`findmnt`) |
| Use % | (higher prior) | **16%** |

---

## 11. CPU / RAM regression

| Field | Value | Gate |
|-------|--------|------|
| `nproc` / CPU(s) | **2** | PASS |
| Model | Common KVM processor | — |
| MemTotal | **2014844** kB (~1.9 Gi) | PASS |
| Swap | **none** (0 kB) | unchanged |
| Regression to Start (1 vCPU / ~961 Mi) | **NO** | PASS |

---

## 12. SSH regression

| Check | Result |
|-------|--------|
| Listener `0.0.0.0:3333` / `[::]:3333` | **PASS** (`sshd` + systemd) |
| `systemctl is-active ssh` | **active** |
| Agent SSH session this wave | **PASS** |

---

## 13. nginx regression

| Check | Result |
|-------|--------|
| Listener `:443` | **PASS** |
| `systemctl is-active nginx` | **active** |
| Workstation TLS `:443` SNI `metacode-cloud.com` | **PASS** (TLSv1.3, verify OK) |

---

## 14. 3X-UI regression

| Check | Result |
|-------|--------|
| Bind `127.0.0.1:20901` | **PASS** (`x-ui`) |
| Public bind of 20901 | **absent** (localhost only) |
| `systemctl is-active x-ui` | **active** |
| Localhost HTTP probe | responds (404 on `/` without panel path — expected) |

---

## 15. Xray / VPN regression

| Check | Result |
|-------|--------|
| Listener `*:8443` (`xray-linux-amd64`) | **PASS** |
| Host openssl verify `:8443` | **Verify return code: 0 (ok)** |
| Workstation TLS `:8443` | **PASS** |
| Profile | `MCA-ONE-FRIENDHOSTING-DE-RAW-8443` (existing; not modified) |
| Local SOCKS `127.0.0.1:10808` → ipify | **92.42.99.126** |
| Local SOCKS → ifconfig.me | **92.42.99.126** |
| HTTPS body transfer (`example.com` via proxy) | **HTTP 200** |
| VPN smoke | **PASS** |
| v2rayN mutation | **0** |

---

## 16. Firewall

| Check | Result |
|-------|--------|
| UFW | **active**; default deny incoming |
| Allowed public | **3333/tcp**, **443/tcp**, **8443/tcp** (+ v6) |
| Panel 20901 public | **NO** (localhost only) |
| Firewall mutation this wave | **0** |

---

## 17. TLS / DNS

| Check | Result |
|-------|--------|
| DNS A `metacode-cloud.com` | **92.42.99.126** |
| nginx `:443` TLS | **PASS** · verify **0** |
| Xray `:8443` TLS | **PASS** · verify **0** |
| Cert CN | `metacode-cloud.com` |
| Validity window (host openssl) | 2026-08-29 → 2026-11-27 |

---

## 18. Cursor smoke

Multiple meaningful operations completed after storage inspection (SSH inspect, TLS probes, VPN HTTPS) without reconnect loops.

**CURSOR STORAGE-WAVE SMOKE = PASS**  
Not a long-term soak claim.

---

## 19. Final Plus hardware baseline

Canonical post-upgrade hardware baseline for the next hardening wave:

| Field | Value |
|-------|--------|
| Tariff | **Plus** |
| vCPU | **2** |
| RAM | **~1.9 GiB** (MemTotal **2014844** kB) |
| Virtual disk | **20 GiB** (`/dev/sda` = 21474836480 B) |
| Root partition | **~19 Gi** (`/dev/sda1` = 20398997504 B) |
| Root ext4 | **~19G** (`df`) / **18.3G** (`findmnt`) |
| Free capacity | **~16G** (`df` Avail) / **15.4G** (`findmnt`) |
| Use % | **16%** |
| Swap | **none** |

Local note: `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\plus-final-hardware-baseline-20260830T083148Z.md`

---

## 20. Known `:2096` residual

| Item | Status |
|------|--------|
| Listener | `*:2096` (`x-ui`) **PRESENT** |
| Workstation HTTP | `404 page not found` |
| UFW explicit allow 2096 | **absent** |
| Mutation this wave | **NOT MUTATED** |

Schedule bind/firewall hardening under **P2**.

---

## 21. Inventory / local-contour updates

| Path | Update |
|------|--------|
| `projects/mars-server-ops/SERVER-INVENTORY-v1.md` | FRIENDHOSTING-DE acceptance + hardware baseline + evidence ref |
| `projects/mars-server-ops/OPERATIONAL-INDEX.md` | Disk wave COMPLETE; next = P2 hardening |
| `local/infrastructure/FRIENDHOSTING-GERMANY/node-identity.local.md` | Disk expansion facts appended |
| `local/.../plus-final-hardware-baseline-20260830T083148Z.md` | Baseline note created |
| `local/.../plus-disk-expansion-01-20260830T083148Z/` | Full capture tree |

---

## 22. Evidence paths

| Locus | Path |
|-------|------|
| Local capture | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\plus-disk-expansion-01-20260830T083148Z\` |
| Git-safe evidence copy | `X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-PLUS-DISK-EXPANSION-01\` |
| Summary JSON | `...\plus-disk-expansion-01-20260830T083148Z\summary.json` |
| Control script (local only) | `...\FRIENDHOSTING-GERMANY\run-plus-disk-expansion-01.py` |
| Prior restore strategy | `projects/mars-server-ops/evidence/FRIENDHOSTING-PLUS-CONTROL-PANEL-REBOOT-GATE-01/RESTORE-STRATEGY.md` |

Secret disclosure in evidence: **0** (password/UUID/URI redacted).

---

## 23. Mutation / Git closeout

| Item | Value |
|------|--------|
| VEESP mutation | **0** |
| EQVPS mutation | **0** |
| FriendHosting storage mutation | **0** (CASE A — inspection only) |
| FriendHosting config mutation | **0** |
| FriendHosting reboot | **0** |
| FriendHosting hardening mutation | **0** |
| Windows network mutation | **0** |
| Secret disclosure | **0** |
| Foreign WIP mutation | **0** |
| commit / push | **0** |

Foreign WIP in repo remains out of scope (iseo / forge-wordpress dirty trees untouched).

---

*MARS Server Ops · FRIENDHOSTING-PLUS-DISK-EXPANSION-01 · 2026-08-30 · PASS / CASE A*

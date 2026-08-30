# MARS SERVER OPS — DUAL LOCAL OPERATIONAL BACKUP FRIENDHOSTING + VEESP 01

**Wave:** DUAL-LOCAL-OPERATIONAL-BACKUP-01  
**Stamp:** `20260830T132309Z`  
**Verdict:** **PASS**  
**Evidence:** [../evidence/DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01/](../evidence/DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01/)  
**Summary JSON:** [../evidence/DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01/Z-summary.json](../evidence/DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01/Z-summary.json)

---

## 1. Executive verdict

Fresh operational backups of **FRIENDHOSTING-DE** and **VEESP / MCA-VPN-001** were created remotely, copied as verified local twins under `X:\AI MARS\local\infrastructure\`, and hash-validated (remote SHA-256 = local SHA-256). Pre/post service health gates **PASS** on both nodes. No VPN/config mutation, reboot, admin credential change, secret disclosure, foreign WIP mutation, or commit/push.

| Gate | Result |
|------|--------|
| Dual local operational backup | **PASS** |
| FriendHosting backup + twin | **PASS** |
| VEESP backup + twin | **PASS** |
| FriendHosting restore strategy | **CONFIRMED** (procedure exists; bare-metal **NOT EXERCISED**) |
| VEESP restore strategy | **CONFIRMED** (new runbook; bare-metal **NOT EXERCISED**) |
| Service regression FriendHosting | **PASS** |
| Service regression VEESP | **PASS** |

---

## 2. Backup purpose

Take verified local copies of both working VPN servers **before** the next VEESP 3X-UI admin-hardening wave, and measure exact X: footprint of the new archives and existing local backup directories.

---

## 3. X: free space before

| Metric | Value |
|--------|-------|
| Captured UTC | `2026-08-30T13:23:09Z` |
| Volume label | `AI WS` |
| Total bytes | **505732395008** (~470.999996 GiB) |
| Free bytes | **111451729920** |
| Free MiB | **106288.652344** |
| Free GiB | **103.797512** |

---

## 4. FriendHosting health

Pre-backup (read-only):

| Check | Result |
|-------|--------|
| SSH `:3333` | PASS |
| nginx `:443` | PASS |
| 3X-UI | PASS |
| Xray `:8443` | PASS |
| TLS (`:443` / `:8443`) | PASS |
| UFW | PASS |
| fail2ban | PASS |
| Client count | **6** (labels present; no legacy) |

Classification: **HEALTHY / FINAL-compatible** for operational backup.

---

## 5. FriendHosting backup

| Field | Value |
|-------|-------|
| Archive | `friendhosting-operational-20260830T132309Z.tgz` |
| Remote | `/root/mars-backups/friendhosting-operational-20260830T132309Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-operational-20260830T132309Z.tgz` |
| Scope | Accepted operational set (3X-UI/DB, Xray runtime, nginx, Let's Encrypt, SSH, UFW, fail2ban, sudo, fstab/swap, journald, package inventory, clients-safe metadata) |
| Members (tar list) | 340 |

---

## 6. FriendHosting validation / hash

| Check | Result |
|-------|--------|
| Remote exists / non-zero | PASS — **80743234** bytes |
| Local exists / non-zero | PASS — **80743234** bytes |
| Archive list/read | PASS |
| Required sections present | PASS |
| Client count in archive metadata | 6 |
| SHA-256 remote | `a434c1fdd178c3df133b74b503e8298b150a6640727c15d89aee341b9bf6e617` |
| SHA-256 local | `a434c1fdd178c3df133b74b503e8298b150a6640727c15d89aee341b9bf6e617` |
| Remote/local match | **YES** |

Archive contents are **not** disclosed in Git.

---

## 7. VEESP live-state audit

Live truth at backup (do **not** assume historical WS-era stack):

| Field | Live value |
|-------|------------|
| Hostname | `wsp-cloud` |
| OS | Ubuntu 22.04.5 LTS |
| Kernel | `5.15.0-187-generic` |
| Domain / IPv4 | `wsp-cloud.com` → `178.173.250.69` |
| SSH | `:22` PASS |
| VPN architecture | **VLESS + TLS + RAW/TCP `:8443`** PASS |
| Xray binary | `/usr/local/x-ui/bin/xray-linux-amd64` |
| Xray version | **26.6.22** |
| 3X-UI / x-ui | active PASS |
| TLS material | `/root/cert/wsp-cloud.com/` present; notAfter **Nov 11 08:03:40 2026 GMT** |
| nginx | **ABSENT** |
| `/etc/letsencrypt` | **ABSENT** |
| UFW | inactive (historical posture) |
| fail2ban | active |
| Inbounds (safe) | VLESS `:8443` (**8** clients) + Reality inbound present |
| Panel bind exposure | public panel listeners observed historically — details **local-secret only**; hardening = **NEXT wave** |

Note: localhost panel curl probe on a historical port was UNREACHABLE during automated gate; SSH + `x-ui` active + `:8443` listen/TLS still **PASS**.

---

## 8. VEESP backup

| Field | Value |
|-------|-------|
| Archive | `veesp-operational-20260830T132309Z.tgz` |
| Remote | `/root/mars-backups/veesp-operational-20260830T132309Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-operational-20260830T132309Z.tgz` |
| Scope | Current stack only: 3X-UI/DB, Xray app tree, `/root/cert` TLS, SSH, fstab, firewall/fail2ban dumps as present, systemd/package inventory, clients-safe metadata — **no invented nginx/LE trees** |
| Members (tar list) | 289 |

Local contour used existing root: `X:\AI MARS\local\infrastructure\MCA-VPN-001\` (created `backups\` under it; no duplicate provider root).

---

## 9. VEESP validation / hash

| Check | Result |
|-------|--------|
| Remote exists / non-zero | PASS — **83967532** bytes |
| Local exists / non-zero | PASS — **83967532** bytes |
| Archive list/read | PASS |
| Expected components | PASS (x-ui, DB, TLS material, ssh, clients-safe) |
| SHA-256 remote | `d10b67cb1b8a9e0beb4a131a583eee1af56cb153e4513d1e599f6e8bba9112c8` |
| SHA-256 local | `d10b67cb1b8a9e0beb4a131a583eee1af56cb153e4513d1e599f6e8bba9112c8` |
| Remote/local match | **YES** |

---

## 10. Restore-strategy state

| Server | BACKUP | RESTORE STRATEGY | Bare-metal |
|--------|--------|------------------|------------|
| FriendHosting | **PASS** | **CONFIRMED** — [FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md](../runbooks/FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md); scope compatible with this stamp | **NOT EXERCISED** |
| VEESP | **PASS** | **CONFIRMED** — [VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md](../runbooks/VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md) created/aligned to this stamp | **NOT EXERCISED** |

Do **not** claim `BARE-METAL RESTORE TESTED`.

---

## 11. Local archive sizes

Binary units: 1 MiB = 1024²; 1 GiB = 1024³.

| Archive | Bytes | MiB | GiB |
|---------|-------|-----|-----|
| FriendHosting | **80743234** | **76.988647** | **0.075184** |
| VEESP | **83967532** | **80.077679** | **0.078201** |

---

## 12. Combined new-backup footprint

| Metric | Value |
|--------|-------|
| Exact bytes | **164710766** |
| MiB | **157.080427** |
| GiB | **0.153399** |

---

## 13. Existing local-backup-directory footprint

No cleanup / no deletes in this wave.

| Directory | Archives (`.tgz`) | Total bytes | GiB |
|-----------|-------------------|-------------|-----|
| `...\FRIENDHOSTING-GERMANY\backups` | **10** | **498452697** | **0.46422** |
| `...\MCA-VPN-001\backups` | **1** | **83967532** | **0.078201** |
| Combined both dirs | — | **582420229** | **0.542421** |

---

## 14. X: free space after

| Metric | Value |
|--------|-------|
| Captured UTC | `2026-08-30T13:24:37Z` |
| Free bytes | **111286951936** |
| Free MiB | **106131.507812** |
| Free GiB | **103.644051** |

---

## 15. Actual X: free-space delta

| Metric | Value |
|--------|-------|
| before − after (bytes) | **164777984** |
| New archives sum (bytes) | **164710766** |
| Difference | **67218** |

Slight excess over archive sum is expected: local `.sha256` sidecars, evidence writes under the programme tree, and filesystem allocation / concurrent volume activity. Not treated as backup failure.

---

## 16. Service regressions

| Node | Checks | Result |
|------|--------|--------|
| FriendHosting | SSH / nginx / 3X-UI / Xray `:8443` / TLS / UFW / fail2ban / 6 clients | **PASS** |
| VEESP | SSH / 3X-UI / Xray `:8443` listen / VLESS RAW+TLS / TLS notAfter | **PASS** |

Config mutation = **0** on both.

---

## 17. Inventory updates

Updated:

- [SERVER-INVENTORY-v1.md](../SERVER-INVENTORY-v1.md) — latest dual-backup stamps, paths, sizes, SHA match, restore status  
- [FRIENDHOSTING-DE-BACKUP-RESTORE-STATE-v1.md](../assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-BACKUP-RESTORE-STATE-v1.md) — current operational twin `20260830T132309Z` (prior final freeze retained as historical)  
- [BACKUP-STATE-v1.md](../assets/MCA-VPN-001/BACKUP-STATE-v1.md) — current verified operational backup section  

No secrets recorded.

---

## 18. Next VEESP 3X-UI admin-hardening wave

**DO NOT EXECUTE in this wave.**

Planned next: **VEESP 3X-UI ADMIN ACCESS HARDENING 01**

1. Audit current VEESP 3X-UI access  
2. Use this VEESP backup as rollback  
3. Change operator panel login  
4. Change operator panel password  
5. Verify secret web path / bind / exposure  
6. Preserve working VLESS RAW/TLS `:8443`  
7. Validate panel + VPN afterward  
8. Update local secret contour and MARS safe docs  

---

## 19. Evidence paths

| Item | Path |
|------|------|
| Evidence root | `X:\AI MARS\projects\mars-server-ops\evidence\DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01\` |
| Summary | `...\Z-summary.json` |
| Helper | `X:\AI MARS\projects\mars-server-ops\tools\dual-local-backup\dual-local-operational-backup-01.py` |
| FH local twin | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-operational-20260830T132309Z.tgz` |
| VE local twin | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-operational-20260830T132309Z.tgz` |
| VE restore runbook | `X:\AI MARS\projects\mars-server-ops\runbooks\VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md` |

---

## 20. Git / mutation closeout

| Item | Value |
|------|-------|
| FriendHosting config mutation | **0** |
| VEESP config mutation | **0** |
| FriendHosting reboot | **0** |
| VEESP reboot | **0** |
| Secret disclosure | **0** |
| Foreign WIP mutation | **0** |
| commit / push | **0** |
| VPN mutation | **0** |
| Admin credential change | **0** |

Foreign WIP elsewhere in the repo remains **OUT OF SCOPE**.

---

*Report closed 2026-08-30 · stamp `20260830T132309Z`.*

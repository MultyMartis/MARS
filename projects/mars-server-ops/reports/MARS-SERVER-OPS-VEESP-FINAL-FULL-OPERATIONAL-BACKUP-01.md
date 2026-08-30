# REPORT — VEESP FINAL FULL OPERATIONAL BACKUP 01

**inventory_ref:** MCA-VPN-001  
**Provider:** VEESP  
**IPv4 / domain:** `178.173.250.69` / `wsp-cloud.com`  
**Wave date (UTC):** 2026-08-30  
**Overall:** **PASS**  
**Commit/push:** **0** (not authorized)

---

## 1. Verdict

| Item | Result |
|------|--------|
| BACKUP | **PASS** |
| RESTORE PROCEDURE | **CONFIRMED** (written; not destructively drilled) |
| BARE-METAL RESTORE | **NOT YET EXERCISED** |
| Preferred stamp | `veesp-final-operational-20260830T184024Z` |
| Remote/local SHA-256 | **MATCH** |
| Archive readability | **PASS** |
| Config / client / reboot mutation | **0** / **0** / **0** |
| FriendHosting mutation | **0** |

This archive is the **preferred current VEESP recovery baseline** after 3X-UI **3.7.0**, Xray **26.7.28**, credential rotation, KEY-ONLY SSH, UFW, fail2ban, swap, journald cap, and accepted panel residuals.

---

## 2. Current accepted VEESP state

| Item | Value |
|------|--------|
| 3X-UI | **3.7.0** |
| Xray | **26.7.28** |
| VPN | VLESS + TLS + RAW/TCP **`:8443`** — REAL-WORKLOAD **PASS** |
| Clients `:8443` | **8** |
| Reality `:46489` | **1** client |
| MTProto `:8445` | Docker present |
| Panel `:5928` | PUBLIC TLS-DIRECT — **ACCEPTED RESIDUAL** |
| Subscription `:2096` | PUBLIC — **UNUSED UNPROVEN** |
| nginx | **ABSENT** |
| SSH | KEY-ONLY (`marsops` + root recovery); PasswordAuthentication **disabled** |
| UFW | **ACTIVE** |
| fail2ban | **PASS** |
| Swap | **1 GiB** |
| journald | `SystemMaxUse=300M` |
| Reboot | **NOT** performed (`reboot-required` may remain set) |

---

## 3. Pre-backup health

| Check | Result |
|-------|--------|
| SSH / marsops key / sudo | **PASS** |
| UFW ACTIVE | **PASS** |
| fail2ban | **PASS** |
| 3X-UI / panel TLS `:5928` | **PASS** |
| Xray / TCP+TLS `:8443` | **PASS** |
| VLESS client count | **8** (unchanged vs gate) |
| Swap active | **PASS** |
| journald cap present | **PASS** |

Critical services healthy → backup proceeded.

---

## 4. Backup scope

Scoped operational archive (not whole-root). Included where present:

- `/etc/x-ui/` (DB, settings, admin credential state, inbounds/clients, subscription config)
- `/usr/local/x-ui/` (application + managed Xray binary/version)
- TLS under `/root/cert/`
- `/etc/ssh/`, sudoers for ops account, authorized_keys patterns (server-side)
- UFW + relevant firewall evidence
- fail2ban config/jails
- fstab / swap / journald / logrotate / systemd units relevant to stack
- package/version inventory + listener baseline evidence bundle

Unrelated user data / full root FS **not** archived.

Tool: `projects/mars-server-ops/tools/veesp-final-backup/veesp-final-full-operational-backup-01.py`  
Evidence: `projects/mars-server-ops/evidence/VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01/`

---

## 5. Remote / local archives

| Field | Value |
|-------|--------|
| Stamp | `20260830T184024Z` |
| Remote | `/root/mars-backups/veesp-final-operational-20260830T184024Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-final-operational-20260830T184024Z.tgz` |
| Bytes | **81065422** |
| MiB | **~77.31** |
| GiB | **~0.0755** |
| Members | **333** |
| Secret-bearing | **YES** — never place in Git |

---

## 6. Hash / readability

| Check | Result |
|-------|--------|
| SHA-256 | `b15631b7d1519fbd8364b73541fbf6e240f5e1032b0b44ef49fc34725bc80cec` |
| Remote/local match | **YES** |
| Archive list/read | **PASS** |
| Expected sections present | **PASS** |

---

## 7. Restore-state reconciliation

Updated:

- [BACKUP-STATE-v1.md](../assets/MCA-VPN-001/BACKUP-STATE-v1.md) — preferred `0final`
- [VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md](../runbooks/VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md)
- Passport / inventory / OPERATIONAL-INDEX

**Preferred restore semantics (this stamp):** 3X-UI **3.7.0**; Xray **26.7.28**; rotated admin DB; KEY-ONLY SSH; UFW; fail2ban; swap; journald; public `:5928` / `:2096`; ports **22 / 8443 / 46489 / 5928 / 2096 / 8445**.

**Historical (retained, not preferred):** post-hardening, pre-hardening, post-upgrade, pre-upgrade, operational, pre-cred — may restore older app/Xray versions, old credentials, or pre-UFW/SSH-hardening state.

Older archives **not deleted**.

---

## 8. Backup storage footprint

| Location | Count / size |
|----------|----------------|
| New final archive | **81065422** B (~0.0755 GiB) |
| `MCA-VPN-001\backups\` `*.tgz` | **7** archives · **492305582** B (~0.458 GiB) |
| FriendHosting backups (optional cheap peek) | ~10 archives · ~0.464 GiB — **not** audited this wave |

---

## 9. Post-backup regression

| Check | Result |
|-------|--------|
| SSH | **PASS** |
| UFW | **PASS** |
| fail2ban | **PASS** |
| 3X-UI | **PASS** |
| Xray | **PASS** |
| VLESS `:8443` | **PASS** |
| Panel `:5928` | **PASS** |
| `:2096` | unchanged PUBLIC / UNUSED UNPROVEN |
| Client count `:8443` | **8 UNCHANGED** |

Server configuration intentionally unchanged by this wave.

---

## 10. Next roadmap

VEESP: **STABLE / ACCEPTED CURRENT VPN WORKLOAD** with documented panel residuals.

**Next programme wave (do not execute here):**  
**FRIENDHOSTING + VEESP SOAK / LIGHTWEIGHT MONITORING 01**

P4 `:24443` remains **DEFERRED**.

---

## 11. Git / mutation closeout

| Item | Value |
|------|--------|
| FriendHosting mutation | **0** |
| VEESP config mutation | **0** |
| VEESP client mutation | **0** |
| VEESP reboot | **0** |
| Secret disclosure | **0** |
| Foreign WIP mutation | **0** |
| commit / push | **0** |

Docs updated under `projects/mars-server-ops/` only. Local secret-bearing twin under `local/infrastructure/MCA-VPN-001/backups/` (Git-excluded contour).

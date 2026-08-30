# VEESP / MCA-VPN-001 — Operational Restore Procedure v1

**inventory_ref:** MCA-VPN-001  
**Provider:** VEESP  
**Status:** RESTORE PROCEDURE **CONFIRMED** (written against hash-validated operational backups)  
**Bare-metal / destructive restore drill:** **NOT YET EXERCISED**  

**Preferred current restore baseline (FINAL FULL OPERATIONAL):** `veesp-final-operational-20260830T184024Z.tgz`  
**SHA-256:** `b15631b7d1519fbd8364b73541fbf6e240f5e1032b0b44ef49fc34725bc80cec`  
**Size:** **81065422** bytes  
**Remote:** `/root/mars-backups/veesp-final-operational-20260830T184024Z.tgz`  
**Local twin:** `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-final-operational-20260830T184024Z.tgz`  

**Historical post–system-security twin (superseded as preferred):** `veesp-post-system-hardening-20260830T163612Z.tgz` — SHA-256 `1857afff8dbc087540b252394438115a9babb1b42c212c03137c4d41e7d920d7`  

**Pre-hardening rollback twin:** `veesp-pre-system-hardening-20260830T162532Z.tgz` — SHA-256 `ec201264ef9ef0062ec19fa67c3c7bb56c6522b803c6ed1842c77e6ef497b7a7`  

**Historical application backup (post 3X-UI 3.7.0 upgrade):** `veesp-xui-postupgrade-20260830T155842Z.tgz` — SHA-256 `97ee0394a308f827b9798d748c86f740ec8b2501a0c60712c7927913db5389d0`  

**Pre-upgrade rollback twin (3.4.1):** `veesp-xui-preupgrade-20260830T154548Z.tgz` — SHA-256 `ae78f5ef548bdbcea0677c259d949698ae66941a5ebe8b95f3b6e9e11b5aac5b`  

**Broader operational inventory twin (pre-upgrade era):** `veesp-operational-20260830T132309Z.tgz` — SHA-256 `d10b67cb1b8a9e0beb4a131a583eee1af56cb153e4513d1e599f6e8bba9112c8`  
**Related model:** [BACKUP-RESTORE-MODEL-v1.md](../BACKUP-RESTORE-MODEL-v1.md)  
**Final backup wave:** [MARS-SERVER-OPS-VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01.md](../reports/MARS-SERVER-OPS-VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01.md)  
**Panel exposure:** [MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md](../reports/MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md)  
**System security wave:** [MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md](../reports/MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md)  
**Upgrade wave:** [MARS-SERVER-OPS-VEESP-3XUI-UPGRADE-PANEL-EXPOSURE-HARDENING-01.md](../reports/MARS-SERVER-OPS-VEESP-3XUI-UPGRADE-PANEL-EXPOSURE-HARDENING-01.md)

---

## 1. Purpose

Restore the **current** VEESP VPN operational stack (VLESS + TLS + RAW/TCP `:8443`) after configuration loss, panel/DB corruption, TLS material loss, accidental mutation, or host-security misconfiguration.

This is a **human-operated** scoped restore. It is **not** an automated DR product and **not** proof of full bare-metal recovery until a destructive drill is chartered and evidenced.

**Do not** assume historical WS-era procedures are current.

---

## 2. Accepted target state (post-restore PASS criteria)

| Item | Expected (live truth for preferred final stamp `20260830T184024Z`; older stamps differ) |
|------|-----------------------------------------------------|
| Hostname | `wsp-cloud` |
| OS | Ubuntu 22.04.5 LTS |
| Domain / IPv4 | `wsp-cloud.com` → `178.173.250.69` |
| SSH | `:22`; KEY-ONLY; account **`marsops`** + root key recovery; PasswordAuthentication **no**; PermitRootLogin **without-password** |
| VPN | VLESS + TLS + RAW/TCP **`:8443`** |
| 3X-UI | **3.7.0** (preferred / post-upgrade stamps); **3.4.1** only when restoring pre-upgrade twin |
| Xray | **26.7.28** (preferred); **26.6.22** only on pre-upgrade / early operational twins — must match restored `/usr/local/x-ui` |
| Panel | PUBLIC TLS-DIRECT `:5928` **ACCEPTED RESIDUAL**; path/credentials **local-secret only**; nginx **ABSENT** |
| `:2096` | PUBLIC — classification **UNUSED UNPROVEN** (subscription HTTPS) |
| Additional public | `:46489` Reality; `:8445` MTProto docker-proxy |
| TLS | Certificate material under `/root/cert/wsp-cloud.com/` |
| fail2ban | active (sshd; 3x-ipl may be present) |
| UFW | **active** — allow 22, 8443, 46489, 5928, 2096, 8445 |
| Swap | `/swapfile` 1 GiB |
| journald | `SystemMaxUse=300M` (drop-in) |
| Inbounds | VLESS `:8443` (**8** clients) + Reality `:46489` (**1** client) — **do not** rotate UUIDs |
| Admin DB | Rotated credentials (preferred stamp) — secrets **local only** |

---

## 3. Prerequisites

1. Operator access to local twin and/or remote archive.  
2. Clean or damaged host with Ubuntu 22.04-class baseline (or in-place repair).  
3. Packages as needed: `openssh-server`, `fail2ban`, `ufw`, SQLite tooling, `curl`.  
4. Private SSH keys from local secret contour (never from Git).  
5. **Do not** restore into Git. Archives are **secret-bearing**.

---

## 4. Integrity check (mandatory before restore)

```text
sha256sum veesp-final-operational-20260830T184024Z.tgz
# expect: b15631b7d1519fbd8364b73541fbf6e240f5e1032b0b44ef49fc34725bc80cec

sha256sum veesp-post-system-hardening-20260830T163612Z.tgz
# expect: 1857afff8dbc087540b252394438115a9babb1b42c212c03137c4d41e7d920d7

sha256sum veesp-pre-system-hardening-20260830T162532Z.tgz
# expect: ec201264ef9ef0062ec19fa67c3c7bb56c6522b803c6ed1842c77e6ef497b7a7

sha256sum veesp-xui-postupgrade-20260830T155842Z.tgz
# expect: 97ee0394a308f827b9798d748c86f740ec8b2501a0c60712c7927913db5389d0

# pre-upgrade rollback twin:
sha256sum veesp-xui-preupgrade-20260830T154548Z.tgz
# expect: ae78f5ef548bdbcea0677c259d949698ae66941a5ebe8b95f3b6e9e11b5aac5b

# broader operational twin (pre-upgrade era):
sha256sum veesp-operational-20260830T132309Z.tgz
# expect: d10b67cb1b8a9e0beb4a131a583eee1af56cb153e4513d1e599f6e8bba9112c8
tar -tzf <archive>.tgz | head
```

Always restore **matching** `/usr/local/x-ui` + `/etc/x-ui` from the **same** archive after the 3.7.0 schema migration (tables such as `client_hwids`, `sub_balancers` appeared post-upgrade).

---

## 5. Restore order (scoped)

Work as root. Keep a second session if mutating SSH.

1. **Stop services:** `systemctl stop x-ui` (and related) before overwriting trees.  
2. **Extract staging** from the chosen archive (prefer `veesp-final-operational-20260830T184024Z` for current accepted host+app+security baseline).  
3. **TLS material:** restore `/root/cert` when present in archive (private keys — handle carefully).  
4. **3X-UI application:** restore `/usr/local/x-ui` when present.  
5. **3X-UI DB/config:** restore `/etc/x-ui`.  
6. **SSH / sudo / authorized_keys:** restore carefully; prefer diff-then-apply for `sshd`; validate `sshd -t` before reload; keep recovery session open.  
7. **UFW / fail2ban / journald / fstab-swap:** restore only if intentionally recovering security posture; re-enable UFW only after SSH allow rule is proven.  
8. **systemd:** ensure x-ui unit installed/enabled.  
9. **Reload:** `systemctl daemon-reload && systemctl start x-ui && systemctl restart fail2ban` as applicable.  
10. **Do not** invent nginx or Let's Encrypt unless separately chartered.

---

## 6. Post-restore validation

| Check | PASS signal |
|-------|-------------|
| SSH key (`marsops` / root recovery) | Login succeeds |
| Password SSH | Rejected |
| x-ui | `systemctl is-active x-ui` = active |
| UFW | active with SSH allow present |
| `:8443` listen | `ss -lntp` shows xray on 8443 |
| TLS | TLS handshake to `wsp-cloud.com:8443` OK |
| Inbound | VLESS on 8443 present in panel/DB |
| Real-workload | Operator smoke with a known client (separate from this doc) |

**Do not claim** FULL DISASTER RESTORE TESTED until a chartered bare-metal drill produces evidence.

**Credential / version caveats (2026-08-30):**

- Restoring `veesp-final-operational-20260830T184024Z.tgz` returns **preferred current** baseline: 3X-UI **3.7.0**, Xray **26.7.28**, rotated admin DB, KEY-ONLY SSH, UFW, fail2ban, swap, journald, public `:5928`/`:2096` residuals.  
- Restoring `veesp-post-system-hardening-20260830T163612Z.tgz` returns near-current host-security + **3.7.0** stack (historical; prefer final stamp).  
- Restoring `veesp-pre-system-hardening-20260830T162532Z.tgz` returns **pre-KEY-ONLY / UFW-inactive** posture — use only for SSH/firewall rollback.  
- Restoring `veesp-xui-postupgrade-20260830T155842Z.tgz` returns **3.7.0** + rotated admin DB (application-focused; may lack later host-security nuance vs final).  
- Restoring `veesp-xui-preupgrade-20260830T154548Z.tgz` returns **3.4.1** + pre-upgrade schema / older Xray.  
- Restoring `veesp-operational-20260830T132309Z.tgz` **or** `veesp-xui-precred-20260830T141517Z.tgz` restores **pre-rotation** panel credentials (and older Xray/panel era for the operational stamp). After such a restore, set admin credentials from the current **local secret** record (`X:\AI MARS\local\infrastructure\MCA-VPN-001\secrets.local.md`) or re-run `x-ui setting -username … -password …`. Do not print those values in Git or this runbook.  
- Panel residuals remain PUBLIC TLS-DIRECT `:5928` (ACCEPTED) / PUBLIC `:2096` (UNUSED UNPROVEN); do not invent nginx during restore.

---

## 7. Recovery risks

| Risk | Mitigation |
|------|------------|
| SSH lockout | Provider console; prove key path before disabling passwords; test `sshd -t` before reload |
| UFW lockout | Keep session open; `ufw --force disable` rollback; never enable without SSH allow |
| Stale/missing TLS | Confirm `/root/cert/wsp-cloud.com/` files restored |
| DB/schema mismatch | Restore matching `/usr/local/x-ui` + `/etc/x-ui` pair from **same** archive |
| Accidental WS-era restore | Use only RAW/TLS `:8443` operational archives; ignore superseded WS handoff as live truth |
| Secret exposure | Keep archives under local infrastructure + root remote paths only |

---

## 8. Labels

```text
BACKUP VERIFIED  ≠  FULL DISASTER RESTORE TESTED
RESTORE STRATEGY: CONFIRMED (procedure written)
BARE-METAL RESTORE: NOT YET EXERCISED
```

---

## 9. Related

- [SERVER-INVENTORY-v1.md](../SERVER-INVENTORY-v1.md)  
- [assets/MCA-VPN-001/BACKUP-STATE-v1.md](../assets/MCA-VPN-001/BACKUP-STATE-v1.md)  
- [assets/MCA-VPN-001/SECURITY-POSTURE-v1.md](../assets/MCA-VPN-001/SECURITY-POSTURE-v1.md)  
- [reports/MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md](../reports/MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md)  
- [reports/MARS-SERVER-OPS-DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01.md](../reports/MARS-SERVER-OPS-DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01.md)  
- Scoped pre-cred snapshot + credential rotation: [reports/MARS-SERVER-OPS-VEESP-3XUI-ADMIN-ACCESS-HARDENING-01.md](../reports/MARS-SERVER-OPS-VEESP-3XUI-ADMIN-ACCESS-HARDENING-01.md)

---

*VEESP operational restore v1 · final full operational backup preferred baseline · 2026-08-30 · no secrets.*

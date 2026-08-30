# REPORT — VEESP SYSTEM SECURITY HARDENING 01

**inventory_ref:** MCA-VPN-001  
**Provider:** VEESP  
**IPv4 / domain:** `178.173.250.69` / `wsp-cloud.com`  
**Wave date (UTC):** 2026-08-30  
**Overall:** **PASS** (server-side)  
**Real-workload post-hardening:** **PENDING OPERATOR**  
**Commit/push:** **0** (not authorized)

---

## 1. Executive verdict

Host security on VEESP was hardened in the required order: independent FriendHosting admin path proven → fresh pre-hardening backup → key-based SSH paths proven in separate sessions → password SSH disabled → exact UFW enabled → fail2ban / swap / journald tuned → post-hardening backup SHA-matched. VPN architecture (`VLESS` + TLS + RAW `:8443`), Xray **26.7.28**, 3X-UI **3.7.0**, and client count (**9**) were not mutated. Panel ports `:5928`/`:2096` remain intentionally public temporary residuals for a separate exposure wave.

Operator must still smoke the existing VEESP client profile (egress `178.173.250.69`) for ChatGPT / YouTube / Cursor / browsing before claiming real-workload PASS.

---

## 2. Independent FriendHosting administration path

| Check | Result |
|-------|--------|
| Workstation public egress | **92.42.99.126** |
| Classification | **FRIENDHOSTING** |
| VEESP used as admin egress | **NO** |
| FriendHosting mutation | **0** |
| Automatic local VPN switch | **0** |

Administration gate: **PASS**.

---

## 3. Pre-hardening baseline

| Item | Value |
|------|-------|
| OS / kernel | Ubuntu 22.04.5 LTS |
| RAM | ~1 GiB; **no swap** |
| Disk | ~20G; ~46% used |
| SSH | `:22`; `PermitRootLogin yes`; `PasswordAuthentication yes`; no `marsops`; no authorized_keys |
| UFW | **inactive**; INPUT ACCEPT |
| fail2ban | active (`sshd`, `3x-ipl`) |
| Listeners | 22, 5928, 2096, 8443, 46489, Docker MTProto 8445 |
| 3X-UI / Xray | **3.7.0** / **26.7.28** |
| Clients / inbounds | **9** / **2** |
| journald | ~1.9G uncapped |
| Reboot-required | **YES** (not rebooted) |
| Health gate | SSH / 3X-UI / Xray / TLS `:8443` / panel TLS **PASS** |

---

## 4. Backup/rollback gate

### Pre-hardening

| Field | Value |
|-------|-------|
| Remote | `/root/mars-backups/veesp-pre-system-hardening-20260830T162532Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-pre-system-hardening-20260830T162532Z.tgz` |
| Size | **81015066** |
| SHA-256 | `ec201264ef9ef0062ec19fa67c3c7bb56c6522b803c6ed1842c77e6ef497b7a7` |
| SHA match | **YES** |
| BACKUP | **PASS** |
| ROLLBACK STRATEGY | **CONFIRMED** before SSH/firewall mutation |

---

## 5. SSH access model

| Role | Model |
|------|-------|
| Operational | **`marsops`** — key login + sudo (password-confirmed; not NOPASSWD) |
| Root | key recovery retained (`PermitRootLogin without-password`) |
| Port | **22** preserved |
| Passwords remote | prohibited after hardening |

---

## 6. Key provisioning

| Item | Value |
|------|-------|
| Ops key | local `...\MCA-VPN-001\ssh\marsops_ed25519` (fingerprint recorded in local evidence; private key never printed) |
| Root recovery key | local `...\MCA-VPN-001\ssh\root_recovery_ed25519` |
| Secret contour | `X:\AI MARS\local\infrastructure\MCA-VPN-001\` only |
| Git exposure | **0** |

---

## 7. Key-login gate

| Check | Result |
|-------|--------|
| Separate ops key session | **PASS** |
| sudo from ops | **PASS** |
| Separate root key session | **PASS** |
| Original recovery session kept open during change | **YES** |

---

## 8. SSH hardening

| Setting | Effective |
|---------|-----------|
| PasswordAuthentication | **no** |
| KbdInteractiveAuthentication | **no** |
| PubkeyAuthentication | **yes** |
| PermitRootLogin | **without-password** |
| Drop-in | `/etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf` |
| `sshd -t` | **PASS** before reload |

---

## 9. Password/root validation

| Check | Result |
|-------|--------|
| Fresh ops key | **PASS** |
| Fresh root key | **PASS** |
| Password auth | **REJECTED** |
| Root password remote | **PROHIBITED** |

---

## 10. Firewall design

Required public allows from **live** evidence:

- **22/tcp** SSH  
- **8443/tcp** VLESS TLS RAW  
- **46489/tcp** Reality (live-required)  
- **5928/tcp** panel TEMPORARY  
- **2096/tcp** subscription residual TEMPORARY  
- **8445/tcp** MTProto docker-proxy  

No invented `:80`/`:443` (nginx ABSENT).

---

## 11. Docker/iptables interaction

| Item | Result |
|------|--------|
| Docker present | YES |
| Published public via docker-proxy | **8445** (MTProto) explicitly allowed |
| UFW = all Docker protected | **NOT CLAIMED** |
| Classification | **RESIDUAL** |

---

## 12. Firewall activation

| Step | Result |
|------|--------|
| Rules present before enable | YES (SSH allow included) |
| Enable | `ufw --force enable` |
| Immediate SSH after enable | **PASS** |
| Immediate `:8443` | **PASS** |
| Rollback command | `ufw --force disable` |
| Final UFW | **ACTIVE** |

---

## 13. External reachability

| Target | Classification |
|--------|----------------|
| 22 | INTENDED PUBLIC — PASS |
| 8443 | INTENDED PUBLIC — PASS (TLS+TCP) |
| 46489 | INTENDED PUBLIC — PASS |
| 5928 | INTENDED PUBLIC TEMPORARY — PASS |
| 2096 | INTENDED PUBLIC TEMPORARY — PASS |
| 8445 | INTENDED PUBLIC (MTProto) — PASS |

---

## 14. fail2ban

| Item | Result |
|------|--------|
| Service | **active** |
| sshd jail | **active** (port 22) |
| Verdict | **PASS** |

---

## 15. swap/OOM

| Item | Result |
|------|--------|
| Before | no swap |
| After | `/swapfile` **1 GiB**, mode `600`, fstab persisted |
| Reboot for activation | **not required** (swapon applied live) |
| Verdict | **PASS** |

---

## 16. logging

| Item | Result |
|------|--------|
| Before | ~1.9G uncapped journal |
| After | `SystemMaxUse=300M`, `RuntimeMaxUse=100M`; usage ~304M |
| Verdict | **PASS** |

---

## 17. security update posture

| Item | Result |
|------|--------|
| Pending upgrades | recorded (~16 packages class) — **not** broadly installed |
| Dist-upgrade | **0** |
| Reboot required | **YES** |
| Reboot performed | **0** |

---

## 18. VPN regressions

| Check | After SSH | After UFW | Final |
|-------|-----------|-----------|-------|
| Xray | PASS | PASS | **PASS** |
| TLS `:8443` | PASS | PASS | **PASS** |
| TCP `:8443` | PASS | PASS | **PASS** |
| Client count | 9 | 9 | **9 UNCHANGED** |
| UUID mutation | 0 | 0 | **0** |
| Architecture mutation | 0 | 0 | **0** |

---

## 19. Panel residuals

| Port | State |
|------|-------|
| 5928 | **PUBLIC TEMPORARY** |
| 2096 | **PUBLIC TEMPORARY** |
| nginx | **ABSENT** |

Panel exposure redesign remains the **next** charter.

---

## 20. Operator real-workload gate

Do **not** auto-switch local VPN.

Ask operator to use the **existing VEESP** profile.

Expected egress: **178.173.250.69**

Required smoke: ChatGPT / YouTube playback / Cursor multiple requests / normal browsing.

**REAL-WORKLOAD POST-HARDENING = PENDING OPERATOR**

---

## 21. Post-hardening backup

| Field | Value |
|-------|-------|
| Remote | `/root/mars-backups/veesp-post-system-hardening-20260830T163612Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-post-system-hardening-20260830T163612Z.tgz` |
| Size | **81048677** |
| SHA-256 | `1857afff8dbc087540b252394438115a9babb1b42c212c03137c4d41e7d920d7` |
| SHA match | **YES** |
| Readability | SSH/UFW/x-ui trees present |
| BACKUP | **PASS** |

---

## 22. Restore-state update

Updated:

- [BACKUP-STATE-v1.md](../assets/MCA-VPN-001/BACKUP-STATE-v1.md)  
- [VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md](../runbooks/VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md)  
- [SECURITY-POSTURE-v1.md](../assets/MCA-VPN-001/SECURITY-POSTURE-v1.md)  

**RESTORE STRATEGY = CONFIRMED** · bare-metal **NOT EXERCISED**.

---

## 23. Remaining risks

1. Panel `:5928`/`:2096` still public.  
2. Docker/UFW interaction residual (MTProto and potential future publishes).  
3. Reboot-required + pending apt packages not applied.  
4. Real-workload operator smoke pending.  
5. 1 GiB RAM still tight even with swap.  
6. Reality `:46489` and MTProto `:8445` remain public by live need.

---

## 24. Next VEESP wave

**VEESP PANEL EXPOSURE HARDENING 01** (not executed):

- assess nginx `:443` reverse proxy;  
- bind 3X-UI localhost;  
- close/restrict public `:5928`;  
- prove whether `:2096` can be closed;  
- preserve VPN `:8443`;  
- operator regression + fresh backup.

---

## 25. Evidence paths

| Path | Role |
|------|------|
| `X:\AI MARS\local\infrastructure\MCA-VPN-001\system-security-harden-01\` | scripts + evidence (cursorignored) |
| `X:\AI MARS\local\infrastructure\MCA-VPN-001\ssh\` | private keys (local only) |
| `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-*-system-hardening-*.tgz` | pre/post twins |
| `projects/mars-server-ops/assets/MCA-VPN-001/SECURITY-POSTURE-v1.md` | sanitized posture |

---

## 26. Git/mutation closeout

| Item | Value |
|------|-------|
| FriendHosting mutation | **0** |
| VEESP VPN architecture mutation | **0** |
| VEESP client mutation | **0** |
| VEESP UUID rotation | **0** |
| VEESP reboot | **0** |
| Secret disclosure | **0** |
| Foreign WIP mutation | **0** |
| commit/push | **0** |

---

*REPORT · VEESP SYSTEM SECURITY HARDENING 01 · 2026-08-30 · no secrets.*

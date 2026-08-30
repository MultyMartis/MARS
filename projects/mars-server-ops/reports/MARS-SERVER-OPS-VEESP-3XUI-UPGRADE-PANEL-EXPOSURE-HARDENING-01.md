# REPORT — VEESP 3X-UI UPGRADE + PANEL EXPOSURE HARDENING 01

**inventory_ref:** MCA-VPN-001  
**Provider:** VEESP  
**IPv4 / domain:** `178.173.250.69` / `wsp-cloud.com`  
**Wave date (UTC):** 2026-08-30  
**Overall:** **PASS WITH RESIDUALS**  
**3X-UI upgrade:** **PASS**  
**Panel exposure hardening:** **DEFERRED**  
**Commit/push:** **0** (not authorized)

---

## 1. Executive verdict

Official 3X-UI upgrade from **3.4.1 → 3.7.0** completed via the project’s supported `update.sh` with pinned tag `XUI_UPDATE_TAG=v3.7.0`, from an independent FriendHosting control path (`92.42.99.126`). Pre-upgrade and post-upgrade dual backups SHA-match. Admin credentials preserved (active login PASS). Inbound/client counts unchanged (**2** inbounds / **9** clients). VLESS TLS RAW `:8443` TCP/TLS PASS server-side. Managed Xray core moved **26.6.22 → 26.7.28** as an expected component of the official updater (not a separate optional click). Panel exposure (`*:5928`, `*:2096`) intentionally **DEFERRED** — nginx still ABSENT; binding localhost without a proven proxy would lock out panel access; combining network rebuild with a fresh app+DB migration was judged disproportionate risk.

Real-workload VEESP smoke (ChatGPT / YouTube / Cursor on existing profile): **PENDING OPERATOR**.

---

## 2. Independent FriendHosting administration path

| Check | Result |
|-------|--------|
| Workstation public egress | **92.42.99.126** |
| Classification | **FRIENDHOSTING-DE** independent control |
| VEESP used as admin egress | **NO** |
| FriendHosting mutation | **0** |
| Automatic v2rayN profile switch | **0** |

Administration gate: **PASS**.

---

## 3. Pre-upgrade VEESP truth

| Item | Value |
|------|-------|
| Hostname | `wsp-cloud` |
| OS | Ubuntu 22.04.5 LTS |
| 3X-UI | **3.4.1** active (`/usr/local/x-ui/x-ui -v`) |
| Xray | **26.6.22** |
| Panel | PUBLIC TLS-DIRECT `*:5928`; webBasePath **NON_DEFAULT** (len 18 after strip); TLS PASS |
| VPN | VLESS TLS RAW `*:8443` (8 clients) + Reality `:46489` (1 client) |
| `:2096` | PUBLIC, owned by `x-ui` |
| nginx | ABSENT |
| UFW | inactive |
| fail2ban | active |
| SSH | `:22`; `PermitRootLogin yes`; `PasswordAuthentication yes` |

Evidence (local contour): `X:\AI MARS\local\infrastructure\MCA-VPN-001\xui-upgrade-panel-harden-01\baseline-*`, `version-resolution.json`.

---

## 4. Installed vs target 3X-UI version

| | |
|--|--|
| Installed before | **3.4.1** |
| Target stable | **v3.7.0** (GitHub latest stable at wave time) |
| Installed after | **3.7.0** |

---

## 5. Official upgrade source/method

| Field | Value |
|-------|-------|
| Source | **OFFICIAL** MHSanaei/3x-ui |
| Mechanism | Same path as `x-ui` menu `update()` → `update.sh` |
| Execution | `curl -fsSL https://raw.githubusercontent.com/MHSanaei/3x-ui/main/update.sh` then `XUI_UPDATE_TAG=v3.7.0 bash …` |
| Pin | Explicit **v3.7.0** (not floating “latest” mid-run) |
| First attempt | Local Windows upload of `update.sh` failed on **CRLF** — aborted; panel remained 3.4.1 healthy |
| Successful attempt | On-server curl (LF) + pinned tag |

---

## 6. Pre-upgrade backup

| Field | Value |
|-------|-------|
| Remote | `/root/mars-backups/veesp-xui-preupgrade-20260830T154548Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-xui-preupgrade-20260830T154548Z.tgz` |
| Size | **83815970** |
| SHA-256 | `ae78f5ef548bdbcea0677c259d949698ae66941a5ebe8b95f3b6e9e11b5aac5b` |
| SHA match | **YES** |
| Scope | `/etc/x-ui`, `/usr/local/x-ui`, unit, `/usr/bin/x-ui`, `/root/cert`, meta |

---

## 7. Rollback strategy

**ROLLBACK STRATEGY = CONFIRMED** before mutation.

1. `systemctl stop x-ui`  
2. Extract **same** pre-upgrade archive  
3. Restore matching `/usr/local/x-ui` + `/etc/x-ui` (+ unit if needed)  
4. `systemctl daemon-reload && systemctl start x-ui`  
5. Validate `:5928` TLS + `:8443` TLS/VLESS  

Do **not** mix old binary with post-migration DB (or the reverse).

---

## 8. Upgrade execution

- Dependencies refresh via official `install_base` (curl/tar/openssl class packages only — **not** Ubuntu release upgrade).  
- Stopped x-ui; replaced application tree; **removed/replaced managed Xray binary** (script message: “Removing old xray version…”).  
- Reinstalled systemd unit; started x-ui.  
- Official post-update: “Start migrating database… Migration done!”  
- Panel settings shown secure with SSL; `hasDefaultCredential: false`; port **5928**; path NON_DEFAULT retained.  
- fail2ban IP-limit setup ran (already installed; 3x-ipl jail present afterward).  
- EXIT_CODE=0.

Sanitized log: local `xui-upgrade-panel-harden-01/upgrade-log-sanitized-20260830T155700Z.txt` (secret path redacted).

---

## 9. DB / config migration

| Change | Observation |
|--------|-------------|
| DB migration | **YES** (official migrator) |
| sqlite tables | 20 → **22** (`client_hwids`, `sub_balancers` added) |
| Panel port / TLS / path | Preserved |
| webListen | Still empty / ABSENT → bind `*` |
| subPort / subEnable | ABSENT in settings (unchanged pattern) |
| Service unit | Reinstalled by updater |
| Settings format | Migrated; admin users table retained (USER_COUNT=1) |

---

## 10. Xray version outcome

| | |
|--|--|
| Before | **26.6.22** |
| After | **26.7.28** |
| Classification | **EXPECTED** — unavoidable managed component of official 3X-UI `update.sh` release tarball |
| Separate optional core update clicked | **NO** |

---

## 11. Immediate post-upgrade regression

| Check | Result |
|-------|--------|
| x-ui service | **PASS** (active) |
| Version | **3.7.0** |
| Panel TLS `:5928` | **PASS** |
| Panel login page | **PASS** |
| Active rotated admin login | **PASS** |
| Inbound count | **2** UNCHANGED |
| Client total | **9** UNCHANGED |
| TCP `:8443` | **PASS** |
| TLS `:8443` | **PASS** (CN=wsp-cloud.com) |
| SSH | **PASS** (session remained) |

PHASE A SERVER-SIDE = **PASS**.

---

## 12. Admin credential preservation

| Item | Result |
|------|--------|
| Credentials preserved through upgrade | **YES** |
| New/current admin login | **PASS** |
| Old admin login | Not re-tested with a stored old payload this wave (`SKIP_NO_FILE`); prior wave established **REVOKED**; default credential still `hasDefaultCredential: false` |
| Secret storage | LOCAL SECRET ONLY under `MCA-VPN-001\secrets.local.md` |

---

## 13. Panel `:5928` exposure

| Item | After upgrade |
|------|----------------|
| Listener | `*:5928` PUBLIC |
| Architecture | PUBLIC TLS-DIRECT 3X-UI |
| Protections present | TLS; NON_DEFAULT path; rotated strong credentials; default cred disabled |
| Residual | Broader than ideal public bind |

---

## 14. Subscription `:2096` analysis

| Item | Result |
|------|--------|
| Owning process | `x-ui` |
| subPort / subEnable in DB | ABSENT |
| subCertFile / subKeyFile | PATH_SET (cert refs present) |
| Classification | **UNUSED UNPROVEN** |
| Action | **DEFER** close/restrict (not UNUSED PROVEN) |

---

## 15. Firewall reality

| Layer | Reality |
|-------|---------|
| UFW | **inactive** |
| iptables | Present; INPUT default **ACCEPT**; fail2ban `f2b-sshd`; Docker chains (incl. DNAT-class rules toward container `:443`) |
| nftables | ruleset lines observed (~110) |
| Provider firewall | SAFE UNKNOWN / not claimed |
| Claim | **No host firewall protection for panel/VPN ports** — SECURITY RESIDUAL |

UFW was **not** activated in this wave.

---

## 16. SSH residual

| Item | Value |
|------|-------|
| Port | 22 |
| PermitRootLogin | yes |
| PasswordAuthentication | yes |
| PubkeyAuthentication | yes |
| fail2ban sshd | active |
| Mutation this wave | **0** |

Recorded for later **SYSTEM SECURITY HARDENING**.

---

## 17. Panel hardening decision

**DEFER** (option C).

Rationale: fresh app upgrade + DB schema migration already landed; introducing nginx/localhost bind in the same wave is a network rebuild; localhost-only without proxy locks out operator; TLS+path+credentials already reduce risk; `:2096` not proven unused.

---

## 18. nginx decision

| Item | Value |
|------|-------|
| nginx | **ABSENT** |
| Host `ss` `:443` | FREE |
| Docker iptables hint | Container path may involve `:443` — another reason not to casually claim host `:443` for panel |
| Migration executed | **NO** |

---

## 19. Final server regression

| Check | Result |
|-------|--------|
| Xray | PASS |
| VLESS TLS RAW `:8443` | PASS |
| Clients | **UNCHANGED** (9) |
| Client mutation | **0** |
| UUID rotation | **0** |
| `:8443` architecture mutation | **0** |
| Reboot | **0** |

---

## 20. Real-workload operator gate

**PENDING OPERATOR.**

Do **not** create a new profile. Switch to the **existing** VEESP VPN profile and confirm egress **178.173.250.69**, then:

1. ChatGPT  
2. YouTube playback  
3. Cursor — multiple meaningful requests  
4. Normal browsing  

Report confirmation to close REAL-WORKLOAD POST-UPGRADE = PASS.

---

## 21. Post-upgrade backup

| Field | Value |
|-------|-------|
| Remote | `/root/mars-backups/veesp-xui-postupgrade-20260830T155842Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-xui-postupgrade-20260830T155842Z.tgz` |
| Size | **80876064** |
| SHA-256 | `97ee0394a308f827b9798d748c86f740ec8b2501a0c60712c7927913db5389d0` |
| SHA match | **YES** |

---

## 22. Restore-runbook update

Updated: [runbooks/VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md](../runbooks/VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md) and [assets/MCA-VPN-001/BACKUP-STATE-v1.md](../assets/MCA-VPN-001/BACKUP-STATE-v1.md).

Explicit caveats:

- Prefer **post-upgrade** archive for current 3.7.0/DB pair.  
- Pre-upgrade archive restores **3.4.1** + matching DB.  
- Older operational/precred stamps may restore **pre-rotation** credentials and older Xray.

---

## 23. Residual risks

1. Public `:5928` / `:2096` with no host firewall.  
2. SSH password + root login enabled.  
3. Docker/iptables surface present (MTProto-era residue).  
4. Operator real-workload post-upgrade not yet confirmed.  
5. Brief upgrade-log exposure of panel path on remote log — scrubbed in evidence copies; path remains LOCAL SECRET for operational use.

---

## 24. Next recommended VEESP wave

1. **VEESP SYSTEM SECURITY HARDENING 01** — firewall policy; SSH password/root posture; fail2ban/logging review; swap/OOM if needed.  
2. Panel exposure completion (nginx/localhost) **only if** still justified after firewall work.  
3. Fresh FULL VEESP operational backup after hardening.  
4. FriendHosting + VEESP soak / lightweight monitoring.

Do **not** start these in this wave.

---

## 25. Evidence paths

| Kind | Path |
|------|------|
| Wave workdir | `X:\AI MARS\local\infrastructure\MCA-VPN-001\xui-upgrade-panel-harden-01\` |
| Pre-upgrade backup validation | `…\preupgrade-backup-validation-20260830T154548Z.json` |
| Upgrade verdict | `…\upgrade-verdict-20260830T155700Z.json` |
| Phase B decision | `…\phaseb-decision-20260830T155842Z.json` |
| Post-upgrade backup validation | `…\postupgrade-backup-validation-20260830T155842Z.json` |
| Canonical docs | `SERVER-INVENTORY-v1.md`, programme `OPERATIONAL-INDEX.md`, passport, backup-state, restore runbook |

---

## 26. Git / mutation closeout

| Item | Value |
|------|-------|
| FriendHosting mutation | **0** |
| VEESP client mutation | **0** |
| VEESP `:8443` architecture mutation | **0** |
| VEESP UUID rotation | **0** |
| VEESP reboot | **0** |
| Secret disclosure in Git/report | **0** (path redacted; credentials not printed) |
| Foreign WIP mutation | **0** |
| commit / push | **0** |

---

*MARS Server Ops · VEESP MCA-VPN-001 · 3X-UI upgrade PASS · panel exposure DEFERRED · 2026-08-30 · no secrets.*

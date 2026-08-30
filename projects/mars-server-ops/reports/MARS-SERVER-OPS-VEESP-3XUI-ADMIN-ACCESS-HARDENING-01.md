# MARS SERVER OPS — VEESP 3X-UI ADMIN ACCESS HARDENING 01

**Wave:** VEESP-3XUI-ADMIN-ACCESS-HARDENING-01  
**inventory_ref:** MCA-VPN-001  
**Provider:** VEESP  
**IPv4 / domain:** `178.173.250.69` / `wsp-cloud.com`  
**Verdict:** **PASS** (server-side) — real-workload post-hardening **PENDING OPERATOR**  
**Date (UTC):** 2026-08-30  

---

## 1. Executive verdict

Operator-selected 3X-UI admin username and password were rotated on VEESP / MCA-VPN-001 via the supported `x-ui setting` CLI. New credentials authenticate; old credentials do not. VPN positive control **VLESS + TLS + RAW/TCP `:8443`** remains healthy. Client identities **unchanged**. Public panel ports `:5928` and `:2096` were **not** architecturally redesigned (nginx still **ABSENT**); they are documented residuals for a separate charter.

| Gate | Result |
|------|--------|
| Preflight (X: / `AI WS` / branch) | PASS |
| Intended credential gate | READY_FOR_ROTATION then CONSUMED_ROTATED |
| Rollback backup SHA | PASS |
| Scoped `/etc/x-ui` snapshot | PASS (remote+local SHA match) |
| Username rotated | YES |
| Password rotated | YES |
| New login | PASS |
| Old login | REVOKED |
| x-ui / panel TLS | PASS |
| VLESS RAW/TLS `:8443` | PASS |
| Client mutation | **0** |
| nginx migration | **not executed** (not required for PASS) |
| FriendHosting mutation | **0** |
| commit/push | **0** |

---

## 1a. Resume authorization

Continuation authorized by operator: **CONTINUE VEESP 3X-UI ADMIN ACCESS HARDENING 01**. Same wave as the prior STOP (no competing report).

---

## 2. Operator request

1. **Mandatory:** change 3X-UI admin login and password to operator-selected credentials.  
2. **Secondary:** establish panel exposure; assess bind / path / nginx / firewall; harden only if safe; preserve VLESS TLS RAW `:8443`; update local secrets + safe docs; regress.

---

## 2a. Intended credential gate

| Check | Result |
|-------|--------|
| File | `X:\AI MARS\local\infrastructure\MCA-VPN-001\admin-credentials-intended.local.md` |
| Status at resume | **READY_FOR_ROTATION** |
| `panel_login_new` | present / non-empty |
| `panel_password_new` | present / non-empty |
| Values printed to Git/chat | **0** |
| After rotation | **CONSUMED_ROTATED** — staging values moved to `secrets.local.md` |

---

## 3. Pre-change backup state

| Field | Value |
|-------|-------|
| Local | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-operational-20260830T132309Z.tgz` |
| Remote | `/root/mars-backups/veesp-operational-20260830T132309Z.tgz` |
| Size | **83967532** |
| SHA-256 | `d10b67cb1b8a9e0beb4a131a583eee1af56cb153e4513d1e599f6e8bba9112c8` |
| Local verify (resume) | **PASS** |
| Restore strategy | **CONFIRMED** — [VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md](../runbooks/VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md) |
| Bare-metal restore | **NOT EXERCISED** |

---

## 3a. Scoped rollback snapshot

Taken immediately before credential mutation (`20260830T141517Z`):

| Field | Value |
|-------|-------|
| Remote | `/root/mars-backups/veesp-xui-precred-20260830T141517Z.tgz` |
| Local twin | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-xui-precred-20260830T141517Z.tgz` |
| Scope | `/etc/x-ui/` (includes `x-ui.db`) |
| Size | **516851** |
| SHA-256 | `ce6134f4b7eed075571323a2d7cbfede0bc192967b81464929ab11c27463c3b3` |
| Remote/local match | **YES** |

Use this snapshot to roll back **panel DB/credentials only** without restoring the full operational archive.

---

## 4. Live VEESP baseline (pre-mutation recheck)

| Field | Live value |
|-------|------------|
| Hostname | `wsp-cloud` |
| OS | Ubuntu 22.04.5 LTS |
| Kernel | `5.15.0-187-generic` |
| SSH | `:22` PASS |
| 3X-UI / `x-ui` | **active** |
| Xray | **26.6.22** |
| VPN architecture | **VLESS + TLS + RAW/TCP `:8443`** (`MCA-Gate-TLS`, **8** clients) |
| Reality inbound | `:46489`, 1 client — **untouched** |
| Panel TLS `:5928` | PASS |
| VPN TLS `:8443` | PASS |
| nginx | **ABSENT** |
| UFW | **inactive** |
| fail2ban | **active** (`sshd`, `3x-ipl`) |

---

## 4a. Credential rotation

| Item | Result |
|------|--------|
| Mechanism | `/usr/local/x-ui/x-ui setting -username … -password …` |
| CLI result | **Username and password updated successfully** (`ROTATE_RC=0`) |
| Direct DB edit | **not used** |
| Service after | `systemctl restart x-ui` → **active**; listeners `:5928` / `:8443` / `:2096` present |
| DB username vs intended | **MATCH** |
| Password bcrypt vs pre-cred snapshot | **CHANGED** |
| VLESS UUID / inbound / TLS cert / web path | **unchanged** |

---

## 5. New login validation

| Method | Result |
|--------|--------|
| HTTPS POST `{webBasePath}login` JSON + CSRF (`X-CSRF-TOKEN`) + session cookie | **success: true** (HTTP 200) |
| Classification | **PASS** |

Credentials were not logged.

---

## 6. Old credential revocation

| Method | Result |
|--------|--------|
| Same login endpoint with previous local-secret admin pair | HTTP 200, **success: false** |
| DB username equals previous secret username | **false** |
| Classification | **REVOKED** |

---

## 7. Secret lifecycle

| Item | State |
|------|-------|
| Active record | `X:\AI MARS\local\infrastructure\MCA-VPN-001\secrets.local.md` |
| panel username/password | **ACTIVE** (rotated UTC `2026-08-30T14:15:17Z`) |
| Previous panel pair | **RETIRED** (not kept as live fields) |
| Staging file | **CONSUMED_ROTATED** |
| Git | local contour remains gitignored (`/local/`) |

---

## 8. Panel exposure final state

**Classification: C — panel public with TLS directly from 3X-UI** (unchanged architecture)

| Aspect | State |
|--------|-------|
| Panel port | **5928** |
| Bind | `*:5928` PUBLIC_ALL_INTERFACES |
| Panel TLS | PASS (`/root/cert/wsp-cloud.com/`) |
| nginx | ABSENT |
| Auth | required; `hasDefaultCredential: false`; **rotated this wave** |
| Web base path | NON_DEFAULT, UNCHANGED (not disclosed) |

Accepted for this wave as **PUBLIC TLS-DIRECT — ACCEPTED TEMPORARY RESIDUAL**. Architectural nginx/localhost migration is a **separate** charter.

---

## 9. `:5928` residual

| Item | Result |
|------|--------|
| Firewall restriction | **none** (UFW inactive; fail2ban `3x-ipl` present, 0 bans at check) |
| Classification | **PUBLIC ADMIN SURFACE** |
| Mutation this wave | **0** |
| Rationale | Credentials + non-default path + TLS are the mandated hardening; closing `:5928` without nginx/tunnel would lock out the operator |

---

## 10. `:2096` residual

| Item | Result |
|------|--------|
| Owner | `x-ui` process |
| Related settings | `subCertFile` / `subKeyFile` present (subscription TLS material) |
| Client inbound dependency | **not proven unused** — do not close |
| Classification | **PUBLIC — IDENTIFIED RESIDUAL / FOLLOW-UP REQUIRED** |
| Mutation this wave | **0** |

---

## 11. Panel web path decision

**UNCHANGED NON_DEFAULT.** Already not trivially guessable (length 20). No churn rotation.

---

## 12. VPN regression

| Check | Result |
|-------|--------|
| Xray version | 26.6.22 |
| `:8443` listen | PASS |
| TLS handshake `wsp-cloud.com:8443` | PASS |
| Inbounds after rotation | id=1 `:8443` VLESS `MCA-Gate-TLS` **8** clients; id=3 `:46489` Reality **1** client |
| vs pre-rotation | **identical** |
| Client mutation | **0** |
| Transport mutation | **0** |

---

## 13. Panel regression

| Check | Result |
|-------|--------|
| x-ui active | PASS |
| HTTPS panel GET (secret path) | HTTP 200 |
| Panel TLS `:5928` | PASS |
| New login | PASS |
| Secret path | UNCHANGED |
| Unexpected new public listener | **none observed** (same set: 22 / 5928 / 2096 / 8443 / 46489 / 8445) |

---

## 14. Real-workload operator gate

Workstation VPN profile **not** changed (no UUID/inbound mutation).

Operator should confirm existing VEESP profile:

| Check | Required |
|-------|----------|
| Egress | `178.173.250.69` |
| ChatGPT | PASS |
| YouTube playback | PASS |
| Cursor | PASS |

**Classification:** SERVER-SIDE HARDENING **PASS** · REAL-WORKLOAD POST-HARDENING = **PENDING OPERATOR**

---

## 15. Residual risks

1. Panel `:5928` publicly reachable (TLS-direct, no nginx/source restriction).  
2. Subscription-related `:2096` publicly reachable; purpose retained pending dedicated assessment.  
3. SSH password auth + `PermitRootLogin yes` (out of scope).  
4. UFW inactive.  
5. Operator real-workload smoke not yet recorded this wave.

---

## 16. Recommended next hardening

**Separate charter: VEESP PANEL EXPOSURE HARDENING 01**

Likely scope:

- nginx `:443` → secret path → localhost x-ui (FriendHosting-like), **or** SSH-tunnel-only panel;  
- restrict/remove public `:5928`;  
- assess/restrict `:2096`;  
- preserve `:8443`;  
- backup before mutation;  
- real-workload regression.

Do **not** mix that rebuild into credential rotation.

Optional later: SSH key-only; UFW allowlist.

---

## 17. Git / mutation closeout

| Item | Value |
|------|-------|
| VEESP VPN architecture mutation | **0** |
| VEESP client mutation | **0** |
| FriendHosting mutation | **0** |
| Firewall mutation | **0** |
| Panel bind/path mutation | **0** |
| Reboot | **0** |
| Secret disclosure in Git docs | **0** |
| Foreign WIP mutation | **0** |
| commit | **0** |
| push | **0** |

---

## Evidence paths

| Path | Role |
|------|------|
| `...\MCA-VPN-001\backups\veesp-operational-20260830T132309Z.tgz` | Full operational rollback |
| `...\MCA-VPN-001\backups\veesp-xui-precred-20260830T141517Z.tgz` | Pre-credential `/etc/x-ui` snapshot |
| `...\MCA-VPN-001\admin-hardening-01-preaudit\` | Live preaudit |
| `...\MCA-VPN-001\admin-hardening-01-rotate\` | Rotation evidence (sanitized) |
| `...\MCA-VPN-001\secrets.local.md` | ACTIVE local secrets |

---

*PASS (server-side) — credential rotation complete — 2026-08-30.*

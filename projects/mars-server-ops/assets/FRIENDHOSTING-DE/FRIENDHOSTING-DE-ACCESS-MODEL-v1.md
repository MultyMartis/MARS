# FRIENDHOSTING-DE — Access model v1

**inventory_ref:** FRIENDHOSTING-DE  
**Status:** **CANONICAL** capability model (no credentials)  
**Secrets:** local contour only  

---

## 1. SSH

| Capability | State |
|------------|-------|
| Operational user | `marsops` — key-based |
| Sudo | Available to `marsops` for chartered work |
| Port | `3333/tcp` |
| PasswordAuthentication | **disabled** |
| Root password remote login | **prohibited** |
| Root key recovery | **retained** (break-glass) |
| Direct root day-to-day ops | Prefer `marsops` + sudo |

Any SSH port/user/auth change requires an explicit charter and pre-change access proof.

---

## 2. 3X-UI panel

| Capability | State |
|------------|-------|
| Public entry | `https://metacode-cloud.com:443` via nginx |
| Auth | Panel username/password (local secrets) |
| Web path | **secret** — stored only under local secret contour |
| Panel process bind | `127.0.0.1:20901` |
| `:2096` external | **UFW DENY** — do not open for convenience |
| Preferred client UX | Native QR / copy-link in panel |

Operator runbook: [../../runbooks/FRIENDHOSTING-3XUI-OPERATOR-RUNBOOK-v1.md](../../runbooks/FRIENDHOSTING-3XUI-OPERATOR-RUNBOOK-v1.md)

---

## 3. VPN client management

| Rule | Detail |
|------|--------|
| Preferred interface | **3X-UI** (create / disable / QR / copy-link) |
| Local client files | Backup / recovery / registry only — **not** primary UX |
| Secret artifacts | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\` |
| Git | Labels and procedures only — never UUIDs/URIs |

---

## 4. Provider console

Out-of-band recovery: FriendHosting control panel (operator account) — used for reboot, disk, console when SSH unavailable. Credentials not in Git.

---

## 5. Related

- Security posture: [FRIENDHOSTING-DE-SECURITY-POSTURE-v1.md](FRIENDHOSTING-DE-SECURITY-POSTURE-v1.md)  
- Programme access template: [../../ACCESS-MODEL-v1.md](../../ACCESS-MODEL-v1.md)

---

*Access model v1 · 2026-08-30.*

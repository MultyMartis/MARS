# EQVPS-MICRO-IP — Controlled SSH Bootstrap

**Working reference:** `EQVPS-MICRO-IP`  
**Date:** 2026-08-27  
**Programme:** MARS Server Ops & VPS Forge  
**Wave:** Controlled SSH bootstrap + authentication hardening (post-intake)  
**Verdict:** **PASS_WITH_RESIDUALS**  
**Pattern basis:** Server B Phase 3C (`SERVER-B-SECURE-SSH-BOOTSTRAP-v1.md`) — first-match OpenSSH drop-in semantics

**Not in this wave:** firewall, fail2ban, reboot, package update/upgrade, DNS/PTR, application stack, SSH port change.

---

## 1. Purpose

Replace temporary public `root` + password SSH bootstrap with controlled MARS operator access:

```text
MARS workstation → dedicated Ed25519 private key → marsops (password sudo) → EQVPS-MICRO-IP
```

Only after independent key-session + sudo validation: disable direct root SSH and SSH password authentication.

---

## 2. Preflight (session)

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| Prior intake | [EQVPS-MICRO-IP-read-only-intake-2026-08-27.md](./EQVPS-MICRO-IP-read-only-intake-2026-08-27.md) — **READY_WITH_RESIDUALS** |
| Foreign WIP | **PRESERVED** (untouched) |
| Commit / push | **NONE** |

---

## 3. Operator account (sanitized)

| Field | Value |
|-------|-------|
| Username | `marsops` |
| UID / GID | `1000` / `1000` |
| Home | `/home/marsops` |
| Shell | `/bin/bash` |
| Groups | `marsops`, `sudo` |
| Remote auth | Ed25519 public key only (post-hardening) |
| Sudo model | password-confirmed (`NOPASSWD` **not** used) |
| Sudo password | **LOCAL ONLY** — `local/infrastructure/EQVPS-MICRO-IP/secrets.local.md` |

Post-change verification: `id marsops` → `groups=1000(marsops),27(sudo)`; `getent group sudo` includes `marsops`.

---

## 4. SSH key (sanitized)

| Field | Value |
|-------|-------|
| Algorithm | Ed25519 |
| Comment | `marsops@eqvps-micro-ip` |
| Fingerprint | `SHA256:L2V62ewZtKftyAnxuDmDof8zjM4V4dlcyyqYCjyqfGk` |
| Local private key path | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\ssh\marsops_ed25519` |
| Local public key path | `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\ssh\marsops_ed25519.pub` |
| Private key in Git | **NONE** |
| Public key body in Git | **NOT COPIED** (fingerprint only) |
| AdminVPS Server B key reuse | **NONE** (dedicated EQVPS key pair) |

---

## 5. Authorized key layout (remote)

| Path | Owner | Mode |
|------|-------|------|
| `/home/marsops/.ssh` | `marsops:marsops` | `700` |
| `/home/marsops/.ssh/authorized_keys` | `marsops:marsops` | `600` |

---

## 6. Mutation sequence (executed)

| Step | Result |
|------|--------|
| A. Generate dedicated local Ed25519 key | **PASS** |
| B. Create `marsops` + `sudo` membership | **PASS** |
| C. Install `authorized_keys` | **PASS** |
| D. Independent key session (pre-harden) | **PASS** — `whoami=marsops`, `hostname=metacode-cloud` |
| E. Sudo validation (pre-harden) | **PASS** — `sudo whoami=root` (password required) |
| F. SSH config forensic (pre-change) | **PASS** — provider drop-in documented |
| G. Apply MARS hardening drop-in + disable provider drop-in | **PASS** |
| H. `sshd -t` | **PASS** |
| I. `systemctl reload ssh` (not reboot) | **PASS** — service **active** |
| J. Post-reload key + sudo (independent session) | **PASS** |
| K. Negative auth (root / password) | **PASS** — rejected (`BadAuthenticationType`) |

**Ordering note:** Provider file `/etc/ssh/sshd_config.d/00-eqvps-permitroot.conf` reinforced `PermitRootLogin yes` and `PasswordAuthentication yes`. Per Server B first-match lesson, provider drop-in was **renamed** (reversible) to `00-eqvps-permitroot.conf.mars-disabled` and MARS managed content placed at **`00-mars-server-ops-hardening.conf`** (lexically first among active drop-ins). Cloud image file `60-cloudimg-settings.conf` remains but is superseded by first-match `00-mars-server-ops-hardening.conf`.

---

## 7. SSH configuration change

| Item | Value |
|------|-------|
| Managed remote path | `/etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf` |
| Provider drop-in (disabled) | `/etc/ssh/sshd_config.d/00-eqvps-permitroot.conf.mars-disabled` |
| Cloud image drop-in | `/etc/ssh/sshd_config.d/60-cloudimg-settings.conf` — **left in place** (superseded by `00-mars-…`) |
| Main `/etc/ssh/sshd_config` | **not destructively rewritten** |
| Apply method | `sshd -t` then `systemctl reload ssh` |
| Port change | **NONE** (22) |

### Effective values — before hardening

| Directive | Effective |
|-----------|-----------|
| `PermitRootLogin` | `yes` |
| `PasswordAuthentication` | `yes` |
| `KbdInteractiveAuthentication` | `no` |
| `PubkeyAuthentication` | `yes` |
| `MaxAuthTries` | `6` |
| `X11Forwarding` | `yes` |
| `Port` | `22` |
| `UsePAM` | `yes` |

### Effective values — after hardening

| Directive | Effective |
|-----------|-----------|
| `PermitRootLogin` | `no` |
| `PasswordAuthentication` | `no` |
| `KbdInteractiveAuthentication` | `no` |
| `PubkeyAuthentication` | `yes` |
| `MaxAuthTries` | `3` |
| `X11Forwarding` | `no` |
| `Port` | `22` |
| `UsePAM` | `yes` |

Managed file contents (non-secret):

```text
# MARS Server Ops — controlled SSH hardening (EQVPS-MICRO-IP)
PermitRootLogin no
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
MaxAuthTries 3
X11Forwarding no
UsePAM yes
Port 22
```

---

## 8. Service / listener evidence (post-harden)

| Check | Result |
|-------|--------|
| `sshd -t` | **PASS** |
| `systemctl is-active ssh` | `active` |
| TCP/22 listeners | `0.0.0.0:22`, `[::]:22` — `sshd` |
| Existing admin session policy | Pre-harden validated session not required for recovery; post-harden independent key access **PASS** |

---

## 9. Positive validation (post-harden)

| Test | Result |
|------|--------|
| `marsops` key login (`whoami`) | **PASS** → `marsops` |
| `sudo -v` / `sudo whoami` | **PASS** → `root` (password required) |
| Effective `sshd -T` | Matches target hardening table |

---

## 10. Negative authentication tests

| Case | Attempts | Result |
|------|----------|--------|
| `root` + password (no pubkey) | 1 | **REJECTED** — `BadAuthenticationType: allowed types: ['publickey']` |
| `marsops` + password (no pubkey) | 1 | **REJECTED** — same |

No brute force. Credentials not recorded in Git artefacts.

---

## 11. Explicit non-mutations (verified)

| Area | State |
|------|-------|
| `apt update/upgrade/install/remove` | **NONE** |
| UFW | **inactive** (unchanged) |
| fail2ban | **absent** |
| Reboot / shutdown | **NONE** |
| DNS / PTR / hostname | **NONE** |
| Swap | **NONE** |
| Application stack (Xray, 3X-UI, nginx, Docker, etc.) | **NONE** |
| SSH port | **22** (unchanged) |

---

## 12. Residuals (expected; not fixed in this wave)

| Residual | Notes |
|----------|-------|
| `/var/run/reboot-required` | **present** — kernel/packages from prior provider state |
| UFW inactive | Next security wave |
| fail2ban absent | Next security wave |
| No swap | Out of scope |
| GPT disk-header warning (intake) | Not remediated |
| cloud-init deprecated-key warning (intake) | Not remediated |
| open-vm-tools on KVM (intake) | Not changed |
| Root SSH recovery | Provider console / reinstall path only — password SSH disabled |

---

## 13. Root recovery state

| Item | State |
|------|-------|
| Root SSH (password or key) | **disabled** (`PermitRootLogin no`, pubkey-only server-wide) |
| Operator path | `marsops` + dedicated Ed25519 + sudo password |
| Provider console | Available as **fallback** (not tested in this wave) |

---

## 14. Local evidence (gitignored)

| Path | Role |
|------|------|
| `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\ssh-bootstrap-raw-2026-08-27\bootstrap-evidence.txt` | Phase A–G operational log |
| `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\ssh-bootstrap-raw-2026-08-27\post-harden-evidence.txt` | Post-harden remote capture |
| `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\ssh-bootstrap-raw-2026-08-27\eqvps_quick_validate.py` | Post-harden validation helper |
| `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\ssh-bootstrap-raw-2026-08-27\eqvps_ssh_bootstrap.py` | Bootstrap automation (local-only) |
| `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\secrets.local.md` | Root + marsops credentials (**local only**) |

---

## 15. Git artefacts (this wave)

| Path | Action |
|------|--------|
| `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-controlled-ssh-bootstrap-2026-08-27.md` | **created** |

**Commit:** **NONE** (by charter).

---

## 16. Recommended next phase

**Base OS security + firewall hardening** — mirror Server B Phase 3D (`SERVER-B-BASE-OS-SECURITY-v1.md`): enable UFW with minimal allow rules, install/configure fail2ban, optional unattended-upgrades policy review — **only after operator confirms this SSH bootstrap report**.

Do **not** reboot solely for kernel until a dedicated maintenance window unless required by a later wave.

---

## 17. Wave closeout

| Item | Value |
|------|-------|
| Verdict | **PASS_WITH_RESIDUALS** |
| Lockout risk observed | **NONE** (independent validation passed pre- and post-harden) |
| Secrets in Git | **NONE** |

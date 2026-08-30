# Server B Bootstrap Baseline v1

**Status:** **SUPERSEDED FOR SSH + HOST SECURITY POSTURE** — Phase 3C SSH + Phase 3D base OS security (2026-08-25)  
**Original wave:** Phase 3B (read-only pristine capture)  
**Locus:** `SERVER-B-PLANNING`  
**Purpose:** Preserve pristine post-provision baseline **and** record Phase 3C/3D security deltas

---

## 1. Phase 3B pristine SSH posture (historical)

| Item | State at Phase 3B | Class |
|------|-------------------|-------|
| Temporary method | `root` + password SSH | historical |
| Port | 22 | historical |
| PermitRootLogin | yes | historical |
| PasswordAuthentication | yes | historical |
| PubkeyAuthentication | yes | historical |
| MaxAuthTries | 6 | historical |
| Dedicated operator user | **ABSENT** | historical |
| Operator SSH key installed | **ABSENT** | historical |

This was **TEMPORARY BOOTSTRAP STATE**.

---

## 2. Phase 3C current SSH posture

| Item | State after Phase 3C | Class |
|------|----------------------|-------|
| Remote method | `marsops` + Ed25519 key | **PRESENT** |
| Port | 22 | **PRESENT** |
| PermitRootLogin | **no** | **HARDENED** |
| PasswordAuthentication | **no** | **HARDENED** |
| KbdInteractiveAuthentication | **no** | **HARDENED** |
| PubkeyAuthentication | **yes** | **PRESENT** |
| MaxAuthTries | **3** | **HARDENED** |
| Dedicated operator user | `marsops` (sudo) | **PRESENT** |
| Operator SSH key installed | **PRESENT** | **PRESENT** |
| Managed drop-in | `/etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf` | **PRESENT** |
| Root password (local secret) | **PRESERVED** (remote root SSH disabled) | **PRESENT** |

Authoritative narrative: [SERVER-B-SECURE-SSH-BOOTSTRAP-v1.md](SERVER-B-SECURE-SSH-BOOTSTRAP-v1.md).

---

## 3. Host firewall / intrusion baseline (Phase 3D)

| Control | State | Class |
|---------|-------|-------|
| ufw | **active** — deny in / allow out; **22/tcp only** | **HARDENED** |
| fail2ban | **active** — jail `sshd` | **HARDENED** |
| External root password guessing (Phase 3B) | observed historically | residual → mitigated by Phase 3C auth + 3D UFW/fail2ban |

Authoritative: [SERVER-B-FIREWALL-BASELINE-v1.md](SERVER-B-FIREWALL-BASELINE-v1.md), [SERVER-B-FAIL2BAN-BASELINE-v1.md](SERVER-B-FAIL2BAN-BASELINE-v1.md), [SERVER-B-BASE-OS-SECURITY-v1.md](SERVER-B-BASE-OS-SECURITY-v1.md).

---

## 4. Service / package posture (selected)

| Item | State |
|------|-------|
| ssh | active; port 22 |
| docker / nginx / x-ui / xray | **ABSENT** |
| atop / snapd / cloud-init | **PRESENT** (not mutated) |
| systemd-timesyncd | enabled; clock synchronized **no** — Phase 3D residual (UDP/123) |

---

## 5. Phase 3C / 3D handoff checklist

| Step | Status |
|------|--------|
| Prove SSH access to pristine host | **DONE** (Phase 3B) |
| Create dedicated operator sudo user | **DONE** (`marsops`) |
| Generate Ed25519 key into local-only contour | **DONE** |
| Install public key; verify second session | **DONE** |
| Verify sudo | **DONE** |
| Disable direct root/password SSH after verification | **DONE** |
| Confirm provider emergency console available | **SAFE UNKNOWN** live / operator policy |
| Host firewall + fail2ban | **DONE** (Phase 3D) |
| NTP sync investigation | **DONE** — residual documented |
| OS package upgrade baseline | **DONE** — reboot required deferred |
| Direct TUN-OFF network retest | **PENDING** Phase 3E (operator script ready) |

---

## 6. Related

- [SERVER-B-BASE-OS-SECURITY-v1.md](SERVER-B-BASE-OS-SECURITY-v1.md)  
- [SERVER-B-SSH-ACCESS-MODEL-v1.md](SERVER-B-SSH-ACCESS-MODEL-v1.md)  
- [SERVER-B-SSH-ROLLBACK-v1.md](SERVER-B-SSH-ROLLBACK-v1.md)  
- [../../SECRET-HANDLING-MODEL-v1.md](../../SECRET-HANDLING-MODEL-v1.md)  

---

*Bootstrap baseline · Phase 3B historical + Phase 3C SSH + Phase 3D host security.*

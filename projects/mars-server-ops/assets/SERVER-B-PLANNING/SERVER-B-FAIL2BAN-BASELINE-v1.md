# Server B Fail2ban Baseline v1

**Status:** **ACTIVE** — 2026-08-25  
**Wave:** MARS Server Ops Phase 3D  
**Package:** `fail2ban` 1.0.2-3ubuntu0.1 (Ubuntu noble)  
**Not:** intentional ban-proof via brute force, custom action scripts, or non-SSH jails

---

## 1. Installation

| Item | Value |
|------|-------|
| Source | Official Ubuntu repository |
| Dependencies newly installed | `python3-pyasyncore`, `python3-pyinotify`, `whois` |
| Third-party scripts | **NONE** |

---

## 2. Managed jail drop-in

**Remote path:** `/etc/fail2ban/jail.d/00-mars-server-ops-ssh.conf`

```ini
[sshd]
enabled = true
port = 22
filter = sshd
backend = systemd
maxretry = 5
findtime = 10m
bantime = 1h
```

| Check | Result |
|-------|--------|
| `fail2ban-client -t` | **PASS** (OK) |
| `systemctl enable --now fail2ban` | **PASS** |
| Unit active | **PASS** |
| Jail list | `sshd` only (Phase 3D) |

---

## 3. Validation snapshot

| Field | Value |
|-------|-------|
| Jail | `sshd` |
| Backend / log source | systemd journal (`_SYSTEMD_UNIT=sshd.service + _COMM=sshd`) |
| Currently banned | 0 |
| Total banned | 0 |
| Brute-force proof test | **NOT PERFORMED** (charter forbids) |

---

## 4. Operator note

Thresholds are intentionally moderate to reduce operator lockout risk. SSH remains key-only; fail2ban complements UFW, it does not replace key auth.

---

*Fail2ban baseline · sshd jail active · no secrets.*

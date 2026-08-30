# Server B Secure SSH Bootstrap v1

**Status:** **COMPLETE** — 2026-08-25  
**Wave:** MARS Server Ops Phase 3C  
**Planning locus:** `SERVER-B-PLANNING`  
**Verdict:** **PASS WITH RESIDUALS**  
**Not:** firewall/fail2ban baseline, NTP fix, DNS, 3X-UI, Xray, Docker, nginx, or Server A work

---

## 1. Purpose

Replace temporary public `root` + password SSH bootstrap with controlled MARS operator access:

```text
MARS/Cursor → Ed25519 private key → marsops (sudo) → Server B
```

Only after dual key-session + sudo validation: disable direct root SSH and SSH password authentication.

---

## 2. Preflight (session)

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| Foreign WIP | **PRESERVED** (untouched) |
| Commit / push | **NONE** |

---

## 3. Operator account (sanitized)

| Field | Value |
|-------|-------|
| Username | `marsops` |
| Home | `/home/marsops` |
| Shell | `/bin/bash` |
| Groups | `marsops`, `sudo` |
| Remote auth | Ed25519 public key only (post-hardening) |
| Sudo model | password-confirmed (`NOPASSWD` **not** used) |
| Sudo password | **LOCAL ONLY** — `secrets.local.md` |

---

## 4. SSH key (sanitized)

| Field | Value |
|-------|-------|
| Algorithm | Ed25519 |
| Comment | `marsops@metacode-cloud.com` |
| Fingerprint | `SHA256:LKHbvYWrslvA0Ip+WHGmZ4AbaULLCuXr22sxGBNAXsA` |
| Local private key path | `X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\ssh\marsops_ed25519` |
| Local public key path | `X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\ssh\marsops_ed25519.pub` |
| Private key in Git | **NONE** |
| Public key body in Git | **NOT COPIED** (fingerprint only) |

---

## 5. Mutation sequence (executed)

| Step | Result |
|------|--------|
| A. Root bootstrap connect | **PASS** |
| B/C. Create `marsops` + sudo | **PASS** |
| D/E. Install authorized_keys (`700` / `600`, owner `marsops`) | **PASS** |
| F/G. First key session | **PASS** |
| H. Sudo validation (`uid=0`) | **PASS** |
| I. Second independent key + sudo | **PASS** |
| J. Prepare hardening drop-in | **PASS** (final path `00-…`) |
| K. `sshd -t` | **PASS** |
| L. `systemctl reload ssh` (not restart) | **PASS** |
| M. Existing elevated session kept usable | **PASS** (marsops keepalive after root remote disabled) |
| N/O. Post-reload key + sudo | **PASS** |
| P. Negative auth (root password / password auth) | **PASS** — rejected |

**Ordering note:** Initial managed file was briefly `99-mars-server-ops-hardening.conf`. Effective `PasswordAuthentication` remained `yes` because Ubuntu OpenSSH first-match retained `50-cloud-init.conf` (`PasswordAuthentication yes`). Corrected in-wave by relocating managed content to `00-mars-server-ops-hardening.conf` (first-match wins) and removing the `99-` file. Final state validated.

---

## 6. SSH configuration change

| Item | Value |
|------|-------|
| Managed remote path | `/etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf` |
| Provider cloud-init drop-in | `/etc/ssh/sshd_config.d/50-cloud-init.conf` — **left in place** (still contains `PasswordAuthentication yes`; superseded by first-match `00-`) |
| Main `/etc/ssh/sshd_config` | **not destructively rewritten** |
| Apply method | `sshd -t` then `systemctl reload ssh` |
| Port change | **NONE** (22) |

Target effective settings (post-fix validation):

| Directive | Effective |
|-----------|-----------|
| `PermitRootLogin` | `no` |
| `PasswordAuthentication` | `no` |
| `KbdInteractiveAuthentication` | `no` |
| `PubkeyAuthentication` | `yes` |
| `MaxAuthTries` | `3` |
| `Port` | `22` |

---

## 7. Negative authentication tests

| Case | Attempts | Result |
|------|----------|--------|
| `marsops` + password | 1 | **REJECTED** (`BadAuthenticationType`) |
| `root` + password | 1 | **REJECTED** (`BadAuthenticationType`) |

No brute force. Credentials not printed.

---

## 8. Root recovery state

| Item | State |
|------|-------|
| Linux `root` account | **PRESENT** (not deleted) |
| Root password | **PRESERVED** in local secret contour (emergency/history) |
| Direct remote root SSH | **DISABLED** |
| Provider emergency console | **UNCHANGED** this wave (availability **SAFE UNKNOWN** live) |

---

## 9. Explicit non-actions

| Surface | State |
|---------|-------|
| UFW / nft / iptables mutation | **NONE** |
| fail2ban install | **NONE** |
| NTP / clock sync fix | **NONE** |
| 3X-UI / Xray / nginx / Docker | **ABSENT** / untouched |
| DNS / TLS | **NONE** |
| Server A | **UNTOUCHED** |
| Provider panel | **UNTOUCHED** |

---

## 10. Residuals

- Clock synchronized = **no** (NTP service residual from Phase 3B)  
- Host firewall inactive; fail2ban absent — Phase 3D  
- Direct post-provision network retest with operator TUN OFF — **PENDING** (not this wave)  
- Final MCA asset registration — **PENDING**  
- DNS for `metacode-cloud.com` — **NOT** mutated  

---

## 11. Evidence / secret refs

| Item | Location |
|------|----------|
| Local secrets | `X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\secrets.local.md` |
| Local keys | `X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\ssh\` |
| Local evidence log | `X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\phase3c_evidence.txt` (operator-local; may contain host identifiers — **not Git**) |

---

## 12. Related

- [SERVER-B-SSH-ACCESS-MODEL-v1.md](SERVER-B-SSH-ACCESS-MODEL-v1.md)  
- [SERVER-B-SSH-ROLLBACK-v1.md](SERVER-B-SSH-ROLLBACK-v1.md)  
- [SERVER-B-BOOTSTRAP-BASELINE-v1.md](SERVER-B-BOOTSTRAP-BASELINE-v1.md)  
- [SERVER-B-CURRENT-PASSPORT-v1.md](SERVER-B-CURRENT-PASSPORT-v1.md)  

---

*Phase 3C secure SSH bootstrap · PASS WITH RESIDUALS · no secrets in Git.*

# Server B SSH Rollback v1

**Status:** **DOCUMENTED** — 2026-08-25  
**Wave:** Phase 3C  
**Scope:** Managed SSH hardening drop-in only  
**Not:** full OS restore, provider rebuild, or password rotation procedure

---

## 1. Managed artifact

| Item | Path |
|------|------|
| Current hardening drop-in | `/etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf` |
| Superseded temporary name (removed) | `/etc/ssh/sshd_config.d/99-mars-server-ops-hardening.conf` |
| Cloud-init drop-in (untouched) | `/etc/ssh/sshd_config.d/50-cloud-init.conf` |

Rollback for Phase 3C SSH policy = remove/replace the **MARS-managed** `00-` file only. Do not blindly rewrite `/etc/ssh/sshd_config`.

---

## 2. Preferred rollback (while key access works)

From a working `marsops` key session with sudo:

```text
1. sudo rm -f /etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf
2. sudo sshd -t
3. sudo systemctl reload ssh
4. Validate: fresh marsops key session still works
5. Re-check: sshd -T | egrep 'permitrootlogin|passwordauthentication|...'
```

**Warning:** Removing the `00-` file may restore first-match `PasswordAuthentication yes` from `50-cloud-init.conf` and/or main-file `PermitRootLogin yes` depending on Include order. Treat that as **emergency temporary** bootstrap only; re-harden promptly.

---

## 3. If new sessions fail but an existing session remains

1. Keep the existing elevated/`marsops` session open.  
2. Restore prior known-good managed file content **or** remove the broken drop-in.  
3. `sshd -t` **before** reload.  
4. `systemctl reload ssh` (not restart / not reboot).  
5. Open a **fresh** validation session before closing the keepalive session.

---

## 4. Provider console fallback

Use provider emergency console **only** if:

- no verified remote key session remains, **and**  
- in-band rollback cannot be executed.

Console steps (operator-led): same file removal / `sshd -t` / reload discipline.

---

## 5. Non-rollback items

| Item | Note |
|------|------|
| `marsops` user | Not removed by SSH drop-in rollback |
| authorized_keys | Independent of drop-in; do not delete casually |
| Root password | Remains local emergency secret |
| UFW / fail2ban | Not installed in Phase 3C — N/A |

---

## 6. Related

- [SERVER-B-SECURE-SSH-BOOTSTRAP-v1.md](SERVER-B-SECURE-SSH-BOOTSTRAP-v1.md)  
- [SERVER-B-SSH-ACCESS-MODEL-v1.md](SERVER-B-SSH-ACCESS-MODEL-v1.md)  

---

*SSH rollback · managed drop-in only · reload not restart · no secrets in Git.*

# FriendHosting — Final Operational Restore Procedure v1

**inventory_ref:** FRIENDHOSTING-DE  
**Status:** RESTORE PROCEDURE **CONFIRMED** (written + hash-validated backup)  
**Bare-metal / destructive restore drill:** **NOT YET EXERCISED**  
**Canonical backup (this freeze):** `friendhosting-final-operational-20260830T125003Z.tgz`  
**SHA-256:** `1012e3157db97ea3ba2a1c4d0b8d02328223e6656adf12ade22fa1adbb3a0ea2`  
**Remote:** `/root/mars-backups/friendhosting-final-operational-20260830T125003Z.tgz`  
**Local twin:** `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-final-operational-20260830T125003Z.tgz`  
**Related model:** [BACKUP-RESTORE-MODEL-v1.md](../BACKUP-RESTORE-MODEL-v1.md)

---

## 1. Purpose

Restore the accepted post–Plus / post–P2 / post–P3 FriendHosting operational stack after:

- configuration loss;
- accidental mutation;
- bad future hardening;
- client-model mistake;
- nginx/TLS breakage;
- 3X-UI / Xray corruption.

This is a **human-operated** scoped restore. It is **not** an automated DR product and **not** proof of full bare-metal recovery until a destructive drill is chartered and evidenced.

---

## 2. Accepted target state (post-restore PASS criteria)

| Item | Expected |
|------|----------|
| Hardware | 2 vCPU / ~1.9 GiB RAM / 20 GiB disk / 2 GiB swap |
| SSH | `:3333`, key-only, PasswordAuthentication disabled |
| nginx | `:443` TLS for `metacode-cloud.com` |
| ACME | webroot `/var/www/letsencrypt`, UFW `:80` allow, certbot.timer active |
| 3X-UI | localhost `:20901`; public `:2096` DENY |
| Xray | VLESS + TLS + RAW/TCP `:8443` |
| Clients | **6** labels: WSP-ONE, MCA-PHONE, Unit-01, Unit-02, Unit-03, Unit-MichaelPhone |
| Legacy | MCA-ONE-FRIENDHOSTING-DE-RAW-8443 **absent** |
| UFW | default deny; allow 3333/443/8443/80; deny 20901/2096 |
| fail2ban | active (sshd + related jails) |

Do **not** invent `:24443` during restore.

---

## 3. Prerequisites (OS / packages)

On a fresh or damaged Ubuntu 24.04 host intended to become FRIENDHOSTING-DE:

1. Confirm operator out-of-band console access (provider panel) before touching SSH.
2. Install baseline packages as needed: `openssh-server`, `ufw`, `fail2ban`, `nginx`, `certbot`, `python3`, `curl`, `sqlite3`.
3. Ensure disk ≥ 20 GiB and enough free space for extract (~200 MiB staging + services).
4. Place the archive on the host (from local twin or remaining remote copy):

```bash
# from operator workstation (example)
scp -P 3333 "X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-final-operational-20260830T125003Z.tgz" root@92.42.99.126:/root/mars-backups/
```

5. Verify integrity:

```bash
cd /root/mars-backups
echo '1012e3157db97ea3ba2a1c4d0b8d02328223e6656adf12ade22fa1adbb3a0ea2  friendhosting-final-operational-20260830T125003Z.tgz' | sha256sum -c -
tar -tzf friendhosting-final-operational-20260830T125003Z.tgz | head
```

6. Extract to staging (do **not** overwrite live trees blindly):

```bash
tar -C /root/mars-backups -xzf /root/mars-backups/friendhosting-final-operational-20260830T125003Z.tgz
ST=/root/mars-backups/friendhosting-final-operational-20260830T125003Z
```

Archive layout (key trees):

- `etc-ssh/`, `etc-sudoers`, `etc-sudoers.d/`
- `etc-ufw/`, `etc-fail2ban/`
- `etc-nginx/`, `etc-letsencrypt/`, `hooks/`
- `usr-local-x-ui/`, `x-ui-db/etc-x-ui/`
- `fstab`, `journald.conf`, `journald.conf.d/`
- `meta/` (safe listeners, UFW status, `clients-safe.json`, fingerprints)
- `systemd/`, `package/`

---

## 4. Restore order (scoped)

**STOP** any concurrent mutation charter. Prefer provider console session open.

### 4.1 SSH (lockout risk — highest care)

1. Diff staging vs live: `/etc/ssh`, sudoers, `authorized_keys` fingerprints in `meta/`.
2. Restore only after confirming a working console path:

```bash
cp -a "$ST/etc-ssh/." /etc/ssh/
# review sudoers before copy
cp -a "$ST/etc-sudoers" /etc/sudoers
cp -a "$ST/etc-sudoers.d/." /etc/sudoers.d/
sshd -t && systemctl reload ssh
```

3. Validate new SSH session on `:3333` **before** closing the console session.
4. Confirm PasswordAuthentication remains disabled (`sshd -T | grep -i passwordauthentication`).

### 4.2 UFW

```bash
cp -a "$ST/etc-ufw/." /etc/ufw/
ufw --force enable
ufw status verbose
```

Expect allow 3333/443/8443/80 and deny 20901/2096. Rule **order** matters — re-check numbered rules if traffic misbehaves.

### 4.3 fail2ban

```bash
cp -a "$ST/etc-fail2ban/." /etc/fail2ban/
systemctl restart fail2ban
fail2ban-client status
```

### 4.4 nginx

```bash
cp -a "$ST/etc-nginx/." /etc/nginx/
nginx -t && systemctl reload nginx
```

### 4.5 Let's Encrypt / certbot

```bash
# SECRET-BEARING — private keys included
cp -a "$ST/etc-letsencrypt/." /etc/letsencrypt/
# restore renewal hooks if present
test -d "$ST/hooks/renewal-hooks" && cp -a "$ST/hooks/renewal-hooks/." /etc/letsencrypt/renewal-hooks/
systemctl enable --now certbot.timer
certbot certificates
# optional non-mutating check when ACME path healthy:
# certbot renew --dry-run
```

Stale certificate risk: if DNS/IP no longer match, do **not** force-renew until nginx webroot and `:80` are correct.

### 4.6 3X-UI / x-ui database + application

```bash
systemctl stop x-ui || true
cp -a "$ST/usr-local-x-ui/." /usr/local/x-ui/
mkdir -p /etc/x-ui
cp -a "$ST/x-ui-db/etc-x-ui/." /etc/x-ui/
# includes x-ui.db — schema must match panel binary version in this archive (3.7.0)
systemctl daemon-reload
systemctl enable x-ui
systemctl start x-ui
```

DB/schema mismatch risk: do not mix a newer/older panel binary with this `x-ui.db` without an explicit migration charter.

### 4.7 Xray operational state

Xray is managed by x-ui; starting `x-ui` should regenerate/bind `:8443` from DB + `bin/config.json` in the restored tree. Confirm:

```bash
ss -lntp | egrep ':(8443|20901)\b'
```

### 4.8 swap / fstab / journald

```bash
cp -a "$ST/fstab" /etc/fstab
# ensure /swapfile exists matching meta/swapfile-ls.txt; recreate if missing:
# fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile
cp -a "$ST/journald.conf" /etc/systemd/journald.conf
test -d "$ST/journald.conf.d" && mkdir -p /etc/systemd/journald.conf.d && cp -a "$ST/journald.conf.d/." /etc/systemd/journald.conf.d/
systemctl restart systemd-journald
swapon --show
```

### 4.9 daemon-reload / service order

Preferred start order after files restored:

1. `sshd` (already validated)
2. `ufw`
3. `fail2ban`
4. `nginx`
5. `certbot.timer`
6. `x-ui` (brings Xray)

```bash
systemctl daemon-reload
systemctl restart fail2ban nginx
systemctl restart x-ui
systemctl is-active ssh nginx x-ui fail2ban certbot.timer
```

---

## 5. Post-restore validation

1. **Listeners:** `ss -lntp` shows `:3333`, `:443`, `:80`, `:8443`, `127.0.0.1:20901`; `:2096` may listen locally but UFW DENY public.
2. **TLS:** handshake PASS on `:443` and `:8443` for `metacode-cloud.com`.
3. **Transport:** VLESS RAW/TCP `:8443` accepts client.
4. **3X-UI:** localhost panel reachable; public `:2096` denied.
5. **Client count / identities:** exactly **6** emails listed above; legacy absent (`meta/clients-safe.json` as reference).
6. **UFW / fail2ban / swap / certbot.timer:** as accepted posture.
7. **Real-workload smoke:** operator activates WSP-ONE (or MCA-PHONE), confirms egress `92.42.99.126`, HTTPS works.

---

## 6. Recovery risks (explicit)

| Risk | Mitigation |
|------|------------|
| SSH lockout | Provider console open; `sshd -t` before reload; dual-session validate |
| Stale certificate state | Restore LE tree intact; fix nginx webroot + `:80` before renew |
| x-ui DB/schema mismatch | Keep panel binary + DB from **same** archive |
| Firewall rule ordering | Compare `ufw status numbered` to `meta/ufw-status.txt` |
| Per-device identity loss | Restore `x-ui.db`; local client registry under `...\FRIENDHOSTING-GERMANY\clients\` is backup only |
| Partial restore drift | Prefer full scoped trees from this freeze; avoid mixing older P2/P3 archives unless intentional rollback |

---

## 7. Restore confidence statement

```text
BACKUP: PASS (remote + local twin, SHA-256 match, archive readable)
RESTORE STRATEGY: CONFIRMED
RESTORE PROCEDURE CONFIRMED
FULL BARE-METAL RESTORE NOT YET EXERCISED
```

---

## 8. Secrets

This archive is **SECRET-BEARING** (TLS private keys, x-ui DB with client IDs, SSH host/config material).  
**Never** commit the `.tgz` to Git. Keep twins under `/root/mars-backups/` and `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\` only.

---

*FriendHosting final operational restore v1 · freeze 20260830T125003Z · human-operated.*

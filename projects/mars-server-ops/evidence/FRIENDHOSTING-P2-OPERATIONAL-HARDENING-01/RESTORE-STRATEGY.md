# Restore strategy — FriendHosting P2 pre-hardening (20260830T093108Z)

## Artifacts
- Remote: `/root/mars-backups/friendhosting-plus-p2-pre-hardening-20260830T085016Z.tgz`
- Local: `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-plus-p2-pre-hardening-20260830T085016Z.tgz`
- SHA-256: see `02-backup-validation.json`

## Covers
3X-UI / x-ui tree, panel DB paths, nginx, Let's Encrypt, SSH, UFW, fail2ban (if present at backup time),
systemd unit cats, package selections, listener snapshot.

## Exact restore order (operator-led; authorize before execute)
1. Keep an active recovery session (provider console or proven SSH key).
2. Copy archive to host; verify SHA-256.
3. Extract to a staging directory under `/root/mars-restore/`.
4. Stop only scoped services: `systemctl stop nginx x-ui` (keep `ssh` running).
5. Restore nginx / letsencrypt / x-ui / ufw from staging **after review**.
6. SSH: **review** `etc-ssh` before overwrite; never lock out `:3333`.
7. `nginx -t` then start nginx; start x-ui; verify listeners.
8. Validate: SSH `:3333`, nginx `:443`, Xray `:8443`, panel localhost `:20901`, VPN egress `92.42.99.126`.

## Rollback boundary
Does **not** automatically roll back later identity/inbound changes if made after this backup.
Full DR drill still optional (P1 residual).

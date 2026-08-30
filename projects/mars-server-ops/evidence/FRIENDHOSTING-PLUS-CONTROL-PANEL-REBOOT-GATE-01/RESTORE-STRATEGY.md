# Restore strategy — FRIENDHOSTING-PLUS-CONTROL-PANEL-REBOOT-GATE-01

## Classification
**BACKUP + RESTORE STRATEGY CONFIRMED**

## Backup anchors
- Remote: `/root/mars-backups/friendhosting-plus-pre-panel-reboot-20260830T073335Z.tgz`
- Local: `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-plus-pre-panel-reboot-20260830T073335Z.tgz`
- SHA-256: `04344ea5fb7d90086360753060197a2e2371f063f0efbef60bd713efe96ff002`
- Hash match remote/local: **YES**

## Scope covered
3X-UI / x-ui tree + DB, Xray binaries/config under `/usr/local/x-ui`, nginx `/etc/nginx`,
Let's Encrypt `/etc/letsencrypt`, UFW `/etc/ufw`, SSH `/etc/ssh`, critical systemd unit cats,
package selections, network/listener/firewall baselines, hardware snapshot.

## Exact restore order (operator-led; authorize before execute)
1. Confirm SSH access on `:3333` still works (or provider console).
2. `mkdir -p /root/mars-backups && cd /root/mars-backups`
3. Verify archive: `sha256sum -c friendhosting-plus-pre-panel-reboot-20260830T073335Z.tgz.sha256` (or compare to `04344ea5fb7d90086360753060197a2e2371f063f0efbef60bd713efe96ff002`).
4. Extract: `tar -C /root/mars-backups -xzf friendhosting-plus-pre-panel-reboot-20260830T073335Z.tgz`
5. Stop services carefully: `systemctl stop nginx x-ui` (keep `ssh` running).
6. Restore 3X-UI: copy `friendhosting-plus-pre-panel-reboot-20260830T073335Z/usr-local/x-ui/` → `/usr/local/x-ui/` (review first).
7. Restore nginx: copy `friendhosting-plus-pre-panel-reboot-20260830T073335Z/etc/nginx/` → `/etc/nginx/` (review sites-enabled).
8. Restore ACME: copy `friendhosting-plus-pre-panel-reboot-20260830T073335Z/etc/letsencrypt/` → `/etc/letsencrypt/` (secret-bearing).
9. Restore UFW configs from `friendhosting-plus-pre-panel-reboot-20260830T073335Z/etc/ufw/` if rules drifted; re-apply intended allows 3333/443/8443.
10. SSH config: **review** `friendhosting-plus-pre-panel-reboot-20260830T073335Z/etc/ssh/` before overwrite; never lock out `:3333`.
11. `systemctl daemon-reload`
12. Start order: `systemctl start x-ui` → verify `127.0.0.1:20901` → `systemctl start nginx` → verify `:443` → confirm Xray `:8443`.
13. Listener check: `ss -lntup` for 3333 / 443 / 8443 / 127.0.0.1:20901.
14. TLS: `openssl s_client` / `openssl verify` for `metacode-cloud.com` on 443 and 8443.
15. VPN validation: profile `MCA-ONE-FRIENDHOSTING-DE-RAW-8443` → egress `92.42.99.126`.
16. Panel validation: nginx → localhost panel path (secret local-only).

## Rollback boundary
- Restores FriendHosting CURRENT-STATE configs/data in archive.
- Does **not** restore VEESP/EQVPS.
- Does **not** expand disk.
- Does **not** invent missing Plus hardware.

## Post-restore PASS criteria
SSH :3333, nginx :443, Xray :8443, 3X-UI 127.0.0.1:20901, TLS verify OK, VPN egress 92.42.99.126.

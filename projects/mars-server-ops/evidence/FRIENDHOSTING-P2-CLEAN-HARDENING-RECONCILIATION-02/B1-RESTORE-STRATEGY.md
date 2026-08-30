# Restore strategy — friendhosting-p2-clean-hardened-state-20260830T102110Z
# inventory_ref: FRIENDHOSTING-DE
# created: 20260830T102110Z
# remote: /root/mars-backups/friendhosting-p2-clean-hardened-state-20260830T102110Z.tgz
# local: X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-p2-clean-hardened-state-20260830T102110Z.tgz
# sha256: bb9a07045cc610c52275895cf4679881699906df24284e147f059486098d243c
# sha_match: True

## Scope
Config/state restore for SSH, sudo, UFW, fail2ban, swap/fstab metadata, journald,
nginx, Let's Encrypt, 3X-UI/x-ui tree + panel DB, systemd unit status snapshot,
package inventory, listeners baseline.

Does NOT restore running RAM, kernel, disk layout, or provider panel settings.
Does NOT automatically reverse later identity/inbound changes made after this backup.

## Procedure (human-operated)
1. STOP active mutation; confirm charter rollback section.
2. Copy archive to host: scp -P 3333 friendhosting-p2-clean-hardened-state-20260830T102110Z.tgz root@92.42.99.126:/root/mars-backups/
3. Verify: sha256sum -c friendhosting-p2-clean-hardened-state-20260830T102110Z.tgz.sha256
4. Extract to staging: tar -C /root/mars-backups -xzf /root/mars-backups/friendhosting-p2-clean-hardened-state-20260830T102110Z.tgz
5. Review diffs before overwrite (esp. sshd, ufw, nginx, x-ui.db, letsencrypt).
6. Restore scoped trees from staging after review.
7. nginx -t && systemctl reload nginx; systemctl restart x-ui (expect brief panel blip).
8. Validate: SSH :3333, nginx :443, Xray :8443, UFW, fail2ban, certbot certificates.
9. File evidence under evidence/FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02/.

## Post-restore validation
- ssh key login root + marsops on :3333
- PasswordAuthentication no
- ufw status shows allow 3333/443/8443 (+80 if ACME webroot active)
- curl TLS :443 / :8443
- systemctl is-active ssh nginx x-ui fail2ban

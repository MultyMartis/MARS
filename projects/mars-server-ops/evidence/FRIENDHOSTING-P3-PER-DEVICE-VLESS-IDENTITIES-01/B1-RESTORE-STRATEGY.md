# Restore strategy — friendhosting-p3-pre-device-identities-20260830T105341Z
# inventory_ref: FRIENDHOSTING-DE
# created: 20260830T105341Z
# remote: /root/mars-backups/friendhosting-p3-pre-device-identities-20260830T105341Z.tgz
# local: X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-p3-pre-device-identities-20260830T105341Z.tgz
# sha256: dbdc2da01a33e1a109b3cedd8e19a3a4323a4cabf1c2d59244139096ef44eaa2
# sha_match: True

## Scope
Pre-mutation P3 checkpoint covering:
- /etc/x-ui (panel DB)
- /usr/local/x-ui (panel + generated Xray)
- meta/x-ui.db + meta/xray-config.json + meta/clients-safe.json
- nginx, letsencrypt, ufw, fail2ban, ssh snapshots (same class as P2)

Does NOT restore RAM/kernel/disk/provider panel.
Does NOT auto-apply later client additions made after this backup.

## Procedure (human-operated)
1. STOP active mutation; confirm charter rollback section.
2. Copy archive: scp -P 3333 friendhosting-p3-pre-device-identities-20260830T105341Z.tgz root@92.42.99.126:/root/mars-backups/
3. Verify: sha256sum -c friendhosting-p3-pre-device-identities-20260830T105341Z.tgz.sha256
4. Extract staging: tar -C /root/mars-backups -xzf /root/mars-backups/friendhosting-p3-pre-device-identities-20260830T105341Z.tgz
5. Review diffs (esp. x-ui.db, xray config, nginx, sshd, ufw).
6. Restore scoped trees from staging after review.
7. nginx -t && systemctl reload nginx; systemctl restart x-ui
8. Validate: SSH :3333, nginx :443, Xray :8443, legacy client MCA-ONE-FRIENDHOSTING-DE-RAW-8443 present.
9. File evidence under evidence/FRIENDHOSTING-P3-PER-DEVICE-VLESS-IDENTITIES-01/

## Post-restore validation
- ssh key login root on :3333
- systemctl is-active x-ui nginx ssh
- TLS :8443 OK
- inbound :8443 still VLESS+TLS+RAW; SNI metacode-cloud.com
- legacy fallback client still enabled

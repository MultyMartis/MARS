# Restore strategy — pre-legacy-retirement
# inventory_ref: FRIENDHOSTING-DE
# remote_full: /root/mars-backups/friendhosting-p3-pre-legacy-retirement-20260830T120733Z.tgz
# sha256_full: 4952b6368ad884be1a6737506f7f81c8464aaa28cb2e44807c038049918abac8
# remote_essential: /root/mars-backups/friendhosting-p3-pre-legacy-retirement-ESSENTIAL-20260830T122055Z.tgz
# local_essential: X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-p3-pre-legacy-retirement-ESSENTIAL-20260830T122055Z.tgz
# sha256_essential: 647ca4da349e26ce4617ecc9a1cf2cfc1aaf7a5c89a8fd31d9f4d1ad30ff9ddc
# sha_match_essential: True

## Scope
Pre-delete seven-client checkpoint (includes legacy `MCA-ONE-FRIENDHOSTING-DE-RAW-8443`).

## Procedure
1. STOP mutation.
2. Verify SHA of essential or full archive.
3. Extract staging under `/root/mars-backups/`.
4. `systemctl stop x-ui`
5. Restore `/etc/x-ui` (from essential or full) after review.
6. Optionally restore `meta/xray-config.json` into `/usr/local/x-ui/bin/config.json` if generator lag.
7. `systemctl start x-ui`
8. Verify **7** clients including legacy; WSP-ONE enabled; SSH :3333; Xray :8443; nginx :443.

## Post-restore
- seven clients
- WSP-ONE smoke

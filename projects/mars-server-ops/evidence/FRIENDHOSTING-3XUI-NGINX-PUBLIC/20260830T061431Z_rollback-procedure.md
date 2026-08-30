# Rollback — FriendHosting nginx 3X-UI public access 20260830T061431Z

## Classification
BACKUP + RESTORE STRATEGY CONFIRMED

## Remote checkpoint
`/root/mars-backups/friendhosting-nginx-3xui-20260830T061431Z`

## Local checkpoint copy
`X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\nginx-public-access-20260830T061431Z\remote-checkpoint.tgz`
SHA256: `c0bf2c5b1a7a82e44047b59f56e081047b10b6afea9fa465c1455ac5457824d9`

## Exact rollback steps
1. `rm -f /etc/nginx/sites-enabled/metacode-cloud-3xui /etc/nginx/sites-available/metacode-cloud-3xui`
2. If nginx installed only for this task: `systemctl disable --now nginx`
3. Restore UFW: `ufw delete allow 443/tcp` if added this wave; keep 3333/8443
4. Verify 127.0.0.1:20901 unchanged
5. Verify :443 free
6. Verify VPN :8443 and SSH :3333 healthy

## Do NOT
- Touch VEESP / EQVPS
- Change VLESS UUID / :8443
- Change SSH :3333
- Open :20901 publicly

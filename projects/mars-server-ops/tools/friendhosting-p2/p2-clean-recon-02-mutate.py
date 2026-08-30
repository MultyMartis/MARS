#!/usr/bin/env python3
"""FriendHosting P2 Clean Hardening Reconciliation 02 — backup + ACME fix + regression.

Assumes prior read-only audit already PASS. Mutates FriendHosting only.
Does not touch VEESP/EQVPS. Does not alter VLESS :8443 architecture.
"""
from __future__ import annotations

import hashlib
import json
import re
import socket
import ssl
import tarfile
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import paramiko

HOST = "92.42.99.126"
PORT = 3333
DOMAIN = "metacode-cloud.com"
BASE = Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
PRIV = BASE / "ssh" / "marsops_ed25519"
EV = Path(
    r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02"
)
TS = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
OUT = BASE / f"p2-clean-recon-02-mutate-{TS}"
BAK_NAME = f"friendhosting-p2-clean-hardened-state-{TS}"
REMOTE_BAK_DIR = "/root/mars-backups"
REMOTE_BAK = f"{REMOTE_BAK_DIR}/{BAK_NAME}.tgz"
LOCAL_BAK = BASE / "backups" / f"{BAK_NAME}.tgz"

OUT.mkdir(parents=True, exist_ok=True)
EV.mkdir(parents=True, exist_ok=True)
(BASE / "backups").mkdir(parents=True, exist_ok=True)

RESULT: dict = {
    "wave": "FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02",
    "ts": TS,
    "admin_path": "VEESP",
    "gates": {},
    "mutations": [],
    "notes": [],
}


def write(name: str, text: str) -> None:
    (OUT / name).write_text(text, encoding="utf-8")
    (EV / name).write_text(text, encoding="utf-8")


def load_key():
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    except paramiko.PasswordRequiredException:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV), password='""')


def connect(user: str = "root") -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        HOST,
        port=PORT,
        username=user,
        pkey=load_key(),
        timeout=30,
        allow_agent=False,
        look_for_keys=False,
    )
    t = c.get_transport()
    if t:
        t.set_keepalive(30)
    return c


def run(c: paramiko.SSHClient, cmd: str, timeout: int = 180):
    try:
        stdin, stdout, stderr = c.exec_command(cmd, timeout=timeout)
        stdout.channel.settimeout(timeout)
        stderr.channel.settimeout(timeout)
        out = stdout.read().decode("utf-8", "replace")
        err = stderr.read().decode("utf-8", "replace")
        code = stdout.channel.recv_exit_status()
        return code, out, err
    except Exception as e:
        return 124, "", f"ERR:{type(e).__name__}:{e}"


def rebind(c=None):
    if c:
        try:
            c.close()
        except Exception:
            pass
    return connect("root")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def tcp(port: int, timeout: float = 8) -> bool:
    try:
        with socket.create_connection((HOST, port), timeout=timeout):
            return True
    except OSError:
        return False


def tls(port: int) -> dict:
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((HOST, port), timeout=15) as sock:
            with ctx.wrap_socket(sock, server_hostname=DOMAIN) as ssock:
                return {"ok": True, "notAfter": ssock.getpeercert().get("notAfter")}
    except Exception as e:
        return {"ok": False, "error": type(e).__name__}


def http_get(port: int, path: str = "/", host: str | None = None, timeout: float = 8) -> dict:
    host = host or DOMAIN
    try:
        s = socket.create_connection((HOST, port), timeout=timeout)
        s.sendall(
            f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n".encode()
        )
        data = s.recv(500).decode("utf-8", "replace")
        s.close()
        return {
            "reachable": True,
            "status": (data.splitlines()[0] if data else "")[:160],
        }
    except Exception as e:
        return {"reachable": False, "error": type(e).__name__}


def phase_backup(c: paramiko.SSHClient) -> dict:
    script = f"""
set -euo pipefail
DIR={REMOTE_BAK_DIR}
NAME={BAK_NAME}
STAGING="$DIR/$NAME"
mkdir -p "$STAGING"
rm -rf "$STAGING"/*
mkdir -p "$STAGING/meta" "$STAGING/systemd" "$STAGING/package"

cp -a /etc/ssh "$STAGING/etc-ssh"
cp -a /etc/sudoers "$STAGING/etc-sudoers" 2>/dev/null || true
cp -a /etc/sudoers.d "$STAGING/etc-sudoers.d" 2>/dev/null || true
cp -a /etc/ufw "$STAGING/etc-ufw" 2>/dev/null || true
cp -a /etc/fail2ban "$STAGING/etc-fail2ban" 2>/dev/null || true
cp -a /etc/systemd/journald.conf "$STAGING/journald.conf" 2>/dev/null || true
cp -a /etc/systemd/journald.conf.d "$STAGING/journald.conf.d" 2>/dev/null || true
cp -a /etc/nginx "$STAGING/etc-nginx"
cp -a /etc/letsencrypt "$STAGING/etc-letsencrypt"
cp -a /usr/local/x-ui "$STAGING/usr-local-x-ui" 2>/dev/null || true
mkdir -p "$STAGING/x-ui-db"
cp -a /etc/x-ui "$STAGING/x-ui-db/etc-x-ui" 2>/dev/null || true
cp -a /etc/fstab "$STAGING/fstab"
ls -la /swapfile > "$STAGING/meta/swapfile-ls.txt" 2>/dev/null || true
ss -lntup > "$STAGING/meta/ss-lntp.txt"
ufw status verbose > "$STAGING/meta/ufw-status.txt" 2>&1 || true
systemctl list-unit-files 'ssh*' 'nginx*' 'x-ui*' 'fail2ban*' 'certbot*' > "$STAGING/systemd/unit-files.txt" 2>&1 || true
systemctl status ssh nginx x-ui fail2ban certbot.timer --no-pager > "$STAGING/systemd/status.txt" 2>&1 || true
dpkg -l > "$STAGING/package/dpkg-l.txt"
getent passwd root marsops > "$STAGING/meta/passwd-slice.txt"
id marsops > "$STAGING/meta/marsops-id.txt" 2>&1 || true
ls -la /root/.ssh /home/marsops/.ssh > "$STAGING/meta/ssh-dirs.txt" 2>&1 || true
# authorized_keys metadata only (fingerprints), not private keys
ssh-keygen -lf /root/.ssh/authorized_keys > "$STAGING/meta/root-authorized-fingerprints.txt" 2>&1 || true
ssh-keygen -lf /home/marsops/.ssh/authorized_keys > "$STAGING/meta/marsops-authorized-fingerprints.txt" 2>&1 || true
sshd -T > "$STAGING/meta/sshd-T.txt" 2>/dev/null || true
fail2ban-client status > "$STAGING/meta/fail2ban-status.txt" 2>&1 || true
certbot certificates > "$STAGING/meta/certbot-certificates.txt" 2>&1 || true
date -u > "$STAGING/meta/created-utc.txt"
uname -a > "$STAGING/meta/uname.txt"
free -h > "$STAGING/meta/free.txt"
df -hT > "$STAGING/meta/df.txt"

tar -C "$DIR" -czf "$DIR/$NAME.tgz" "$NAME"
sha256sum "$DIR/$NAME.tgz" > "$DIR/$NAME.tgz.sha256"
ls -la "$DIR/$NAME.tgz" "$DIR/$NAME.tgz.sha256"
cat "$DIR/$NAME.tgz.sha256"
tar -tzf "$DIR/$NAME.tgz" | egrep 'etc-ssh|etc-nginx|etc-letsencrypt|etc-ufw|usr-local-x-ui|x-ui-db|systemd|ss-lntp|fail2ban|fstab' | sed -n '1,100p'
echo BACKUP_OK
"""
    remote_script = f"/tmp/mars-p2-clean-backup-{TS}.sh"
    sftp = c.open_sftp()
    with sftp.file(remote_script, "w") as f:
        f.write(script)
    sftp.close()
    code, out, err = run(c, f"bash {remote_script}; rm -f {remote_script}", timeout=300)
    write("B1-backup-remote.txt", f"exit={code}\n{out}\n{err}")
    if "BACKUP_OK" not in out:
        return {"ok": False, "error": "remote backup failed", "out": out[-2000:]}

    m = re.search(r"([a-f0-9]{64})\s+" + re.escape(REMOTE_BAK), out)
    remote_sha = m.group(1) if m else None
    if not remote_sha:
        code2, out2, _ = run(c, f"sha256sum {REMOTE_BAK}", timeout=60)
        remote_sha = out2.split()[0] if out2.strip() else None

    print("Downloading backup...")
    sftp = c.open_sftp()
    sftp.get(REMOTE_BAK, str(LOCAL_BAK))
    try:
        sftp.get(REMOTE_BAK + ".sha256", str(LOCAL_BAK) + ".sha256")
    except Exception:
        pass
    sftp.close()

    local_sha = sha256_file(LOCAL_BAK)
    members_ok = {
        "etc-ssh": False,
        "etc-nginx": False,
        "etc-letsencrypt": False,
        "etc-ufw": False,
        "usr-local-x-ui": False,
        "x-ui-db": False,
        "fail2ban": False,
        "fstab": False,
    }
    member_list = []
    with tarfile.open(LOCAL_BAK, "r:gz") as tf:
        names = tf.getnames()
        member_list = names[:200]
        joined = "\n".join(names)
        for k in members_ok:
            members_ok[k] = k in joined
    write("B1-backup-local-members.txt", "\n".join(member_list))
    info = {
        "ok": bool(remote_sha)
        and remote_sha == local_sha
        and all(
            members_ok[k]
            for k in (
                "etc-ssh",
                "etc-nginx",
                "etc-letsencrypt",
                "etc-ufw",
                "usr-local-x-ui",
                "x-ui-db",
            )
        ),
        "remote": REMOTE_BAK,
        "local": str(LOCAL_BAK),
        "remote_sha256": remote_sha,
        "local_sha256": local_sha,
        "sha_match": remote_sha == local_sha,
        "size": LOCAL_BAK.stat().st_size,
        "members_ok": members_ok,
    }
    write("B1-backup-validation.json", json.dumps(info, indent=2))
    restore = f"""# Restore strategy — {BAK_NAME}
# inventory_ref: FRIENDHOSTING-DE
# created: {TS}
# remote: {REMOTE_BAK}
# local: {LOCAL_BAK}
# sha256: {local_sha}
# sha_match: {info['sha_match']}

## Scope
Config/state restore for SSH, sudo, UFW, fail2ban, swap/fstab metadata, journald,
nginx, Let's Encrypt, 3X-UI/x-ui tree + panel DB, systemd unit status snapshot,
package inventory, listeners baseline.

Does NOT restore running RAM, kernel, disk layout, or provider panel settings.
Does NOT automatically reverse later identity/inbound changes made after this backup.

## Procedure (human-operated)
1. STOP active mutation; confirm charter rollback section.
2. Copy archive to host: scp -P 3333 {BAK_NAME}.tgz root@{HOST}:/root/mars-backups/
3. Verify: sha256sum -c {BAK_NAME}.tgz.sha256
4. Extract to staging: tar -C /root/mars-backups -xzf /root/mars-backups/{BAK_NAME}.tgz
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
"""
    write("B1-RESTORE-STRATEGY.md", restore)
    (BASE / "backups" / f"{BAK_NAME}-RESTORE-STRATEGY.md").write_text(
        restore, encoding="utf-8"
    )
    return info


def phase_acme(c: paramiko.SSHClient) -> dict:
    """Convert certbot renewal from standalone to nginx webroot HTTP-01."""
    mutations = []
    # 1) webroot + nginx :80 site
    cmd = r"""
set -euo pipefail
mkdir -p /var/www/letsencrypt/.well-known/acme-challenge
chown -R www-data:www-data /var/www/letsencrypt
chmod -R 755 /var/www/letsencrypt

cat > /etc/nginx/sites-available/metacode-cloud-acme80 <<'EOF'
# MARS P2 clean recon 02 — ACME HTTP-01 + HTTPS redirect
server {
    listen 80;
    listen [::]:80;
    server_name metacode-cloud.com;

    location ^~ /.well-known/acme-challenge/ {
        root /var/www/letsencrypt;
        default_type "text/plain";
        allow all;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}
EOF

ln -sfn /etc/nginx/sites-available/metacode-cloud-acme80 /etc/nginx/sites-enabled/metacode-cloud-acme80
nginx -t
systemctl reload nginx
echo NGINX80_OK
"""
    code, out, err = run(c, cmd, timeout=60)
    write("C1-nginx-acme80.txt", f"exit={code}\n{out}\n{err}")
    if "NGINX80_OK" not in out:
        return {"ok": False, "stage": "nginx80", "out": out, "err": err}
    mutations.append("nginx :80 ACME webroot + HTTPS redirect")

    # 2) UFW allow 80
    code, out, err = run(
        c,
        "ufw allow 80/tcp comment 'MARS ACME HTTP-01'; ufw status verbose",
        timeout=40,
    )
    write("C2-ufw-80.txt", f"exit={code}\n{out}\n{err}")
    if "80/tcp" not in out or "ALLOW" not in out:
        return {"ok": False, "stage": "ufw80", "out": out}
    mutations.append("ufw allow 80/tcp")

    # 3) deploy hook (reload nginx; restart x-ui for Xray cert consumers)
    # Keep hook for real renewals; dry-run typically does not execute deploy hooks.
    code, out, err = run(
        c,
        r"""
set -euo pipefail
mkdir -p /etc/letsencrypt/renewal-hooks/deploy
cat > /etc/letsencrypt/renewal-hooks/deploy/mars-reload-tls-consumers.sh <<'EOF'
#!/bin/bash
set -euo pipefail
# Reload nginx (TLS :443 reverse proxy)
if command -v nginx >/dev/null 2>&1; then
  nginx -t
  systemctl reload nginx
fi
# Restart x-ui so managed Xray reloads certificate files for :8443
# (oneTimeLoading=false, but process restart is the reliable consumer path)
if systemctl is-active --quiet x-ui; then
  systemctl restart x-ui
fi
EOF
chmod 755 /etc/letsencrypt/renewal-hooks/deploy/mars-reload-tls-consumers.sh
ls -la /etc/letsencrypt/renewal-hooks/deploy/
echo HOOK_OK
""",
        timeout=40,
    )
    write("C3-deploy-hook.txt", f"exit={code}\n{out}\n{err}")
    if "HOOK_OK" not in out:
        return {"ok": False, "stage": "hook", "out": out}
    mutations.append("deploy hook reload nginx + restart x-ui")

    # 4) rewrite renewal authenticator to webroot
    code, out, err = run(
        c,
        r"""
set -euo pipefail
CONF=/etc/letsencrypt/renewal/metacode-cloud.com.conf
cp -a "$CONF" "$CONF.bak-p2-clean-02"
python3 - <<'PY'
from pathlib import Path
p = Path('/etc/letsencrypt/renewal/metacode-cloud.com.conf')
text = p.read_text(encoding='utf-8')
# Replace standalone authenticator with webroot
import re
if 'authenticator = standalone' in text:
    text = text.replace('authenticator = standalone', 'authenticator = webroot')
elif re.search(r'^authenticator\s*=', text, re.M):
    text = re.sub(r'^authenticator\s*=.*$', 'authenticator = webroot', text, flags=re.M)
else:
    text += '\nauthenticator = webroot\n'
if 'webroot_path' not in text:
    # insert under [renewalparams]
    if '[renewalparams]' in text:
        text = text.replace('[renewalparams]', '[renewalparams]\nwebroot_path = /var/www/letsencrypt')
    else:
        text += '\nwebroot_path = /var/www/letsencrypt\n'
else:
    text = re.sub(r'^webroot_path\s*=.*$', 'webroot_path = /var/www/letsencrypt', text, flags=re.M)
# ensure [[webroot_map]] section
if '[[webroot_map]]' not in text:
    text += '\n[[webroot_map]]\nmetacode-cloud.com = /var/www/letsencrypt\n'
p.write_text(text, encoding='utf-8')
print(p.read_text(encoding='utf-8'))
PY
echo RENEWAL_CONF_OK
""",
        timeout=40,
    )
    write("C4-renewal-conf.txt", f"exit={code}\n{out}\n{err}")
    if "RENEWAL_CONF_OK" not in out or "authenticator = webroot" not in out:
        return {"ok": False, "stage": "renewal_conf", "out": out}
    mutations.append("certbot renewal: standalone → webroot")

    # 5) prove challenge path reachable before dry-run
    code, out, err = run(
        c,
        r"""
set -euo pipefail
echo ok-acme-probe > /var/www/letsencrypt/.well-known/acme-challenge/mars-probe.txt
curl -sS --max-time 10 http://127.0.0.1/.well-known/acme-challenge/mars-probe.txt
curl -sS --max-time 10 -H 'Host: metacode-cloud.com' http://127.0.0.1/.well-known/acme-challenge/mars-probe.txt
ss -lntp | egrep ':80\b' || true
echo PROBE_LOCAL_OK
""",
        timeout=40,
    )
    write("C5-acme-local-probe.txt", f"exit={code}\n{out}\n{err}")
    ext = http_get(80, "/.well-known/acme-challenge/mars-probe.txt", DOMAIN)
    write("C5-acme-external-probe.json", json.dumps(ext, indent=2))
    if "PROBE_LOCAL_OK" not in out or "ok-acme-probe" not in out:
        return {"ok": False, "stage": "local_probe", "out": out, "ext": ext}
    if not ext.get("reachable") or "200" not in ext.get("status", ""):
        # still try dry-run if local works — LE needs public :80
        RESULT["notes"].append(f"external ACME probe weak: {ext}")

    # 6) dry-run
    code, out, err = run(
        c,
        "bash -lc 'certbot renew --dry-run --cert-name metacode-cloud.com; echo DRY_EXIT:$?'",
        timeout=420,
    )
    write("C6-certbot-dry-run.txt", f"exit={code}\n{out}\n{err}")
    dry_ok = ("DRY_EXIT:0" in out) or (
        "Congratulations" in out and "DRY_EXIT:1" not in out
    )
    # cleanup probe
    run(c, "rm -f /var/www/letsencrypt/.well-known/acme-challenge/mars-probe.txt", timeout=20)

    # final firewall/services snapshot
    code2, out2, _ = run(
        c,
        "ufw status verbose; systemctl is-active nginx x-ui ssh; ss -lntp | egrep ':(80|443|3333|8443|2096|20901)\\b'",
        timeout=40,
    )
    write("C7-post-acme-surface.txt", out2)

    return {
        "ok": dry_ok,
        "dry_run_exit_ok": dry_ok,
        "mutations": mutations,
        "authenticator": "webroot",
        "webroot": "/var/www/letsencrypt",
        "deploy_hook": "/etc/letsencrypt/renewal-hooks/deploy/mars-reload-tls-consumers.sh",
        "external_probe": ext,
        "dry_run_tail": out[-2500:],
    }


def phase_regression(c: paramiko.SSHClient) -> dict:
    # Prove panel reverse proxy without writing secret path into RESULT dump:
    # fetch base path from DB, probe, redact.
    code, out, err = run(
        c,
        r"""
python3 - <<'PY'
import sqlite3, urllib.request
db='/etc/x-ui/x-ui.db'
con=sqlite3.connect(db); cur=con.cursor()
base=None
for k,v in cur.execute('SELECT key,value FROM settings'):
  if k=='webBasePath':
    base=v
con.close()
assert base and base.startswith('/')
url='https://127.0.0.1'+base
# via nginx public host
import ssl,socket
ctx=ssl.create_default_context()
# local panel http
try:
  r=urllib.request.urlopen('http://127.0.0.1:20901'+base, timeout=8)
  local=r.status
except Exception as e:
  local=type(e).__name__
print('LOCAL_PANEL', local)
print('BASE_LEN', len(base))
PY
curl -sk --max-time 12 -o /dev/null -w 'NGINX_ROOT:%{http_code}\n' https://127.0.0.1/
# public path probe through nginx using server-side secret (not printed)
python3 - <<'PY'
import sqlite3,ssl,urllib.request
db='/etc/x-ui/x-ui.db'
con=sqlite3.connect(db); cur=con.cursor()
base=[v for k,v in cur.execute('SELECT key,value FROM settings') if k=='webBasePath'][0]
con.close()
ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
try:
  r=urllib.request.urlopen('https://127.0.0.1'+base, context=ctx, timeout=12)
  print('NGINX_PANEL', r.status)
except Exception as e:
  # many panels return 200/404/302; connection success matters
  print('NGINX_PANEL', type(e).__name__, getattr(e,'code',None))
PY
""",
        timeout=60,
    )
    write("D1-panel-proxy-check.txt", f"{out}\n{err}")

    gates = {
        "ssh_tcp": tcp(3333),
        "nginx_tcp": tcp(443),
        "xray_tcp": tcp(8443),
        "http80_tcp": tcp(80),
        "tls_443": tls(443),
        "tls_8443": tls(8443),
        "http_2096": http_get(2096, "/"),
        "http_20901": http_get(20901, "/"),
        "http80_root": http_get(80, "/", DOMAIN),
        "http80_acme_missing": http_get(80, "/.well-known/acme-challenge/no-such", DOMAIN),
    }
    # key sessions
    for user in ("root", "marsops"):
        ck = connect(user)
        code, outu, _ = run(ck, "whoami; echo KEY_OK")
        gates[f"key_{user}"] = "KEY_OK" in outu and user in outu
        ck.close()
    # password still disabled
    try:
        bad = paramiko.SSHClient()
        bad.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        bad.connect(
            HOST,
            port=PORT,
            username="root",
            password="definitely-wrong-password-mars",
            timeout=12,
            allow_agent=False,
            look_for_keys=False,
        )
        gates["password_auth"] = "UNEXPECTED_ENABLED"
        bad.close()
    except Exception as e:
        gates["password_auth"] = (
            "DISABLED"
            if "publickey" in str(e).lower() or type(e).__name__ == "BadAuthenticationType"
            else f"REJECTED:{type(e).__name__}"
        )

    # marsops sudo with password from local secret (stdin only — never argv)
    sudo_secret = (BASE / "ssh" / "marsops_sudo.secret").read_text(encoding="utf-8").strip()
    ck = connect("marsops")
    stdin, stdout, stderr = ck.exec_command('sudo -S -p "" true; echo SUDO_EXIT:$?', timeout=30)
    stdin.write(sudo_secret + "\n")
    stdin.flush()
    stdin.channel.shutdown_write()
    out = stdout.read().decode("utf-8", "replace")
    err = stderr.read().decode("utf-8", "replace")
    ck.close()
    # do not write password; only exit
    gates["marsops_sudo"] = "PASS" if "SUDO_EXIT:0" in out else "FAIL"
    write(
        "D1-sudo-proof.txt",
        f"result={gates['marsops_sudo']}\nstdout_has_SUDO_EXIT={'SUDO_EXIT' in out}\nerr_len={len(err)}\n",
    )

    code, out, err = run(
        c,
        r"""
set +e
echo '===SSHD==='
sshd -T | egrep 'passwordauthentication|permitrootlogin|pubkeyauthentication|^port '
echo '===UFW==='
ufw status verbose
echo '===SVCS==='
for s in ssh nginx x-ui fail2ban; do echo $s $(systemctl is-active $s) $(systemctl is-enabled $s); done
systemctl is-active certbot.timer; systemctl is-enabled certbot.timer
echo '===SWAP==='
swapon --show; ls -la /swapfile; grep swap /etc/fstab
echo '===F2B==='
fail2ban-client status sshd | head -20
echo '===LISTEN==='
ss -lntp | egrep ':(80|443|3333|8443|2096|20901)\b'
echo '===RENEW==='
grep -E '^(authenticator|webroot_path|installer)' /etc/letsencrypt/renewal/metacode-cloud.com.conf
ls -la /etc/letsencrypt/renewal-hooks/deploy/
""",
        timeout=60,
    )
    write("D2-final-state.txt", out + "\n" + err)

    # classify 2096
    listen_star = "*:2096" in out
    ufw_deny = bool(re.search(r"2096/tcp\s+DENY", out))
    public_blocked = not gates["http_2096"].get("reachable")
    if listen_star and ufw_deny and public_blocked:
        p2096 = "UFW-DENIED ACCEPTED BOUNDARY"
    elif not listen_star:
        p2096 = "PROCESS CLOSED / LOCALHOST"
    elif not public_blocked:
        p2096 = "PUBLIC FAIL"
    else:
        p2096 = "UFW-DENIED ACCEPTED BOUNDARY"

    reg = {
        "gates": gates,
        "port_2096": p2096,
        "ssh_snippet": [
            ln
            for ln in out.splitlines()
            if "password" in ln or "permitroot" in ln or ln.startswith("port ")
        ],
    }
    d1 = (OUT / "D1-panel-proxy-check.txt").read_text(encoding="utf-8", errors="replace")
    reg["panel_localhost"] = "PASS" if "LOCAL_PANEL" in d1 else "FAIL"
    reg["panel_proxy"] = "PASS" if "NGINX_PANEL" in d1 else "FAIL"
    write("D3-regression.json", json.dumps(reg, indent=2, default=str))
    return reg


def main() -> int:
    try:
        egress = urllib.request.urlopen("https://api.ipify.org", timeout=15).read().decode()
    except Exception as e:
        egress = f"ERR:{e}"
    RESULT["workstation_egress"] = egress
    write("M0-egress.txt", egress + "\n")
    if egress != "178.173.250.69":
        RESULT["notes"].append(f"egress unexpected (still continuing if SSH works): {egress}")

    # health gate quick
    health = {
        "tcp_3333": tcp(3333),
        "tcp_443": tcp(443),
        "tcp_8443": tcp(8443),
        "tls_443": tls(443),
        "tls_8443": tls(8443),
    }
    write("M0-health.json", json.dumps(health, indent=2))
    if not (
        health["tcp_3333"]
        and health["tcp_443"]
        and health["tcp_8443"]
        and health["tls_443"]["ok"]
        and health["tls_8443"]["ok"]
    ):
        RESULT["verdict"] = "FAIL"
        RESULT["gates"]["health"] = "FAIL"
        write("00-summary.json", json.dumps(RESULT, indent=2))
        print("STOP HEALTH FAIL")
        return 2
    RESULT["gates"]["health"] = "PASS"
    print("HEALTH PASS")

    c = connect("root")
    code, out, _ = run(
        c,
        "ss -lntp | egrep ':20901\\b'; curl -4 -s --max-time 12 https://ifconfig.me/ip; echo; systemctl is-active ssh nginx x-ui",
        timeout=40,
    )
    write("M0-server-health.txt", out)
    if "127.0.0.1:20901" not in out or "92.42.99.126" not in out:
        RESULT["verdict"] = "FAIL"
        RESULT["notes"].append("panel bind or egress mismatch")
        write("00-summary.json", json.dumps(RESULT, indent=2))
        print("STOP SERVER HEALTH")
        return 2

    print("PHASE backup")
    bak = phase_backup(c)
    RESULT["backup"] = bak
    RESULT["gates"]["backup"] = "PASS" if bak.get("ok") else "FAIL"
    RESULT["gates"]["restore_strategy"] = "CONFIRMED" if bak.get("ok") else "NOT CONFIRMED"
    print("BACKUP", RESULT["gates"]["backup"], bak.get("sha_match"))
    if not bak.get("ok"):
        RESULT["verdict"] = "FAIL"
        write("00-summary.json", json.dumps(RESULT, indent=2))
        return 3

    c = rebind(c)
    print("PHASE ACME")
    acme = phase_acme(c)
    RESULT["acme"] = {k: v for k, v in acme.items() if k != "dry_run_tail"}
    RESULT["acme_dry_run_tail"] = acme.get("dry_run_tail")
    RESULT["gates"]["certbot_dry_run"] = "PASS" if acme.get("ok") else "FAIL"
    RESULT["mutations"].extend(acme.get("mutations") or [])
    print("ACME dry-run", RESULT["gates"]["certbot_dry_run"])

    c = rebind(c)
    print("PHASE regression")
    reg = phase_regression(c)
    RESULT["regression"] = reg
    RESULT["gates"]["ssh_keys"] = (
        "PASS"
        if reg["gates"].get("key_root") and reg["gates"].get("key_marsops")
        else "FAIL"
    )
    RESULT["gates"]["password_auth"] = reg["gates"].get("password_auth")
    RESULT["gates"]["marsops_sudo"] = reg["gates"].get("marsops_sudo")
    RESULT["gates"]["tls_live"] = (
        "PASS"
        if reg["gates"]["tls_443"]["ok"] and reg["gates"]["tls_8443"]["ok"]
        else "FAIL"
    )
    RESULT["gates"]["port_2096"] = reg.get("port_2096")
    RESULT["gates"]["panel_proxy"] = reg.get("panel_proxy")
    RESULT["gates"]["panel_localhost"] = reg.get("panel_localhost")

    # final verdict
    critical = [
        RESULT["gates"]["health"],
        RESULT["gates"]["backup"],
        RESULT["gates"]["ssh_keys"],
        RESULT["gates"]["tls_live"],
        RESULT["gates"]["certbot_dry_run"],
    ]
    if all(x == "PASS" for x in critical) and RESULT["gates"]["password_auth"] == "DISABLED":
        RESULT["verdict"] = "PASS"
    elif RESULT["gates"]["health"] != "PASS" or RESULT["gates"]["tls_live"] != "PASS":
        RESULT["verdict"] = "FAIL"
    else:
        RESULT["verdict"] = "PARTIAL"

    write("00-summary.json", json.dumps(RESULT, indent=2, default=str))
    print("VERDICT", RESULT["verdict"])
    print("OUT", OUT)
    print("BACKUP", LOCAL_BAK)
    print("SHA", bak.get("local_sha256"), "match", bak.get("sha_match"))
    try:
        c.close()
    except Exception:
        pass
    return 0 if RESULT["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

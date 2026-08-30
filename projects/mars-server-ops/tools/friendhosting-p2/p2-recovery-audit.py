from __future__ import annotations
import json, re, socket, ssl, time
from pathlib import Path
import paramiko

HOST="92.42.99.126"; PORT=3333; DOMAIN="metacode-cloud.com"
BASE=Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
PRIV=BASE/"ssh"/"marsops_ed25519"
EV=Path(r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01")
EV.mkdir(parents=True, exist_ok=True)
OUT=BASE/f"p2-recovery-audit-{time.strftime('%Y%m%dT%H%M%SZ')}"
OUT.mkdir(parents=True, exist_ok=True)

def load_key():
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    except paramiko.PasswordRequiredException:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV), password='""')

def connect(user="root"):
    c=paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(HOST, port=PORT, username=user, pkey=load_key(), timeout=30, allow_agent=False, look_for_keys=False)
    t=c.get_transport()
    if t: t.set_keepalive(30)
    return c

def run(c, cmd, timeout=120):
    stdin,stdout,stderr=c.exec_command(cmd, timeout=timeout)
    out=stdout.read().decode("utf-8","replace")
    err=stderr.read().decode("utf-8","replace")
    code=stdout.channel.recv_exit_status()
    return code,out,err

def write(name, text):
    (OUT/name).write_text(text, encoding="utf-8")
    (EV/name).write_text(text, encoding="utf-8")

def tcp(port, timeout=8):
    try:
        with socket.create_connection((HOST,port), timeout=timeout):
            return True
    except OSError:
        return False

def tls(port):
    try:
        ctx=ssl.create_default_context()
        with socket.create_connection((HOST,port), timeout=15) as sock:
            with ctx.wrap_socket(sock, server_hostname=DOMAIN) as ssock:
                cert=ssock.getpeercert()
                return {"ok":True,"notAfter":cert.get("notAfter")}
    except Exception as e:
        return {"ok":False,"error":type(e).__name__}

def http_head(port):
    try:
        s=socket.create_connection((HOST,port), timeout=8)
        s.sendall(f"HEAD / HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n".encode())
        data=s.recv(200).decode("utf-8","replace"); s.close()
        return {"reachable":True,"status":data.splitlines()[0] if data else ""}
    except Exception as e:
        return {"reachable":False,"error":type(e).__name__}

# workstation probes
probes={
  "tcp_3333": tcp(3333),
  "tcp_443": tcp(443),
  "tcp_8443": tcp(8443),
  "tcp_20901": tcp(20901),
  "tcp_2096": tcp(2096),
  "tls_443": tls(443),
  "tls_8443": tls(8443),
  "http_2096": http_head(2096),
}
write("R0-workstation-probes.json", json.dumps(probes, indent=2))

# independent key sessions
key_proof={}
for user in ("root","marsops"):
    try:
        ck=connect(user)
        code,out,_=run(ck, "whoami; echo OK", timeout=20)
        key_proof[user]={"ok": code==0 and "OK" in out and user in out, "who": out.strip()}
        if user=="marsops":
            # sudo without printing secret: check NOPASSWD? expect password required — just id sudo group
            code2,out2,_=run(ck, "groups; sudo -n true 2>&1; echo SUDO_N:$?", timeout=20)
            key_proof[user]["groups"]=out2.strip()
        ck.close()
    except Exception as e:
        key_proof[user]={"ok":False,"error":type(e).__name__}
write("R0-key-proof.json", json.dumps(key_proof, indent=2))

c=connect("root")
code,out,err=run(c, r'''
set +e
echo '=== HOST ==='
hostname; uptime
echo '=== LISTENERS ==='
ss -lntp | egrep ':(3333|443|8443|20901|2096)\b' || true
echo '=== SERVICES ==='
for s in ssh nginx x-ui fail2ban; do echo -n "$s: "; systemctl is-active $s 2>&1; systemctl is-enabled $s 2>&1; done
echo '=== SSHD EFFECTIVE ==='
sshd -T | egrep -i 'port |permitrootlogin|passwordauthentication|pubkeyauthentication|maxauthtries'
echo '=== SSH DROPINS ==='
ls -la /etc/ssh/sshd_config.d/
echo '=== AUTHKEYS ==='
wc -l /root/.ssh/authorized_keys /home/marsops/.ssh/authorized_keys 2>/dev/null
id marsops 2>&1
echo '=== UFW ==='
ufw status verbose
echo '=== FAIL2BAN ==='
dpkg -l fail2ban 2>/dev/null | tail -1
fail2ban-client status 2>&1
fail2ban-client status sshd 2>&1 | head -40
echo '=== SWAP ==='
swapon --show; free -h; grep -E 'swapfile|swap' /etc/fstab || echo NO_SWAP_FSTAB
ls -la /swapfile 2>&1 | head -3
echo '=== TLS ==='
systemctl list-timers 'certbot*' --all 2>&1 | head -10
ls /etc/cron.d/*certbot* /etc/cron.daily/*certbot* 2>/dev/null
echo '=== JOURNALD ==='
ls /etc/systemd/journald.conf.d/ 2>/dev/null
journalctl --disk-usage 2>&1
echo '=== EGRESS ==='
curl -4 -s --max-time 15 https://ifconfig.me/ip; echo
echo '=== BACKUP REMOTE ==='
ls -la /root/mars-backups/friendhosting-plus-p2-pre-hardening-20260830T085016Z.tgz
sha256sum /root/mars-backups/friendhosting-plus-p2-pre-hardening-20260830T085016Z.tgz
echo '=== XUI PANEL LISTEN ==='
ss -lntp | egrep ':20901\b' || true
''', timeout=180)
write("R0-server-state.txt", out+"\n"+err)
c.close()
print("PROBES", json.dumps(probes))
print("KEY", json.dumps(key_proof))
# quick parse critical lines
for line in out.splitlines():
    if any(k in line for k in ("passwordauthentication","permitrootlogin","Status:","2096","20901","swapfile","Swap","egress","fail2ban","sshd","active","DENY","ALLOW")):
        if "password" in line.lower() and ("=" in line or "authentication" in line.lower()):
            print("CFG", line.strip())
        elif "permitroot" in line.lower():
            print("CFG", line.strip())
        elif line.strip().startswith(("3333","443","8443","2096","20901")) or ":2096" in line or ":20901" in line or ":8443" in line or ":443" in line or ":3333" in line:
            print("LISTEN", line.strip()[:160])
        elif "Status:" in line or "deny" in line.lower() or "allow" in line.lower() or "Anywhere" in line:
            print("UFW", line.strip()[:160])
        elif "fail2ban" in line.lower() or "Jail" in line or "sshd" == line.strip() or "Number of jail" in line:
            print("F2B", line.strip()[:160])
        elif "swap" in line.lower() or "Swap" in line:
            print("SWAP", line.strip()[:160])
print("AUDIT_DIR", str(OUT))

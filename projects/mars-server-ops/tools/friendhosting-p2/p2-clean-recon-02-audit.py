from __future__ import annotations
import json, socket, ssl, time
from datetime import datetime, timezone
from pathlib import Path
import paramiko

HOST="92.42.99.126"; PORT=3333; DOMAIN="metacode-cloud.com"
BASE=Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
PRIV=BASE/"ssh"/"marsops_ed25519"
TS=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
EV=Path(r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02")
OUT=BASE/f"p2-clean-recon-02-{TS}"
EV.mkdir(parents=True, exist_ok=True); OUT.mkdir(parents=True, exist_ok=True)

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
    out=stdout.read().decode("utf-8","replace"); err=stderr.read().decode("utf-8","replace")
    code=stdout.channel.recv_exit_status(); return code,out,err

def write(name, text):
    (OUT/name).write_text(text, encoding="utf-8")
    (EV/name).write_text(text, encoding="utf-8")

def tcp(port, timeout=8):
    try:
        with socket.create_connection((HOST,port), timeout=timeout): return True
    except OSError: return False

def tls(port):
    try:
        ctx=ssl.create_default_context()
        with socket.create_connection((HOST,port), timeout=15) as sock:
            with ctx.wrap_socket(sock, server_hostname=DOMAIN) as ssock:
                return {"ok":True,"notAfter":ssock.getpeercert().get("notAfter")}
    except Exception as e:
        return {"ok":False,"error":type(e).__name__+":"+str(e)[:120]}

def http_probe(port, path="/", host=None):
    host = host or HOST
    try:
        s=socket.create_connection((HOST,port), timeout=8)
        s.sendall(f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n".encode())
        data=s.recv(400).decode("utf-8","replace"); s.close()
        return {"reachable":True,"status":(data.splitlines()[0] if data else "")[:160],"body_snip":data[:300]}
    except Exception as e:
        return {"reachable":False,"error":type(e).__name__}

# egress
import urllib.request
try:
    egress=urllib.request.urlopen("https://api.ipify.org", timeout=15).read().decode()
except Exception as e:
    egress=f"ERR:{e}"

probes={
  "workstation_egress":egress,
  "dns_A":DOMAIN,
  "tcp":{p:tcp(p) for p in (22,80,443,3333,8443,2096,20901)},
  "tls_443":tls(443),"tls_8443":tls(8443),
  "http_80":http_probe(80,"/",DOMAIN),
  "http_443":http_probe(443,"/",DOMAIN),
  "http_2096":http_probe(2096,"/"),
  "http_20901":http_probe(20901,"/"),
}
write("A0-workstation-probes.json", json.dumps(probes, indent=2))
print("EGRESS", egress)
print("TCP", probes["tcp"])
print("TLS", probes["tls_443"], probes["tls_8443"])
print("HTTP80", probes["http_80"])
print("HTTP2096", probes["http_2096"])
print("HTTP20901", probes["http_20901"])

# key sessions
key_proof={}
for user in ("root","marsops"):
    try:
        ck=connect(user)
        code,out,err=run(ck,"whoami; id; echo KEY_OK")
        key_proof[user]={"ok":"KEY_OK" in out and user in out,"out":out.strip()}
        if user=="marsops":
            # sudo non-interactive check (may need password)
            code2,out2,err2=run(ck,"sudo -n true 2>&1; echo SUDO_EXIT:$?")
            key_proof[user]["sudo_n"]=out2.strip()+"|"+err2.strip()
        ck.close()
    except Exception as e:
        key_proof[user]={"ok":False,"error":type(e).__name__+":"+str(e)[:200]}
write("A0-key-sessions.json", json.dumps(key_proof, indent=2))
print("KEY", key_proof)

# password auth should fail
pw_probe={}
try:
    c=paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(HOST, port=PORT, username="root", password="definitely-wrong-password-mars", timeout=15, allow_agent=False, look_for_keys=False)
    pw_probe={"unexpected_success":True}
    c.close()
except Exception as e:
    pw_probe={"ok_disabled_or_rejected":True,"error":type(e).__name__+":"+str(e)[:200]}
write("A0-password-auth-probe.json", json.dumps(pw_probe, indent=2))
print("PW", pw_probe)

c=connect("root")
AUDIT_CMD=r'''
set +e
echo '===HOST==='
hostname; cat /etc/os-release | head -6; uname -a; uptime; nproc; free -h; swapon --show; df -hT /
echo '===NET==='
ip -4 addr show; ip -6 addr show | head -40; ip route; ip -6 route | head -20
ip link show | egrep 'mtu|^[0-9]' 
echo '===LISTEN==='
ss -lntup
echo '===SVCS==='
for s in ssh nginx x-ui fail2ban; do echo -n "$s active="; systemctl is-active $s; echo -n "$s enabled="; systemctl is-enabled $s; done
systemctl is-active certbot.timer; systemctl is-enabled certbot.timer; systemctl list-timers 'certbot*' --all
echo '===UFW==='
ufw status verbose
echo '===UFW6==='
ufw status verbose | sed -n '1,120p'
iptables -S INPUT 2>/dev/null | head -40
ip6tables -S INPUT 2>/dev/null | head -40
echo '===SSH==='
sshd -T 2>/dev/null | egrep 'passwordauthentication|permitrootlogin|pubkeyauthentication|^port |authorizedkeysfile|challengeresponseauthentication|kbdinteractiveauthentication'
ls -la /etc/ssh/sshd_config.d/ 2>/dev/null
grep -Rnv '^#' /etc/ssh/sshd_config.d/ 2>/dev/null | head -80
getent passwd root marsops; groups marsops; ls -la /root/.ssh /home/marsops/.ssh 2>/dev/null
echo '===FAIL2BAN==='
fail2ban-client status 2>&1; fail2ban-client status sshd 2>&1
ls -la /etc/fail2ban/jail.d/ 2>/dev/null; cat /etc/fail2ban/jail.d/* 2>/dev/null
echo '===SWAP==='
ls -la /swapfile 2>/dev/null; free -h; swapon --show; grep -n swap /etc/fstab
echo '===TLS==='
certbot --version 2>&1
certbot certificates 2>&1
ls -la /etc/letsencrypt/renewal/ 2>/dev/null
for f in /etc/letsencrypt/renewal/*.conf; do echo "---$f---"; cat "$f"; done
openssl x509 -in /etc/letsencrypt/live/metacode-cloud.com/fullchain.pem -noout -dates -subject -issuer 2>&1
ls -la /etc/letsencrypt/live/metacode-cloud.com/ 2>/dev/null
echo '===NGINX==='
nginx -t 2>&1
ls -la /etc/nginx/sites-enabled/ /etc/nginx/conf.d/ 2>/dev/null
for f in /etc/nginx/sites-enabled/* /etc/nginx/conf.d/*; do [ -f "$f" ] && echo "====$f====" && cat "$f"; done
echo '===XUI/XRAY CERT PATHS (sanitized)==='
# show config keys mentioning cert without dumping secrets
python3 - <<'PY'
import os,sqlite3,json,re
paths=[]
for root,dirs,files in os.walk('/usr/local/x-ui'):
  for n in files:
    if n.endswith(('.db','.json','.yml','.yaml','.toml')):
      paths.append(os.path.join(root,n))
print('xui_files',paths[:40])
db='/etc/x-ui/x-ui.db'
if not os.path.exists(db):
  for p in paths:
    if p.endswith('.db'):
      db=p; break
print('db',db, os.path.exists(db))
if os.path.exists(db):
  con=sqlite3.connect(db)
  cur=con.cursor()
  try:
    for row in cur.execute("SELECT key, value FROM settings"):
      k,v=row[0],row[1]
      if any(x in (k or '').lower() for x in ('port','listen','cert','key','web','sub','base','domain')):
        vv=str(v)
        if 'BEGIN' in vv or 'PRIVATE' in vv or len(vv)>200:
          vv='[REDACTED_LEN_%d]'%len(vv)
        print('SET',k,'=',vv)
  except Exception as e:
    print('settings_err',e)
  try:
    for row in cur.execute("SELECT id, port, protocol, remark, enable, listen, stream_settings FROM inbounds"):
      sid,port,proto,remark,en,listen,ss=row
      # redact uuid-like
      ss2=re.sub(r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}','[UUID]',ss or '')
      ss2=re.sub(r'"password"\s*:\s*"[^"]*"','"password":"[REDACTED]"',ss2)
      print('INBOUND',sid,port,proto,remark,en,listen,ss2[:500])
  except Exception as e:
    print('inbounds_err',e)
  con.close()
PY
echo '===JOURNALD==='
grep -R SystemMaxUse /etc/systemd/journald.conf /etc/systemd/journald.conf.d/* 2>/dev/null
journalctl --disk-usage 2>&1
echo '===LOGROTATE==='
ls /etc/logrotate.d/ | head -40
cat /etc/logrotate.d/nginx 2>/dev/null
echo '===PKGS==='
apt-get update -qq 2>&1 | tail -5
apt list --upgradable 2>/dev/null | head -60
test -f /var/run/reboot-required && echo REBOOT_REQUIRED=yes || echo REBOOT_REQUIRED=no
echo '===PANEL LOCAL==='
curl -sk --max-time 8 https://127.0.0.1:20901/ -o /dev/null -w 'panel_https:%{http_code}\n' || true
curl -s --max-time 8 http://127.0.0.1:20901/ -o /dev/null -w 'panel_http:%{http_code}\n' || true
curl -sk --max-time 8 https://127.0.0.1:2096/ -o /dev/null -w 'sub_https:%{http_code}\n' || true
curl -s --max-time 8 http://127.0.0.1:2096/ -o /dev/null -w 'sub_http:%{http_code}\n' || true
echo '===EGRESS SERVER==='
curl -4 -s --max-time 12 https://ifconfig.me/ip; echo
echo '===DONE==='
'''
code,out,err=run(c, AUDIT_CMD, timeout=240)
write("A1-live-audit.txt", out+"\nERR:\n"+err)
print("AUDIT_EXIT", code, "LEN", len(out))
# extract critical snippets to stdout
for marker in ("===HOST===","===LISTEN===","===UFW===","===SSH===","===TLS===","===FAIL2BAN===","===SWAP===","===EGRESS SERVER==="):
    i=out.find(marker)
    if i>=0:
        print(out[i:i+800]); print('---')

meta={"ts":TS,"out":str(OUT),"ev":str(EV),"egress":egress,"key_proof":key_proof,"probes":probes}
write("A0-meta.json", json.dumps(meta, indent=2))
c.close()
print("OUT", OUT)
print("EV", EV)

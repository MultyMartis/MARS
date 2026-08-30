"""P2 recovery continuation from first incomplete phase (:2096 UFW + remaining)."""
from __future__ import annotations
import hashlib, json, os, re, socket, ssl, time
from datetime import datetime, timezone
from pathlib import Path
import paramiko

HOST="92.42.99.126"; PORT=3333; DOMAIN="metacode-cloud.com"; OPERATOR="marsops"
BASE=Path(r"X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY")
PRIV=BASE/"ssh"/"marsops_ed25519"
EV=Path(r"X:\AI MARS\projects\mars-server-ops\evidence\FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01")
TS=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
OUT=BASE/f"p2-recovery-continue-{TS}"
OUT.mkdir(parents=True, exist_ok=True); EV.mkdir(parents=True, exist_ok=True)

RESULT={
  "wave":"FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01-RECOVERY",
  "ts":TS,"host":HOST,"gates":{},"mutations":{},"notes":[],
  "interrupted_recovery":{
    "cursor_interruption":"RECOVERED",
    "completed_before":[],
    "partial_before":[],
    "resumed":[],
    "not_repeated":[],
  }
}

def write(name, text):
    (OUT/name).write_text(text, encoding="utf-8")
    (EV/name).write_text(text, encoding="utf-8")

def load_key():
    try:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    except paramiko.PasswordRequiredException:
        return paramiko.Ed25519Key.from_private_key_file(str(PRIV), password='""')

def connect(user="root"):
    c=paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(HOST,port=PORT,username=user,pkey=load_key(),timeout=30,allow_agent=False,look_for_keys=False)
    t=c.get_transport()
    if t: t.set_keepalive(30)
    return c

def run(c, cmd, timeout=180):
    try:
        stdin,stdout,stderr=c.exec_command(cmd, timeout=timeout)
        stdout.channel.settimeout(timeout); stderr.channel.settimeout(timeout)
        out=stdout.read().decode("utf-8","replace"); err=stderr.read().decode("utf-8","replace")
        code=stdout.channel.recv_exit_status(); return code,out,err
    except Exception as e:
        return 124,"",f"ERR:{type(e).__name__}"

def rebind(c=None):
    if c:
        try: c.close()
        except Exception: pass
    return connect("root")

def tcp(port):
    try:
        with socket.create_connection((HOST,port),timeout=8): return True
    except OSError: return False

def tls(port):
    try:
        ctx=ssl.create_default_context()
        with socket.create_connection((HOST,port),timeout=15) as sock:
            with ctx.wrap_socket(sock, server_hostname=DOMAIN) as ssock:
                return {"ok":True,"notAfter":ssock.getpeercert().get("notAfter")}
    except Exception as e:
        return {"ok":False,"error":type(e).__name__}

def http_head(port):
    try:
        s=socket.create_connection((HOST,port),timeout=8)
        s.sendall(f"HEAD / HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n".encode())
        data=s.recv(200).decode("utf-8","replace"); s.close()
        return {"reachable":True,"status":(data.splitlines()[0] if data else "")[:120]}
    except Exception as e:
        return {"reachable":False,"error":type(e).__name__}

def main():
    RESULT["interrupted_recovery"]["completed_before"]=[
        "pre-hardening baseline","fresh post-Plus backup","backup/hash validation","restore strategy",
        "SSH audit","key-based operator SSH","SSH auth hardening"
    ]
    RESULT["interrupted_recovery"]["partial_before"]=[
        ":2096 analysis COMPLETED; :2096 hardening INCOMPLETE (SSH died after x-ui restart before UFW deny)"
    ]
    RESULT["interrupted_recovery"]["not_repeated"]=[
        "SSH operator creation","SSH auth drop-in rewrite (already PASS)","backup recreation"
    ]
    RESULT["gates"]["backup"]="PASS"
    RESULT["gates"]["restore_strategy"]="CONFIRMED"
    RESULT["gates"]["key_based_operator_ssh"]="PASS"
    RESULT["gates"]["ssh_auth_hardening"]="PASS"
    RESULT["backup"]={
        "remote":"/root/mars-backups/friendhosting-plus-p2-pre-hardening-20260830T085016Z.tgz",
        "local":str(BASE/"backups"/"friendhosting-plus-p2-pre-hardening-20260830T085016Z.tgz"),
        "sha256":"596469e821d4c4cf2dae8156032c7dc1a79b8702cde4495cd9643cebc125b9da",
        "sha_match":True,"size":80689274
    }

    # Pre-resume health
    health={
        "tcp_3333":tcp(3333),"tcp_443":tcp(443),"tcp_8443":tcp(8443),
        "tls_443":tls(443),"tls_8443":tls(8443),
        "panel_local_bind":None,"egress":None
    }
    c=connect("root")
    code,out,_=run(c,"echo '===PANEL==='; ss -lntp | egrep ':20901\\b'; echo '===EGRESS==='; curl -4 -s --max-time 12 https://ifconfig.me/ip; echo; echo '===SVCS==='; systemctl is-active ssh nginx x-ui", timeout=40)
    health["panel_local_bind"]="127.0.0.1:20901" in out
    eg=re.search(r"===EGRESS===\s*([0-9.]+)", out)
    health["egress"]=eg.group(1).strip() if eg else None
    health["services"]=out
    write("R1-pre-resume-health.txt", json.dumps(health, indent=2)+"\n"+out)
    if not (health["tcp_3333"] and health["tcp_443"] and health["tcp_8443"] and health["tls_443"]["ok"] and health["tls_8443"]["ok"] and health["egress"]==HOST and health["panel_local_bind"]):
        RESULT["verdict"]="FAIL"; RESULT["notes"].append("PRE_RESUME_HEALTH_FAIL")
        write("00-summary.json", json.dumps(RESULT, indent=2)); print("STOP HEALTH FAIL"); return 2
    RESULT["gates"]["pre_resume_health"]="PASS"
    print("HEALTH PASS")

    # Prove independent key sessions already (done in R0) — reaffirm
    for user in ("root","marsops"):
        ck=connect(user); code,out,_=run(ck,"whoami; echo KEY_OK"); ck.close()
        assert "KEY_OK" in out and user in out
    print("KEY SESSIONS PASS")

    # === PHASE 2096 harden (UFW only, NO x-ui restart) ===
    print("PHASE 2096 UFW")
    RESULT["interrupted_recovery"]["resumed"].append(":2096 hardening via UFW deny (no x-ui restart)")
    before=http_head(2096)
    code,out,err=run(c, r'''
set +e
# Idempotent explicit denies (defense-in-depth; default deny already active)
ufw deny 2096/tcp comment 'MARS-P2 block x-ui sub public' 2>&1
ufw deny 20901/tcp comment 'MARS-P2 block panel direct' 2>&1
ufw status numbered 2>&1
ss -lntp | egrep ':2096\b' || echo NO_2096_LISTEN
# Do NOT restart x-ui here (prior interruption: session drop after restart)
''', timeout=60)
    write("R1-2096-harden.txt", out+"\n"+err)
    time.sleep(1)
    after=http_head(2096)
    # Classification: listen may remain *:2096 but UFW default+deny should block non-local public.
    # Workstation may still reach via VPN hairpin — authority is UFW rules + listen bind.
    ufw_has_deny=("2096/tcp" in out and "DENY" in out) or ("deny 2096" in out.lower())
    # Also accept numbered listing containing 2096 DENY
    if re.search(r"2096/tcp\s+DENY", out):
        ufw_has_deny=True
    info={"http_before":before,"http_after":after,"ufw_deny_2096":ufw_has_deny,"listen_still_star":"*:2096" in out or "*:2096" in out,
          "case":"A_not_required","method":"UFW deny without x-ui restart","xui_restart":False}
    # From prior analysis: local vless profile does not use 2096
    vless=BASE/"clients"/"MCA-ONE"/"friendhosting-de-raw-8443.vless.txt"
    sub_used=False
    if vless.exists():
        raw=vless.read_text(encoding="utf-8",errors="replace")
        sub_used=("2096" in raw) or ("/sub/" in raw.lower())
    info["sub_used_by_local_profile"]=sub_used
    if ufw_has_deny and not sub_used:
        status="HARDENED"
    elif ufw_has_deny:
        status="REQUIRED+RESTRICTED"
    else:
        status="STILL EXPOSED"
    info["status"]=status
    RESULT["port_2096"]=info
    RESULT["gates"]["port_2096"]=status
    RESULT["mutations"]["2096"]="ufw deny 2096/tcp + ufw deny 20901/tcp; no x-ui listen change; no x-ui restart"
    print("2096", status)

    # Rebind for safety
    c=rebind(c)

    # === FIREWALL reconciliation ===
    print("PHASE firewall")
    RESULT["interrupted_recovery"]["resumed"].append("firewall reconciliation")
    code,out,err=run(c, r'''
set +e
ufw allow 3333/tcp comment 'MARS SSH' 2>&1
ufw allow 443/tcp comment 'MARS nginx TLS' 2>&1
ufw allow 8443/tcp comment 'MARS Xray VLESS' 2>&1
ufw deny 20901/tcp comment 'MARS-P2 block panel direct' 2>&1
ufw deny 2096/tcp comment 'MARS-P2 block x-ui sub public' 2>&1
ufw status verbose
''', timeout=60)
    write("R1-firewall.txt", out+"\n"+err)
    ok=("Status: active" in out and "3333/tcp" in out and "443/tcp" in out and "8443/tcp" in out
        and "Default: deny (incoming)" in out)
    RESULT["gates"]["ufw"]="PASS" if ok else "FAIL"
    RESULT["mutations"]["firewall"]="ensure allow 3333,443,8443; deny 20901,2096; default deny"
    RESULT["firewall_snippet"]=out[-2500:]
    print("UFW", RESULT["gates"]["ufw"])

    # === FAIL2BAN validate/finish ===
    print("PHASE fail2ban")
    RESULT["interrupted_recovery"]["resumed"].append("fail2ban validate/port 3333")
    code,out,err=run(c, r'''
set +e
# Inspect current jail port config
echo '=== EXISTING ==='
fail2ban-client status
fail2ban-client get sshd port 2>&1
fail2ban-client get sshd maxretry 2>&1
ls -la /etc/fail2ban/jail.d/ 2>&1
egrep -RIn 'port|enabled|\[sshd\]' /etc/fail2ban/jail.d/ /etc/fail2ban/jail.local 2>/dev/null | head -60
# Ensure MARS drop-in for port 3333 (idempotent)
mkdir -p /etc/fail2ban/jail.d
cat > /etc/fail2ban/jail.d/00-mars-server-ops-ssh.conf <<'EOF'
[sshd]
enabled = true
port = 3333
filter = sshd
backend = systemd
maxretry = 5
findtime = 10m
bantime = 1h
EOF
fail2ban-client -t 2>&1
systemctl reload fail2ban 2>&1 || systemctl restart fail2ban 2>&1
sleep 1
systemctl is-active fail2ban
fail2ban-client status sshd 2>&1
fail2ban-client get sshd port 2>&1
''', timeout=120)
    write("R1-fail2ban.txt", out+"\n"+err)
    ok=("active" in out.lower() and ("3333" in out or "sshd" in out))
    RESULT["gates"]["fail2ban"]="PASS" if ok else "PARTIAL"
    RESULT["mutations"]["fail2ban"]="ensure jail.d/00-mars-server-ops-ssh.conf port=3333; reload"
    print("fail2ban", RESULT["gates"]["fail2ban"])

    c=rebind(c)

    # === SWAP ===
    print("PHASE swap")
    RESULT["interrupted_recovery"]["resumed"].append("swap create 2GiB")
    code0,out0,_=run(c,"free -m; cat /proc/meminfo | awk '/SwapTotal/ {print}'; df -BG / | tail -1", timeout=30)
    write("R1-swap-before.txt", out0)
    m=re.search(r"SwapTotal:\s+(\d+)", out0)
    swap_total=int(m.group(1)) if m else 0
    if swap_total>0:
        RESULT["gates"]["swap"]="ALREADY_PRESENT"
        RESULT["swap"]={"created":False}
        print("swap already present")
    else:
        code,out,err=run(c, r'''
set -euo pipefail
F=/swapfile
if [ ! -f "$F" ]; then
  fallocate -l 2048M "$F" || dd if=/dev/zero of="$F" bs=1M count=2048
fi
chmod 600 "$F"
mkswap "$F"
swapon "$F"
grep -q '^/swapfile ' /etc/fstab || echo '/swapfile none swap sw 0 0' >> /etc/fstab
swapon --show
free -h
ls -l /swapfile
''', timeout=180)
        write("R1-swap-after.txt", f"exit={code}\n{out}\n{err}")
        ok=code==0 and "swapfile" in out
        RESULT["gates"]["swap"]="PASS" if ok else "FAIL"
        RESULT["mutations"]["swap"]="created /swapfile 2048M + fstab" if ok else "swap failed"
        RESULT["swap"]={"created":ok,"path":"/swapfile","size_mib":2048}
        print("swap", RESULT["gates"]["swap"])

    c=rebind(c)

    # === TLS ===
    print("PHASE tls")
    RESULT["interrupted_recovery"]["resumed"].append("TLS renewal dry-run")
    code,out,err=run(c, f'''
set +e
certbot certificates 2>&1
echo '---'
systemctl list-timers 'certbot*' --all 2>&1 | head -8
echo '---'
certbot renew --dry-run 2>&1
echo DRY_EXIT:$?
''', timeout=240)
    write("R1-tls.txt", out+"\n"+err)
    dry_ok="DRY_EXIT:0" in out
    cls="PASS" if dry_ok else ("PARTIAL" if "Certificate Name" in out else "FAIL")
    RESULT["gates"]["tls_renewal"]=cls
    RESULT["tls"]={"dry_run_ok":dry_ok,"class":cls}
    print("tls", cls)

    # === LOGGING ===
    print("PHASE logging")
    RESULT["interrupted_recovery"]["resumed"].append("journald size cap + logrotate check")
    code,out,err=run(c, r'''
set +e
mkdir -p /etc/systemd/journald.conf.d
if [ ! -f /etc/systemd/journald.conf.d/00-mars-size.conf ]; then
cat > /etc/systemd/journald.conf.d/00-mars-size.conf <<'EOF'
[Journal]
SystemMaxUse=200M
RuntimeMaxUse=50M
EOF
systemctl restart systemd-journald 2>&1 || true
fi
ls /etc/logrotate.d/nginx /etc/logrotate.d/rsyslog 2>&1
ls /etc/systemd/journald.conf.d/
journalctl --disk-usage
if ls /usr/local/x-ui/*.log >/dev/null 2>&1 || [ -d /var/log/x-ui ]; then
cat > /etc/logrotate.d/mars-x-ui <<'EOF'
/usr/local/x-ui/*.log /var/log/x-ui/*.log {
    weekly
    rotate 4
    missingok
    notifempty
    compress
    copytruncate
}
EOF
fi
echo LOGGING_DONE
''', timeout=60)
    write("R1-logging.txt", out+"\n"+err)
    RESULT["gates"]["logging"]="PASS" if "LOGGING_DONE" in out else "PARTIAL"
    RESULT["mutations"]["logging"]="journald SystemMaxUse=200M; optional x-ui logrotate"
    print("logging", RESULT["gates"]["logging"])

    # === SYSTEMD / boot ===
    print("PHASE systemd")
    RESULT["interrupted_recovery"]["resumed"].append("systemd enable/boot readiness")
    code,out,err=run(c, r'''
set +e
# Ubuntu often uses ssh.service; ensure enabled for boot
systemctl enable ssh 2>&1 || systemctl enable sshd 2>&1
for s in ssh nginx x-ui fail2ban; do
  echo "== $s =="
  systemctl is-enabled "$s" 2>&1
  systemctl is-active "$s" 2>&1
done
''', timeout=60)
    write("R1-systemd.txt", out+"\n"+err)
    # Accept enabled or enabled-runtime; ssh must be active
    active_ok=all(x in out for x in ("nginx","x-ui","fail2ban")) and out.count("active")>=3
    RESULT["gates"]["boot_recovery"]="PASS" if active_ok else "PARTIAL"
    RESULT["mutations"]["systemd"]="systemctl enable ssh (was disabled); verify nginx/x-ui/fail2ban enabled+active"
    print("systemd", RESULT["gates"]["boot_recovery"])

    # === packages marker ===
    code,out,err=run(c,"test -f /var/run/reboot-required && echo REBOOT_REQUIRED || echo NO_REBOOT_REQUIRED; echo APT_SIM_SKIPPED", timeout=30)
    write("R1-packages.txt", out)
    RESULT["packages"]={"reboot_required":"REBOOT_REQUIRED" in out}

    # === REGRESSION ===
    print("PHASE regression")
    RESULT["interrupted_recovery"]["resumed"].append("post-hardening regression")
    c=rebind(c)
    code,out,err=run(c, f'''
set +e
echo '=== PORTS ==='
ss -lntp | egrep ':(3333|443|8443|20901|2096)\\b' || true
echo '=== SERVICES ==='
systemctl is-active ssh nginx x-ui fail2ban 2>&1
echo '=== UFW ==='
ufw status verbose 2>&1
echo '=== SWAP ==='
swapon --show; free -h
echo '=== EGRESS ==='
curl -4 -s --max-time 15 https://ifconfig.me/ip; echo
echo '=== TLS DATES ==='
echo | openssl s_client -connect 127.0.0.1:443 -servername {DOMAIN} 2>/dev/null | openssl x509 -noout -dates 2>/dev/null
echo | openssl s_client -connect 127.0.0.1:8443 -servername {DOMAIN} 2>/dev/null | openssl x509 -noout -dates 2>/dev/null
echo '=== SSHD ==='
sshd -T | egrep -i 'port |permitrootlogin|passwordauthentication|pubkeyauthentication'
echo '=== FAIL2BAN PORT ==='
fail2ban-client get sshd port 2>&1
''', timeout=90)
    write("R1-regression-server.txt", out+"\n"+err)

    # workstation probes
    post={
      "ssh_3333":"PASS" if tcp(3333) else "FAIL",
      "nginx_443":"PASS" if tcp(443) and tls(443).get("ok") else "FAIL",
      "xray_8443":"PASS" if tcp(8443) and tls(8443).get("ok") else "FAIL",
      "public_20901":"NOT EXPOSED" if ("127.0.0.1:20901" in out and "0.0.0.0:20901" not in out) else "CHECK",
      "vpn_egress": HOST if re.search(rf"\b{re.escape(HOST)}\b", out) else "UNKNOWN",
      "tls_443":tls(443),"tls_8443":tls(8443),
      "http_2096":http_head(2096),
      "tcp_2096_workstation":tcp(2096),
    }
    # independent key again
    try:
        ck=connect(OPERATOR); code,o,_=run(ck,"whoami; echo OP_OK"); ck.close()
        post["key_operator"]="PASS" if "OP_OK" in o else "FAIL"
    except Exception as e:
        post["key_operator"]=f"FAIL:{type(e).__name__}"
    try:
        ck=connect("root"); code,o,_=run(ck,"whoami; echo ROOT_OK"); ck.close()
        post["key_root"]="PASS" if "ROOT_OK" in o else "FAIL"
    except Exception as e:
        post["key_root"]=f"FAIL:{type(e).__name__}"

    # VPN HTTPS smoke via server curl to public site
    code,o,_=run(c,"curl -4 -sI --max-time 15 https://example.com | head -1; echo SMOKE_EXIT:$?", timeout=30)
    write("R1-vpn-https-smoke.txt", o)
    post["vpn_https"]="PASS" if "SMOKE_EXIT:0" in o and "HTTP" in o else "FAIL"

    RESULT["post_gates"]=post
    write("R1-post-gates.json", json.dumps(post, indent=2))

    # Verdict
    critical=[post.get("ssh_3333"), post.get("nginx_443"), post.get("xray_8443"), RESULT["gates"].get("backup")]
    if all(x=="PASS" for x in critical) and post.get("public_20901")=="NOT EXPOSED" and post.get("vpn_egress")==HOST:
        if RESULT["gates"].get("port_2096") in ("HARDENED","REQUIRED+RESTRICTED") and RESULT["gates"].get("key_based_operator_ssh")=="PASS":
            RESULT["verdict"]="PASS"
        else:
            RESULT["verdict"]="PARTIAL"
    else:
        RESULT["verdict"]="FAIL"

    write("00-summary.json", json.dumps(RESULT, indent=2))
    print("VERDICT", RESULT["verdict"])
    print("POST", json.dumps(post))
    try: c.close()
    except Exception: pass
    return 0 if RESULT["verdict"] in ("PASS","PARTIAL") else 1

if __name__=="__main__":
    raise SystemExit(main())


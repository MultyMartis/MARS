#!/bin/bash
set -euo pipefail
echo "HOST=$(hostname)"
date -u
echo "XUI_ACTIVE=$(systemctl is-active x-ui)"
XRAY_BIN=/usr/local/x-ui/bin/xray-linux-amd64
"$XRAY_BIN" version | head -5 || true
dpkg -l x-ui 2>/dev/null | tail -1 || true
command -v nginx >/dev/null && echo NGINX=present || echo NGINX=absent
echo '=== SS ==='
ss -lntp | awk 'NR==1 || /:22|:443|:8443|:24443|:9443|:20901|:2096|:80/'
echo '=== UFW ==='
ufw status numbered
echo '=== INBOUNDS ==='
python3 - <<'PY'
import json,sqlite3,shutil
conn=sqlite3.connect('/etc/x-ui/x-ui.db')
cur=conn.cursor()
for row in cur.execute('SELECT id, remark, port, protocol, enable FROM inbounds ORDER BY port'):
    print(row)
for port in (443,8443,24443,9443):
    cur.execute('SELECT id, remark, stream_settings, settings, sniffing FROM inbounds WHERE port=?',(port,))
    r=cur.fetchone()
    if not r:
        print('PORT',port,'MISSING'); continue
    iid,remark,ss,st,sn=r
    ssj=json.loads(ss); stj=json.loads(st)
    sniff=json.loads(sn) if sn else {}
    print('PORT',port,'id',iid,'remark',remark,'net',ssj.get('network'),'sec',ssj.get('security'),'clients',len(stj.get('clients',[])),'sniff',sniff.get('enabled'))
conn.close()
PY
echo '=== TLS8443 ==='
echo | openssl s_client -connect 127.0.0.1:8443 -servername metacode-cloud.com -alpn http/1.1 2>/dev/null | openssl x509 -noout -subject -issuer 2>/dev/null || true

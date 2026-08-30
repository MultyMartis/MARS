#!/bin/bash
set -euo pipefail
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
NAME="eqvps-pre-alt-a-reality-vision-${STAMP}"
ROOT=/root/mars-backups
DIR="${ROOT}/${NAME}"
TGZ="${ROOT}/${NAME}.tgz"
mkdir -p "${DIR}/meta" "${DIR}/certs-meta"
cp -a /etc/x-ui "${DIR}/etc-x-ui"
cp -a /usr/local/x-ui/bin/config.json "${DIR}/config.json"
cp -a /etc/letsencrypt/live/metacode-cloud.com/fullchain.pem "${DIR}/certs-meta/" || true
cp -a /etc/letsencrypt/live/metacode-cloud.com/privkey.pem "${DIR}/certs-meta/" || true
ufw status numbered > "${DIR}/meta/ufw-status.txt" 2>&1 || true
ss -lntp > "${DIR}/meta/ss-lntp.txt" 2>&1 || true
systemctl status x-ui --no-pager > "${DIR}/meta/x-ui-status.txt" 2>&1 || true
/usr/local/x-ui/bin/xray-linux-amd64 version > "${DIR}/meta/xray-version.txt" 2>&1 || true
dpkg -l x-ui > "${DIR}/meta/x-ui-dpkg.txt" 2>&1 || true
python3 - "$DIR" <<'PY'
import json,sqlite3,sys
d=sys.argv[1]
conn=sqlite3.connect('/etc/x-ui/x-ui.db')
cur=conn.cursor()
rows=[]
for r in cur.execute('SELECT id,remark,port,protocol,enable,stream_settings FROM inbounds ORDER BY port'):
    ss=json.loads(r[5])
    rows.append({'id':r[0],'remark':r[1],'port':r[2],'protocol':r[3],'enable':r[4],'network':ss.get('network'),'security':ss.get('security')})
open(d+'/meta/inbounds-safe.json','w').write(json.dumps(rows,indent=2))
conn.close()
PY
tar -czf "${TGZ}" -C "${ROOT}" "${NAME}"
sha256sum "${TGZ}"
echo "BACKUP_TGZ=${TGZ}"
echo "BACKUP_NAME=${NAME}"

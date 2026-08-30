#!/bin/bash
set -euo pipefail
NAME="$1"
ADDR="$2"
XRAY=/usr/local/x-ui/bin/xray-linux-amd64
CFG=/tmp/mars-alt-a-${NAME}.json
LOG=/tmp/mars-alt-a-${NAME}.log
SRC=/home/marsops/mars-alt-a-${NAME}.json
cp "$SRC" "$CFG"
chmod 600 "$CFG"
pkill -f "$CFG" >/dev/null 2>&1 || true
ss -lntp | grep ':9443' || true
$XRAY run -c "$CFG" >"$LOG" 2>&1 &
XPID=$!
sleep 3
if ! kill -0 "$XPID" 2>/dev/null; then
  echo XRAY_DIED
  tail -40 "$LOG" || true
  exit 0
fi
echo "XRAY_PID=$XPID"
IP=$(curl -sS --max-time 15 -x socks5h://127.0.0.1:18095 https://api.ipify.org || echo CURL_FAIL)
echo "EGRESS=$IP"
echo TRACE_BEGIN
curl -sS --max-time 15 -x socks5h://127.0.0.1:18095 https://www.cloudflare.com/cdn-cgi/trace | head -8 || true
echo TRACE_END
kill "$XPID" >/dev/null 2>&1 || true
wait "$XPID" 2>/dev/null || true
rm -f "$CFG" "$SRC"
echo "DONE_${NAME^^}"

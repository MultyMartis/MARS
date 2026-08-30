#!/usr/bin/env python3
import json, subprocess, os, time, signal, uuid, hashlib

XRAY = "/usr/local/x-ui/bin/xray-linux-amd64"
PORT = 19443
out = subprocess.check_output([XRAY, "x25519"], text=True)
priv = pub = None
for line in out.splitlines():
    low = line.lower()
    if "private" in low:
        priv = line.split(":", 1)[-1].strip()
    if "public" in low:
        pub = line.split(":", 1)[-1].strip()
if not priv or not pub:
    print("KEYGEN_FAIL")
    print(out)
    raise SystemExit(2)
uid = str(uuid.uuid4())
sid = os.urandom(8).hex()
dest = "www.cloudflare.com:443"
sni = "www.cloudflare.com"
server = {
    "log": {"loglevel": "warning"},
    "inbounds": [
        {
            "listen": "127.0.0.1",
            "port": PORT,
            "protocol": "vless",
            "settings": {
                "clients": [{"id": uid, "flow": "xtls-rprx-vision"}],
                "decryption": "none",
            },
            "streamSettings": {
                "network": "tcp",
                "security": "reality",
                "realitySettings": {
                    "show": False,
                    "dest": dest,
                    "xver": 0,
                    "serverNames": [sni],
                    "privateKey": priv,
                    "shortIds": ["", sid],
                },
            },
            "sniffing": {"enabled": False, "destOverride": ["http", "tls"]},
        }
    ],
    "outbounds": [{"protocol": "freedom", "tag": "direct"}],
}
client = {
    "log": {"loglevel": "warning"},
    "inbounds": [
        {
            "listen": "127.0.0.1",
            "port": 18098,
            "protocol": "socks",
            "settings": {"udp": False},
        }
    ],
    "outbounds": [
        {
            "protocol": "vless",
            "settings": {
                "vnext": [
                    {
                        "address": "127.0.0.1",
                        "port": PORT,
                        "users": [
                            {
                                "id": uid,
                                "encryption": "none",
                                "flow": "xtls-rprx-vision",
                            }
                        ],
                    }
                ]
            },
            "streamSettings": {
                "network": "tcp",
                "security": "reality",
                "realitySettings": {
                    "fingerprint": "chrome",
                    "serverName": sni,
                    "publicKey": pub,
                    "shortId": sid,
                    "spiderX": "/",
                },
            },
        }
    ],
}
spath = "/home/marsops/mars-standalone-server.json"
cpath = "/home/marsops/mars-standalone-client.json"
open(spath, "w").write(json.dumps(server))
os.chmod(spath, 0o600)
open(cpath, "w").write(json.dumps(client))
os.chmod(cpath, 0o600)
# Do NOT pkill the probe script itself (name contains mars-standalone).
subprocess.call(
    ["pkill", "-f", "xray-linux-amd64 run -c /home/marsops/mars-standalone-"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
)
time.sleep(1)
sp = subprocess.Popen(
    [XRAY, "run", "-c", spath],
    stdout=open("/home/marsops/mars-standalone-server.log", "w"),
    stderr=subprocess.STDOUT,
)
time.sleep(2)
if sp.poll() is not None:
    print("SERVER_DIED")
    print(open("/home/marsops/mars-standalone-server.log").read()[-1500:])
    raise SystemExit(3)
print("SERVER_UP")
cp = subprocess.Popen(
    [XRAY, "run", "-c", cpath],
    stdout=open("/home/marsops/mars-standalone-client.log", "w"),
    stderr=subprocess.STDOUT,
)
time.sleep(2)
if cp.poll() is not None:
    print("CLIENT_DIED")
    print(open("/home/marsops/mars-standalone-client.log").read()[-1500:])
    sp.send_signal(signal.SIGTERM)
    raise SystemExit(4)
print("CLIENT_UP")
try:
    eg = subprocess.check_output(
        [
            "curl",
            "-sS",
            "--max-time",
            "15",
            "-x",
            "socks5h://127.0.0.1:18098",
            "https://api.ipify.org",
        ],
        text=True,
        stderr=subprocess.STDOUT,
        timeout=25,
    ).strip()
    print("EGRESS=" + eg)
except subprocess.CalledProcessError as e:
    print("CURL_FAIL", (e.output or "")[:300])
    print("CLIENT_LOG", open("/home/marsops/mars-standalone-client.log").read()[-1000:])
    print("SERVER_LOG", open("/home/marsops/mars-standalone-server.log").read()[-1000:])
except Exception as e:
    print("ERR", type(e).__name__, e)
finally:
    for p in (cp, sp):
        try:
            p.send_signal(signal.SIGTERM)
            p.wait(timeout=3)
        except Exception:
            try:
                p.kill()
            except Exception:
                pass
    for f in (spath, cpath):
        try:
            os.remove(f)
        except Exception:
            pass
print("PUB_SHA12=" + hashlib.sha256(pub.encode()).hexdigest()[:12])
print("DONE")

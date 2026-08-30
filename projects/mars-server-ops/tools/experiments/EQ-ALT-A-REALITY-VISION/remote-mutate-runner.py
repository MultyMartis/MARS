#!/usr/bin/env python3
"""Apply EQ-ALT-A REALITY+Vision inbound from payload JSON. Runs on EQVPS as root."""
from __future__ import annotations

import json
import sqlite3
import sys
import time

PAYLOAD_PATH = "/home/marsops/mars-alt-a-reality-payload.json"


def main() -> int:
    payload = json.load(open(PAYLOAD_PATH, encoding="utf-8"))
    port = payload["port"]
    conn = sqlite3.connect("/etc/x-ui/x-ui.db")
    cur = conn.cursor()

    cur.execute("SELECT id FROM inbounds WHERE port=?", (port,))
    if cur.fetchone():
        print("PORT_EXISTS")
        return 2
    cur.execute("SELECT id FROM inbounds WHERE remark=?", (payload["remark"],))
    if cur.fetchone():
        print("REMARK_EXISTS")
        return 3

    # Sniffing OFF — align with known-good VEESP control (vs EQVPS :8443 sniffing-on)
    sniff = {
        "enabled": False,
        "destOverride": ["http", "tls", "quic", "fakedns"],
        "metadataOnly": False,
        "routeOnly": False,
    }
    client = {
        "id": payload["uuid"],
        "flow": payload["flow"],
        "email": payload["client_email"],
        "limitIp": 0,
        "totalGB": 0,
        "expiryTime": 0,
        "enable": True,
        "tgId": "",
        "subId": payload["client_subid"],
        "comment": "EQ-ALT-A REALITY+Vision isolated test",
        "reset": 0,
    }
    settings = {
        "clients": [client],
        "decryption": "none",
        "encryption": "none",
        "fallbacks": [],
    }
    stream = {
        "network": "tcp",
        "security": "reality",
        "externalProxy": [],
        "realitySettings": {
            "show": False,
            "xver": 0,
            "dest": payload["dest"],
            "serverNames": payload["serverNames"],
            "privateKey": payload["privateKey"],
            "minClient": "",
            "maxClient": "",
            "maxTimediff": 0,
            "shortIds": payload["shortIds"],
            "settings": {
                "publicKey": payload["publicKey"],
                "fingerprint": payload["fingerprint"],
                "serverName": "",
                "spiderX": payload["spiderX"],
            },
        },
        "tcpSettings": {"acceptProxyProtocol": False, "header": {"type": "none"}},
    }
    now = int(time.time() * 1000)
    ib_cols = [r[1] for r in cur.execute("PRAGMA table_info(inbounds)")]
    row = {
        "user_id": 0,
        "up": 0,
        "down": 0,
        "total": 0,
        "remark": payload["remark"],
        "enable": 1,
        "expiry_time": 0,
        "listen": "",
        "port": port,
        "protocol": "vless",
        "settings": json.dumps(settings, separators=(",", ":")),
        "stream_settings": json.dumps(stream, separators=(",", ":")),
        "tag": payload["tag"],
        "sniffing": json.dumps(sniff, separators=(",", ":")),
        "share_addr_strategy": "node",
        "disable_flow": 0,
        "sub_sort_index": 3,
        "traffic_reset": "never",
        "traffic_reset_day": 1,
        "last_traffic_reset_time": 0,
    }
    cols = [c for c in ib_cols if c != "id" and c in row]
    cur.execute(
        "INSERT INTO inbounds(" + ",".join(cols) + ") VALUES(" + ",".join(["?"] * len(cols)) + ")",
        [row[c] for c in cols],
    )
    iid = cur.lastrowid

    c_cols = [r[1] for r in cur.execute("PRAGMA table_info(clients)")]
    candidates = {
        "enable": 1,
        "email": payload["client_email"],
        "uuid": payload["uuid"],
        "sub_id": payload["client_subid"],
        "created_at": now,
        "updated_at": now,
        "flow": payload["flow"],
        "total_gb": 0,
        "expiry_time": 0,
        "limit_ip": 0,
        "tg_id": 0,
        "reset": 0,
        "comment": "EQ-ALT-A REALITY+Vision",
        "totalGB": 0,
        "expiryTime": 0,
        "limitIp": 0,
        "tgId": 0,
        "subId": payload["client_subid"],
    }
    crow = {col: candidates[col] for col in c_cols if col != "id" and col in candidates}
    cur.execute("SELECT id FROM clients WHERE email=?", (payload["client_email"],))
    ex = cur.fetchone()
    if ex:
        client_id = ex[0]
        sets = ",".join([f"{k}=?" for k in crow])
        cur.execute(f"UPDATE clients SET {sets} WHERE id=?", list(crow.values()) + [client_id])
    else:
        cols = list(crow.keys())
        cur.execute(
            "INSERT INTO clients(" + ",".join(cols) + ") VALUES(" + ",".join(["?"] * len(cols)) + ")",
            [crow[k] for k in cols],
        )
        client_id = cur.lastrowid

    cur.execute(
        "DELETE FROM client_inbounds WHERE client_id=? AND inbound_id=?",
        (client_id, iid),
    )
    ci_cols = [r[1] for r in cur.execute("PRAGMA table_info(client_inbounds)")]
    ci = {"client_id": client_id, "inbound_id": iid}
    if "created_at" in ci_cols:
        ci["created_at"] = now
    if "flow_override" in ci_cols:
        ci["flow_override"] = None
    cur.execute(
        "INSERT INTO client_inbounds(" + ",".join(ci.keys()) + ") VALUES(" + ",".join(["?"] * len(ci)) + ")",
        list(ci.values()),
    )
    conn.commit()
    conn.close()
    print("MUTATION_OK", "inbound_id", iid, "client_id", client_id)
    return 0


if __name__ == "__main__":
    sys.exit(main())

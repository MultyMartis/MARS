#!/usr/bin/env python3
"""Create INACTIVE Admin.v3.rollback n8n workflow + mars_core registry row.

Does NOT activate any workflow. Does NOT touch Admin.dev / Operational.*.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
EVID = ROOT / "evidence" / "candidate-workflow" / "iseo-admin-v3"
WF_PATH = ROOT / "workflows" / "admin-v3-rollback" / "Admin.v3.rollback.n8n.json"
N8N_ENV = Path(r"X:\AI MARS\local\tokens\n8n-api.env")
PRIV = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_ed25519")
SUDO_PATH = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_sudo.secret")
HOST = "178.173.255.239"
PROD_WF_ID = "wLrLp4WQHm1VJmxz"
CAND_WF_ID = "Zk9b1BiXpYN9rMMo"
WF_NAME = "i-SEO Sales Manager - Admin.v3.rollback"


def load_dotenv(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def n8n_request(method: str, path: str, body: dict | None = None) -> dict:
    env = load_dotenv(N8N_ENV)
    base = env.get("N8N_API_URL") or env.get("N8N_BASE_URL") or env.get("N8N_URL")
    key = env.get("N8N_API_KEY") or env.get("API_KEY")
    if not base or not key:
        raise SystemExit("missing_n8n_api_url_or_key")
    url = base.rstrip("/") + path
    data = None if body is None else json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "X-N8N-API-KEY": key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        raw = resp.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def ssh_sudo(script: str, timeout: int = 120) -> tuple[int, str, str]:
    sudo = SUDO_PATH.read_text(encoding="utf-8").strip()
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkey = paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    c.connect(HOST, 22, "marsops", pkey=pkey, timeout=60, allow_agent=False, look_for_keys=False)
    chan = c.get_transport().open_session()
    chan.settimeout(timeout)
    chan.exec_command("sudo -S -p '' bash -s")
    chan.sendall((sudo + "\n").encode())
    chan.sendall(script.encode())
    chan.shutdown_write()
    out = chan.makefile("rb").read().decode("utf-8", "replace")
    err = chan.makefile_stderr("rb").read().decode("utf-8", "replace")
    st = chan.recv_exit_status()
    c.close()
    return st, out, err


def main() -> int:
    EVID.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    export = json.loads(WF_PATH.read_text(encoding="utf-8"))
    pre_hash = hashlib.sha256(WF_PATH.read_bytes()).hexdigest()

    listing = n8n_request("GET", "/api/v1/workflows?limit=250")
    data = listing.get("data", listing) if isinstance(listing, dict) else listing
    wf_id = None
    if isinstance(data, list):
        for w in data:
            if w.get("name") == WF_NAME:
                wf_id = w.get("id")
                break

    payload = {
        "name": WF_NAME,
        "nodes": export.get("nodes"),
        "connections": export.get("connections"),
        "settings": export.get("settings")
        or {"executionOrder": "v1", "callerPolicy": "workflowsFromSameOwner"},
        "staticData": None,
    }
    if wf_id:
        created = n8n_request("PUT", f"/api/v1/workflows/{wf_id}", payload)
    else:
        created = n8n_request("POST", "/api/v1/workflows", payload)
        wf_id = created.get("id")
    try:
        n8n_request("POST", f"/api/v1/workflows/{wf_id}/deactivate", {})
    except Exception:
        pass

    prod = n8n_request("GET", f"/api/v1/workflows/{PROD_WF_ID}")
    cand = n8n_request("GET", f"/api/v1/workflows/{CAND_WF_ID}")
    rb = n8n_request("GET", f"/api/v1/workflows/{wf_id}")

    export["id"] = wf_id
    export["active"] = False
    export["name"] = WF_NAME
    meta = export.get("meta") or {}
    meta["n8n_workflow_id"] = wf_id
    meta["status"] = "rollback"
    meta["pin_ts"] = ts
    export["meta"] = meta
    WF_PATH.write_text(json.dumps(export, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    new_hash = hashlib.sha256(WF_PATH.read_bytes()).hexdigest()

    reg_sql = f"""
DELETE FROM mars_core.workflow_releases wr
USING mars_core.apps a
WHERE wr.app_id = a.id
  AND a.app_key = 'app_iseo_sales'
  AND wr.workflow_family = 'admin_runtime'
  AND wr.release_version = 'Admin.v3.rollback';

INSERT INTO mars_core.workflow_releases (
  app_id, workflow_family, n8n_workflow_id, release_version,
  data_contract_version, status, git_export_hash, notes, metadata
)
SELECT a.id, 'admin_runtime', '{wf_id}', 'Admin.v3.rollback',
  'iseo-sales-v1', 'rollback', '{new_hash}',
  'PG-compatible Admin rollback pin; inactive; never reactivate Sheets Admin.dev after PG_PRIMARY',
  jsonb_build_object(
    'pinned_from', 'Admin.v3.dev',
    'pinned_from_id', '{CAND_WF_ID}',
    'credential_id', 'XCmmOgzZ1RWT4Fg3',
    'credential_name', 'ISEO Runtime PG (v3)',
    'role', 'iseo_runtime',
    'pin_ts', '{ts}',
    'pre_id_hash', '{pre_hash}'
  )
FROM mars_core.apps a WHERE a.app_key='app_iseo_sales'
RETURNING id, status, n8n_workflow_id, release_version;

SELECT wr.release_version, wr.status, wr.n8n_workflow_id, left(wr.git_export_hash,12) AS hash12
FROM mars_core.workflow_releases wr
JOIN mars_core.apps a ON a.id = wr.app_id
WHERE a.app_key='app_iseo_sales' AND wr.workflow_family='admin_runtime'
ORDER BY wr.created_at;
"""
    remote = f"/opt/mars/tmp/admin_v3_rollback_register_{ts}.sql"
    local = EVID / f"register_rollback_{ts}.sql"
    local.write_text(reg_sql, encoding="utf-8")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkey = paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    c.connect(HOST, 22, "marsops", pkey=pkey, timeout=60, allow_agent=False, look_for_keys=False)
    sftp = c.open_sftp()
    tmp = f"/tmp/admin_v3_rollback_register_{ts}.sql"
    sftp.put(str(local), tmp)
    sftp.close()
    c.close()
    st, out, err = ssh_sudo(
        f"mkdir -p /opt/mars/tmp; mv '{tmp}' '{remote}'; "
        f"docker exec -i mars-postgres psql -U mars_admin -d mars -v ON_ERROR_STOP=1 < '{remote}'\n",
        timeout=60,
    )
    (EVID / "rollback_registry_stdout.txt").write_text(out + "\n---STDERR---\n" + err, encoding="utf-8")

    proof = {
        "pin_ts": ts,
        "rollback": {
            "id": wf_id,
            "name": rb.get("name"),
            "active": bool(rb.get("active")),
            "export_hash": new_hash,
            "pre_id_hash": pre_hash,
        },
        "candidate": {
            "id": CAND_WF_ID,
            "name": cand.get("name"),
            "active": bool(cand.get("active")),
        },
        "production": {
            "id": PROD_WF_ID,
            "name": prod.get("name"),
            "active": bool(prod.get("active")),
        },
        "registry_exit": st,
        "registry_ok": st == 0,
        "hard_stops": {
            "activated_v3": False,
            "deactivated_production": False,
            "activated_rollback": False,
            "sheets_admin_as_post_pg_rollback": False,
        },
    }
    (EVID / "rollback_pin_proof.json").write_text(json.dumps(proof, indent=2), encoding="utf-8")
    print(json.dumps(proof, indent=2))
    if bool(rb.get("active")) or not bool(prod.get("active")) or bool(cand.get("active")):
        print("ACTIVE_STATE_VIOLATION", file=sys.stderr)
        return 2
    if st != 0:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

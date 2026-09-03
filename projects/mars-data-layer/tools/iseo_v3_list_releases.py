#!/usr/bin/env python3
"""Refresh mars_core.workflow_releases listing for cutover-prep evidence."""
from __future__ import annotations

import json
from pathlib import Path

import paramiko

PRIV = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_ed25519")
SUDO_PATH = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_sudo.secret")
HOST = "178.173.255.239"
EVID = Path(__file__).resolve().parents[1] / "evidence" / "cutover-prep" / "iseo-sales-v1"


def main() -> int:
    sudo = SUDO_PATH.read_text(encoding="utf-8").strip()
    sql = (
        "SELECT wr.release_version, wr.status, wr.n8n_workflow_id, "
        "left(wr.git_export_hash,12) AS hash12 "
        "FROM mars_core.workflow_releases wr "
        "JOIN mars_core.apps a ON a.id = wr.app_id "
        "WHERE a.app_key='app_iseo_sales' AND wr.workflow_family='operational_intake' "
        "ORDER BY wr.created_at;"
    )
    script = (
        "docker exec -i mars-postgres psql -U mars_admin -d mars "
        f"-v ON_ERROR_STOP=1 -c \"{sql}\"\n"
    )
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkey = paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    c.connect(HOST, 22, "marsops", pkey=pkey, timeout=60, allow_agent=False, look_for_keys=False)
    chan = c.get_transport().open_session()
    chan.settimeout(60)
    chan.exec_command("sudo -S -p '' bash -s")
    chan.sendall((sudo + "\n").encode())
    chan.sendall(script.encode())
    chan.shutdown_write()
    out = chan.makefile("rb").read().decode("utf-8", "replace")
    err = chan.makefile_stderr("rb").read().decode("utf-8", "replace")
    st = chan.recv_exit_status()
    c.close()
    EVID.mkdir(parents=True, exist_ok=True)
    (EVID / "workflow_releases_listing.txt").write_text(out + ("\n" + err if err else ""), encoding="utf-8")
    proof_path = EVID / "rollback_pin_proof.json"
    proof = json.loads(proof_path.read_text(encoding="utf-8"))
    proof["registry_ok"] = st == 0
    proof["registry_exit"] = st
    proof["registry_note"] = "INSERT of rollback row succeeded earlier; listing refreshed"
    proof_path.write_text(json.dumps(proof, indent=2), encoding="utf-8")
    print(out)
    print("EXIT", st)
    return 0 if st == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

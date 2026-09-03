#!/usr/bin/env python3
"""Probe VEESP PG/n8n for Operational.v3 candidate build. No secrets printed."""
from __future__ import annotations

from pathlib import Path

import paramiko

HOST = "178.173.255.239"
PRIV = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_ed25519")
SUDO_PATH = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_sudo.secret")


def main() -> None:
    sudo = SUDO_PATH.read_text(encoding="utf-8").strip()
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkey = paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    c.connect(HOST, 22, "marsops", pkey=pkey, timeout=30, allow_agent=False, look_for_keys=False)
    chan = c.get_transport().open_session()
    chan.settimeout(90)
    chan.exec_command("sudo -S -p '' bash -s")
    chan.sendall((sudo + "\n").encode())
    script = r"""
set -euo pipefail
echo NET:
docker network inspect mars-postgres-net -f '{{range .Containers}}{{.Name}} {{end}}'
echo ROLES:
docker exec mars-postgres psql -U mars_admin -d mars -tAc "SELECT rolname||'|'||rolcanlogin FROM pg_roles WHERE rolname LIKE 'iseo%' OR rolname LIKE 'mars_%' ORDER BY 1"
echo MIG:
docker exec mars-postgres psql -U mars_admin -d mars -tAc "SELECT schema_name||'|'||version FROM mars_core.schema_migrations WHERE schema_name IN ('app_iseo_sales','mars_core') ORDER BY 1,2"
echo APPS:
docker exec mars-postgres psql -U mars_admin -d mars -tAc "SELECT id||'|'||app_key FROM mars_core.apps ORDER BY 1"
echo N8N_NET:
docker ps --format '{{.Names}}' | while read -r n; do
  nets=$(docker inspect "$n" --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}} {{end}}' 2>/dev/null || true)
  echo "$n :: $nets"
done
echo COUNTS:
docker exec mars-postgres psql -U mars_admin -d mars -tAc "SELECT 'inbound='||count(*) FROM app_iseo_sales.inbound_events; SELECT 'leads='||count(*) FROM app_iseo_sales.leads; SELECT 'deliveries='||count(*) FROM app_iseo_sales.deliveries"
"""
    chan.sendall(script.encode())
    chan.shutdown_write()
    out = chan.makefile("rb").read().decode("utf-8", "replace")
    err = chan.makefile_stderr("rb").read().decode("utf-8", "replace")
    st = chan.recv_exit_status()
    print(out)
    if err.strip():
        print("STDERR:", err[:1000])
    print("exit", st)
    c.close()


if __name__ == "__main__":
    main()

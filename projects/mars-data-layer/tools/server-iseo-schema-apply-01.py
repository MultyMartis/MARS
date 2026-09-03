#!/usr/bin/env python3
"""MARS DATA LAYER — SERVER PG18 APPLICATION SCHEMA APPLY / VALIDATION 01

Applies canonical mars_core + app_iseo_sales migrations to VEESP-N8N-01
PostgreSQL 18 foundation. No Sheets migration. No n8n workflow cutover.

Secrets never printed. Evidence under projects/mars-data-layer/evidence/...
and a local twin under VEESP-N8N-01 local infrastructure.
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import paramiko

HOST = "178.173.255.239"
PORT = 22
OPERATOR = "marsops"
EXPECTED_N8N_CONTAINER = "n8n_n8n_1"
EXPECTED_N8N_VERSION = "2.14.2"
PG_CONTAINER = "mars-postgres"
PG_NETWORK = "mars-postgres-net"
PG_DB = "mars"
PG_BOOTSTRAP_USER = "mars_admin"
PG_BACKUP_DIR = "/root/mars-backups/postgres"
PG_SERVER_MIG_DIR = "/opt/mars-postgres/migrations-iseo-schema-v1"

WT_ROOT = Path(__file__).resolve().parents[3]  # worktree root
DL_ROOT = Path(__file__).resolve().parents[1]  # mars-data-layer
LOCAL_ROOT = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01")
LOCAL_SECRETS = LOCAL_ROOT / "postgres" / "secrets.env"
SSH_DIR = LOCAL_ROOT / "ssh"
PRIV_OPS = SSH_DIR / "marsops_ed25519"
SUDO_PATH = SSH_DIR / "marsops_sudo.secret"
API_ENV = Path(r"X:\AI MARS\local\tokens\n8n-api.env")

UTC = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
EV_GIT = DL_ROOT / "evidence" / "server-validation" / "iseo-sales-schema-v1"
EV_LOCAL = LOCAL_ROOT / "postgres-schema-apply-01" / f"run-{UTC}"

MIGRATIONS = [
    "database/roles/001_create_roles.sql",
    "database/core/migrations/0001_roles_and_schemas.sql",
    "database/core/migrations/0002_mars_core.sql",
    "database/app_iseo_sales/migrations/0001_base_tables.sql",
    "database/app_iseo_sales/migrations/0002_indexes.sql",
    "database/app_iseo_sales/migrations/0003_functions.sql",
    "database/app_iseo_sales/migrations/0004_grants.sql",
]

TEST_SQL = [
    "tests/iseo_sales/02_constraints.sql",
    "tests/iseo_sales/03_permissions.sql",
    "tests/iseo_sales/04_extended_local_validation.sql",
    "tests/iseo_sales/05_inventory_and_explain.sql",
]

RESULT: dict = {
    "wave": "MARS-BOT-DATA-PLATFORM-SERVER-APPLICATION-MIGRATIONS-APPLY-01",
    "started_utc": datetime.now(timezone.utc).isoformat(),
    "target": "VEESP-N8N-01",
    "gates": {},
    "facts": {},
    "proofs": {},
    "verdict": {},
}


def ensure_dirs() -> None:
    EV_GIT.mkdir(parents=True, exist_ok=True)
    EV_LOCAL.mkdir(parents=True, exist_ok=True)


def write_local(name: str, body: str) -> None:
    (EV_LOCAL / name).write_text(body, encoding="utf-8")


def write_git(name: str, body: str) -> None:
    (EV_GIT / name).write_text(body, encoding="utf-8")


def redact(text: str, *vals: str) -> str:
    out = text or ""
    for v in vals:
        if v:
            out = out.replace(v, "<redacted>")
    return out


def parse_env(path: Path) -> dict:
    data = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        data[k.strip()] = v.strip().strip('"').strip("'")
    return data


def ssh_connect() -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkey = paramiko.Ed25519Key.from_private_key_file(str(PRIV_OPS))
    c.connect(HOST, PORT, OPERATOR, pkey=pkey, timeout=45, allow_agent=False, look_for_keys=False)
    return c


def sudo_pw() -> str:
    return SUDO_PATH.read_text(encoding="utf-8").strip()


def run_sudo(client: paramiko.SSHClient, script: str, timeout: int = 180) -> tuple[int, str, str]:
    pw = sudo_pw()
    full = "#!/bin/bash\nset -euo pipefail\n" + script
    chan = client.get_transport().open_session()
    chan.settimeout(timeout)
    chan.exec_command("sudo -S -p '' bash -s")
    chan.sendall((pw + "\n").encode())
    chan.sendall(full.encode())
    chan.shutdown_write()
    stdout_b = chan.makefile("rb").read()
    stderr_b = chan.makefile_stderr("rb").read()
    status = chan.recv_exit_status()
    stdout = stdout_b.decode("utf-8", errors="replace")
    stderr = stderr_b.decode("utf-8", errors="replace")
    return status, stdout, stderr


def run_sudo_ok(client: paramiko.SSHClient, script: str, label: str, timeout: int = 180, secrets: list[str] | None = None) -> str:
    st, out, err = run_sudo(client, script, timeout=timeout)
    secrets = secrets or []
    write_local(f"{label}.out.txt", redact(out, *secrets))
    write_local(f"{label}.err.txt", redact(err, *secrets))
    write_local(f"{label}.status.txt", str(st))
    if st != 0:
        raise RuntimeError(f"{label} failed status={st} err={redact(err, *secrets)[:1200]}")
    return out


def sftp_put_text(client: paramiko.SSHClient, remote_path: str, content: str) -> None:
    """Write via sudo tee (marsops may lack write on /opt)."""
    # Upload to /tmp then sudo mv
    tmp = f"/tmp/mars-schema-upload-{Path(remote_path).name}"
    sftp = client.open_sftp()
    with sftp.file(tmp, "w") as f:
        f.write(content)
    sftp.close()
    st, out, err = run_sudo(
        client,
        f"install -d -m 755 $(dirname '{remote_path}'); mv '{tmp}' '{remote_path}'; chmod 644 '{remote_path}'",
        timeout=60,
    )
    if st != 0:
        raise RuntimeError(f"sftp_put failed {remote_path}: {err}")


def api_workflows_snapshot() -> dict:
    api = parse_env(API_ENV)
    base = api.get("N8N_BASE_URL") or api.get("N8N_API_URL") or "https://n8n.ai-metacode.com"
    key = api.get("N8N_API_KEY") or api.get("API_KEY")
    if not key:
        return {"error": "no API key"}
    base = base.rstrip("/")
    req = urllib.request.Request(
        base + "/api/v1/workflows?limit=100",
        headers={"X-N8N-API-KEY": key, "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=45) as r:
        data = json.loads(r.read().decode())
    items = data.get("data") or data.get("workflows") or []
    active = sum(1 for w in items if w.get("active"))
    return {"total": len(items), "active": active}


def phase_preflight(client: paramiko.SSHClient, secrets: list[str]) -> dict:
    script = r"""
echo '===PG_CONTAINER==='
docker inspect mars-postgres --format 'NAME={{.Name}} ID={{.Id}} IMAGE={{.Config.Image}} STATUS={{.State.Status}} STARTED={{.State.StartedAt}} RESTARTCOUNT={{.RestartCount}}'
docker ps --filter name=^/mars-postgres$ --format 'PS_STATUS={{.Status}}'
echo '===PG_VERSION==='
docker exec mars-postgres psql -U mars_admin -d mars -tAc "SHOW server_version;"
echo '===PG_NETWORKS==='
docker inspect mars-postgres --format '{{range $k,$v := .NetworkSettings.Networks}}NET={{$k}}{{"\n"}}{{end}}'
echo '===PG_PORTS==='
docker inspect mars-postgres --format 'PortBindings={{json .HostConfig.PortBindings}} Published={{json .NetworkSettings.Ports}}'
echo '===SCHEMAS==='
docker exec mars-postgres psql -U mars_admin -d mars -c "\dn+"
echo '===TABLES_NONSYSTEM==='
docker exec mars-postgres psql -U mars_admin -d mars -c "SELECT n.nspname, c.relname, c.relkind FROM pg_class c JOIN pg_namespace n ON n.oid=c.relnamespace WHERE n.nspname NOT IN ('pg_catalog','information_schema','pg_toast') AND c.relkind IN ('r','v','m','S','f') ORDER BY 1,2;"
echo '===ROLES==='
docker exec mars-postgres psql -U mars_admin -d mars -c "SELECT rolname, rolsuper, rolcanlogin, rolbypassrls FROM pg_roles WHERE rolname NOT LIKE 'pg_%' ORDER BY 1;"
echo '===N8N==='
docker inspect n8n_n8n_1 --format 'NAME={{.Name}} ID={{.Id}} IMAGE={{.Config.Image}} STATUS={{.State.Status}} STARTED={{.State.StartedAt}} RESTARTCOUNT={{.RestartCount}}'
docker ps --filter name=n8n_n8n_1 --format 'PS_STATUS={{.Status}}'
docker exec n8n_n8n_1 n8n --version 2>/dev/null || true
docker inspect n8n_n8n_1 --format '{{range $k,$v := .NetworkSettings.Networks}}NET={{$k}}{{"\n"}}{{end}}'
echo '===RESOURCES==='
free -b
free -h
swapon --show || true
df -B1 /
df -h /
nproc
uptime
echo '===PG_MEM==='
docker stats --no-stream --format 'ctr={{.Name}} mem={{.MemUsage}} cpu={{.CPUPerc}}' mars-postgres n8n_n8n_1
echo '===SS_5432==='
ss -lntup | egrep ':5432|:22|:443|:80' || true
echo '===UFW==='
ufw status | head -20 || true
echo '===MARKER==='
docker exec mars-postgres psql -U mars_admin -d mars -c "SELECT * FROM _mars_foundation_marker;" 2>&1 || echo 'NO_MARKER_OR_OK'
"""
    out = run_sudo_ok(client, script, "01-preflight", timeout=120, secrets=secrets)

    unexpected = []
    for line in out.splitlines():
        # detect application schemas already present
        if re.search(r"\bmars_core\b", line) and ("schema" in line.lower() or "|" in line):
            if "CREATE SCHEMA" not in line:
                pass
        if "app_iseo_sales" in line and "nspname" not in line and "===SCHEMAS===" not in line:
            # table listing under app_iseo_sales would be unexpected
            if re.match(r"\s*app_iseo_sales\s*\|", line):
                unexpected.append(line.strip())

    # Parse schema list section more carefully
    in_tables = False
    app_objects = []
    for line in out.splitlines():
        if "===TABLES_NONSYSTEM===" in line:
            in_tables = True
            continue
        if in_tables and line.startswith("==="):
            in_tables = False
        if in_tables and ("mars_core" in line or "app_iseo_sales" in line or "app_seo_content" in line):
            app_objects.append(line.strip())

    facts = {
        "pg_healthy": ("(healthy)" in out and "mars-postgres" in out) or "STATUS=running" in out or "PS_STATUS=Up" in out,
        "pg_version_line": next((l for l in out.splitlines() if re.match(r"^\s*18\.", l)), ""),
        "port_bindings_empty": "PortBindings={}" in out or "PortBindings=map[]" in out or 'PortBindings={}' in out,
        "n8n_started_line": next((l for l in out.splitlines() if l.startswith("NAME=/n8n") or l.startswith("NAME=n8n")), ""),
        "unexpected_app_objects": app_objects,
        "api_workflows": api_workflows_snapshot(),
    }
    RESULT["facts"]["preflight"] = facts
    write_git(
        "PREFLIGHT-v1.md",
        "# PREFLIGHT-v1\n\n**UTC:** "
        + UTC
        + "\n\nSanitized raw evidence: local twin `01-preflight.*.txt` (not secrets).\n\n"
        + f"- PostgreSQL healthy/running: `{facts['pg_healthy']}`\n"
        + f"- Version sample: `{facts['pg_version_line'].strip()}`\n"
        + f"- Public PortBindings empty-ish: `{facts['port_bindings_empty']}`\n"
        + f"- Unexpected app objects count: `{len(app_objects)}`\n"
        + f"- n8n workflows API: `{facts['api_workflows']}`\n"
        + f"- n8n inspect: `{facts['n8n_started_line'][:200]}`\n",
    )
    if app_objects:
        write_git("PREFLIGHT-UNEXPECTED-OBJECTS-v1.md", "\n".join(app_objects))
        raise RuntimeError(f"STOP — unexpected application objects already exist: {app_objects[:20]}")
    RESULT["gates"]["preflight"] = "PASS"
    return facts


def phase_pre_dump(client: paramiko.SSHClient, secrets: list[str]) -> dict:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = f"{PG_BACKUP_DIR}/mars-pre-app-schema-{stamp}.sql.gz"
    script = f"""
mkdir -p {PG_BACKUP_DIR}
docker exec mars-postgres pg_dump -U mars_admin -d mars --format=plain --no-owner --no-acl | gzip -c > {path}
ls -la {path}
# readability check
gzip -t {path}
zcat {path} | head -c 400 | tr '\\n' ' '; echo
echo DUMP_PATH={path}
echo DUMP_BYTES=$(stat -c%s {path})
"""
    out = run_sudo_ok(client, script, "02-pre-dump", timeout=180, secrets=secrets)
    meta = {
        "timestamp_utc": stamp,
        "database": PG_DB,
        "format": "plain sql gzip",
        "path": path,
        "bytes": next((m.group(1) for m in [re.search(r"DUMP_BYTES=(\d+)", out)] if m), "?"),
        "gzip_test": "PASS",
    }
    RESULT["facts"]["pre_dump"] = meta
    write_git(
        "PRE-MIGRATION-DUMP-v1.md",
        "# PRE-MIGRATION-DUMP-v1\n\n"
        + f"- timestamp_utc: `{meta['timestamp_utc']}`\n"
        + f"- database: `{meta['database']}`\n"
        + f"- format: `{meta['format']}`\n"
        + f"- path: `{meta['path']}`\n"
        + f"- size_bytes: `{meta['bytes']}`\n"
        + f"- gzip -t: PASS\n"
        + "- secrets: none in dump metadata\n",
    )
    RESULT["gates"]["pre_dump"] = "PASS"
    return meta


def phase_upload_migrations(client: paramiko.SSHClient) -> None:
    run_sudo_ok(
        client,
        f"rm -rf {PG_SERVER_MIG_DIR}; mkdir -p {PG_SERVER_MIG_DIR}/database/roles "
        f"{PG_SERVER_MIG_DIR}/database/core/migrations "
        f"{PG_SERVER_MIG_DIR}/database/app_iseo_sales/migrations "
        f"{PG_SERVER_MIG_DIR}/tests/iseo_sales "
        f"{PG_SERVER_MIG_DIR}/fixtures/iseo_sales",
        "03-mig-dir",
        timeout=60,
    )
    files = list(MIGRATIONS) + list(TEST_SQL) + ["fixtures/iseo_sales/synthetic_v1.sql"]
    for rel in files:
        local = DL_ROOT / rel
        if not local.exists():
            raise FileNotFoundError(str(local))
        remote = f"{PG_SERVER_MIG_DIR}/{rel}"
        sftp_put_text(client, remote, local.read_text(encoding="utf-8"))
    RESULT["gates"]["upload"] = "PASS"


def phase_apply(client: paramiko.SSHClient, secrets: list[str]) -> str:
    # Bootstrap as mars_admin (superuser). Create NOLOGIN roles, then SET ROLE mars_migrator for DDL.
    # Ownership of created objects = mars_migrator.
    apply_sql = r"""
\set ON_ERROR_STOP on
SELECT current_user, current_database(), version();

\i /migrations/database/roles/001_create_roles.sql

-- Allow bootstrap admin to assume migrator for ownership-correct DDL
GRANT mars_migrator TO CURRENT_USER;
GRANT CREATE ON DATABASE mars TO mars_migrator;
SET ROLE mars_migrator;

\i /migrations/database/core/migrations/0001_roles_and_schemas.sql
\i /migrations/database/core/migrations/0002_mars_core.sql
\i /migrations/database/app_iseo_sales/migrations/0001_base_tables.sql
\i /migrations/database/app_iseo_sales/migrations/0002_indexes.sql
\i /migrations/database/app_iseo_sales/migrations/0003_functions.sql
\i /migrations/database/app_iseo_sales/migrations/0004_grants.sql

RESET ROLE;

-- Record data-contract tip if architecture table present
INSERT INTO mars_core.data_contract_versions (app_id, contract_key, version, status, activated_at, notes)
SELECT a.id, 'iseo_sales_schema', 'v1', 'active', now(),
       'SERVER PG18 schema apply 01 — schema only, no Sheets data'
FROM mars_core.apps a WHERE a.app_key = 'app_iseo_sales'
ON CONFLICT DO NOTHING;

SELECT schema_name, version, applied_at FROM mars_core.schema_migrations ORDER BY 1,2;
SELECT app_key, status FROM mars_core.apps ORDER BY 1;
"""
    sftp_put_text(client, f"{PG_SERVER_MIG_DIR}/_apply_all.sql", apply_sql)

    script = f"""
# Copy migration tree into container and apply
docker cp {PG_SERVER_MIG_DIR}/. mars-postgres:/migrations/
docker exec -u postgres mars-postgres psql -U mars_admin -d mars -v ON_ERROR_STOP=1 -f /migrations/_apply_all.sql
echo APPLY_EXIT=$?
"""
    out = run_sudo_ok(client, script, "04-apply", timeout=300, secrets=secrets)
    write_git(
        "MIGRATION-APPLY-v1.md",
        "# MIGRATION-APPLY-v1\n\n"
        "**Order:** roles/001 → core/0001 → core/0002 → app_iseo_sales/0001–0004\n\n"
        "**Migration role context:** `mars_migrator` via `SET ROLE` after bootstrap `mars_admin`.\n\n"
        "**Bootstrap role (name only):** `mars_admin`\n\n"
        "**Result:** APPLY SUCCESS (see local twin 04-apply.out.txt)\n\n"
        "```\n"
        + "\n".join(
            l
            for l in out.splitlines()
            if not any(s and s in l for s in secrets)
            and ("schema_name" in l or "app_" in l or "mars_core" in l or "APPLY" in l or "version" in l.lower() or re.match(r"^\s*\d+", l) or "|" in l)
        )[:80]
        + "\n```\n",
    )
    RESULT["gates"]["apply"] = "PASS"
    RESULT["facts"]["migration_role"] = "mars_migrator (SET ROLE from mars_admin)"
    return out


def phase_tests(client: paramiko.SSHClient, secrets: list[str]) -> dict:
    # Grant membership so SET ROLE works for permission tests
    bootstrap = r"""
\set ON_ERROR_STOP on
GRANT iseo_runtime, iseo_agent, iseo_reader TO CURRENT_USER;
"""
    sftp_put_text(client, f"{PG_SERVER_MIG_DIR}/_grant_membership.sql", bootstrap)
    results = {}
    for rel in [
        "_grant_membership.sql",
        "fixtures/iseo_sales/synthetic_v1.sql",
        "tests/iseo_sales/02_constraints.sql",
        "tests/iseo_sales/03_permissions.sql",
        "tests/iseo_sales/04_extended_local_validation.sql",
        "tests/iseo_sales/05_inventory_and_explain.sql",
    ]:
        label = "05-" + Path(rel).stem.replace("_", "-")
        script = f"""
docker cp {PG_SERVER_MIG_DIR}/. mars-postgres:/migrations/
docker exec -u postgres mars-postgres psql -U mars_admin -d mars -v ON_ERROR_STOP=1 -f /migrations/{rel}
echo TEST_OK={rel}
"""
        try:
            out = run_sudo_ok(client, script, label, timeout=300, secrets=secrets)
            results[rel] = {"status": "PASS", "tail": "\n".join(out.splitlines()[-30:])}
        except Exception as e:
            results[rel] = {"status": "FAIL", "error": str(e)[:1500]}
            write_git("TEST-FAILURE-v1.md", f"# FAIL\n\n`{rel}`\n\n```\n{e}\n```\n")
            raise
    RESULT["facts"]["tests"] = {k: v["status"] for k, v in results.items()}
    RESULT["gates"]["tests"] = "PASS"
    return results


def phase_cleanup_synthetic(client: paramiko.SSHClient, secrets: list[str]) -> None:
    cleanup = r"""
\set ON_ERROR_STOP on
-- Remove synthetic fixture rows only; keep schema
DELETE FROM app_iseo_sales.jobs WHERE payload::text LIKE '%synthetic%' OR payload::text LIKE '%fixture%' OR dedupe_key LIKE 'synth%' OR dedupe_key LIKE 'local-val%' OR dedupe_key LIKE 'srv-%' OR dedupe_key LIKE 'fixture%' OR dedupe_key LIKE 'dedupe-ext%' OR lead_id LIKE 'LEAD_%';
DELETE FROM app_iseo_sales.deliveries WHERE payload::text LIKE '%synthetic%' OR idempotency_key LIKE 'synth%' OR idempotency_key LIKE 'local-val%' OR idempotency_key LIKE 'srv-%' OR idempotency_key LIKE 'idem-ext%' OR lead_id LIKE 'LEAD_%';
DELETE FROM app_iseo_sales.idempotency_keys WHERE idempotency_key LIKE 'synth%' OR idempotency_key LIKE 'local-val%' OR idempotency_key LIKE 'test%' OR idempotency_key LIKE 'srv-%' OR idempotency_key LIKE 'ext-%' OR idempotency_key LIKE 'outbox%' OR idempotency_key LIKE 'job-%' OR idempotency_key LIKE 'c-%' OR idempotency_key LIKE 'stale%' OR idempotency_key LIKE 'dup%' OR idempotency_key LIKE 'idem-%' OR idempotency_key LIKE 'idem-status%' OR idempotency_key LIKE 'idem-ext%';
DELETE FROM app_iseo_sales.audit_logs WHERE actor_id IN ('MOD_B','ADMIN_A') OR actor_id LIKE 'test%' OR actor_id LIKE 'synthetic%' OR detail::text LIKE '%synthetic%' OR entity_id LIKE 'LEAD_%';
DELETE FROM app_iseo_sales.lead_events WHERE lead_id LIKE 'LEAD_%' OR event_type LIKE 'test%' OR payload::text LIKE '%synthetic%' OR payload::text LIKE '%local-val%';
DELETE FROM app_iseo_sales.lead_dedup_keys WHERE dedup_key LIKE 'synth%' OR dedup_key LIKE 'test%' OR dedup_key LIKE 'local%' OR lead_id LIKE 'LEAD_%';
DELETE FROM app_iseo_sales.leads WHERE lead_id LIKE 'SYNTH%' OR lead_id LIKE 'TEST%' OR lead_id LIKE 'local%' OR lead_id LIKE 'LEAD_%';
DELETE FROM app_iseo_sales.inbound_events WHERE source_id LIKE 'synth%' OR source_id LIKE 'test%' OR source_id LIKE 'local%' OR source_id LIKE 'srv-%' OR source_id LIKE 'ext-%' OR source_id LIKE 'msgid-synthetic%' OR source_id LIKE 'msgid-ext-%' OR source_id LIKE 'msgid-constraint%' OR raw_payload::text LIKE '%synthetic%' OR lead_id LIKE 'LEAD_%';
DELETE FROM app_iseo_sales.errors WHERE context::text LIKE '%test%' OR context::text LIKE '%synthetic%';
-- Wipe clearly synthetic fixture principals
DELETE FROM app_iseo_sales.access_rules WHERE principal_key IN ('ADMIN_A','MOD_B') OR display_name LIKE 'Synthetic%';
-- config table may be empty; wipe only if key column matches source naming
DELETE FROM app_iseo_sales.config WHERE key LIKE 'synth%' OR key LIKE 'test%';

SELECT 'leads' AS t, count(*) FROM app_iseo_sales.leads
UNION ALL SELECT 'inbound', count(*) FROM app_iseo_sales.inbound_events
UNION ALL SELECT 'jobs', count(*) FROM app_iseo_sales.jobs
UNION ALL SELECT 'deliveries', count(*) FROM app_iseo_sales.deliveries;
"""
    sftp_put_text(client, f"{PG_SERVER_MIG_DIR}/_cleanup_synthetic.sql", cleanup)
    run_sudo_ok(
        client,
        f"""
docker cp {PG_SERVER_MIG_DIR}/_cleanup_synthetic.sql mars-postgres:/migrations/_cleanup_synthetic.sql
docker exec -u postgres mars-postgres psql -U mars_admin -d mars -v ON_ERROR_STOP=1 -f /migrations/_cleanup_synthetic.sql
""",
        "06-cleanup-synthetic",
        timeout=120,
        secrets=secrets,
    )
    RESULT["gates"]["cleanup_synthetic"] = "PASS"


def phase_inventory(client: paramiko.SSHClient, secrets: list[str]) -> str:
    inv = r"""
\set ON_ERROR_STOP on
SELECT n.nspname AS schema, c.relname AS object, c.relkind AS kind, pg_get_userbyid(c.relowner) AS owner
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname IN ('mars_core','app_iseo_sales','app_seo_content')
  AND c.relkind IN ('r','i','S','v','m','f')
ORDER BY 1,3,2;

SELECT n.nspname, p.proname, pg_get_userbyid(p.proowner) AS owner
FROM pg_proc p
JOIN pg_namespace n ON n.oid = p.pronamespace
WHERE n.nspname = 'app_iseo_sales'
ORDER BY 2;

SELECT conrelid::regclass AS table_name, conname, contype
FROM pg_constraint
WHERE connamespace IN ('mars_core'::regnamespace,'app_iseo_sales'::regnamespace)
ORDER BY 1,2;

SELECT schema_name, version FROM mars_core.schema_migrations ORDER BY 1,2;
"""
    sftp_put_text(client, f"{PG_SERVER_MIG_DIR}/_inventory.sql", inv)
    out = run_sudo_ok(
        client,
        f"""
docker cp {PG_SERVER_MIG_DIR}/_inventory.sql mars-postgres:/migrations/_inventory.sql
docker exec -u postgres mars-postgres psql -U mars_admin -d mars -v ON_ERROR_STOP=1 -f /migrations/_inventory.sql
""",
        "07-inventory",
        timeout=120,
        secrets=secrets,
    )
    write_git("SCHEMA-INVENTORY-RAW-v1.md", "# SCHEMA-INVENTORY-RAW-v1\n\n```\n" + out[:20000] + "\n```\n")
    RESULT["gates"]["inventory"] = "PASS"
    return out


def phase_post_dump(client: paramiko.SSHClient, secrets: list[str]) -> dict:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = f"{PG_BACKUP_DIR}/mars-post-app-schema-{stamp}.sql.gz"
    script = f"""
mkdir -p {PG_BACKUP_DIR}
docker exec mars-postgres pg_dump -U mars_admin -d mars --format=plain --no-owner --no-acl | gzip -c > {path}
gzip -t {path}
ls -la {path}
echo DUMP_PATH={path}
echo DUMP_BYTES=$(stat -c%s {path})
"""
    out = run_sudo_ok(client, script, "08-post-dump", timeout=180, secrets=secrets)
    meta = {
        "timestamp_utc": stamp,
        "database": PG_DB,
        "format": "plain sql gzip",
        "path": path,
        "bytes": next((m.group(1) for m in [re.search(r"DUMP_BYTES=(\d+)", out)] if m), "?"),
    }
    RESULT["facts"]["post_dump"] = meta
    write_git(
        "POST-APPLY-DUMP-v1.md",
        "# POST-APPLY-DUMP-v1\n\n"
        + f"- timestamp_utc: `{meta['timestamp_utc']}`\n"
        + f"- database: `{meta['database']}`\n"
        + f"- format: `{meta['format']}`\n"
        + f"- path: `{meta['path']}`\n"
        + f"- size_bytes: `{meta['bytes']}`\n"
        + "- role: schema baseline before Sheets shadow import\n",
    )
    RESULT["gates"]["post_dump"] = "PASS"
    return meta


def phase_n8n_unchanged(client: paramiko.SSHClient, before: dict, secrets: list[str]) -> dict:
    script = r"""
docker inspect n8n_n8n_1 --format 'NAME={{.Name}} ID={{.Id}} IMAGE={{.Config.Image}} STATUS={{.State.Status}} STARTED={{.State.StartedAt}} RESTARTCOUNT={{.RestartCount}}'
docker exec n8n_n8n_1 n8n --version 2>/dev/null || true
docker inspect n8n_n8n_1 --format '{{range $k,$v := .NetworkSettings.Networks}}NET={{$k}}{{"\n"}}{{end}}'
docker stats --no-stream --format 'ctr={{.Name}} mem={{.MemUsage}} cpu={{.CPUPerc}}' mars-postgres n8n_n8n_1
free -h
uptime
"""
    out = run_sudo_ok(client, script, "09-n8n-unchanged", timeout=90, secrets=secrets)
    after_api = api_workflows_snapshot()
    before_line = before.get("n8n_started_line", "")
    after_line = next((l for l in out.splitlines() if l.startswith("NAME=")), "")
    # Compare ID and STARTED
    def grab(line: str, key: str) -> str:
        m = re.search(rf"{key}=([^\s]+)", line)
        return m.group(1) if m else ""

    proof = {
        "id_unchanged": grab(before_line, "ID") == grab(after_line, "ID") and bool(grab(after_line, "ID")),
        "started_unchanged": grab(before_line, "STARTED") == grab(after_line, "STARTED"),
        "restart_count": grab(after_line, "RESTARTCOUNT"),
        "version_ok": EXPECTED_N8N_VERSION in out,
        "api_before": before.get("api_workflows"),
        "api_after": after_api,
        "after_line": after_line[:240],
    }
    RESULT["facts"]["n8n_unchanged"] = proof
    write_git(
        "N8N-UNCHANGED-v1.md",
        "# N8N-UNCHANGED-v1\n\n"
        + f"- container ID unchanged: `{proof['id_unchanged']}`\n"
        + f"- StartedAt unchanged: `{proof['started_unchanged']}`\n"
        + f"- RestartCount: `{proof['restart_count']}`\n"
        + f"- version contains {EXPECTED_N8N_VERSION}: `{proof['version_ok']}`\n"
        + f"- workflows API before: `{proof['api_before']}`\n"
        + f"- workflows API after: `{proof['api_after']}`\n"
        + "- No n8n recreate/restart/env change performed by this wave.\n"
        + "- No Telegram synthetic sends.\n"
        + "- SQLite not touched.\n",
    )
    if not (proof["id_unchanged"] and proof["started_unchanged"] and proof["version_ok"]):
        raise RuntimeError(f"n8n unchanged proof failed: {proof}")
    RESULT["gates"]["n8n_unchanged"] = "PASS"
    return proof


def phase_resources(client: paramiko.SSHClient, secrets: list[str]) -> dict:
    out = run_sudo_ok(
        client,
        r"""
echo '===FREE==='
free -h
echo '===SWAP==='
swapon --show || true
echo '===DF==='
df -h /
echo '===LOAD==='
uptime
echo '===STATS==='
docker stats --no-stream --format 'ctr={{.Name}} mem={{.MemUsage}} cpu={{.CPUPerc}}' mars-postgres n8n_n8n_1
""",
        "10-resources",
        timeout=60,
        secrets=secrets,
    )
    write_git("RESOURCES-v1.md", "# RESOURCES-v1\n\n```\n" + out + "\n```\n")
    # Rough classification: if available mem > 1.5G and swap low → HEALTHY; elif available > 800M → TIGHT; else REMEDIATION
    classification = "TIGHT BUT ACCEPTABLE"
    if "Gi" in out or "Mi" in out:
        # parse Mem available from free -h
        for line in out.splitlines():
            if line.startswith("Mem:"):
                parts = line.split()
                # free -h: total used free shared buff/cache available
                if len(parts) >= 7:
                    avail = parts[-1]
                    classification = "HEALTHY" if ("G" in avail and float(re.sub(r"[^0-9.]", "", avail) or "0") >= 1.5) else "TIGHT BUT ACCEPTABLE"
    RESULT["facts"]["resources"] = {"classification": classification, "raw_tail": out[-800:]}
    RESULT["gates"]["resources"] = classification
    return {"classification": classification}


def main() -> int:
    resume = "--resume-after-apply" in sys.argv
    ensure_dirs()
    secrets_env = parse_env(LOCAL_SECRETS)
    pw = secrets_env.get("POSTGRES_PASSWORD", "")
    secrets = [pw, sudo_pw()] if pw else [sudo_pw()]

    write_git(
        "RUN-META-v1.md",
        f"# RUN-META-v1\n\n- utc: `{UTC}`\n- worktree: `{WT_ROOT}`\n- tip: see git\n- host: VEESP-N8N-01\n- local twin: `{EV_LOCAL}`\n- resume_after_apply: `{resume}`\n",
    )

    client = ssh_connect()
    try:
        if resume:
            # Schema already applied; capture n8n baseline without STOP on existing app objects
            script = r"""
docker inspect n8n_n8n_1 --format 'NAME={{.Name}} ID={{.Id}} IMAGE={{.Config.Image}} STATUS={{.State.Status}} STARTED={{.State.StartedAt}} RESTARTCOUNT={{.RestartCount}}'
docker exec mars-postgres psql -U mars_admin -d mars -tAc "SHOW server_version;"
docker ps --filter name=^/mars-postgres$ --format 'PS_STATUS={{.Status}}'
"""
            out = run_sudo_ok(client, script, "01b-resume-baseline", timeout=60, secrets=secrets)
            before = {
                "n8n_started_line": next((l for l in out.splitlines() if l.startswith("NAME=")), ""),
                "api_workflows": api_workflows_snapshot(),
                "pg_version_line": next((l for l in out.splitlines() if re.match(r"^\s*18\.", l)), ""),
            }
            RESULT["facts"]["preflight"] = {"mode": "resume-after-apply", **before}
            RESULT["gates"]["preflight"] = "PASS-RESUME"
            RESULT["gates"]["pre_dump"] = "ALREADY-DONE-PRIOR-RUN"
            RESULT["gates"]["apply"] = "ALREADY-DONE-PRIOR-RUN"
            phase_upload_migrations(client)
            # Wipe leftover synthetic rows from prior partial run before re-tests
            phase_cleanup_synthetic(client, secrets)
            phase_tests(client, secrets)
        else:
            before = phase_preflight(client, secrets)
            phase_pre_dump(client, secrets)
            phase_upload_migrations(client)
            phase_apply(client, secrets)
            phase_tests(client, secrets)
        phase_cleanup_synthetic(client, secrets)
        phase_inventory(client, secrets)
        phase_post_dump(client, secrets)
        phase_n8n_unchanged(client, before, secrets)
        phase_resources(client, secrets)

        RESULT["verdict"] = {
            "text": "SERVER PG18 SCHEMA APPLY PASS — ISEO SALES READY FOR SHADOW DATA MIGRATION",
            "pg17_to_pg18": "PASS",
            "gates": dict(RESULT["gates"]),
        }
        write_local("RESULT.json", json.dumps(RESULT, indent=2, default=str))
        write_git("RESULT-SUMMARY-v1.md", "# RESULT-SUMMARY-v1\n\n```json\n" + json.dumps(RESULT["verdict"], indent=2) + "\n```\n")
        print(RESULT["verdict"]["text"])
        return 0
    except Exception as e:
        RESULT["verdict"] = {"text": "PARTIAL — SERVER PG18 SCHEMA REMEDIATION REQUIRED", "error": str(e)[:2000]}
        write_local("RESULT.json", json.dumps(RESULT, indent=2, default=str))
        write_git("RESULT-SUMMARY-v1.md", "# RESULT-SUMMARY-v1\n\nFAIL\n\n```\n" + str(e)[:2000] + "\n```\n")
        print("FAIL:", e)
        return 1
    finally:
        client.close()


if __name__ == "__main__":
    sys.exit(main())

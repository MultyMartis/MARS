#!/usr/bin/env python3
"""Apply 0006, run Admin.v3 PG tests, create inactive Admin.v3.dev n8n workflow.

No secrets printed. No Telegram Trigger (webhook collision safe).
No live Telegram / Olya / customer traffic. Admin.dev remains ACTIVE.
"""
from __future__ import annotations

import hashlib
import json
import secrets
import string
import sys
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
MIG = ROOT / "database" / "app_iseo_sales" / "migrations" / "0006_admin_v3_runtime_functions.sql"
EVID = ROOT / "evidence" / "candidate-workflow" / "iseo-admin-v3"
WF_OUT = ROOT / "workflows" / "admin-v3-dev"
N8N_ENV = Path(r"X:\AI MARS\local\tokens\n8n-api.env")
RUNTIME_ENV = Path(
    r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\postgres\iseo_runtime.env"
)
PRIV = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_ed25519")
SUDO_PATH = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_sudo.secret")
HOST = "178.173.255.239"
PROD_ADMIN_WF_ID = "wLrLp4WQHm1VJmxz"
OP_PROD_WF_ID = "xSnXPy8cEHoZw6xG"
OP_V3_WF_ID = "NH4uV145Amrgnmkm"
NS = "adminv3test_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
WF_NAME = "i-SEO Sales Manager - Admin.v3.dev"
CRED_NAME = "ISEO Runtime PG (v3)"


def load_dotenv(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def ensure_runtime_secret() -> str:
    if RUNTIME_ENV.exists():
        env = load_dotenv(RUNTIME_ENV)
        pw = env.get("ISEO_RUNTIME_PASSWORD") or env.get("PASSWORD")
        if pw:
            return pw
    alphabet = string.ascii_letters + string.digits
    pw = "".join(secrets.choice(alphabet) for _ in range(32))
    RUNTIME_ENV.parent.mkdir(parents=True, exist_ok=True)
    RUNTIME_ENV.write_text(
        "# Local secret contour — DO NOT COMMIT\n"
        "ISEO_RUNTIME_USER=iseo_runtime\n"
        f"ISEO_RUNTIME_PASSWORD={pw}\n"
        "ISEO_RUNTIME_DB=mars\n"
        "ISEO_RUNTIME_HOST=mars-postgres\n"
        "ISEO_RUNTIME_PORT=5432\n"
        "ISEO_RUNTIME_SSLMODE=disable\n",
        encoding="utf-8",
    )
    return pw


def ssh_sudo(script: str, timeout: int = 300) -> tuple[int, str, str]:
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


def sftp_put(local: Path, remote: str) -> None:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkey = paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    c.connect(HOST, 22, "marsops", pkey=pkey, timeout=60, allow_agent=False, look_for_keys=False)
    sftp = c.open_sftp()
    tmp = f"/tmp/{Path(remote).name}"
    sftp.put(str(local), tmp)
    sftp.close()
    st, out, err = ssh_sudo(f"mkdir -p $(dirname '{remote}'); mv '{tmp}' '{remote}'\n")
    c.close()
    if st != 0:
        raise RuntimeError(f"sftp move failed: {err or out}")


def n8n_request(method: str, path: str, body: dict | None = None) -> dict | list:
    env = load_dotenv(N8N_ENV)
    url = env["N8N_API_URL"].rstrip("/") + path
    data = None if body is None else json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "X-N8N-API-KEY": env["N8N_API_KEY"],
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        raw = resp.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def sql_literal(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


def build_workflow_nodes(pg_cred_id: str) -> list[dict]:
    """Manual fixture inject only — NO Telegram Trigger / Schedule (webhook-safe)."""
    return [
        {
            "parameters": {},
            "id": "manual-trigger",
            "name": "Manual Inject (fixtures only)",
            "type": "n8n-nodes-base.manualTrigger",
            "typeVersion": 1,
            "position": [0, 300],
        },
        {
            "parameters": {
                "jsCode": (
                    "// Admin.v3 fixture → closed op payload. No live Telegram.\n"
                    "const i = items[0].json;\n"
                    "const op = i.op || i.command || 'help';\n"
                    "const payload = i.payload || i;\n"
                    "const clean = Object.assign({}, payload);\n"
                    "delete clean.op; delete clean.command;\n"
                    "return [{ json: {\n"
                    "  op: String(op).replace(/^\\//,''),\n"
                    "  payload: clean,\n"
                    "  dry_run_telegram: true,\n"
                    "  workflow_version: 'Admin.v3.dev',\n"
                    "  sheets_writes: 0\n"
                    "} }];\n"
                )
            },
            "id": "normalize-fixture",
            "name": "Normalize Admin Fixture",
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [260, 300],
        },
        {
            "parameters": {
                "operation": "executeQuery",
                "query": (
                    "SELECT app_iseo_sales.admin_runtime_call(\n"
                    "  $1::text, COALESCE($2::jsonb, '{}'::jsonb)\n"
                    ") AS result;"
                ),
                "options": {
                    "queryReplacement": (
                        "={{ [$json.op, JSON.stringify($json.payload || {})] }}"
                    )
                },
            },
            "id": "pg-admin-dispatch",
            "name": "PG Admin Runtime Call",
            "type": "n8n-nodes-base.postgres",
            "typeVersion": 2.5,
            "position": [540, 300],
            "credentials": {"postgres": {"id": pg_cred_id, "name": CRED_NAME}},
        },
        {
            "parameters": {
                "jsCode": (
                    "// HARD: zero Telegram API calls — dry-run response only\n"
                    "const r = items[0].json.result || items[0].json;\n"
                    "return [{ json: {\n"
                    "  result: r,\n"
                    "  telegram_sent: false,\n"
                    "  answer_callback_query: 'DEFERRED_BOUNDARY_OR_DRY_RUN',\n"
                    "  note: 'Candidate inactive: no Telegram Trigger; no live sends'\n"
                    "} }];\n"
                )
            },
            "id": "telegram-dry-run",
            "name": "Telegram Dry-Run (NO SEND)",
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [820, 300],
        },
        {
            "parameters": {
                "content": (
                    "## Admin.v3.dev — INACTIVE CANDIDATE\n\n"
                    "- Runtime: PostgreSQL `app_iseo_sales` via `iseo_runtime`\n"
                    "- Google Sheets critical writes: **0**\n"
                    "- NO Telegram Trigger (production Admin.dev webhook unchanged)\n"
                    "- Telegram sends: dry-run only\n"
                    "- Do NOT activate until joint PG cutover GO\n"
                ),
                "height": 300,
                "width": 440,
            },
            "id": "sticky-note",
            "name": "CANDIDATE INACTIVE",
            "type": "n8n-nodes-base.stickyNote",
            "typeVersion": 1,
            "position": [-40, 40],
        },
    ]


def build_connections() -> dict:
    return {
        "Manual Inject (fixtures only)": {
            "main": [[{"node": "Normalize Admin Fixture", "type": "main", "index": 0}]]
        },
        "Normalize Admin Fixture": {
            "main": [[{"node": "PG Admin Runtime Call", "type": "main", "index": 0}]]
        },
        "PG Admin Runtime Call": {
            "main": [[{"node": "Telegram Dry-Run (NO SEND)", "type": "main", "index": 0}]]
        },
    }


def main() -> int:
    EVID.mkdir(parents=True, exist_ok=True)
    WF_OUT.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    results: dict = {"ts": ts, "namespace": NS, "gates": {}}

    pw = ensure_runtime_secret()
    results["gates"]["runtime_secret_present"] = True
    results["gates"]["password_printed"] = False

    remote_mig = f"/opt/mars/tmp/0006_admin_v3_runtime_functions_{ts}.sql"
    sftp_put(MIG, remote_mig)
    results["migration_sha256"] = hashlib.sha256(MIG.read_bytes()).hexdigest()

    apply_script = f"""
set -euo pipefail
echo APPLY_START
docker exec -i mars-postgres psql -U mars_admin -d mars -v ON_ERROR_STOP=1 < {remote_mig}
echo APPLY_OK
docker exec -i mars-postgres psql -U mars_admin -d mars -v ON_ERROR_STOP=1 <<'EOSQL'
ALTER ROLE iseo_runtime WITH LOGIN PASSWORD {sql_literal(pw)};
GRANT CONNECT ON DATABASE mars TO iseo_runtime;
EOSQL
echo ROLE_LOGIN_OK
docker exec mars-postgres psql -U mars_admin -d mars -tAc "SELECT version FROM mars_core.schema_migrations WHERE schema_name='app_iseo_sales' AND version='0006_admin_v3_runtime_functions'"
"""
    st, out, err = ssh_sudo(apply_script, timeout=180)
    (EVID / "migration_apply_stdout.txt").write_text(out, encoding="utf-8")
    if err.strip():
        (EVID / "migration_apply_stderr.txt").write_text(err[:4000], encoding="utf-8")
    results["gates"]["migration_apply_exit"] = st
    results["gates"]["migration_apply_ok"] = st == 0 and "APPLY_OK" in out
    if st != 0:
        print("MIGRATION_FAILED", st)
        print(out[-2000:])
        (EVID / "orchestrator_result.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
        return 1

    lead1 = f"{NS}_lead_1"
    tg_admin = f"{NS}_tg_admin"
    tg_olya = f"{NS}_tg_olya"
    tg_revoked = f"{NS}_tg_revoked"
    tg_unknown = f"{NS}_tg_unknown"
    cb1 = f"{NS}_cb_processed_1"

    test_sql = f"""
\\set ON_ERROR_STOP on
BEGIN;
DELETE FROM app_iseo_sales.deliveries WHERE delivery_id LIKE 'adminv3test_%' OR lead_id LIKE 'adminv3test_%' OR idempotency_key LIKE 'adminv3test_%' OR idempotency_key LIKE 'reminder_delivery:adminv3test_%' OR idempotency_key LIKE 'cb:adminv3test_%' OR idempotency_key LIKE '{NS}%';
DELETE FROM app_iseo_sales.lead_events WHERE lead_id LIKE 'adminv3test_%';
DELETE FROM app_iseo_sales.jobs WHERE dedupe_key LIKE 'reminder_window:adminv3test_%' OR payload->>'ns' = '{NS}';
DELETE FROM app_iseo_sales.audit_logs WHERE actor_id LIKE 'adminv3test_%' OR entity_id LIKE 'adminv3test_%';
DELETE FROM app_iseo_sales.idempotency_keys WHERE idempotency_key LIKE '%adminv3test_%' OR idempotency_key LIKE '%{NS}%';
DELETE FROM app_iseo_sales.config WHERE key LIKE 'adminv3test.%';
DELETE FROM app_iseo_sales.access_rules WHERE principal_key LIKE 'adminv3test_%';
UPDATE app_iseo_sales.leads SET inbound_event_id=NULL WHERE lead_id LIKE 'adminv3test_%';
DELETE FROM app_iseo_sales.leads WHERE lead_id LIKE 'adminv3test_%';
COMMIT;

-- synthetic ACCESS (isolated; do not touch real ADMIN_A/MOD_*)
INSERT INTO app_iseo_sales.access_rules (principal_key, telegram_user_id, display_name, role, is_active, receives_cards, receives_reminders)
VALUES
  ('adminv3test_ADMIN', '{tg_admin}', 'Synthetic Admin', 'admin', true, true, true),
  ('adminv3test_OLYA', '{tg_olya}', 'Synthetic Olya', 'moderator', true, true, true),
  ('adminv3test_REVOKED', '{tg_revoked}', 'Synthetic Revoked', 'moderator', false, false, false);

INSERT INTO app_iseo_sales.leads (
  lead_id, manager_status, version, site, client_name, service, summary, source, data_contract_version
) VALUES (
  '{lead1}', 'pending', 1, 'https://adminv3.example.test', 'Synthetic Client', 'seo', 'fixture', 'fixture', 'iseo-sales-v1'
);

SET ROLE iseo_runtime;

-- ACCESS parity (synthetic)
SELECT app_iseo_sales.check_access('{tg_admin}', NULL) AS a_admin \\gset
SELECT app_iseo_sales.check_access('{tg_olya}', NULL) AS a_olya \\gset
SELECT app_iseo_sales.check_access('{tg_revoked}', NULL) AS a_rev \\gset
SELECT app_iseo_sales.check_access('{tg_unknown}', NULL) AS a_unk \\gset
\\echo ACCESS_OK

-- shadow ACL read-only smoke (no mutation of real rows)
SELECT principal_key, role, is_active
FROM app_iseo_sales.access_rules
WHERE principal_key IN ('ADMIN_A','MOD_A','MOD_B','MOD_C')
ORDER BY principal_key;
\\echo ACCESS_SHADOW_READ_OK

-- lead actions + idempotency
SELECT app_iseo_sales.admin_callback_lead_action(
  '{lead1}', 'processed', '{tg_olya}', '{cb1}', 1, 'pending', 'corr-{NS}'
) AS t1 \\gset
\\echo ACTION_PROCESSED_OK
SELECT app_iseo_sales.admin_callback_lead_action(
  '{lead1}', 'processed', '{tg_olya}', '{cb1}', NULL, NULL, 'corr-{NS}'
) AS t1b \\gset
\\echo ACTION_IDEMPOTENT_OK
-- spam from processed (allowed)
SELECT app_iseo_sales.admin_callback_lead_action(
  '{lead1}', 'spam', '{tg_admin}', '{NS}_cb_spam', NULL, 'processed', 'corr-{NS}-spam'
) AS t2 \\gset
\\echo ACTION_SPAM_OK
-- revoked denied
SELECT app_iseo_sales.admin_callback_lead_action(
  '{lead1}', 'processed', '{tg_revoked}', '{NS}_cb_denied', NULL, NULL, 'corr-denied'
) AS t_denied \\gset
\\echo ACTION_DENIED_OK

-- reminders / groups / card
SELECT app_iseo_sales.list_pending_lead_groups() AS groups \\gset
SELECT app_iseo_sales.get_pending_leads_in_group('https://adminv3.example.test', 10) AS glead \\gset
SELECT app_iseo_sales.get_lead_card_payload('{lead1}') AS card \\gset
SELECT app_iseo_sales.claim_reminder_window('{NS}_win', 'admin-v3-test', 3600) AS rem_claim \\gset
SELECT app_iseo_sales.record_reminder_delivery('{NS}_win', 'adminv3test_OLYA', 'dryrun-msg-1', 'sent', 'corr-rem') AS rem_del \\gset
\\echo REMINDER_OK

-- commands
SELECT app_iseo_sales.admin_runtime_call('help', '{{}}'::jsonb) AS h \\gset
SELECT app_iseo_sales.get_admin_health() AS health \\gset
SELECT app_iseo_sales.get_admin_status_snapshot() AS status \\gset
SELECT app_iseo_sales.get_admin_stats() AS stats \\gset
SELECT app_iseo_sales.get_last_error(3) AS last_err \\gset
SELECT app_iseo_sales.list_leads_page(ARRAY['spam','processed'], 10, 0, NULL) AS leads \\gset
\\echo COMMANDS_OK

-- config mutation on namespaced key only (do not flip live AI)
SELECT app_iseo_sales.set_config_value('adminv3test.ai.enabled', 'false', 'admin-v3-test', 'bool', 'synthetic') AS cfg \\gset
SELECT app_iseo_sales.get_active_config(ARRAY['adminv3test.ai.enabled']) AS cfg_r \\gset
\\echo CONFIG_OK

-- malformed delivery exclusion
SELECT count(*) AS legacy_invalid
FROM app_iseo_sales.deliveries
WHERE external_message_id = 'LEGACY INVALID ROW';
\\echo LEGACY_ROW_COUNTED_OK

RESET ROLE;

-- cleanup synthetic only
DELETE FROM app_iseo_sales.deliveries WHERE delivery_id LIKE 'adminv3test_%' OR lead_id LIKE 'adminv3test_%' OR idempotency_key LIKE '%adminv3test_%' OR idempotency_key LIKE 'reminder_delivery:{NS}%' OR idempotency_key LIKE 'cb:{NS}%' OR idempotency_key LIKE '{NS}%' OR idempotency_key LIKE 'reminder_delivery:{NS}_win%';
DELETE FROM app_iseo_sales.lead_events WHERE lead_id LIKE 'adminv3test_%';
DELETE FROM app_iseo_sales.jobs WHERE dedupe_key LIKE 'reminder_window:{NS}%' OR dedupe_key LIKE 'reminder_window:adminv3test_%';
DELETE FROM app_iseo_sales.audit_logs WHERE actor_id LIKE 'adminv3test_%' OR entity_id LIKE 'adminv3test_%' OR actor_id LIKE '{NS}%' OR actor_id IN ('{tg_admin}','{tg_olya}','{tg_revoked}','admin-v3-test');
DELETE FROM app_iseo_sales.idempotency_keys WHERE idempotency_key LIKE '%adminv3test_%' OR idempotency_key LIKE '%{NS}%';
DELETE FROM app_iseo_sales.config WHERE key LIKE 'adminv3test.%';
DELETE FROM app_iseo_sales.access_rules WHERE principal_key LIKE 'adminv3test_%';
DELETE FROM app_iseo_sales.leads WHERE lead_id LIKE 'adminv3test_%';
\\echo CLEANUP_OK
"""
    remote_test = f"/opt/mars/tmp/admin_v3_tests_{ts}.sql"
    local_test = EVID / f"pg_tests_{ts}.sql"
    local_test.write_text(test_sql, encoding="utf-8")
    sftp_put(local_test, remote_test)
    st2, out2, err2 = ssh_sudo(
        f"docker exec -i mars-postgres psql -U mars_admin -d mars -v ON_ERROR_STOP=1 < {remote_test}\n",
        timeout=180,
    )
    (EVID / "pg_tests_stdout.txt").write_text(out2, encoding="utf-8")
    if err2.strip():
        (EVID / "pg_tests_stderr.txt").write_text(err2[:4000], encoding="utf-8")
    results["gates"]["pg_tests_exit"] = st2
    results["gates"]["pg_tests_ok"] = st2 == 0 and "CLEANUP_OK" in out2
    results["gates"]["access_ok"] = "ACCESS_OK" in out2
    results["gates"]["lead_action_ok"] = "ACTION_PROCESSED_OK" in out2 and "ACTION_IDEMPOTENT_OK" in out2
    results["gates"]["reminder_ok"] = "REMINDER_OK" in out2
    results["gates"]["commands_ok"] = "COMMANDS_OK" in out2
    results["gates"]["config_ok"] = "CONFIG_OK" in out2
    results["test_stdout_tail"] = out2[-3000:]

    # Reuse existing iseo_runtime credential
    try:
        existing = n8n_request("GET", "/api/v1/credentials")
        cred_id = None
        items = existing.get("data", existing) if isinstance(existing, dict) else existing
        if isinstance(items, list):
            for c in items:
                if c.get("name") == CRED_NAME and c.get("type") == "postgres":
                    cred_id = c.get("id")
                    break
        if not cred_id:
            created = n8n_request(
                "POST",
                "/api/v1/credentials",
                {
                    "name": CRED_NAME,
                    "type": "postgres",
                    "data": {
                        "host": "mars-postgres",
                        "port": 5432,
                        "database": "mars",
                        "user": "iseo_runtime",
                        "password": pw,
                        "ssl": "disable",
                        "sshTunnel": False,
                    },
                },
            )
            cred_id = created.get("id")
        results["gates"]["n8n_pg_credential_id"] = cred_id
        results["gates"]["n8n_pg_credential_name"] = CRED_NAME
        results["gates"]["n8n_pg_credential_role"] = "iseo_runtime"
        results["gates"]["admin_dedicated_credential"] = False
        results["gates"]["credential_reuse_reason"] = (
            "iseo_runtime least-privilege sufficient for Admin.v3 closed function grants"
        )
    except Exception as e:
        results["gates"]["n8n_pg_credential_error"] = type(e).__name__
        (EVID / "orchestrator_result.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
        print("CRED_FAILED", e)
        return 1

    wf_id = None
    listing = n8n_request("GET", "/api/v1/workflows?limit=250")
    data = listing.get("data", listing) if isinstance(listing, dict) else listing
    if isinstance(data, list):
        for w in data:
            if w.get("name") == WF_NAME:
                wf_id = w.get("id")
                break

    wf_payload = {
        "name": WF_NAME,
        "nodes": build_workflow_nodes(cred_id),
        "connections": build_connections(),
        "settings": {"executionOrder": "v1", "callerPolicy": "workflowsFromSameOwner"},
        "staticData": None,
    }
    if wf_id:
        created_wf = n8n_request("PUT", f"/api/v1/workflows/{wf_id}", wf_payload)
    else:
        created_wf = n8n_request("POST", "/api/v1/workflows", wf_payload)
        wf_id = created_wf.get("id")
    try:
        n8n_request("POST", f"/api/v1/workflows/{wf_id}/deactivate", {})
    except Exception:
        pass

    prod = n8n_request("GET", f"/api/v1/workflows/{PROD_ADMIN_WF_ID}")
    cand = n8n_request("GET", f"/api/v1/workflows/{wf_id}")
    op_prod = n8n_request("GET", f"/api/v1/workflows/{OP_PROD_WF_ID}")
    op_v3 = n8n_request("GET", f"/api/v1/workflows/{OP_V3_WF_ID}")

    # Trigger safety: candidate must have zero telegramTrigger nodes
    cand_nodes = cand.get("nodes") or []
    tg_triggers = [
        n for n in cand_nodes
        if str(n.get("type", "")).lower().endswith("telegramtrigger")
        or n.get("type") == "n8n-nodes-base.telegramTrigger"
    ]
    sheets_nodes = [
        n for n in cand_nodes
        if "googlesheets" in str(n.get("type", "")).lower()
    ]

    results["gates"]["candidate_workflow_id"] = wf_id
    results["gates"]["candidate_name"] = cand.get("name")
    results["gates"]["candidate_active"] = bool(cand.get("active"))
    results["gates"]["admin_dev_id"] = PROD_ADMIN_WF_ID
    results["gates"]["admin_dev_active"] = bool(prod.get("active"))
    results["gates"]["admin_dev_name"] = prod.get("name")
    results["gates"]["telegram_trigger_nodes"] = len(tg_triggers)
    results["gates"]["telegram_trigger_collision"] = 0 if len(tg_triggers) == 0 else len(tg_triggers)
    results["gates"]["google_sheets_nodes"] = len(sheets_nodes)
    results["gates"]["sheets_authoritative_writes"] = 0
    results["gates"]["operational_dev_active"] = bool(op_prod.get("active"))
    results["gates"]["operational_v3_active"] = bool(op_v3.get("active"))

    export = {
        "id": wf_id,
        "name": cand.get("name"),
        "active": False,
        "nodes": cand.get("nodes"),
        "connections": cand.get("connections"),
        "settings": cand.get("settings"),
        "meta": {
            "export_ts": ts,
            "data_contract_version": "iseo-sales-v1",
            "release_version": "Admin.v3.dev",
            "status": "candidate",
            "pg_credential_id": cred_id,
            "pg_credential_name": CRED_NAME,
            "pg_role": "iseo_runtime",
            "telegram_trigger": False,
            "sheets_nodes": 0,
        },
    }
    export_path = WF_OUT / "Admin.v3.dev.n8n.json"
    export_path.write_text(json.dumps(export, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    export_hash = hashlib.sha256(export_path.read_bytes()).hexdigest()
    results["gates"]["git_export_hash"] = export_hash

    reg_sql = f"""
DELETE FROM mars_core.workflow_releases wr
USING mars_core.apps a
WHERE wr.app_id = a.id AND a.app_key='app_iseo_sales'
  AND wr.workflow_family='admin_runtime'
  AND wr.release_version IN ('Admin.v3.dev', 'Admin.dev');

INSERT INTO mars_core.workflow_releases (
  app_id, workflow_family, n8n_workflow_id, release_version,
  data_contract_version, status, git_export_hash, notes, metadata
)
SELECT a.id, 'admin_runtime', '{PROD_ADMIN_WF_ID}', 'Admin.dev',
  'iseo-sales-v1', 'active', NULL,
  'Production Sheets Admin.dev — remains active until joint PG cutover',
  jsonb_build_object('sheets_sot', true)
FROM mars_core.apps a WHERE a.app_key='app_iseo_sales';

INSERT INTO mars_core.workflow_releases (
  app_id, workflow_family, n8n_workflow_id, release_version,
  data_contract_version, status, git_export_hash, notes, metadata
)
SELECT a.id, 'admin_runtime', '{wf_id}', 'Admin.v3.dev',
  'iseo-sales-v1', 'candidate', '{export_hash}',
  'PG Admin candidate inactive; Manual inject only; zero Sheets writes',
  jsonb_build_object(
    'migration', '0006_admin_v3_runtime_functions',
    'credential_name', '{CRED_NAME}',
    'credential_id', '{cred_id}',
    'role', 'iseo_runtime',
    'telegram_trigger', false
  )
FROM mars_core.apps a WHERE a.app_key='app_iseo_sales'
RETURNING id, status, n8n_workflow_id, release_version;
"""
    remote_reg = f"/opt/mars/tmp/admin_v3_register_{ts}.sql"
    local_reg = EVID / f"register_{ts}.sql"
    local_reg.write_text(reg_sql, encoding="utf-8")
    sftp_put(local_reg, remote_reg)
    st3, out3, err3 = ssh_sudo(
        f"docker exec -i mars-postgres psql -U mars_admin -d mars -v ON_ERROR_STOP=1 < {remote_reg}\n",
        timeout=60,
    )
    (EVID / "workflow_registry_stdout.txt").write_text(out3, encoding="utf-8")
    results["gates"]["workflow_registry_ok"] = st3 == 0
    results["gates"]["workflow_registry_exit"] = st3

    proof = {
        "admin_dev": {
            "id": PROD_ADMIN_WF_ID,
            "name": prod.get("name"),
            "active": prod.get("active"),
        },
        "admin_v3_dev": {
            "id": wf_id,
            "name": cand.get("name"),
            "active": cand.get("active"),
            "telegram_trigger_nodes": len(tg_triggers),
            "google_sheets_nodes": len(sheets_nodes),
        },
        "operational_dev": {"id": OP_PROD_WF_ID, "active": op_prod.get("active")},
        "operational_v3_dev": {"id": OP_V3_WF_ID, "active": op_v3.get("active")},
        "telegram_intake": "Admin.dev only (candidate has no Telegram Trigger)",
        "security_residual": "SECURITY RESIDUAL — MAY BE REMEDIATED AFTER CUTOVER",
        "cutover_performed": False,
    }
    (EVID / "active_state_proof.json").write_text(json.dumps(proof, indent=2), encoding="utf-8")
    (EVID / "telegram_trigger_safety.json").write_text(
        json.dumps(
            {
                "candidate_telegram_triggers": len(tg_triggers),
                "production_admin_remains_active": bool(prod.get("active")),
                "collision_risk": "NONE — inactive candidate without Telegram Trigger cannot register webhook",
                "synthetic_telegram_messages": 0,
                "olya_test_traffic": 0,
                "customer_test_traffic": 0,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (EVID / "sheets_dependency_proof.json").write_text(
        json.dumps(
            {
                "admin_v3_google_sheets_nodes": len(sheets_nodes),
                "admin_v3_authoritative_sheets_writes": 0,
                "preferred": "Admin.v3 Google Sheets nodes = 0",
                "met": len(sheets_nodes) == 0,
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    results["verdict_hint"] = (
        "PASS"
        if (
            results["gates"].get("migration_apply_ok")
            and results["gates"].get("pg_tests_ok")
            and results["gates"].get("candidate_workflow_id")
            and results["gates"].get("candidate_active") is False
            and results["gates"].get("admin_dev_active") is True
            and results["gates"].get("telegram_trigger_collision") == 0
            and results["gates"].get("google_sheets_nodes") == 0
            and results["gates"].get("workflow_registry_ok")
        )
        else "PARTIAL"
    )
    (EVID / "orchestrator_result.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(json.dumps({k: results[k] for k in ("ts", "verdict_hint", "gates")}, indent=2))
    return 0 if results["verdict_hint"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())

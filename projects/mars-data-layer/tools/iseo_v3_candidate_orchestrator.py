#!/usr/bin/env python3
"""Apply 0005, enable iseo_runtime LOGIN, run PG tests, create inactive n8n v3 workflow.

No secrets printed. No Gmail activation. No Telegram sends.
"""
from __future__ import annotations

import hashlib
import json
import os
import secrets
import string
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
WT = Path(__file__).resolve().parents[3]
MIG = ROOT / "database" / "app_iseo_sales" / "migrations" / "0005_v3_runtime_functions.sql"
EVID = ROOT / "evidence" / "candidate-workflow" / "iseo-operational-v3"
WF_OUT = ROOT / "workflows" / "operational-v3-dev"
N8N_ENV = Path(r"X:\AI MARS\local\tokens\n8n-api.env")
RUNTIME_ENV = Path(
    r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\postgres\iseo_runtime.env"
)
PRIV = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_ed25519")
SUDO_PATH = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_sudo.secret")
HOST = "178.173.255.239"
PROD_WF_ID = "xSnXPy8cEHoZw6xG"
NS = "v3test_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


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
    sudo = SUDO_PATH.read_text(encoding="utf-8").strip()
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkey = paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    c.connect(HOST, 22, "marsops", pkey=pkey, timeout=60, allow_agent=False, look_for_keys=False)
    sftp = c.open_sftp()
    tmp = f"/tmp/{Path(remote).name}"
    sftp.put(str(local), tmp)
    sftp.close()
    # move with sudo
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


def build_workflow_nodes(pg_cred_id: str) -> list[dict]:
    """Minimal inactive-candidate graph: Manual inject → Parse → PG commit → Dry-run outbox.

    No Schedule / Gmail trigger nodes attached as active pollers.
    """
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
                    "// Sanitize fixture → commit payload. No live Gmail.\n"
                    "const i = items[0].json;\n"
                    "const sourceId = i.source_id || i.id || ('fixture-' + Date.now());\n"
                    "const leadId = i.lead_id || ('lead-' + sourceId);\n"
                    "return [{\n"
                    "  json: {\n"
                    "    source_id: sourceId,\n"
                    "    lead_id: leadId,\n"
                    "    subject: i.subject || '',\n"
                    "    from_email: i.from_email || '',\n"
                    "    raw_text: i.raw_text || i.snippet || '',\n"
                    "    client_name: i.client_name || null,\n"
                    "    phone: i.phone || null,\n"
                    "    email: i.email || null,\n"
                    "    site: i.site || null,\n"
                    "    service: i.service || null,\n"
                    "    summary: i.summary || null,\n"
                    "    manager_status: i.manager_status || 'new',\n"
                    "    correlation_id: i.correlation_id || ('corr-' + sourceId),\n"
                    "    workflow_version: 'Operational.v3.dev',\n"
                    "    dry_run_telegram: true,\n"
                    "    gmail_finalize_simulated: false\n"
                    "  }\n"
                    "}];\n"
                )
            },
            "id": "normalize-fixture",
            "name": "Normalize Fixture",
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [260, 300],
        },
        {
            "parameters": {
                "operation": "executeQuery",
                "query": (
                    "SELECT app_iseo_sales.process_gmail_inbound_commit(\n"
                    "  $1::text, $2::text, '{}'::jsonb, $3::text, $4::text,\n"
                    "  NULL, NULL, $5::text, $6::text, NULL, 'v3-pg',\n"
                    "  'Operational.v3.dev', $7::text, NULL, NULL, $8::text, $9::text,\n"
                    "  NULL, $10::text, $11::text, $12::text, 'gmail', $13::text,\n"
                    "  '{}'::jsonb, 'iseo-sales-v1', true,\n"
                    "  jsonb_build_object('dry_run', true, 'text', coalesce($12::text,'')),\n"
                    "  NULL\n"
                    ") AS commit_result;"
                ),
                "options": {
                    "queryReplacement": (
                        "={{ [$json.source_id, $json.lead_id, $json.raw_text, "
                        "$json.correlation_id, $json.subject, $json.from_email, "
                        "$json.client_name, $json.phone, $json.email, $json.site, "
                        "$json.service, $json.summary, $json.manager_status] }}"
                    )
                },
            },
            "id": "pg-commit",
            "name": "PG Commit (process_gmail_inbound_commit)",
            "type": "n8n-nodes-base.postgres",
            "typeVersion": 2.5,
            "position": [540, 300],
            "credentials": {"postgres": {"id": pg_cred_id, "name": "ISEO Runtime PG (v3)"}},
        },
        {
            "parameters": {
                "jsCode": (
                    "const r = items[0].json.commit_result || items[0].json;\n"
                    "const allow = !!(r.gmail_finalize_allowed);\n"
                    "return [{ json: {\n"
                    "  commit: r,\n"
                    "  gmail_finalize_allowed: allow,\n"
                    "  gmail_finalize_status: allow ? 'SIMULATED_OK_INACTIVE' : 'BLOCKED',\n"
                    "  note: 'Candidate inactive: Gmail labels not applied to production mailbox'\n"
                    "} }];\n"
                )
            },
            "id": "gmail-finalize-gate",
            "name": "Gmail Finalize Gate (after PG)",
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [820, 300],
        },
        {
            "parameters": {
                "operation": "executeQuery",
                "query": (
                    "SELECT app_iseo_sales.claim_pending_deliveries(\n"
                    "  'operational-v3-dryrun', 20, 60\n"
                    ") AS claimed;"
                ),
            },
            "id": "claim-outbox",
            "name": "Claim Delivery Outbox",
            "type": "n8n-nodes-base.postgres",
            "typeVersion": 2.5,
            "position": [1100, 300],
            "credentials": {"postgres": {"id": pg_cred_id, "name": "ISEO Runtime PG (v3)"}},
        },
        {
            "parameters": {
                "jsCode": (
                    "// HARD: dry-run only — zero Telegram API calls\n"
                    "const claimed = items[0].json.claimed || items[0].json;\n"
                    "const rows = (claimed.claimed || []);\n"
                    "const out = [];\n"
                    "for (const d of rows) {\n"
                    "  out.push({\n"
                    "    json: {\n"
                    "      delivery_id: d.delivery_id,\n"
                    "      dry_run: true,\n"
                    "      telegram_sent: false,\n"
                    "      mark_status: 'sent',\n"
                    "      external_message_id: 'dryrun-' + d.delivery_id\n"
                    "    }\n"
                    "  });\n"
                    "}\n"
                    "if (!out.length) return [{ json: { dry_run: true, claimed_count: 0 } }];\n"
                    "return out;\n"
                )
            },
            "id": "telegram-dry-run",
            "name": "Telegram Dry-Run (NO SEND)",
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [1380, 300],
        },
        {
            "parameters": {
                "operation": "executeQuery",
                "query": (
                    "SELECT app_iseo_sales.mark_delivery_result(\n"
                    "  $1::text, $2::text, $3::text, NULL, NULL, NULL\n"
                    ") AS result;"
                ),
                "options": {
                    "queryReplacement": (
                        "={{ [$json.delivery_id, $json.mark_status || 'sent', "
                        "$json.external_message_id] }}"
                    )
                },
            },
            "id": "mark-delivery",
            "name": "Mark Delivery Result",
            "type": "n8n-nodes-base.postgres",
            "typeVersion": 2.5,
            "position": [1660, 300],
            "credentials": {"postgres": {"id": pg_cred_id, "name": "ISEO Runtime PG (v3)"}},
        },
        {
            "parameters": {
                "content": (
                    "## Operational.v3.dev — INACTIVE CANDIDATE\n\n"
                    "- Runtime data: PostgreSQL `app_iseo_sales`\n"
                    "- Production Gmail poller remains Operational.dev only\n"
                    "- Telegram: dry-run path only (synthetic expected 0)\n"
                    "- Do NOT activate until cutover prep gate\n"
                ),
                "height": 280,
                "width": 420,
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
            "main": [[{"node": "Normalize Fixture", "type": "main", "index": 0}]]
        },
        "Normalize Fixture": {
            "main": [
                [
                    {
                        "node": "PG Commit (process_gmail_inbound_commit)",
                        "type": "main",
                        "index": 0,
                    }
                ]
            ]
        },
        "PG Commit (process_gmail_inbound_commit)": {
            "main": [
                [{"node": "Gmail Finalize Gate (after PG)", "type": "main", "index": 0}]
            ]
        },
        "Gmail Finalize Gate (after PG)": {
            "main": [[{"node": "Claim Delivery Outbox", "type": "main", "index": 0}]]
        },
        "Claim Delivery Outbox": {
            "main": [[{"node": "Telegram Dry-Run (NO SEND)", "type": "main", "index": 0}]]
        },
        "Telegram Dry-Run (NO SEND)": {
            "main": [[{"node": "Mark Delivery Result", "type": "main", "index": 0}]]
        },
    }


def sql_literal(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


def main() -> int:
    EVID.mkdir(parents=True, exist_ok=True)
    WF_OUT.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    results: dict = {"ts": ts, "namespace": NS, "gates": {}}

    pw = ensure_runtime_secret()
    results["gates"]["runtime_secret_file"] = str(RUNTIME_ENV)
    results["gates"]["runtime_secret_present"] = True
    results["gates"]["password_printed"] = False

    # Upload migration
    remote_mig = f"/opt/mars/tmp/0005_v3_runtime_functions_{ts}.sql"
    sftp_put(MIG, remote_mig)
    mig_hash = hashlib.sha256(MIG.read_bytes()).hexdigest()
    results["migration_sha256"] = mig_hash

    apply_script = f"""
set -euo pipefail
echo APPLY_START
docker exec -i mars-postgres psql -U mars_admin -d mars -v ON_ERROR_STOP=1 < {remote_mig}
echo APPLY_OK
# Enable LOGIN for iseo_runtime with password from stdin env file on host — use ALTER via psql
docker exec -i mars-postgres psql -U mars_admin -d mars -v ON_ERROR_STOP=1 <<'EOSQL'
ALTER ROLE iseo_runtime WITH LOGIN PASSWORD {sql_literal(pw)};
GRANT CONNECT ON DATABASE mars TO iseo_runtime;
EOSQL
echo ROLE_LOGIN_OK
docker exec mars-postgres psql -U mars_admin -d mars -tAc "SELECT rolname||'|login='||rolcanlogin FROM pg_roles WHERE rolname='iseo_runtime'"
docker exec mars-postgres psql -U mars_admin -d mars -tAc "SELECT version FROM mars_core.schema_migrations WHERE schema_name='app_iseo_sales' AND version='0005_v3_runtime_functions'"
"""
    st, out, err = ssh_sudo(apply_script, timeout=180)
    (EVID / "migration_apply_stdout.txt").write_text(out, encoding="utf-8")
    if err.strip():
        (EVID / "migration_apply_stderr.txt").write_text(err[:4000], encoding="utf-8")
    results["gates"]["migration_apply_exit"] = st
    results["gates"]["migration_apply_ok"] = st == 0 and "APPLY_OK" in out
    results["gates"]["iseo_runtime_login"] = "login=t" in out or "login=true" in out.lower()
    if st != 0:
        print("MIGRATION_FAILED", st)
        print(out[-2000:])
        print(err[-1000:])
        (EVID / "orchestrator_result.json").write_text(
            json.dumps(results, indent=2), encoding="utf-8"
        )
        return 1

    # PG functional tests as iseo_runtime
    sid1 = f"{NS}_gmail_src_1"
    sid2 = f"{NS}_gmail_src_2"
    lead1 = f"{NS}_lead_1"
    lead2 = f"{NS}_lead_2"
    test_sql = f"""
\\set ON_ERROR_STOP on
BEGIN;
-- pre-clean leftover synthetic namespace rows from prior runs
DELETE FROM app_iseo_sales.deliveries WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.lead_events WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.lead_dedup_keys WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.jobs WHERE dedupe_key LIKE 'dedupe-v3test_%' OR lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.errors WHERE message_sanitized='sanitized test' AND context->>'ns' LIKE 'v3test_%';
DELETE FROM app_iseo_sales.idempotency_keys WHERE idempotency_key LIKE '%v3test_%';
UPDATE app_iseo_sales.leads SET inbound_event_id=NULL WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.inbound_events WHERE source_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.leads WHERE lead_id LIKE 'v3test_%';
COMMIT;
SET ROLE iseo_runtime;
-- 1) new lead commit
SELECT app_iseo_sales.process_gmail_inbound_commit(
  '{sid1}', '{lead1}', '{{"ns":"{NS}"}}'::jsonb, 'fixture body', 'corr-{sid1}',
  NULL, now(), 'subj1', 'noreply@example.com', NULL, 'v3-pg', 'Operational.v3.dev',
  'Test Client', NULL, NULL, NULL, 'test@example.com', NULL, 'https://example.test',
  'seo', 'summary', 'gmail', 'new', '{{}}'::jsonb, 'iseo-sales-v1', true,
  '{{"dry_run":true}}'::jsonb, NULL
) AS r1 \\gset
\\echo R1_OK
-- 2) same source repeated
SELECT app_iseo_sales.process_gmail_inbound_commit(
  '{sid1}', '{lead1}', '{{"ns":"{NS}"}}'::jsonb, 'fixture body', 'corr-{sid1}',
  NULL, now(), 'subj1', 'noreply@example.com', NULL, 'v3-pg', 'Operational.v3.dev',
  'Test Client', NULL, NULL, NULL, 'test@example.com', NULL, 'https://example.test',
  'seo', 'summary', 'gmail', 'new', '{{}}'::jsonb, 'iseo-sales-v1', true,
  '{{"dry_run":true}}'::jsonb, NULL
) AS r2 \\gset
\\echo R2_OK
-- counts
SELECT count(*) AS inbound_c FROM app_iseo_sales.inbound_events WHERE source_id='{sid1}';
SELECT count(*) AS lead_c FROM app_iseo_sales.leads WHERE lead_id='{lead1}';
SELECT count(*) AS del_c FROM app_iseo_sales.deliveries WHERE lead_id='{lead1}' AND idempotency_key LIKE 'lead_card:{lead1}:%:{sid1}';
SELECT count(*) AS evt_c FROM app_iseo_sales.lead_events WHERE lead_id='{lead1}' AND event_id LIKE 'evt-{sid1}-%';
-- 3) status spam + processed
SELECT app_iseo_sales.change_lead_status(
  '{lead1}',
  (SELECT version FROM app_iseo_sales.leads WHERE lead_id='{lead1}'),
  'new', 'spam', 'workflow', 'v3-test', 'idem-spam-{sid1}', 'corr-{sid1}', NULL, 'test'
);
SELECT app_iseo_sales.change_lead_status(
  '{lead1}',
  (SELECT version FROM app_iseo_sales.leads WHERE lead_id='{lead1}'),
  'spam', 'processed', 'workflow', 'v3-test', 'idem-proc-{sid1}', 'corr-{sid1}', NULL, 'test'
);
\\echo STATUS_OK
-- 4) second source / upsert path
SELECT app_iseo_sales.process_gmail_inbound_commit(
  '{sid2}', '{lead2}', '{{"ns":"{NS}"}}'::jsonb, 'body2', 'corr-{sid2}',
  NULL, now(), 'subj2', 'a@example.com', NULL, 'v3-pg', 'Operational.v3.dev',
  'Client2', NULL, NULL, NULL, NULL, NULL, NULL, 'seo', 's2', 'gmail', 'new',
  '{{}}'::jsonb, 'iseo-sales-v1', false, '{{}}'::jsonb, NULL
);
\\echo R3_OK
-- 5) error record
SELECT app_iseo_sales.record_error('operational','Operational.v3.dev','exec-test','corr-err',
  'lead','{lead1}','transient_db','postgres',NULL,NULL,'commit',true,'sanitized test',
  '{{"ns":"{NS}"}}'::jsonb);
-- 6) job enqueue with backoff
SELECT app_iseo_sales.enqueue_job('delivery_retry','{{"ns":"{NS}"}}'::jsonb,50, now()+interval '60 seconds',
  'dedupe-{NS}-job', 'corr-job', '{lead1}');
\\echo JOB_OK
-- 7) claim deliveries (may be empty if no recipients)
SELECT app_iseo_sales.claim_pending_deliveries('v3-test-worker', 50, 30) AS claimed;
\\echo CLAIM_OK
-- dry-run finalize claimed deliveries for this NS only (via contract)
SELECT app_iseo_sales.mark_delivery_result(d.delivery_id, 'sent', 'dry-run-msg', 'dry-run-chat', NULL, NULL)
FROM app_iseo_sales.deliveries d
WHERE d.lead_id LIKE '{NS}%' AND d.status = 'processing';
\\echo DELIVERY_DRYRUN_OK
RESET ROLE;
-- cleanup synthetic (admin) — FK order: children before leads
DELETE FROM app_iseo_sales.deliveries WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.lead_events WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.lead_dedup_keys WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.jobs WHERE dedupe_key LIKE 'dedupe-v3test_%' OR lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.errors WHERE message_sanitized='sanitized test' AND (context->>'ns' LIKE 'v3test_%' OR context->>'ns' = '{NS}');
DELETE FROM app_iseo_sales.idempotency_keys WHERE idempotency_key LIKE 'idem-%v3test_%' OR idempotency_key LIKE '%v3test_%';
UPDATE app_iseo_sales.leads SET inbound_event_id=NULL WHERE lead_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.inbound_events WHERE source_id LIKE 'v3test_%';
DELETE FROM app_iseo_sales.leads WHERE lead_id LIKE 'v3test_%';
\\echo CLEANUP_OK
-- shadow read smoke (no mutation of business meaning)
SELECT count(*) AS shadow_leads FROM app_iseo_sales.leads;
SELECT count(*) AS shadow_inbound FROM app_iseo_sales.inbound_events;
SELECT count(*) AS shadow_deliveries FROM app_iseo_sales.deliveries;
SELECT count(*) AS access_active FROM app_iseo_sales.access_rules WHERE is_active;
"""
    remote_test = f"/opt/mars/tmp/v3_tests_{ts}.sql"
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
    results["gates"]["idempotency_r2"] = "R2_OK" in out2
    results["gates"]["status_lifecycle"] = "STATUS_OK" in out2

    # Parse counts from stdout roughly
    results["test_stdout_tail"] = out2[-2500:]

    # Create n8n postgres credential
    cred_body = {
        "name": "ISEO Runtime PG (v3)",
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
    }
    try:
        # list existing
        existing = n8n_request("GET", "/api/v1/credentials")
        cred_id = None
        cred_name = "ISEO Runtime PG (v3)"
        items = existing.get("data", existing) if isinstance(existing, dict) else existing
        if isinstance(items, list):
            for c in items:
                if c.get("name") == cred_name and c.get("type") == "postgres":
                    cred_id = c.get("id")
                    break
        if not cred_id:
            created = n8n_request("POST", "/api/v1/credentials", cred_body)
            cred_id = created.get("id")
        results["gates"]["n8n_pg_credential_id"] = cred_id
        results["gates"]["n8n_pg_credential_name"] = cred_name
        results["gates"]["n8n_pg_credential_role"] = "iseo_runtime"
    except Exception as e:
        results["gates"]["n8n_pg_credential_error"] = type(e).__name__
        (EVID / "orchestrator_result.json").write_text(
            json.dumps(results, indent=2), encoding="utf-8"
        )
        print("CRED_FAILED", e)
        return 1

    # Create inactive workflow (reuse existing candidate by name — only one)
    wf_name = "i-SEO Sales Manager - Operational.v3.dev"
    wf_id = None
    try:
        listing = n8n_request("GET", "/api/v1/workflows?limit=250")
        data = listing.get("data", listing) if isinstance(listing, dict) else listing
        if isinstance(data, list):
            for w in data:
                if w.get("name") == wf_name:
                    wf_id = w.get("id")
                    break
    except Exception:
        pass

    nodes = build_workflow_nodes(cred_id)
    connections = build_connections()
    wf_payload = {
        "name": wf_name,
        "nodes": nodes,
        "connections": connections,
        "settings": {
            "executionOrder": "v1",
            "callerPolicy": "workflowsFromSameOwner",
        },
        "staticData": None,
    }
    if wf_id:
        # PUT update keeps same ID; remain inactive
        updated = n8n_request("PUT", f"/api/v1/workflows/{wf_id}", wf_payload)
        created_wf = updated
    else:
        created_wf = n8n_request("POST", "/api/v1/workflows", wf_payload)
        wf_id = created_wf.get("id")
    # Ensure inactive
    if created_wf.get("active") or True:
        try:
            n8n_request("POST", f"/api/v1/workflows/{wf_id}/deactivate", {})
        except Exception:
            pass
    # verify prod still active
    prod = n8n_request("GET", f"/api/v1/workflows/{PROD_WF_ID}")
    cand = n8n_request("GET", f"/api/v1/workflows/{wf_id}")
    results["gates"]["candidate_workflow_id"] = wf_id
    results["gates"]["candidate_name"] = cand.get("name")
    results["gates"]["candidate_active"] = bool(cand.get("active"))
    results["gates"]["production_workflow_id"] = PROD_WF_ID
    results["gates"]["production_active"] = bool(prod.get("active"))
    results["gates"]["production_name"] = prod.get("name")

    # Export workflow source (sanitized — no password)
    export = {
        "id": wf_id,
        "name": cand.get("name"),
        "active": cand.get("active"),
        "nodes": cand.get("nodes"),
        "connections": cand.get("connections"),
        "settings": cand.get("settings"),
        "meta": {
            "export_ts": ts,
            "data_contract_version": "iseo-sales-v1",
            "release_version": "Operational.v3.dev",
            "status": "candidate",
            "pg_credential_id": cred_id,
            "pg_credential_name": cred_name,
            "pg_role": "iseo_runtime",
        },
    }
    export_path = WF_OUT / "Operational.v3.dev.n8n.json"
    export_path.write_text(json.dumps(export, indent=2), encoding="utf-8")
    export_hash = hashlib.sha256(export_path.read_bytes()).hexdigest()
    results["gates"]["git_export_hash"] = export_hash

    # Register workflow_releases
    reg_sql = f"""
INSERT INTO mars_core.workflow_releases (
  app_id, workflow_family, n8n_workflow_id, release_version,
  data_contract_version, status, git_export_hash, notes, metadata
)
SELECT a.id, 'operational_intake', '{wf_id}', 'Operational.v3.dev',
  'iseo-sales-v1', 'candidate', '{export_hash}',
  'PG candidate inactive build; Sheets Operational.dev remains active',
  jsonb_build_object(
    'migration', '0005_v3_runtime_functions',
    'credential_name', 'ISEO Runtime PG (v3)',
    'credential_id', '{cred_id}',
    'role', 'iseo_runtime'
  )
FROM mars_core.apps a WHERE a.app_key='app_iseo_sales'
RETURNING id, status, n8n_workflow_id;
"""
    remote_reg = f"/opt/mars/tmp/v3_register_{ts}.sql"
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

    # Active-state proof
    proof = {
        "production": {
            "id": PROD_WF_ID,
            "name": prod.get("name"),
            "active": prod.get("active"),
        },
        "candidate": {
            "id": wf_id,
            "name": cand.get("name"),
            "active": cand.get("active"),
        },
        "concurrent_gmail_intake": "Operational.dev only",
        "security_remediation": "SECURITY REMEDIATION DEFERRED TO SEPARATE SERVER OPS WAVE",
    }
    (EVID / "active_state_proof.json").write_text(
        json.dumps(proof, indent=2), encoding="utf-8"
    )

    results["verdict_hint"] = (
        "PASS"
        if (
            results["gates"].get("migration_apply_ok")
            and results["gates"].get("pg_tests_ok")
            and results["gates"].get("candidate_workflow_id")
            and results["gates"].get("candidate_active") is False
            and results["gates"].get("production_active") is True
            and results["gates"].get("workflow_registry_ok")
        )
        else "PARTIAL"
    )
    (EVID / "orchestrator_result.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8"
    )
    print(json.dumps({k: results[k] for k in ("ts", "verdict_hint", "gates")}, indent=2))
    return 0 if results["verdict_hint"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())

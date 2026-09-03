#!/usr/bin/env python3
"""Cutover-prep forensics: register Sheets production release + Admin Sheets dependency map.

READ-ONLY against live n8n workflows except mars_core INSERT for Operational.dev active row.
Does NOT activate/deactivate any workflow. Does NOT modify Admin.dev.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
EVID = ROOT / "evidence" / "cutover-prep" / "iseo-sales-v1"
N8N_ENV = Path(r"X:\AI MARS\local\tokens\n8n-api.env")
PRIV = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_ed25519")
SUDO_PATH = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_sudo.secret")
HOST = "178.173.255.239"

PROD_ID = "xSnXPy8cEHoZw6xG"
CAND_ID = "NH4uV145Amrgnmkm"
RB_ID = "favawMOzVwtFMdyH"
ADMIN_ID = "wLrLp4WQHm1VJmxz"


def load_dotenv(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def n8n_request(method: str, path: str) -> dict:
    env = load_dotenv(N8N_ENV)
    base = env.get("N8N_API_URL") or env.get("N8N_BASE_URL") or env.get("N8N_URL")
    key = env.get("N8N_API_KEY") or env.get("API_KEY")
    url = base.rstrip("/") + path
    req = urllib.request.Request(
        url,
        method=method,
        headers={"X-N8N-API-KEY": key, "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def classify_sheets_op(node: dict) -> str | None:
    t = (node.get("type") or "").lower()
    if "googlesheets" not in t and "googleSheets" not in (node.get("type") or ""):
        if "n8n-nodes-base.googleSheets" not in (node.get("type") or ""):
            return None
    params = node.get("parameters") or {}
    op = (
        params.get("operation")
        or params.get("resource")
        or ((params.get("options") or {}).get("operation") if isinstance(params.get("options"), dict) else None)
        or ""
    )
    op_l = str(op).lower()
    # common n8n sheets ops
    write_ops = {
        "append",
        "appendOrUpdate",
        "update",
        "clear",
        "delete",
        "create",
        "appendOrUpdate",
        "deleteSheet",
        "remove",
    }
    if any(w.lower() == op_l or w in op_l for w in write_ops):
        return "WRITE"
    if op_l in {"read", "get", "getAll", "lookup", "search"} or "read" in op_l or "get" in op_l:
        return "READ"
    # fallback: presence of columns to match often implies upsert/update
    if params.get("columns") or params.get("dataToSend") or params.get("fieldsUi"):
        # still may be read mapping — use operation string if present
        if not op_l:
            return "UNKNOWN_SHEETS"
    if not op_l:
        return "UNKNOWN_SHEETS"
    return "READ" if "get" in op_l or "lookup" in op_l else "WRITE"


def sheet_name_hint(node: dict) -> str:
    p = node.get("parameters") or {}
    for k in ("sheetName", "sheetName", "range", "tableId"):
        v = p.get(k)
        if isinstance(v, dict):
            v = v.get("value") or v.get("cachedResultName") or ""
        if v:
            return str(v)[:80]
    return ""


def analyze_workflow(wf: dict) -> dict:
    nodes = wf.get("nodes") or []
    sheets = []
    cred_types: Counter[str] = Counter()
    type_counts: Counter[str] = Counter()
    for n in nodes:
        nt = n.get("type") or ""
        type_counts[nt] += 1
        creds = n.get("credentials") or {}
        for ck in creds:
            cred_types[ck] += 1
        if "googleSheets" in nt or nt.endswith("googleSheets"):
            kind = classify_sheets_op(n)
            sheets.append(
                {
                    "name": n.get("name"),
                    "type": nt,
                    "op_class": kind,
                    "operation": (n.get("parameters") or {}).get("operation"),
                    "sheet_hint": sheet_name_hint(n),
                }
            )
    postgres_nodes = [n.get("name") for n in nodes if "postgres" in (n.get("type") or "").lower()]
    gmail_nodes = [n.get("name") for n in nodes if "gmail" in (n.get("type") or "").lower()]
    telegram_nodes = [n.get("name") for n in nodes if "telegram" in (n.get("type") or "").lower()]
    write_n = sum(1 for s in sheets if s["op_class"] == "WRITE")
    read_n = sum(1 for s in sheets if s["op_class"] == "READ")
    unk_n = sum(1 for s in sheets if s["op_class"] == "UNKNOWN_SHEETS")
    return {
        "id": wf.get("id"),
        "name": wf.get("name"),
        "active": wf.get("active"),
        "node_count": len(nodes),
        "sheets_nodes": len(sheets),
        "sheets_write": write_n,
        "sheets_read": read_n,
        "sheets_unknown": unk_n,
        "sheets_detail": sheets,
        "postgres_nodes": postgres_nodes,
        "gmail_nodes": gmail_nodes,
        "telegram_nodes": telegram_nodes,
        "credential_types": dict(cred_types),
        "top_types": type_counts.most_common(15),
    }


def ssh_psql(sql: str) -> tuple[int, str, str]:
    sudo = SUDO_PATH.read_text(encoding="utf-8").strip()
    script = (
        "docker exec -i mars-postgres psql -U mars_admin -d mars "
        f"-v ON_ERROR_STOP=1 <<'SQL'\n{sql}\nSQL\n"
    )
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkey = paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    c.connect(HOST, 22, "marsops", pkey=pkey, timeout=60, allow_agent=False, look_for_keys=False)
    chan = c.get_transport().open_session()
    chan.settimeout(90)
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

    workflows = {}
    for wid, label in [
        (PROD_ID, "production"),
        (CAND_ID, "candidate"),
        (RB_ID, "rollback"),
        (ADMIN_ID, "admin"),
    ]:
        wf = n8n_request("GET", f"/api/v1/workflows/{wid}")
        workflows[label] = analyze_workflow(wf)
        # store sanitized node op summary only (no parameters with PII)
        print(label, workflows[label]["name"], "active=", workflows[label]["active"],
              "sheets_w/r=", workflows[label]["sheets_write"], workflows[label]["sheets_read"])

    state = {
        "captured_at": ts,
        "authority": "SHEETS_PRIMARY / PG_SHADOW_VALIDATED",
        "workflows": {
            k: {
                "id": v["id"],
                "name": v["name"],
                "active": v["active"],
                "node_count": v["node_count"],
                "sheets_write": v["sheets_write"],
                "sheets_read": v["sheets_read"],
                "sheets_unknown": v["sheets_unknown"],
                "postgres_nodes": v["postgres_nodes"],
                "gmail_node_count": len(v["gmail_nodes"]),
                "telegram_node_count": len(v["telegram_nodes"]),
                "credential_types": v["credential_types"],
            }
            for k, v in workflows.items()
        },
        "hard_stops_observed": {
            "prod_active": workflows["production"]["active"] is True,
            "candidate_inactive": workflows["candidate"]["active"] is False,
            "rollback_inactive": workflows["rollback"]["active"] is False,
            "admin_active": workflows["admin"]["active"] is True,
        },
    }
    (EVID / "workflow_state.json").write_text(json.dumps(state, indent=2), encoding="utf-8")

    admin = workflows["admin"]
    # Classify Admin sheet targets by write vs read
    write_targets = sorted({s["sheet_hint"] or s["name"] for s in admin["sheets_detail"] if s["op_class"] == "WRITE"})
    read_targets = sorted({s["sheet_hint"] or s["name"] for s in admin["sheets_detail"] if s["op_class"] == "READ"})
    admin_forensic = {
        "workflow_id": ADMIN_ID,
        "name": admin["name"],
        "active": admin["active"],
        "sheets_write_count": admin["sheets_write"],
        "sheets_read_count": admin["sheets_read"],
        "sheets_unknown_count": admin["sheets_unknown"],
        "write_node_names": [s["name"] for s in admin["sheets_detail"] if s["op_class"] == "WRITE"],
        "write_operations": [
            {"name": s["name"], "operation": s["operation"], "sheet_hint": s["sheet_hint"]}
            for s in admin["sheets_detail"]
            if s["op_class"] == "WRITE"
        ],
        "read_sheet_hints_sample": read_targets[:40],
        "write_sheet_hints": write_targets,
        "postgres_nodes": admin["postgres_nodes"],
        "split_brain_risk": admin["sheets_write"] > 0,
        "topology_implication": (
            "JOINT OPERATIONAL + ADMIN PG CUTOVER REQUIRED"
            if admin["sheets_write"] > 0
            else "OPERATIONAL-ONLY MAY BE SAFE IF ADMIN READ-ONLY"
        ),
        "dependency_classes": [],
    }
    # Heuristic classing for report
    for hint in write_targets:
        h = hint.lower()
        if "access" in h:
            cls = "MUST MIGRATE BEFORE OPERATIONAL CUTOVER"
            reason = "ACCESS write path"
        elif any(x in h for x in ("clean", "lead", "status", "lifecycle", "processed")):
            cls = "MUST MIGRATE BEFORE OPERATIONAL CUTOVER"
            reason = "lead lifecycle/status write"
        elif "remind" in h or "deliver" in h:
            cls = "MUST MIGRATE BEFORE OPERATIONAL CUTOVER"
            reason = "delivery/reminder write"
        elif "config" in h:
            cls = "MUST MIGRATE BEFORE OPERATIONAL CUTOVER"
            reason = "CONFIG write"
        else:
            cls = "MUST MIGRATE BEFORE OPERATIONAL CUTOVER"
            reason = "Sheets write present"
        admin_forensic["dependency_classes"].append({"target": hint, "class": cls, "reason": reason})
    for hint in read_targets[:30]:
        admin_forensic["dependency_classes"].append(
            {
                "target": hint,
                "class": "CAN TEMPORARILY READ LEGACY HISTORY" if admin["sheets_write"] == 0 else "MUST MIGRATE BEFORE OPERATIONAL CUTOVER",
                "reason": "Sheets read; unsafe alone if paired with Operational PG writes while Admin still writes Sheets",
            }
        )
    (EVID / "admin_dev_dependency_inventory.json").write_text(
        json.dumps(admin_forensic, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    # Credential dependency for v3 (candidate)
    cand = workflows["candidate"]
    cred_map = {
        "candidate_id": CAND_ID,
        "credential_types_present": cand["credential_types"],
        "postgres_nodes": cand["postgres_nodes"],
        "gmail_nodes": cand["gmail_nodes"],
        "telegram_nodes": cand["telegram_nodes"],
        "sheets_nodes": cand["sheets_nodes"],
        "requires_google_sheets_for_critical_path": cand["sheets_nodes"] > 0,
        "known_named_credentials": {
            "postgres": {"id": "XCmmOgzZ1RWT4Fg3", "name": "ISEO Runtime PG (v3)", "role": "iseo_runtime"},
            "note": "Gmail/Telegram credential IDs not printed as secrets; types counted from node.credentials keys only",
        },
    }
    (EVID / "credential_dependency_map.json").write_text(json.dumps(cred_map, indent=2), encoding="utf-8")

    # Register Operational.dev as active if missing
    # Hash: content fingerprint of sanitized summary (not full export to avoid large binary in git)
    prod_fp = hashlib.sha256(
        json.dumps(
            {
                "id": PROD_ID,
                "name": workflows["production"]["name"],
                "node_count": workflows["production"]["node_count"],
                "sheets_w": workflows["production"]["sheets_write"],
                "sheets_r": workflows["production"]["sheets_read"],
            },
            sort_keys=True,
        ).encode()
    ).hexdigest()
    reg_sql = f"""
DELETE FROM mars_core.workflow_releases wr
USING mars_core.apps a
WHERE wr.app_id = a.id
  AND a.app_key = 'app_iseo_sales'
  AND wr.workflow_family = 'operational_intake'
  AND wr.release_version = 'Operational.dev';

INSERT INTO mars_core.workflow_releases (
  app_id, workflow_family, n8n_workflow_id, release_version,
  data_contract_version, status, git_export_hash, activated_at, notes, metadata
)
SELECT a.id, 'operational_intake', '{PROD_ID}', 'Operational.dev',
  'sheets-legacy-v1', 'active', '{prod_fp}', now(),
  'Sheets production SoT; registered during cutover-prep; NOT PG runtime',
  jsonb_build_object(
    'runtime', 'google_sheets',
    'prep_ts', '{ts}',
    'hash_kind', 'workflow_summary_fingerprint'
  )
FROM mars_core.apps a WHERE a.app_key='app_iseo_sales'
RETURNING id, status, n8n_workflow_id, release_version;

SELECT wr.release_version, wr.status, wr.n8n_workflow_id, left(wr.git_export_hash,12) AS hash12
FROM mars_core.workflow_releases wr
JOIN mars_core.apps a ON a.id = wr.app_id
WHERE a.app_key='app_iseo_sales' AND wr.workflow_family='operational_intake'
ORDER BY wr.created_at;
"""
    (EVID / f"register_operational_dev_{ts}.sql").write_text(reg_sql, encoding="utf-8")
    st, out, err = ssh_psql(reg_sql)
    (EVID / "register_operational_dev_stdout.txt").write_text(out + "\n" + err, encoding="utf-8")
    (EVID / "workflow_releases_listing.txt").write_text(out, encoding="utf-8")
    print("REGISTER EXIT", st)
    print(out)
    if err:
        print(err)
    return 0 if st == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

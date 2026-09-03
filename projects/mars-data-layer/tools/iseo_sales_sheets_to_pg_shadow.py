#!/usr/bin/env python3
"""
ISEO Sales Sheets → PostgreSQL shadow migration orchestrator (Windows → VEESP).

Subcommands: inventory | dry-run | apply | reconcile | prove-live

Uploads worker to host, runs under sudo, downloads sanitized evidence.
Does not print secrets/tokens. Sheets remain authoritative; PG is shadow only.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import paramiko

HOST = "178.173.255.239"
PRIV = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_ed25519")
SUDO_PATH = Path(r"X:\AI MARS\local\infrastructure\VEESP-N8N-01\ssh\marsops_sudo.secret")
TOOLS = Path(__file__).resolve().parent
WORKER_LOCAL = TOOLS / "iseo_sales_shadow_worker.py"
EVIDENCE = TOOLS.parent / "evidence" / "shadow-migration" / "iseo-sales-v1"
REMOTE_WORKER = "/tmp/iseo_sales_shadow_worker.py"


def connect() -> paramiko.SSHClient:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkey = paramiko.Ed25519Key.from_private_key_file(str(PRIV))
    c.connect(HOST, 22, "marsops", pkey=pkey, timeout=60, allow_agent=False, look_for_keys=False)
    return c


def sudo_run(client: paramiko.SSHClient, script: str, timeout: int = 600) -> tuple[int, str, str]:
    pw = SUDO_PATH.read_text(encoding="utf-8").strip()
    chan = client.get_transport().open_session()
    chan.settimeout(timeout)
    chan.exec_command("sudo -S -p '' bash -s")
    chan.sendall((pw + "\n").encode())
    chan.sendall(("set -euo pipefail\n" + script + "\n").encode())
    chan.shutdown_write()
    out = chan.makefile("rb").read().decode("utf-8", "replace")
    err = chan.makefile_stderr("rb").read().decode("utf-8", "replace")
    st = chan.recv_exit_status()
    return st, out, err


def upload_worker(client: paramiko.SSHClient) -> None:
    if not WORKER_LOCAL.is_file():
        raise SystemExit(f"missing_worker:{WORKER_LOCAL}")
    sftp = client.open_sftp()
    sftp.put(str(WORKER_LOCAL), REMOTE_WORKER)
    sftp.close()


def download_dir(client: paramiko.SSHClient, remote_work: str, dest: Path) -> list[str]:
    dest.mkdir(parents=True, exist_ok=True)
    sftp = client.open_sftp()
    saved: list[str] = []
    try:
        for name in sftp.listdir(remote_work):
            if name.endswith(".sql") and name == "apply.sql":
                # keep apply.sql off git; still download for local operator audit under evidence if needed
                # Store only size/hash marker, not full SQL with potential PII
                remote = f"{remote_work}/{name}"
                local_meta = dest / "apply_sql_meta.json"
                st = sftp.stat(remote)
                local_meta.write_text(
                    json.dumps({"remote": remote, "size": st.st_size, "note": "full SQL kept on host only"}, indent=2),
                    encoding="utf-8",
                )
                saved.append(local_meta.name)
                continue
            if name.endswith(".sql"):
                continue
            remote = f"{remote_work}/{name}"
            local = dest / name
            sftp.get(remote, str(local))
            saved.append(name)
    finally:
        sftp.close()
    return saved


def parse_worker_stdout(out: str) -> dict:
    lines = [ln.strip() for ln in out.splitlines() if ln.strip()]
    for ln in reversed(lines):
        if ln.startswith("{") and '"ok"' in ln:
            try:
                return json.loads(ln)
            except json.JSONDecodeError:
                continue
    return {"ok": False, "parse_error": True, "stdout_tail": out[-4000:]}


def run_mode(mode: str) -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    client = connect()
    try:
        upload_worker(client)
        script = f"""
python3 {REMOTE_WORKER}
"""
        # Pass mode via env
        script = f"""
export ISEO_MODE={mode}
python3 {REMOTE_WORKER}
"""
        st, out, err = sudo_run(client, script, timeout=900)
        parsed = parse_worker_stdout(out)
        summary = {
            "mode": mode,
            "ssh_status": st,
            "stderr_tail": err[-2000:],
            "worker": {k: parsed.get(k) for k in ("ok", "work", "snapshot_id", "mode") if k in parsed},
            "result_keys": list((parsed.get("result") or {}).keys()) if isinstance(parsed.get("result"), dict) else [],
        }
        # Avoid dumping full counters with potential sensitive structure into console beyond summary
        if isinstance(parsed.get("result"), dict):
            counters = parsed["result"].get("counters")
            if isinstance(counters, dict):
                summary["counter_keys"] = sorted(counters.keys())
                summary["counters_sample"] = {k: counters[k] for k in list(counters)[:40]}
            if "reconcile" in parsed["result"]:
                summary["reconcile"] = parsed["result"]["reconcile"]
            if "pre_dump" in parsed["result"]:
                summary["pre_dump"] = parsed["result"]["pre_dump"]
            if "post_dump" in parsed["result"]:
                summary["post_dump"] = parsed["result"]["post_dump"]
            if "sql_bytes" in parsed["result"]:
                summary["sql_bytes"] = parsed["result"]["sql_bytes"]
            if "tabs" in parsed["result"]:
                summary["tabs"] = parsed["result"]["tabs"]
            if "prove_live" in parsed["result"]:
                summary["prove_live"] = parsed["result"]["prove_live"]
            if "unknown_count" in parsed["result"]:
                summary["unknown_count"] = parsed["result"]["unknown_count"]

        (EVIDENCE / f"orchestrator_{mode}_summary.json").write_text(
            json.dumps(summary, indent=2, default=str), encoding="utf-8"
        )
        (EVIDENCE / f"orchestrator_{mode}_raw_stdout.txt").write_text(out[-20000:], encoding="utf-8")
        if err.strip():
            (EVIDENCE / f"orchestrator_{mode}_raw_stderr.txt").write_text(err[-8000:], encoding="utf-8")

        work = parsed.get("work")
        saved = []
        if work and parsed.get("ok"):
            saved = download_dir(client, work, EVIDENCE / f"run_{mode}_{parsed.get('snapshot_id', 'na')}")
            summary["downloaded"] = saved
            (EVIDENCE / f"orchestrator_{mode}_summary.json").write_text(
                json.dumps(summary, indent=2, default=str), encoding="utf-8"
            )

        print(json.dumps({"ok": bool(parsed.get("ok")) and st == 0, "summary": summary}, indent=2, default=str))
        return 0 if (parsed.get("ok") and st == 0) else 1
    finally:
        client.close()


def main() -> None:
    ap = argparse.ArgumentParser(description="ISEO Sales Sheets → PG shadow orchestrator")
    ap.add_argument(
        "mode",
        choices=["inventory", "dry-run", "apply", "reconcile", "prove-live"],
        help="Worker mode to execute on VEESP",
    )
    args = ap.parse_args()
    sys.exit(run_mode(args.mode))


if __name__ == "__main__":
    main()

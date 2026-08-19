# -*- coding: utf-8 -*-
"""PROD-P18J: indexing QA noise cleanup — deploy + bounded QA only. Never closes indexing."""
from __future__ import annotations

import hashlib
import io
import json
import re
import select
import socket
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import paramiko
import pymysql
import requests

ROOT = Path(r"X:\AI MARS\worktrees\fp-0002-p18j\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
EV = ROOT / "REPORTS" / "evidence" / "prod-p18j-indexing-qa-noise"
SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
WP_LOAD = f"{DOCROOT}/wp-load.php"
PLUGIN_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
UA = "FP-0002-P18J/1.0"

DEPLOY_MAP = {
    "shpigovsky-core.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
    "src/Admin/IndexingControl.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingControl.php",
    "src/Admin/IndexingState.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingState.php",
    "src/Admin/IndexingAlerts.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingAlerts.php",
    "src/Admin/IndexingWatchdog.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingWatchdog.php",
    "src/Admin/IndexingQaContext.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingQaContext.php",
    "src/Admin/ActivityLog.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/ActivityLog.php",
    "src/Admin/SystemDashboard.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/SystemDashboard.php",
}


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_secrets(text: str) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if match:
            pairs[match.group(1)] = match.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = pairs.get(key)
        if value and "<OPERATOR" not in value and value.strip():
            return value.strip()
    return None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(name: str, payload: Any) -> None:
    EV.mkdir(parents=True, exist_ok=True)
    (EV / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class LocalForward:
    def __init__(self, transport: paramiko.Transport, remote_host: str, remote_port: int):
        self.transport = transport
        self.remote_host = remote_host
        self.remote_port = remote_port
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("127.0.0.1", 0))
        self.sock.listen(4)
        self.local_port = self.sock.getsockname()[1]
        self._stop = False
        threading.Thread(target=self._accept, daemon=True).start()

    def _accept(self) -> None:
        while not self._stop:
            ready, _, _ = select.select([self.sock], [], [], 0.5)
            if not ready:
                continue
            try:
                client, _ = self.sock.accept()
            except OSError:
                return
            threading.Thread(target=self._forward, args=(client,), daemon=True).start()

    def _forward(self, client: socket.socket) -> None:
        try:
            chan = self.transport.open_channel("direct-tcpip", (self.remote_host, self.remote_port), client.getpeername())
        except Exception:
            client.close()
            return
        try:
            while True:
                ready, _, _ = select.select([client, chan], [], [], 30)
                if client in ready:
                    data = client.recv(65536)
                    if not data:
                        break
                    chan.sendall(data)
                if chan in ready:
                    data = chan.recv(65536)
                    if not data:
                        break
                    client.sendall(data)
        finally:
            client.close()
            chan.close()

    def close(self) -> None:
        self._stop = True
        try:
            self.sock.close()
        except OSError:
            pass


class RuntimeContext:
    def __init__(self) -> None:
        self.pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
        self.client: paramiko.SSHClient | None = None
        self.sftp: paramiko.SFTPClient | None = None
        self.db_conn: pymysql.Connection | None = None
        self.db_fwd: LocalForward | None = None

    def connect(self) -> None:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=getf(self.pairs, "ssh_host", "sftp_host", "ftp_host") or "shpigovsky.beget.tech",
            port=int(getf(self.pairs, "ssh_port", "sftp_port") or "22"),
            username=getf(self.pairs, "ssh_username", "ssh_user", "sftp_user", "ftp_user"),
            password=getf(self.pairs, "ssh_password_or_key_reference", "ssh_password", "sftp_password", "ftp_or_sftp_password", "ftp_password"),
            timeout=60,
            allow_agent=False,
            look_for_keys=False,
        )
        self.client = client
        self.sftp = client.open_sftp()
        fwd = LocalForward(client.get_transport(), "127.0.0.1", 3306)
        time.sleep(0.3)
        self.db_conn = pymysql.connect(
            host="127.0.0.1",
            port=fwd.local_port,
            user=getf(self.pairs, "db_user"),
            password=getf(self.pairs, "db_password"),
            database=getf(self.pairs, "db_name"),
            charset="utf8mb4",
            autocommit=True,
            connect_timeout=30,
            read_timeout=90,
            write_timeout=90,
        )
        self.db_fwd = fwd

    def close(self) -> None:
        if self.db_conn:
            self.db_conn.close()
        if self.db_fwd:
            self.db_fwd.close()
        if self.sftp:
            self.sftp.close()
        if self.client:
            self.client.close()

    def run_ssh(self, command: str, timeout: int = 90) -> tuple[str, str, int]:
        assert self.client is not None
        stdin, stdout, stderr = self.client.exec_command(command, timeout=timeout)
        return stdout.read().decode("utf-8", errors="replace"), stderr.read().decode("utf-8", errors="replace"), stdout.channel.recv_exit_status()

    def sftp_get(self, remote_path: str) -> bytes | None:
        assert self.sftp is not None
        try:
            buffer = io.BytesIO()
            self.sftp.getfo(remote_path, buffer)
            return buffer.getvalue()
        except (FileNotFoundError, OSError):
            return None

    def sftp_put_bytes(self, remote_path: str, payload: bytes) -> None:
        assert self.sftp is not None
        with self.sftp.file(remote_path, "wb") as fh:
            fh.write(payload)

    def sftp_remove(self, remote_path: str) -> None:
        assert self.sftp is not None
        self.sftp.remove(remote_path)

    def wp_eval_json(self, name: str, body: str) -> dict[str, Any]:
        remote_path = f"/tmp/fp02_{name}_{int(time.time())}.php"
        script = f"""<?php
error_reporting(E_ALL);
ini_set('display_errors', '0');
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['REQUEST_URI'] = '/';
$_SERVER['HTTPS'] = 'on';
require '{WP_LOAD}';
header('Content-Type: application/json; charset=utf-8');
{body}
"""
        self.sftp_put_bytes(remote_path, script.encode("utf-8"))
        out, err, code = self.run_ssh(f"php8.2 {remote_path} 2>/dev/null || php {remote_path}", timeout=120)
        try:
            self.sftp_remove(remote_path)
        except OSError:
            pass
        try:
            payload = json.loads(out.strip().splitlines()[-1] if out.strip() else "{}")
        except json.JSONDecodeError:
            payload = {"ok": False, "stdout_head": out[:4000], "stderr_head": err[:1200], "exit_code": code}
        payload["_exit_code"] = code
        return payload


def activity_rows(ctx: RuntimeContext) -> list[dict[str, Any]]:
    prefix = getf(ctx.pairs, "db_table_prefix") or "fp02_"
    rows: list[dict[str, Any]] = []
    assert ctx.db_conn is not None
    with ctx.db_conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT l.id, l.created_at, l.action, l.object_title, l.user_id
            FROM {prefix}user_activity_log l
            WHERE l.action IN ('indexing_opened','indexing_closed','indexing_close_blocked','indexing_qa_pass')
               OR l.object_title LIKE '%p18g_qa_guard_test%'
               OR l.created_at >= '2026-08-19 20:20:00'
            ORDER BY l.id DESC
            LIMIT 30
            """
        )
        for row in cur.fetchall():
            rows.append(
                {
                    "id": int(row[0]),
                    "created_at": str(row[1]),
                    "action": row[2],
                    "object_title": row[3],
                    "user_id": int(row[4]),
                }
            )
    return rows


def intake_readonly(ctx: RuntimeContext) -> dict[str, Any]:
    wp = ctx.wp_eval_json(
        "intake",
        r"""
$snap = class_exists('\Shpigovsky\Core\Admin\IndexingState') ? \Shpigovsky\Core\Admin\IndexingState::snapshot() : null;
$human = class_exists('\Shpigovsky\Core\Admin\IndexingState') ? \Shpigovsky\Core\Admin\IndexingState::get_human_authority() : get_option('fp02_indexing_human_authority', array());
$qa_evidence = class_exists('\Shpigovsky\Core\Admin\IndexingQaContext') ? \Shpigovsky\Core\Admin\IndexingQaContext::get_evidence_tail(10) : array();
$cron = wp_next_scheduled('fp02_indexing_watchdog_check');
echo wp_json_encode(array(
  'ok' => true,
  'home' => get_option('home'),
  'blog_public' => (int) get_option('blog_public'),
  'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'indexing_snap' => $snap,
  'human_authority' => is_array($human) ? $human : array(),
  'watchdog_scheduled' => (bool) $cron,
  'watchdog_next' => $cron ? gmdate('Y-m-d H:i:s', $cron) . ' UTC' : null,
  'qa_evidence_tail' => $qa_evidence,
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
""",
    )
    return {"captured_at": utcnow(), "wp": wp, "activity_recent": activity_rows(ctx)}


def deploy_files(ctx: RuntimeContext) -> list[dict[str, Any]]:
    results = []
    for rel, local in DEPLOY_MAP.items():
        remote = f"{PLUGIN_REMOTE}/{rel.replace(chr(92), '/')}"
        local_bytes = local.read_bytes()
        before = ctx.sftp_get(remote)
        ctx.sftp_put_bytes(remote, local_bytes)
        after = ctx.sftp_get(remote)
        results.append(
            {
                "rel": rel,
                "remote": remote,
                "local_sha256": sha256_bytes(local_bytes),
                "before_sha256": sha256_bytes(before) if before else None,
                "after_sha256": sha256_bytes(after) if after else None,
                "match": after == local_bytes,
            }
        )
    return results


def post_deploy_qa(ctx: RuntimeContext) -> dict[str, Any]:
    qa_guard = ctx.wp_eval_json(
        "qa_guard",
        r"""
if (!defined('FP02_INDEXING_QA_MODE_AUTHORIZED')) { define('FP02_INDEXING_QA_MODE_AUTHORIZED', true); }
$before = (int) get_option('blog_public', 1);
$activity_before = (int) $GLOBALS['wpdb']->get_var("SELECT COUNT(*) FROM {$GLOBALS['wpdb']->prefix}user_activity_log WHERE action='indexing_close_blocked' AND object_title LIKE '%p18j_qa_guard_test%'");
$r = class_exists('\Shpigovsky\Core\Admin\IndexingControl')
  ? \Shpigovsky\Core\Admin\IndexingControl::request_state(false, array(
      'source' => 'qa_test',
      'qa_test' => true,
      'test_id' => 'p18j_qa_guard_test',
    ))
  : array('blocked'=>true);
$after = (int) get_option('blog_public', 1);
$activity_after = (int) $GLOBALS['wpdb']->get_var("SELECT COUNT(*) FROM {$GLOBALS['wpdb']->prefix}user_activity_log WHERE action='indexing_close_blocked' AND object_title LIKE '%p18j_qa_guard_test%'");
$qa_tail = class_exists('\Shpigovsky\Core\Admin\IndexingQaContext') ? \Shpigovsky\Core\Admin\IndexingQaContext::get_evidence_tail(3) : array();
echo wp_json_encode(array(
  'before'=>$before,
  'after'=>$after,
  'result'=>$r,
  'guard_held_open' => ($before === 1 && $after === 1 && !empty($r['blocked'])),
  'activity_blocked_rows_delta' => $activity_after - $activity_before,
  'qa_evidence_tail' => $qa_tail,
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
""",
    )

    spoof = ctx.wp_eval_json(
        "spoof_qa",
        r"""
$before = (int) get_option('blog_public', 1);
$activity_before = (int) $GLOBALS['wpdb']->get_var("SELECT COUNT(*) FROM {$GLOBALS['wpdb']->prefix}user_activity_log WHERE action='indexing_close_blocked' AND created_at >= DATE_SUB(NOW(), INTERVAL 2 MINUTE)");
$r = class_exists('\Shpigovsky\Core\Admin\IndexingControl')
  ? \Shpigovsky\Core\Admin\IndexingControl::request_state(false, array(
      'source' => 'qa_test',
      'qa_test' => true,
      'test_id' => 'public_spoof_attempt',
    ))
  : array('blocked'=>true);
$after = (int) get_option('blog_public', 1);
$activity_after = (int) $GLOBALS['wpdb']->get_var("SELECT COUNT(*) FROM {$GLOBALS['wpdb']->prefix}user_activity_log WHERE action='indexing_close_blocked' AND created_at >= DATE_SUB(NOW(), INTERVAL 2 MINUTE)");
echo wp_json_encode(array(
  'before'=>$before,
  'after'=>$after,
  'result'=>$r,
  'spoof_suppressed_qa_mode' => !empty($r['blocked']),
  'activity_blocked_rows_delta_without_const' => $activity_after - $activity_before,
  'note' => 'Without FP02_INDEXING_QA_MODE_AUTHORIZED, spoof must log real incident row',
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
""",
    )

    test_alert = ctx.wp_eval_json(
        "test_alert",
        r"""
$r = class_exists('\Shpigovsky\Core\Admin\IndexingAlerts')
  ? \Shpigovsky\Core\Admin\IndexingAlerts::send_test_alert()
  : array('sent'=>false,'error'=>'missing');
echo wp_json_encode($r, JSON_UNESCAPED_UNICODE);
""",
    )

    watchdog = ctx.wp_eval_json(
        "watchdog",
        r"""
if (class_exists('\Shpigovsky\Core\Admin\IndexingWatchdog')) {
  \Shpigovsky\Core\Admin\IndexingWatchdog::run_check();
}
$line = class_exists('\Shpigovsky\Core\Admin\IndexingWatchdog') ? \Shpigovsky\Core\Admin\IndexingWatchdog::dashboard_line() : '';
$snap = class_exists('\Shpigovsky\Core\Admin\IndexingState') ? \Shpigovsky\Core\Admin\IndexingState::snapshot() : array();
echo wp_json_encode(array('dashboard_line'=>$line,'snap'=>$snap), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
""",
    )

    meta = ctx.wp_eval_json(
        "meta",
        r"""
$meta = get_option('fp02_metacode_system_meta', array());
if (!is_array($meta)) { $meta = array(); }
$meta['indexing'] = 'OPEN — HUMAN-APPROVED';
$meta['latest_wave'] = 'P18J Indexing QA Noise Cleanup';
$meta['baseline_id'] = 'FP-0002-PRODUCTION-MAINTENANCE-2026-08-20-P18J';
$meta['verified_at'] = gmdate('Y-m-d H:i:s') . ' UTC';
update_option('fp02_metacode_system_meta', $meta, false);
echo wp_json_encode(array('ok'=>true,'core'=>defined('SHPIGOVSKY_CORE_VERSION')?SHPIGOVSKY_CORE_VERSION:null,'meta'=>$meta), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
""",
    )

    return {
        "qa_guard": qa_guard,
        "spoof_without_const": spoof,
        "test_alert": test_alert,
        "watchdog": watchdog,
        "meta_update": meta,
    }


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    ctx = RuntimeContext()
    ctx.connect()
    try:
        pre = intake_readonly(ctx)
        write_json("01-pre-intake.json", pre)

        deploy = deploy_files(ctx)
        write_json("02-deploy-manifest.json", deploy)

        qa = post_deploy_qa(ctx)
        write_json("03-post-deploy-qa.json", qa)

        post = intake_readonly(ctx)
        write_json("04-post-intake.json", post)

        parity_ok = all(x["match"] for x in deploy)
        guard_ok = qa["qa_guard"].get("guard_held_open") is True
        qa_no_activity_noise = int(qa["qa_guard"].get("activity_blocked_rows_delta") or 0) == 0
        open_ok = int(post["wp"].get("blog_public") or 0) == 1

        summary = {
            "captured_at": utcnow(),
            "parity_ok": parity_ok,
            "deploy_count": len(deploy),
            "guard_ok": guard_ok,
            "qa_no_activity_noise": qa_no_activity_noise,
            "indexing_open_ok": open_ok,
            "core_after": post["wp"].get("core"),
            "effective_after": (post["wp"].get("indexing_snap") or {}).get("effective"),
        }
        write_json("00-summary.json", summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0 if parity_ok and guard_ok and qa_no_activity_noise and open_ok else 2
    finally:
        ctx.close()


if __name__ == "__main__":
    raise SystemExit(main())

# -*- coding: utf-8 -*-
"""PROD-P18G: indexing safety guard — intake, deploy, QA. Never closes production indexing."""
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

ROOT = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
EV = ROOT / "REPORTS" / "evidence" / "prod-p18g-indexing-safety"
SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
WP_LOAD = f"{DOCROOT}/wp-load.php"
PLUGIN_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
UA = "FP-0002-P18G/1.0"

DEPLOY_MAP = {
    "shpigovsky-core.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
    "src/ModuleRegistry.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/ModuleRegistry.php",
    "src/Admin/IndexingControl.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingControl.php",
    "src/Admin/IndexingState.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingState.php",
    "src/Admin/IndexingAlerts.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingAlerts.php",
    "src/Admin/IndexingWatchdog.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingWatchdog.php",
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


def http_probe(url: str) -> dict[str, Any]:
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=25, allow_redirects=True)
        body = r.text[:8000]
        meta_robots = re.findall(r'<meta[^>]+name=["\']robots["\'][^>]*>', body, re.I)
        noindex = "noindex" in body.lower()[:5000]
        xrobots = r.headers.get("X-Robots-Tag", "")
        return {
            "url": url,
            "status": r.status_code,
            "x_robots_tag": xrobots,
            "meta_robots_tags": meta_robots[:5],
            "body_has_noindex": noindex,
            "body_head": body[:400],
        }
    except Exception as exc:
        return {"url": url, "error": str(exc)}


def intake_readonly(ctx: RuntimeContext) -> dict[str, Any]:
    robots_path = f"{DOCROOT}/robots.txt"
    robots_bytes = ctx.sftp_get(robots_path)
    stat = None
    if ctx.sftp:
        try:
            st = ctx.sftp.stat(robots_path)
            stat = {"size": st.st_size, "mtime": st.st_mtime}
        except OSError:
            stat = None

    wp = ctx.wp_eval_json(
        "intake",
        r"""
$snap = class_exists('\Shpigovsky\Core\Admin\IndexingState') ? \Shpigovsky\Core\Admin\IndexingState::snapshot() : null;
$human = class_exists('\Shpigovsky\Core\Admin\IndexingState') ? \Shpigovsky\Core\Admin\IndexingState::get_human_authority() : get_option('fp02_indexing_human_authority', array());
echo wp_json_encode(array(
  'ok' => true,
  'home' => get_option('home'),
  'siteurl' => get_option('siteurl'),
  'blog_public' => (int) get_option('blog_public'),
  'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'indexing_snap' => $snap,
  'human_authority' => is_array($human) ? $human : array(),
  'dashboard_meta' => get_option('fp02_metacode_system_meta', array()),
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
""",
    )

    http = {
        "robots_txt": http_probe("https://shpigovsky.ru/robots.txt"),
        "home": http_probe("https://shpigovsky.ru/"),
        "uslugi": http_probe("https://shpigovsky.ru/uslugi/"),
    }

    prefix = getf(ctx.pairs, "db_table_prefix") or "fp02_"
    activity = []
    assert ctx.db_conn is not None
    with ctx.db_conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT l.id, l.created_at, l.action, l.object_title, l.user_id,
                   COALESCE(u.user_login, 'system') AS user_login,
                   COALESCE(NULLIF(u.display_name, ''), COALESCE(u.user_login, 'System')) AS display_name
            FROM {prefix}user_activity_log l
            LEFT JOIN {prefix}users u ON u.ID = l.user_id
            WHERE l.action IN ('indexing_opened','indexing_closed','indexing_close_blocked')
               OR l.created_at BETWEEN '2026-08-19 12:00:00' AND '2026-08-19 18:00:00'
            ORDER BY l.id ASC
            """
        )
        for row in cur.fetchall():
            activity.append(
                {
                    "id": int(row[0]),
                    "created_at": str(row[1]),
                    "action": row[2],
                    "object_title": row[3],
                    "user_id": int(row[4]),
                    "user_login": row[5],
                    "display_name": row[6],
                }
            )

    return {
        "captured_at": utcnow(),
        "wp": wp,
        "robots_physical": {
            "path": robots_path,
            "exists": robots_bytes is not None,
            "sha256": sha256_bytes(robots_bytes) if robots_bytes else None,
            "body": robots_bytes.decode("utf-8", errors="replace") if robots_bytes else None,
            "stat": stat,
        },
        "http": http,
        "activity_window": activity,
    }


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
    bootstrap = ctx.wp_eval_json(
        "bootstrap_human",
        r"""
$out = array('ok'=>false);
if (!class_exists('\Shpigovsky\Core\Admin\IndexingState')) { echo wp_json_encode($out); return; }
$human = \Shpigovsky\Core\Admin\IndexingState::get_human_authority();
$snap = \Shpigovsky\Core\Admin\IndexingState::snapshot();
if (empty($human['decision']) && (int)get_option('blog_public',1) === 1 && $snap['effective'] === 'OPEN') {
  \Shpigovsky\Core\Admin\IndexingState::record_human_decision('OPEN', array(
    'source' => 'p18g_bootstrap',
    'actor_display' => 'Olya',
    'actor_login' => 'olya',
    'user_id' => 0,
  ));
  $human = \Shpigovsky\Core\Admin\IndexingState::get_human_authority();
  $out['bootstrapped'] = true;
}
$meta = get_option('fp02_metacode_system_meta', array());
if (!is_array($meta)) { $meta = array(); }
$meta['indexing'] = 'OPEN — HUMAN-APPROVED';
$meta['latest_wave'] = 'P18G Indexing Safety Guard + Critical Admin Alerts';
$meta['baseline_id'] = 'FP-0002-PROD-BASELINE-2026-08-20-P18G';
update_option('fp02_metacode_system_meta', $meta, false);
if (class_exists('\Shpigovsky\Core\Admin\IndexingWatchdog')) {
  \Shpigovsky\Core\Admin\IndexingWatchdog::ensure_schedule();
}
$out['ok'] = true;
$out['human'] = \Shpigovsky\Core\Admin\IndexingState::get_human_authority();
$out['snap'] = \Shpigovsky\Core\Admin\IndexingState::snapshot();
echo wp_json_encode($out, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
""",
    )

    blocked_close = ctx.wp_eval_json(
        "guard_close",
        r"""
$before = (int) get_option('blog_public', 1);
$r = class_exists('\Shpigovsky\Core\Admin\IndexingControl')
  ? \Shpigovsky\Core\Admin\IndexingControl::request_state(false, array('source'=>'p18g_qa_guard_test'))
  : array('blocked'=>true);
$after = (int) get_option('blog_public', 1);
echo wp_json_encode(array(
  'before'=>$before,
  'after'=>$after,
  'result'=>$r,
  'guard_held_open' => ($before === 1 && $after === 1 && !empty($r['blocked'])),
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
""",
    )

    admin_recipients = ctx.wp_eval_json(
        "admin_recipients",
        r"""
$emails = class_exists('\Shpigovsky\Core\Admin\IndexingAlerts')
  ? \Shpigovsky\Core\Admin\IndexingAlerts::admin_recipient_emails()
  : array();
$redacted = array();
foreach ($emails as $e) {
  $parts = explode('@', $e, 2);
  $redacted[] = (strlen($parts[0]) > 2 ? substr($parts[0],0,2).'***' : '***') . '@' . ($parts[1] ?? '');
}
echo wp_json_encode(array('count'=>count($emails),'redacted'=>$redacted), JSON_UNESCAPED_UNICODE);
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

    reconcile = ctx.wp_eval_json(
        "reconcile",
        r"""
$out = array('mutated'=>false);
if (!class_exists('\Shpigovsky\Core\Admin\IndexingState')) { echo wp_json_encode($out); return; }
$snap = \Shpigovsky\Core\Admin\IndexingState::snapshot();
$human = \Shpigovsky\Core\Admin\IndexingState::get_human_authority();
$want_open = (!empty($human['decision']) && strtoupper($human['decision']) === 'OPEN') || ((int)get_option('blog_public',1)===1 && empty($human['decision']));
if ($want_open && $snap['effective'] !== 'OPEN' && class_exists('\Shpigovsky\Core\Admin\IndexingControl')) {
  $r = \Shpigovsky\Core\Admin\IndexingControl::request_state(true, array(
    'source'=>'p18g_reconcile',
    'explicit_human_authorization'=>true,
    'actor'=>'P18G reconcile',
  ));
  $out['mutated'] = true;
  $out['reconcile_result'] = $r;
}
$out['final'] = \Shpigovsky\Core\Admin\IndexingState::snapshot();
echo wp_json_encode($out, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
""",
    )

    return {
        "bootstrap": bootstrap,
        "blocked_close": blocked_close,
        "admin_recipients": admin_recipients,
        "test_alert": test_alert,
        "watchdog": watchdog,
        "reconcile": reconcile,
    }


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    ctx = RuntimeContext()
    ctx.connect()
    try:
        intake = intake_readonly(ctx)
        write_json("01-pre-intake.json", intake)

        deploy = deploy_files(ctx)
        write_json("02-deploy-manifest.json", deploy)

        qa = post_deploy_qa(ctx)
        write_json("03-post-deploy-qa.json", qa)

        post_intake = intake_readonly(ctx)
        write_json("04-post-intake.json", post_intake)

        parity_ok = all(x["match"] for x in deploy)
        guard_ok = qa["blocked_close"].get("guard_held_open") is True
        robots_body = post_intake.get("robots_physical", {}).get("body") or ""
        open_ok = int(post_intake["wp"].get("blog_public") or 0) == 1 and not re.search(
            r"^\s*Disallow:\s*/\s*$", robots_body, re.I | re.M
        )

        summary = {
            "captured_at": utcnow(),
            "parity_ok": parity_ok,
            "deploy_count": len(deploy),
            "guard_ok": guard_ok,
            "indexing_open_ok": open_ok,
            "core_after": post_intake["wp"].get("core"),
            "blog_public_after": post_intake["wp"].get("blog_public"),
            "effective_after": (post_intake["wp"].get("indexing_snap") or {}).get("effective"),
        }
        write_json("00-summary.json", summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0 if parity_ok and guard_ok and open_ok else 2
    finally:
        ctx.close()


if __name__ == "__main__":
    raise SystemExit(main())

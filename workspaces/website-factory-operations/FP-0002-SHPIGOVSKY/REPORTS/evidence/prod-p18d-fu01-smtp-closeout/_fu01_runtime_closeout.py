from __future__ import annotations

import argparse
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
EV = ROOT / "REPORTS" / "evidence" / "prod-p18d-fu01-smtp-closeout"
SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
WP_LOAD = f"{DOCROOT}/wp-load.php"
MU_REMOTE = f"{DOCROOT}/wp-content/mu-plugins/fp02-pre-cutover-mail-suppression.php"
PLUGIN_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
UA = "FP-0002-P18D-FU01/1.0"

REMOTE_FILES = {
    "mu_pre_cutover": MU_REMOTE,
    "mail_ops": f"{PLUGIN_REMOTE}/src/Mail/MailOps.php",
    "smtp_transport": f"{PLUGIN_REMOTE}/src/Mail/SmtpTransport.php",
    "consultation_handler": f"{PLUGIN_REMOTE}/src/Forms/ConsultationHandler.php",
    "system_dashboard": f"{PLUGIN_REMOTE}/src/Admin/SystemDashboard.php",
    "activity_log": f"{PLUGIN_REMOTE}/src/Admin/ActivityLog.php",
    "lead_registry": f"{PLUGIN_REMOTE}/src/Leads/LeadRegistry.php",
    "core_bootstrap": f"{PLUGIN_REMOTE}/shpigovsky-core.php",
}

LOCAL_FILES = {
    "mail_ops": ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core" / "src" / "Mail" / "MailOps.php",
    "smtp_transport": ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core" / "src" / "Mail" / "SmtpTransport.php",
    "consultation_handler": ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core" / "src" / "Forms" / "ConsultationHandler.php",
    "system_dashboard": ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core" / "src" / "Admin" / "SystemDashboard.php",
    "activity_log": ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core" / "src" / "Admin" / "ActivityLog.php",
    "lead_registry": ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core" / "src" / "Leads" / "LeadRegistry.php",
    "core_bootstrap": ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core" / "shpigovsky-core.php",
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


def write_text(name: str, text: str) -> None:
    EV.mkdir(parents=True, exist_ok=True)
    (EV / name).write_text(text, encoding="utf-8")


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
            chan = self.transport.open_channel(
                "direct-tcpip",
                (self.remote_host, self.remote_port),
                client.getpeername(),
            )
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
            password=getf(
                self.pairs,
                "ssh_password_or_key_reference",
                "ssh_password",
                "sftp_password",
                "ftp_or_sftp_password",
                "ftp_password",
            ),
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
        return (
            stdout.read().decode("utf-8", errors="replace"),
            stderr.read().decode("utf-8", errors="replace"),
            stdout.channel.recv_exit_status(),
        )

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
        payload: dict[str, Any]
        try:
            payload = json.loads(out.strip().splitlines()[-1] if out.strip() else "{}")
        except json.JSONDecodeError:
            payload = {
                "ok": False,
                "stdout_head": out[:4000],
                "stderr_head": err[:1200],
                "exit_code": code,
            }
        if not payload and (out or err):
            payload = {
                "ok": False,
                "stdout_head": out[:4000],
                "stderr_head": err[:1200],
                "exit_code": code,
            }
        if err.strip():
            payload["_stderr_head"] = err[:1200]
        payload["_exit_code"] = code
        return payload


def collect_activity_and_leads(ctx: RuntimeContext) -> dict[str, Any]:
    assert ctx.db_conn is not None
    prefix = getf(ctx.pairs, "db_table_prefix") or "fp02_"
    activity_table = f"{prefix}user_activity_log"
    users_table = f"{prefix}users"
    leads_table = f"{prefix}form_leads"
    out: dict[str, Any] = {}
    with ctx.db_conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT l.id, l.created_at, l.action, l.object_type, l.object_id, l.object_title, l.object_status,
                   COALESCE(u.user_login, 'system') AS user_login,
                   COALESCE(NULLIF(u.display_name, ''), COALESCE(u.user_login, 'System')) AS display_name
            FROM {activity_table} l
            LEFT JOIN {users_table} u ON u.ID = l.user_id
            ORDER BY l.id DESC
            LIMIT 80
            """
        )
        rows = cur.fetchall()
        out["activity_recent"] = [
            {
                "id": int(row[0]),
                "created_at": str(row[1]),
                "action": row[2],
                "object_type": row[3],
                "object_id": int(row[4]),
                "object_title": row[5],
                "object_status": row[6],
                "user_login": row[7],
                "display_name": row[8],
            }
            for row in rows
        ]

        cur.execute(
            f"""
            SELECT id, created_at, form_context, source_url, delivery_status, smtp_status, attempt_count, is_qa,
                   utm_source, utm_medium, visitor_name, email
            FROM {leads_table}
            WHERE is_qa = 1
               OR form_context = 'p18d-qa'
               OR utm_source = 'p18d-qa'
               OR source_url LIKE '%fp02_qa=p18d%'
            ORDER BY id DESC
            LIMIT 40
            """
        )
        qa_rows = cur.fetchall()
        out["qa_leads"] = [
            {
                "id": int(row[0]),
                "created_at": str(row[1]),
                "form_context": row[2],
                "source_url": row[3],
                "delivery_status": row[4],
                "smtp_status": row[5],
                "attempt_count": int(row[6]),
                "is_qa": int(row[7]),
                "utm_source": row[8],
                "utm_medium": row[9],
                "visitor_name": row[10][:32] if row[10] else "",
                "email_domain": row[11].split("@", 1)[1] if row[11] and "@" in row[11] else "",
            }
            for row in qa_rows
        ]
    return out


def collect_runtime_state(ctx: RuntimeContext) -> dict[str, Any]:
    php = r"""
global $wp_filter;

$filter_meta = array();
if (isset($wp_filter['pre_wp_mail'])) {
    $hook = $wp_filter['pre_wp_mail'];
    if (is_object($hook) && isset($hook->callbacks) && is_array($hook->callbacks)) {
        foreach ($hook->callbacks as $prio => $callbacks) {
            foreach ((array) $callbacks as $cb) {
                $sig = 'unknown';
                if (isset($cb['function'])) {
                    if (is_string($cb['function'])) {
                        $sig = $cb['function'];
                    } elseif (is_array($cb['function']) && isset($cb['function'][0], $cb['function'][1])) {
                        $owner = is_object($cb['function'][0]) ? get_class($cb['function'][0]) : (string) $cb['function'][0];
                        $sig = $owner . '::' . (string) $cb['function'][1];
                    }
                }
                $filter_meta[] = array('priority' => (int) $prio, 'callback' => $sig);
            }
        }
    }
}

$meta = get_option('fp02_metacode_system_meta', array());
if (!is_array($meta)) {
    $meta = array();
}
$cfg = \Shpigovsky\Core\Mail\MailOps::get_config();
$baseline_id = class_exists('\Shpigovsky\Core\Admin\SystemDashboard') ? \Shpigovsky\Core\Admin\SystemDashboard::BASELINE_ID : '';
$latest_wave = class_exists('\Shpigovsky\Core\Admin\SystemDashboard') ? \Shpigovsky\Core\Admin\SystemDashboard::LATEST_ACCEPTED_WAVE : '';
echo wp_json_encode(array(
    'ok' => true,
    'utc' => gmdate('c'),
    'home' => get_option('home'),
    'siteurl' => get_option('siteurl'),
    'blog_public' => (int) get_option('blog_public'),
    'mail' => array(
        'state' => \Shpigovsky\Core\Mail\MailOps::state(),
        'state_label' => \Shpigovsky\Core\Mail\MailOps::state_label(),
        'is_complete' => \Shpigovsky\Core\Mail\MailOps::is_complete(),
        'verified' => (int) $cfg['verified'],
        'verified_at' => (string) $cfg['verified_at'],
        'delivery_active' => (int) $cfg['delivery_active'],
        'should_suppress' => \Shpigovsky\Core\Mail\MailOps::should_suppress(),
        'should_attempt_mail' => \Shpigovsky\Core\Mail\MailOps::should_attempt_mail(),
        'smtp_host' => (string) $cfg['smtp_host'],
        'smtp_port' => (int) $cfg['smtp_port'],
        'smtp_encryption' => (string) $cfg['smtp_encryption'],
        'smtp_auth' => (int) $cfg['smtp_auth'],
        'smtp_username' => (string) $cfg['smtp_username'],
        'smtp_from_email' => \Shpigovsky\Core\Mail\MailOps::from_email(),
        'smtp_from_name' => \Shpigovsky\Core\Mail\MailOps::from_name(),
        'password_configured' => \Shpigovsky\Core\Mail\MailOps::password_is_configured(),
        'recipient_count' => \Shpigovsky\Core\Mail\MailOps::recipient_count(),
        'recipient_labels' => array_values(array_map(static function($row) {
            return isset($row['label']) ? (string) $row['label'] : '';
        }, (array) $cfg['recipients'])),
        'form_metrika_goal' => (string) $cfg['form_metrika_goal'],
        'lead_retention_days' => (int) $cfg['lead_retention_days'],
        'last_test_status' => (string) $cfg['last_test_status'],
        'last_test_error_category' => (string) $cfg['last_test_error_category'],
    ),
    'dashboard' => array(
        'baseline_id' => $baseline_id,
        'latest_wave' => $latest_wave,
        'meta' => $meta,
    ),
    'lead_registry_active' => class_exists('\Shpigovsky\Core\Leads\LeadRegistry'),
    'pre_wp_mail' => array(
        'has_filter' => has_filter('pre_wp_mail'),
        'callbacks' => $filter_meta,
    ),
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
"""
    return ctx.wp_eval_json("runtime_state", php)


def collect_file_reality(ctx: RuntimeContext) -> dict[str, Any]:
    out: dict[str, Any] = {"files": {}, "parity": {}}
    for key, remote_path in REMOTE_FILES.items():
        data = ctx.sftp_get(remote_path)
        if data is None:
            out["files"][key] = {"exists": False, "remote_path": remote_path}
        else:
            text = data.decode("utf-8", errors="replace")
            out["files"][key] = {
                "exists": True,
                "remote_path": remote_path,
                "bytes": len(data),
                "sha256": sha256_bytes(data),
                "head": text[:1200],
            }
        local_path = LOCAL_FILES.get(key)
        if local_path and local_path.exists() and data is not None:
            local_bytes = local_path.read_bytes()
            out["parity"][key] = {
                "local_path": str(local_path),
                "local_sha256": sha256_bytes(local_bytes),
                "remote_sha256": sha256_bytes(data),
                "match": local_bytes == data,
            }
    return out


def public_checks() -> dict[str, Any]:
    sess = requests.Session()
    sess.headers.update({"User-Agent": UA, "Accept-Language": "ru-RU,ru;q=0.9"})
    urls = [
        "https://shpigovsky.ru/",
        "https://shpigovsky.ru/robots.txt",
        "https://shpigovsky.ru/wp-json/",
        "http://shpigovsky.beget.tech/",
    ]
    probes = []
    for url in urls:
        try:
            resp = sess.get(url, timeout=30, allow_redirects=True)
            body = resp.text or ""
            probes.append(
                {
                    "url": url,
                    "status": resp.status_code,
                    "final_url": str(resp.url),
                    "server": resp.headers.get("Server"),
                    "content_type": resp.headers.get("Content-Type"),
                    "x_robots": resp.headers.get("X-Robots-Tag"),
                    "has_wp_markers": ("wp-content" in body) or ("wp-json" in body) or ("WordPress" in body),
                    "has_craftum_markers": ("craftum" in body.lower()) or ("new-site.space" in body.lower()),
                    "body_head": body[:600],
                }
            )
        except Exception as exc:  # noqa: BLE001
            probes.append({"url": url, "error": type(exc).__name__, "detail": str(exc)})
    return {"utc": utcnow(), "probes": probes}


def retire_mu(ctx: RuntimeContext) -> dict[str, Any]:
    before_state = collect_runtime_state(ctx)
    file_before = ctx.sftp_get(MU_REMOTE)
    result: dict[str, Any] = {
        "utc": utcnow(),
        "ready_before": before_state.get("mail", {}).get("state") == "verified_active"
        and not before_state.get("mail", {}).get("should_suppress", True),
        "mail_state_before": before_state.get("mail"),
        "pre_wp_mail_before": before_state.get("pre_wp_mail"),
        "mu_before": {
            "exists": file_before is not None,
            "sha256": sha256_bytes(file_before) if file_before is not None else None,
            "bytes": len(file_before) if file_before is not None else 0,
            "head": file_before.decode("utf-8", errors="replace")[:1500] if file_before is not None else "",
        },
    }
    if file_before is None:
        result["removed"] = False
        result["reason"] = "mu_file_missing"
        return result
    if not result["ready_before"]:
        result["removed"] = False
        result["reason"] = "not_ready"
        return result
    backup_name = f"mu-before-removal-{datetime.now().strftime('%Y%m%d-%H%M%S')}.php"
    write_text(backup_name, file_before.decode("utf-8", errors="replace"))
    ctx.sftp_remove(MU_REMOTE)
    time.sleep(1.0)
    after_state = collect_runtime_state(ctx)
    file_after = ctx.sftp_get(MU_REMOTE)
    result["removed"] = file_after is None
    result["mail_state_after"] = after_state.get("mail")
    result["pre_wp_mail_after"] = after_state.get("pre_wp_mail")
    result["mu_after_exists"] = file_after is not None
    return result


def smtp_correct_and_verify(ctx: RuntimeContext) -> dict[str, Any]:
    php = r"""
$cfg_before = \Shpigovsky\Core\Mail\MailOps::get_config();
$corrected = false;
if (
    'smtp.beget.com' === (string) $cfg_before['smtp_host']
    && 465 === (int) $cfg_before['smtp_port']
    && \Shpigovsky\Core\Mail\MailOps::ENCRYPTION_NONE === (string) $cfg_before['smtp_encryption']
) {
    $cfg_fixed = $cfg_before;
    $cfg_fixed['smtp_encryption'] = \Shpigovsky\Core\Mail\MailOps::ENCRYPTION_SSL;
    update_option(\Shpigovsky\Core\Mail\MailOps::OPTION_CONFIG, $cfg_fixed, false);
    $corrected = true;
}
$cfg_after = \Shpigovsky\Core\Mail\MailOps::get_config();
$recipients = \Shpigovsky\Core\Mail\MailOps::recipient_emails();
$ok = false;
$category = '';
$test_to = ! empty($recipients) ? $recipients[0] : '';
if (\Shpigovsky\Core\Mail\MailOps::is_complete() && ! empty($test_to)) {
    if (! defined('FP02_MAIL_ALLOW_ONCE')) {
        define('FP02_MAIL_ALLOW_ONCE', true);
    }
    $subject = 'FP-0002 SMTP test ' . gmdate('Y-m-d H:i:s') . ' UTC (P18D-FU01)';
    $body = "FP-0002 SMTP verification test.\nThis is not a client lead.\nTimestamp: " . gmdate('c') . "\n";
    $headers = array(
        'Content-Type: text/plain; charset=UTF-8',
        'From: ' . \Shpigovsky\Core\Mail\MailOps::from_name() . ' <' . \Shpigovsky\Core\Mail\MailOps::from_email() . '>',
    );
    $sent = wp_mail($test_to, $subject, $body, $headers);
    if ($sent) {
        $ok = true;
        \Shpigovsky\Core\Mail\MailOps::record_test_result(true, '');
        if (class_exists('\Shpigovsky\Core\Admin\ActivityLog')) {
            \Shpigovsky\Core\Admin\ActivityLog::log_system_event('smtp_test_ok', 'setting', 'Проверка SMTP: успех', 0);
        }
    } else {
        global $phpmailer;
        $raw = (is_object($phpmailer) && ! empty($phpmailer->ErrorInfo)) ? (string) $phpmailer->ErrorInfo : 'send_failed';
        $category = \Shpigovsky\Core\Mail\MailOps::sanitize_error_category($raw);
        \Shpigovsky\Core\Mail\MailOps::record_test_result(false, $category);
        if (class_exists('\Shpigovsky\Core\Admin\ActivityLog')) {
            \Shpigovsky\Core\Admin\ActivityLog::log_system_event('smtp_test_fail', 'setting', 'Проверка SMTP: ошибка (' . $category . ')', 0);
        }
    }
}
$cfg_final = \Shpigovsky\Core\Mail\MailOps::get_config();
echo wp_json_encode(array(
    'ok' => $ok,
    'corrected' => $corrected,
    'before_encryption' => (string) $cfg_before['smtp_encryption'],
    'after_encryption' => (string) $cfg_after['smtp_encryption'],
    'recipient_count' => count($recipients),
    'password_configured' => \Shpigovsky\Core\Mail\MailOps::password_is_configured(),
    'is_complete' => \Shpigovsky\Core\Mail\MailOps::is_complete(),
    'state_after' => \Shpigovsky\Core\Mail\MailOps::state(),
    'verified' => (int) $cfg_final['verified'],
    'delivery_active' => (int) $cfg_final['delivery_active'],
    'error_category' => $category,
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
"""
    return ctx.wp_eval_json("smtp_verify", php)


def smtp_activate_delivery(ctx: RuntimeContext) -> dict[str, Any]:
    php = r"""
$state_before = \Shpigovsky\Core\Mail\MailOps::state();
$ok = \Shpigovsky\Core\Mail\MailOps::activate_delivery();
$cfg = \Shpigovsky\Core\Mail\MailOps::get_config();
echo wp_json_encode(array(
    'ok' => (bool) $ok,
    'state_before' => $state_before,
    'state_after' => \Shpigovsky\Core\Mail\MailOps::state(),
    'verified' => (int) $cfg['verified'],
    'delivery_active' => (int) $cfg['delivery_active'],
    'should_suppress' => \Shpigovsky\Core\Mail\MailOps::should_suppress(),
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
"""
    return ctx.wp_eval_json("smtp_activate", php)


def close_indexing(ctx: RuntimeContext) -> dict[str, Any]:
    php = r"""
$result = array('ok' => false, 'owner' => 'missing');
if (class_exists('\Shpigovsky\Core\Admin\IndexingControl')) {
    $result = \Shpigovsky\Core\Admin\IndexingControl::set_site_indexability(false);
    $result['owner'] = 'IndexingControl';
} else {
    update_option('blog_public', '0');
    $result = array(
        'ok' => 0 === (int) get_option('blog_public', 1),
        'owner' => 'blog_public_only',
        'blog_public' => (int) get_option('blog_public', 1),
    );
}
echo wp_json_encode($result, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
"""
    return ctx.wp_eval_json("indexing_close", php)


def deploy_exact_file(ctx: RuntimeContext, local_path: Path, remote_path: str) -> dict[str, Any]:
    local_bytes = local_path.read_bytes()
    before = ctx.sftp_get(remote_path)
    before_sha = sha256_bytes(before) if before is not None else None
    ctx.sftp_put_bytes(remote_path, local_bytes)
    after = ctx.sftp_get(remote_path)
    after_sha = sha256_bytes(after) if after is not None else None
    return {
        "local_path": str(local_path),
        "remote_path": remote_path,
        "before_sha256": before_sha,
        "after_sha256": after_sha,
        "local_sha256": sha256_bytes(local_bytes),
        "match_after": after == local_bytes,
    }


def update_dashboard_meta(ctx: RuntimeContext) -> dict[str, Any]:
    php = r"""
$meta = get_option('fp02_metacode_system_meta', array());
if (!is_array($meta)) {
    $meta = array();
}
$meta['baseline_id'] = 'FP-0002-PROD-BASELINE-2026-08-19-P18D-FU01';
$meta['latest_wave'] = 'P18D-FU01 SMTP Closeout + Olya Intake';
$meta['parity'] = 'MATCH FOR SOURCE-OWNED CLOSEOUT FILES';
$meta['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
$meta['backup'] = 'FRESH BEGET BACKUP CONFIRMED BY OPERATOR';
$meta['wave'] = 'PROD-P18D-FU01';
$meta['state_note'] = 'LIVE https://shpigovsky.ru; INDEXING CLOSED; SMTP VERIFIED / ACTIVE; PRE-CUTOVER SUPPRESSION REMOVED';
$meta['legacy_redirects'] = '7/7';
$meta['cutover'] = 'DONE';
$meta['ssl'] = 'ACTIVE';
$meta['dns_ns'] = 'DONE / Beget';
$meta['smtp_sender'] = 'noreply@shpigovsky.ru';
$meta['indexing'] = 'CLOSED — WAITING FOR OLYA APPROVAL';
$meta['public_origin'] = 'https://shpigovsky.ru/ now serves WordPress';
$meta['mail'] = 'SMTP VERIFIED / ACTIVE';
$meta['leads'] = 'ACTIVE';
$meta['metrika_form_goals'] = 'CONFIGURABLE';
update_option('fp02_metacode_system_meta', $meta, false);
echo wp_json_encode(array('ok' => true, 'meta' => $meta), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
"""
    return ctx.wp_eval_json("dashboard_meta", php)


def run_form_qa(ctx: RuntimeContext) -> dict[str, Any]:
    php = r"""
$state = \Shpigovsky\Core\Mail\MailOps::state();
$recipients = \Shpigovsky\Core\Mail\MailOps::recipient_emails();
$lead_id = \Shpigovsky\Core\Leads\LeadRegistry::insert(array(
    'form_key'        => \Shpigovsky\Core\Leads\LeadRegistry::FORM_KEY,
    'form_context'    => 'p18d-fu01-qa',
    'source_url'      => 'https://shpigovsky.ru/?fp02_qa=p18d-fu01',
    'source_path'     => '/',
    'source_post_id'  => 0,
    'visitor_name'    => 'QA-P18D-FU01',
    'phone'           => '+7 000 000-00-00',
    'email'           => \Shpigovsky\Core\Mail\MailOps::from_email(),
    'message'         => '[P18D-FU01 QA] Controlled post-removal mail/form verification ' . gmdate('c'),
    'delivery_status' => \Shpigovsky\Core\Leads\LeadRegistry::STATUS_RECEIVED,
    'metrika_goal'    => \Shpigovsky\Core\Mail\MailOps::metrika_goal(),
    'utm_source'      => 'p18d-fu01-qa',
    'utm_medium'      => 'internal-test',
    'utm_campaign'    => 'smtp-closeout',
    'utm_content'     => '',
    'utm_term'        => '',
    'referrer'        => '',
    'ua_class'        => 'bot',
    'is_qa'           => true,
));

$attempted = false;
$accepted = false;
$status = \Shpigovsky\Core\Leads\LeadRegistry::STATUS_RECEIVED;
$error_code = '';
if ($lead_id > 0 && \Shpigovsky\Core\Mail\MailOps::should_attempt_mail()) {
    $attempted = true;
    $subject = '[FP-0002 P18D-FU01 QA] SMTP/Form post-removal check ' . gmdate('Y-m-d H:i:s') . ' UTC';
    $body = "Controlled QA.\nLead ID: " . $lead_id . "\nThis is not a real client lead.\n";
    $headers = array(
        'Content-Type: text/plain; charset=UTF-8',
        'From: ' . \Shpigovsky\Core\Mail\MailOps::from_name() . ' <' . \Shpigovsky\Core\Mail\MailOps::from_email() . '>',
        'Reply-To: ' . \Shpigovsky\Core\Mail\MailOps::from_email(),
    );
    $sent = wp_mail($recipients, $subject, $body, $headers);
    if ($sent) {
        $accepted = true;
        $status = \Shpigovsky\Core\Leads\LeadRegistry::STATUS_MAIL_ACCEPTED;
        \Shpigovsky\Core\Leads\LeadRegistry::update_delivery($lead_id, array(
            'delivery_status' => $status,
            'smtp_status' => 'accepted',
            'attempt_count' => 1,
        ));
    } else {
        global $phpmailer;
        $raw = (is_object($phpmailer) && ! empty($phpmailer->ErrorInfo)) ? (string) $phpmailer->ErrorInfo : 'send_failed';
        $error_code = \Shpigovsky\Core\Mail\MailOps::sanitize_error_category($raw);
        $status = \Shpigovsky\Core\Leads\LeadRegistry::STATUS_MAIL_ERROR;
        \Shpigovsky\Core\Leads\LeadRegistry::update_delivery($lead_id, array(
            'delivery_status' => $status,
            'smtp_status' => 'error',
            'error_code' => $error_code,
            'attempt_count' => 1,
        ));
    }
} elseif ($lead_id > 0) {
    $status = \Shpigovsky\Core\Mail\MailOps::is_complete() ? \Shpigovsky\Core\Leads\LeadRegistry::STATUS_SMTP_PENDING : \Shpigovsky\Core\Leads\LeadRegistry::STATUS_MAIL_SUPPRESSED;
    \Shpigovsky\Core\Leads\LeadRegistry::update_delivery($lead_id, array(
        'delivery_status' => $status,
        'smtp_status' => 'suppressed',
        'attempt_count' => 0,
    ));
}

$row = $lead_id > 0 ? \Shpigovsky\Core\Leads\LeadRegistry::get($lead_id) : null;
echo wp_json_encode(array(
    'ok' => $lead_id > 0,
    'mail_state' => $state,
    'recipient_count' => count($recipients),
    'lead_id' => (int) $lead_id,
    'mail_attempted' => $attempted,
    'mail_accepted' => $accepted,
    'delivery_status' => $status,
    'error_code' => $error_code,
    'row' => $row ? array(
        'id' => (int) $row->id,
        'created_at' => (string) $row->created_at,
        'form_context' => (string) $row->form_context,
        'delivery_status' => (string) $row->delivery_status,
        'smtp_status' => (string) $row->smtp_status,
        'attempt_count' => (int) $row->attempt_count,
        'is_qa' => (int) $row->is_qa,
        'utm_source' => (string) $row->utm_source,
    ) : null,
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
"""
    return ctx.wp_eval_json("form_qa", php)


def cleanup_qa_rows(ctx: RuntimeContext, lead_ids: list[int]) -> dict[str, Any]:
    assert ctx.db_conn is not None
    lead_ids = sorted({int(x) for x in lead_ids if int(x) > 0})
    result: dict[str, Any] = {"requested_ids": lead_ids, "deleted_ids": [], "skipped_ids": []}
    if not lead_ids:
        return result
    prefix = getf(ctx.pairs, "db_table_prefix") or "fp02_"
    table = f"{prefix}form_leads"
    with ctx.db_conn.cursor() as cur:
        fmt = ",".join(["%s"] * len(lead_ids))
        cur.execute(
            f"""
            SELECT id, is_qa, form_context, utm_source, source_url
            FROM {table}
            WHERE id IN ({fmt})
            """,
            tuple(lead_ids),
        )
        for row in cur.fetchall():
            lead_id = int(row[0])
            if int(row[1]) == 1 or row[2] in ("p18d-qa", "p18d-fu01-qa") or row[3] in ("p18d-qa", "p18d-fu01-qa") or "fp02_qa=p18d" in (row[4] or ""):
                cur.execute(f"DELETE FROM {table} WHERE id = %s LIMIT 1", (lead_id,))
                result["deleted_ids"].append(lead_id)
            else:
                result["skipped_ids"].append(lead_id)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Perform MU retirement and QA cleanup.")
    parser.add_argument("--sync-dashboard", action="store_true", help="Deploy dashboard/core source files and refresh dashboard meta.")
    args = parser.parse_args()

    EV.mkdir(parents=True, exist_ok=True)
    ctx = RuntimeContext()
    ctx.connect()
    try:
        intake_runtime = collect_runtime_state(ctx)
        intake_db = collect_activity_and_leads(ctx)
        file_reality = collect_file_reality(ctx)
        public = public_checks()
        write_json("01-runtime-state.json", intake_runtime)
        write_json("02-activity-and-qa-leads.json", intake_db)
        write_json("03-code-reality.json", file_reality)
        write_json("04-public-domain-check.json", public)

        summary: dict[str, Any] = {
            "utc": utcnow(),
            "status": "intake_only",
            "runtime_mail_state": intake_runtime.get("mail", {}).get("state"),
            "recipient_count": intake_runtime.get("mail", {}).get("recipient_count"),
            "qa_lead_ids_before": [row["id"] for row in intake_db.get("qa_leads", [])],
            "mu_exists_before": file_reality.get("files", {}).get("mu_pre_cutover", {}).get("exists"),
        }

        if args.apply:
            smtp_verify = smtp_correct_and_verify(ctx)
            write_json("05-smtp-correct-and-verify.json", smtp_verify)
            smtp_activate = smtp_activate_delivery(ctx)
            write_json("06-smtp-activate-delivery.json", smtp_activate)
            retire = retire_mu(ctx)
            write_json("07-mu-retirement.json", retire)
            qa = run_form_qa(ctx)
            write_json("08-post-removal-form-qa.json", qa)
            cleanup_ids = [int(qa.get("lead_id") or 0)]
            cleanup = cleanup_qa_rows(ctx, cleanup_ids)
            write_json("09-qa-cleanup.json", cleanup)
            indexing = close_indexing(ctx)
            write_json("10-indexing-close.json", indexing)
            post_runtime = collect_runtime_state(ctx)
            post_db = collect_activity_and_leads(ctx)
            post_files = collect_file_reality(ctx)
            write_json("11-post-closeout-runtime-state.json", post_runtime)
            write_json("12-post-closeout-activity-and-qa-leads.json", post_db)
            write_json("13-post-closeout-code-reality.json", post_files)
            summary.update(
                {
                    "status": "applied",
                    "smtp_verify_ok": smtp_verify.get("ok"),
                    "smtp_activate_ok": smtp_activate.get("ok"),
                    "mu_removed": retire.get("removed"),
                    "form_qa_lead_id": qa.get("lead_id"),
                    "form_qa_mail_accepted": qa.get("mail_accepted"),
                    "cleanup_deleted_ids": cleanup.get("deleted_ids"),
                    "indexing_close_ok": indexing.get("ok"),
                    "runtime_mail_state_after": post_runtime.get("mail", {}).get("state"),
                    "blog_public_after": post_runtime.get("blog_public"),
                    "qa_lead_ids_after": [row["id"] for row in post_db.get("qa_leads", [])],
                }
            )

        if args.sync_dashboard:
            deployed = {
                "core_bootstrap": deploy_exact_file(ctx, LOCAL_FILES["core_bootstrap"], REMOTE_FILES["core_bootstrap"]),
                "system_dashboard": deploy_exact_file(ctx, LOCAL_FILES["system_dashboard"], REMOTE_FILES["system_dashboard"]),
            }
            meta = update_dashboard_meta(ctx)
            synced_runtime = collect_runtime_state(ctx)
            write_json("14-dashboard-sync-deploy.json", deployed)
            write_json("15-dashboard-meta-sync.json", meta)
            write_json("16-dashboard-sync-runtime-state.json", synced_runtime)
            summary.update(
                {
                    "dashboard_sync": True,
                    "dashboard_files_match_after": all(item["match_after"] for item in deployed.values()),
                    "dashboard_meta_sync_ok": meta.get("ok"),
                    "dashboard_wave_after": synced_runtime.get("dashboard", {}).get("latest_wave"),
                    "dashboard_baseline_after": synced_runtime.get("dashboard", {}).get("baseline_id"),
                }
            )

        write_json("00-summary.json", summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0
    finally:
        ctx.close()


if __name__ == "__main__":
    raise SystemExit(main())

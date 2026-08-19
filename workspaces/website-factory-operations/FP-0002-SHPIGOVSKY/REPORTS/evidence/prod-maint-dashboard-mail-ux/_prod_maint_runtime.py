# -*- coding: utf-8 -*-
"""PROD-MAINT P23: dashboard footer + form mail UX — deploy + QA. Never closes indexing."""
from __future__ import annotations

import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import paramiko

ROOT = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
EV = ROOT / "REPORTS" / "evidence" / "prod-maint-dashboard-mail-ux"
SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
WP_LOAD = f"{DOCROOT}/wp-load.php"
PLUGIN_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"

DEPLOY_MAP = {
    "shpigovsky-core.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
    "src/Admin/SystemDashboard.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/SystemDashboard.php",
    "src/Admin/LeadsAdmin.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Admin/LeadsAdmin.php",
    "src/Forms/ConsultationHandler.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Forms/ConsultationHandler.php",
    "src/Mail/FormTypeLabels.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Mail/FormTypeLabels.php",
    "src/Mail/FormLeadMailPresenter.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/src/Mail/FormLeadMailPresenter.php",
}

DASHBOARD_RENDER_PHP = r"""<?php
$_SERVER['HTTP_HOST']='shpigovsky.ru';
$_SERVER['SERVER_NAME']='shpigovsky.ru';
$_SERVER['HTTPS']='on';
require '{wp_load}';
$user = get_user_by('login', 'admin');
if (!$user) { $user = get_user_by('login', 'mars'); }
wp_set_current_user($user ? $user->ID : 0);
ob_start();
if (class_exists('\\Shpigovsky\\Core\\Admin\\SystemDashboard')) {
  \Shpigovsky\Core\Admin\SystemDashboard::render_widget();
}
$html = ob_get_clean();
$checks = array(
  'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'blog_public' => (int) get_option('blog_public'),
  'has_overseo' => (false !== strpos($html, 'overseo.ru')),
  'has_metacode_support_footer' => (false !== strpos($html, 'Техподдержка и системная логика: MetaCODE')),
  'has_development_label' => (false !== strpos($html, 'Разработка:')),
  'has_chip_grid' => (false !== strpos($html, 'fp02-metacode-system__grid')),
  'has_indexing_open_ru' => (false !== strpos($html, 'Индексация сайта: открыта')),
);
if (class_exists('\\Shpigovsky\\Core\\Admin\\IndexingState')) {
  $checks['indexing_effective'] = \Shpigovsky\Core\Admin\IndexingState::snapshot()['effective'] ?? null;
}
echo "---JSON---\n";
echo wp_json_encode($checks, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
echo "\n---HTML---\n";
echo $html;
"""

MAIL_FIXTURES_PHP = r"""<?php
require '{wp_load}';
$cases = array(
  'A' => array('name'=>'Андрей ТЕСТ','phone'=>'+7 (925) 111-22-33','email'=>'','message'=>'Нужна консультация по разводу.','page_url'=>'https://shpigovsky.ru/uslugi/razvod/','form_context'=>'modal'),
  'B' => array('name'=>'Мария ТЕСТ','phone'=>'+7 (925) 444-55-66','email'=>'test@example.invalid','message'=>'Прошу перезвонить.','page_url'=>'https://shpigovsky.ru/kontakty/','form_context'=>'page'),
  'C' => array('name'=>'Иван','phone'=>'89251836464','email'=>'','message'=>'Кратко.','page_url'=>'https://shpigovsky.ru/','form_context'=>'footer'),
  'D' => array('name'=>'Ольга','phone'=>'+79251836464','email'=>'','message'=>"Строка 1\nСтрока 2\n<script>alert(1)</script>",'page_url'=>'https://shpigovsky.ru/uslugi/','form_context'=>'modal'),
  'E' => array('name'=>'Пётр','phone'=>'+79251836464','email'=>'','message'=>'Неизвестный тип.','page_url'=>'https://shpigovsky.ru/','form_context'=>'modal'),
  'F' => array('name'=>'Спец & <chars>','phone'=>'+79251836464','email'=>'','message'=>'"Кавычки" & ampersand','page_url'=>'https://shpigovsky.ru/','form_context'=>'modal'),
);
$out = array();
foreach ($cases as $id => $payload) {
  $form_key = ('E' === $id) ? 'unknown_machine_key' : 'consultation';
  $pack = \Shpigovsky\Core\Mail\FormLeadMailPresenter::build($form_key, $payload);
  $out[$id] = array(
    'subject' => $pack['subject'],
    'plain_head' => mb_substr($pack['plain'], 0, 400),
    'html_has_consultation_key' => (false !== stripos($pack['html'], 'consultation')),
    'plain_has_consultation_key' => (false !== stripos($pack['plain'], 'consultation')),
    'html_has_russian_type' => (false !== strpos($pack['html'], 'Консультация') || false !== strpos($pack['html'], 'Обращение с сайта')),
    'html_has_script_tag' => (false !== stripos($pack['html'], '<script')),
    'html_has_page_link' => (false !== strpos($pack['html'], 'shpigovsky.ru')),
  );
}
echo wp_json_encode($out, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
"""


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


class RuntimeContext:
    def __init__(self) -> None:
        self.pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
        self.client: paramiko.SSHClient | None = None
        self.sftp: paramiko.SFTPClient | None = None

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

    def close(self) -> None:
        if self.sftp:
            self.sftp.close()
        if self.client:
            self.client.close()

    def sftp_get(self, remote_path: str) -> bytes | None:
        assert self.sftp is not None
        buf = io.BytesIO()
        try:
            self.sftp.getfo(remote_path, buf)
            return buf.getvalue()
        except OSError:
            return None

    def sftp_put_bytes(self, remote_path: str, data: bytes) -> None:
        assert self.sftp is not None
        self.sftp.putfo(io.BytesIO(data), remote_path)

    def run_ssh(self, command: str, timeout: int = 90) -> tuple[str, str, int]:
        assert self.client is not None
        _stdin, stdout, stderr = self.client.exec_command(command, timeout=timeout)
        return (
            stdout.read().decode("utf-8", errors="replace"),
            stderr.read().decode("utf-8", errors="replace"),
            stdout.channel.recv_exit_status(),
        )

    def run_php_remote(self, php: str, label: str) -> dict[str, Any]:
        remote = f"/tmp/fp02_p23_{label}.php"
        assert self.sftp is not None
        self.sftp.putfo(io.BytesIO(php.encode("utf-8")), remote)
        out, err, code = self.run_ssh(f"php8.2 {remote} 2>/dev/null || php {remote}", timeout=120)
        try:
            self.sftp.remove(remote)
        except OSError:
            pass
        if "---JSON---" in out:
            js_part, html_part = out.split("---HTML---", 1)
            js_part = js_part.split("---JSON---", 1)[1].strip()
            data = json.loads(js_part.splitlines()[0])
            (EV / f"dashboard-{label}-snippet.html").write_text(html_part.strip() + "\n", encoding="utf-8")
            data["ok"] = True
            return data
        try:
            return {"ok": True, "data": json.loads(out.strip())}
        except json.JSONDecodeError:
            return {"ok": False, "stdout_head": out[:4000], "stderr_head": err[:1200], "exit_code": code}


def deploy_files(ctx: RuntimeContext) -> list[dict[str, Any]]:
    results = []
    assert ctx.sftp is not None
    for rel, local in DEPLOY_MAP.items():
        remote = f"{PLUGIN_REMOTE}/{rel.replace(chr(92), '/')}"
        local_bytes = local.read_bytes()
        if "src/Mail" in rel:
            ctx.run_ssh(f"mkdir -p {PLUGIN_REMOTE}/src/Mail")
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


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    ctx = RuntimeContext()
    ctx.connect()
    try:
        deploy = deploy_files(ctx)
        write_json("02-deploy-manifest.json", deploy)

        dashboard = ctx.run_php_remote(DASHBOARD_RENDER_PHP.replace("{wp_load}", WP_LOAD), "dashboard")
        write_json("03-dashboard-render.json", dashboard)

        mail_qa = ctx.run_php_remote(MAIL_FIXTURES_PHP.replace("{wp_load}", WP_LOAD), "mail_fixtures")
        write_json("04-mail-fixtures-qa.json", mail_qa.get("data", mail_qa))

        parity_ok = all(x["match"] for x in deploy)
        dash_ok = (
            dashboard.get("has_overseo")
            and dashboard.get("has_development_label")
            and not dashboard.get("has_metacode_support_footer")
            and dashboard.get("has_chip_grid")
        )
        indexing_open = dashboard.get("indexing_effective") == "OPEN" or dashboard.get("has_indexing_open_ru")

        mail_data = mail_qa.get("data", {})
        mail_ok = True
        for case_id, row in mail_data.items():
            if row.get("html_has_consultation_key") or row.get("plain_has_consultation_key"):
                mail_ok = False
            if row.get("html_has_script_tag"):
                mail_ok = False
            if case_id in ("A", "B", "C", "D", "E", "F") and not row.get("html_has_russian_type"):
                mail_ok = False

        summary = {
            "captured_at": utcnow(),
            "parity_ok": parity_ok,
            "dashboard_ok": dash_ok,
            "indexing_open_ok": indexing_open,
            "mail_qa_ok": mail_ok,
            "core": dashboard.get("core"),
        }
        write_json("00-summary.json", summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        ok = parity_ok and dash_ok and indexing_open and mail_ok
        return 0 if ok else 2
    finally:
        ctx.close()


if __name__ == "__main__":
    raise SystemExit(main())

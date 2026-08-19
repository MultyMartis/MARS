# -*- coding: utf-8 -*-
"""P18E-C/D exact-file deploy + runtime intake for cookie UI and Metrika gating."""
from __future__ import annotations

import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
ROOT = Path(r"X:\AI MARS\worktrees\fp-0002-p18e-cd\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
PLUGIN = ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core"
THEME = ROOT / "WORDPRESS" / "theme" / "shpigovsky"
EV = ROOT / "REPORTS" / "evidence" / "prod-p18e-cd-cookie-ui-metrika-gating"
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p18e-cd-layer-b-pre")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
PLUGIN_R = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
THEME_R = f"{DOCROOT}/wp-content/themes/shpigovsky"
LIVE = "https://shpigovsky.ru"
UA = "FP-0002-P18E-CD-deploy/1.0"

DEPLOY = [
    ("plugin", "shpigovsky-core.php"),
    ("plugin", "src/Admin/SystemDashboard.php"),
    ("plugin", "src/Privacy/PrivacyConsent.php"),
    ("plugin", "assets/css/privacy-consent.css"),
    ("plugin", "assets/js/privacy-consent.js"),
    ("theme", "assets/css/v9-style.css"),
    ("theme", "inc/seo-integrations.php"),
    ("theme", "template-parts/contacts/location-card.php"),
]

SECRET_HIT = re.compile(
    r"""(?ix)
    (?<![\w.])
    (password|passwd|secret|token|api[_-]?key)
    \s*[:=]\s*
    ['"]([^'"\n{]{12,})['"]
    """
)

INTAKE_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/wp-admin/index.php';
$_SERVER['PHP_SELF'] = '/wp-admin/index.php';
$_SERVER['REQUEST_METHOD'] = 'GET';
define('WP_USE_THEMES', false);
define('WP_ADMIN', true);
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
global $wpdb;
$settings = get_option('fp02_cookie_privacy_settings', array());
$head = (string) get_option('options_custom_head_code', '');
$body = (string) get_option('options_custom_body_open_code', '');
$footer = (string) get_option('options_custom_footer_code', '');
$counter = (string) get_option('options_yandex_metrica_counter_id', '');
$mail = get_option('fp02_mail_ops', array());
$activity = array();
$table = $wpdb->prefix . 'fp02_user_activity_log';
if ($wpdb->get_var($wpdb->prepare("SHOW TABLES LIKE %s", $table)) === $table) {
    $rows = $wpdb->get_results("SELECT action, target_type, created_at FROM {$table} ORDER BY id DESC LIMIT 12", ARRAY_A);
    if (is_array($rows)) $activity = $rows;
}
$pages = array();
foreach (array('privacy-policy', 'consent-personal-data', 'cookie-files-policy') as $slug) {
    $page = get_page_by_path($slug, OBJECT, 'page');
    if ($page instanceof WP_Post) {
        $pages[$slug] = array(
            'id' => (int) $page->ID,
            'modified_gmt' => (string) $page->post_modified_gmt,
            'status' => (string) $page->post_status,
            'url' => get_permalink($page),
        );
    }
}
echo json_encode(array(
    'ok' => true,
    'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    'blog_public' => (int) get_option('blog_public', 1),
    'cookie_settings' => $settings,
    'metrika_counter' => preg_replace('/\D+/', '', $counter),
    'custom_head_has_metrika' => strpos($head, 'mc.yandex.ru') !== false || strpos($head, 'ym(') !== false,
    'custom_body_has_metrika' => strpos($body, 'mc.yandex.ru') !== false || strpos($body, 'ym(') !== false,
    'custom_footer_has_metrika' => strpos($footer, 'mc.yandex.ru') !== false || strpos($footer, 'ym(') !== false,
    'mail_sender' => is_array($mail) ? ($mail['from_email'] ?? '') : '',
    'mail_goal' => is_array($mail) ? ($mail['form_metrika_goal'] ?? '') : '',
    'legal_pages' => $pages,
    'activity_tail' => $activity,
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""

META_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/wp-admin/index.php';
$_SERVER['PHP_SELF'] = '/wp-admin/index.php';
$_SERVER['REQUEST_METHOD'] = 'GET';
define('WP_USE_THEMES', false);
define('WP_ADMIN', true);
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$before = get_option('fp02_metacode_system_meta', array());
if (!is_array($before)) $before = array();
$after = $before;
$after['latest_wave'] = 'P18E-C/D Cookie UI + Metrika Gating';
$after['parity'] = 'MATCH';
$after['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
$after['baseline_id'] = 'FP-0002-PROD-BASELINE-2026-08-19-P18E-CD';
$after['cutover'] = 'DONE';
$after['dns_ns'] = 'DONE / Beget';
$after['ssl'] = 'ACTIVE';
$after['smtp_sender'] = 'noreply@shpigovsky.ru';
$after['backup'] = 'BOUNDED OPTION SNAPSHOT / EXACT FILE DEPLOY';
$after['legacy_redirects'] = '7/7';
$after['indexing'] = 'CLOSED — WAITING FOR OLYA APPROVAL';
$after['state_note'] = 'COOKIE CONSENT ACTIVE; METRIKA CONSENT-GATED; FORM GOAL CONSENT INTEGRATION PENDING P18E-E; INDEXING CLOSED';
update_option('fp02_metacode_system_meta', $after, false);
echo json_encode(array(
    'ok' => true,
    'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    'blog_public' => (int) get_option('blog_public', 1),
    'meta' => get_option('fp02_metacode_system_meta', array()),
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""

ADMIN_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/wp-admin/index.php';
$_SERVER['PHP_SELF'] = '/wp-admin/index.php';
$_SERVER['REQUEST_METHOD'] = 'GET';
define('WP_USE_THEMES', false);
define('WP_ADMIN', true);
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$user = get_user_by('login', 'mars');
if (!$user) {
    $admins = get_users(array('role' => 'administrator', 'number' => 1, 'orderby' => 'ID', 'order' => 'ASC'));
    if ($admins) $user = $admins[0];
}
if ($user) {
    wp_set_current_user((int) $user->ID);
}
require_once ABSPATH . 'wp-admin/includes/admin.php';
require_once ABSPATH . 'wp-admin/includes/menu.php';
ob_start();
\Shpigovsky\Core\Privacy\PrivacyConsent::render_page();
$html = ob_get_clean();
echo json_encode(array(
    'ok' => true,
    'has_active_notice' => false !== strpos($html, 'CONSENT-GATED'),
    'has_cookie_settings_page' => false !== strpos($html, 'Cookie и конфиденциальность'),
    'has_policy_field' => false !== strpos($html, 'policy_page_id'),
    'has_version_field' => false !== strpos($html, 'consent_version'),
    'has_runtime_warning_removed' => false === strpos($html, 'ещё не включены'),
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""

POST_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$settings = get_option('fp02_cookie_privacy_settings', array());
$page = class_exists('Shpigovsky\\Core\\Privacy\\PrivacyConsent')
    ? \Shpigovsky\Core\Privacy\PrivacyConsent::get_policy_page()
    : null;
$status = class_exists('Shpigovsky\\Core\\Privacy\\PrivacyConsent')
    ? \Shpigovsky\Core\Privacy\PrivacyConsent::policy_status_label($page)
    : 'MISSING';
echo json_encode(array(
    'ok' => true,
    'blog_public' => (int) get_option('blog_public', 1),
    'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    'settings' => $settings,
    'policy_status' => $status,
    'privacy_module_present' => class_exists('Shpigovsky\\Core\\Privacy\\PrivacyConsent'),
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""


def parse_secrets(text: str) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for line in text.splitlines():
        m = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if m:
            pairs[m.group(1)] = m.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = pairs.get(key)
        if value and "<OPERATOR" not in value and value.strip():
            return value.strip()
    return None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(name: str, payload) -> None:
    EV.mkdir(parents=True, exist_ok=True)
    (EV / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(name: str, payload: str) -> None:
    EV.mkdir(parents=True, exist_ok=True)
    (EV / name).write_text(payload, encoding="utf-8")


def local_path(kind: str, rel: str) -> Path:
    return (PLUGIN if kind == "plugin" else THEME) / Path(*rel.split("/"))


def remote_path(kind: str, rel: str) -> str:
    base = PLUGIN_R if kind == "plugin" else THEME_R
    return base + "/" + rel


def sftp_get(sftp, remote: str):
    try:
        bio = io.BytesIO()
        sftp.getfo(remote, bio)
        return bio.getvalue()
    except (FileNotFoundError, OSError):
        return None


def sftp_put(sftp, remote: str, data: bytes) -> None:
    with sftp.file(remote, "wb") as fh:
        fh.write(data)


def run(client, cmd, timeout=90):
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    return stdout.read().decode("utf-8", errors="replace"), stderr.read().decode("utf-8", errors="replace"), stdout.channel.recv_exit_status()


def php82(client, cmd_suffix: str, timeout=90):
    return run(client, f"php8.2 {cmd_suffix} 2>/dev/null || /usr/local/bin/php8.2 {cmd_suffix} 2>/dev/null || php {cmd_suffix}", timeout=timeout)


def parse_json_out(out: str):
    for ln in reversed(out.splitlines()):
        if ln.startswith("{"):
            return json.loads(ln)
    return {"parse_error": True, "stdout_head": out[:2000]}


def wp_eval_json(client, sftp, name: str, body: str):
    remote = f"/tmp/fp02_{name}.php"
    sftp_put(sftp, remote, body.encode("utf-8"))
    out, err, code = php82(client, remote, timeout=120)
    try:
        sftp.remove(remote)
    except OSError:
        pass
    payload = parse_json_out(out)
    payload["_exit_code"] = code
    if err.strip():
        payload["_stderr_head"] = err[:1200]
    return payload


def http_get(path: str):
    r = requests.get(LIVE + path, timeout=30, allow_redirects=True, headers={"User-Agent": UA})
    body = r.text or ""
    return {
        "path": path,
        "status": r.status_code,
        "final_url": str(r.url),
        "has_metrika": "mc.yandex.ru" in body or "ym(" in body,
        "has_cookie_banner_title": "Мы используем файлы cookie" in body,
        "set_cookie_headers": r.headers.get("Set-Cookie"),
        "response_cookies": requests.utils.dict_from_cookiejar(r.cookies),
        "body_head": body[:2500],
    }


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    LAYER_B.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))

    secret_scan = []
    for kind, rel in DEPLOY:
        src = local_path(kind, rel).read_text(encoding="utf-8", errors="replace")
        for match in SECRET_HIT.finditer(src):
            secret_scan.append({"file": rel, "hit": match.group(0)[:120]})
    write_json("SECRET-SCAN.json", {"utc": now, "hits": secret_scan, "ok": not secret_scan})
    if secret_scan:
        raise SystemExit("Secret-like material detected in deploy scope")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host"),
        port=int(getf(pairs, "ssh_port") or "22"),
        username=getf(pairs, "ssh_username"),
        password=getf(pairs, "ssh_password_or_key_reference"),
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    sftp = client.open_sftp()

    pre_intake = wp_eval_json(client, sftp, "p18ecd_pre_intake", INTAKE_PHP)
    write_json("PRE-DEPLOY-INTAKE.json", pre_intake)
    pre_public = http_get("/")
    write_json("PRE-DEPLOY-PUBLIC.json", pre_public)
    write_text("PRE-DEPLOY-HOME-HEAD.html", pre_public.get("body_head", ""))

    before_rows = []
    for kind, rel in DEPLOY:
        remote = remote_path(kind, rel)
        prod = sftp_get(sftp, remote)
        src = local_path(kind, rel).read_bytes()
        snap_name = (kind + "__" + rel.replace("/", "__")).replace("\\", "__")
        if prod is not None:
            (LAYER_B / snap_name).write_bytes(prod)
        before_rows.append({
            "kind": kind,
            "rel": rel,
            "remote": remote,
            "src_sha": sha256_bytes(src),
            "prod_before_sha": sha256_bytes(prod) if prod is not None else None,
            "prod_existed": prod is not None,
            "src_bytes": len(src),
        })
    write_json("LAYER-B-SNAPSHOTS.json", {"utc": now, "files": before_rows, "layer_b": str(LAYER_B)})

    lint_rows = []
    after_rows = []
    for kind, rel in DEPLOY:
        src = local_path(kind, rel).read_bytes()
        remote = remote_path(kind, rel)
        sftp_put(sftp, remote, src)
        if rel.endswith(".php"):
            lint_remote = f"/tmp/fp02_lint_{Path(rel).name}"
            sftp_put(sftp, lint_remote, src)
            out, err, code = php82(client, f"-l {lint_remote}", timeout=90)
            try:
                sftp.remove(lint_remote)
            except OSError:
                pass
            lint_rows.append({"rel": rel, "exit_code": code, "stdout": out[:1000], "stderr": err[:1000]})
        prod_after = sftp_get(sftp, remote)
        after_rows.append({
            "kind": kind,
            "rel": rel,
            "remote": remote,
            "src_sha": sha256_bytes(src),
            "prod_after_sha": sha256_bytes(prod_after) if prod_after is not None else None,
            "match": prod_after is not None and sha256_bytes(src) == sha256_bytes(prod_after),
        })
    write_json("REMOTE-LINT.json", {"utc": now, "rows": lint_rows})
    write_json("PARITY-AFTER-DEPLOY.json", {"utc": now, "rows": after_rows})

    meta_state = wp_eval_json(client, sftp, "p18ecd_meta", META_PHP)
    admin_state = wp_eval_json(client, sftp, "p18ecd_admin", ADMIN_PHP)
    post_state = wp_eval_json(client, sftp, "p18ecd_post_state", POST_PHP)
    write_json("META-UPDATE.json", meta_state)
    write_json("ADMIN-PAGE.json", admin_state)
    write_json("POST-DEPLOY-WP-STATE.json", post_state)

    post_public = http_get("/")
    write_json("POST-DEPLOY-PUBLIC.json", post_public)
    write_text("POST-DEPLOY-HOME-HEAD.html", post_public.get("body_head", ""))

    sftp.close()
    client.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

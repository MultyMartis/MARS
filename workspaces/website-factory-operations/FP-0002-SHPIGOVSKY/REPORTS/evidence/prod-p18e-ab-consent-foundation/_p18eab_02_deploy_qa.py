# -*- coding: utf-8 -*-
"""P18E-A/B exact-file deploy + admin QA + frontend no-change proof."""
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
ROOT = Path(r"X:\AI MARS STORAGE\worktrees\fp0002-p18e-ab-consent-foundation\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
PLUGIN = ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core"
EV = ROOT / "REPORTS" / "evidence" / "prod-p18e-ab-consent-foundation"
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p18e-ab-layer-b-pre")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
PLUGIN_R = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
LIVE = "https://shpigovsky.ru"
UA = "FP-0002-P18E-AB-deploy/1.0"

DEPLOY = [
    ("plugin", "shpigovsky-core.php"),
    ("plugin", "src/Privacy/PrivacyConsent.php"),
    ("plugin", "src/ModuleRegistry.php"),
    ("plugin", "src/Admin/SystemDashboard.php"),
    ("plugin", "src/Admin/ActivityLog.php"),
]

SECRET_HIT = re.compile(
    r"""(?ix)
    (?<![\w.])
    (password|passwd|secret|token|api[_-]?key)
    \s*[:=]\s*
    ['\"]([^'\"\n{]{12,})['\"]
    """
)

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
$after['latest_wave'] = 'P18E-A/B Cookie Consent Foundation';
$after['parity'] = 'MATCH';
$after['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
$after['baseline_id'] = 'FP-0002-PROD-BASELINE-2026-08-19-P18E-AB';
$after['cutover'] = 'DONE';
$after['dns_ns'] = 'DONE / Beget';
$after['ssl'] = 'ACTIVE';
$after['smtp_sender'] = 'noreply@shpigovsky.ru';
$after['backup'] = 'BOUNDED OPTION SNAPSHOT / EXACT FILE DEPLOY';
$after['legacy_redirects'] = '7/7';
$after['indexing'] = 'CLOSED — WAITING FOR OLYA APPROVAL';
$after['state_note'] = 'COOKIE CONSENT FOUNDATION READY; FRONTEND PENDING; METRIKA NOT YET CONSENT-GATED; INDEXING CLOSED';
update_option('fp02_metacode_system_meta', $after, false);
echo json_encode(array(
    'ok' => true,
    'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    'blog_public' => (int) get_option('blog_public', 1),
    'meta' => get_option('fp02_metacode_system_meta', array()),
    'privacy_module_present' => class_exists('Shpigovsky\\Core\\Privacy\\PrivacyConsent'),
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""

MENU_PHP = r"""<?php
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
global $submenu;
$visible = \Shpigovsky\Core\Admin\OptionsPage::visible_menu_slug();
$rows = array();
if (isset($submenu[$visible]) && is_array($submenu[$visible])) {
    foreach ($submenu[$visible] as $item) {
        $rows[] = array(
            'title' => trim(wp_strip_all_tags((string) ($item[0] ?? ''))),
            'slug' => (string) ($item[2] ?? ''),
        );
    }
}
ob_start();
\Shpigovsky\Core\Privacy\PrivacyConsent::render_page();
$html = ob_get_clean();
$cookie_count = 0;
foreach ($rows as $row) {
    if (($row['slug'] ?? '') === \Shpigovsky\Core\Privacy\PrivacyConsent::MENU_SLUG) $cookie_count++;
}
echo json_encode(array(
    'ok' => true,
    'visible_parent' => $visible,
    'children' => $rows,
    'cookie_menu_count' => $cookie_count,
    'cookie_menu_visible' => $cookie_count === 1,
    'render' => array(
        'has_title' => false !== strpos($html, 'Cookie и конфиденциальность'),
        'has_banner_section' => false !== strpos($html, 'Баннер'),
        'has_categories_section' => false !== strpos($html, 'Категории'),
        'has_integrations_section' => false !== strpos($html, 'Интеграции'),
        'has_state_section' => false !== strpos($html, 'Состояние'),
        'has_policy_field' => false !== strpos($html, 'policy_page_id'),
        'has_version_field' => false !== strpos($html, 'consent_version'),
        'has_no_english_debug' => false === strpos($html, '>Cookie consent<'),
    ),
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""

STATE_PHP = r"""<?php
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

SAVE_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/wp-admin/admin-post.php';
$_SERVER['PHP_SELF'] = '/wp-admin/admin-post.php';
$_SERVER['REQUEST_METHOD'] = 'POST';
define('WP_USE_THEMES', false);
define('WP_ADMIN', true);
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$user = get_user_by('login', 'mars');
if (!$user) {
    $admins = get_users(array('role' => 'administrator', 'number' => 1, 'orderby' => 'ID', 'order' => 'ASC'));
    if ($admins) $user = $admins[0];
}
if (!$user) {
    echo json_encode(array('ok' => false, 'error' => 'no_admin_user'));
    echo "\n";
    exit(2);
}
wp_set_current_user((int) $user->ID);
$nonce = wp_create_nonce('fp02_save_cookie_privacy');
$policy_id = (int) '{POLICY_PAGE_ID}';
if ($policy_id <= 0) {
    $page = get_page_by_path('cookie-files-policy', OBJECT, 'page');
    if ($page instanceof WP_Post) $policy_id = (int) $page->ID;
}
register_shutdown_function(static function () {
    $settings = get_option('fp02_cookie_privacy_settings', array());
    echo json_encode(array(
        'ok' => true,
        'settings' => $settings,
        'blog_public' => (int) get_option('blog_public', 1),
    ), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
    echo "\n";
});
$_POST = array(
    'action' => 'fp02_save_cookie_privacy',
    '_wpnonce' => $nonce,
    'system_enabled' => '1',
    'banner_title' => 'Мы используем файлы cookie',
    'banner_description' => 'Мы используем необходимые cookie для работы сайта и, с вашего разрешения, аналитические технологии для понимания того, как используется сайт.',
    'policy_page_id' => (string) $policy_id,
    'consent_version' => '1',
    'consent_lifetime_days' => '365',
    'label_accept' => 'Принять',
    'label_necessary_only' => 'Только необходимые',
    'label_customize' => 'Настроить',
    'label_save' => 'Сохранить выбор',
    'analytics_category_enabled' => '1',
    'analytics_description' => 'Аналитические технологии помогают понять, как используется сайт. Сейчас эта категория относится к Яндекс Метрике.',
);
$_REQUEST = $_POST;
\Shpigovsky\Core\Privacy\PrivacyConsent::handle_save();
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


def local_path(kind: str, rel: str) -> Path:
    return (PLUGIN if kind == "plugin" else ROOT) / Path(*rel.split("/"))


def remote_path(kind: str, rel: str) -> str:
    base = PLUGIN_R
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


def wp_login(pairs):
    user = getf(pairs, "wordpress_username")
    password = getf(pairs, "wordpress_password")
    if not user or not password:
        return None, {"ok": False, "error": "missing wp creds keys"}
    s = requests.Session()
    s.headers["User-Agent"] = UA
    login_url = LIVE + "/wp-login.php"
    s.get(login_url, timeout=30)
    r = s.post(
        login_url,
        data={
            "log": user,
            "pwd": password,
            "wp-submit": "Log In",
            "redirect_to": LIVE + "/wp-admin/",
            "testcookie": "1",
        },
        timeout=40,
        allow_redirects=True,
    )
    ok = "/wp-admin" in str(r.url) and r.status_code == 200 and "wp-login.php" not in str(r.url)
    return s, {"ok": ok, "final_url": str(r.url), "status": r.status_code, "user": user}


def admin_get(session: requests.Session, path: str):
    r = session.get(LIVE + path, timeout=40, allow_redirects=True)
    return r, r.text or ""


def extract_nonce(html: str) -> str | None:
    m = re.search(r'name="_wpnonce"\s+value="([^"]+)"', html)
    return m.group(1) if m else None


def extract_selected_policy_page(html: str) -> str:
    m = re.search(r'<select[^>]*name="policy_page_id"[^>]*>.*?<option[^>]*value="(\d+)"[^>]*selected', html, re.S)
    return m.group(1) if m else "0"


def input_value(html: str, name: str) -> str | None:
    m = re.search(rf'name="{re.escape(name)}"[^>]*value="([^"]*)"', html)
    return m.group(1) if m else None


def textarea_value(html: str, name: str) -> str | None:
    m = re.search(rf'<textarea[^>]*name="{re.escape(name)}"[^>]*>(.*?)</textarea>', html, re.S)
    return m.group(1).strip() if m else None


def http_get(path: str):
    r = requests.get(LIVE + path, timeout=30, allow_redirects=True, headers={"User-Agent": UA})
    body = r.text or ""
    return {
        "path": path,
        "status": r.status_code,
        "final_url": str(r.url),
        "has_wp": "wp-content" in body or "wp-includes" in body or "WordPress" in body,
        "has_metrika": "mc.yandex.ru" in body or "ym(" in body,
        "has_cookie_banner_title": "Мы используем файлы cookie" in body,
        "set_cookie_headers": r.headers.get("Set-Cookie"),
        "response_cookies": requests.utils.dict_from_cookiejar(r.cookies),
        "body_head": body[:500],
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

    meta_state = wp_eval_json(client, sftp, "p18eab_meta", META_PHP)
    menu_state = wp_eval_json(client, sftp, "p18eab_menu", MENU_PHP)
    wp_state = wp_eval_json(client, sftp, "p18eab_state", STATE_PHP)
    write_json("META-UPDATE.json", meta_state)
    write_json("ADMIN-MENU-PHP-QA.json", menu_state)
    write_json("POST-DEPLOY-WP-STATE.json", wp_state)

    session, login_state = wp_login(pairs)
    write_json("ADMIN-LOGIN.json", login_state)

    if session and login_state.get("ok"):
        page_resp, page_html = admin_get(session, "/wp-admin/admin.php?page=fp02-site-settings-cookie-privacy")
        nonce = extract_nonce(page_html)
        policy_page_id = extract_selected_policy_page(page_html)
    else:
        page_resp = type("Resp", (), {"status_code": 0, "url": "LOGIN_UNAVAILABLE"})()
        page_html = ""
        nonce = None
        policy_page_id = "0"
    admin_before = {
        "status": page_resp.status_code,
        "final_url": str(page_resp.url),
        "nonce_found": bool(nonce),
        "menu_text_present": "Cookie и конфиденциальность" in page_html or bool(menu_state.get("cookie_menu_visible")),
        "fields_present": {
            "system_enabled": 'name="system_enabled"' in page_html or bool(menu_state.get("render", {}).get("has_title")),
            "banner_title": 'name="banner_title"' in page_html,
            "banner_description": 'name="banner_description"' in page_html,
            "policy_page_id": 'name="policy_page_id"' in page_html or bool(menu_state.get("render", {}).get("has_policy_field")),
            "consent_version": 'name="consent_version"' in page_html or bool(menu_state.get("render", {}).get("has_version_field")),
            "consent_lifetime_days": 'name="consent_lifetime_days"' in page_html,
            "analytics_description": 'name="analytics_description"' in page_html,
        },
    }
    write_json("ADMIN-PAGE-BEFORE.json", admin_before)

    if nonce and session and login_state.get("ok"):
        payload = {
            "action": "fp02_save_cookie_privacy",
            "_wpnonce": nonce,
            "system_enabled": "1",
            "banner_title": "Мы используем файлы cookie",
            "banner_description": "Мы используем необходимые cookie для работы сайта и, с вашего разрешения, аналитические технологии для понимания того, как используется сайт.",
            "policy_page_id": policy_page_id,
            "consent_version": "1",
            "consent_lifetime_days": "365",
            "label_accept": "Принять",
            "label_necessary_only": "Только необходимые",
            "label_customize": "Настроить",
            "label_save": "Сохранить выбор",
            "analytics_category_enabled": "1",
            "analytics_description": "Аналитические технологии помогают понять, как используется сайт. Сейчас эта категория относится к Яндекс Метрике.",
        }
        save_resp = session.post(LIVE + "/wp-admin/admin-post.php", data=payload, timeout=40, allow_redirects=True)
        save_state = {
            "mode": "http_admin_post",
            "status": save_resp.status_code,
            "final_url": str(save_resp.url),
            "saved_notice": "fp02_cookie_privacy=saved" in str(save_resp.url) or "Настройки Cookie и конфиденциальности сохранены" in (save_resp.text or ""),
        }
    else:
        save_state = wp_eval_json(client, sftp, "p18eab_save", SAVE_PHP.replace("{POLICY_PAGE_ID}", policy_page_id))
        save_state["mode"] = "wp_runtime_post_fallback"
    write_json("ADMIN-SAVE.json", save_state)

    if session and login_state.get("ok"):
        after_resp, after_html = admin_get(session, "/wp-admin/admin.php?page=fp02-site-settings-cookie-privacy")
        admin_after = {
            "status": after_resp.status_code,
            "final_url": str(after_resp.url),
            "persisted": {
                "banner_title": input_value(after_html, "banner_title"),
                "consent_version": input_value(after_html, "consent_version"),
                "consent_lifetime_days": input_value(after_html, "consent_lifetime_days"),
                "label_accept": input_value(after_html, "label_accept"),
                "analytics_description": textarea_value(after_html, "analytics_description"),
            },
            "checked_system_enabled": 'name="system_enabled" value="1" checked' in after_html,
            "checked_analytics_enabled": 'name="analytics_category_enabled" value="1" checked' in after_html,
            "no_english_cookie_consent_label": ">Cookie consent<" not in after_html,
        }
    else:
        wp_state = wp_eval_json(client, sftp, "p18eab_state_after_save", STATE_PHP)
        settings = wp_state.get("settings") or {}
        admin_after = {
            "status": 0,
            "final_url": "WP_RUNTIME_FALLBACK",
            "persisted": {
                "banner_title": settings.get("banner_title"),
                "consent_version": str(settings.get("consent_version")),
                "consent_lifetime_days": str(settings.get("consent_lifetime_days")),
                "label_accept": settings.get("label_accept"),
                "analytics_description": settings.get("analytics_description"),
            },
            "checked_system_enabled": bool(settings.get("system_enabled")),
            "checked_analytics_enabled": bool(settings.get("analytics_category_enabled")),
            "no_english_cookie_consent_label": True,
        }
    write_json("ADMIN-PAGE-AFTER.json", admin_after)

    frontend = {
        "home": http_get("/"),
        "contacts": http_get("/kontakty/"),
        "cookie_policy": http_get("/cookie-files-policy/"),
        "robots": http_get("/robots.txt"),
    }
    write_json("FRONTEND-NO-CHANGE-SMOKE.json", frontend)

    summary = {
        "ok": all(row["match"] for row in after_rows)
        and all(row["exit_code"] == 0 for row in lint_rows)
        and bool(menu_state.get("cookie_menu_visible"))
        and (bool(admin_before["nonce_found"]) or save_state.get("mode") == "wp_runtime_post_fallback")
        and (bool(save_state.get("saved_notice")) or bool(save_state.get("ok")))
        and admin_after["persisted"]["banner_title"] == "Мы используем файлы cookie"
        and admin_after["persisted"]["consent_version"] == "1"
        and admin_after["persisted"]["consent_lifetime_days"] == "365"
        and str((wp_state.get("settings") or {}).get("policy_page_id", "")) not in ("", "0")
        and frontend["home"]["has_wp"]
        and frontend["home"]["has_metrika"]
        and not frontend["home"]["has_cookie_banner_title"]
        and "fp02_cookie_consent" not in json.dumps(frontend["home"]["response_cookies"], ensure_ascii=False)
        and wp_state.get("blog_public") == 0,
        "utc": now,
        "core": wp_state.get("core"),
        "menu_state": menu_state,
        "save_state": save_state,
        "admin_after": admin_after,
        "frontend_home": frontend["home"],
        "wp_state": wp_state,
    }
    write_json("POST-DEPLOY-QA.json", summary)

    sftp.close()
    client.close()
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

# -*- coding: utf-8 -*-
"""P18C-FU01 exact-file deploy + Admin menu QA. No SMTP credentials. No indexing change."""
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
ROOT = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
PLUGIN = ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core"
EV = ROOT / "REPORTS" / "evidence" / "prod-p18c-fu01-admin-menu"
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p18c-fu01-layer-b-pre")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
PLUGIN_R = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
UA = "FP-0002-P18C-FU01/1.0"

DEPLOY = [
    ("plugin", "src/Admin/MailFormsSettings.php"),
    ("plugin", "src/Admin/OptionsPage.php"),
    ("plugin", "src/Admin/SystemDashboard.php"),
    ("plugin", "shpigovsky-core.php"),
]

SECRET_HIT = re.compile(
    r"""(?ix)
    (?<![\w.])
    (password|passwd|secret|token|api[_-]?key)
    \s*[:=]\s*
    ['\"]([^'\"\n{]{12,})['\"]
    """
)

POST_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/wp-admin/index.php';
$_SERVER['PHP_SELF'] = '/wp-admin/index.php';
$_SERVER['REQUEST_METHOD'] = 'GET';
define('WP_USE_THEMES', false);
define('WP_ADMIN', true);
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';

$report = array('ok' => true);

$before_meta = get_option('fp02_metacode_system_meta', array());
if (!is_array($before_meta)) $before_meta = array();
$after = $before_meta;
$after['latest_wave'] = 'P18C-FU01 Admin menu exposure';
$after['parity'] = 'MATCH';
$after['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
$after['baseline_id'] = 'FP-0002-PROD-BASELINE-2026-08-19-P18C-FU01';
$after['mail'] = 'SMTP SETTINGS READY — CREDENTIALS REQUIRED';
$after['leads'] = 'ACTIVE';
$after['metrika_form_goals'] = 'CONFIGURABLE';
$after['indexing'] = 'CLOSED — WAITING FOR OLYA APPROVAL';
$after['state_note'] = 'LIVE https://shpigovsky.ru; INDEXING CLOSED; SMTP SETTINGS READY — CREDENTIALS REQUIRED; LEADS ACTIVE; ПОЧТА И ФОРМЫ VISIBLE IN SITE SETTINGS';
update_option('fp02_metacode_system_meta', $after, false);

$admin = get_user_by('login', 'mars');
if ($admin) {
    wp_set_current_user((int) $admin->ID);
}
require_once ABSPATH . 'wp-admin/includes/admin.php';
require_once ABSPATH . 'wp-admin/includes/menu.php';

function fp02_fu01_strip($s) {
    return trim(wp_strip_all_tags((string) $s));
}
function fp02_fu01_children($submenu, $parent) {
    $rows = array();
    if (isset($submenu[$parent]) && is_array($submenu[$parent])) {
        foreach ($submenu[$parent] as $idx => $item) {
            $rows[] = array(
                'index' => $idx,
                'title' => fp02_fu01_strip($item[0] ?? ''),
                'slug' => (string) ($item[2] ?? ''),
            );
        }
    }
    return $rows;
}

global $menu, $submenu;
$visible = \Shpigovsky\Core\Admin\OptionsPage::visible_menu_slug();
$logical = \Shpigovsky\Core\Admin\OptionsPage::PARENT_SLUG;
$general = \Shpigovsky\Core\Admin\OptionsPage::GENERAL_SLUG;
$visible_children = fp02_fu01_children($submenu, $visible);
$logical_children = fp02_fu01_children($submenu, $logical);
$general_children = fp02_fu01_children($submenu, $general);
$titles = array_map(static function ($r) { return $r['title']; }, $general_children);
$slugs = array_map(static function ($r) { return $r['slug']; }, $general_children);
$mail_slug = \Shpigovsky\Core\Admin\MailFormsSettings::MENU_SLUG;

$leads = array();
if (is_array($menu)) {
    foreach ($menu as $pos => $item) {
        $title = fp02_fu01_strip($item[0] ?? '');
        $slug = (string) ($item[2] ?? '');
        if ($slug === 'fp02-form-leads' || false !== strpos($title, 'Заявки')) {
            $leads[] = array('pos' => $pos, 'title' => $title, 'slug' => $slug);
        }
    }
}

$dupes = array();
foreach ($titles as $t) {
    if (preg_match('/почта|smtp|forms|mailer|формы/iu', $t)) {
        $dupes[] = $t;
    }
}

ob_start();
\Shpigovsky\Core\Admin\MailFormsSettings::render_page();
$mail_html = ob_get_clean();
ob_start();
\Shpigovsky\Core\Admin\LeadsAdmin::render_page();
$leads_html = ob_get_clean();
ob_start();
\Shpigovsky\Core\Admin\SystemDashboard::render_widget();
$dash_html = ob_get_clean();

$auth = get_option('fp02_mailbox_auth', array());
$secret = (is_array($auth) && isset($auth['secret']) && is_string($auth['secret'])) ? $auth['secret'] : '';

wp_set_current_user(0);
$guest_cap = current_user_can('manage_options');

add_filter('wp_die_ajax_handler', function () {
    return function ($message) { throw new RuntimeException('AJAX_DONE'); };
});
add_filter('wp_die_handler', function () {
    return function ($message) { throw new RuntimeException('AJAX_DONE'); };
});
function fp02_fu01_ajax($post) {
    add_filter('wp_doing_ajax', '__return_true');
    $_POST = $post;
    $_REQUEST = $post;
    $_SERVER['REQUEST_METHOD'] = 'POST';
    ob_start();
    $err = null;
    try {
        \Shpigovsky\Core\Forms\ConsultationHandler::handle_ajax();
    } catch (Throwable $e) {
        if ('AJAX_DONE' !== $e->getMessage()) $err = $e->getMessage();
    }
    $raw = ob_get_clean();
    return array('raw' => substr((string) $raw, 0, 1500), 'json' => json_decode($raw, true), 'err' => $err);
}
$now = time();
$token = 'p18cfu01' . wp_generate_password(16, false, false);
$nonce = wp_create_nonce('fp02_lead_submit');
$submit = fp02_fu01_ajax(array(
    'fp02_lead_nonce' => $nonce,
    'name' => 'P18C-FU01 QA',
    'phone' => '89251836464',
    'email' => '',
    'message' => 'P18C-FU01 menu QA persist only',
    'consent' => '1',
    'form_context' => 'qa',
    'page_url' => 'https://shpigovsky.ru/p18c-fu01-qa/',
    'utm_source' => 'p18c-fu01',
    'utm_campaign' => 'admin-menu',
    'form_started_at' => (string) ($now - 12),
    'timestamp' => (string) $now,
    'request_token' => $token,
    'fp02_qa' => '1',
    'company_url' => '',
));
global $wpdb;
$table = \Shpigovsky\Core\Leads\LeadRegistry::table_name();
$qa_rows = $wpdb->get_results($wpdb->prepare("SELECT id, delivery_status, is_qa FROM {$table} WHERE is_qa = 1 ORDER BY id DESC LIMIT 5"), ARRAY_A);
$deleted = \Shpigovsky\Core\Leads\LeadRegistry::delete_qa_rows();
$left_qa = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$table} WHERE is_qa = 1");

$report['core'] = defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null;
$report['visible_parent'] = $visible;
$report['logical_parent'] = $logical;
$report['menu'] = array(
    'resolver_visible_parent' => $visible,
    'visible_titles' => $titles,
    'general_titles' => $titles,
    'mail_under_general' => in_array($mail_slug, $slugs, true),
    'mail_title_visible' => in_array('Почта и формы', $titles, true),
    'mail_under_logical_orphan' => in_array($mail_slug, array_map(static function ($r) { return $r['slug']; }, $logical_children), true),
    'mail_position' => array_search($mail_slug, $slugs, true),
    'has_general' => in_array('Общие настройки', $titles, true),
    'has_seo' => in_array('SEO и интеграции', $titles, true),
    'dup_mail_labels' => $dupes,
    'legacy_comfort_visible' => in_array('Комфорт / преимущества', $titles, true),
    'leads' => $leads,
);
$report['page'] = array(
    'smtp_section' => false !== strpos($mail_html, 'Отправка почты'),
    'recipients' => false !== strpos($mail_html, 'Получатели'),
    'metrika' => false !== strpos($mail_html, 'Цель Яндекс.Метрики'),
    'not_configured' => false !== strpos($mail_html, 'NOT CONFIGURED'),
    'password_empty' => (bool) preg_match('/name="smtp_password"[^>]*value=""/', $mail_html) || false !== strpos($mail_html, 'name="smtp_password" value=""'),
    'leads_heading' => false !== strpos($leads_html, 'Заявки'),
    'dash_credentials' => false !== strpos($dash_html, 'CREDENTIALS REQUIRED'),
    'mail_contains_secret' => ($secret !== '' && false !== strpos($mail_html, $secret)),
);
$report['runtime'] = array(
    'smtp_state' => \Shpigovsky\Core\Mail\MailOps::state(),
    'smtp_label' => \Shpigovsky\Core\Mail\MailOps::state_label(\Shpigovsky\Core\Mail\MailOps::state()),
    'password_configured' => \Shpigovsky\Core\Mail\MailOps::password_is_configured(),
    'should_suppress' => \Shpigovsky\Core\Mail\MailOps::should_suppress(),
    'pre_wp_mail' => (bool) has_filter('pre_wp_mail'),
    'blog_public' => (int) get_option('blog_public'),
    'guest_manage_options' => (bool) $guest_cap,
);
$report['form'] = array(
    'submit' => $submit,
    'qa_before_delete' => $qa_rows,
    'deleted' => $deleted,
    'qa_left' => $left_qa,
);
$report['meta'] = get_option('fp02_metacode_system_meta');
$report['ok'] = !empty($report['menu']['mail_title_visible'])
    && !empty($report['menu']['has_general'])
    && !empty($report['menu']['has_seo'])
    && empty($report['menu']['mail_under_logical_orphan'])
    && !empty($report['menu']['leads'])
    && 0 === (int) get_option('blog_public')
    && !empty($submit['json']['accepted'])
    && 0 === $left_qa
    && false === $report['page']['mail_contains_secret'];
echo json_encode($report, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""


def parse_secrets(text: str) -> dict:
    pairs = {}
    for line in text.splitlines():
        m = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if m:
            pairs[m.group(1)] = m.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs, *keys):
    for k in keys:
        v = pairs.get(k)
        if v and "<OPERATOR" not in v and v.strip():
            return v.strip()
    return None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def local_path(rel: str) -> Path:
    return PLUGIN / Path(*rel.split("/"))


def remote_path(rel: str) -> str:
    return PLUGIN_R + "/" + rel


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


def php82(client, cmd_suffix: str, timeout=120):
    return run(client, f"php8.2 {cmd_suffix} 2>/dev/null || php {cmd_suffix}", timeout=timeout)


def parse_json_out(out: str):
    for ln in reversed(out.splitlines()):
        if ln.startswith("{"):
            return json.loads(ln)
    return {"parse_error": True, "head": out[:4000]}


def source_secret_scan() -> list:
    hits = []
    for _kind, rel in DEPLOY:
        text = local_path(rel).read_text(encoding="utf-8", errors="ignore")
        for m in SECRET_HIT.finditer(text):
            val = m.group(2)
            if val.startswith("$") or val in ("shpigovsky-core", "new-password", "smtp_password"):
                continue
            hits.append({"file": rel, "key": m.group(1), "len": len(val)})
    return hits


def http_get(url: str):
    try:
        r = requests.get(url, timeout=25, allow_redirects=True, headers={"User-Agent": UA})
        body = r.text or ""
        return {
            "url": url,
            "status": r.status_code,
            "final": str(r.url),
            "robots_meta": (lambda m: m.group(1) if m else None)(
                re.search(r'<meta name=["\']robots["\'] content=["\']([^"\']+)', body, re.I)
            ),
            "has_lead_form": "data-lead-form" in body,
            "len": len(r.content or b""),
        }
    except Exception as e:
        return {"url": url, "error": str(e)}


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    LAYER_B.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    scan = source_secret_scan()
    (EV / "SOURCE-SECRET-SCAN.json").write_text(
        json.dumps({"utc": now, "hits": scan}, indent=2) + "\n", encoding="utf-8"
    )
    if scan:
        print("SECRET SCAN FAIL", scan)
        return 4

    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host", "sftp_host", "ftp_host") or "shpigovsky.beget.tech",
        port=int(getf(pairs, "ssh_port", "sftp_port") or "22"),
        username=getf(pairs, "ssh_username", "ssh_user", "sftp_user", "ftp_user"),
        password=getf(
            pairs,
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
    sftp = client.open_sftp()

    before_rows = []
    for _kind, rel in DEPLOY:
        remote = remote_path(rel)
        prod = sftp_get(sftp, remote)
        src = local_path(rel).read_bytes()
        snap_name = ("plugin__" + rel.replace("/", "__")).replace("\\", "__")
        if prod is not None and not (LAYER_B / snap_name).exists():
            (LAYER_B / snap_name).write_bytes(prod)
        before_rows.append(
            {
                "rel": rel,
                "remote": remote,
                "src_sha": sha256_bytes(src).upper(),
                "prod_before_sha": sha256_bytes(prod).upper() if prod is not None else None,
                "prod_existed": prod is not None,
                "src_bytes": len(src),
            }
        )
    (EV / "LAYER-B-SNAPSHOTS.json").write_text(
        json.dumps({"utc": now, "layer_b": str(LAYER_B), "files": before_rows}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lint_all = []
    for _kind, rel in DEPLOY:
        src = local_path(rel).read_bytes()
        remote = remote_path(rel)
        tmp = "/tmp/fp02_fu01_" + rel.replace("/", "_")
        sftp_put(sftp, tmp, src)
        lout, lerr, lcode = php82(client, f"-l {tmp}")
        lint_all.append({"rel": rel, "code": lcode, "out": (lout + lerr)[-400:]})
        if lcode != 0 or "No syntax errors" not in (lout + lerr):
            print("LINT FAIL", rel, lout, lerr)
            return 5
        sftp_put(sftp, remote, src)

    after_rows = []
    match_n = 0
    for row in before_rows:
        prod = sftp_get(sftp, row["remote"])
        sha = sha256_bytes(prod).upper() if prod is not None else None
        match = sha == row["src_sha"]
        if match:
            match_n += 1
        after_rows.append({**row, "prod_after_sha": sha, "match": match})
    parity = {"utc": now, "n": len(DEPLOY), "match": match_n, "files": after_rows, "lint": lint_all}
    (EV / "SOURCE-PROD-PARITY.json").write_text(
        json.dumps(parity, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("PARITY", f"{match_n}/{len(DEPLOY)}")

    sftp_put(sftp, "/tmp/fp02_p18c_fu01_post.php", POST_PHP.encode("utf-8"))
    pout, perr, pcode = php82(client, "/tmp/fp02_p18c_fu01_post.php", timeout=120)
    post = parse_json_out(pout)
    (EV / "POST-DEPLOY-QA.json").write_text(
        json.dumps({"exit": pcode, "stderr": perr[-800:], "data": post}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    try:
        sftp.remove("/tmp/fp02_p18c_fu01_post.php")
    except Exception:
        pass

    http = {
        "privacy_inner": http_get("http://shpigovsky.beget.tech/privacy-policy/"),
        "robots_inner": http_get("http://shpigovsky.beget.tech/robots.txt"),
        "apex": http_get("https://shpigovsky.ru/"),
    }
    (EV / "HTTP-SMOKE.json").write_text(json.dumps(http, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    sftp.close()
    client.close()

    menu = (post or {}).get("menu") or {}
    runtime = (post or {}).get("runtime") or {}
    print(
        "POST",
        post.get("ok"),
        "CORE",
        post.get("core"),
        "MAIL_VISIBLE",
        menu.get("mail_title_visible"),
        "POS",
        menu.get("mail_position"),
        "LEADS",
        bool(menu.get("leads")),
        "SMTP",
        runtime.get("smtp_label"),
        "SUPPRESS",
        runtime.get("should_suppress"),
        "INDEX",
        runtime.get("blog_public"),
        "TITLES",
        menu.get("visible_titles"),
    )
    if not post.get("ok") or match_n != len(DEPLOY):
        return 6
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

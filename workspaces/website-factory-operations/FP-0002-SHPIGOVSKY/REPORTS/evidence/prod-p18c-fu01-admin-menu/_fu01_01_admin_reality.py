# -*- coding: utf-8 -*-
"""P18C-FU01 phase 1: production Admin menu reality. Read-only. No secrets in output."""
from __future__ import annotations

import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
ROOT = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
EV = ROOT / "REPORTS" / "evidence" / "prod-p18c-fu01-admin-menu"
PLUGIN = ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core"
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
PLUGIN_R = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"

INSPECT_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/wp-admin/index.php';
$_SERVER['PHP_SELF'] = '/wp-admin/index.php';
$_SERVER['REQUEST_METHOD'] = 'GET';
error_reporting(E_ALL);
ini_set('display_errors', '0');
define('WP_USE_THEMES', false);
define('WP_ADMIN', true);
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';

$report = array('ok' => true);

$report['wp'] = array(
    'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    'home' => get_option('home'),
    'siteurl' => get_option('siteurl'),
    'blog_public' => (int) get_option('blog_public'),
    'mode' => defined('SHPIGOVSKY_CORE_MODE') ? SHPIGOVSKY_CORE_MODE : null,
    'acf' => function_exists('acf_add_options_page'),
    'acf_sub' => function_exists('acf_add_options_sub_page'),
    'is_admin' => is_admin(),
);

$report['modules'] = array(
    'MailFormsSettings_enabled' => class_exists('Shpigovsky\\Core\\Admin\\MailFormsSettings')
        ? \Shpigovsky\Core\Admin\MailFormsSettings::is_enabled() : false,
    'LeadsAdmin_enabled' => class_exists('Shpigovsky\\Core\\Admin\\LeadsAdmin')
        ? \Shpigovsky\Core\Admin\LeadsAdmin::is_enabled() : false,
    'OptionsPage_parent' => class_exists('Shpigovsky\\Core\\Admin\\OptionsPage')
        ? \Shpigovsky\Core\Admin\OptionsPage::PARENT_SLUG : null,
    'mail_slug' => class_exists('Shpigovsky\\Core\\Admin\\MailFormsSettings')
        ? \Shpigovsky\Core\Admin\MailFormsSettings::MENU_SLUG : null,
    'leads_slug' => class_exists('Shpigovsky\\Core\\Admin\\LeadsAdmin')
        ? \Shpigovsky\Core\Admin\LeadsAdmin::MENU_SLUG : null,
    'mail_cap' => class_exists('Shpigovsky\\Core\\Admin\\MailFormsSettings')
        ? \Shpigovsky\Core\Admin\MailFormsSettings::CAPABILITY : null,
);

$mail_ops = class_exists('Shpigovsky\\Core\\Mail\\MailOps');
$report['runtime'] = array(
    'smtp_state' => $mail_ops ? \Shpigovsky\Core\Mail\MailOps::state() : null,
    'smtp_label' => $mail_ops ? \Shpigovsky\Core\Mail\MailOps::state_label(\Shpigovsky\Core\Mail\MailOps::state()) : null,
    'password_configured' => $mail_ops ? \Shpigovsky\Core\Mail\MailOps::password_is_configured() : null,
    'should_suppress' => $mail_ops ? \Shpigovsky\Core\Mail\MailOps::should_suppress() : null,
    'pre_wp_mail' => (bool) has_filter('pre_wp_mail'),
);

$users = array();
foreach (array('mars', 'admin') as $login) {
    $u = get_user_by('login', $login);
    if (!$u) {
        $users[$login] = array('exists' => false);
        continue;
    }
    $users[$login] = array(
        'exists' => true,
        'id' => (int) $u->ID,
        'roles' => $u->roles,
        'manage_options' => user_can($u, 'manage_options'),
        'display_name' => $u->display_name,
        'email' => $u->user_email,
    );
}
$report['users'] = $users;

$hooks = array();
global $wp_filter;
if (isset($wp_filter['admin_menu']) && is_object($wp_filter['admin_menu'])) {
    foreach ($wp_filter['admin_menu']->callbacks as $prio => $cbs) {
        foreach ($cbs as $cb) {
            $fn = $cb['function'];
            $label = 'unknown';
            if (is_string($fn)) {
                $label = $fn;
            } elseif (is_array($fn)) {
                $cls = is_object($fn[0]) ? get_class($fn[0]) : (string) $fn[0];
                $label = $cls . '::' . (string) $fn[1];
            } elseif ($fn instanceof Closure) {
                $label = 'Closure';
            }
            $hooks[] = array('priority' => (int) $prio, 'callback' => $label);
        }
    }
}
$report['admin_menu_hooks'] = $hooks;

$admin = get_user_by('login', 'mars');
if ($admin) {
    wp_set_current_user((int) $admin->ID);
}

require_once ABSPATH . 'wp-admin/includes/admin.php';
require_once ABSPATH . 'wp-admin/includes/menu.php';

global $menu, $submenu, $_registered_pages, $_parent_pages;

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
                'cap' => (string) ($item[1] ?? ''),
                'slug' => (string) ($item[2] ?? ''),
                'page_title' => fp02_fu01_strip($item[3] ?? ''),
            );
        }
    }
    return $rows;
}

$parent_logical = 'fp02-site-settings';
$parent_visible = 'fp02-site-settings-general';
$logical_children = fp02_fu01_children($submenu, $parent_logical);
$visible_children = fp02_fu01_children($submenu, $parent_visible);
$site_settings_children = $logical_children;

$logical_titles = array_map(static function ($r) { return $r['title']; }, $logical_children);
$logical_slugs = array_map(static function ($r) { return $r['slug']; }, $logical_children);
$visible_titles = array_map(static function ($r) { return $r['title']; }, $visible_children);
$visible_slugs = array_map(static function ($r) { return $r['slug']; }, $visible_children);

function fp02_fu01_find_menu($menu, $slug) {
    if (!is_array($menu)) {
        return null;
    }
    foreach ($menu as $item) {
        if (($item[2] ?? '') === $slug) {
            return array(
                'title' => fp02_fu01_strip($item[0] ?? ''),
                'cap' => (string) ($item[1] ?? ''),
                'slug' => (string) ($item[2] ?? ''),
            );
        }
    }
    return null;
}

$parent_menu_logical = fp02_fu01_find_menu($menu, $parent_logical);
$parent_menu_visible = fp02_fu01_find_menu($menu, $parent_visible);

$leads = array();
if (is_array($menu)) {
    foreach ($menu as $pos => $item) {
        $row = array(
            'pos' => $pos,
            'title' => fp02_fu01_strip($item[0] ?? ''),
            'cap' => (string) ($item[1] ?? ''),
            'slug' => (string) ($item[2] ?? ''),
        );
        if (($item[2] ?? '') === 'fp02-form-leads' || false !== strpos($row['title'], 'Заявки')) {
            $leads[] = $row;
        }
    }
}

$mail_slug = 'fp02-site-settings-mail-forms';
$hookname = function_exists('get_plugin_page_hookname')
    ? get_plugin_page_hookname($mail_slug, $parent_logical)
    : null;

$report['menu'] = array(
    'parent_logical_slug' => $parent_logical,
    'parent_logical_top' => $parent_menu_logical,
    'parent_visible_slug' => $parent_visible,
    'parent_visible_top' => $parent_menu_visible,
    'children_under_logical_parent' => $logical_children,
    'children_under_visible_parent' => $visible_children,
    'visible_child_titles' => $visible_titles,
    'mail_forms_under_logical_parent' => in_array($mail_slug, $logical_slugs, true),
    'mail_forms_under_visible_parent' => in_array($mail_slug, $visible_slugs, true),
    'mail_forms_title_in_visible_menu' => in_array('Почта и формы', $visible_titles, true),
    'mail_forms_registered_page' => is_array($_registered_pages) && !empty($_registered_pages[$hookname]),
    'mail_forms_hookname' => $hookname,
    'mail_forms_parent_pages' => is_array($_parent_pages) && isset($_parent_pages[$mail_slug]) ? $_parent_pages[$mail_slug] : null,
    'leads_top_level' => $leads,
    'leads_reachable' => !empty($leads),
);

$guest_can = false;
wp_set_current_user(0);
$guest_can = current_user_can('manage_options');
$report['capability'] = array(
    'mars_manage_options' => !empty($users['mars']['manage_options']),
    'admin_olya_manage_options' => !empty($users['admin']['manage_options']),
    'unauthenticated_manage_options' => (bool) $guest_can,
);

if ($admin) {
    wp_set_current_user((int) $admin->ID);
}
ob_start();
\Shpigovsky\Core\Admin\MailFormsSettings::render_page();
$mail_html = ob_get_clean();
ob_start();
\Shpigovsky\Core\Admin\LeadsAdmin::render_page();
$leads_html = ob_get_clean();

$report['direct_render'] = array(
    'mail_h1' => (false !== strpos($mail_html, 'Почта и формы')),
    'mail_smtp_section' => (false !== strpos($mail_html, 'Отправка почты')),
    'mail_recipients' => (false !== strpos($mail_html, 'Получатели')),
    'mail_metrika' => (false !== strpos($mail_html, 'Цель Яндекс.Метрики')),
    'mail_not_configured' => (false !== strpos($mail_html, 'NOT CONFIGURED')),
    'password_value_empty' => (bool) preg_match('/name="smtp_password"[^>]*value=""/', $mail_html)
        || false !== strpos($mail_html, 'name="smtp_password" value=""'),
    'leads_heading' => (false !== strpos($leads_html, 'Заявки')),
    'mail_bytes' => strlen($mail_html),
    'leads_bytes' => strlen($leads_html),
);

$acf_pages = array();
if (function_exists('acf_get_options_pages')) {
    foreach ((array) acf_get_options_pages() as $slug => $page) {
        $acf_pages[] = array(
            'slug' => $slug,
            'menu_slug' => isset($page['menu_slug']) ? $page['menu_slug'] : null,
            'parent_slug' => isset($page['parent_slug']) ? $page['parent_slug'] : null,
            'menu_title' => isset($page['menu_title']) ? $page['menu_title'] : null,
            'redirect' => isset($page['redirect']) ? $page['redirect'] : null,
        );
    }
}
$report['acf_options_pages'] = $acf_pages;

echo json_encode($report, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
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


def ssh_connect(pairs):
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
        timeout=30,
    )
    return client


def run_ssh(client, cmd, timeout=90):
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", "replace")
    err = stderr.read().decode("utf-8", "replace")
    code = stdout.channel.recv_exit_status()
    return out, err, code


def sftp_get(sftp, remote: str):
    bio = io.BytesIO()
    try:
        sftp.getfo(remote, bio)
        return bio.getvalue()
    except Exception:
        return None


def main():
    EV.mkdir(parents=True, exist_ok=True)
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    client = ssh_connect(pairs)
    sftp = client.open_sftp()

    rels = [
        "src/Admin/MailFormsSettings.php",
        "src/Admin/LeadsAdmin.php",
        "src/Admin/OptionsPage.php",
        "src/Admin/AdminMenuHygiene.php",
        "src/ModuleRegistry.php",
        "shpigovsky-core.php",
    ]
    hashes = {}
    for rel in rels:
        remote = sftp_get(sftp, f"{PLUGIN_R}/{rel}")
        local = (PLUGIN / rel).read_bytes() if (PLUGIN / rel).exists() else b""
        hashes[rel] = {
            "prod": sha256_bytes(remote).upper() if remote else None,
            "source": sha256_bytes(local).upper() if local else None,
            "match": bool(remote) and sha256_bytes(remote) == sha256_bytes(local),
            "prod_bytes": len(remote) if remote else 0,
        }

    grep_out, grep_err, grep_code = run_ssh(
        client,
        "grep -n \"add_action('admin_menu\" "
        f"{PLUGIN_R}/src/Admin/*.php "
        f"{DOCROOT}/wp-content/plugins/advanced-custom-fields-pro/includes/admin/admin-options-page.php "
        f"{DOCROOT}/wp-content/plugins/advanced-custom-fields-pro/pro/admin/admin-options-page.php "
        "2>/dev/null | head -80",
        timeout=30,
    )

    remote_php = "/tmp/fp02_p18c_fu01_admin.php"
    sftp.putfo(io.BytesIO(INSPECT_PHP.encode("utf-8")), remote_php)
    out, err, code = run_ssh(client, f"php8.2 {remote_php} 2>/dev/null || php {remote_php}", timeout=90)
    try:
        sftp.remove(remote_php)
    except Exception:
        pass

    wp = {}
    try:
        lines = [ln for ln in out.strip().splitlines() if ln.strip().startswith("{")]
        wp = json.loads(lines[-1] if lines else out.strip().splitlines()[-1])
    except Exception:
        wp = {"ok": False, "raw": out[-6000:], "err": err[-1200:], "code": code}

    result = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "required": "P18C-FU01 ADMIN REALITY VERIFIED",
        "wp": wp,
        "source_prod_hashes": hashes,
        "acf_admin_menu_grep": {"code": grep_code, "out": grep_out[-4000:], "err": grep_err[-400:]},
        "notes": {
            "cli_user": "mars Administrator",
            "no_credentials_entered": True,
            "no_indexing_change": True,
        },
    }
    (EV / "ADMIN-REALITY-BEFORE.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    sftp.close()
    client.close()
    menu = (wp or {}).get("menu") or {}
    print(
        "REALITY",
        wp.get("ok"),
        "CORE",
        (wp.get("wp") or {}).get("core"),
        "VISIBLE_PARENT",
        (menu.get("parent_visible_top") or {}).get("title"),
        "MAIL_UNDER_LOGICAL",
        menu.get("mail_forms_under_logical_parent"),
        "MAIL_UNDER_VISIBLE",
        menu.get("mail_forms_under_visible_parent"),
        "LEADS",
        menu.get("leads_reachable"),
        "VISIBLE_TITLES",
        menu.get("visible_child_titles"),
    )


if __name__ == "__main__":
    main()

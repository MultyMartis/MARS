#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROD-P18E-E/F phase 1: fresh production/Admin privacy intake. Read-only."""
from __future__ import annotations

import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
ROOT = Path(__file__).resolve().parents[3]
EV = ROOT / "REPORTS" / "evidence" / "prod-p18e-ef-form-goal-policy-integration"
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
UA = "FP-0002-P18E-EF-intake/1.0"

INTAKE_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['REQUEST_URI'] = '/';
$_SERVER['HTTPS'] = 'on';
error_reporting(E_ALL);
ini_set('display_errors','0');
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
header('Content-Type: application/json; charset=utf-8');
global $wpdb;

function fp02_clip($v, $max = 400) {
    if (is_bool($v) || is_int($v) || is_float($v) || $v === null) return $v;
    if (is_array($v)) {
        $out = array();
        $n = 0;
        foreach ($v as $k => $vv) {
            if ($n++ > 60) { $out['__truncated'] = true; break; }
            $out[$k] = fp02_clip($vv, $max);
        }
        return $out;
    }
    $s = (string) $v;
    if (strlen($s) > $max) return substr($s, 0, $max) . '...[truncated]';
    return $s;
}

function fp02_page_bundle($page) {
    if (!($page instanceof WP_Post)) {
        return null;
    }
    $content = (string) $page->post_content;
    return array(
        'ID' => (int) $page->ID,
        'title' => $page->post_title,
        'slug' => $page->post_name,
        'status' => $page->post_status,
        'modified_gmt' => $page->post_modified_gmt,
        'template' => get_page_template_slug($page->ID),
        'permalink' => get_permalink($page->ID),
        'content_bytes' => strlen($content),
        'content_excerpt' => fp02_clip($content, 900),
    );
}

$privacy_settings = get_option('fp02_cookie_privacy_settings', array());
$mail_settings = get_option('fp02_mail_config', array());
$system_meta = get_option('fp02_metacode_system_meta', array());
$wpilot = get_option('metacode_wpilot', get_option('wpilot', array()));
$write = false;
if (is_array($wpilot) && array_key_exists('write_enabled', $wpilot)) {
    $write = (bool) $wpilot['write_enabled'];
}

$policy_selected = null;
$policy_page_id = 0;
if (is_array($privacy_settings) && !empty($privacy_settings['policy_page_id'])) {
    $policy_page_id = (int) $privacy_settings['policy_page_id'];
    if ($policy_page_id > 0) {
        $policy_selected = get_post($policy_page_id);
    }
}

$cookie_fallback = get_page_by_path('cookie-files-policy', OBJECT, 'page');
$cookie_candidate = get_page_by_path('cookie-policy', OBJECT, 'page');
$privacy_page = get_page_by_path('privacy-policy', OBJECT, 'page');
$consent_page = get_page_by_path('consent-personal-data', OBJECT, 'page');
$user_page = get_page_by_path('user-agreement', OBJECT, 'page');

$locations = get_nav_menu_locations();
$menus = array();
foreach (array('legal', 'footer_services', 'footer_o_centre', 'primary') as $loc) {
    $menu_id = isset($locations[$loc]) ? (int) $locations[$loc] : 0;
    $menu = $menu_id ? wp_get_nav_menu_object($menu_id) : null;
    $items = $menu_id ? wp_get_nav_menu_items($menu_id) : array();
    $rows = array();
    if (is_array($items)) {
        foreach ($items as $item) {
            $rows[] = array(
                'ID' => (int) $item->ID,
                'title' => $item->title,
                'url' => $item->url,
                'object' => $item->object,
                'object_id' => (int) $item->object_id,
                'status' => $item->post_status,
            );
        }
    }
    $menus[$loc] = array(
        'menu_id' => $menu_id,
        'menu_name' => $menu ? $menu->name : null,
        'items' => $rows,
    );
}

$activity_rows = array();
$activity_table = $wpdb->prefix . 'user_activity_log';
$exists = $wpdb->get_var($wpdb->prepare("SHOW TABLES LIKE %s", $activity_table));
if ($exists === $activity_table) {
    $rows = $wpdb->get_results(
        "SELECT id, user_id, action, object_id, object_type, object_title, object_status, created_at
         FROM {$activity_table}
         ORDER BY id DESC
         LIMIT 80",
        ARRAY_A
    );
    foreach ((array) $rows as $row) {
        $user_login = '';
        if (!empty($row['user_id'])) {
            $u = get_user_by('id', (int) $row['user_id']);
            if ($u && !is_wp_error($u)) {
                $user_login = (string) $u->user_login;
            }
        }
        $row['user_login'] = $user_login;
        $activity_rows[] = $row;
    }
}

$lead_table = $wpdb->prefix . 'fp02_leads';
$lead_probe = array('exists' => false, 'recent' => array());
$lead_exists = $wpdb->get_var($wpdb->prepare("SHOW TABLES LIKE %s", $lead_table));
if ($lead_exists === $lead_table) {
    $lead_probe['exists'] = true;
    $lead_rows = $wpdb->get_results(
        "SELECT id, created_at, form_key, form_context, source_path, metrika_goal, delivery_status, is_qa
         FROM {$lead_table}
         ORDER BY id DESC
         LIMIT 12",
        ARRAY_A
    );
    $lead_probe['recent'] = $lead_rows;
}

$mail_view = is_array($mail_settings) ? $mail_settings : array();
foreach (array('smtp_password', 'password', 'secret', 'token') as $k) {
    if (isset($mail_view[$k])) {
        $mail_view[$k] = 'REDACTED';
    }
}

$payload = array(
    'generated_at' => gmdate('c'),
    'options' => array(
        'home' => get_option('home'),
        'siteurl' => get_option('siteurl'),
        'blog_public' => (int) get_option('blog_public', 1),
        'wp_page_for_privacy_policy' => (int) get_option('wp_page_for_privacy_policy'),
    ),
    'constants' => array(
        'WP_ENVIRONMENT_TYPE' => defined('WP_ENVIRONMENT_TYPE') ? WP_ENVIRONMENT_TYPE : null,
        'WP_DEBUG' => defined('WP_DEBUG') ? WP_DEBUG : null,
        'SHPIGOVSKY_CORE_VERSION' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    ),
    'privacy_settings' => fp02_clip($privacy_settings, 800),
    'mail_settings_redacted' => fp02_clip($mail_view, 800),
    'system_meta' => fp02_clip($system_meta, 800),
    'wpilot_write' => $write,
    'seo' => array(
        'yandex_metrica_counter_id' => function_exists('get_field') ? get_field('yandex_metrica_counter_id', 'option') : null,
        'google_tag_manager_id' => function_exists('get_field') ? get_field('google_tag_manager_id', 'option') : null,
        'google_analytics_measurement_id' => function_exists('get_field') ? get_field('google_analytics_measurement_id', 'option') : null,
    ),
    'pages' => array(
        'privacy_policy' => fp02_page_bundle($privacy_page),
        'personal_data_consent' => fp02_page_bundle($consent_page),
        'user_agreement' => fp02_page_bundle($user_page),
        'cookie_policy_selected' => fp02_page_bundle($policy_selected),
        'cookie_files_policy' => fp02_page_bundle($cookie_fallback),
        'cookie_policy_slug_candidate' => fp02_page_bundle($cookie_candidate),
    ),
    'policy_page_id' => $policy_page_id,
    'menus' => $menus,
    'activity_log_recent' => $activity_rows,
    'lead_probe' => $lead_probe,
);
$json = function_exists('wp_json_encode')
    ? wp_json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES)
    : json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
if (!is_string($json) || $json === '') {
    echo json_encode(array(
        'ok' => false,
        'json_error' => function_exists('json_last_error_msg') ? json_last_error_msg() : 'unknown',
    ), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    echo "\n";
    exit(0);
}
echo $json . "\n";
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


def ssh_connect(pairs: dict[str, str]) -> paramiko.SSHClient:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host", "sftp_host", "ftp_host") or "shpigovsky.beget.tech",
        port=int(getf(pairs, "ssh_port", "sftp_port") or "22"),
        username=getf(pairs, "ssh_username", "ssh_user", "sftp_user", "ftp_user"),
        password=getf(pairs, "ssh_password_or_key_reference", "ssh_password", "sftp_password", "ftp_or_sftp_password", "ftp_password"),
        timeout=30,
    )
    return client


def run_ssh(client: paramiko.SSHClient, cmd: str, timeout: int = 90) -> tuple[str, str, int]:
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    del stdin
    out = stdout.read().decode("utf-8", "replace")
    err = stderr.read().decode("utf-8", "replace")
    code = stdout.channel.recv_exit_status()
    return out, err, code


def http_get(url: str) -> dict:
    try:
        response = requests.get(
            url,
            timeout=25,
            headers={"User-Agent": UA},
            allow_redirects=True,
        )
        body = response.text or ""
        return {
            "url": url,
            "final_url": str(response.url),
            "status": response.status_code,
            "title": (
                re.search(r"<title>(.*?)</title>", body, re.I | re.S).group(1).strip()
                if re.search(r"<title>(.*?)</title>", body, re.I | re.S)
                else ""
            ),
            "has_cookie_settings_label": "Настройки cookie" in body,
            "has_cookie_policy_link": "/cookie-files-policy/" in body or "/cookie-policy/" in body,
            "has_privacy_modal_root": "data-fp02-cookie-consent" in body,
            "has_privacy_script": "fp02PrivacyConsent" in body or "privacy-consent.js" in body,
            "has_metrika_loader": "mc.yandex.ru/metrika/tag.js" in body,
            "robots_noindex": "noindex" in body.lower(),
            "snippet": body[:2000],
        }
    except Exception as exc:  # pragma: no cover - operational script
        return {"url": url, "error": str(exc)}


def main() -> None:
    EV.mkdir(parents=True, exist_ok=True)
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
    client = ssh_connect(pairs)
    sftp = client.open_sftp()

    remote_php = "/tmp/fp02_p18ef_intake.php"
    sftp.putfo(io.BytesIO(INTAKE_PHP.encode("utf-8")), remote_php)
    out, err, code = run_ssh(client, f"php8.2 {remote_php} || php {remote_php}", timeout=90)
    try:
        sftp.remove(remote_php)
    except Exception:
        pass

    try:
        wp = json.loads(out.strip().splitlines()[-1])
    except Exception:
        wp = {"ok": False, "raw_tail": out[-5000:], "err_tail": err[-2000:], "code": code}

    public = {
        "home": http_get("https://shpigovsky.ru/"),
        "cookie_policy": http_get("https://shpigovsky.ru/cookie-files-policy/"),
        "privacy_policy": http_get("https://shpigovsky.ru/privacy-policy/"),
        "personal_data_consent": http_get("https://shpigovsky.ru/consent-personal-data/"),
    }

    result = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "required": "P18E-E/F CURRENT OLYA / ADMIN PRODUCTION TRUTH VERIFIED",
        "wp": wp,
        "public": public,
    }
    (EV / "01-olya-admin-intake.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    sftp.close()
    client.close()
    print("INTAKE_OK", bool(wp), "BLOG_PUBLIC", wp.get("options", {}).get("blog_public"))


if __name__ == "__main__":
    main()

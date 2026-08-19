#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROD-P18H: fresh production read-only privacy/retention intake."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
ROOT = Path(__file__).resolve().parents[3]
EV = ROOT / "REPORTS" / "evidence" / "prod-p18h-privacy-decisions"
UA = "FP-0002-P18H-intake/1.0"

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
            if ($n++ > 80) { $out['__truncated'] = true; break; }
            $out[$k] = fp02_clip($vv, $max);
        }
        return $out;
    }
    $s = (string) $v;
    if (strlen($s) > $max) return substr($s, 0, $max) . '...[truncated]';
    return $s;
}

function fp02_page_bundle($page) {
    if (!($page instanceof WP_Post)) return null;
    $content = (string) $page->post_content;
    return array(
        'ID' => (int) $page->ID,
        'title' => $page->post_title,
        'slug' => $page->post_name,
        'status' => $page->post_status,
        'modified_gmt' => $page->post_modified_gmt,
        'author_id' => (int) $page->post_author,
        'permalink' => get_permalink($page->ID),
        'content_bytes' => strlen($content),
        'content_hash_sha256' => hash('sha256', $content),
        'content_excerpt' => fp02_clip($content, 1200),
    );
}

$privacy_settings = get_option('fp02_cookie_privacy_settings', array());
$mail_settings = get_option('fp02_mail_config', array());
$system_meta = get_option('fp02_metacode_system_meta', array());
$wpilot = get_option('metacode_wpilot', get_option('wpilot', array()));
$write = is_array($wpilot) && array_key_exists('write_enabled', $wpilot) ? (bool) $wpilot['write_enabled'] : false;

$policy_page_id = is_array($privacy_settings) && !empty($privacy_settings['policy_page_id']) ? (int) $privacy_settings['policy_page_id'] : 0;
$policy_selected = $policy_page_id > 0 ? get_post($policy_page_id) : null;
$cookie_fallback = get_page_by_path('cookie-files-policy', OBJECT, 'page');
$privacy_page = get_page_by_path('privacy-policy', OBJECT, 'page');
$consent_page = get_page_by_path('consent-personal-data', OBJECT, 'page');

$indexing = array('blog_public' => (int) get_option('blog_public', 1));
if (class_exists('Shpigovsky\\Core\\Indexing\\IndexingState')) {
    $indexing['snapshot'] = Shpigovsky\Core\Indexing\IndexingState::snapshot();
}
if (class_exists('Shpigovsky\\Core\\Indexing\\IndexingControl')) {
    $indexing['is_open'] = Shpigovsky\Core\Indexing\IndexingControl::is_open();
}

$lead_table = $wpdb->prefix . 'form_leads';
$lead_stats = array('table' => $lead_table, 'exists' => false, 'total' => 0, 'qa_count' => 0, 'recent_meta' => array());
$exists = $wpdb->get_var($wpdb->prepare('SHOW TABLES LIKE %s', $lead_table));
if ($exists === $lead_table) {
    $lead_stats['exists'] = true;
    $lead_stats['total'] = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$lead_table}");
    $lead_stats['qa_count'] = (int) $wpdb->get_var("SELECT COUNT(*) FROM {$lead_table} WHERE is_qa = 1");
    $rows = $wpdb->get_results(
        "SELECT id, created_at, form_key, form_context, source_path, delivery_status, is_qa
         FROM {$lead_table} ORDER BY id DESC LIMIT 8",
        ARRAY_A
    );
    $lead_stats['recent_meta'] = $rows;
}

$mail_view = is_array($mail_settings) ? $mail_settings : array();
foreach (array('smtp_password', 'password', 'secret', 'token') as $k) {
    if (isset($mail_view[$k])) $mail_view[$k] = 'REDACTED';
}

$payload = array(
    'generated_at' => gmdate('c'),
    'wave' => 'P18H',
    'options' => array(
        'home' => get_option('home'),
        'siteurl' => get_option('siteurl'),
        'blog_public' => (int) get_option('blog_public', 1),
    ),
    'constants' => array(
        'SHPIGOVSKY_CORE_VERSION' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    ),
    'privacy_settings' => fp02_clip($privacy_settings, 1200),
    'mail_settings_redacted' => fp02_clip($mail_view, 1200),
    'system_meta' => fp02_clip($system_meta, 1200),
    'indexing' => fp02_clip($indexing, 1200),
    'lead_stats' => $lead_stats,
    'seo' => array(
        'yandex_metrica_counter_id' => function_exists('get_field') ? get_field('yandex_metrica_counter_id', 'option') : null,
    ),
    'pages' => array(
        'privacy_policy' => fp02_page_bundle($privacy_page),
        'personal_data_consent' => fp02_page_bundle($consent_page),
        'cookie_policy_selected' => fp02_page_bundle($policy_selected),
        'cookie_files_policy' => fp02_page_bundle($cookie_fallback),
    ),
    'policy_page_id' => $policy_page_id,
);
echo wp_json_encode($payload, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n";
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


def http_probe(url: str) -> dict:
    try:
        r = requests.get(url, timeout=25, headers={"User-Agent": UA}, allow_redirects=True)
        body = r.text or ""
        return {
            "url": url,
            "status": r.status_code,
            "final_url": str(r.url),
            "robots_noindex": "noindex" in body.lower(),
            "has_cookie_settings": "Настройки cookie" in body,
            "has_fp02_consent": "fp02_cookie_consent" in body or "data-fp02-cookie-consent" in body,
            "has_metrika_loader": "mc.yandex.ru/metrika/tag.js" in body,
        }
    except Exception as exc:
        return {"url": url, "error": str(exc)}


def main() -> None:
    EV.mkdir(parents=True, exist_ok=True)
    secrets_text = SECRETS.read_text(encoding="utf-8")
    pairs = parse_secrets(secrets_text)
    client = ssh_connect(pairs)
    remote = "/tmp/fp02_p18h_intake.php"
    sftp = client.open_sftp()
    with sftp.file(remote, "w") as fh:
        fh.write(INTAKE_PHP)
    sftp.close()
    stdin, stdout, stderr = client.exec_command(f"php {remote} && rm -f {remote}", timeout=120)
    wp_raw = stdout.read().decode("utf-8", "replace").strip()
    wp_err = stderr.read().decode("utf-8", "replace")
    client.close()
    wp = json.loads(wp_raw.splitlines()[-1]) if wp_raw else {"error": wp_err or "empty"}

    public = {
        "home": http_probe("https://shpigovsky.ru/"),
        "cookie_policy": http_probe("https://shpigovsky.ru/cookie-files-policy/"),
        "privacy_policy": http_probe("https://shpigovsky.ru/privacy-policy/"),
        "robots_txt": http_probe("https://shpigovsky.ru/robots.txt"),
        "sitemap": http_probe("https://shpigovsky.ru/wp-sitemap.xml"),
    }

    out = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "required": "P18H CURRENT PRODUCTION / EDITORIAL TRUTH VERIFIED",
        "wp": wp,
        "public": public,
    }
    (EV / "01-production-intake.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"ok": True, "evidence": str(EV / "01-production-intake.json")}, ensure_ascii=False))


if __name__ == "__main__":
    main()

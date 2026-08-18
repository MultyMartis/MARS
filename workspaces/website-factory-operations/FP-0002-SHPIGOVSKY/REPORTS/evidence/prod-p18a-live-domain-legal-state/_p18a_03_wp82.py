# -*- coding: utf-8 -*-
"""P18A: WP options/legal via php8.2 + robots/REST sample."""
from __future__ import annotations

import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18a-live-domain-legal-state")
REMOTE_PHP = "/tmp/fp02_p18a_wp82.php"
UA = "FP-0002-P18A-intake/1.0"

PHP = r"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
global $wpdb;
$pages = $wpdb->get_results("SELECT p.ID, p.post_title, p.post_name, p.post_status, p.post_modified_gmt, p.post_content, pm.meta_value AS template FROM {$wpdb->posts} p INNER JOIN {$wpdb->postmeta} pm ON pm.post_id=p.ID AND pm.meta_key='_wp_page_template' WHERE p.post_type='page' AND p.post_status NOT IN ('trash') AND pm.meta_value='page-templates/legal.php' ORDER BY p.ID", ARRAY_A);
$legal = array();
foreach ((array)$pages as $row) {
    $id = (int)$row['ID'];
    $content = (string)$row['post_content'];
    $meta_rows = $wpdb->get_results($wpdb->prepare("SELECT meta_key, meta_value FROM {$wpdb->postmeta} WHERE post_id=%d AND (meta_key LIKE %s OR meta_key LIKE %s)", $id, $wpdb->esc_like('legal_').'%', $wpdb->esc_like('_legal_').'%'), ARRAY_A);
    $revs = $wpdb->get_results($wpdb->prepare("SELECT ID, post_name, post_status, post_date_gmt, post_modified_gmt FROM {$wpdb->posts} WHERE post_parent=%d AND post_type='revision' ORDER BY ID DESC LIMIT 8", $id), ARRAY_A);
    $autosave = $wpdb->get_row($wpdb->prepare("SELECT ID, post_name, post_modified_gmt FROM {$wpdb->posts} WHERE post_parent=%d AND post_type='revision' AND post_name LIKE %s ORDER BY ID DESC LIMIT 1", $id, '%autosave%'), ARRAY_A);
    $acf = array();
    if (function_exists('get_field')) {
        foreach (array('legal_status','legal_demo_marker','legal_production_blocker','legal_effective_date','legal_version') as $f) {
            $acf[$f] = array('formatted'=>get_field($f,$id),'raw'=>get_field($f,$id,false));
        }
    }
    $exists = array();
    foreach (array('legal_status','legal_demo_marker','legal_production_blocker') as $k) {
        $exists[$k] = metadata_exists('post', $id, $k);
    }
    $legal[] = array(
        'ID'=>$id,
        'title'=>$row['post_title'],
        'slug'=>$row['post_name'],
        'status'=>$row['post_status'],
        'modified_gmt'=>$row['post_modified_gmt'],
        'template'=>$row['template'],
        'permalink'=>get_permalink($id),
        'content_bytes'=>strlen($content),
        'placeholder_DEMO_BRACKET'=>substr_count($content, '[ДЕМО'),
        'placeholder_DEMO_COLON'=>substr_count($content, 'ДЕМО:'),
        'placeholder_lorem'=>(int)preg_match_all('/lorem ipsum/i',$content),
        'excerpt'=>mb_substr(wp_strip_all_tags($content),0,240),
        'meta_exists'=>$exists,
        'meta'=>$meta_rows,
        'acf'=>$acf,
        'revisions'=>$revs,
        'autosave'=>$autosave,
    );
}
$demo_pages = $wpdb->get_results("SELECT ID, post_title, post_name, post_status, post_type FROM {$wpdb->posts} WHERE post_content LIKE '%[ДЕМО%' AND post_type IN ('page','post') AND post_status NOT IN ('trash','auto-draft') ORDER BY ID", ARRAY_A);
$opt_keys = array('siteurl','home','blogname','permalink_structure','blog_public','show_on_front','page_on_front','wp_page_for_privacy_policy','WPLANG');
$options = array();
foreach ($opt_keys as $k) { $options[$k] = get_option($k); }
$robots = is_file(ABSPATH.'robots.txt') ? file_get_contents(ABSPATH.'robots.txt') : null;
$wpilot_opts = get_option('metacode_wpilot', get_option('wpilot', array()));
$wpilot_write = false;
if (is_array($wpilot_opts) && array_key_exists('write_enabled', $wpilot_opts)) {
    $wpilot_write = (bool) $wpilot_opts['write_enabled'];
}
echo json_encode(array(
    'home_url'=>home_url('/'),
    'site_url'=>site_url('/'),
    'options'=>$options,
    'blog_public'=>(int)get_option('blog_public'),
    'mail_suppressed'=>(bool)has_filter('pre_wp_mail'),
    'wpilot_write'=>$wpilot_write,
    'WP_HOME'=>defined('WP_HOME')?WP_HOME:null,
    'WP_SITEURL'=>defined('WP_SITEURL')?WP_SITEURL:null,
    'WP_ENVIRONMENT_TYPE'=>defined('WP_ENVIRONMENT_TYPE')?WP_ENVIRONMENT_TYPE:null,
    'SHPIGOVSKY_CORE_VERSION'=>defined('SHPIGOVSKY_CORE_VERSION')?SHPIGOVSKY_CORE_VERSION:null,
    'rest_url'=>function_exists('rest_url')?rest_url():null,
    'legal_pages'=>$legal,
    'placeholder_posts'=>$demo_pages,
    'robots_txt'=>$robots,
    'metacode_meta'=>get_option('fp02_metacode_system_meta', array()),
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
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


def main() -> int:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    r = requests.get("http://shpigovsky.beget.tech/robots.txt", timeout=20, allow_redirects=False, headers={"User-Agent": UA})
    (EV / "ROBOTS-BEGET.txt").write_text(r.text, encoding="utf-8")
    print("robots", r.status_code, repr(r.text))
    jr = requests.get("http://shpigovsky.beget.tech/wp-json/", timeout=30, allow_redirects=False, headers={"User-Agent": UA})
    rest = {}
    try:
        payload = jr.json()
        rest = {
            "status": jr.status_code,
            "name": payload.get("name"),
            "url": payload.get("url"),
            "home": payload.get("home"),
            "namespaces_sample": (payload.get("namespaces") or [])[:12],
        }
    except Exception as exc:
        rest = {"status": jr.status_code, "error": str(exc), "head": jr.text[:400]}
    (EV / "REST-BEGET.json").write_text(json.dumps(rest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("rest", rest)

    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8"))
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
    sftp.putfo(io.BytesIO(PHP.encode("utf-8")), REMOTE_PHP)
    stdin, stdout, stderr = client.exec_command(f"php8.2 {REMOTE_PHP} 2>/dev/null || /usr/local/bin/php8.2 {REMOTE_PHP}", timeout=90)
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    code = stdout.channel.recv_exit_status()
    try:
        sftp.remove(REMOTE_PHP)
    except OSError:
        pass
    (EV / "WP-INTAKE-RAW.txt").write_text(out + "\n---stderr---\n" + err + f"\nexit={code}\n", encoding="utf-8")
    data = None
    for ln in out.splitlines():
        if ln.startswith("{"):
            data = json.loads(ln)
            break
    if data is None:
        data = {"parse_error": True, "head": out[:2000], "stderr": err[-2000:], "exit": code}
    (EV / "WP-INTAKE.json").write_text(json.dumps({"generated_at": now, "php_exit": code, "data": data}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("exit", code)
    if isinstance(data, dict):
        print("HOME", (data.get("options") or {}).get("home"), data.get("home_url"))
        print("SITEURL", (data.get("options") or {}).get("siteurl"))
        print("blog_public", data.get("blog_public"), "mail", data.get("mail_suppressed"))
        for p in data.get("legal_pages") or []:
            print("LEGAL", p.get("ID"), p.get("slug"), p.get("status"), p.get("acf"), "placeholders", p.get("placeholder_DEMO_BRACKET"))
    sftp.close()
    client.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

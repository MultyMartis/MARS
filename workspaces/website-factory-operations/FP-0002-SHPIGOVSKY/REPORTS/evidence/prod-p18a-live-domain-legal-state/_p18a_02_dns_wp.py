# -*- coding: utf-8 -*-
"""P18A follow-up: public DNS (NS/A/MX), PHP debug, WP options/legal via SSH."""
from __future__ import annotations

import io
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p18a-live-domain-legal-state")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
REMOTE_PHP = "/tmp/fp02_p18a_wp.php"
UA = "FP-0002-P18A-intake/1.0"

PHP = r"""<?php
error_reporting(E_ALL);
ini_set('display_errors','1');
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
global $wpdb;
$pages = $wpdb->get_results("SELECT p.ID, p.post_title, p.post_name, p.post_status, p.post_modified_gmt, p.post_content, pm.meta_value AS template FROM {$wpdb->posts} p LEFT JOIN {$wpdb->postmeta} pm ON pm.post_id=p.ID AND pm.meta_key='_wp_page_template' WHERE p.post_type='page' AND p.post_status NOT IN ('trash') AND pm.meta_value='page-templates/legal.php' ORDER BY p.ID", ARRAY_A);
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
        'placeholder_lorem'=>preg_match_all('/lorem ipsum/i',$content),
        'excerpt'=>mb_substr(wp_strip_all_tags($content),0,240),
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
echo json_encode(array(
    'home_url'=>home_url('/'),
    'site_url'=>site_url('/'),
    'options'=>$options,
    'blog_public'=>(int)get_option('blog_public'),
    'mail_suppressed'=>(bool)has_filter('pre_wp_mail'),
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


def nslookup(query: str, server: str | None = None) -> str:
    cmd = ["nslookup"]
    if " " in query:
        # type query: "set type=NS" not portable; use -type=
        parts = query.split()
        cmd = ["nslookup"] + parts
    else:
        cmd.append(query)
    if server:
        cmd.append(server)
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=20, text=True, encoding="utf-8", errors="replace")
    except subprocess.CalledProcessError as exc:
        return exc.output or str(exc)
    except Exception as exc:
        return str(exc)


def main() -> int:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    dns = {
        "generated_at": now,
        "queries": {},
    }
    for label, args in [
        ("ns_apex_system", ["nslookup", "-type=NS", "shpigovsky.ru"]),
        ("ns_apex_8888", ["nslookup", "-type=NS", "shpigovsky.ru", "8.8.8.8"]),
        ("ns_apex_1111", ["nslookup", "-type=NS", "shpigovsky.ru", "1.1.1.1"]),
        ("a_apex_8888", ["nslookup", "-type=A", "shpigovsky.ru", "8.8.8.8"]),
        ("a_apex_1111", ["nslookup", "-type=A", "shpigovsky.ru", "1.1.1.1"]),
        ("a_www_8888", ["nslookup", "-type=A", "www.shpigovsky.ru", "8.8.8.8"]),
        ("mx_apex_8888", ["nslookup", "-type=MX", "shpigovsky.ru", "8.8.8.8"]),
        ("a_beget_8888", ["nslookup", "-type=A", "shpigovsky.beget.tech", "8.8.8.8"]),
    ]:
        try:
            dns["queries"][label] = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=20, text=True, encoding="utf-8", errors="replace")
        except subprocess.CalledProcessError as exc:
            dns["queries"][label] = exc.output or str(exc)
        except Exception as exc:
            dns["queries"][label] = str(exc)
        print(label, "ok")
    (EV / "DNS-PUBLIC-RESOLVERS.json").write_text(json.dumps(dns, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # WordPress-on-Beget without following homepage 301 to old site
    beget_probes = []
    for path in ["/", "/privacy-policy/", "/uslugi/", "/specyalisty/", "/blog/", "/kontakty/", "/wp-json/", "/wp-sitemap.xml", "/robots.txt", "/wp-login.php"]:
        url = "http://shpigovsky.beget.tech" + path
        try:
            r = requests.get(url, timeout=25, allow_redirects=False, headers={"User-Agent": UA})
            rec = {
                "url": url,
                "status": r.status_code,
                "location": r.headers.get("Location"),
                "server": r.headers.get("Server"),
                "x_robots": r.headers.get("X-Robots-Tag"),
                "has_demo_notice": "Документ подготовлен для демонстрационной версии сайта" in r.text,
                "has_wp": ("wp-content" in r.text) or ("wordpress" in r.text.lower()) or ("/wp-json/" in r.text),
                "has_old_title": "Лечение алкоголизма" in r.text or "alkogol" in r.text.lower(),
                "canonical": None,
                "body_bytes": len(r.content),
            }
            m = re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', r.text, re.I)
            if m:
                rec["canonical"] = m.group(1)
            rec["generator"] = None
            gm = re.search(r'name=["\']generator["\'][^>]*content=["\']([^"\']+)', r.text, re.I)
            if gm:
                rec["generator"] = gm.group(1)
            beget_probes.append(rec)
            print("BEGET", path, rec["status"], rec.get("location"), "demo", rec["has_demo_notice"], "wp", rec["has_wp"])
        except Exception as exc:
            beget_probes.append({"url": url, "error": str(exc)})
            print("BEGET", path, exc)
    (EV / "BEGET-HOST-NOFOLLOW.json").write_text(json.dumps({"generated_at": now, "probes": beget_probes}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    old_site = []
    for path in ["/", "/privacy-policy/", "/uslugi/", "/wp-json/", "/robots.txt"]:
        url = "https://shpigovsky.ru" + path
        try:
            r = requests.get(url, timeout=25, allow_redirects=False, verify=True, headers={"User-Agent": UA})
            rec = {
                "url": url,
                "status": r.status_code,
                "location": r.headers.get("Location"),
                "server": r.headers.get("Server"),
                "has_wp": "wp-content" in r.text,
                "has_old_title": "Лечение алкоголизма" in r.text,
                "body_bytes": len(r.content),
                "snippet": r.text[:400],
            }
            old_site.append(rec)
            print("APEX", path, rec["status"], "wp", rec["has_wp"], "old", rec["has_old_title"])
        except Exception as exc:
            old_site.append({"url": url, "error": str(exc)})
    (EV / "APEX-OLD-HOST-PROBES.json").write_text(json.dumps({"generated_at": now, "probes": old_site}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

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

    def run(cmd, timeout=90):
        stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
        out = stdout.read().decode("utf-8", errors="replace")
        err = stderr.read().decode("utf-8", errors="replace")
        code = stdout.channel.recv_exit_status()
        return out, err, code

    php_v_out, php_v_err, php_v_code = run("which php; php -v; ls -l /tmp/fp02_p18a_intake.php 2>/dev/null || true")
    (EV / "PHP-CLI.txt").write_text(php_v_out + "\n---stderr---\n" + php_v_err + f"\nexit={php_v_code}\n", encoding="utf-8")
    print("php -v exit", php_v_code)

    sftp.putfo(io.BytesIO(PHP.encode("utf-8")), REMOTE_PHP)
    out, err, code = run(f"php {REMOTE_PHP}")
    try:
        sftp.remove(REMOTE_PHP)
    except OSError:
        pass
    (EV / "WP-INTAKE-RAW.txt").write_text(out + "\n---stderr---\n" + err + f"\nexit={code}\n", encoding="utf-8")
    print("wp php exit", code, "out_len", len(out), "err_len", len(err))
    data = None
    try:
        # last JSON line
        lines = [ln for ln in out.splitlines() if ln.strip().startswith("{")]
        data = json.loads(lines[-1]) if lines else {"parse_error": True, "head": out[:2000]}
    except json.JSONDecodeError as exc:
        data = {"parse_error": True, "error": str(exc), "head": out[:2000], "stderr": err[-2000:]}
    (EV / "WP-INTAKE.json").write_text(json.dumps({"generated_at": now, "php_exit": code, "data": data}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if isinstance(data, dict) and data.get("options"):
        print("HOME", data["options"].get("home"))
        print("SITEURL", data["options"].get("siteurl"))
        print("blog_public", data.get("blog_public"))
        print("legal", [(p.get("ID"), p.get("slug"), p.get("acf")) for p in data.get("legal_pages") or []])

    sftp.close()
    client.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

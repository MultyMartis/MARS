# -*- coding: utf-8 -*-
"""PROD-P18A phase 1: live-domain reality + legal state intake. Read-only on production."""
from __future__ import annotations

import hashlib
import io
import json
import re
import socket
import ssl
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
ROOT = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
THEME_SRC = ROOT / "WORDPRESS" / "theme" / "shpigovsky"
PLUGIN_SRC = ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core"
EV = ROOT / "REPORTS" / "evidence" / "prod-p18a-live-domain-legal-state"
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p18a-layer-b-pre")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
THEME_REMOTE = f"{DOCROOT}/wp-content/themes/shpigovsky"
PLUGIN_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
MU_REMOTE = f"{DOCROOT}/wp-content/mu-plugins"
REMOTE_PHP = "/tmp/fp02_p18a_intake.php"
UA = "FP-0002-P18A-intake/1.0"

HOSTS = [
    "shpigovsky.ru",
    "www.shpigovsky.ru",
    "shpigovsky.beget.tech",
    "www.shpigovsky.beget.tech",
]
URLS = [
    "http://shpigovsky.ru/",
    "https://shpigovsky.ru/",
    "http://www.shpigovsky.ru/",
    "https://www.shpigovsky.ru/",
    "http://shpigovsky.beget.tech/",
    "https://shpigovsky.beget.tech/",
]
LEGAL_PATHS = [
    "/privacy-policy/",
    "/user-agreement/",
    "/consent-personal-data/",
    "/cookie-files-policy/",
]
SMOKE_PATHS = [
    "/",
    "/uslugi/",
    "/specyalisty/",
    "/blog/",
    "/kontakty/",
    "/privacy-policy/",
    "/wp-json/",
    "/wp-sitemap.xml",
    "/robots.txt",
    "/wp-admin/",
    "/wp-login.php",
]
FOCUS_FILES = [
    ("theme", "template-parts/legal/document-page.php"),
    ("theme", "page-templates/legal.php"),
    ("theme", "functions.php"),
    ("plugin", "shpigovsky-core.php"),
    ("plugin", "src/Admin/SystemDashboard.php"),
    ("plugin", "src/Fields/FieldGroups.php"),
    ("plugin", "src/Admin/EditorRestrictions.php"),
]

INTAKE_PHP = r"""<?php
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

function fp02_meta_bundle($post_id) {
    $keys = array(
        'legal_status','legal_demo_marker','legal_production_blocker',
        'legal_effective_date','legal_version',
        '_legal_status','_legal_demo_marker','_legal_production_blocker',
        'demo_marker','legal_demo','fp02_legal_demo_marker',
    );
    $out = array();
    foreach ($keys as $k) {
        $exists = metadata_exists('post', $post_id, $k);
        $raw = get_post_meta($post_id, $k, false);
        $out[$k] = array(
            'exists' => $exists,
            'raw' => $raw,
            'get_post_meta_single' => get_post_meta($post_id, $k, true),
        );
    }
    $acf = array();
    if (function_exists('get_field')) {
        foreach (array('legal_status','legal_demo_marker','legal_production_blocker','legal_effective_date','legal_version') as $f) {
            $acf[$f] = array(
                'get_field' => get_field($f, $post_id),
                'get_field_unformatted' => get_field($f, $post_id, false),
            );
        }
    }
    return array('named' => $out, 'acf' => $acf);
}

$opt_keys = array(
    'siteurl','home','blogname','blogdescription','permalink_structure',
    'blog_public','show_on_front','page_on_front','page_for_posts',
    'wp_page_for_privacy_policy','WPLANG','users_can_register',
);
$options = array();
foreach ($opt_keys as $k) {
    $options[$k] = get_option($k);
}

$wpilot_opts = get_option('metacode_wpilot', get_option('wpilot', array()));
$wpilot_write = false;
if (is_array($wpilot_opts) && array_key_exists('write_enabled', $wpilot_opts)) {
    $wpilot_write = (bool) $wpilot_opts['write_enabled'];
}

$legal_q = new WP_Query(array(
    'post_type' => 'page',
    'post_status' => 'any',
    'posts_per_page' => 50,
    'meta_key' => '_wp_page_template',
    'meta_value' => 'page-templates/legal.php',
    'orderby' => 'ID',
    'order' => 'ASC',
    'no_found_rows' => true,
));
$legal_pages = array();
foreach ($legal_q->posts as $p) {
    $revs = array();
    foreach (wp_get_post_revisions($p->ID, array('numberposts' => 8)) as $r) {
        $revs[] = array(
            'ID' => (int) $r->ID,
            'date' => $r->post_date_gmt,
            'status' => $r->post_status,
            'modified' => $r->post_modified_gmt,
            'parent' => (int) $r->post_parent,
        );
    }
    $autosave = wp_get_post_autosave($p->ID);
    $content = (string) $p->post_content;
    $legal_pages[] = array(
        'ID' => (int) $p->ID,
        'title' => $p->post_title,
        'slug' => $p->post_name,
        'status' => $p->post_status,
        'modified_gmt' => $p->post_modified_gmt,
        'permalink' => get_permalink($p->ID),
        'template' => get_page_template_slug($p->ID),
        'content_bytes' => strlen($content),
        'placeholder_hits' => array(
            'DEMO_BRACKET' => substr_count($content, '[ДЕМО'),
            'DEMO_COLON' => substr_count($content, 'ДЕМО:'),
            'lorem' => preg_match_all('/lorem ipsum/i', $content),
            'TEST' => substr_count($content, '[TEST'),
        ),
        'content_excerpt' => fp02_clip($content, 280),
        'revisions' => $revs,
        'autosave' => $autosave ? array(
            'ID' => (int) $autosave->ID,
            'date' => $autosave->post_date_gmt,
            'modified' => $autosave->post_modified_gmt,
        ) : null,
        'meta' => fp02_meta_bundle($p->ID),
    );
}

$like_demo = '%' . $wpdb->esc_like('[ДЕМО') . '%';
$demo_posts = $wpdb->get_results($wpdb->prepare(
    "SELECT ID, post_title, post_name, post_status, post_type FROM {$wpdb->posts} WHERE post_content LIKE %s AND post_type IN ('page','post') AND post_status NOT IN ('trash','auto-draft') ORDER BY ID",
    $like_demo
), ARRAY_A);

$like_lorem = '%Lorem ipsum%';
$lorem_posts = $wpdb->get_results($wpdb->prepare(
    "SELECT ID, post_title, post_name, post_status, post_type FROM {$wpdb->posts} WHERE post_content LIKE %s AND post_type IN ('page','post') AND post_status NOT IN ('trash','auto-draft') ORDER BY ID",
    $like_lorem
), ARRAY_A);

$acf_group = null;
if (function_exists('acf_get_field_group')) {
    $acf_group = acf_get_field_group('group_fp02_page_legal');
    if (is_array($acf_group) && isset($acf_group['fields'])) {
        $slim = array();
        foreach ((array) $acf_group['fields'] as $f) {
            $slim[] = array(
                'key' => $f['key'] ?? null,
                'name' => $f['name'] ?? null,
                'label' => $f['label'] ?? null,
                'type' => $f['type'] ?? null,
                'default_value' => $f['default_value'] ?? null,
            );
        }
        $acf_group = array(
            'key' => $acf_group['key'] ?? null,
            'title' => $acf_group['title'] ?? null,
            'fields' => $slim,
        );
    }
}

$robots_path = ABSPATH . 'robots.txt';
$robots = is_file($robots_path) ? file_get_contents($robots_path) : null;

echo json_encode(array(
    'generated_at' => gmdate('c'),
    'constants' => array(
        'WP_ENVIRONMENT_TYPE' => defined('WP_ENVIRONMENT_TYPE') ? WP_ENVIRONMENT_TYPE : null,
        'WP_DEBUG' => defined('WP_DEBUG') ? WP_DEBUG : null,
        'WP_HOME' => defined('WP_HOME') ? WP_HOME : null,
        'WP_SITEURL' => defined('WP_SITEURL') ? WP_SITEURL : null,
        'SHPIGOVSKY_CORE_VERSION' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
        'home_url' => home_url('/'),
        'site_url' => site_url('/'),
        'content_url' => content_url(),
        'rest_url' => rest_url(),
    ),
    'options' => $options,
    'blog_public' => (int) get_option('blog_public', 1),
    'mail_suppressed' => (bool) has_filter('pre_wp_mail'),
    'wpilot_write' => $wpilot_write,
    'metacode_meta' => get_option('fp02_metacode_system_meta', array()),
    'legal_pages' => $legal_pages,
    'privacy_page_id' => (int) get_option('wp_page_for_privacy_policy'),
    'placeholder_posts_demo_bracket' => $demo_posts,
    'placeholder_posts_lorem' => $lorem_posts,
    'acf_legal_group' => $acf_group,
    'robots_txt' => $robots,
    'sitemap_home' => home_url('/wp-sitemap.xml'),
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


def getf(pairs: dict, *keys):
    for k in keys:
        v = pairs.get(k)
        if v and "<OPERATOR" not in v and v.strip():
            return v.strip()
    return None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sftp_get(sftp, remote: str) -> bytes | None:
    try:
        bio = io.BytesIO()
        sftp.getfo(remote, bio)
        return bio.getvalue()
    except (FileNotFoundError, OSError):
        return None


def snapshot_file(sftp, remote: str, dest: Path) -> dict:
    data = sftp_get(sftp, remote)
    rec = {"remote": remote, "exists": data is not None, "bytes": None, "sha256": None}
    if data is None:
        return rec
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    rec["bytes"] = len(data)
    rec["sha256"] = sha256_bytes(data)
    rec["local_snap"] = str(dest)
    return rec


def dns_lookup(host: str) -> dict:
    rec = {"host": host, "A": [], "AAAA": [], "CNAME": [], "NS": [], "MX": [], "error": None}
    try:
        raw = subprocess.check_output(
            ["nslookup", host],
            stderr=subprocess.STDOUT,
            timeout=20,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        rec["nslookup_raw"] = raw[-4000:]
        rec["A"] = re.findall(r"Address:\s+(\d+\.\d+\.\d+\.\d+)", raw)
        # first Address is often the DNS server; keep all then unique
        rec["A"] = list(dict.fromkeys(rec["A"]))
    except Exception as exc:
        rec["error"] = str(exc)
    try:
        rec["getaddrinfo"] = list(
            dict.fromkeys(ai[4][0] for ai in socket.getaddrinfo(host, None))
        )
    except Exception as exc:
        rec["getaddrinfo_error"] = str(exc)
    return rec


def ssl_probe(host: str, port: int = 443) -> dict:
    rec = {"host": host, "port": port, "ok": False, "error": None}
    ctx = ssl.create_default_context()
    try:
        with socket.create_connection((host, port), timeout=15) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                rec["ok"] = True
                rec["protocol"] = ssock.version()
                rec["cipher"] = ssock.cipher()
                rec["subject"] = cert.get("subject")
                rec["issuer"] = cert.get("issuer")
                rec["notBefore"] = cert.get("notBefore")
                rec["notAfter"] = cert.get("notAfter")
                rec["subjectAltName"] = cert.get("subjectAltName")
    except ssl.SSLCertVerificationError as exc:
        rec["error"] = f"SSLCertVerificationError: {exc}"
        rec["verify_code"] = getattr(exc, "verify_code", None)
        rec["verify_message"] = getattr(exc, "verify_message", None)
        # retry without verify to read presented cert
        try:
            insecure = ssl._create_unverified_context()
            with socket.create_connection((host, port), timeout=15) as sock:
                with insecure.wrap_socket(sock, server_hostname=host) as ssock:
                    cert = ssock.getpeercert()
                    rec["unverified_ok"] = True
                    rec["unverified_subject"] = cert.get("subject")
                    rec["unverified_issuer"] = cert.get("issuer")
                    rec["unverified_notBefore"] = cert.get("notBefore")
                    rec["unverified_notAfter"] = cert.get("notAfter")
                    rec["unverified_san"] = cert.get("subjectAltName")
        except Exception as exc2:
            rec["unverified_error"] = str(exc2)
    except Exception as exc:
        rec["error"] = f"{type(exc).__name__}: {exc}"
    return rec


def http_probe(url: str, allow_redirects: bool = False, verify: bool = True) -> dict:
    rec = {
        "url": url,
        "allow_redirects": allow_redirects,
        "verify": verify,
        "error": None,
    }
    try:
        r = requests.get(
            url,
            timeout=25,
            allow_redirects=allow_redirects,
            verify=verify,
            headers={"User-Agent": UA},
        )
        rec["status"] = r.status_code
        rec["final_url"] = str(r.url)
        rec["headers"] = {
            k: r.headers.get(k)
            for k in (
                "Location",
                "Server",
                "Content-Type",
                "X-Robots-Tag",
                "Strict-Transport-Security",
                "Link",
            )
            if r.headers.get(k)
        }
        rec["history"] = [
            {"status": h.status_code, "url": str(h.url), "location": h.headers.get("Location")}
            for h in r.history
        ]
        rec["body_bytes"] = len(r.content)
        rec["body_snippet"] = r.text[:800]
        rec["has_demo_notice"] = "Документ подготовлен для демонстрационной версии сайта" in r.text
        rec["has_demo_placeholder"] = "[ДЕМО" in r.text
        rec["canonical_host"] = None
        m = re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', r.text, re.I)
        if not m:
            m = re.search(r'href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']', r.text, re.I)
        if m:
            rec["canonical"] = m.group(1)
            rec["canonical_host"] = urlparse(m.group(1)).hostname
        rec["beget_abs_count"] = r.text.count("shpigovsky.beget.tech")
        rec["live_abs_count"] = r.text.count("shpigovsky.ru")
        rec["rest_link"] = r.headers.get("Link")
    except requests.exceptions.SSLError as exc:
        rec["error"] = f"SSLError: {exc}"
    except Exception as exc:
        rec["error"] = f"{type(exc).__name__}: {exc}"
    return rec


def classify_ssl(ssl_rec: dict) -> str:
    if ssl_rec.get("ok"):
        return "A. VALID AND ACTIVE"
    err = (ssl_rec.get("error") or "") + " " + (ssl_rec.get("verify_message") or "")
    if "CERTIFICATE_VERIFY_FAILED" in err or "certificate verify failed" in err.lower():
        if ssl_rec.get("unverified_ok"):
            return "C. ISSUANCE IN PROGRESS"
        return "D. FAILED / BLOCKED"
    if "timed out" in err.lower() or "Name or service not known" in err:
        return "C. ISSUANCE IN PROGRESS"
    if ssl_rec.get("error"):
        return "C. ISSUANCE IN PROGRESS"
    return "C. ISSUANCE IN PROGRESS"


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    LAYER_B.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    dns = [dns_lookup(h) for h in HOSTS]
    (EV / "DNS-LOOKUPS.json").write_text(
        json.dumps({"generated_at": now, "lookups": dns}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print("DNS done")

    ssl_recs = {}
    for h in ("shpigovsky.ru", "www.shpigovsky.ru", "shpigovsky.beget.tech"):
        ssl_recs[h] = ssl_probe(h)
        ssl_recs[h]["classification"] = classify_ssl(ssl_recs[h])
        print("SSL", h, ssl_recs[h]["classification"], ssl_recs[h].get("error"))
    (EV / "SSL-STATE.json").write_text(
        json.dumps({"generated_at": now, "certs": ssl_recs}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    http = []
    for url in URLS:
        rec = http_probe(url, allow_redirects=False, verify=True)
        if rec.get("error") and "SSL" in (rec.get("error") or ""):
            rec_insecure = http_probe(url, allow_redirects=False, verify=False)
            rec["insecure_fallback"] = rec_insecure
        rec_follow = http_probe(url, allow_redirects=True, verify=False)
        rec["follow"] = rec_follow
        http.append(rec)
        print("HTTP", url, rec.get("status"), rec.get("error"))
    (EV / "HTTP-PROBES.json").write_text(
        json.dumps({"generated_at": now, "probes": http}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    legal_http = []
    for path in LEGAL_PATHS:
        for base in ("http://shpigovsky.ru", "http://shpigovsky.beget.tech"):
            rec = http_probe(base + path, allow_redirects=True, verify=False)
            legal_http.append(rec)
            print("LEGAL", rec["url"], rec.get("status"), "demo_notice", rec.get("has_demo_notice"))
    (EV / "LEGAL-HTTP-BEFORE.json").write_text(
        json.dumps({"generated_at": now, "probes": legal_http}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    smoke = []
    for path in SMOKE_PATHS:
        rec = http_probe("http://shpigovsky.ru" + path, allow_redirects=True, verify=False)
        smoke.append(rec)
        print("SMOKE", path, rec.get("status"), rec.get("error"))
    (EV / "FRONTEND-SMOKE-BEFORE.json").write_text(
        json.dumps({"generated_at": now, "probes": smoke}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

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

    snaps = []
    for remote, name in [
        (f"{THEME_REMOTE}/template-parts/legal/document-page.php", "theme__document-page.php"),
        (f"{THEME_REMOTE}/page-templates/legal.php", "theme__legal.php"),
        (f"{THEME_REMOTE}/functions.php", "theme__functions.php"),
        (f"{PLUGIN_REMOTE}/shpigovsky-core.php", "plugin__shpigovsky-core.php"),
        (f"{PLUGIN_REMOTE}/src/Admin/SystemDashboard.php", "plugin__SystemDashboard.php"),
        (f"{PLUGIN_REMOTE}/src/Fields/FieldGroups.php", "plugin__FieldGroups.php"),
        (f"{MU_REMOTE}/fp02-pre-cutover-mail-suppression.php", "mu__fp02-pre-cutover-mail-suppression.php"),
        (f"{DOCROOT}/robots.txt", "robots.txt"),
        (f"{DOCROOT}/.htaccess", "htaccess"),
    ]:
        rec = snapshot_file(sftp, remote, LAYER_B / name)
        snaps.append(rec)
        print("SNAP", name, rec["exists"], rec["sha256"])
    (EV / "LAYER-B-SNAPSHOTS.json").write_text(
        json.dumps(
            {
                "generated_at": now,
                "note": "File bytes live in STORAGE Layer B; hashes only here. No wp-config in git evidence.",
                "snaps": snaps,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    focus = []
    for kind, rel in FOCUS_FILES:
        local = (THEME_SRC if kind == "theme" else PLUGIN_SRC) / Path(*rel.split("/"))
        remote = f"{THEME_REMOTE if kind == 'theme' else PLUGIN_REMOTE}/{rel}"
        rb = sftp_get(sftp, remote)
        lb = local.read_bytes() if local.is_file() else None
        rec = {
            "kind": kind,
            "rel": rel,
            "prod_sha256": sha256_bytes(rb) if rb else None,
            "local_sha256": sha256_bytes(lb) if lb else None,
            "match": rb is not None and lb is not None and rb == lb,
            "prod_bytes": len(rb) if rb else None,
            "local_bytes": len(lb) if lb else None,
        }
        focus.append(rec)
        print("FOCUS", "MATCH" if rec["match"] else "DRIFT", kind, rel)
    (EV / "SOURCE-PROD-FOCUS-BEFORE.json").write_text(
        json.dumps({"generated_at": now, "files": focus}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    sftp.putfo(io.BytesIO(INTAKE_PHP.encode("utf-8")), REMOTE_PHP)
    stdin, stdout, stderr = client.exec_command(f"php {REMOTE_PHP}", timeout=90)
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    code = stdout.channel.recv_exit_status()
    try:
        sftp.remove(REMOTE_PHP)
    except OSError:
        pass
    (EV / "WP-INTAKE-RAW.txt").write_text(out + ("\n---stderr---\n" + err if err else ""), encoding="utf-8")
    wp = None
    try:
        wp = json.loads(out.strip().split("\n")[-1] if out.strip() else "{}")
    except json.JSONDecodeError:
        wp = {"parse_error": True, "exit": code, "stderr": err[-2000:], "stdout_head": out[:2000]}
    # strip any accidental secrets
    if isinstance(wp, dict):
        wp.pop("db_password", None)
        wp.pop("ssh_password", None)
    (EV / "WP-INTAKE.json").write_text(
        json.dumps({"generated_at": now, "php_exit": code, "data": wp}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print("WP intake exit", code)
    if isinstance(wp, dict) and "data" not in wp:
        home = (wp.get("options") or {}).get("home")
        siteurl = (wp.get("options") or {}).get("siteurl")
        print("home", home, "siteurl", siteurl, "blog_public", wp.get("blog_public"))
        print("legal pages", len(wp.get("legal_pages") or []))
    elif isinstance(wp, dict):
        data = wp.get("data") or wp
        print("home", (data.get("options") or {}).get("home"))

    sftp.close()
    client.close()

    summary = {
        "generated_at": now,
        "ssl_classifications": {h: ssl_recs[h]["classification"] for h in ssl_recs},
        "http_statuses": {p["url"]: p.get("status") or p.get("error") for p in http},
        "operator_live_domain_intake": True,
        "note": "Do not revert home/siteurl. SSL pending is not a WordPress regression.",
    }
    (EV / "INTAKE-SUMMARY.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("INTAKE COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

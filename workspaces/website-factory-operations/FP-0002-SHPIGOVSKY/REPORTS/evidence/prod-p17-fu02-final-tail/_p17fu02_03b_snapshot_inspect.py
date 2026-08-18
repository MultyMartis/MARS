# -*- coding: utf-8 -*-
"""Download obsolete tar + inspect mars-runtime PHP locally. Do not re-hit mutating PHP URLs."""
from __future__ import annotations

import hashlib
import io
import json
import re
import tarfile
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p17-fu02-final-tail")
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p17-fu02-layer-b-pre")
OBSOLETE = LAYER_B / "obsolete-webroot-snapshot"
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
REMOTE_TAR = "/tmp/fp02_p17fu02_obsolete_20260818-101831.tar.gz"
REMOTE_PHP = "/tmp/fp02_p17fu02_probe.php"
BASE = "http://shpigovsky.beget.tech"

PROBE_PHP = r"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
global $wpdb;
$out = array();
$pats = array('new-site.space','@localhost.test','localhost','shpigovsky.test');
foreach ($pats as $pat) {
    $like = '%' . $wpdb->esc_like($pat) . '%';
    $opts = $wpdb->get_results($wpdb->prepare(
        "SELECT option_id, option_name, LENGTH(option_value) bytes, LEFT(option_value, 220) preview
         FROM {$wpdb->options}
         WHERE option_value LIKE %s AND option_name NOT LIKE '\\_transient%' AND option_name NOT LIKE '\\_site\\_transient%'
         LIMIT 30", $like), ARRAY_A);
    $posts = $wpdb->get_results($wpdb->prepare(
        "SELECT ID, post_type, post_status, post_name, post_title,
                (post_content LIKE %s) in_content, (post_excerpt LIKE %s) in_excerpt
         FROM {$wpdb->posts} WHERE post_content LIKE %s OR post_excerpt LIKE %s LIMIT 40",
        $like,$like,$like,$like), ARRAY_A);
    $guid_only = (int) $wpdb->get_var($wpdb->prepare(
        "SELECT COUNT(*) FROM {$wpdb->posts} WHERE guid LIKE %s AND post_content NOT LIKE %s AND post_excerpt NOT LIKE %s",
        $like,$like,$like));
    $meta = $wpdb->get_results($wpdb->prepare(
        "SELECT meta_id, post_id, meta_key, LEFT(meta_value, 220) preview FROM {$wpdb->postmeta} WHERE meta_value LIKE %s LIMIT 40",
        $like), ARRAY_A);
    $out[$pat] = array('options'=>$opts,'content_posts'=>$posts,'guid_only_count'=>$guid_only,'postmeta'=>$meta);
}
$like = '%' . $wpdb->esc_like('shpigovsky.beget.tech') . '%';
$out['beget_options_full'] = $wpdb->get_results($wpdb->prepare(
    "SELECT option_id, option_name, option_value FROM {$wpdb->options}
     WHERE option_value LIKE %s AND option_name NOT LIKE '\\_transient%' AND option_name NOT LIKE '\\_site\\_transient%'", $like), ARRAY_A);
$out['beget_postmeta_full'] = $wpdb->get_results($wpdb->prepare(
    "SELECT meta_id, post_id, meta_key, meta_value FROM {$wpdb->postmeta} WHERE meta_value LIKE %s ORDER BY meta_key, post_id", $like), ARRAY_A);
$out['menu_urls'] = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title, p.post_name, pm.meta_value FROM {$wpdb->posts} p
     JOIN {$wpdb->postmeta} pm ON pm.post_id=p.ID AND pm.meta_key='_menu_item_url'
     WHERE p.post_type='nav_menu_item' AND pm.meta_value LIKE %s", $like), ARRAY_A);
echo json_encode($out, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
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


def run(client, cmd, timeout=180):
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    return stdout.read().decode("utf-8", errors="replace"), stderr.read().decode("utf-8", errors="replace"), stdout.channel.recv_exit_status()


def main() -> int:
    OBSOLETE.mkdir(parents=True, exist_ok=True)
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

    local_tar = OBSOLETE / "obsolete-webroot-20260818-101831.tar.gz"
    print("GET TAR")
    sftp.get(REMOTE_TAR, str(local_tar))
    sha = hashlib.sha256(local_tar.read_bytes()).hexdigest()
    print("TAR", local_tar.stat().st_size, sha)

    extract_dir = OBSOLETE / "extracted"
    extract_dir.mkdir(parents=True, exist_ok=True)
    with tarfile.open(local_tar, "r:gz") as tf:
        names = tf.getnames()
        tf.extractall(extract_dir)
    print("EXTRACTED", len(names))

    php_notes = []
    for p in extract_dir.rglob("*.php"):
        text = p.read_text(encoding="utf-8", errors="replace")
        php_notes.append({
            "rel": str(p.relative_to(extract_dir)).replace("\\", "/"),
            "bytes": p.stat().st_size,
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "mentions_wp_insert": "wp_insert" in text,
            "mentions_wp_update": "wp_update" in text or "wp_update_post" in text,
            "mentions_delete": "wp_delete" in text,
            "requires_wp_load": "wp-load.php" in text,
            "preview_head": "\n".join(text.splitlines()[:40]),
        })

    with sftp.file(REMOTE_PHP, "wb") as fh:
        fh.write(PROBE_PHP.encode("utf-8"))
    out, err, code = run(client, f"php8.2 {REMOTE_PHP} 2>/dev/null || php {REMOTE_PHP}")
    try:
        sftp.remove(REMOTE_PHP)
    except OSError:
        pass
    inv = None
    for ln in out.splitlines():
        if ln.startswith("{"):
            inv = json.loads(ln)
            break

    sftp.close()
    client.close()

    sess = requests.Session()
    sess.headers.update({"User-Agent": "FP0002-P17-FU02-probe/1.0"})
    http_rows = []
    # Do NOT re-request mutating populate PHP.
    for path in [
        "/mars-runtime/scripts/validate-wpilot-readonly.ps1",
        "/mars-runtime/scripts/create-foundation-002a-checkpoint.ps1",
        "/mars-runtime/scripts/reset-to-foundation.ps1",
        "/acf-json/",
        "/wp-content/debug.log",
    ]:
        r = sess.head(BASE + path, allow_redirects=False, timeout=20)
        http_rows.append({"path": path, "method": "HEAD", "status": r.status_code, "ctype": r.headers.get("Content-Type"), "len": r.headers.get("Content-Length")})
        print("HEAD", path, r.status_code)

    blog = sess.get(BASE + "/blog/nazvanie-stati/", timeout=30)
    contexts = []
    for m in re.finditer(r".{0,100}new-site\.space.{0,100}", blog.text or "", re.I | re.S):
        contexts.append(re.sub(r"\s+", " ", m.group(0)))

    payload = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "tar": {"path": str(local_tar), "bytes": local_tar.stat().st_size, "sha256": sha, "names": names},
        "php_notes": php_notes,
        "db_probe": inv,
        "http_head": http_rows,
        "prior_get_observed": {
            "populate-fp-0002-pages.php": {"status": 200, "body": "FP-0002 pages and menus OK"},
            "fp0002-access-encoding-wpilot-task.php": {"status": 200, "body": "JSON wp_options dump (blogname etc)"},
            "backup-runtime.ps1": {"status": 200},
            "app css": {"status": 200},
            "debug.log": {"status": 200, "empty": True},
            "broken mpegts bak": {"status": 200, "downloadable": True},
        },
        "new_site_space_html_contexts": contexts,
        "token": "MARS-RUNTIME STATUS RESOLVED",
    }
    (EV / "MARS-RUNTIME-AND-LEFTOVER-PROBE.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("WROTE probe json")
    return 0 if inv else 2


if __name__ == "__main__":
    raise SystemExit(main())

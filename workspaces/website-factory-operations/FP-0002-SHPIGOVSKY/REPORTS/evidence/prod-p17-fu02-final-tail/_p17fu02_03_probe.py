# -*- coding: utf-8 -*-
"""P17-FU02 follow-up probes: HTTP exposure, leftover options, new-site.space, postmeta URL inventory."""
from __future__ import annotations

import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p17-fu02-final-tail")
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p17-fu02-layer-b-pre")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
BASE = "http://shpigovsky.beget.tech"
REMOTE_PHP = "/tmp/fp02_p17fu02_probe.php"

PROBE_PHP = r"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
global $wpdb;
function clip($v,$m=300){ $s=(string)$v; return strlen($s)>$m ? substr($s,0,$m).'...[truncated]' : $s; }

$out = array();
$pats = array('new-site.space','@localhost.test','localhost','shpigovsky.test');
foreach ($pats as $pat) {
    $like = '%' . $wpdb->esc_like($pat) . '%';
    $opts = $wpdb->get_results($wpdb->prepare(
        "SELECT option_id, option_name, LENGTH(option_value) bytes, LEFT(option_value, 220) preview
         FROM {$wpdb->options}
         WHERE option_value LIKE %s
           AND option_name NOT LIKE '\\_transient%'
           AND option_name NOT LIKE '\\_site\\_transient%'
         LIMIT 30",
        $like
    ), ARRAY_A);
    $posts = $wpdb->get_results($wpdb->prepare(
        "SELECT ID, post_type, post_status, post_name, post_title,
                (guid LIKE %s) in_guid, (post_content LIKE %s) in_content, (post_excerpt LIKE %s) in_excerpt
         FROM {$wpdb->posts}
         WHERE post_content LIKE %s OR post_excerpt LIKE %s
         LIMIT 40",
        $like,$like,$like,$like,$like
    ), ARRAY_A);
    $guid_only = (int) $wpdb->get_var($wpdb->prepare(
        "SELECT COUNT(*) FROM {$wpdb->posts} WHERE guid LIKE %s AND post_content NOT LIKE %s AND post_excerpt NOT LIKE %s",
        $like,$like,$like
    ));
    $meta = $wpdb->get_results($wpdb->prepare(
        "SELECT meta_id, post_id, meta_key, LEFT(meta_value, 220) preview
         FROM {$wpdb->postmeta} WHERE meta_value LIKE %s LIMIT 40",
        $like
    ), ARRAY_A);
    $out[$pat] = array('options'=>$opts,'content_posts'=>$posts,'guid_only_count'=>$guid_only,'postmeta'=>$meta);
}

$like = '%' . $wpdb->esc_like('shpigovsky.beget.tech') . '%';
$beget_opts = $wpdb->get_results($wpdb->prepare(
    "SELECT option_id, option_name, option_value
     FROM {$wpdb->options}
     WHERE option_value LIKE %s
       AND option_name NOT LIKE '\\_transient%'
       AND option_name NOT LIKE '\\_site\\_transient%'",
    $like
), ARRAY_A);
$beget_meta = $wpdb->get_results($wpdb->prepare(
    "SELECT meta_id, post_id, meta_key, meta_value
     FROM {$wpdb->postmeta} WHERE meta_value LIKE %s
     ORDER BY meta_key, post_id",
    $like
), ARRAY_A);
$out['beget_options_full'] = $beget_opts;
$out['beget_postmeta_full'] = $beget_meta;

$menu = $wpdb->get_results($wpdb->prepare(
    "SELECT p.ID, p.post_title, p.post_name, pm.meta_value
     FROM {$wpdb->posts} p
     JOIN {$wpdb->postmeta} pm ON pm.post_id=p.ID AND pm.meta_key='_menu_item_url'
     WHERE p.post_type='nav_menu_item' AND pm.meta_value LIKE %s",
    $like
), ARRAY_A);
$out['menu_urls'] = $menu;

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


def run(client, cmd, timeout=90):
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    return stdout.read().decode("utf-8", errors="replace"), stderr.read().decode("utf-8", errors="replace"), stdout.channel.recv_exit_status()


def sftp_get(sftp, remote):
    try:
        bio = io.BytesIO()
        sftp.getfo(remote, bio)
        return bio.getvalue()
    except (FileNotFoundError, OSError):
        return None


def main() -> int:
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

    # Snapshot mars-runtime + app (full tree tar on remote then download)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    remote_tar = f"/tmp/fp02_p17fu02_obsolete_{stamp}.tar.gz"
    tar_cmd = (
        f"cd {DOCROOT} && tar -czf {remote_tar} mars-runtime app "
        f"wp-content/debug.log "
        f"wp-content/themes/shpigovsky/assets/video/sergey-shpigovsky-interview.mp4.BROKEN-MPEGTS.bak "
        f"wp-content/uploads/2026/07/sergey-shpigovsky-interview.mp4.BROKEN-MPEGTS.bak "
        f"2>/tmp/fp02_p17fu02_tar.err; echo EXIT:$?; wc -c {remote_tar}; cat /tmp/fp02_p17fu02_tar.err"
    )
    tout, terr, tcode = run(client, tar_cmd, timeout=180)
    print("TAR", tout[-800:])

    # Inspect mars-runtime PHP for secret-like tokens (names only)
    secretish = []
    for rel in [
        "mars-runtime/scripts/fp0002-access-encoding-wpilot-task.php",
        "mars-runtime/scripts/populate-fp-0002-pages.php",
    ]:
        data = sftp_get(sftp, f"{DOCROOT}/{rel}")
        if not data:
            continue
        text = data.decode("utf-8", errors="replace")
        keys = re.findall(r"(password|passwd|secret|token|api_key|DB_|mysql)", text, re.I)
        secretish.append({"rel": rel, "bytes": len(data), "cue_hits": sorted(set(keys))[:20], "has_define_db": "DB_PASSWORD" in text})

    sftp.close()
    client.close()

    sess = requests.Session()
    sess.headers.update({"User-Agent": "FP0002-P17-FU02-probe/1.0"})
    http_paths = [
        "/mars-runtime/",
        "/mars-runtime/scripts/",
        "/mars-runtime/scripts/populate-fp-0002-pages.php",
        "/mars-runtime/scripts/fp0002-access-encoding-wpilot-task.php",
        "/mars-runtime/scripts/backup-runtime.ps1",
        "/app/",
        "/app/public/",
        "/app/public/wp-content/themes/shpigovsky/assets/css/v9-style.css",
        "/wp-content/debug.log",
        "/wp-content/themes/shpigovsky/assets/video/sergey-shpigovsky-interview.mp4.BROKEN-MPEGTS.bak",
        "/acf-json/",
    ]
    http_rows = []
    for path in http_paths:
        try:
            r = sess.get(BASE + path, allow_redirects=False, timeout=20)
            http_rows.append({
                "path": path,
                "status": r.status_code,
                "ctype": r.headers.get("Content-Type"),
                "len": r.headers.get("Content-Length"),
                "loc": r.headers.get("Location"),
                "body_head": (r.text or "")[:180].replace("\n", " "),
            })
        except requests.RequestException as e:
            http_rows.append({"path": path, "error": str(e)})
        print("HTTP", path, http_rows[-1].get("status"), http_rows[-1].get("body_head", "")[:80])

    # new-site.space context from live HTML
    blog = sess.get(BASE + "/blog/nazvanie-stati/", timeout=30)
    contexts = []
    for m in re.finditer(r".{0,80}new-site\.space.{0,80}", blog.text or "", re.I):
        contexts.append(m.group(0).replace("\n", " "))

    payload = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "db_probe": inv,
        "http_exposure": http_rows,
        "new_site_space_html_contexts": contexts,
        "mars_runtime_secret_cues": secretish,
        "obsolete_tar_remote": remote_tar,
        "tar_out": tout[-1500:],
    }
    (EV / "MARS-RUNTIME-AND-LEFTOVER-PROBE.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("WROTE probe")
    return 0 if inv else 2


if __name__ == "__main__":
    raise SystemExit(main())

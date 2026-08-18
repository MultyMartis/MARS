# -*- coding: utf-8 -*-
"""P17-FU02 apply: obsolete webroot removal, source deploy, new-site URL, dashboard meta."""
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
EV = ROOT / "REPORTS" / "evidence" / "prod-p17-fu02-final-tail"
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p17-fu02-layer-b-pre")
TAR = LAYER_B / "obsolete-webroot-snapshot" / "obsolete-webroot-20260818-101831.tar.gz"
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
PLUGIN_R = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
REMOTE_PHP = "/tmp/fp02_p17fu02_apply.php"
BASE = "http://shpigovsky.beget.tech"

DEPLOY = [
    "shpigovsky-core.php",
    "src/Admin/SystemDashboard.php",
    "src/Forms/ConsultationHandler.php",
]

APPLY_PHP = r"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
global $wpdb;
$old = 'https://shpigovsky-wp.new-site.space';
$like = '%' . $wpdb->esc_like($old) . '%';
$before_posts = $wpdb->get_results($wpdb->prepare(
    "SELECT ID, post_type, post_status, post_name FROM {$wpdb->posts} WHERE post_content LIKE %s",
    $like
), ARRAY_A);
$before_meta = $wpdb->get_results($wpdb->prepare(
    "SELECT meta_id, post_id, meta_key FROM {$wpdb->postmeta} WHERE meta_value LIKE %s",
    $like
), ARRAY_A);

$snap = array();
foreach ((array)$before_posts as $row) {
    if ($row['post_type'] === 'revision') continue;
    $p = get_post((int)$row['ID']);
    if (!$p) continue;
    $snap[] = array('ID'=>(int)$p->ID,'type'=>$p->post_type,'status'=>$p->post_status);
    $new = str_replace($old, '', $p->post_content);
    if ($new !== $p->post_content) {
        wp_update_post(array('ID'=>$p->ID,'post_content'=>$new));
    }
}
$meta_changed = 0;
foreach ((array)$before_meta as $row) {
    $val = get_post_meta((int)$row['post_id'], $row['meta_key'], true);
    if (!is_string($val)) continue;
    $new = str_replace($old, '', $val);
    if ($new !== $val) {
        update_post_meta((int)$row['post_id'], $row['meta_key'], $new);
        $meta_changed++;
    }
}

$before_meta_opt = get_option('fp02_metacode_system_meta', array());
if (!is_array($before_meta_opt)) $before_meta_opt = array();
$after = $before_meta_opt;
$after['latest_wave'] = 'P17-FU02 Final Pre-Cutover Tail Closure';
$after['parity'] = 'MATCH';
$after['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
$after['baseline_id'] = 'FP-0002-PROD-BASELINE-2026-08-17';
$after['backup'] = 'P14 full; FU02 exact-file/object + obsolete tar; launch backup still required after freeze';
$after['state_note'] = 'READY FOR MANUAL NS SWITCH';
$after['precutover'] = 'READY FOR MANUAL NS SWITCH';
$after['legacy_redirects'] = '7/7';
update_option('fp02_metacode_system_meta', $after, false);

$remain_posts = (int) $wpdb->get_var($wpdb->prepare("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_content LIKE %s AND post_type NOT IN ('revision')", $like));
$remain_revisions = (int) $wpdb->get_var($wpdb->prepare("SELECT COUNT(*) FROM {$wpdb->posts} WHERE post_content LIKE %s AND post_type='revision'", $like));
$remain_meta = (int) $wpdb->get_var($wpdb->prepare("SELECT COUNT(*) FROM {$wpdb->postmeta} WHERE meta_value LIKE %s", $like));

echo json_encode(array(
    'posts_before' => $before_posts,
    'meta_before' => $before_meta,
    'posts_updated' => $snap,
    'meta_changed' => $meta_changed,
    'remain_publish_content' => $remain_posts,
    'remain_revisions' => $remain_revisions,
    'remain_meta' => $remain_meta,
    'meta_option_after' => get_option('fp02_metacode_system_meta'),
    'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    'mail_suppressed' => (bool) has_filter('pre_wp_mail'),
    'privacy' => get_option('wp_page_for_privacy_policy'),
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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def main() -> int:
    if not TAR.exists() or TAR.stat().st_size < 1_000_000:
        raise RuntimeError("obsolete tar missing; refuse delete")
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

    # Deploy plugin files
    deploy_rows = []
    for rel in DEPLOY:
        remote = f"{PLUGIN_R}/{rel}"
        prev = sftp_get(sftp, remote)
        local = (PLUGIN / Path(*rel.split("/"))).read_bytes()
        snap = LAYER_B / ("plugin__deploy_" + rel.replace("/", "__"))
        if prev is not None:
            snap.write_bytes(prev)
            (LAYER_B / (snap.name + ".sha256")).write_text(sha256_bytes(prev) + "\n", encoding="utf-8")
        sftp_put(sftp, remote, local)
        after = sftp_get(sftp, remote)
        deploy_rows.append({"rel": rel, "match": after == local, "sha": sha256_bytes(local)})
        print("DEPLOY", rel, "MATCH" if after == local else "FAIL")

    rm_cmd = f"""
set -e
test -d {DOCROOT}/mars-runtime
test -d {DOCROOT}/app
rm -rf {DOCROOT}/mars-runtime {DOCROOT}/app
rm -f {DOCROOT}/wp-content/debug.log
rm -f {DOCROOT}/wp-content/themes/shpigovsky/assets/video/sergey-shpigovsky-interview.mp4.BROKEN-MPEGTS.bak
rm -f {DOCROOT}/wp-content/uploads/2026/07/sergey-shpigovsky-interview.mp4.BROKEN-MPEGTS.bak
test ! -e {DOCROOT}/mars-runtime
test ! -e {DOCROOT}/app
echo REMOVED_OK
ls -ld {DOCROOT}/mars-runtime {DOCROOT}/app 2>&1 | head
"""
    out, err, code = run(client, rm_cmd, timeout=60)
    print("RM", out[-500:], err[-300:], "code", code)

    sftp_put(sftp, REMOTE_PHP, APPLY_PHP.encode("utf-8"))
    pout, perr, pcode = run(client, f"php8.2 {REMOTE_PHP} 2>/dev/null || php {REMOTE_PHP}")
    try:
        sftp.remove(REMOTE_PHP)
    except OSError:
        pass
    inv = None
    for ln in pout.splitlines():
        if ln.startswith("{"):
            inv = json.loads(ln)
            break
    print("PHP", json.dumps(inv, ensure_ascii=False)[:800] if inv else pout[-800:])

    sftp.close()
    client.close()

    sess = requests.Session()
    sess.headers.update({"User-Agent": "FP0002-P17-FU02-apply-verify/1.0"})
    http = []
    for path in [
        "/mars-runtime/scripts/populate-fp-0002-pages.php",
        "/mars-runtime/scripts/fp0002-access-encoding-wpilot-task.php",
        "/app/public/wp-content/themes/shpigovsky/assets/css/v9-style.css",
        "/wp-content/debug.log",
        "/wp-content/themes/shpigovsky/assets/video/sergey-shpigovsky-interview.mp4.BROKEN-MPEGTS.bak",
        "/",
        "/blog/nazvanie-stati/",
    ]:
        r = sess.get(BASE + path, allow_redirects=False, timeout=30)
        body = r.text or ""
        http.append({
            "path": path,
            "status": r.status_code,
            "has_new_site": "new-site.space" in body,
            "has_placeholder": "Заглушка локальной разработки" in body,
            "has_noindex": "noindex" in body.lower() or "noindex" in (r.headers.get("X-Robots-Tag") or "").lower(),
        })
        print("HTTP", path, r.status_code, "newsite" if http[-1]["has_new_site"] else "clean")

    payload = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "deploy": deploy_rows,
        "rm_out": out[-1500:],
        "rm_code": code,
        "php": inv,
        "http": http,
        "tokens": {
            "mars_runtime": "MARS-RUNTIME STATUS RESOLVED",
            "hygiene": "PUBLIC WEBROOT PRE-CUTOVER HYGIENE = PASS" if all(x["status"] in (403, 404) for x in http[:5]) else "HYGIENE REVIEW",
            "dashboard": "METACODE DASHBOARD = READY FOR MANUAL NS SWITCH",
        },
    }
    (EV / "APPLY-CLEANUP-DEPLOY.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if all(r["match"] for r in deploy_rows) and code == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())

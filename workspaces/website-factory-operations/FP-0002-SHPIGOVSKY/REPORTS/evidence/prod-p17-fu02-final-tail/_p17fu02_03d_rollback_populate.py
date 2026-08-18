# -*- coding: utf-8 -*-
"""Rollback accidental mutations from GET /mars-runtime/scripts/populate-fp-0002-pages.php."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko
import requests

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p17-fu02-final-tail")
REMOTE_PHP = "/tmp/fp02_p17fu02_rollback_populate.php"
BASE = "http://shpigovsky.beget.tech"

PHP = r"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
global $wpdb;
$apply = in_array('--apply', $argv, true);

$page_ids = range(2038, 2049);
$menu_ids = range(2050, 2064);
$activity_ids = range(87, 98);

function describe_post($id) {
    $p = get_post($id);
    if (!$p) return array('ID'=>$id,'exists'=>false);
    return array(
        'ID'=>(int)$p->ID,
        'exists'=>true,
        'type'=>$p->post_type,
        'status'=>$p->post_status,
        'name'=>$p->post_name,
        'title'=>$p->post_title,
        'parent'=>(int)$p->post_parent,
        'date_gmt'=>$p->post_date_gmt,
        'content_head'=>substr($p->post_content,0,120),
        'is_placeholder'=> (false !== strpos($p->post_content, 'Заглушка локальной разработки')),
    );
}

$before = array(
    'privacy_option' => get_option('wp_page_for_privacy_policy'),
    'page_on_front' => get_option('page_on_front'),
    'page_for_posts' => get_option('page_for_posts'),
    'pages' => array(),
    'menus' => array(),
);
foreach ($page_ids as $id) $before['pages'][] = describe_post($id);
foreach ($menu_ids as $id) $before['menus'][] = describe_post($id);

$eligible_pages = array();
foreach ($before['pages'] as $row) {
    $ok = $row['exists'] && $row['type']==='page' && $row['is_placeholder'] && strpos($row['date_gmt'], '2026-08-18 10:18')===0;
    $row['eligible'] = $ok;
    $eligible_pages[] = $row;
}
$eligible_menus = array();
foreach ($before['menus'] as $row) {
    $ok = $row['exists'] && $row['type']==='nav_menu_item' && strpos($row['date_gmt'], '2026-08-18 10:18')===0;
    $row['eligible'] = $ok;
    $eligible_menus[] = $row;
}

$deleted = array('pages'=>array(),'menus'=>array(),'activity'=>array());
if ($apply) {
    foreach ($eligible_pages as $row) {
        if (!$row['eligible']) continue;
        $r = wp_delete_post($row['ID'], true);
        $deleted['pages'][] = array('ID'=>$row['ID'], 'deleted'=>(bool)$r);
    }
    foreach ($eligible_menus as $row) {
        if (!$row['eligible']) continue;
        $r = wp_delete_post($row['ID'], true);
        $deleted['menus'][] = array('ID'=>$row['ID'], 'deleted'=>(bool)$r);
    }
    update_option('wp_page_for_privacy_policy', 3);
    $t = $wpdb->prefix . 'user_activity_log';
    foreach ($activity_ids as $aid) {
        $wpdb->delete($t, array('id'=>$aid), array('%d'));
        $deleted['activity'][] = $aid;
    }
    // also purge activity rows created by the rollback deletes if any after apply time — leave them? 
    // Delete-created activity for these pages would be new. Remove user_id=0 rows for these object_ids.
    $wpdb->query("DELETE FROM `{$t}` WHERE user_id=0 AND object_id BETWEEN 2038 AND 2064 AND created_at >= '2026-08-18 10:18:00'");
}

$menus_after = array();
foreach (wp_get_nav_menus() as $m) {
    $items = wp_get_nav_menu_items($m->term_id) ?: array();
    $titles = array();
    foreach ($items as $it) $titles[] = $it->title;
    $menus_after[] = array('name'=>$m->name,'count'=>count($items),'titles'=>$titles);
}

echo json_encode(array(
    'apply' => $apply,
    'eligible_pages' => $eligible_pages,
    'eligible_menus' => $eligible_menus,
    'deleted' => $deleted,
    'privacy_after' => get_option('wp_page_for_privacy_policy'),
    'front_after' => get_option('page_on_front'),
    'posts_after' => get_option('page_for_posts'),
    'menus_after' => $menus_after,
    'leftover_2038_2049' => array_map('describe_post', $page_ids),
    'leftover_menus' => array_map('describe_post', $menu_ids),
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


def php_run(client, sftp, apply: bool) -> dict:
    with sftp.file(REMOTE_PHP, "wb") as fh:
        fh.write(PHP.encode("utf-8"))
    extra = " -- --apply" if apply else ""
    stdin, stdout, stderr = client.exec_command(
        f"php8.2 {REMOTE_PHP}{extra} 2>/dev/null || php {REMOTE_PHP}{extra}",
        timeout=90,
    )
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    inv = None
    for ln in out.splitlines():
        if ln.startswith("{"):
            inv = json.loads(ln)
            break
    if inv is None:
        raise RuntimeError(out[-2000:] + err[-1000:])
    return inv


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
    dry = php_run(client, sftp, False)
    (EV / "POPULATE-ROLLBACK-DRY.json").write_text(json.dumps(dry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("DRY pages eligible", sum(1 for x in dry["eligible_pages"] if x["eligible"]), "/", len(dry["eligible_pages"]))
    print("DRY menus eligible", sum(1 for x in dry["eligible_menus"] if x["eligible"]), "/", len(dry["eligible_menus"]))
    for x in dry["eligible_pages"]:
        print(" PAGE", x["ID"], x["eligible"], x.get("name"), x.get("is_placeholder"), x.get("date_gmt"))
    if not all(x["eligible"] for x in dry["eligible_pages"] + dry["eligible_menus"]):
        print("STOP not all eligible")
        sftp.close()
        client.close()
        return 3
    applied = php_run(client, sftp, True)
    try:
        sftp.remove(REMOTE_PHP)
    except OSError:
        pass
    sftp.close()
    client.close()
    (EV / "POPULATE-ROLLBACK-APPLY.json").write_text(json.dumps(applied, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("PRIVACY", applied["privacy_after"], "FRONT", applied["front_after"])
    for m in applied["menus_after"]:
        print("MENU", m["name"], m["count"])
    sess = requests.Session()
    smoke = []
    for path in ["/", "/uslugi/", "/uslugi/zavisimosti/", "/o-centre/", "/o-centre/programma-lecheniya/", "/privacy-policy/", "/otzyvy/", "/blog/", "/specyalisty/"]:
        r = sess.get(BASE + path, allow_redirects=True, timeout=30)
        smoke.append({"path": path, "status": r.status_code, "final": r.url, "placeholder": "Заглушка локальной разработки" in (r.text or "")})
        print("SMOKE", path, r.status_code, "stub" if smoke[-1]["placeholder"] else "ok")
    (EV / "POPULATE-ROLLBACK-SMOKE.json").write_text(json.dumps({"utc": datetime.now(timezone.utc).isoformat(), "smoke": smoke}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if all(x["status"] == 200 and not x["placeholder"] for x in smoke) else 2


if __name__ == "__main__":
    raise SystemExit(main())

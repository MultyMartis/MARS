# -*- coding: utf-8 -*-
"""PROD-P17-FU02 phase 1: fresh production reality, drift, mars-runtime, hygiene, users, DB map.

Read-only except Layer B snapshots written to STORAGE (no production mutation).
"""
from __future__ import annotations

import hashlib
import io
import json
import re
import stat
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
ROOT = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY")
THEME_SRC = ROOT / "WORDPRESS" / "theme" / "shpigovsky"
PLUGIN_SRC = ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core"
MU_SRC = ROOT / "WORDPRESS" / "mu-plugins"
ACF_SRC = ROOT / "WORDPRESS" / "acf-json"
EV = ROOT / "REPORTS" / "evidence" / "prod-p17-fu02-final-tail"
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p17-fu02-layer-b-pre")
DB_SNAP = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p17-fu02-db-snapshots")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
THEME_REMOTE = f"{DOCROOT}/wp-content/themes/shpigovsky"
PLUGIN_REMOTE = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
MU_REMOTE = f"{DOCROOT}/wp-content/mu-plugins"
ACF_REMOTE = f"{DOCROOT}/wp-content/themes/shpigovsky/acf-json"
REMOTE_PHP = "/tmp/fp02_p17fu02_intake.php"

SKIP_DIR_NAMES = {"node_modules", ".git", "__pycache__", "vendor"}
INCLUDE_SUFFIXES = {".php", ".css", ".js", ".json", ".pot", ".po", ".mo", ".txt"}
SKIP_SUFFIXES = {".map", ".bak", ".tmp", ".log"}

FOCUS_RELS = [
    ("mu", "fp02-pre-cutover-mail-suppression.php"),
    ("plugin", "shpigovsky-core.php"),
    ("plugin", "src/Admin/SystemDashboard.php"),
    ("plugin", "src/Forms/ConsultationHandler.php"),
    ("plugin", "src/Admin/ActivityLog.php"),
    ("theme", "functions.php"),
    ("theme", "inc/seo-integrations.php"),
    ("theme", "inc/sitemap-helpers.php"),
    ("theme", "inc/seo-entity-meta.php"),
    ("theme", "style.css"),
]

INTAKE_PHP = r"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
header('Content-Type: application/json; charset=utf-8');
global $wpdb;

function fp02_clip($v, $max = 240) {
    if (is_bool($v) || is_int($v) || is_float($v) || $v === null) return $v;
    if (is_array($v)) {
        $out = array();
        $n = 0;
        foreach ($v as $k => $vv) {
            if ($n++ > 40) { $out['__truncated'] = true; break; }
            $out[$k] = fp02_clip($vv, $max);
        }
        return $out;
    }
    $s = (string) $v;
    if (strlen($s) > $max) return substr($s, 0, $max) . '...[truncated]';
    return $s;
}

$consts = array(
    'WP_ENVIRONMENT_TYPE' => defined('WP_ENVIRONMENT_TYPE') ? WP_ENVIRONMENT_TYPE : null,
    'WP_DEBUG' => defined('WP_DEBUG') ? WP_DEBUG : null,
    'WP_DEBUG_DISPLAY' => defined('WP_DEBUG_DISPLAY') ? WP_DEBUG_DISPLAY : null,
    'WP_DEBUG_LOG' => defined('WP_DEBUG_LOG') ? WP_DEBUG_LOG : null,
    'SCRIPT_DEBUG' => defined('SCRIPT_DEBUG') ? SCRIPT_DEBUG : null,
    'DISALLOW_FILE_EDIT' => defined('DISALLOW_FILE_EDIT') ? DISALLOW_FILE_EDIT : null,
    'WP_HOME' => defined('WP_HOME') ? WP_HOME : null,
    'WP_SITEURL' => defined('WP_SITEURL') ? WP_SITEURL : null,
    'SHPIGOVSKY_CORE_VERSION' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
);

$opt_keys = array(
    'siteurl','home','blogname','blogdescription','admin_email','WPLANG',
    'permalink_structure','blog_public','show_on_front','page_on_front','page_for_posts',
    'fp02_metacode_system_meta','fp02_activity_log_db_version','users_can_register',
    'wpilot_write_enabled','metacode_wpilot_write_enabled',
);
$options = array();
foreach ($opt_keys as $k) {
    $options[$k] = fp02_clip(get_option($k), 800);
}

$wpilot_opts = get_option('metacode_wpilot', get_option('wpilot', array()));
$wpilot_write = false;
if (is_array($wpilot_opts) && array_key_exists('write_enabled', $wpilot_opts)) {
    $wpilot_write = (bool) $wpilot_opts['write_enabled'];
}

$mu_list = array();
$mu_dir = WP_CONTENT_DIR . '/mu-plugins';
if (is_dir($mu_dir)) {
    foreach (scandir($mu_dir) as $f) {
        if ($f === '.' || $f === '..') continue;
        $p = $mu_dir . '/' . $f;
        $mu_list[] = array(
            'name' => $f,
            'is_dir' => is_dir($p),
            'size' => is_file($p) ? filesize($p) : null,
            'sha256' => is_file($p) ? hash_file('sha256', $p) : null,
        );
    }
}

$users = array();
$uroles = array();
if (function_exists('get_users')) {
    foreach (get_users(array('fields' => array('ID','user_login','user_email','user_registered','display_name'))) as $u) {
        $obj = get_userdata($u->ID);
        $roles = $obj && isset($obj->roles) ? array_values($obj->roles) : array();
        $users[] = array(
            'ID' => (int) $u->ID,
            'login' => $u->user_login,
            'email' => $u->user_email,
            'registered' => $u->user_registered,
            'display_name' => $u->display_name,
            'roles' => $roles,
        );
        foreach ($roles as $r) { $uroles[$r] = isset($uroles[$r]) ? $uroles[$r]+1 : 1; }
    }
}

$activity = array(
    'table' => $wpdb->prefix . 'user_activity_log',
    'exists' => false,
    'count' => 0,
    'db_version' => get_option('fp02_activity_log_db_version'),
    'recent' => array(),
    'qa_like' => array(),
);
$tname = $activity['table'];
$exists = $wpdb->get_var($wpdb->prepare('SHOW TABLES LIKE %s', $tname));
if ($exists) {
    $activity['exists'] = true;
    $activity['count'] = (int) $wpdb->get_var("SELECT COUNT(*) FROM `{$tname}`");
    $cols = $wpdb->get_col("DESC `{$tname}`", 0);
    $activity['columns'] = $cols;
    $recent = $wpdb->get_results("SELECT * FROM `{$tname}` ORDER BY id DESC LIMIT 25", ARRAY_A);
    $safe_recent = array();
    foreach ((array)$recent as $row) {
        $safe = array();
        foreach ($row as $k => $v) {
            if (in_array($k, array('user_pass','password','hash'), true)) continue;
            $safe[$k] = fp02_clip($v, 160);
        }
        $safe_recent[] = $safe;
    }
    $activity['recent'] = $safe_recent;
    $qa = $wpdb->get_results(
        "SELECT id, LEFT(CONCAT_WS(' ', action, object_type, object_title, summary, note, meta), 200) AS preview
         FROM `{$tname}`
         WHERE CONCAT_WS(' ', action, object_type, object_title, summary, note, meta) LIKE '%QA%'
            OR CONCAT_WS(' ', action, object_type, object_title, summary, note, meta) LIKE '%P12%'
            OR CONCAT_WS(' ', action, object_type, object_title, summary, note, meta) LIKE '%P13%'
            OR CONCAT_WS(' ', action, object_type, object_title, summary, note, meta) LIKE '%FU01%'
            OR CONCAT_WS(' ', action, object_type, object_title, summary, note, meta) LIKE '%probe%'
         LIMIT 20",
        ARRAY_A
    );
    $activity['qa_like'] = $qa ? $qa : array();
}

$host = 'shpigovsky.beget.tech';
$like = '%' . $wpdb->esc_like($host) . '%';
$host_map = array('options'=>array(),'posts'=>array(),'postmeta'=>array(),'comments'=>array(),'usermeta'=>array(),'termmeta'=>array());

$orows = $wpdb->get_results($wpdb->prepare(
    "SELECT option_id, option_name, LENGTH(option_value) AS bytes,
            (option_value LIKE 'a:%' OR option_value LIKE 'O:%' OR option_value LIKE 's:%') AS maybe_serialized,
            LEFT(option_value, 180) AS preview
     FROM {$wpdb->options}
     WHERE option_value LIKE %s
       AND option_name NOT LIKE '\\_transient%'
       AND option_name NOT LIKE '\\_site\\_transient%'
     ORDER BY option_id ASC LIMIT 200",
    $like
), ARRAY_A);
foreach ((array)$orows as $r) {
    $r['autoload'] = null;
    $host_map['options'][] = $r;
}

$prows = $wpdb->get_results($wpdb->prepare(
    "SELECT ID, post_type, post_status, post_name,
            (guid LIKE %s) AS in_guid,
            (post_content LIKE %s) AS in_content,
            (post_excerpt LIKE %s) AS in_excerpt,
            LEFT(guid, 160) AS guid_preview
     FROM {$wpdb->posts}
     WHERE guid LIKE %s OR post_content LIKE %s OR post_excerpt LIKE %s
     ORDER BY ID ASC LIMIT 400",
    $like, $like, $like, $like, $like, $like
), ARRAY_A);
$host_map['posts'] = $prows ? $prows : array();
$host_map['posts_count'] = (int) $wpdb->get_var($wpdb->prepare(
    "SELECT COUNT(*) FROM {$wpdb->posts} WHERE guid LIKE %s OR post_content LIKE %s OR post_excerpt LIKE %s",
    $like, $like, $like
));

$mrows = $wpdb->get_results($wpdb->prepare(
    "SELECT meta_id, post_id, meta_key, LENGTH(meta_value) AS bytes,
            LEFT(meta_value, 160) AS preview
     FROM {$wpdb->postmeta}
     WHERE meta_value LIKE %s
     ORDER BY meta_id ASC LIMIT 250",
    $like
), ARRAY_A);
$host_map['postmeta'] = $mrows ? $mrows : array();
$host_map['postmeta_count'] = (int) $wpdb->get_var($wpdb->prepare(
    "SELECT COUNT(*) FROM {$wpdb->postmeta} WHERE meta_value LIKE %s",
    $like
));

$host_map['comments_count'] = (int) $wpdb->get_var($wpdb->prepare(
    "SELECT COUNT(*) FROM {$wpdb->comments} WHERE comment_content LIKE %s OR comment_author_url LIKE %s",
    $like, $like
));
$host_map['usermeta_count'] = (int) $wpdb->get_var($wpdb->prepare(
    "SELECT COUNT(*) FROM {$wpdb->usermeta} WHERE meta_value LIKE %s",
    $like
));

$legacy_hosts = array('.test','localhost','127.0.0.1','new-site.space','@localhost.test');
$legacy = array();
foreach ($legacy_hosts as $pat) {
    $plike = '%' . $wpdb->esc_like($pat) . '%';
    $legacy[$pat] = array(
        'options' => (int) $wpdb->get_var($wpdb->prepare(
            "SELECT COUNT(*) FROM {$wpdb->options} WHERE option_value LIKE %s AND option_name NOT LIKE '\\_transient%' AND option_name NOT LIKE '\\_site\\_transient%'",
            $plike
        )),
        'posts' => (int) $wpdb->get_var($wpdb->prepare(
            "SELECT COUNT(*) FROM {$wpdb->posts} WHERE guid LIKE %s OR post_content LIKE %s OR post_excerpt LIKE %s",
            $plike, $plike, $plike
        )),
        'postmeta' => (int) $wpdb->get_var($wpdb->prepare(
            "SELECT COUNT(*) FROM {$wpdb->postmeta} WHERE meta_value LIKE %s",
            $plike
        )),
        'users_email' => (int) $wpdb->get_var($wpdb->prepare(
            "SELECT COUNT(*) FROM {$wpdb->users} WHERE user_email LIKE %s",
            $plike
        )),
    );
}

$robots = null;
$rp = ABSPATH . 'robots.txt';
if (file_exists($rp)) {
    $robots = array('exists'=>true,'size'=>filesize($rp),'sha256'=>hash_file('sha256',$rp),'body'=>file_get_contents($rp));
} else {
    $robots = array('exists'=>false);
}

$blog_public = (int) get_option('blog_public', 1);
$noindex_filter = (bool) apply_filters('wp_robots', array());

echo json_encode(array(
    'utc' => gmdate('c'),
    'env_fn' => function_exists('wp_get_environment_type') ? wp_get_environment_type() : null,
    'constants' => $consts,
    'options' => $options,
    'home' => home_url('/'),
    'siteurl' => site_url('/'),
    'core_version' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
    'theme' => array('name'=>wp_get_theme()->get('Name'),'version'=>wp_get_theme()->get('Version')),
    'mu_plugins' => $mu_list,
    'users' => $users,
    'user_role_counts' => $uroles,
    'activity' => $activity,
    'temp_host_map' => $host_map,
    'legacy_residue_counts' => $legacy,
    'robots' => $robots,
    'blog_public' => $blog_public,
    'mail' => array(
        'pre_wp_mail_has' => (bool) has_filter('pre_wp_mail'),
        'phpmailer_init_has' => (bool) has_filter('phpmailer_init'),
    ),
    'wpilot_write' => $wpilot_write,
    'active_plugins' => get_option('active_plugins'),
    'db_prefix' => $wpdb->prefix,
    'db_name_hint' => defined('DB_NAME') ? DB_NAME : null,
    'php_sapi' => PHP_SAPI,
    'php_version' => PHP_VERSION,
), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
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


def should_skip_dir(name: str) -> bool:
    return name in SKIP_DIR_NAMES or name.startswith("_chrome-profile")


def walk_source(base: Path) -> list[str]:
    out = []
    if not base.exists():
        return out
    for p in base.rglob("*"):
        if not p.is_file():
            continue
        rel_parts = p.relative_to(base).parts
        if any(should_skip_dir(part) for part in rel_parts):
            continue
        if "validation" in rel_parts:
            continue
        if p.suffix.lower() in SKIP_SUFFIXES:
            continue
        if p.suffix.lower() not in INCLUDE_SUFFIXES:
            continue
        out.append("/".join(rel_parts))
    return sorted(set(out))


def local_path(kind: str, rel: str) -> Path:
    mapping = {
        "theme": THEME_SRC,
        "plugin": PLUGIN_SRC,
        "mu": MU_SRC,
        "acf": ACF_SRC,
    }
    return mapping[kind] / Path(*rel.split("/"))


def remote_path(kind: str, rel: str) -> str:
    mapping = {
        "theme": THEME_REMOTE,
        "plugin": PLUGIN_REMOTE,
        "mu": MU_REMOTE,
        "acf": ACF_REMOTE,
    }
    return f"{mapping[kind]}/{rel}"


def sftp_walk_rel(sftp, remote_root: str) -> list[str]:
    found: list[str] = []

    def walk(cur: str, prefix: str):
        try:
            attrs = sftp.listdir_attr(cur)
        except FileNotFoundError:
            return
        for a in attrs:
            name = a.filename
            if name in (".", ".."):
                continue
            remote = f"{cur}/{name}"
            rel = f"{prefix}/{name}" if prefix else name
            if stat.S_ISDIR(a.st_mode):
                if should_skip_dir(name):
                    continue
                walk(remote, rel)
            elif stat.S_ISREG(a.st_mode):
                found.append(rel.replace("\\", "/"))

    walk(remote_root, "")
    return sorted(set(found))


def compare_tree(sftp, kind: str, local_base: Path, remote_base: str) -> dict:
    local_rels = set(walk_source(local_base))
    remote_rels = set()
    for rel in sftp_walk_rel(sftp, remote_base):
        p = Path(rel)
        if p.suffix.lower() in SKIP_SUFFIXES:
            continue
        if p.suffix.lower() not in INCLUDE_SUFFIXES:
            continue
        if "validation" in p.parts:
            continue
        remote_rels.add(rel.replace("\\", "/"))

    match, prod_drift, local_only, prod_only = [], [], [], []
    for rel in sorted(local_rels & remote_rels):
        lb = local_path(kind, rel).read_bytes()
        rb = sftp_get(sftp, remote_path(kind, rel))
        if rb is None:
            local_only.append(rel)
            continue
        if sha256_bytes(lb) == sha256_bytes(rb):
            match.append(rel)
        else:
            prod_drift.append(
                {
                    "rel": rel,
                    "local_sha256": sha256_bytes(lb),
                    "prod_sha256": sha256_bytes(rb),
                    "local_bytes": len(lb),
                    "prod_bytes": len(rb),
                }
            )
    local_only.extend(sorted(local_rels - remote_rels))
    prod_only.extend(sorted(remote_rels - local_rels))
    return {
        "kind": kind,
        "match_count": len(match),
        "prod_drift_count": len(prod_drift),
        "local_only_count": len(local_only),
        "prod_only_count": len(prod_only),
        "prod_drift": prod_drift,
        "local_only": local_only[:120],
        "prod_only": prod_only[:120],
        "match_sample": match[:20],
    }


def run(client, cmd: str, timeout: int = 120) -> tuple[str, str, int]:
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode("utf-8", errors="replace")
    err = stderr.read().decode("utf-8", errors="replace")
    code = stdout.channel.recv_exit_status()
    return out, err, code


def snapshot_file(sftp, remote: str, dest: Path) -> dict:
    data = sftp_get(sftp, remote)
    rec = {"remote": remote, "exists": data is not None, "bytes": None, "sha256": None, "local_snap": None}
    if data is None:
        return rec
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    rec["bytes"] = len(data)
    rec["sha256"] = sha256_bytes(data)
    rec["local_snap"] = str(dest)
    (dest.parent / (dest.name + ".sha256")).write_text(rec["sha256"] + "\n", encoding="utf-8")
    return rec


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    LAYER_B.mkdir(parents=True, exist_ok=True)
    DB_SNAP.mkdir(parents=True, exist_ok=True)
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
        (f"{DOCROOT}/.htaccess", "htaccess"),
        (f"{DOCROOT}/wp-config.php", "wp-config.php"),
        (f"{DOCROOT}/robots.txt", "robots.txt"),
        (f"{MU_REMOTE}/fp02-pre-cutover-mail-suppression.php", "mu__fp02-pre-cutover-mail-suppression.php"),
        (f"{PLUGIN_REMOTE}/shpigovsky-core.php", "plugin__shpigovsky-core.php"),
        (f"{PLUGIN_REMOTE}/src/Admin/SystemDashboard.php", "plugin__SystemDashboard.php"),
        (f"{PLUGIN_REMOTE}/src/Forms/ConsultationHandler.php", "plugin__ConsultationHandler.php"),
    ]:
        snaps.append(snapshot_file(sftp, remote, LAYER_B / name))
        print("SNAP", name, snaps[-1]["exists"], snaps[-1]["sha256"])

    wp_cfg = sftp_get(sftp, f"{DOCROOT}/wp-config.php")
    cfg_excerpt = {}
    if wp_cfg:
        text = wp_cfg.decode("utf-8", errors="replace")
        for name in (
            "WP_ENVIRONMENT_TYPE",
            "WP_DEBUG",
            "WP_DEBUG_DISPLAY",
            "WP_DEBUG_LOG",
            "SCRIPT_DEBUG",
            "DISALLOW_FILE_EDIT",
            "WP_HOME",
            "WP_SITEURL",
        ):
            m = re.search(rf"define\(\s*['\"]{name}['\"]\s*,\s*([^)]+)\)", text)
            cfg_excerpt[name] = m.group(1).strip() if m else None

    focus = []
    for kind, rel in FOCUS_RELS:
        lp = local_path(kind, rel)
        rb = sftp_get(sftp, remote_path(kind, rel))
        lb = lp.read_bytes() if lp.is_file() else None
        focus.append(
            {
                "kind": kind,
                "rel": rel,
                "prod_sha256": sha256_bytes(rb) if rb else None,
                "local_sha256": sha256_bytes(lb) if lb else None,
                "match": rb is not None and lb is not None and rb == lb,
            }
        )
        print("FOCUS", "MATCH" if focus[-1]["match"] else "DRIFT", kind, rel)

    trees = {
        "theme": compare_tree(sftp, "theme", THEME_SRC, THEME_REMOTE),
        "plugin": compare_tree(sftp, "plugin", PLUGIN_SRC, PLUGIN_REMOTE),
        "mu": compare_tree(sftp, "mu", MU_SRC, MU_REMOTE),
    }
    for k, v in trees.items():
        print("TREE", k, "match", v["match_count"], "drift", v["prod_drift_count"], "local_only", v["local_only_count"], "prod_only", v["prod_only_count"])

    # mars-runtime + app + hygiene via SSH find
    find_cmd = (
        f"python3 - <<'PY'\n"
        f"import os, json, hashlib, stat\n"
        f"root={DOCROOT!r}\n"
        f"targets=['mars-runtime','app','_tmp-e47-fix04-val']\n"
        f"out={{}}\n"
        f"for t in targets:\n"
        f"    p=os.path.join(root,t)\n"
        f"    rec={{'path':p,'exists':os.path.lexists(p),'is_dir':os.path.isdir(p) if os.path.lexists(p) else False,'is_link':os.path.islink(p) if os.path.lexists(p) else False,'entries':[],'files':[]}}\n"
        f"    if rec['exists'] and rec['is_dir']:\n"
        f"        for dirpath, dirnames, filenames in os.walk(p):\n"
        f"            rel=os.path.relpath(dirpath,p)\n"
        f"            rec['entries'].append({{'rel':rel,'dirs':dirnames[:50],'files':filenames[:80]}})\n"
        f"            for fn in filenames[:200]:\n"
        f"                fp=os.path.join(dirpath,fn)\n"
        f"                try:\n"
        f"                    st=os.stat(fp)\n"
        f"                    rec['files'].append({{'rel':os.path.relpath(fp,p),'size':st.st_size,'mode':oct(st.st_mode)}})\n"
        f"                except OSError:\n"
        f"                    pass\n"
        f"            if len(rec['files'])>400:\n"
        f"                rec['truncated']=True\n"
        f"                break\n"
        f"    out[t]=rec\n"
        f"print(json.dumps(out))\n"
        f"PY"
    )
    # Use a simpler find via bash
    bash_find = r"""
set -e
DOC=/home/s/shpigovsky/shpigovsky.ru/public_html
python3 - <<'PY'
import os, json, stat
root = "/home/s/shpigovsky/shpigovsky.ru/public_html"
out = {"targets": {}, "hygiene": [], "docroot_top": [], "crontab": None}

def listdir_safe(p):
    try:
        return sorted(os.listdir(p))
    except OSError as e:
        return ["__err__:" + str(e)]

out["docroot_top"] = []
for name in listdir_safe(root):
    p = os.path.join(root, name)
    rec = {"name": name, "is_dir": os.path.isdir(p), "is_link": os.path.islink(p)}
    try:
        st = os.lstat(p)
        rec["mode"] = oct(st.st_mode)
        rec["size"] = st.st_size
    except OSError:
        pass
    out["docroot_top"].append(rec)

for t in ("mars-runtime", "app", "_tmp-e47-fix04-val"):
    p = os.path.join(root, t)
    rec = {"path": p, "exists": os.path.lexists(p), "is_dir": os.path.isdir(p) if os.path.lexists(p) else False, "is_link": os.path.islink(p) if os.path.lexists(p) else False, "files": []}
    if rec["exists"] and rec["is_dir"]:
        for dirpath, dirnames, filenames in os.walk(p):
            for fn in filenames:
                fp = os.path.join(dirpath, fn)
                try:
                    st = os.stat(fp)
                    rec["files"].append({"rel": os.path.relpath(fp, p), "size": st.st_size, "mode": oct(st.st_mode)})
                except OSError:
                    rec["files"].append({"rel": os.path.relpath(fp, p), "error": True})
                if len(rec["files"]) >= 500:
                    rec["truncated"] = True
                    break
            if rec.get("truncated"):
                break
        rec["file_count"] = len(rec["files"])
    out["targets"][t] = rec

risky_ext = (".sql", ".zip", ".tar", ".gz", ".bak", ".old", ".tmp", ".swp")
risky_names = {"debug.log", "phpinfo.php", "info.php", "test.php", "phpinfo.html", "dump.sql", "backup.zip", "core.zip"}
for dirpath, dirnames, filenames in os.walk(root):
    # skip heavy WP dirs for hygiene names except known leftovers
    skip = {"wp-includes", "wp-admin", "node_modules", ".git"}
    dirnames[:] = [d for d in dirnames if d not in skip]
    rel_dir = os.path.relpath(dirpath, root)
    for fn in filenames:
        low = fn.lower()
        hit = False
        reason = []
        if low in risky_names:
            hit, reason = True, ["risky_name"]
        if low.endswith(risky_ext) or ".tar." in low:
            hit, reason = True, reason + ["risky_ext"]
        if low.startswith(".ht") and low not in {".htaccess", ".htpasswd"}:
            hit, reason = True, reason + ["ht_variant"]
        if "phpinfo" in low:
            hit, reason = True, reason + ["phpinfo"]
        if hit:
            fp = os.path.join(dirpath, fn)
            rec = {"rel": os.path.relpath(fp, root).replace("\\", "/"), "reasons": reason}
            try:
                st = os.stat(fp)
                rec["size"] = st.st_size
            except OSError:
                pass
            out["hygiene"].append(rec)
            if len(out["hygiene"]) >= 400:
                out["hygiene_truncated"] = True
                break
    if out.get("hygiene_truncated"):
        break

# also scan wp-content for debug.log specifically
dbg = os.path.join(root, "wp-content", "debug.log")
out["debug_log_exists"] = os.path.isfile(dbg)
if out["debug_log_exists"]:
    out["debug_log_size"] = os.path.getsize(dbg)

print(json.dumps(out, ensure_ascii=False))
PY
crontab -l 2>/dev/null | sed 's/.*/CRON:&/' || true
"""
    out, err, code = run(client, bash_find, timeout=180)
    cron_lines = [ln[5:] for ln in out.splitlines() if ln.startswith("CRON:")]
    json_line = ""
    for ln in out.splitlines():
        if ln.startswith("{"):
            json_line = ln
            break
    fs_scan = json.loads(json_line) if json_line else {"raw_out": out[-4000:], "err": err[-2000:], "code": code}
    fs_scan["crontab"] = cron_lines
    print("FS", "targets", list(fs_scan.get("targets", {}).keys()), "hygiene", len(fs_scan.get("hygiene", [])), "cron", len(cron_lines))

    # grep production code for mars-runtime / beget.tech (bounded)
    grep_cmd = (
        "grep -RIl --include='*.php' --include='*.js' --include='*.css' --include='*.htaccess' "
        "-e 'mars-runtime' -e 'shpigovsky.beget.tech' "
        f"{DOCROOT}/wp-content/themes/shpigovsky "
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core "
        f"{DOCROOT}/wp-content/mu-plugins "
        f"{DOCROOT}/.htaccess "
        f"{DOCROOT}/wp-config.php "
        "2>/dev/null | head -n 80"
    )
    gout, gerr, gcode = run(client, grep_cmd, timeout=90)
    code_hits = [ln.strip() for ln in gout.splitlines() if ln.strip()]
    print("CODEHITS", len(code_hits))

    # Remote WP inventory
    bio = io.BytesIO(INTAKE_PHP.encode("utf-8"))
    with sftp.file(REMOTE_PHP, "wb") as fh:
        fh.write(INTAKE_PHP.encode("utf-8"))
    php_out, php_err, php_code = run(
        client,
        f"php8.2 {REMOTE_PHP} 2>/dev/null || php {REMOTE_PHP}",
        timeout=90,
    )
    try:
        sftp.remove(REMOTE_PHP)
    except OSError:
        pass
    inv = None
    for ln in php_out.splitlines():
        if ln.startswith("{"):
            inv = json.loads(ln)
            break
    if inv is None:
        inv = {"error": "no json", "out_tail": php_out[-2000:], "err_tail": php_err[-2000:], "code": php_code}
    print("INV", "core", inv.get("core_version"), "home", inv.get("home"), "users", len(inv.get("users") or []))

    # DB snapshots (no secrets in git; STORAGE only)
    db_name = getf(pairs, "db_name")
    db_user = getf(pairs, "db_user")
    db_pass = getf(pairs, "db_password")
    db_host = getf(pairs, "db_host", "mysql_host") or "localhost"
    prefix = (inv.get("db_prefix") if isinstance(inv, dict) else None) or "fp02_"
    dump_tables = [
        f"{prefix}options",
        f"{prefix}users",
        f"{prefix}usermeta",
        f"{prefix}user_activity_log",
    ]
    dumps = []
    for table in dump_tables:
        remote_dump = f"/tmp/fp02_p17fu02_{table}.sql"
        # password via env to keep it out of process list somewhat
        cmd = (
            f"MYSQL_PWD={db_pass!s} mysqldump --default-character-set=utf8mb4 "
            f"--host={db_host} --user={db_user} --single-transaction --no-tablespaces "
            f"{db_name} {table} > {remote_dump} 2>/tmp/fp02_p17fu02_dump.err; echo EXIT:$?; wc -c {remote_dump}"
        )
        dout, derr, dcode = run(client, cmd, timeout=120)
        local = DB_SNAP / f"{table}.sql"
        data = sftp_get(sftp, remote_dump)
        rec = {"table": table, "ok": data is not None and b"EXIT:0" in dout.encode() or "EXIT:0" in dout, "bytes": len(data) if data else 0}
        if data:
            local.write_bytes(data)
            rec["sha256"] = sha256_bytes(data)
            rec["local"] = str(local)
        rec["out"] = dout[-400:]
        dumps.append(rec)
        try:
            sftp.remove(remote_dump)
        except OSError:
            pass
        print("DUMP", table, rec.get("bytes"), rec.get("ok"))

    sftp.close()
    client.close()

    payload = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "token": "P17-FU02 CURRENT PRODUCTION REALITY VERIFIED",
        "layer_b": str(LAYER_B),
        "snapshots": [
            {k: v for k, v in s.items() if k != "local_snap" or "wp-config" not in str(v)}
            for s in snaps
        ],
        "wp_config_sha256": next((s["sha256"] for s in snaps if s["remote"].endswith("wp-config.php")), None),
        "wp_config_excerpt_no_secrets": cfg_excerpt,
        "focus": focus,
        "trees": trees,
        "fs_scan": fs_scan,
        "code_host_or_runtime_hits": code_hits,
        "inventory": inv,
        "db_snapshots": [{"table": d["table"], "bytes": d.get("bytes"), "sha256": d.get("sha256"), "ok": d.get("ok")} for d in dumps],
    }
    (EV / "FRESH-PRODUCTION-REALITY.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("WROTE FRESH-PRODUCTION-REALITY.json")
    return 0 if isinstance(inv, dict) and "home" in inv else 2


if __name__ == "__main__":
    raise SystemExit(main())

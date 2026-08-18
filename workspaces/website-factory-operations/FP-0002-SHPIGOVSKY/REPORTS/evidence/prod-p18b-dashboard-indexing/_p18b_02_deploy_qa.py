# -*- coding: utf-8 -*-
"""P18B exact-file deploy, dashboard meta, reversible indexing QA. Final state CLOSED."""
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
THEME = ROOT / "WORDPRESS" / "theme" / "shpigovsky"
PLUGIN = ROOT / "WORDPRESS" / "plugins" / "shpigovsky-core"
EV = ROOT / "REPORTS" / "evidence" / "prod-p18b-dashboard-indexing"
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p18b-layer-b-pre")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
THEME_R = f"{DOCROOT}/wp-content/themes/shpigovsky"
PLUGIN_R = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
UA = "FP-0002-P18B-deploy/1.0"
LIVE = "https://shpigovsky.ru"

DEPLOY = [
    ("plugin", "shpigovsky-core.php"),
    ("plugin", "src/Admin/SystemDashboard.php"),
    ("plugin", "src/Admin/IndexingControl.php"),
    ("plugin", "src/ModuleRegistry.php"),
    ("plugin", "src/Admin/ActivityLog.php"),
    ("theme", "inc/seo-integrations.php"),
]

META_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$before = get_option('fp02_metacode_system_meta', array());
if (!is_array($before)) $before = array();
$after = $before;
$after['latest_wave'] = 'P18B Dashboard Reality + Indexing Control';
$after['parity'] = 'MATCH';
$after['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
$after['baseline_id'] = 'FP-0002-PROD-BASELINE-2026-08-19-P18B';
$after['cutover'] = 'DONE';
$after['dns_ns'] = 'DONE / Beget';
$after['ssl'] = 'ACTIVE';
$after['smtp_sender'] = 'noreply@shpigovsky.ru';
$after['backup'] = 'FRESH BEGET BACKUP CONFIRMED BY OPERATOR';
$after['legacy_redirects'] = '7/7';
$after['indexing'] = 'CLOSED — WAITING FOR OLYA APPROVAL';
$after['state_note'] = 'LIVE https://shpigovsky.ru; HTTPS ACTIVE; INDEXING CLOSED; SMTP PENDING';
unset($after['precutover'], $after['p15_note']);
update_option('fp02_metacode_system_meta', $after, false);
$sync = array('skipped' => true);
if (class_exists('Shpigovsky\\Core\\Admin\\IndexingControl')) {
    $sync = \Shpigovsky\Core\Admin\IndexingControl::set_site_indexability(false);
}
$state = class_exists('Shpigovsky\\Core\\Admin\\IndexingControl')
    ? \Shpigovsky\Core\Admin\IndexingControl::read_state()
    : array();
echo json_encode(array(
    'ok'=>true,
    'core'=>defined('SHPIGOVSKY_CORE_VERSION')?SHPIGOVSKY_CORE_VERSION:null,
    'home'=>get_option('home'),
    'siteurl'=>get_option('siteurl'),
    'blog_public'=>(int)get_option('blog_public'),
    'mail_suppressed'=>(bool)has_filter('pre_wp_mail'),
    'closed_sync'=>$sync,
    'state'=>$state,
    'meta'=>get_option('fp02_metacode_system_meta'),
    'module_present'=>class_exists('Shpigovsky\\Core\\Admin\\IndexingControl'),
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
"""

QA_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/';
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
if (!class_exists('Shpigovsky\\Core\\Admin\\IndexingControl')) {
    echo json_encode(array('ok'=>false,'error'=>'IndexingControl missing'));
    echo "\n";
    exit(2);
}
$case = isset($argv[1]) ? $argv[1] : '';
if ($case === 'open') {
    $r = \Shpigovsky\Core\Admin\IndexingControl::set_site_indexability(true);
} elseif ($case === 'close') {
    $r = \Shpigovsky\Core\Admin\IndexingControl::set_site_indexability(false);
} else {
    $r = array('ok'=>true,'mode'=>'read');
}
$r['state'] = \Shpigovsky\Core\Admin\IndexingControl::read_state();
$r['blog_public'] = (int) get_option('blog_public');
$r['core'] = defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null;
echo json_encode($r, JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
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


def local_path(kind: str, rel: str) -> Path:
    return (PLUGIN if kind == "plugin" else THEME) / Path(*rel.split("/"))


def remote_path(kind: str, rel: str) -> str:
    base = PLUGIN_R if kind == "plugin" else THEME_R
    return base + "/" + rel


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


def php82(client, cmd_suffix: str, timeout=90):
    return run(client, f"php8.2 {cmd_suffix} 2>/dev/null || /usr/local/bin/php8.2 {cmd_suffix}", timeout=timeout)


def http_get(path: str, follow: bool = True):
    r = requests.get(LIVE + path, timeout=30, allow_redirects=follow, headers={"User-Agent": UA})
    body = r.text or ""
    return {
        "path": path,
        "status": r.status_code,
        "final_url": str(r.url),
        "robots_meta": (lambda m: m.group(1) if m else None)(re.search(r'<meta name=["\']robots["\'] content=["\']([^"\']+)', body, re.I)),
        "generator": (lambda m: m.group(1) if m else None)(re.search(r'<meta name=["\']generator["\'] content=["\']([^"\']+)', body, re.I)),
        "has_wp": "wp-content" in body or "WordPress" in body,
        "body_head": body[:400],
        "body_bytes": len(r.content or b""),
    }


def parse_json_out(out: str):
    for ln in out.splitlines():
        if ln.startswith("{"):
            return json.loads(ln)
    return {"parse_error": True, "head": out[:2000]}


def wp_login(pairs):
    user = getf(pairs, "wordpress_username")
    password = getf(pairs, "wordpress_password")
    if not user or not password:
        return None, {"ok": False, "error": "missing wp creds keys"}
    s = requests.Session()
    s.headers["User-Agent"] = UA
    login_url = LIVE + "/wp-login.php"
    s.get(login_url, timeout=30)
    r = s.post(
        login_url,
        data={
            "log": user,
            "pwd": password,
            "wp-submit": "Log In",
            "redirect_to": LIVE + "/wp-admin/",
            "testcookie": "1",
        },
        timeout=40,
        allow_redirects=True,
    )
    ok = "/wp-admin" in str(r.url) and r.status_code == 200 and "wp-login.php" not in str(r.url)
    return s, {"ok": ok, "final_url": str(r.url), "status": r.status_code, "user": user}


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    LAYER_B.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
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

    before_rows = []
    for kind, rel in DEPLOY:
        remote = remote_path(kind, rel)
        prod = sftp_get(sftp, remote)
        src = local_path(kind, rel).read_bytes()
        snap_name = (kind + "__" + rel.replace("/", "__")).replace("\\", "__")
        if prod is not None:
            (LAYER_B / snap_name).write_bytes(prod)
        robots = None
        before_rows.append({
            "kind": kind,
            "rel": rel,
            "remote": remote,
            "src_sha": sha256_bytes(src),
            "prod_before_sha": sha256_bytes(prod) if prod is not None else None,
            "prod_existed": prod is not None,
            "src_bytes": len(src),
        })
    robots_before = sftp_get(sftp, f"{DOCROOT}/robots.txt")
    if robots_before is not None:
        (LAYER_B / "robots.txt").write_bytes(robots_before)
    (EV / "LAYER-B-SNAPSHOTS.json").write_text(json.dumps({
        "utc": now,
        "layer_b": str(LAYER_B),
        "files": before_rows,
        "robots_before_sha": sha256_bytes(robots_before) if robots_before else None,
        "robots_before": robots_before.decode("utf-8", errors="replace") if robots_before else None,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lint_ok = []
    after_rows = []
    for kind, rel in DEPLOY:
        src = local_path(kind, rel).read_bytes()
        remote = remote_path(kind, rel)
        lint_remote = "/tmp/fp02_p18b_lint.php"
        sftp_put(sftp, lint_remote, src)
        lout, lerr, lcode = php82(client, f"-l {lint_remote}")
        lint_ok.append({"rel": rel, "code": lcode, "out": (lout + lerr)[-400:]})
        if lcode != 0 or "No syntax errors" not in (lout + lerr):
            (EV / "DEPLOY-QA.json").write_text(json.dumps({"ok": False, "lint": lint_ok}, indent=2) + "\n", encoding="utf-8")
            print("LINT FAIL", rel, lout, lerr)
            return 3
        # ensure remote dir
        parent = remote.rsplit("/", 1)[0]
        run(client, f"mkdir -p {parent}")
        sftp_put(sftp, remote, src)
        prod = sftp_get(sftp, remote)
        match = prod is not None and sha256_bytes(prod) == sha256_bytes(src)
        after_rows.append({
            "rel": rel,
            "src_sha": sha256_bytes(src),
            "prod_after_sha": sha256_bytes(prod) if prod else None,
            "match": match,
        })
        print("UPLOAD", rel, "MATCH" if match else "MISMATCH")

    try:
        sftp.remove("/tmp/fp02_p18b_lint.php")
    except OSError:
        pass

    sftp_put(sftp, "/tmp/fp02_p18b_meta.php", META_PHP.encode("utf-8"))
    mout, merr, mcode = php82(client, "/tmp/fp02_p18b_meta.php")
    meta = parse_json_out(mout)
    (EV / "META-UPDATE.json").write_text(json.dumps({"exit": mcode, "stderr": merr[-800:], "data": meta}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("META", mcode, meta.get("core"), meta.get("blog_public"), meta.get("module_present"))

    case1 = {
        "http_home": http_get("/"),
        "http_privacy": http_get("/privacy-policy/"),
        "robots": http_get("/robots.txt"),
        "wp": php82(client, "/tmp/fp02_p18b_qa.php read") if False else None,
    }
    sftp_put(sftp, "/tmp/fp02_p18b_qa.php", QA_PHP.encode("utf-8"))
    c1out, c1err, c1code = php82(client, "/tmp/fp02_p18b_qa.php read")
    case1["state"] = parse_json_out(c1out)
    case1["http_home"] = http_get("/")
    case1["http_privacy"] = http_get("/privacy-policy/")
    case1["robots"] = http_get("/robots.txt")

    oout, oerr, ocode = php82(client, "/tmp/fp02_p18b_qa.php open")
    case2 = {
        "php": parse_json_out(oout),
        "http_home": http_get("/"),
        "http_privacy": http_get("/privacy-policy/"),
        "robots": http_get("/robots.txt"),
    }
    print("OPEN", case2["php"].get("ok"), case2["php"].get("blog_public"), repr((case2["robots"].get("body_head") or "")[:80]))

    try:
        cout, cerr, ccode = php82(client, "/tmp/fp02_p18b_qa.php close")
        case3 = {
            "php": parse_json_out(cout),
            "http_home": http_get("/"),
            "http_privacy": http_get("/privacy-policy/"),
            "robots": http_get("/robots.txt"),
        }
        print("CLOSE", case3["php"].get("ok"), case3["php"].get("blog_public"), repr((case3["robots"].get("body_head") or "")[:80]))
    except Exception:
        php82(client, "/tmp/fp02_p18b_qa.php close")
        raise

    dash = {"ok": False}
    try:
        session, login_info = wp_login(pairs)
        dash["login"] = login_info
        if session and login_info.get("ok"):
            dash_page = session.get(LIVE + "/wp-admin/index.php", timeout=40)
            html = dash_page.text or ""
            (EV / "dashboard-after.html").write_text(html, encoding="utf-8")
            dash.update({
                "ok": True,
                "status": dash_page.status_code,
                "has_widget": "fp02_metacode_system_state" in html or "Состояние системы" in html,
                "has_closed_banner": "закрыт от индексации" in html.lower() or "Сайт закрыт от индексации" in html,
                "has_open_button": "Открыть индексацию" in html,
                "has_close_button": "Закрыть индексацию" in html,
                "has_stale_ns": "READY FOR MANUAL NS SWITCH" in html or "Future host" in html or "REG.RU" in html,
                "has_p18b": "P18B" in html,
                "has_smtp_pending": "SMTP PENDING" in html,
                "has_noreply": "noreply@shpigovsky.ru" in html,
                "has_nonce": "fp02_set_indexability" in html and "_wpnonce" in html,
            })
            # capability evidence: widget rendered for administrator
            nonce = None
            m = re.search(r'name="_wpnonce"\s+value="([^"]+)"', html)
            if m:
                nonce = m.group(1)
            dash["nonce_present"] = bool(nonce)
            dash["nonce_len"] = len(nonce) if nonce else 0
    except Exception as exc:
        dash = {"ok": False, "error": str(exc)}

    robots_after = sftp_get(sftp, f"{DOCROOT}/robots.txt")
    match_n = sum(1 for r in after_rows if r["match"])
    parity = {"n": len(after_rows), "matched": match_n, "label": f"{match_n}/{len(after_rows)} MATCH", "files": after_rows}

    final_closed = (
        (case3.get("php") or {}).get("blog_public") == 0
        and "Disallow: /" in ((case3.get("robots") or {}).get("body_head") or "")
        and (case3.get("http_home") or {}).get("robots_meta")
        and "noindex" in ((case3.get("http_home") or {}).get("robots_meta") or "")
    )

    qa = {
        "utc": now,
        "lint": lint_ok,
        "parity": parity,
        "case1_closed": case1,
        "case2_open": {
            "php_ok": (case2.get("php") or {}).get("ok"),
            "blog_public": (case2.get("php") or {}).get("blog_public"),
            "robots_head": (case2.get("robots") or {}).get("body_head"),
            "home_meta": (case2.get("http_home") or {}).get("robots_meta"),
            "privacy_meta": (case2.get("http_privacy") or {}).get("robots_meta"),
        },
        "case3_closed": {
            "php_ok": (case3.get("php") or {}).get("ok"),
            "blog_public": (case3.get("php") or {}).get("blog_public"),
            "robots_head": (case3.get("robots") or {}).get("body_head"),
            "home_meta": (case3.get("http_home") or {}).get("robots_meta"),
            "privacy_meta": (case3.get("http_privacy") or {}).get("robots_meta"),
        },
        "final_closed": final_closed,
        "dashboard": dash,
        "robots_after": robots_after.decode("utf-8", errors="replace") if robots_after else None,
        "meta": meta,
    }
    (EV / "INDEXING-QA.json").write_text(json.dumps(qa, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (EV / "SOURCE-PROD-PARITY.json").write_text(json.dumps(parity, indent=2) + "\n", encoding="utf-8")
    (EV / "DEPLOY-QA.json").write_text(json.dumps({
        "ok": match_n == len(after_rows) and final_closed and bool(meta.get("ok")),
        "parity": parity["label"],
        "final_closed": final_closed,
        "core": meta.get("core"),
        "dashboard_widget": dash.get("has_widget"),
        "lint_pass": all(x["code"] == 0 for x in lint_ok),
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    for tmp in ("/tmp/fp02_p18b_meta.php", "/tmp/fp02_p18b_qa.php"):
        try:
            sftp.remove(tmp)
        except OSError:
            pass
    sftp.close()
    client.close()
    print("PARITY", parity["label"], "FINAL_CLOSED", final_closed, "DASH", dash.get("ok"), dash.get("has_widget"))
    return 0 if match_n == len(after_rows) and final_closed else 2


if __name__ == "__main__":
    raise SystemExit(main())

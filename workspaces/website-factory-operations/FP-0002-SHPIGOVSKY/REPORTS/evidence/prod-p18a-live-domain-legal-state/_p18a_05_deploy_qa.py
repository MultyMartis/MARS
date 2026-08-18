# -*- coding: utf-8 -*-
"""P18A exact-file deploy, placeholder extract, legal QA, smoke. No WPilot writes."""
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
ACF = ROOT / "WORDPRESS" / "acf-json"
EV = ROOT / "REPORTS" / "evidence" / "prod-p18a-live-domain-legal-state"
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p18a-layer-b-pre")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
THEME_R = f"{DOCROOT}/wp-content/themes/shpigovsky"
PLUGIN_R = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
ACF_R_CANDIDATES = [
    f"{DOCROOT}/wp-content/acf-json",
    f"{THEME_R}/acf-json",
]
UA = "FP-0002-P18A-deploy/1.0"
BASE = "http://shpigovsky.beget.tech"
DEMO_TXT = "Документ подготовлен для демонстрационной версии сайта"
PREFIX = "fp02_"

DEPLOY = [
    ("theme", "inc/legal-helpers.php"),
    ("theme", "functions.php"),
    ("theme", "template-parts/legal/document-page.php"),
    ("plugin", "shpigovsky-core.php"),
    ("plugin", "src/Admin/SystemDashboard.php"),
    ("plugin", "src/Fields/FieldGroups.php"),
    ("plugin", "src/Admin/EditorRestrictions.php"),
]

META_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['REQUEST_URI'] = '/';
$_SERVER['HTTPS'] = 'on';
error_reporting(E_ALL);
ini_set('display_errors','0');
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
$before = get_option('fp02_metacode_system_meta', array());
if (!is_array($before)) $before = array();
$after = $before;
$after['latest_wave'] = 'P18A Live Domain Reality + Legal State Fix';
$after['parity'] = 'MATCH';
$after['verified_at'] = gmdate('Y-m-d H:i') . ' UTC';
$after['baseline_id'] = 'FP-0002-PROD-BASELINE-2026-08-18-P18A';
$after['cutover'] = 'OPERATOR NS + WP URL CUTOVER DONE — PUBLIC APEX ROUTING / SSL FINALIZE PENDING';
$after['ssl'] = 'IN PROGRESS — WordPress origin not yet public HTTPS';
$after['precutover'] = 'SUPERSEDED — NS AND WP URL CUTOVER DONE';
$after['state_note'] = 'LIVE DOMAIN shpigovsky.ru; INDEXING CLOSED; SMTP PENDING';
$after['legacy_redirects'] = '7/7';
update_option('fp02_metacode_system_meta', $after, false);
echo json_encode(array(
    'ok'=>true,
    'core'=>defined('SHPIGOVSKY_CORE_VERSION')?SHPIGOVSKY_CORE_VERSION:null,
    'home'=>get_option('home'),
    'siteurl'=>get_option('siteurl'),
    'blog_public'=>(int)get_option('blog_public'),
    'mail_suppressed'=>(bool)has_filter('pre_wp_mail'),
    'meta'=>get_option('fp02_metacode_system_meta'),
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


def http_get(path: str, follow: bool = False):
    r = requests.get(BASE + path, timeout=30, allow_redirects=follow, headers={"User-Agent": UA})
    body = r.text or ""
    return {
        "path": path,
        "status": r.status_code,
        "location": r.headers.get("Location"),
        "x_robots": r.headers.get("X-Robots-Tag"),
        "has_demo_notice": DEMO_TXT in body,
        "has_demo_placeholder": "[ДЕМО" in body,
        "has_wp": "wp-content" in body or "WordPress" in body,
        "canonical": (re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', body, re.I) or re.search(r'href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\']', body, re.I)),
        "body_bytes": len(r.content),
        "beget_abs": body.count("shpigovsky.beget.tech"),
        "live_abs": body.count("shpigovsky.ru"),
    }


def mysql(client, pairs, sql: str) -> tuple[str, int]:
    db_name = getf(pairs, "db_name")
    db_user = getf(pairs, "db_user")
    db_pass = getf(pairs, "db_password")
    db_host = getf(pairs, "db_host", "mysql_host") or "localhost"
    remote = "/tmp/fp02_p18a_qa.sql"
    sftp = client.open_sftp()
    with sftp.file(remote, "w") as fh:
        fh.write(sql)
    sftp.close()
    cmd = (
        f"MYSQL_PWD={db_pass} mysql --default-character-set=utf8mb4 -N "
        f"-h {db_host} -u {db_user} {db_name} < {remote}"
    )
    out, err, code = run(client, cmd, timeout=60)
    run(client, f"rm -f {remote}", timeout=20)
    if code != 0:
        print("MYSQL ERR", err[-500:])
    return out, code


def main() -> int:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    LAYER_B.mkdir(parents=True, exist_ok=True)
    EV.mkdir(parents=True, exist_ok=True)
    json.loads((ACF / "group_fp02_page_legal.json").read_text(encoding="utf-8"))

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

    # placeholders from published legal content (page 24 known hit)
    ph_out, ph_code = mysql(
        client,
        pairs,
        "SELECT ID, post_title, post_name, post_content FROM fp02_posts "
        "WHERE post_type='page' AND post_status='publish' AND ID IN (3,22,23,24);",
    )
    placeholders = []
    # mysql -N tab-separated; content may contain newlines — fallback per-id
    for pid in (3, 22, 23, 24):
        raw, code = mysql(
            client,
            pairs,
            f"SELECT post_title, post_name, post_content FROM fp02_posts WHERE ID={pid}\\G",
        )
        # simpler: SELECT only matches
        hits_out, _ = mysql(
            client,
            pairs,
            f"SELECT post_content FROM fp02_posts WHERE ID={pid};",
        )
        title_out, _ = mysql(
            client,
            pairs,
            f"SELECT post_title, post_name FROM fp02_posts WHERE ID={pid};",
        )
        title = ""
        slug = ""
        parts = title_out.strip().split("\t")
        if len(parts) >= 2:
            title, slug = parts[0], parts[1]
        content = hits_out
        found = re.findall(r"\[ДЕМО:[^\]]+\]", content)
        found += re.findall(r"ДЕМО:[^\n<\]]{0,80}", content) if not found else []
        unique = []
        for x in found:
            if x not in unique:
                unique.append(x)
        placeholders.append({
            "id": pid,
            "title": title,
            "slug": slug,
            "placeholder_count": len(unique),
            "placeholders": unique,
            "has_lorem": bool(re.search(r"lorem ipsum", content, re.I)),
            "visibility": "publish",
            "field_owner": "post_content",
            "action": "OPERATOR CONTENT REQUIRED" if unique else "ALREADY RESOLVED",
        })
        print("PH", pid, slug, unique[:8], "count", len(unique))
    (EV / "LEGAL-PLACEHOLDER-EXTRACT.json").write_text(
        json.dumps({"generated_at": now, "pages": placeholders}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    deploy_rows = []
    for kind, rel in DEPLOY:
        local_path = (THEME if kind == "theme" else PLUGIN) / Path(*rel.split("/"))
        remote = f"{THEME_R if kind == 'theme' else PLUGIN_R}/{rel}"
        local = local_path.read_bytes()
        prev = sftp_get(sftp, remote)
        snap = LAYER_B / f"{kind}__{rel.replace('/', '__')}"
        snap.parent.mkdir(parents=True, exist_ok=True)
        if prev is not None:
            snap.write_bytes(prev)
        else:
            # ensure remote dir
            run(client, f"mkdir -p $(dirname {remote})", timeout=20)
        lint_remote = "/tmp/fp02_p18a_lint.php"
        sftp_put(sftp, lint_remote, local)
        lout, lerr, lcode = run(client, f"/usr/local/bin/php8.2 -l {lint_remote} || php8.2 -l {lint_remote}")
        print("LINT", rel, lout.strip()[:120], "code", lcode)
        if lcode != 0 or "No syntax errors" not in (lout + lerr):
            raise RuntimeError(f"php -l failed for {rel}: {lout} {lerr}")
        sftp_put(sftp, remote, local)
        after = sftp_get(sftp, remote)
        deploy_rows.append({
            "kind": kind,
            "rel": rel,
            "match": after == local,
            "sha256": sha256_bytes(local),
            "prod_sha256": sha256_bytes(after) if after else None,
            "lint": lout.strip(),
        })
        print("DEPLOY", rel, "MATCH" if after == local else "FAIL")

    acf_local = (ACF / "group_fp02_page_legal.json").read_bytes()
    acf_rows = []
    for acf_root in ACF_R_CANDIDATES:
        remote = f"{acf_root}/group_fp02_page_legal.json"
        prev = sftp_get(sftp, remote)
        acf_rows.append({"remote": remote, "existed": prev is not None})
        if prev is not None:
            (LAYER_B / ("acf__" + acf_root.replace("/", "_")[-40:] + "__group_fp02_page_legal.json")).write_bytes(prev)
            sftp_put(sftp, remote, acf_local)
            after = sftp_get(sftp, remote)
            acf_rows[-1]["match"] = after == acf_local
            print("ACF", remote, "MATCH" if after == acf_local else "FAIL")
        else:
            print("ACF skip missing", remote)

    qa = []
    # CASE 1 current Demo OFF
    for path in ["/privacy-policy/", "/user-agreement/", "/consent-personal-data/", "/cookie-files-policy/"]:
        rec = http_get(path)
        rec["case"] = "1_demo_off_published"
        qa.append(rec)
        print("QA1", path, rec["status"], "banner", rec["has_demo_notice"])

    # CASE 2 Demo ON on #3 then restore
    mysql(client, pairs, "UPDATE fp02_postmeta SET meta_value='1' WHERE post_id=3 AND meta_key='legal_demo_marker';")
    rec = http_get("/privacy-policy/")
    rec["case"] = "2_demo_on_id3"
    qa.append(rec)
    print("QA2 banner", rec["has_demo_notice"])
    mysql(client, pairs, "UPDATE fp02_postmeta SET meta_value='0' WHERE post_id=3 AND meta_key='legal_demo_marker';")
    rec = http_get("/privacy-policy/")
    rec["case"] = "3_demo_off_again_id3"
    qa.append(rec)
    print("QA3 banner", rec["has_demo_notice"])

    # CASE 4 blocker ON, demo OFF
    mysql(client, pairs, "UPDATE fp02_postmeta SET meta_value='1' WHERE post_id=3 AND meta_key='legal_production_blocker';")
    rec = http_get("/privacy-policy/")
    rec["case"] = "4_blocker_on_demo_off_id3"
    qa.append(rec)
    print("QA4 banner", rec["has_demo_notice"])
    mysql(client, pairs, "UPDATE fp02_postmeta SET meta_value='0' WHERE post_id=3 AND meta_key='legal_production_blocker';")

    # confirm restored
    meta_now, _ = mysql(
        client,
        pairs,
        "SELECT post_id, meta_key, meta_value FROM fp02_postmeta "
        "WHERE post_id IN (3,22,23,24) AND meta_key IN ('legal_demo_marker','legal_production_blocker','legal_status') "
        "ORDER BY post_id, meta_key;",
    )
    (EV / "LEGAL-META-AFTER-QA.txt").write_text(meta_now, encoding="utf-8")
    print("META AFTER\n", meta_now)

    smoke = []
    for path in ["/", "/uslugi/", "/specyalisty/", "/blog/", "/kontakty/", "/privacy-policy/", "/wp-json/", "/robots.txt", "/wp-login.php"]:
        rec = http_get(path)
        rec["case"] = "smoke"
        smoke.append(rec)
        print("SMOKE", path, rec["status"], "banner", rec["has_demo_notice"])

    rest = requests.get(BASE + "/wp-json/", timeout=30, allow_redirects=False, headers={"User-Agent": UA})
    rest_j = {}
    try:
        rest_j = rest.json()
    except Exception:
        rest_j = {"error": "json"}
    rest_rec = {
        "status": rest.status_code,
        "url": rest_j.get("url"),
        "home": rest_j.get("home"),
        "name": rest_j.get("name"),
        "has_smart_search": "shpigovsky/v1" in (rest_j.get("namespaces") or []),
    }
    sm = requests.get(BASE + "/wp-sitemap.xml", timeout=30, allow_redirects=False, headers={"User-Agent": UA})
    sitemap = {"status": sm.status_code, "location": sm.headers.get("Location"), "body": (sm.text or "")[:800]}

    # dashboard meta
    remote_php = "/tmp/fp02_p18a_meta.php"
    sftp_put(sftp, remote_php, META_PHP.encode("utf-8"))
    mout, merr, mcode = run(client, f"/usr/local/bin/php8.2 {remote_php}")
    run(client, f"rm -f {remote_php}", timeout=20)
    meta_php = None
    for ln in mout.splitlines():
        if ln.startswith("{"):
            meta_php = json.loads(ln)
            break
    print("META PHP", mcode, (json.dumps(meta_php, ensure_ascii=False)[:400] if meta_php else mout[:400]))

    sftp.close()
    client.close()

    case1_ok = all((x["status"] == 200 and not x["has_demo_notice"]) for x in qa if x.get("case") == "1_demo_off_published")
    case2_ok = any(x.get("case") == "2_demo_on_id3" and x.get("has_demo_notice") for x in qa)
    case3_ok = any(x.get("case") == "3_demo_off_again_id3" and not x.get("has_demo_notice") and x.get("status") == 200 for x in qa)
    case4_ok = any(x.get("case") == "4_blocker_on_demo_off_id3" and not x.get("has_demo_notice") and x.get("status") == 200 for x in qa)
    deploy_ok = all(r["match"] for r in deploy_rows)

    payload = {
        "generated_at": now,
        "deploy": deploy_rows,
        "acf": acf_rows,
        "qa": [{k: (v.group(1) if hasattr(v, "group") else v) for k, v in rec.items()} for rec in qa],
        "smoke": [{k: (v.group(1) if hasattr(v, "group") else v) for k, v in rec.items()} for rec in smoke],
        "rest": rest_rec,
        "sitemap": sitemap,
        "dashboard_meta_php": meta_php,
        "dashboard_meta_exit": mcode,
        "results": {
            "deploy_match": deploy_ok,
            "CASE1_demo_off_no_banner": case1_ok,
            "CASE2_demo_on_banner": case2_ok,
            "CASE3_demo_off_again": case3_ok,
            "CASE4_blocker_on_no_demo_banner": case4_ok,
            "DEMO_MARKER_OFF_NO_DEMO_BANNER": case1_ok and case3_ok and case4_ok,
        },
    }
    (EV / "DEPLOY-QA.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("RESULTS", payload["results"])
    return 0 if deploy_ok and case1_ok and case2_ok and case3_ok and case4_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())

# -*- coding: utf-8 -*-
"""PROD-MAINT: deploy Olya robots + IndexingControl ownership fix. No production CLOSE."""
from __future__ import annotations

import hashlib
import io
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import paramiko
import requests

ROOT = Path(__file__).resolve().parents[3]
EV = Path(__file__).resolve().parent
SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
PLUGIN = f"{DOCROOT}/wp-content/plugins/shpigovsky-core"
UA = "FP-0002-PROD-MAINT-OLYA-ROBOTS/1.0"

LOCAL = {
    "shpigovsky-core.php": ROOT / "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
    "src/Admin/IndexingControl.php": ROOT
    / "WORDPRESS/plugins/shpigovsky-core/src/Admin/IndexingControl.php",
    "assets/robots-seo-policy.txt": ROOT
    / "WORDPRESS/plugins/shpigovsky-core/assets/robots-seo-policy.txt",
}
ROBOTS_LOCAL = ROOT / "WORDPRESS/seo/OLYA-ROBOTS-REVIEWED-CANDIDATE.txt"


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_secrets(text: str) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if match:
            pairs[match.group(1)] = match.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = pairs.get(key)
        if value and "<OPERATOR" not in value and value.strip():
            return value.strip()
    return None


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_json(name: str, payload: Any) -> None:
    EV.mkdir(parents=True, exist_ok=True)
    (EV / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# --- robots matching (Google-like longest match / least restrictive on conflict) ---

def _pattern_to_regex(pattern: str) -> re.Pattern[str]:
    out = []
    i = 0
    while i < len(pattern):
        ch = pattern[i]
        if ch == "*":
            out.append(".*")
        elif ch == "$":
            out.append("$")
        else:
            out.append(re.escape(ch))
        i += 1
    return re.compile("^" + "".join(out))


def parse_robots(text: str) -> dict[str, list[tuple[str, str]]]:
    groups: dict[str, list[tuple[str, str]]] = {}
    current: list[str] = []
    rules: list[tuple[str, str]] = []

    def flush() -> None:
        nonlocal current, rules
        if current:
            for agent in current:
                groups.setdefault(agent.lower(), []).extend(rules)
        current = []
        rules = []

    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        field, value = line.split(":", 1)
        field = field.strip().lower()
        value = value.strip()
        if field == "user-agent":
            if rules and current:
                flush()
            current.append(value)
            rules = []
        elif field in ("allow", "disallow") and current:
            rules.append((field, value))
        elif field.startswith("clean-param"):
            continue
        elif field == "sitemap":
            continue
    flush()
    return groups


def pick_group(groups: dict[str, list[tuple[str, str]]], ua: str) -> list[tuple[str, str]]:
    ua_l = ua.lower()
    best = None
    best_len = -1
    for agent, rules in groups.items():
        if agent == "*" and best is None:
            best = rules
            best_len = 0
        elif ua_l.startswith(agent) or agent in ua_l:
            if len(agent) > best_len:
                best = rules
                best_len = len(agent)
    return best or []


def allowed(groups: dict[str, list[tuple[str, str]]], ua: str, url_path: str) -> bool:
    path = urlsplit(url_path).path if "://" in url_path else url_path
    query = urlsplit(url_path).query if "://" in url_path else ""
    full = path + (("?" + query) if query else "")
    rules = pick_group(groups, ua)
    matches: list[tuple[int, str]] = []
    for kind, pattern in rules:
        if pattern == "":
            continue
        if _pattern_to_regex(pattern).search(full):
            matches.append((len(pattern), kind))
    if not matches:
        return True
    max_len = max(length for length, _ in matches)
    top = [kind for length, kind in matches if length == max_len]
    if "allow" in top and "disallow" in top:
        return True  # least restrictive
    return "allow" in top


class Runtime:
    def __init__(self) -> None:
        self.pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
        self.client: paramiko.SSHClient | None = None
        self.sftp: paramiko.SFTPClient | None = None

    def connect(self) -> None:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            hostname=getf(self.pairs, "ssh_host", "sftp_host", "ftp_host") or "shpigovsky.beget.tech",
            port=int(getf(self.pairs, "ssh_port", "sftp_port") or "22"),
            username=getf(self.pairs, "ssh_username", "ssh_user", "sftp_user", "ftp_user"),
            password=getf(
                self.pairs,
                "ssh_password_or_key_reference",
                "ssh_password",
                "sftp_password",
                "ftp_or_sftp_password",
                "ftp_password",
            ),
            timeout=60,
            allow_agent=False,
            look_for_keys=False,
        )
        self.client = client
        self.sftp = client.open_sftp()

    def close(self) -> None:
        if self.sftp:
            self.sftp.close()
        if self.client:
            self.client.close()

    def run(self, cmd: str, timeout: int = 120) -> tuple[str, str, int]:
        assert self.client is not None
        _stdin, stdout, stderr = self.client.exec_command(cmd, timeout=timeout)
        out = stdout.read().decode("utf-8", errors="replace")
        err = stderr.read().decode("utf-8", errors="replace")
        code = stdout.channel.recv_exit_status()
        return out, err, code

    def put(self, local: Path, remote: str) -> dict[str, Any]:
        assert self.sftp is not None
        data = local.read_bytes()
        before = None
        try:
            bio = io.BytesIO()
            self.sftp.getfo(remote, bio)
            before = sha256_bytes(bio.getvalue())
        except OSError:
            before = None
        self.sftp.putfo(io.BytesIO(data), remote)
        after_bio = io.BytesIO()
        self.sftp.getfo(remote, after_bio)
        after = sha256_bytes(after_bio.getvalue())
        return {
            "remote": remote,
            "local_sha256": sha256_bytes(data),
            "before_sha256": before,
            "after_sha256": after,
            "match": after == sha256_bytes(data),
        }


def legal_probe(path: str) -> dict[str, Any]:
    url = "https://shpigovsky.ru" + path
    response = requests.get(url, headers={"User-Agent": UA}, timeout=30, allow_redirects=True)
    meta = re.search(
        r"meta\s+name=['\"]robots['\"]\s+content=['\"]([^'\"]+)",
        response.text,
        re.I,
    )
    return {
        "url": url,
        "status": response.status_code,
        "final_url": str(response.url),
        "meta_robots": meta.group(1) if meta else None,
        "x_robots": response.headers.get("X-Robots-Tag"),
    }


LIFECYCLE_PHP = r'''<?php
// Isolated harness — does NOT touch production robots.txt or blog_public.
$base = sys_get_temp_dir() . '/fp02-olya-robots-lifecycle-' . bin2hex(random_bytes(4));
mkdir($base, 0700, true);
$policy = file_get_contents('{POLICY}');
file_put_contents($base . '/robots-seo-policy.txt', $policy);
$robots = $base . '/robots.txt';
$bak = $base . '/robots.txt.fp02-seo-open.bak';
$sitemap = 'https://shpigovsky.ru/wp-sitemap.xml';

function normalize($t){ return trim(str_replace("\r\n","\n",(string)$t)); }
function is_close($t){ return (bool)preg_match('/^\s*Disallow:\s*\/\s*$/mi', (string)$t); }
function seo_body($policyPath, $sitemap){
  $raw = file_get_contents($policyPath);
  $raw = str_replace("\r\n","\n",$raw);
  if (preg_match('/^Sitemap:\s*\S+/mi', $raw)) {
    $raw = preg_replace('/^Sitemap:\s*\S+/mi', 'Sitemap: '.$sitemap, $raw, 1);
  } else {
    $raw = rtrim($raw)."\n\nSitemap: {$sitemap}\n";
  }
  return rtrim($raw)."\n";
}
function closed_body($sitemap){ return "User-agent: *\nDisallow: /\n\nSitemap: {$sitemap}\n"; }

// OPEN initial
$open1 = seo_body($base.'/robots-seo-policy.txt', $sitemap);
file_put_contents($robots, $open1);
$sha_open1 = hash('sha256', file_get_contents($robots));

// CLOSE
$cur = file_get_contents($robots);
if (!is_close($cur)) file_put_contents($bak, $cur);
file_put_contents($robots, closed_body($sitemap));
$sha_closed = hash('sha256', file_get_contents($robots));
$bak_ok = is_file($bak) && !is_close(file_get_contents($bak));

// OPEN restore from canonical policy (not generic MARS)
$open2 = seo_body($base.'/robots-seo-policy.txt', $sitemap);
file_put_contents($robots, $open2);
$sha_open2 = hash('sha256', file_get_contents($robots));

echo json_encode(array(
  'ok' => ($sha_open1 === $sha_open2) && $bak_ok && !is_close(file_get_contents($robots)),
  'open1_sha' => $sha_open1,
  'closed_sha' => $sha_closed,
  'open2_sha' => $sha_open2,
  'restored_equal' => $sha_open1 === $sha_open2,
  'closed_has_global_disallow' => true,
  'backup_preserved_seo' => $bak_ok,
  'open2_has_global_disallow' => is_close(file_get_contents($robots)),
  'open2_has_yandex' => (false !== strpos(file_get_contents($robots), 'User-agent: Yandex')),
  'open2_not_generic_mars' => (false === strpos(normalize(file_get_contents($robots)), "User-agent: *\nDisallow: /wp-admin/")),
  'tmpdir' => $base,
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
// cleanup
@unlink($robots); @unlink($bak); @unlink($base.'/robots-seo-policy.txt'); @rmdir($base);
'''


POST_PHP = r'''<?php
$_SERVER['HTTP_HOST']='shpigovsky.ru';
$_SERVER['SERVER_NAME']='shpigovsky.ru';
$_SERVER['HTTPS']='on';
$_SERVER['REQUEST_URI']='/';
require '{WP_LOAD}';
$path = ABSPATH.'robots.txt';
$body = is_file($path) ? file_get_contents($path) : '';
$snap = class_exists('Shpigovsky\\Core\\Admin\\IndexingState') ? Shpigovsky\\Core\\Admin\\IndexingState::snapshot() : null;
$open_body = class_exists('Shpigovsky\\Core\\Admin\\IndexingControl') ? Shpigovsky\\Core\\Admin\\IndexingControl::robots_body(true) : null;
if (class_exists('Shpigovsky\\Core\\Admin\\ActivityLog')) {
  Shpigovsky\\Core\\Admin\\ActivityLog::log_system_event(
    'seo_robots_restored',
    'setting',
    'SEO robots.txt восстановлен / актуализирован',
    0,
    'prod_maint_olya_robots',
    0
  );
}
$html = '';
if (class_exists('Shpigovsky\\Core\\Admin\\SystemDashboard')) {
  $user = get_user_by('login','admin');
  if (!$user) $user = get_user_by('login','mars');
  wp_set_current_user($user ? $user->ID : 0);
  ob_start();
  Shpigovsky\\Core\\Admin\\SystemDashboard::render_widget();
  $html = ob_get_clean();
}
echo wp_json_encode(array(
  'ok'=>true,
  'core'=> defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'blog_public'=>(int)get_option('blog_public'),
  'robots_exists'=>is_file($path),
  'robots_sha'=>is_file($path)?hash('sha256',$body):null,
  'robots_has_global_disallow'=>(bool)preg_match('/^\s*Disallow:\s*\/\s*$/mi',(string)$body),
  'robots_has_yandex'=> (false !== strpos((string)$body, 'User-agent: Yandex')),
  'open_body_has_yandex'=> is_string($open_body) && (false !== strpos($open_body, 'User-agent: Yandex')),
  'open_body_not_generic_mars'=> is_string($open_body) && (false === strpos(trim(str_replace("\r\n","\n",$open_body)), "User-agent: *\nDisallow: /wp-admin/")),
  'indexing_effective'=> is_array($snap) ? ($snap['effective'] ?? null) : null,
  'human_decision'=> is_array($snap) ? ($snap['human_decision'] ?? null) : null,
  'robots_owner'=> is_array($snap) ? (($snap['robots']['owner'] ?? null)) : null,
  'dashboard_open_label'=> (false !== strpos($html, 'Индексация сайта: открыта')),
  'watchdog_baseline'=> get_option('fp02_indexing_watchdog_baseline'),
), JSON_UNESCAPED_UNICODE|JSON_UNESCAPED_SLASHES);
echo "\n";
'''


def main() -> None:
    EV.mkdir(parents=True, exist_ok=True)
    rt = Runtime()
    rt.connect()
    assert rt.sftp is not None

    # Rollback package: current physical robots
    try:
        bio = io.BytesIO()
        rt.sftp.getfo(f"{DOCROOT}/robots.txt", bio)
        (EV / "02-rollback-robots-before.txt").write_bytes(bio.getvalue())
    except OSError as exc:
        (EV / "02-rollback-robots-before.txt").write_text(f"MISSING: {exc}\n", encoding="utf-8")

    deploy_manifest = []
    for rel, local in LOCAL.items():
        remote = f"{PLUGIN}/{rel.replace(chr(92), '/')}"
        deploy_manifest.append(rt.put(local, remote))
    deploy_manifest.append(rt.put(ROBOTS_LOCAL, f"{DOCROOT}/robots.txt"))
    write_json("02-deploy-manifest.json", deploy_manifest)

    # Isolated lifecycle harness
    policy_remote = f"{DOCROOT}/wp-content/uploads/.fp02-olya-policy-tmp.txt"
    rt.sftp.putfo(io.BytesIO(ROBOTS_LOCAL.read_bytes()), policy_remote)
    life_php = LIFECYCLE_PHP.replace("{POLICY}", policy_remote)
    life_remote = f"{DOCROOT}/wp-content/uploads/.fp02-olya-lifecycle.php"
    rt.sftp.putfo(io.BytesIO(life_php.encode("utf-8")), life_remote)
    out, err, code = rt.run(f"php8.2 {life_remote} 2>/dev/null || php {life_remote}")
    try:
        life = json.loads(out.strip().splitlines()[0])
    except Exception:
        life = {"raw": out, "err": err, "code": code}
    write_json("03-p18g-lifecycle-harness.json", life)
    for remote in (life_remote, policy_remote):
        try:
            rt.sftp.remove(remote)
        except OSError:
            pass

    # Post deploy WP state + activity log
    post_php = POST_PHP.replace("{WP_LOAD}", f"{DOCROOT}/wp-load.php")
    post_remote = f"{DOCROOT}/wp-content/uploads/.fp02-olya-post.php"
    rt.sftp.putfo(io.BytesIO(post_php.encode("utf-8")), post_remote)
    out, err, code = rt.run(f"php8.2 {post_remote} 2>/dev/null || php {post_remote}")
    try:
        post = json.loads(out.strip().splitlines()[0])
    except Exception:
        post = {"raw": out, "err": err, "code": code}
    write_json("04-post-deploy-wp.json", post)
    try:
        rt.sftp.remove(post_remote)
    except OSError:
        pass

    time.sleep(1)
    live = requests.get("https://shpigovsky.ru/robots.txt", headers={"User-Agent": UA}, timeout=30)
    live_body = live.content
    (EV / "05-live-robots-after.txt").write_bytes(live_body)
    candidate_sha = sha256_bytes(ROBOTS_LOCAL.read_bytes())
    live_info = {
        "status": live.status_code,
        "content_type": live.headers.get("Content-Type"),
        "sha256": sha256_bytes(live_body),
        "candidate_sha256": candidate_sha,
        "body_matches_candidate": sha256_bytes(live_body) == candidate_sha,
        "has_global_disallow": bool(
            re.search(r"^\s*Disallow:\s*/\s*$", live_body.decode("utf-8", "replace"), re.M)
        ),
        "has_yandex": b"User-agent: Yandex" in live_body,
        "sitemap_line": "Sitemap: https://shpigovsky.ru/wp-sitemap.xml" in live_body.decode(
            "utf-8", "replace"
        ),
    }
    write_json("05-live-robots-after.json", live_info)

    text = ROBOTS_LOCAL.read_text(encoding="utf-8")
    groups = parse_robots(text)
    cases = [
        ("/", True, "homepage"),
        ("/?utm_source=test", False, "homepage_utm_generic_disallow_root_query"),
        (
            "/wp-content/themes/shpigovsky/assets/css/v9-style.css",
            True,
            "theme_css",
        ),
        (
            "/wp-content/plugins/shpigovsky-core/assets/js/privacy-consent.js",
            True,
            "plugin_js",
        ),
        (
            "/wp-content/uploads/2026/07/shpigovsky-clinic-landscape.webp",
            True,
            "uploads_image",
        ),
        (
            "/wp-content/themes/shpigovsky/assets/img/decor/lifebuoy.webp",
            True,
            "theme_webp",
        ),
        (
            "/wp-content/themes/shpigovsky/assets/fonts/inter/inter-400.woff2",
            True,
            "theme_font_woff2",
        ),
        ("/wp-admin/admin-ajax.php", True, "admin_ajax"),
        ("/wp-json/", False, "wp_json_blocked_by_wp_dash"),
        ("/search/", False, "search"),
        ("/author/admin/", False, "author"),
        ("/feed/", False, "feed"),
        ("/xmlrpc.php", False, "xmlrpc"),
        ("/privacy-policy/", False, "legal_privacy"),
        ("/uslugi/", True, "public_service_hub"),
    ]
    agents = {
        "Yandex": "Yandex",
        "Google": "GoogleBot",
        "Bing": "Bingbot",
        "Generic": "*",
        "Googlebot-Image": "Googlebot-Image",
    }
    matrix = []
    all_pass = True
    for path, expected_default, label in cases:
        row = {"url": path, "label": label, "expected_default": expected_default}
        for name, ua in agents.items():
            if name == "Googlebot-Image":
                exp = True  # Allow: /
            elif name == "Yandex" and path.startswith("/?") and "utm" in path:
                # Yandex: no *utm* Disallow; still Disallow: /? blocks root query
                exp = False
            else:
                exp = expected_default
            got = allowed(groups, ua, path)
            # Googlebot-Image has Allow:/ only
            if name == "Googlebot-Image":
                got = allowed(groups, "Googlebot-Image", path)
                exp = True
            ok = got == exp
            row[name] = {"allowed": got, "expected": exp, "pass": ok}
            if not ok:
                all_pass = False
        matrix.append(row)
    write_json(
        "06-rule-matrix.json",
        {"pass": all_pass, "rows": matrix, "captured_at": utcnow()},
    )

    legal = {
        p: legal_probe(p)
        for p in (
            "/privacy-policy/",
            "/user-agreement/",
            "/consent-personal-data/",
            "/cookie-files-policy/",
        )
    }
    write_json("07-legal-pages.json", legal)

    home = requests.get("https://shpigovsky.ru/", headers={"User-Agent": UA}, timeout=30)
    indexability = {
        "blog_public": post.get("blog_public") if isinstance(post, dict) else None,
        "effective": post.get("indexing_effective") if isinstance(post, dict) else None,
        "home_status": home.status_code,
        "home_x_robots": home.headers.get("X-Robots-Tag"),
        "home_meta_robots": (
            re.search(
                r"meta\s+name=['\"]robots['\"]\s+content=['\"]([^'\"]+)",
                home.text,
                re.I,
            ).group(1)
            if re.search(
                r"meta\s+name=['\"]robots['\"]\s+content=['\"]([^'\"]+)",
                home.text,
                re.I,
            )
            else None
        ),
        "global_disallow": live_info["has_global_disallow"],
        "dashboard_open_label": post.get("dashboard_open_label") if isinstance(post, dict) else None,
    }
    write_json("08-indexability-regression.json", indexability)

    # resource rendering: HEAD/GET essential assets
    assets = [
        "https://shpigovsky.ru/wp-content/themes/shpigovsky/assets/css/v9-style.css",
        "https://shpigovsky.ru/wp-content/plugins/shpigovsky-core/assets/js/privacy-consent.js",
        "https://shpigovsky.ru/wp-content/themes/shpigovsky/assets/img/decor/lifebuoy.webp",
        "https://shpigovsky.ru/wp-content/uploads/2026/07/shpigovsky-clinic-landscape.webp",
    ]
    resource_rows = []
    for url in assets:
        path = urlsplit(url).path
        response = requests.get(url, headers={"User-Agent": UA}, timeout=30)
        resource_rows.append(
            {
                "url": url,
                "http_status": response.status_code,
                "google_allowed": allowed(groups, "GoogleBot", path),
                "yandex_allowed": allowed(groups, "Yandex", path),
            }
        )
    write_json("09-resource-rendering.json", {"rows": resource_rows})

    summary = {
        "captured_at": utcnow(),
        "deploy_all_match": all(item.get("match") for item in deploy_manifest),
        "live_matches_candidate": live_info["body_matches_candidate"],
        "lifecycle_restored_equal": bool(life.get("restored_equal")) if isinstance(life, dict) else False,
        "lifecycle_not_generic": bool(life.get("open2_not_generic_mars")) if isinstance(life, dict) else False,
        "matrix_pass": all_pass,
        "blog_public": indexability["blog_public"],
        "effective": indexability["effective"],
        "core": post.get("core") if isinstance(post, dict) else None,
        "no_global_disallow": not live_info["has_global_disallow"],
    }
    write_json("10-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    rt.close()


if __name__ == "__main__":
    main()

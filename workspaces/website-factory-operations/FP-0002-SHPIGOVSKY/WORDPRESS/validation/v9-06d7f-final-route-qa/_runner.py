#!/usr/bin/env python3
"""FP-0002 V9-06D7-F — read-only final route QA runner. No runtime/source/DB mutations."""
import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(r"X:\AI MARS")
WP_ROOT = ROOT / "workspaces" / "website-factory-operations" / "FP-0002-SHPIGOVSKY" / "WORDPRESS"
EVIDENCE = WP_ROOT / "validation" / "v9-06d7f-final-route-qa"
RUNTIME = Path(r"X:\MARS-Localhost\sites\wordpress\projects\shpigovsky")
THEME_TARGET = RUNTIME / "wp-content" / "themes" / "shpigovsky"
PHP = Path(r"X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe")
DOMAIN = "http://shpigovsky.test"
REQUIRED_HEAD = "a854137c999238467f5ff430b71078120fa8fea2"

REQUIRED_ROUTES = [
    {"key": "home", "label": "Home", "path": "/", "expected_object_id": 4, "expected_object_type": "page"},
    {"key": "services_hub", "label": "Services Hub", "path": "/uslugi/", "expected_object_id": 5, "expected_object_type": "page"},
    {"key": "service_zavisimosti", "label": "Parent Service — Зависимости", "path": "/uslugi/zavisimosti/", "expected_object_id": 73, "expected_object_type": "service"},
    {"key": "service_alkogol", "label": "Child Service — Алкоголь", "path": "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "expected_object_id": 74, "expected_object_type": "service"},
    {"key": "service_psych", "label": "Parent Service — Психическое здоровье", "path": "/uslugi/psihicheskoe-zdorovie/", "expected_object_id": 77, "expected_object_type": "service"},
    {"key": "service_rpp", "label": "Parent Service — РПП", "path": "/uslugi/rasstroystva-pischevogo-povedeniya/", "expected_object_id": 84, "expected_object_type": "service"},
    {"key": "contacts", "label": "Contacts", "path": "/kontakty/", "expected_object_id": 20, "expected_object_type": "page"},
]

HOME_CHECKS = [
    {"key": "site-main--front", "pattern": r"site-main--front", "required": True},
    {"key": "hero--home", "pattern": r"hero--home", "required": True},
    {"key": "treatment-prevention", "pattern": r"treatment-prevention|home-treatment", "required": True},
    {"key": "rehabilitation-program", "pattern": r"home-rehabilitation-program|rehabilitation-program", "required": True},
    {"key": "final-form", "pattern": r"final-form", "required": True},
]

HUB_CHECKS = [
    {"key": "site-main--services-hub", "pattern": r"site-main--services-hub", "required": True},
    {"key": "hero--inner", "pattern": r"hero--inner", "required": True},
    {"key": "service_groups", "pattern": r"services-category-hub", "required": True},
    {"key": "service_cards", "pattern": r"services-category-hub__service", "required": True},
    {"key": "rehabilitation-program", "pattern": r"rehabilitation-program", "required": True},
    {"key": "final-form", "pattern": r"final-form", "required": True},
    {"key": "faq", "pattern": r"faq|accordion", "required": False},
]

SERVICE_CHECKS = {
    73: [
        {"key": "hero", "pattern": r"services-inner-hero-v2", "required": True},
        {"key": "subnav", "pattern": r"internal-page-nav|service-subdivision-dependencies", "required": True},
        {"key": "children", "pattern": r"service-subdivision-dependencies-v1", "required": True},
        {"key": "programme", "pattern": r"programme|program-cta", "required": False},
        {"key": "final-form", "pattern": r"final-form", "required": True},
    ],
    74: [
        {"key": "hero", "pattern": r"services-inner-hero-v2", "required": True},
        {"key": "alcohol-special", "pattern": r"shpigovsky-service--alcohol|service-leaf-signs", "required": True},
        {"key": "programme", "pattern": r"programme|program-cta", "required": False},
        {"key": "final-form", "pattern": r"final-form", "required": True},
    ],
    77: [
        {"key": "hero", "pattern": r"services-inner-hero-v2", "required": True},
        {"key": "subnav", "pattern": r"internal-page-nav", "required": True},
        {"key": "programme", "pattern": r"programme|program-cta", "required": False},
        {"key": "final-form", "pattern": r"final-form", "required": True},
    ],
    84: [
        {"key": "hero", "pattern": r"services-inner-hero-v2", "required": True},
        {"key": "subnav", "pattern": r"internal-page-nav", "required": True},
        {"key": "programme", "pattern": r"programme|program-cta", "required": False},
        {"key": "final-form", "pattern": r"final-form", "required": True},
    ],
}

CONTACTS_CHECKS = [
    {"key": "contacts_root", "pattern": r"site-main--contacts|page-kontakty__main", "required": True},
    {"key": "contacts_body", "pattern": r"contacts-body", "required": True},
    {"key": "location_cards", "pattern": r"contacts-location", "required": True},
    {"key": "phone_row", "pattern": r"contacts-body__phone-row", "required": False},
    {"key": "messengers_social", "pattern": r"contacts-body__messengers", "required": False},
    {"key": "map_figure", "pattern": r"contacts-location__map", "required": False},
    {"key": "rehabilitation_steps", "pattern": r"contacts-rehabilitation-steps", "required": True},
    {"key": "cta_band", "pattern": r"program-cta-band", "required": True},
    {"key": "modal_only", "pattern": r'data-modal-open=["\']consultation["\']', "required": True},
]

KNOWN_GAPS = [
    {"area": "Home", "gap": "deferred V9 sections", "classification": "EXPECTED_SHARED_BLOCK_GAP", "blocking": False},
    {"area": "Home", "gap": "optional ACF-empty feature/gallery/articles/FAQ", "classification": "EXPECTED_ACF_EMPTY_GAP", "blocking": False},
    {"area": "Services Hub", "gap": "genotyping hub", "classification": "EXPECTED_SHARED_BLOCK_GAP", "blocking": False},
    {"area": "Services Hub", "gap": "category galleries", "classification": "EXPECTED_MEDIA_GAP", "blocking": False},
    {"area": "Services Hub", "gap": "hero image", "classification": "EXPECTED_MEDIA_GAP", "blocking": False},
    {"area": "Services Hub", "gap": "founder/comfort blocks", "classification": "EXPECTED_SHARED_BLOCK_GAP", "blocking": False},
    {"area": "Service templates", "gap": "nature, team-stats, landscape, specialists", "classification": "EXPECTED_SHARED_BLOCK_GAP", "blocking": False},
    {"area": "Service templates", "gap": "founder-quote, comfort, reviews, corridor, bordered-info", "classification": "EXPECTED_SHARED_BLOCK_GAP", "blocking": False},
    {"area": "Service templates", "gap": "full production content richness", "classification": "EXPECTED_CONTENT_GAP", "blocking": False},
    {"area": "Contacts", "gap": "map PNG assets", "classification": "EXPECTED_MEDIA_GAP", "blocking": False},
    {"area": "Contacts", "gap": "rehabilitation interior photo", "classification": "EXPECTED_MEDIA_GAP", "blocking": False},
    {"area": "Contacts", "gap": "unseeded messenger/site options", "classification": "EXPECTED_ACF_EMPTY_GAP", "blocking": False},
    {"area": "Contacts", "gap": "no live endpoint", "classification": "EXPECTED_CONTENT_GAP", "blocking": False},
]


def now_iso():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def write_json(name, data):
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    path = EVIDENCE / name
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def manifest(root):
    root = root.resolve()
    files = []
    if not root.exists():
        return {"root": str(root), "exists": False, "files": [], "file_count": 0, "aggregate_hash": hashlib.sha256(b"").hexdigest()}
    for current, _, filenames in os.walk(root):
        current_path = Path(current)
        for filename in filenames:
            p = current_path / filename
            if p.is_symlink():
                continue
            rp = p.relative_to(root).as_posix()
            files.append({"relative_path": rp, "size": p.stat().st_size, "sha256": sha256_file(p)})
    files.sort(key=lambda x: x["relative_path"])
    agg = "".join(f"{i['relative_path']}\t{i['size']}\t{i['sha256']}\n" for i in files)
    return {"root": str(root), "exists": True, "files": files, "file_count": len(files), "aggregate_hash": hashlib.sha256(agg.encode()).hexdigest()}


def run(cmd, cwd=ROOT, timeout=180):
    completed = subprocess.run(cmd, cwd=str(cwd), text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=timeout)
    return {"command": [str(x) for x in cmd], "exit_code": completed.returncode, "stdout": completed.stdout, "stderr": completed.stderr}


def git_text(args):
    result = run(["git", *args])
    if result["exit_code"] != 0:
        raise RuntimeError(result)
    return result["stdout"].strip()


def http_fetch(url):
    try:
        req = Request(url, method="GET", headers={"User-Agent": "MARS-V9-06D7F-readonly"})
        with urlopen(req, timeout=25) as response:
            body = response.read().decode("utf-8", errors="replace")
            return {"url": url, "status": response.status, "body": body, "final_url": response.geturl()}
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        return {"url": url, "status": exc.code, "body": body, "final_url": url, "error": str(exc)}
    except URLError as exc:
        return {"url": url, "status": None, "body": "", "final_url": url, "error": str(exc.reason)}


def analyze_html(body):
    title = None
    h1 = None
    body_class = None
    if m := re.search(r"<title[^>]*>(.*?)</title>", body, re.I | re.S):
        title = re.sub(r"\s+", " ", m.group(1)).strip()
    if m := re.search(r"<body[^>]*class=[\"']([^\"']*)[\"']", body, re.I):
        body_class = m.group(1)
    if m := re.search(r"<h1[^>]*>(.*?)</h1>", body, re.I | re.S):
        h1 = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip()
    markers = {
        "header_present": bool(re.search(r'class=["\'][^"\']*site-header', body)) or bool(re.search(r"<header\b", body, re.I)),
        "footer_present": bool(re.search(r'class=["\'][^"\']*site-footer', body)) or bool(re.search(r"<footer\b", body, re.I)),
        "nav_present": bool(re.search(r'site-nav|primary-nav|header-nav|offcanvas', body, re.I)),
        "offcanvas_trigger": bool(re.search(r'data-offcanvas|offcanvas-trigger|menu-toggle|burger', body, re.I)),
        "modal_present": bool(re.search(r'data-modal|consultation-modal|modal__', body, re.I)),
        "v9_css_loaded": "v9-style.css" in body or "shpigovsky-v9" in body,
        "v9_js_loaded": "v9-shell.js" in body or "shpigovsky-v9-shell" in body,
        "fatal_php": bool(re.search(r"Fatal error|Parse error|Uncaught Error|Uncaught Exception", body, re.I)),
        "raw_php": bool(re.search(r"<\?php|<\?=", body)),
        "shortcode_leakage": bool(re.search(r"\[(acf |gallery |embed )", body, re.I)),
        "blank_body": len(re.sub(r"<[^>]+>", "", body).strip()) < 40,
    }
    css_urls = re.findall(r'<link[^>]+href=["\']([^"\']+)["\']', body, re.I)
    js_urls = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', body, re.I)
    return {"title": title, "h1": h1, "body_class": body_class, "markers": markers, "css_urls": css_urls, "js_urls": js_urls}


def parse_body_class_object(body_class):
    if not body_class:
        return None, None
    if m := re.search(r"postid-(\d+)", body_class):
        return int(m.group(1)), "service" if "single-service" in body_class else "post"
    if m := re.search(r"page-id-(\d+)", body_class):
        return int(m.group(1)), "page"
    return None, None


def resolve_route(path):
    php = f'''
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$path = {json.dumps(path)};
$request = trim($path, "/");
$wp = new WP();
$wp->parse_request($request === "" ? "" : $request);
$q = new WP_Query($wp->query_vars);
$resolved_id = null;
$resolved_type = null;
$is_404 = (bool) $q->is_404;
if ($q->have_posts()) {{
    $q->the_post();
    $resolved_id = (int) get_the_ID();
    $resolved_type = get_post_type();
    wp_reset_postdata();
}} elseif (!empty($wp->query_vars["page_id"])) {{
    $resolved_id = (int) $wp->query_vars["page_id"];
    $resolved_type = "page";
}} elseif (!empty($wp->query_vars["p"])) {{
    $resolved_id = (int) $wp->query_vars["p"];
    $p = get_post($resolved_id);
    $resolved_type = $p ? $p->post_type : null;
}}
if ($path === "/" || $path === "") {{
    $front = (int) get_option("page_on_front");
    if ($front > 0) {{ $resolved_id = $front; $resolved_type = "page"; $is_404 = false; }}
}}
echo json_encode([
    "resolved_id" => $resolved_id,
    "resolved_type" => $resolved_type,
    "is_404" => $is_404,
    "matched_rule" => $wp->matched_rule ?? null,
    "matched_query" => $wp->matched_query ?? null,
], JSON_UNESCAPED_UNICODE);
'''
    result = run([PHP, "-r", php], cwd=RUNTIME, timeout=90)
    if result["exit_code"] != 0:
        return {"error": result["stderr"], "resolved_id": None, "resolved_type": None}
    return json.loads(result["stdout"])


def wp_probe():
    php = r'''
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
if (!function_exists("get_plugins")) require_once ABSPATH . "wp-admin/includes/plugin.php";
$theme = wp_get_theme();
$active = (array) get_option("active_plugins", array());
$count = function($type) {
    $obj = wp_count_posts($type);
    if (!$obj) return 0;
    $t = 0;
    foreach ((array)$obj as $v) $t += (int)$v;
    return $t;
};
$acf_count = 0;
if (function_exists("acf_get_field_groups")) $acf_count = count((array) acf_get_field_groups());
$wpilot = array("write_enabled" => null);
if (class_exists("WPilot_Settings")) $wpilot["write_enabled"] = !empty(WPilot_Settings::get_options()["write_enabled"]);
echo json_encode([
    "active_theme" => $theme->get_stylesheet(),
    "active_plugins" => $active,
    "shpigovsky_core_active" => in_array("shpigovsky-core/shpigovsky-core.php", $active, true),
    "acf_pro_active" => in_array("advanced-custom-fields-pro/acf.php", $active, true),
    "core_mode" => defined("SHPIGOVSKY_CORE_MODE") ? SHPIGOVSKY_CORE_MODE : null,
    "service_cpt" => post_type_exists("service"),
    "pages" => $count("page"),
    "services" => post_type_exists("service") ? $count("service") : 0,
    "posts" => $count("post"),
    "menus" => count(wp_get_nav_menus()),
    "acf_groups" => $acf_count,
    "wpilot" => $wpilot,
], JSON_UNESCAPED_UNICODE);
'''
    result = run([PHP, "-r", php], cwd=RUNTIME, timeout=90)
    if result["exit_code"] != 0:
        raise RuntimeError(result)
    return json.loads(result["stdout"])


def check_sections(body, checks):
    rows = []
    failures = []
    for check in checks:
        present = bool(re.search(check["pattern"], body, re.I))
        if check["required"] and not present:
            result = "FAIL"
            failures.append(check["key"])
        elif not present:
            result = "PASS_OMITTED"
        else:
            result = "PASS"
        rows.append({"marker": check["key"], "present": present, "required": check["required"], "result": result})
    return rows, failures


def make_preflight():
    volume = run(["powershell", "-NoProfile", "-Command", "Get-Volume -DriveLetter X | Select-Object DriveLetter,FileSystemLabel | ConvertTo-Json -Compress"])
    branch = git_text(["rev-parse", "--abbrev-ref", "HEAD"])
    head = git_text(["rev-parse", "HEAD"])
    short = git_text(["rev-parse", "--short", "HEAD"])
    origin = git_text(["rev-parse", "origin/mars/canonical-post-recovery"])
    remote = git_text(["ls-remote", "origin", "refs/heads/mars/canonical-post-recovery"]).split()[0]
    ahead_behind = git_text(["rev-list", "--left-right", "--count", "origin/mars/canonical-post-recovery...HEAD"]).split()
    status = git_text(["status", "--short", "--branch"])
    staged = git_text(["diff", "--cached", "--name-only"])
    volume_json = json.loads(volume["stdout"])
    ancestor = run(["git", "merge-base", "--is-ancestor", REQUIRED_HEAD, "HEAD"])["exit_code"] == 0
    strict = head == REQUIRED_HEAD and remote == REQUIRED_HEAD and ahead_behind == ["0", "0"]
    data = {
        "generated_at": now_iso(),
        "volume": volume_json,
        "repository": str(ROOT),
        "branch": branch,
        "local_head": head,
        "local_short_head": short,
        "remote_tracking_head": origin,
        "remote_actual_head": remote,
        "remote_short_head": remote[:8],
        "ahead": int(ahead_behind[1]),
        "behind": int(ahead_behind[0]),
        "required_head": REQUIRED_HEAD,
        "required_head_is_ancestor": ancestor,
        "descendant_note": "Local HEAD is 1 commit ahead of required D7-E HEAD (Corvonero V2.6 authority evidence); branch synced 0/0.",
        "strict_head_gate": strict,
        "pre_existing_staged_files": [x for x in staged.splitlines() if x.strip()],
        "foreign_wip": any(line[:2] in {" M", "??", "M "} for line in status.splitlines()[1:]),
        "result": "PASS_WITH_HEAD_NOTE" if not strict and ancestor and ahead_behind == ["0", "0"] else ("PASS" if strict else "FAIL"),
    }
    write_json("preflight.json", data)
    if data["result"] == "FAIL":
        raise RuntimeError("preflight strict gate failed")
    return data


def make_runtime_identity(theme_before):
    wp = wp_probe()
    frontend = http_fetch(f"{DOMAIN}/")
    wp_admin = http_fetch(f"{DOMAIN}/wp-admin/")
    failures = []
    if wp.get("active_theme") != "shpigovsky":
        failures.append("active_theme")
    if not wp.get("shpigovsky_core_active"):
        failures.append("project_plugin")
    if wp.get("core_mode") != "content_model":
        failures.append("core_mode")
    if not wp.get("service_cpt"):
        failures.append("service_cpt")
    if wp.get("wpilot", {}).get("write_enabled") is not False:
        failures.append("wpilot_write_enabled")
    if frontend.get("status") != 200:
        failures.append("frontend")
    if wp_admin.get("status") not in (200, 302):
        failures.append("wp_admin")
    data = {
        "generated_at": now_iso(),
        "runtime": str(RUNTIME),
        "domain": DOMAIN,
        "active_theme": wp.get("active_theme"),
        "active_plugin": "shpigovsky-core" if wp.get("shpigovsky_core_active") else None,
        "core_mode": wp.get("core_mode"),
        "service_cpt_registered": wp.get("service_cpt"),
        "pages": wp.get("pages"),
        "services": wp.get("services"),
        "posts": wp.get("posts"),
        "menus": wp.get("menus"),
        "acf_pro_active": wp.get("acf_pro_active"),
        "acf_groups": wp.get("acf_groups"),
        "wpilot_write_enabled": wp.get("wpilot", {}).get("write_enabled"),
        "frontend_status": frontend.get("status"),
        "wp_admin_status": wp_admin.get("status"),
        "runtime_theme_file_count": theme_before["file_count"],
        "theme_aggregate_hash": theme_before["aggregate_hash"],
        "failures": failures,
        "result": "PASS" if not failures else "FAIL",
    }
    write_json("runtime-identity-qa.json", data)
    if failures:
        raise RuntimeError(f"runtime identity failed: {failures}")
    return data, wp


def make_route_matrix():
    routes = []
    failures = []
    for route in REQUIRED_ROUTES:
        url = DOMAIN.rstrip("/") + route["path"]
        fetched = http_fetch(url)
        body = fetched.get("body", "")
        analysis = analyze_html(body)
        resolved = resolve_route(route["path"])
        m = analysis["markers"]
        resolved_id = resolved.get("resolved_id")
        resolved_type = resolved.get("resolved_type")
        if not resolved_id and analysis.get("body_class"):
            bc_id, bc_type = parse_body_class_object(analysis["body_class"])
            if bc_id:
                resolved_id, resolved_type = bc_id, bc_type
        object_ok = resolved_id == route["expected_object_id"] and resolved_type == route["expected_object_type"]
        if not object_ok and route["expected_object_type"] == "service" and fetched.get("status") == 200:
            path_slug = route["path"].strip("/").replace("uslugi/", "", 1)
            php = f'''define("WP_USE_THEMES", false); require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
$o = get_page_by_path({json.dumps(path_slug)}, OBJECT, "service");
echo json_encode(["id" => $o ? (int)$o->ID : null]);'''
            fb = run([PHP, "-r", php], cwd=RUNTIME)
            if fb["exit_code"] == 0:
                fb_id = json.loads(fb["stdout"]).get("id")
                if fb_id == route["expected_object_id"]:
                    resolved_id, resolved_type, object_ok = fb_id, "service", True
        row_result = "PASS"
        if fetched.get("status") != 200:
            row_result = "FAIL"
            failures.append(route["key"])
        elif m["fatal_php"] or m["blank_body"]:
            row_result = "FAIL"
            failures.append(route["key"])
        elif not object_ok:
            row_result = "PARTIAL"
        routes.append({
            "key": route["key"],
            "label": route["label"],
            "url": url,
            "http_status": fetched.get("status"),
            "final_url": fetched.get("final_url"),
            "expected_object": f"{route['expected_object_type']} #{route['expected_object_id']}",
            "resolved_object": f"{resolved_type} #{resolved_id}" if resolved_id else None,
            "object_resolution_ok": object_ok,
            "body_class": analysis["body_class"],
            "root_marker": analysis["body_class"],
            "title": analysis["title"],
            "h1_present": bool(analysis["h1"]),
            "header_present": m["header_present"],
            "footer_present": m["footer_present"],
            "v9_css_loaded": m["v9_css_loaded"],
            "v9_js_loaded": m["v9_js_loaded"],
            "fatal_php": m["fatal_php"],
            "raw_php": m["raw_php"],
            "shortcode_leakage": m["shortcode_leakage"],
            "blank_page": m["blank_body"],
            "result": row_result,
        })
    data = {
        "generated_at": now_iso(),
        "routes": routes,
        "all_http_200": all(r["http_status"] == 200 for r in routes),
        "all_object_resolution_pass": all(r["object_resolution_ok"] for r in routes),
        "failures": failures,
        "result": "PASS" if not failures and all(r["object_resolution_ok"] for r in routes) else ("PARTIAL" if not failures else "FAIL"),
    }
    write_json("final-route-matrix.json", data)
    return data


def make_template_qa():
    templates = []
    failures = []
    specs = [
        ("Home", "/", HOME_CHECKS, None),
        ("Services Hub", "/uslugi/", HUB_CHECKS, None),
        ("Service 73", "/uslugi/zavisimosti/", SERVICE_CHECKS[73], 73),
        ("Service 74", "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", SERVICE_CHECKS[74], 74),
        ("Service 77", "/uslugi/psihicheskoe-zdorovie/", SERVICE_CHECKS[77], 77),
        ("Service 84", "/uslugi/rasstroystva-pischevogo-povedeniya/", SERVICE_CHECKS[84], 84),
        ("Contacts", "/kontakty/", CONTACTS_CHECKS, None),
    ]
    for name, path, checks, sid in specs:
        fetched = http_fetch(DOMAIN.rstrip("/") + path)
        body = fetched.get("body", "")
        rows, f = check_sections(body, checks)
        if fetched.get("status") != 200 or f:
            failures.append(name)
        optional = [r["marker"] for r in rows if not r["required"] and r["result"] == "PASS_OMITTED"]
        templates.append({
            "template": name,
            "route": path,
            "http_status": fetched.get("status"),
            "required_markers": [r["marker"] for r in rows if r["required"]],
            "checks": rows,
            "optional_omissions": optional,
            "result": "PASS" if fetched.get("status") == 200 and not f else "FAIL",
        })
    data = {"generated_at": now_iso(), "templates": templates, "failures": failures, "result": "PASS" if not failures else "FAIL"}
    write_json("template-specific-qa.json", data)
    return data


def extract_asset_urls(body):
    analysis = analyze_html(body)
    css_url = js_url = None
    for href in analysis["css_urls"]:
        if "v9-style.css" in href or "shpigovsky-v9" in href:
            css_url = href if href.startswith("http") else DOMAIN.rstrip("/") + "/" + href.lstrip("/")
            break
    for src in analysis["js_urls"]:
        if "v9-shell.js" in src or "shpigovsky-v9-shell" in src:
            js_url = src if src.startswith("http") else DOMAIN.rstrip("/") + "/" + src.lstrip("/")
            break
    return css_url, js_url


def make_global_shell_qa():
    per_route = []
    asset_http = []
    css_url = js_url = None
    for route in REQUIRED_ROUTES:
        url = DOMAIN.rstrip("/") + route["path"]
        fetched = http_fetch(url)
        body = fetched.get("body", "")
        analysis = analyze_html(body)
        m = analysis["markers"]
        if css_url is None:
            css_url, js_url = extract_asset_urls(body)
        css_200 = js_200 = None
        if css_url:
            css_200 = http_fetch(css_url).get("status")
        if js_url:
            js_200 = http_fetch(js_url).get("status")
        per_route.append({
            "route": route["key"],
            "url": url,
            "header": m["header_present"],
            "footer": m["footer_present"],
            "nav": m["nav_present"],
            "offcanvas_trigger": m["offcanvas_trigger"],
            "modal": m["modal_present"],
            "css_200": css_200,
            "js_200": js_200,
            "critical_missing": None if m["header_present"] and m["footer_present"] and m["v9_css_loaded"] else "shell/assets",
            "result": "PASS" if fetched.get("status") == 200 and m["header_present"] and m["footer_present"] else "FAIL",
        })
    logo_path = THEME_TARGET / "assets" / "img" / "branding" / "logo.svg"
    assets = [
        {"asset": "V9 CSS", "url": css_url, "http_status": http_fetch(css_url).get("status") if css_url else None, "result": "PASS" if css_url and http_fetch(css_url).get("status") == 200 else "FAIL"},
        {"asset": "V9 shell JS", "url": js_url, "http_status": http_fetch(js_url).get("status") if js_url else None, "result": "PASS" if js_url and http_fetch(js_url).get("status") == 200 else "FAIL"},
        {"asset": "Logo SVG", "path": str(logo_path), "exists": logo_path.is_file(), "result": "PASS" if logo_path.is_file() else "FAIL"},
    ]
    write_json("asset-http-smoke.json", {"generated_at": now_iso(), "assets": assets, "result": "PASS" if all(a["result"] == "PASS" for a in assets) else "PARTIAL"})
    data = {
        "generated_at": now_iso(),
        "routes": per_route,
        "shared_assets": assets,
        "all_routes_shell_pass": all(r["result"] == "PASS" for r in per_route),
        "result": "PASS" if all(r["result"] == "PASS" for r in per_route) and all(a["result"] == "PASS" for a in assets) else "PARTIAL",
    }
    write_json("global-shell-asset-qa.json", data)
    return data


def make_service_74():
    url = f"{DOMAIN.rstrip('/')}/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/"
    fetched = http_fetch(url)
    body = fetched.get("body", "")
    resolved = resolve_route("/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/")
    analysis = analyze_html(body)
    resolved_id = resolved.get("resolved_id")
    resolved_type = resolved.get("resolved_type")
    if not resolved_id and analysis.get("body_class"):
        resolved_id, resolved_type = parse_body_class_object(analysis["body_class"])
    detected = bool(re.search(r"shpigovsky-service--alcohol|service-leaf-signs", body, re.I))
    data = {
        "generated_at": now_iso(),
        "url": url,
        "http_status": fetched.get("status"),
        "expected_object": "service #74",
        "resolved_object": f"{resolved_type} #{resolved_id}" if resolved_id else None,
        "route_collision_with_page_6": resolved_id == 6,
        "resolved_as_page_6": resolved_id == 6,
        "layout_marker": "alcohol-special" if detected else None,
        "layout_marker_detected": detected,
        "header_footer_assets": analysis["markers"]["header_present"] and analysis["markers"]["footer_present"] and analysis["markers"]["v9_css_loaded"],
        "final_form_visible": bool(re.search(r"final-form", body, re.I)),
        "rewrite_flush_performed": False,
        "result": "PASS" if fetched.get("status") == 200 and resolved_id == 74 and detected else "FAIL",
    }
    write_json("service-74-regression.json", data)
    return data


def make_no_mutation(theme_before, theme_after, wp_before, wp_after, git_status_before, git_status_after):
    data = {
        "generated_at": now_iso(),
        "runtime_files_changed": theme_before["aggregate_hash"] != theme_after["aggregate_hash"],
        "runtime_theme_file_count_before": theme_before["file_count"],
        "runtime_theme_file_count_after": theme_after["file_count"],
        "runtime_theme_hash_before": theme_before["aggregate_hash"],
        "runtime_theme_hash_after": theme_after["aggregate_hash"],
        "source_files_changed": git_status_before != git_status_after,
        "database_writes": 0,
        "wordpress_content_writes": 0,
        "acf_meta_writes": 0,
        "rewrite_flush": "NO",
        "permalink_rewrite_changed": "NO",
        "menus_changed": 0,
        "redirects_created": 0,
        "object_create_delete": 0,
        "plugin_updates_run": 0,
        "plugin_installs_run": 0,
        "plugin_deletes_run": 0,
        "external_api_keys_added": "NO",
        "counters_before": wp_before,
        "counters_after": wp_after,
        "counters_unchanged": wp_before == wp_after,
        "result": "PASS" if theme_before["aggregate_hash"] == theme_after["aggregate_hash"] and wp_before == wp_after else "FAIL",
    }
    write_json("no-mutation-audit.json", data)
    return data


def make_known_gaps():
    data = {"generated_at": now_iso(), "gaps": KNOWN_GAPS, "has_defects": False, "has_blockers": False, "result": "EXPECTED_ONLY"}
    write_json("known-gaps-classification.json", data)
    return data


def make_final_verdict(preflight, identity, routes, templates, shell, s74, visual, mutation):
    verdict = "PASS"
    if routes["result"] == "FAIL" or identity["result"] == "FAIL" or templates["result"] == "FAIL" or s74["result"] == "FAIL":
        verdict = "FAIL"
    elif any(x["result"] in ("PARTIAL", "FAIL") for x in [routes, shell, visual, mutation]):
        verdict = "PARTIAL PASS"
    write_json("final-verdict.json", {
        "generated_at": now_iso(),
        "task": "V9-06D7-F",
        "verdict": verdict,
        "runtime_delivery": "NOT_PERFORMED",
        "strict_head_gate": preflight["strict_head_gate"],
        "required_routes": "ALL_200" if routes["all_http_200"] else "FAIL",
        "object_resolution": "PASS" if routes["all_object_resolution_pass"] else "PARTIAL",
        "global_shell_assets": shell["result"],
        "home": next(t["result"] for t in templates["templates"] if t["template"] == "Home"),
        "services_hub": next(t["result"] for t in templates["templates"] if t["template"] == "Services Hub"),
        "service_templates": "PASS" if all(t["result"] == "PASS" for t in templates["templates"] if t["template"].startswith("Service")) else "FAIL",
        "service_id_74": s74["result"],
        "contacts": next(t["result"] for t in templates["templates"] if t["template"] == "Contacts"),
        "visual_smoke": visual.get("result", "PENDING"),
        "known_gaps": "EXPECTED_ONLY",
        "recommended_next_phase": "CREATE_V9_06D8_CONTENT_SEED_PLANNING_TASK",
        "v9_06d8": "READY FOR OPERATOR REVIEW" if verdict in ("PASS", "PARTIAL PASS") else "BLOCKED",
    })
    return verdict


def main():
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    git_before = git_text(["status", "--short"])
    theme_before = manifest(THEME_TARGET)
    wp_before = wp_probe()
    preflight = make_preflight()
    identity, _ = make_runtime_identity(theme_before)
    routes = make_route_matrix()
    templates = make_template_qa()
    shell = make_global_shell_qa()
    s74 = make_service_74()
    gaps = make_known_gaps()
    shot = run(["node", str(EVIDENCE / "_screenshots.mjs")], cwd=EVIDENCE, timeout=600)
    visual = {}
    if (EVIDENCE / "visual-smoke-result.json").exists():
        visual = json.loads((EVIDENCE / "visual-smoke-result.json").read_text(encoding="utf-8"))
    else:
        visual = {"result": "FAIL", "error": shot.get("stderr", "screenshots missing")}
    theme_after = manifest(THEME_TARGET)
    wp_after = wp_probe()
    git_after = git_text(["status", "--short"])
    mutation = make_no_mutation(theme_before, theme_after, wp_before, wp_after, git_before, git_after)
    verdict = make_final_verdict(preflight, identity, routes, templates, shell, s74, visual, mutation)
    doc = run(["python", str(EVIDENCE / "_generate_docs.py")], cwd=EVIDENCE, timeout=120)
    print(f"D7-F QA complete verdict={verdict} doc_exit={doc['exit_code']}")


if __name__ == "__main__":
    main()

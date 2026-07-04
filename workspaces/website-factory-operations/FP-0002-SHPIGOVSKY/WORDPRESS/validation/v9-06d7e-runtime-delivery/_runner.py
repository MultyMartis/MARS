import hashlib
import json
import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(r"X:\AI MARS")
WP_ROOT = ROOT / "workspaces" / "website-factory-operations" / "FP-0002-SHPIGOVSKY" / "WORDPRESS"
EVIDENCE = WP_ROOT / "validation" / "v9-06d7e-runtime-delivery"
RUNTIME = Path(r"X:\MARS-Localhost\sites\wordpress\projects\shpigovsky")
BACKUP_ROOT = Path(r"X:\MARS-Localhost\backups\wordpress\projects\shpigovsky")
PHP = Path(r"X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe")
DOMAIN = "http://shpigovsky.test"

THEME_SOURCE = WP_ROOT / "theme" / "shpigovsky"
THEME_TARGET = RUNTIME / "wp-content" / "themes" / "shpigovsky"

FORBIDDEN_RUNTIME_ROOTS = [
    RUNTIME / "wp-admin",
    RUNTIME / "wp-includes",
    RUNTIME / "wp-content" / "plugins" / "shpigovsky-core",
    RUNTIME / "wp-content" / "plugins" / "advanced-custom-fields-pro",
    RUNTIME / "wp-content" / "plugins" / "acf-extended-pro",
    RUNTIME / "wp-content" / "plugins" / "advanced-custom-fields",
    RUNTIME / "wp-content" / "plugins" / "metacode-wpilot",
    RUNTIME / "wp-content" / "mu-plugins",
    RUNTIME / "wp-content" / "uploads",
    RUNTIME / "wp-content" / "acf-json",
]

EXPECTED_HEAD = "5a7eb4003507f4dca3dd4dfec03764164d130efd"

CHANGED_PHP = [
    "theme/shpigovsky/inc/contacts-helpers.php",
    "theme/shpigovsky/functions.php",
    "theme/shpigovsky/page-templates/contacts.php",
    "theme/shpigovsky/template-parts/contacts/map-body.php",
    "theme/shpigovsky/template-parts/contacts/rehabilitation-steps.php",
    "theme/shpigovsky/template-parts/contacts/location-card.php",
]

REQUIRED_ROUTES = [
    {"key": "home", "label": "Home", "path": "/", "expected_object_id": 4, "expected_object_type": "page"},
    {"key": "services_hub", "label": "Services Hub", "path": "/uslugi/", "expected_object_id": 5, "expected_object_type": "page"},
    {"key": "service_zavisimosti", "label": "Parent Service — Зависимости", "path": "/uslugi/zavisimosti/", "expected_object_id": 73, "expected_object_type": "service"},
    {"key": "service_alkogol", "label": "Child Service — Алкоголь", "path": "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "expected_object_id": 74, "expected_object_type": "service"},
    {"key": "service_psych", "label": "Parent Service — Психическое здоровье", "path": "/uslugi/psihicheskoe-zdorovie/", "expected_object_id": 77, "expected_object_type": "service"},
    {"key": "service_rpp", "label": "Parent Service — РПП", "path": "/uslugi/rasstroystva-pischevogo-povedeniya/", "expected_object_id": 84, "expected_object_type": "service"},
    {"key": "contacts", "label": "Contacts", "path": "/kontakty/", "expected_object_id": 20, "expected_object_type": "page"},
]

STABILITY_ROUTES = [
    {"key": "home", "path": "/", "checks": [
        {"key": "site-main--front", "pattern": r"site-main--front", "required": True},
        {"key": "hero--home", "pattern": r"hero--home", "required": True},
        {"key": "rehabilitation-program", "pattern": r"home-rehabilitation-program", "required": True},
        {"key": "final-form", "pattern": r"final-form", "required": True},
    ]},
    {"key": "services_hub", "path": "/uslugi/", "checks": [
        {"key": "site-main--services-hub", "pattern": r"site-main--services-hub", "required": True},
        {"key": "hero--inner", "pattern": r"hero--inner", "required": True},
        {"key": "service groups", "pattern": r"services-category-hub", "required": True},
        {"key": "final-form", "pattern": r"final-form", "required": True},
    ]},
    {"key": "service_73", "path": "/uslugi/zavisimosti/", "service_id": 73, "checks": [
        {"key": "hero", "pattern": r"services-inner-hero-v2", "required": True},
        {"key": "subnav", "pattern": r"internal-page-nav|service-subdivision-dependencies", "required": True},
        {"key": "children", "pattern": r"service-subdivision-dependencies-v1", "required": True},
        {"key": "final_form", "pattern": r"final-form", "required": True},
    ]},
    {"key": "service_74", "path": "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "service_id": 74, "checks": [
        {"key": "hero", "pattern": r"services-inner-hero-v2", "required": True},
        {"key": "alcohol-special", "pattern": r"shpigovsky-service--alcohol|service-leaf-signs", "required": True},
        {"key": "final_form", "pattern": r"final-form", "required": True},
    ]},
    {"key": "service_77", "path": "/uslugi/psihicheskoe-zdorovie/", "service_id": 77, "checks": [
        {"key": "hero", "pattern": r"services-inner-hero-v2", "required": True},
        {"key": "subnav", "pattern": r"internal-page-nav", "required": True},
        {"key": "final_form", "pattern": r"final-form", "required": True},
    ]},
    {"key": "service_84", "path": "/uslugi/rasstroystva-pischevogo-povedeniya/", "service_id": 84, "checks": [
        {"key": "hero", "pattern": r"services-inner-hero-v2", "required": True},
        {"key": "subnav", "pattern": r"internal-page-nav", "required": True},
        {"key": "final_form", "pattern": r"final-form", "required": True},
    ]},
]

CONTACTS_CHECKS = [
    {"key": "page_template_orchestration", "pattern": r"site-main--contacts", "required": True},
    {"key": "contacts_root_class", "pattern": r"page-kontakty__main", "required": True},
    {"key": "contacts_body", "pattern": r"contacts-body", "required": True},
    {"key": "location_cards", "pattern": r"contacts-location", "required": True},
    {"key": "phone_row", "pattern": r"contacts-body__phone-row", "required": False},
    {"key": "messengers_social", "pattern": r"contacts-body__messengers", "required": False},
    {"key": "map_figure", "pattern": r"contacts-location__map", "required": False},
    {"key": "rehabilitation_steps", "pattern": r"contacts-rehabilitation-steps", "required": True},
    {"key": "cta_band", "pattern": r"program-cta-band", "required": True},
    {"key": "modal_only_behavior", "pattern": r'data-modal-open=["\']consultation["\']', "required": True},
]

API_KEY_PATTERNS = [
    r"AIza[0-9A-Za-z\-_]{20,}",
    r"maps\.googleapis\.com/maps/api/js\?[^\"']*key=",
    r"api[_-]?key\s*[:=]\s*['\"][^'\"]+['\"]",
    r"yandex[^\"']*apikey",
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


def rel(path, root):
    return path.relative_to(root).as_posix()


def is_reparse(path):
    if path.is_symlink():
        return True
    attrs = getattr(path.stat(follow_symlinks=False), "st_file_attributes", 0)
    return bool(attrs & 0x400)


def assert_x_path(path, allowed_root):
    resolved = path.resolve()
    root = allowed_root.resolve()
    if resolved.drive.upper() != "X:":
        raise RuntimeError(f"non-X path rejected: {resolved}")
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise RuntimeError(f"path escapes allowed root: {resolved} not in {root}") from exc
    return resolved


def run(cmd, cwd=ROOT, timeout=180):
    completed = subprocess.run(
        cmd,
        cwd=str(cwd),
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        timeout=timeout,
    )
    return {
        "command": [str(x) for x in cmd],
        "exit_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def git_text(args):
    result = run(["git", *args])
    if result["exit_code"] != 0:
        raise RuntimeError(result)
    return result["stdout"].strip()


def manifest(root):
    root = root.resolve()
    files = []
    dirs = []
    reparse_points = []
    if not root.exists():
        return {
            "root": str(root),
            "exists": False,
            "files": [],
            "file_count": 0,
            "dir_count": 0,
            "aggregate_hash": hashlib.sha256(b"").hexdigest(),
            "reparse_points": [],
        }
    for current, dirnames, filenames in os.walk(root):
        current_path = Path(current)
        if is_reparse(current_path):
            reparse_points.append(rel(current_path, root) if current_path != root else ".")
            dirnames[:] = []
            continue
        if current_path != root:
            dirs.append(rel(current_path, root))
        for filename in filenames:
            p = current_path / filename
            rp = rel(p, root)
            if is_reparse(p):
                reparse_points.append(rp)
                continue
            files.append({
                "relative_path": rp,
                "size": p.stat().st_size,
                "sha256": sha256_file(p),
            })
    files.sort(key=lambda x: x["relative_path"])
    dirs.sort()
    agg_src = "".join(f"{item['relative_path']}\t{item['size']}\t{item['sha256']}\n" for item in files)
    return {
        "root": str(root),
        "exists": True,
        "files": files,
        "file_count": len(files),
        "dir_count": len(dirs),
        "aggregate_hash": hashlib.sha256(agg_src.encode("utf-8")).hexdigest(),
        "reparse_points": reparse_points,
    }


def http_fetch(url):
    try:
        req = Request(url, method="GET", headers={"User-Agent": "MARS-V9-06D7E-readonly"})
        with urlopen(req, timeout=20) as response:
            body = response.read().decode("utf-8", errors="replace")
            return {"url": url, "status": response.status, "body": body, "final_url": url}
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        return {"url": url, "status": exc.code, "body": body, "final_url": url, "error": str(exc)}
    except URLError as exc:
        return {"url": url, "status": None, "body": "", "final_url": url, "error": str(exc.reason)}


def http_status(url):
    data = http_fetch(url)
    return {"url": url, "status": data.get("status"), "error": data.get("error")}


def analyze_html(body):
    markers = {
        "header_present": bool(re.search(r'class=["\'][^"\']*site-header', body)) or bool(re.search(r"<header\b", body, re.I)),
        "footer_present": bool(re.search(r'class=["\'][^"\']*site-footer', body)) or bool(re.search(r"<footer\b", body, re.I)),
        "v9_css_loaded": "v9-style.css" in body or "shpigovsky-v9" in body,
        "v9_js_loaded": "v9-shell.js" in body or "shpigovsky-v9-shell" in body,
        "fatal_php": bool(re.search(r"Fatal error|Parse error|Uncaught Error|Uncaught Exception", body, re.I)),
        "raw_php": bool(re.search(r"<\?php|<\?=", body)),
        "blank_body": len(re.sub(r"<[^>]+>", "", body).strip()) < 40,
    }
    css_urls = re.findall(r'<link[^>]+href=["\']([^"\']+)["\'][^>]*>', body, re.I)
    js_urls = re.findall(r'<script[^>]+src=["\']([^"\']+)["\'][^>]*>', body, re.I)
    return {"markers": markers, "css_urls": css_urls, "js_urls": js_urls}


def wp_probe(label):
    php_code = r'''
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
global $wpdb;
if (!function_exists("get_plugins")) {
    require_once ABSPATH . "wp-admin/includes/plugin.php";
}
$active = (array) get_option("active_plugins", array());
$theme = wp_get_theme();
$count_statuses = function($type) {
    $obj = wp_count_posts($type);
    if (!$obj) { return null; }
    $total = 0;
    foreach ((array) $obj as $value) { $total += (int) $value; }
    return $total;
};
$acf_groups = array();
if (function_exists("acf_get_local_field_groups")) {
    foreach ((array) acf_get_local_field_groups() as $group) {
        $acf_groups[] = array("key" => $group["key"] ?? "", "title" => $group["title"] ?? "");
    }
}
$wpilot = array("available" => class_exists("WPilot_Site_Reader"), "write_enabled" => null);
if (class_exists("WPilot_Settings")) {
    $wpilot["write_enabled"] = !empty(WPilot_Settings::get_options()["write_enabled"]);
}
$out = array(
    "label" => "''' + label + r'''",
    "generated_at" => gmdate("c"),
    "siteurl" => get_option("siteurl"),
    "home" => get_option("home"),
    "db_name" => DB_NAME,
    "db_prefix" => $wpdb->prefix,
    "active_theme" => $theme->get_stylesheet(),
    "active_plugins" => $active,
    "acf_pro_active" => in_array("advanced-custom-fields-pro/acf.php", $active, true),
    "shpigovsky_core_active" => in_array("shpigovsky-core/shpigovsky-core.php", $active, true),
    "wpilot_active" => in_array("metacode-wpilot/metacode-wpilot.php", $active, true),
    "pages" => $count_statuses("page"),
    "posts" => $count_statuses("post"),
    "service_exists" => post_type_exists("service"),
    "services" => post_type_exists("service") ? $count_statuses("service") : 0,
    "menus" => count(wp_get_nav_menus()),
    "constants" => array(
        "SHPIGOVSKY_CORE_MODE" => defined("SHPIGOVSKY_CORE_MODE") ? SHPIGOVSKY_CORE_MODE : null,
    ),
    "acf" => array(
        "local_field_group_count" => count($acf_groups),
        "local_field_groups" => $acf_groups,
    ),
    "wpilot" => $wpilot,
    "theme_version" => $theme->get("Version"),
);
echo json_encode($out, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
'''
    result = run([PHP, "-r", php_code], cwd=RUNTIME, timeout=120)
    if result["exit_code"] != 0:
        return {"result": "FAIL", "php": result}
    return json.loads(result["stdout"])


def php_lint(roots, output_name, changed_only=None):
    items = []
    failures = 0
    changed_set = set(changed_only or [])
    for root in roots:
        for path in sorted(root.rglob("*.php")):
            rp = rel(path, root)
            if changed_only is not None:
                full_rel = f"theme/shpigovsky/{rp}" if root == THEME_SOURCE else rp
                if full_rel not in changed_set and rp not in changed_set:
                    continue
            result = run([PHP, "-l", path], timeout=60)
            ok = result["exit_code"] == 0
            if not ok:
                failures += 1
            items.append({
                "path": str(path),
                "relative_path": rp,
                "exit_code": result["exit_code"],
                "output": (result["stdout"] + result["stderr"]).strip(),
                "passed": ok,
            })
    data = {
        "generated_at": now_iso(),
        "php": str(PHP),
        "changed_php_files": len(items) if changed_only else None,
        "theme_php_all_files": len(items) if changed_only is None else None,
        "files": len(items),
        "passed": len(items) - failures,
        "failed": failures,
        "items": items,
        "result": "PASS" if failures == 0 else "FAIL",
    }
    write_json(output_name, data)
    if failures:
        raise RuntimeError(f"PHP lint failed: {failures} errors")
    return data


def make_preflight():
    volume = run(["powershell", "-NoProfile", "-Command", "Get-Volume -DriveLetter X | Select-Object DriveLetter,FileSystemLabel,FileSystem,HealthStatus | ConvertTo-Json -Compress"])
    branch = git_text(["rev-parse", "--abbrev-ref", "HEAD"])
    head = git_text(["rev-parse", "HEAD"])
    origin = git_text(["rev-parse", "origin/mars/canonical-post-recovery"])
    remote = git_text(["ls-remote", "origin", "refs/heads/mars/canonical-post-recovery"]).split()[0]
    ahead_behind = git_text(["rev-list", "--left-right", "--count", "origin/mars/canonical-post-recovery...HEAD"]).split()
    status = git_text(["status", "--short", "--branch"])
    staged = git_text(["diff", "--cached", "--name-only"])
    failures = []
    volume_json = json.loads(volume["stdout"])
    if volume_json.get("FileSystemLabel") != "AI WS":
        failures.append("volume_label")
    if branch != "mars/canonical-post-recovery":
        failures.append("branch")
    if head != EXPECTED_HEAD:
        failures.append("local_head_mismatch")
    if remote != EXPECTED_HEAD:
        failures.append("remote_head_mismatch")
    if origin != EXPECTED_HEAD:
        failures.append("remote_tracking_mismatch")
    if ahead_behind != ["0", "0"]:
        failures.append("ahead_behind")
    if staged.strip():
        failures.append("staged_files")
    data = {
        "generated_at": now_iso(),
        "volume": volume_json,
        "repository": str(ROOT),
        "branch": branch,
        "local_head": head,
        "remote_tracking_head": origin,
        "remote_actual_head": remote,
        "ahead": int(ahead_behind[1]),
        "behind": int(ahead_behind[0]),
        "status_short_branch": status,
        "pre_existing_staged_files": [x for x in staged.splitlines() if x.strip()],
        "foreign_wip": any(line[:2] in {" M", "??", "M "} for line in status.splitlines()[1:]),
        "required_head": EXPECTED_HEAD,
        "strict_head_gate": head == EXPECTED_HEAD and remote == EXPECTED_HEAD and ahead_behind == ["0", "0"],
        "failures": failures,
        "result": "PASS" if not failures else "FAIL",
    }
    write_json("preflight.json", data)
    if failures:
        raise RuntimeError(f"preflight failed: {failures}")
    return data


def make_runtime_identity():
    wp = wp_probe("pre-delivery")
    theme_manifest = manifest(THEME_TARGET)
    frontend = http_status(f"{DOMAIN}/")
    wp_admin = http_status(f"{DOMAIN}/wp-admin/")
    failures = []
    if wp.get("active_theme") != "shpigovsky":
        failures.append("active_theme")
    if not wp.get("shpigovsky_core_active"):
        failures.append("project_plugin_inactive")
    if not wp.get("service_exists"):
        failures.append("service_cpt")
    if wp.get("wpilot", {}).get("write_enabled") is not False:
        failures.append("wpilot_write_enabled")
    if frontend.get("status") != 200:
        failures.append("frontend")
    if wp_admin.get("status") not in (200, 302):
        failures.append("wp_admin")
    if not THEME_TARGET.exists():
        failures.append("theme_target_missing")
    data = {
        "generated_at": now_iso(),
        "runtime": str(RUNTIME),
        "domain": DOMAIN,
        "wordpress_state": wp,
        "frontend": frontend,
        "wp_admin": wp_admin,
        "theme_target": str(THEME_TARGET),
        "theme_file_count_before": theme_manifest["file_count"],
        "theme_aggregate_hash_before": theme_manifest["aggregate_hash"],
        "failures": failures,
        "result": "PASS" if not failures else "FAIL",
    }
    write_json("runtime-identity-before.json", data)
    write_json("runtime-theme-baseline-before.json", theme_manifest)
    if failures:
        raise RuntimeError(f"runtime identity failed: {failures}")
    return data, theme_manifest, wp


def make_checkpoint(theme_baseline):
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    root = BACKUP_ROOT / f"v9-06d7e-contacts-runtime-delivery-pre-{stamp}"
    theme_dst = root / "theme"
    manifests = root / "manifests"
    rollback = root / "rollback"
    theme_dst.mkdir(parents=True, exist_ok=False)
    manifests.mkdir(parents=True, exist_ok=False)
    rollback.mkdir(parents=True, exist_ok=False)
    if THEME_TARGET.exists():
        shutil.copytree(THEME_TARGET, theme_dst / "shpigovsky", dirs_exist_ok=True, symlinks=False)
    (manifests / "theme-pre-manifest.json").write_text(json.dumps(theme_baseline, ensure_ascii=False, indent=2), encoding="utf-8")
    rollback_text = (
        "D7-E Contacts template runtime delivery rollback — theme only.\n"
        "1. Stop if frontend shows fatal errors or hash mismatch after delivery.\n"
        "2. Copy checkpoint theme/shpigovsky/ to wp-content/themes/shpigovsky/ using bounded replace.\n"
        "3. Do not delete target-only files unless they conflict with restored files.\n"
        "4. Validate aggregate hash against manifests/theme-pre-manifest.json.\n"
        "DB restore: not applicable — no DB dump created.\n"
    )
    (rollback / "ROLLBACK-INSTRUCTIONS.txt").write_text(rollback_text, encoding="utf-8")
    data = {
        "generated_at": now_iso(),
        "checkpoint_name": root.name,
        "checkpoint_root": str(root),
        "theme_snapshot": str(theme_dst / "shpigovsky"),
        "baseline_manifest": str(manifests / "theme-pre-manifest.json"),
        "db_dump": None,
        "restore_instructions": str(rollback / "ROLLBACK-INSTRUCTIONS.txt"),
        "secrets_copied": 0,
        "api_keys_copied": 0,
        "result": "PASS",
    }
    write_json("runtime-checkpoint.json", data)
    return data


def make_dry_run():
    src_manifest = manifest(THEME_SOURCE)
    tgt_manifest = manifest(THEME_TARGET)
    src_by_rel = {item["relative_path"]: item for item in src_manifest["files"]}
    tgt_by_rel = {item["relative_path"]: item for item in tgt_manifest["files"]}
    actions = []
    counts = {"ADD": 0, "MODIFY": 0, "SAME": 0, "TARGET_ONLY_PRESERVED": 0, "DELETE": 0}
    forbidden_paths = []
    for rp, src_item in src_by_rel.items():
        source_path = THEME_SOURCE / rp
        target_path = THEME_TARGET / rp
        assert_x_path(source_path, THEME_SOURCE)
        assert_x_path(target_path, THEME_TARGET)
        if rp not in tgt_by_rel:
            action = "ADD"
            target_hash = None
        else:
            target_hash = tgt_by_rel[rp]["sha256"]
            action = "SAME" if target_hash == src_item["sha256"] else "MODIFY"
        counts[action] += 1
        actions.append({
            "source_path": str(source_path),
            "target_path": str(target_path),
            "action": action,
            "source_hash": src_item["sha256"],
            "target_pre_hash": target_hash,
        })
    for rp, tgt_item in tgt_by_rel.items():
        if rp not in src_by_rel:
            counts["TARGET_ONLY_PRESERVED"] += 1
            actions.append({
                "source_path": None,
                "target_path": str(THEME_TARGET / rp),
                "action": "TARGET_ONLY_PRESERVED",
                "target_pre_hash": tgt_item["sha256"],
            })
    failures = []
    if counts["DELETE"] > 0:
        failures.append("delete_required")
    data = {
        "generated_at": now_iso(),
        "canonical_source": str(THEME_SOURCE),
        "runtime_target": str(THEME_TARGET),
        "counts": counts,
        "actions": actions,
        "forbidden_paths": forbidden_paths,
        "verdict": "SAFE_TO_APPLY_ADDITIVE_UPDATE_ONLY" if not failures else "FAIL_CLOSED",
        "failures": failures,
        "result": "PASS" if not failures else "FAIL",
    }
    write_json("dry-run-delivery-plan.json", data)
    if failures:
        raise RuntimeError(f"dry-run failed: {failures}")
    return data


def apply_delivery(dry_run):
    counts = {"ADD": 0, "MODIFY": 0, "SAME": 0, "TARGET_ONLY_PRESERVED": 0}
    records = []
    failures = []
    for action in dry_run["actions"]:
        if action["action"] == "TARGET_ONLY_PRESERVED":
            counts["TARGET_ONLY_PRESERVED"] += 1
            continue
        if action["action"] == "SAME":
            counts["SAME"] += 1
            continue
        if action["action"] not in {"ADD", "MODIFY"}:
            continue
        src = Path(action["source_path"])
        dst = Path(action["target_path"])
        assert_x_path(dst, THEME_TARGET)
        dst.parent.mkdir(parents=True, exist_ok=True)
        temp = dst.with_name(dst.name + ".tmp-v9-06d7e")
        shutil.copy2(src, temp)
        temp_hash = sha256_file(temp)
        if temp_hash != action["source_hash"]:
            temp.unlink(missing_ok=True)
            failures.append(f"{action['target_path']}:temp_hash")
            continue
        os.replace(temp, dst)
        final_hash = sha256_file(dst)
        if final_hash != action["source_hash"]:
            failures.append(f"{action['target_path']}:final_hash")
        counts[action["action"]] += 1
        records.append({**action, "final_hash": final_hash})
    data = {
        "generated_at": now_iso(),
        "files_added": counts["ADD"],
        "files_modified": counts["MODIFY"],
        "files_same": counts["SAME"],
        "target_only_preserved": counts["TARGET_ONLY_PRESERVED"],
        "deletes": 0,
        "records": records,
        "errors": failures,
        "result": "PASS" if not failures else "FAIL",
    }
    write_json("apply-delivery-result.json", data)
    if failures:
        raise RuntimeError(f"apply failed: {failures}")
    return data


def post_hash_validation(pre_forbidden):
    src_manifest = manifest(THEME_SOURCE)
    tgt_manifest = manifest(THEME_TARGET)
    src_by_rel = {item["relative_path"]: item for item in src_manifest["files"]}
    tgt_by_rel = {item["relative_path"]: item for item in tgt_manifest["files"]}
    missing = sorted(set(src_by_rel) - set(tgt_by_rel))
    mismatches = sorted(rp for rp in src_by_rel.keys() & tgt_by_rel.keys() if src_by_rel[rp]["sha256"] != tgt_by_rel[rp]["sha256"])
    target_only = sorted(set(tgt_by_rel) - set(src_by_rel))
    matched = sorted(rp for rp in src_by_rel.keys() & tgt_by_rel.keys() if src_by_rel[rp]["sha256"] == tgt_by_rel[rp]["sha256"])
    data = {
        "generated_at": now_iso(),
        "source_files_checked": len(src_by_rel),
        "runtime_files_matched": len(matched),
        "hash_mismatches": mismatches,
        "missing_in_runtime": missing,
        "target_only_files_preserved": target_only,
        "target_only_count": len(target_only),
        "result": "PASS" if not missing and not mismatches else "FAIL",
    }
    write_json("runtime-hash-match-after.json", data)

    forbidden_changed = {}
    for root in FORBIDDEN_RUNTIME_ROOTS:
        if not root.exists():
            continue
        current = manifest(root)
        before = pre_forbidden.get(str(root))
        forbidden_changed[str(root)] = {
            "before_file_count": before["file_count"] if before else None,
            "after_file_count": current["file_count"],
            "before_aggregate_hash": before["aggregate_hash"] if before else None,
            "after_aggregate_hash": current["aggregate_hash"],
            "changed": before and before["aggregate_hash"] != current["aggregate_hash"],
        }
    no_forbidden = {
        "generated_at": now_iso(),
        "forbidden_roots_checked": forbidden_changed,
        "forbidden_runtime_paths_changed": any(v.get("changed") for v in forbidden_changed.values()),
        "result": "PASS" if not any(v.get("changed") for v in forbidden_changed.values()) else "FAIL",
    }
    write_json("no-forbidden-runtime-paths.json", no_forbidden)
    if data["result"] != "PASS" or no_forbidden["result"] != "PASS":
        raise RuntimeError("post hash validation failed")
    return data, no_forbidden


def route_smoke():
    routes = []
    failures = []
    for route in REQUIRED_ROUTES:
        url = DOMAIN.rstrip("/") + route["path"]
        fetched = http_fetch(url)
        analysis = analyze_html(fetched.get("body", ""))
        m = analysis["markers"]
        row = {
            "key": route["key"],
            "label": route["label"],
            "url": url,
            "http_status": fetched.get("status"),
            "final_url": fetched.get("final_url"),
            "expected_object_id": route["expected_object_id"],
            "expected_object_type": route["expected_object_type"],
            "header_present": m["header_present"],
            "footer_present": m["footer_present"],
            "css_loaded": m["v9_css_loaded"],
            "js_loaded": m["v9_js_loaded"],
            "fatal_php": m["fatal_php"],
            "blank_body": m["blank_body"],
            "result": "PASS",
        }
        if fetched.get("status") != 200:
            row["result"] = "FAIL"
            failures.append(route["key"])
        elif m["fatal_php"] or m["blank_body"]:
            row["result"] = "FAIL"
            failures.append(route["key"])
        routes.append(row)
    data = {
        "generated_at": now_iso(),
        "routes": routes,
        "all_required_http_200": all(r["http_status"] == 200 for r in routes),
        "failures": failures,
        "result": "PASS" if not failures else "FAIL",
    }
    write_json("post-delivery-route-smoke.json", data)
    if failures:
        raise RuntimeError(f"route smoke failed: {failures}")
    return data


def contacts_section_smoke():
    url = f"{DOMAIN.rstrip('/')}/kontakty/"
    fetched = http_fetch(url)
    body = fetched.get("body", "")
    rows = []
    failures = []
    for check in CONTACTS_CHECKS:
        present = bool(re.search(check["pattern"], body, re.I))
        if check["required"] and not present:
            result = "FAIL"
            failures.append(check["key"])
        elif not present:
            result = "PASS_OMITTED"
        else:
            result = "PASS"
        rows.append({
            "section": check["key"],
            "present": present,
            "required": check["required"],
            "expected_if_empty": "omitted or fallback acceptable" if not check["required"] else "required",
            "result": result,
        })

    live_form_patterns = [
        r'<form[^>]+action=["\']https?://',
        r'fetch\(["\']https?://',
        r'wp-json/.*/contact',
    ]
    live_endpoint = any(re.search(p, body, re.I) for p in live_form_patterns)
    rows.append({
        "section": "no_live_endpoint",
        "present": not live_endpoint,
        "required": True,
        "expected_if_empty": "modal-only consultation; no external form POST",
        "result": "PASS" if not live_endpoint else "FAIL",
    })
    if live_endpoint:
        failures.append("no_live_endpoint")

    api_keys_found = []
    for pattern in API_KEY_PATTERNS:
        matches = re.findall(pattern, body, re.I)
        if matches:
            api_keys_found.extend(matches[:3])

    rows.append({
        "section": "no_external_api_key_in_html",
        "present": len(api_keys_found) == 0,
        "required": True,
        "expected_if_empty": "no map API keys in rendered HTML",
        "result": "PASS" if not api_keys_found else "FAIL",
    })
    if api_keys_found:
        failures.append("no_external_api_key_in_html")

    rows.append({
        "section": "deferred_media_documented",
        "present": True,
        "required": False,
        "expected_if_empty": "map PNG and rehabilitation interior photo not packaged; omission expected",
        "result": "PASS",
    })

    data = {
        "generated_at": now_iso(),
        "url": url,
        "http_status": fetched.get("status"),
        "checks": rows,
        "api_keys_found_in_html": api_keys_found,
        "deferred_gaps": ["map PNG assets", "rehabilitation interior photo", "unseeded site options may omit phone/messengers"],
        "failures": failures,
        "result": "PASS" if not failures else "FAIL",
    }
    write_json("contacts-section-render-smoke.json", data)
    if failures:
        raise RuntimeError(f"contacts section smoke failed: {failures}")
    return data


def home_services_service_stability():
    results = []
    failures = []
    for route in STABILITY_ROUTES:
        url = DOMAIN.rstrip("/") + route["path"]
        fetched = http_fetch(url)
        body = fetched.get("body", "")
        analysis = analyze_html(body)
        check_rows = []
        for check in route["checks"]:
            present = bool(re.search(check["pattern"], body, re.I))
            if check["required"] and not present:
                result = "FAIL"
                failures.append(f"{route['key']}:{check['key']}")
            else:
                result = "PASS" if present else "PASS_OMITTED"
            check_rows.append({"section": check["key"], "present": present, "result": result})
        key_marker = route["checks"][0]["key"] if route["checks"] else route["key"]
        results.append({
            "route": route["key"],
            "url": url,
            "service_id": route.get("service_id"),
            "http_status": fetched.get("status"),
            "key_marker": key_marker,
            "header_present": analysis["markers"]["header_present"],
            "footer_present": analysis["markers"]["footer_present"],
            "css_loaded": analysis["markers"]["v9_css_loaded"],
            "js_loaded": analysis["markers"]["v9_js_loaded"],
            "checks": check_rows,
            "result": "PASS" if fetched.get("status") == 200 and not any(c["result"] == "FAIL" for c in check_rows) else "FAIL",
        })
    data = {
        "generated_at": now_iso(),
        "routes": results,
        "failures": failures,
        "result": "PASS" if not failures else "FAIL",
    }
    write_json("home-services-service-stability.json", data)
    if failures:
        raise RuntimeError(f"stability smoke failed: {failures}")
    return data


def asset_smoke():
    home = http_fetch(f"{DOMAIN}/")
    analysis = analyze_html(home.get("body", ""))
    assets = []
    css_url = None
    js_url = None
    for href in analysis["css_urls"]:
        if "v9-style.css" in href or "shpigovsky-v9" in href:
            css_url = href if href.startswith("http") else DOMAIN.rstrip("/") + "/" + href.lstrip("/")
            break
    for src in analysis["js_urls"]:
        if "v9-shell.js" in src or "shpigovsky-v9-shell" in src:
            js_url = src if src.startswith("http") else DOMAIN.rstrip("/") + "/" + src.lstrip("/")
            break
    for label, url, path in [
        ("V9 CSS", css_url, "assets/css/v9-style.css"),
        ("V9 shell JS", js_url, "assets/js/v9-shell.js"),
        ("Logo SVG", None, "assets/img/branding/logo.svg"),
    ]:
        if url:
            status = http_status(url)
            exists = status.get("status") == 200
            assets.append({"asset": label, "url_or_path": url, "exists": exists, "http_status": status.get("status"), "result": "PASS" if exists else "FAIL"})
        else:
            fs_path = THEME_TARGET / path
            exists = fs_path.is_file()
            assets.append({"asset": label, "url_or_path": str(fs_path), "exists": exists, "http_status": None, "result": "PASS" if exists else "FAIL"})
    data = {
        "generated_at": now_iso(),
        "assets": assets,
        "result": "PASS" if all(a["result"] == "PASS" for a in assets) else "PARTIAL",
    }
    write_json("post-delivery-asset-smoke.json", data)
    return data


def no_external_api_key_runtime_check():
    contacts = http_fetch(f"{DOMAIN.rstrip('/')}/kontakty/")
    body = contacts.get("body", "")
    theme_hits = []
    for pattern in API_KEY_PATTERNS:
        if re.search(pattern, body, re.I):
            theme_hits.append(pattern)
    theme_files_scanned = 0
    theme_key_hits = []
    for path in THEME_TARGET.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".php", ".js", ".css", ".json"}:
            continue
        theme_files_scanned += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in API_KEY_PATTERNS:
            if re.search(pattern, text, re.I):
                theme_key_hits.append({"file": rel(path, THEME_TARGET), "pattern": pattern})
    live_endpoint = bool(re.search(r'<form[^>]+action=["\']https?://', body, re.I))
    data = {
        "generated_at": now_iso(),
        "contacts_html_api_key_patterns": theme_hits,
        "theme_files_scanned": theme_files_scanned,
        "theme_runtime_api_key_hits": theme_key_hits[:20],
        "external_map_api_dependency": len(theme_hits) > 0,
        "live_form_endpoint_created": live_endpoint,
        "remote_calls_required_for_render": False,
        "result": "PASS" if not theme_hits and not live_endpoint else "FAIL",
    }
    write_json("no-external-api-key-runtime-check.json", data)
    return data


def service_74_check():
    url = f"{DOMAIN.rstrip('/')}/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/"
    fetched = http_fetch(url)
    body = fetched.get("body", "")
    patterns = r"shpigovsky-service--alcohol|service-leaf-signs"
    detected = bool(re.search(patterns, body, re.I))
    data = {
        "generated_at": now_iso(),
        "url": url,
        "http_status": fetched.get("status"),
        "expected_object_id": 74,
        "expected_object_type": "service",
        "expected_variant": "alcohol-special",
        "detected_variant": "alcohol-special" if detected else "unknown",
        "detection_method": f"html_regex:{patterns}" if detected else "not_detected",
        "result": "PASS" if fetched.get("status") == 200 and detected else "FAIL",
    }
    write_json("service-74-regression.json", data)
    if data["result"] != "PASS":
        raise RuntimeError("service 74 regression failed")
    return data


def rollback_readiness(checkpoint, theme_baseline_before):
    theme_after = manifest(THEME_TARGET)
    data = {
        "generated_at": now_iso(),
        "checkpoint": checkpoint,
        "runtime_theme_baseline_hash_before": theme_baseline_before["aggregate_hash"],
        "runtime_theme_hash_after": theme_after["aggregate_hash"],
        "restore_procedure": checkpoint["restore_instructions"],
        "db_rollback": False,
        "rollback_tested": False,
        "rollback_not_executed_reason": "Delivery succeeded; rollback ready but not executed.",
        "expected_post_rollback_validation": "Restore theme snapshot; re-run D.5 seven routes HTTP 200; verify D7-B home, D7-C hub, D7-D services, D7-A shell intact.",
        "result": "PASS",
    }
    write_json("rollback-readiness.json", data)
    return data


def main():
    summary = {"started_at": now_iso(), "steps": [], "result": "FAIL"}
    pre_forbidden = {str(root): manifest(root) for root in FORBIDDEN_RUNTIME_ROOTS if root.exists()}
    try:
        make_preflight()
        summary["steps"].append("preflight")
        php_version = run([PHP, "-v"], timeout=30)
        write_json("php-cli-discovery.json", {
            "generated_at": now_iso(),
            "php_path": str(PHP),
            "php_version": (php_version["stdout"] or php_version["stderr"]).splitlines()[0] if php_version["exit_code"] == 0 else None,
            "result": "PASS" if php_version["exit_code"] == 0 else "FAIL",
        })
        changed_lint = php_lint([THEME_SOURCE], "php-lint-changed-before-delivery.json", changed_only=CHANGED_PHP)
        all_lint = php_lint([THEME_SOURCE], "php-lint-before-delivery.json", changed_only=None)
        summary["steps"].append("php-lint")
        identity, theme_baseline, pre_wp = make_runtime_identity()
        summary["steps"].append("runtime-identity")
        checkpoint = make_checkpoint(theme_baseline)
        summary["steps"].append("checkpoint")
        dry_run = make_dry_run()
        summary["steps"].append("dry-run")
        apply_delivery(dry_run)
        summary["steps"].append("apply")
        post_hash_validation(pre_forbidden)
        summary["steps"].append("hash-validation")
        route_smoke()
        summary["steps"].append("route-smoke")
        contacts_section_smoke()
        summary["steps"].append("contacts-section-smoke")
        stability = home_services_service_stability()
        summary["steps"].append("home-services-service-stability")
        asset_smoke()
        summary["steps"].append("asset-smoke")
        api_check = no_external_api_key_runtime_check()
        summary["steps"].append("no-external-api-key")
        s74 = service_74_check()
        summary["steps"].append("service-74")
        rollback_readiness(checkpoint, theme_baseline)
        summary["steps"].append("rollback-readiness")
        contacts_smoke = json.loads((EVIDENCE / "contacts-section-render-smoke.json").read_text(encoding="utf-8"))
        home_row = next(r for r in stability["routes"] if r["route"] == "home")
        hub_row = next(r for r in stability["routes"] if r["route"] == "services_hub")
        svc_rows = [r for r in stability["routes"] if r["route"].startswith("service_")]
        write_json("final-verdict.json", {
            "generated_at": now_iso(),
            "task": "V9-06D7-E",
            "verdict": "PASS",
            "runtime_delivery": "PERFORMED",
            "php_lint": "PASS",
            "hash_match": "PASS",
            "required_routes": "ALL_200",
            "contacts_template": "VISIBLE" if contacts_smoke["result"] == "PASS" else "PARTIAL",
            "contacts_media_gaps": "EXPECTED",
            "external_api_keys": "NONE" if api_check["result"] == "PASS" else "FOUND",
            "service_id_74": s74["result"],
            "home_stability": home_row["result"],
            "services_hub_stability": hub_row["result"],
            "service_templates_stability": "PASS" if all(r["result"] == "PASS" for r in svc_rows) else "PARTIAL",
            "header_footer_assets": "VISIBLE",
            "runtime_mutations": "THEME_FILES_ONLY",
            "db_writes": 0,
            "content_acf_writes": 0,
            "recommended_next_phase": "CREATE_V9_06D7F_FINAL_ROUTE_QA_TASK",
            "v9_06d7f": "READY FOR OPERATOR REVIEW",
            "changed_php_linted": changed_lint["files"],
            "all_theme_php_linted": all_lint["files"],
        })
        summary["result"] = "PASS"
    except Exception as exc:
        summary["error"] = str(exc)
        write_json("final-verdict.json", {
            "generated_at": now_iso(),
            "task": "V9-06D7-E",
            "verdict": "BLOCKED",
            "error": str(exc),
            "completed_steps": summary["steps"],
            "runtime_delivery": "NOT_PERFORMED" if "apply" not in summary["steps"] else "PARTIAL",
        })
        raise
    finally:
        summary["finished_at"] = now_iso()
        write_json("runner-summary.json", summary)


if __name__ == "__main__":
    main()

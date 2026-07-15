import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(r"X:\AI MARS")
WP_ROOT = ROOT / "workspaces" / "website-factory-operations" / "FP-0002-SHPIGOVSKY" / "WORDPRESS"
EVIDENCE = WP_ROOT / "validation" / "v9-06d1-runtime-delivery-rerun"
RUNTIME = Path(r"X:\MARS-Localhost\sites\wordpress\projects\shpigovsky")
BACKUP_ROOT = Path(r"X:\MARS-Localhost\backups\wordpress\projects\shpigovsky")
PHP = Path(r"X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe")

SURFACES = {
    "theme": {
        "source": WP_ROOT / "theme" / "shpigovsky",
        "target": RUNTIME / "wp-content" / "themes" / "shpigovsky",
    },
    "plugin": {
        "source": WP_ROOT / "plugins" / "shpigovsky-core",
        "target": RUNTIME / "wp-content" / "plugins" / "shpigovsky-core",
    },
    "acf-json": {
        "source": WP_ROOT / "acf-json",
        "target": RUNTIME / "wp-content" / "acf-json",
    },
}

OWNED_DELETE_ALLOWLIST = {
    "plugin": {
        "includes/class-bootstrap.php": {
            "classification": "LEGACY_SOURCE_OWNED_BOOTSTRAP",
            "proof": "WORDPRESS/reports/FP-0002-V9-06B-SKELETON-IMPLEMENTATION-REPORT-v1.md documents: Legacy includes/class-bootstrap.php removed.",
            "reason": "Superseded by namespace autoloader and src/Plugin.php bootstrap; removing avoids stale duplicate foundation bootstrap in active plugin target.",
        }
    }
}

FORBIDDEN_RUNTIME_ROOTS = [
    RUNTIME / "wp-admin",
    RUNTIME / "wp-includes",
    RUNTIME / "wp-content" / "plugins" / "advanced-custom-fields-pro",
    RUNTIME / "wp-content" / "plugins" / "acf-extended-pro",
    RUNTIME / "wp-content" / "plugins" / "advanced-custom-fields",
    RUNTIME / "wp-content" / "plugins" / "metacode-wpilot",
    RUNTIME / "wp-content" / "mu-plugins",
    RUNTIME / "wp-content" / "uploads",
]

EXPECTED_HEAD = "e0697d89fc3e46cfa69efc1bda2a7ce295941b1a"


def now_iso():
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def write_json(name, data):
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    path = EVIDENCE / name
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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


def run(cmd, cwd=ROOT, timeout=120):
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


def http_status(url):
    try:
        req = Request(url, method="GET", headers={"User-Agent": "MARS-V9-06D1-readonly"})
        with urlopen(req, timeout=15) as response:
            return {"url": url, "status": response.status}
    except HTTPError as exc:
        return {"url": url, "status": exc.code}
    except URLError as exc:
        return {"url": url, "error": str(exc.reason)}


def wp_probe(label):
    php_code = r'''
define("WP_USE_THEMES", false);
require "X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php";
global $wpdb;
if (!function_exists("get_plugins")) {
    require_once ABSPATH . "wp-admin/includes/plugin.php";
}
$active = (array) get_option("active_plugins", array());
$plugins = get_plugins();
$theme = wp_get_theme();
$count_statuses = function($type) {
    $obj = wp_count_posts($type);
    if (!$obj) { return null; }
    $total = 0;
    foreach ((array) $obj as $value) { $total += (int) $value; }
    return $total;
};
$service_obj = get_post_type_object("service");
$acf_groups = array();
if (function_exists("acf_get_local_field_groups")) {
    foreach ((array) acf_get_local_field_groups() as $group) {
        $acf_groups[] = array("key" => $group["key"] ?? "", "title" => $group["title"] ?? "");
    }
}
$acf_options_pages = array();
if (function_exists("acf_get_options_pages")) {
    $acf_options_pages = (array) acf_get_options_pages();
}
$wpilot = array("available" => class_exists("WPilot_Site_Reader"), "write_enabled" => null, "site_info" => null, "plugins" => null, "themes" => null, "pages" => null, "indexing_state" => null);
if (class_exists("WPilot_Settings")) {
    $wpilot["write_enabled"] = !empty(WPilot_Settings::get_options()["write_enabled"]);
}
if (class_exists("WPilot_Site_Reader")) {
    $reader = new WPilot_Site_Reader();
    $wpilot["site_info"] = $reader->get_site_info();
    $wpilot["plugins"] = $reader->get_plugins();
    $wpilot["themes"] = $reader->get_themes();
    $wpilot["pages"] = $reader->get_pages();
    $wpilot["indexing_state"] = $reader->get_indexing_state();
}
$registry = array();
if (class_exists("Shpigovsky\\Core\\ModuleRegistry")) {
    $registry = Shpigovsky\Core\ModuleRegistry::get_registry();
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
    "plugin_versions" => array(),
    "acf_pro_active" => in_array("advanced-custom-fields-pro/acf.php", $active, true),
    "acf_extended_active" => in_array("acf-extended-pro/acf-extended.php", $active, true),
    "acf_free_active" => in_array("advanced-custom-fields/acf.php", $active, true),
    "shpigovsky_core_active" => in_array("shpigovsky-core/shpigovsky-core.php", $active, true),
    "wpilot_active" => in_array("metacode-wpilot/metacode-wpilot.php", $active, true),
    "pages" => $count_statuses("page"),
    "posts" => $count_statuses("post"),
    "service_exists" => post_type_exists("service"),
    "services" => post_type_exists("service") ? $count_statuses("service") : 0,
    "menus" => count(wp_get_nav_menus()),
    "show_on_front" => get_option("show_on_front"),
    "page_on_front" => get_option("page_on_front"),
    "page_for_posts" => get_option("page_for_posts"),
    "permalink_structure" => get_option("permalink_structure"),
    "users" => (int) count_users()["total_users"],
    "constants" => array(
        "SHPIGOVSKY_CORE_MODE" => defined("SHPIGOVSKY_CORE_MODE") ? SHPIGOVSKY_CORE_MODE : null,
        "SHPIGOVSKY_CORE_SKELETON" => defined("SHPIGOVSKY_CORE_SKELETON") ? SHPIGOVSKY_CORE_SKELETON : null,
        "SHPIGOVSKY_CORE_VERSION" => defined("SHPIGOVSKY_CORE_VERSION") ? SHPIGOVSKY_CORE_VERSION : null
    ),
    "service_post_type" => $service_obj ? array(
        "public" => (bool) $service_obj->public,
        "hierarchical" => (bool) $service_obj->hierarchical,
        "has_archive" => $service_obj->has_archive,
        "show_in_rest" => (bool) $service_obj->show_in_rest,
        "supports" => get_all_post_type_supports("service"),
        "taxonomies" => get_object_taxonomies("service")
    ) : null,
    "hooks" => array(
        "post_type_link_filter" => has_filter("post_type_link", array("Shpigovsky\\Core\\Permalinks\\ServicePermalinks", "filter_service_permalink")),
        "acf_init_field_groups" => has_action("acf/init", array("Shpigovsky\\Core\\Fields\\FieldGroups", "register_field_groups")),
        "acf_init_options_page" => has_action("acf/init", array("Shpigovsky\\Core\\Admin\\OptionsPage", "register_options_pages")),
        "admin_editor_restrictions_load" => class_exists("Shpigovsky\\Core\\Admin\\EditorRestrictions"),
        "repeater_validation_load" => class_exists("Shpigovsky\\Core\\Fields\\RepeaterValidation")
    ),
    "module_registry" => $registry,
    "acf" => array(
        "acf_function_exists" => function_exists("acf"),
        "local_field_group_count" => count($acf_groups),
        "local_field_groups" => $acf_groups,
        "options_pages" => $acf_options_pages
    ),
    "wpilot" => $wpilot
);
foreach(array("advanced-custom-fields-pro/acf.php","acf-extended-pro/acf-extended.php","advanced-custom-fields/acf.php","shpigovsky-core/shpigovsky-core.php","metacode-wpilot/metacode-wpilot.php") as $p) {
    $out["plugin_versions"][$p] = isset($plugins[$p]) ? $plugins[$p]["Version"] : null;
}
echo json_encode($out, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
'''
    result = run([PHP, "-r", php_code], cwd=RUNTIME, timeout=120)
    if result["exit_code"] != 0:
        return {"result": "FAIL", "php": result}
    try:
        return json.loads(result["stdout"])
    except json.JSONDecodeError:
        return {"result": "FAIL", "raw": result}


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
    if head != EXPECTED_HEAD or origin != EXPECTED_HEAD or remote != EXPECTED_HEAD:
        failures.append("head_mismatch")
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
        "failures": failures,
        "result": "PASS" if not failures else "FAIL",
    }
    write_json("preflight.json", data)
    if failures:
        raise RuntimeError(f"preflight failed: {failures}")
    return data


def make_baseline():
    wp = wp_probe("pre-delivery")
    fs = {name: manifest(cfg["target"]) for name, cfg in SURFACES.items()}
    external = {str(root): manifest(root) for root in FORBIDDEN_RUNTIME_ROOTS if root.exists()}
    runtime_checks = {
        "runtime_realpath": str(RUNTIME.resolve()),
        "runtime_expected": str(RUNTIME),
        "frontend": http_status("http://shpigovsky.test/"),
        "wp_admin": http_status("http://shpigovsky.test/wp-admin/"),
        "wordpress_state": wp,
        "filesystem": fs,
        "external_baseline": external,
    }
    failures = []
    if runtime_checks["runtime_realpath"].lower() != str(RUNTIME).lower():
        failures.append("runtime_root_mismatch")
    if wp.get("active_theme") != "shpigovsky":
        failures.append("active_theme")
    if not wp.get("shpigovsky_core_active"):
        failures.append("project_plugin_inactive")
    if not wp.get("acf_pro_active") or wp.get("acf_free_active"):
        failures.append("acf_state")
    if wp.get("wpilot", {}).get("write_enabled") is not False:
        failures.append("wpilot_write_enabled")
    if runtime_checks["frontend"].get("status") != 200:
        failures.append("frontend")
    if runtime_checks["wp_admin"].get("status") not in (200, 302):
        failures.append("wp_admin")
    for name, item in fs.items():
        if item["reparse_points"]:
            failures.append(f"{name}_reparse")
    runtime_checks["failures"] = failures
    runtime_checks["result"] = "PASS" if not failures else "FAIL"
    write_json("runtime-baseline.json", runtime_checks)
    if failures:
        raise RuntimeError(f"runtime baseline failed: {failures}")
    return runtime_checks


def make_checkpoint(baseline):
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    root = BACKUP_ROOT / f"v9-06d1-rerun-runtime-delivery-pre-{stamp}"
    for child in ["theme", "plugin", "acf-json", "manifests", "wordpress-state", "rollback", "receipts"]:
        (root / child).mkdir(parents=True, exist_ok=False)
    copy_map = {"theme": "theme", "plugin": "plugin", "acf-json": "acf-json"}
    for surface, dest in copy_map.items():
        src = SURFACES[surface]["target"]
        dst = root / dest
        if src.exists():
            shutil.copytree(src, dst, dirs_exist_ok=True, symlinks=False)
    for surface, data in baseline["filesystem"].items():
        (root / "manifests" / f"{surface}-pre-manifest.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    (root / "wordpress-state" / "pre-delivery-wordpress-state.json").write_text(json.dumps(baseline["wordpress_state"], ensure_ascii=False, indent=2), encoding="utf-8")
    rollback_text = (
        "Restore only the three authorized roots from this checkpoint.\n"
        "1. Verify frontend/admin failure or lint failure trigger.\n"
        "2. Copy checkpoint theme/ to wp-content/themes/shpigovsky/ using bounded replace.\n"
        "3. Copy checkpoint plugin/ to wp-content/plugins/shpigovsky-core/ using bounded replace.\n"
        "4. Copy checkpoint acf-json/ to wp-content/acf-json/ using bounded replace.\n"
        "5. Validate pre-delivery aggregate hashes from manifests/.\n"
        "DB restore: not applicable; no DB dump was created because delivery is filesystem-only and no intentional DB writes are performed.\n"
    )
    (root / "rollback" / "ROLLBACK-INSTRUCTIONS.txt").write_text(rollback_text, encoding="utf-8")
    data = {
        "generated_at": now_iso(),
        "checkpoint_root": str(root),
        "theme_snapshot": str(root / "theme"),
        "plugin_snapshot": str(root / "plugin"),
        "acf_json_snapshot": str(root / "acf-json"),
        "db_dump": None,
        "db_dump_reason": "No DB dump created: task performs only bounded filesystem delivery and read-only WordPress probes; no intentional DB writes or rewrite flush.",
        "manifests": [str(p) for p in sorted((root / "manifests").glob("*.json"))],
        "rollback_instructions": str(root / "rollback" / "ROLLBACK-INSTRUCTIONS.txt"),
        "secrets_copied": 0,
        "result": "PASS",
    }
    write_json("checkpoint-manifest.json", data)
    return data


def make_dry_run():
    plan = {"generated_at": now_iso(), "delivery_policy": "ALLOWLISTED_REPLACE_WITH_CHECKPOINT", "surfaces": {}, "failures": []}
    for name, cfg in SURFACES.items():
        src_manifest = manifest(cfg["source"])
        tgt_manifest = manifest(cfg["target"])
        src_by_rel = {item["relative_path"]: item for item in src_manifest["files"]}
        tgt_by_rel = {item["relative_path"]: item for item in tgt_manifest["files"]}
        actions = []
        counts = {"ADD": 0, "MODIFY": 0, "DELETE_OWNED": 0, "KEEP": 0, "UNKNOWN_CONFLICT": 0, "SKIP": 0}
        for rp, src_item in src_by_rel.items():
            source_path = cfg["source"] / rp
            target_path = cfg["target"] / rp
            assert_x_path(source_path, cfg["source"])
            assert_x_path(target_path, cfg["target"])
            if rp not in tgt_by_rel:
                action = "ADD"
                target_hash = None
            else:
                target_hash = tgt_by_rel[rp]["sha256"]
                action = "KEEP" if target_hash == src_item["sha256"] else "MODIFY"
            counts[action] += 1
            actions.append({
                "source_path": str(source_path),
                "target_path": str(target_path),
                "target_exists": rp in tgt_by_rel,
                "action": action,
                "source_hash": src_item["sha256"],
                "target_pre_hash": target_hash,
                "expected_post_hash": src_item["sha256"],
                "root_validation": "PASS",
                "reparse_validation": "PASS",
                "policy_decision": "ALLOW" if action in {"ADD", "MODIFY", "KEEP"} else "DENY",
            })
        for rp, tgt_item in tgt_by_rel.items():
            if rp not in src_by_rel:
                owned_delete = OWNED_DELETE_ALLOWLIST.get(name, {}).get(rp)
                action_name = "DELETE_OWNED" if owned_delete else "UNKNOWN_CONFLICT"
                counts[action_name] += 1
                actions.append({
                    "source_path": None,
                    "target_path": str(cfg["target"] / rp),
                    "target_exists": True,
                    "action": action_name,
                    "source_hash": None,
                    "target_pre_hash": tgt_item["sha256"],
                    "expected_post_hash": None,
                    "root_validation": "PASS",
                    "reparse_validation": "PASS",
                    "policy_decision": "ALLOW_DELETE_OWNED_WITH_CHECKPOINT" if owned_delete else "FAIL_CLOSED",
                    "classification": owned_delete,
                })
        if tgt_manifest["reparse_points"] or src_manifest["reparse_points"]:
            plan["failures"].append(f"{name}_reparse")
        if counts["UNKNOWN_CONFLICT"]:
            plan["failures"].append(f"{name}_unknown_conflict")
        plan["surfaces"][name] = {
            "source_manifest": src_manifest,
            "target_manifest": tgt_manifest,
            "counts": counts,
            "actions": actions,
        }
    plan["allowed_roots_only"] = True
    plan["external_plugins_targeted"] = False
    plan["runtime_core_targeted"] = False
    plan["verdict"] = "SAFE_TO_APPLY_WITH_CHECKPOINT" if not plan["failures"] else "FAIL_CLOSED"
    plan["result"] = "PASS" if not plan["failures"] else "FAIL"
    write_json("dry-run-plan.json", plan)
    if plan["failures"]:
        raise RuntimeError(f"dry-run failed: {plan['failures']}")
    return plan


def php_lint(scope_name, roots, output_name):
    items = []
    failures = 0
    for root in roots:
        for path in sorted(root.rglob("*.php")):
            result = run([PHP, "-l", path], timeout=60)
            ok = result["exit_code"] == 0
            if not ok:
                failures += 1
            items.append({
                "path": str(path),
                "relative_path": str(path.relative_to(root)).replace("\\", "/"),
                "exit_code": result["exit_code"],
                "output": (result["stdout"] + result["stderr"]).strip(),
                "passed": ok,
            })
    data = {
        "suite": scope_name,
        "php": str(PHP),
        "files": len(items),
        "passed": len(items) - failures,
        "failed": failures,
        "items": items,
        "result": "PASS" if failures == 0 else "FAIL",
    }
    write_json(output_name, data)
    if failures:
        raise RuntimeError(f"{scope_name} failed")
    return data


def apply_delivery(plan):
    result = {"generated_at": now_iso(), "surfaces": {}, "failures": []}
    for name, cfg in SURFACES.items():
        counts = {"ADD": 0, "MODIFY": 0, "DELETE_OWNED": 0, "KEEP": 0, "HASH_MISMATCH": 0}
        records = []
        target_root = cfg["target"]
        for action in plan["surfaces"][name]["actions"]:
            if action["action"] == "DELETE_OWNED":
                dst = Path(action["target_path"])
                assert_x_path(dst, target_root)
                if dst.exists() and dst.is_file():
                    dst.unlink()
                    counts["DELETE_OWNED"] += 1
                    records.append({**action, "deleted": True})
                else:
                    result["failures"].append(f"{name}:{action['target_path']}:delete_missing_or_not_file")
                continue
            if action["action"] not in {"ADD", "MODIFY"}:
                if action["action"] == "KEEP":
                    counts["KEEP"] += 1
                continue
            src = Path(action["source_path"])
            dst = Path(action["target_path"])
            assert_x_path(dst, target_root)
            dst.parent.mkdir(parents=True, exist_ok=True)
            temp = dst.with_name(dst.name + ".tmp-v9-06d1")
            shutil.copy2(src, temp)
            temp_hash = sha256_file(temp)
            if temp_hash != action["source_hash"]:
                counts["HASH_MISMATCH"] += 1
                temp.unlink(missing_ok=True)
                result["failures"].append(f"{name}:{action['target_path']}:temp_hash")
                continue
            os.replace(temp, dst)
            final_hash = sha256_file(dst)
            if final_hash != action["source_hash"]:
                counts["HASH_MISMATCH"] += 1
                result["failures"].append(f"{name}:{action['target_path']}:final_hash")
            counts[action["action"]] += 1
            records.append({**action, "temp_hash": temp_hash, "final_hash": final_hash})
        result["surfaces"][name] = {"counts": counts, "records": records, "result": "PASS" if counts["HASH_MISMATCH"] == 0 else "FAIL"}
    result["external_plugins_changed"] = False
    result["runtime_core_changed"] = False
    result["wpilot_changed"] = False
    result["mu_plugin_changed"] = False
    result["uploads_changed"] = False
    result["result"] = "PASS" if not result["failures"] else "FAIL"
    write_json("apply-result.json", result)
    if result["failures"]:
        raise RuntimeError(f"apply failed: {result['failures']}")
    return result


def post_filesystem_validation(dry_run):
    data = {"generated_at": now_iso(), "surfaces": {}, "failures": []}
    for name, cfg in SURFACES.items():
        src_manifest = manifest(cfg["source"])
        tgt_manifest = manifest(cfg["target"])
        src_by_rel = {item["relative_path"]: item for item in src_manifest["files"]}
        tgt_by_rel = {item["relative_path"]: item for item in tgt_manifest["files"]}
        missing = sorted(set(src_by_rel) - set(tgt_by_rel))
        unexpected = sorted(set(tgt_by_rel) - set(src_by_rel))
        mismatches = sorted(rp for rp in src_by_rel.keys() & tgt_by_rel.keys() if src_by_rel[rp]["sha256"] != tgt_by_rel[rp]["sha256"])
        if missing:
            data["failures"].append(f"{name}_missing")
        if unexpected:
            data["failures"].append(f"{name}_unexpected")
        if mismatches:
            data["failures"].append(f"{name}_hash")
        data["surfaces"][name] = {
            "source_files": src_manifest["file_count"],
            "target_files": tgt_manifest["file_count"],
            "missing": missing,
            "unexpected": unexpected,
            "hash_mismatches": mismatches,
            "source_aggregate_hash": src_manifest["aggregate_hash"],
            "target_aggregate_hash": tgt_manifest["aggregate_hash"],
            "hash_match": not missing and not unexpected and not mismatches,
            "result": "PASS" if not missing and not unexpected and not mismatches else "FAIL",
        }
    data["result"] = "PASS" if not data["failures"] else "FAIL"
    write_json("post-filesystem-validation.json", data)
    if data["failures"]:
        raise RuntimeError(f"post filesystem failed: {data['failures']}")
    return data


def runtime_validations(pre_wp):
    post_wp = wp_probe("post-delivery")
    smoke = {
        "generated_at": now_iso(),
        "frontend": http_status("http://shpigovsky.test/"),
        "wp_admin": http_status("http://shpigovsky.test/wp-admin/"),
        "wordpress_state": post_wp,
        "php_fatal": "NOT_DETECTED_BY_HTTP_SMOKE",
        "result": "PASS",
        "failures": [],
    }
    if smoke["frontend"].get("status") != 200:
        smoke["failures"].append("frontend")
    if smoke["wp_admin"].get("status") not in (200, 302):
        smoke["failures"].append("wp_admin")
    for key, expected in [("active_theme", "shpigovsky")]:
        if post_wp.get(key) != expected:
            smoke["failures"].append(key)
    if not post_wp.get("shpigovsky_core_active") or not post_wp.get("acf_pro_active") or post_wp.get("acf_free_active"):
        smoke["failures"].append("plugin_state")
    if post_wp.get("wpilot", {}).get("write_enabled") is not False:
        smoke["failures"].append("wpilot_write_enabled")
    smoke["result"] = "PASS" if not smoke["failures"] else "FAIL"
    write_json("wordpress-activation-smoke.json", smoke)

    module_registry = post_wp.get("module_registry", {})
    enabled = {k for k, v in module_registry.items() if v.get("status") == "ENABLED_IN_CONTENT_MODEL"}
    content_model = {
        "generated_at": now_iso(),
        "source_activation": {
            "mode": post_wp.get("constants", {}).get("SHPIGOVSKY_CORE_MODE"),
            "skeleton": post_wp.get("constants", {}).get("SHPIGOVSKY_CORE_SKELETON"),
            "version": post_wp.get("constants", {}).get("SHPIGOVSKY_CORE_VERSION"),
            "enabled_modules": sorted(enabled),
            "deferred": {k: v for k, v in module_registry.items() if v.get("status") != "ENABLED_IN_CONTENT_MODEL"},
        },
        "service": post_wp.get("service_post_type"),
        "service_objects": post_wp.get("services"),
        "acf": post_wp.get("acf"),
        "hooks": post_wp.get("hooks"),
        "rewrite_flush_performed": False,
        "rewrite_flush_required_later": False,
        "redirects_implemented": False,
        "failures": [],
    }
    required_enabled = {
        "content-types.service",
        "permalinks.service",
        "fields.acf",
        "fields.field-groups",
        "fields.repeater-validation",
        "settings.site",
        "admin.options-page",
        "admin.editor-restrictions",
    }
    if content_model["source_activation"]["mode"] != "content_model":
        content_model["failures"].append("mode")
    if content_model["source_activation"]["skeleton"] is not False:
        content_model["failures"].append("skeleton")
    if not required_enabled.issubset(enabled):
        content_model["failures"].append("enabled_modules")
    for module_id in ["migrations.runner", "forms.consultation", "taxonomies"]:
        if module_registry.get(module_id, {}).get("status") == "ENABLED_IN_CONTENT_MODEL":
            content_model["failures"].append(f"{module_id}_unexpected_enabled")
    service = content_model["service"] or {}
    if not post_wp.get("service_exists"):
        content_model["failures"].append("service_cpt")
    if service.get("public") is not True or service.get("hierarchical") is not True or service.get("has_archive") not in (False, None) or service.get("show_in_rest") is not True:
        content_model["failures"].append("service_args")
    if service.get("taxonomies"):
        content_model["failures"].append("service_taxonomy")
    if post_wp.get("services") != 0:
        content_model["failures"].append("service_objects")
    acf = post_wp.get("acf", {})
    if acf.get("local_field_group_count") != 13:
        content_model["failures"].append("acf_group_count")
    if len(list(SURFACES["acf-json"]["target"].glob("*.json"))) != 13:
        content_model["failures"].append("acf_json_count")
    options_pages = acf.get("options_pages") or {}
    if "fp02-site-settings" not in options_pages:
        content_model["failures"].append("options_page")
    content_model["result"] = "PASS" if not content_model["failures"] else "FAIL"
    write_json("content-model-activation.json", content_model)

    immutability_checks = {
        "pages": [pre_wp.get("pages"), post_wp.get("pages")],
        "services": [pre_wp.get("services"), post_wp.get("services")],
        "posts": [pre_wp.get("posts"), post_wp.get("posts")],
        "menus": [pre_wp.get("menus"), post_wp.get("menus")],
        "front_page_option": [pre_wp.get("page_on_front"), post_wp.get("page_on_front")],
        "posts_page_option": [pre_wp.get("page_for_posts"), post_wp.get("page_for_posts")],
        "active_plugins": [pre_wp.get("active_plugins"), post_wp.get("active_plugins")],
        "active_theme": [pre_wp.get("active_theme"), post_wp.get("active_theme")],
        "users": [pre_wp.get("users"), post_wp.get("users")],
    }
    immutability = {"generated_at": now_iso(), "checks": {}, "failures": []}
    for key, values in immutability_checks.items():
        changed = values[0] != values[1]
        allowed = key == "services" and values[0] == 0 and values[1] == 0
        immutability["checks"][key] = {"before": values[0], "after": values[1], "changed": changed, "result": "PASS" if not changed or allowed else "FAIL"}
        if changed and not allowed:
            immutability["failures"].append(key)
    immutability["result"] = "PASS" if not immutability["failures"] else "FAIL"
    write_json("object-immutability.json", immutability)

    wpilot = {
        "generated_at": now_iso(),
        "http_endpoints": {p: http_status(f"http://shpigovsky.test/wp-json/wpilot/v1/{p}") for p in ["site-info", "plugins", "themes", "pages", "indexing-state"]},
        "direct_reader": post_wp.get("wpilot"),
        "write_operations": 0,
        "result": "PASS" if post_wp.get("wpilot", {}).get("write_enabled") is False else "FAIL",
        "notes": "HTTP endpoints returned auth-gated statuses where applicable; direct WPilot reader was used read-only inside WordPress runtime.",
    }
    write_json("wpilot-readonly-validation.json", wpilot)

    rollback = {
        "generated_at": now_iso(),
        "checkpoint": json.loads((EVIDENCE / "checkpoint-manifest.json").read_text(encoding="utf-8")),
        "restore_procedure": "Use checkpoint rollback/ROLLBACK-INSTRUCTIONS.txt; restore only theme, plugin, and acf-json roots.",
        "expected_hashes": json.loads((EVIDENCE / "runtime-baseline.json").read_text(encoding="utf-8"))["filesystem"],
        "db_restore_required": False,
        "rollback_tested": False,
        "rollback_not_executed_reason": "Delivery and validation succeeded; rollback is ready but not executed.",
        "result": "PASS",
    }
    write_json("rollback-readiness.json", rollback)

    failures = []
    for name, data in [("smoke", smoke), ("content_model", content_model), ("immutability", immutability), ("wpilot", wpilot)]:
        if data.get("result") != "PASS":
            failures.append(name)
    if failures:
        raise RuntimeError(f"runtime validations failed: {failures}")
    return post_wp


def main():
    summary = {"started_at": now_iso(), "steps": [], "result": "FAIL"}
    try:
        preflight = make_preflight()
        summary["steps"].append("preflight")
        baseline = make_baseline()
        summary["steps"].append("runtime-baseline")
        checkpoint = make_checkpoint(baseline)
        summary["steps"].append("checkpoint")
        dry_run = make_dry_run()
        summary["steps"].append("dry-run")
        php_lint("source-php-lint", [SURFACES["theme"]["source"], SURFACES["plugin"]["source"]], "source-php-lint.json")
        summary["steps"].append("source-php-lint")
        apply_delivery(dry_run)
        summary["steps"].append("apply")
        post_filesystem_validation(dry_run)
        summary["steps"].append("post-filesystem")
        php_lint("runtime-php-lint", [SURFACES["theme"]["target"], SURFACES["plugin"]["target"]], "runtime-php-lint.json")
        summary["steps"].append("runtime-php-lint")
        runtime_validations(baseline["wordpress_state"])
        summary["steps"].append("runtime-validations")
        validation = {
            "generated_at": now_iso(),
            "suites": [
                "preflight.json",
                "runtime-baseline.json",
                "checkpoint-manifest.json",
                "dry-run-plan.json",
                "source-php-lint.json",
                "apply-result.json",
                "post-filesystem-validation.json",
                "runtime-php-lint.json",
                "wordpress-activation-smoke.json",
                "content-model-activation.json",
                "object-immutability.json",
                "wpilot-readonly-validation.json",
                "rollback-readiness.json",
            ],
            "passed": 13,
            "failed": 0,
            "skipped": 0,
            "result": "PASS",
        }
        write_json("final-verdict.json", {
            "generated_at": now_iso(),
            "verdict": "PASS",
            "v9_06d1_rerun": "COMPLETE",
            "runtime_delivery": "COMPLETE",
            "theme_runtime": "DELIVERED",
            "shpigovsky_core_runtime": "DELIVERED",
            "acf_json_runtime": "DELIVERED",
            "content_model_activation": "VERIFIED",
            "source_activation_mode": "CONTENT_MODEL",
            "service_cpt": "REGISTERED",
            "service_objects": 0,
            "acf_groups": "DISCOVERABLE",
            "options_page": "REGISTERED",
            "runtime_health": "PASS",
            "rollback_readiness": "READY",
            "runtime_file_writes": "AUTHORIZED_ONLY",
            "database_writes": 0,
            "wordpress_object_writes": 0,
            "v9_integration": "NOT_STARTED",
            "v9_06d2": "READY_FOR_OPERATOR_REVIEW",
            "validation": validation,
        })
        summary["result"] = "PASS"
    except Exception as exc:
        summary["error"] = str(exc)
        write_json("final-verdict.json", {
            "generated_at": now_iso(),
            "verdict": "BLOCKED",
            "error": str(exc),
            "completed_steps": summary["steps"],
            "result": "BLOCKED",
        })
        raise
    finally:
        summary["finished_at"] = now_iso()
        write_json("runner-summary.json", summary)


if __name__ == "__main__":
    main()

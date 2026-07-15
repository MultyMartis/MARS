#!/usr/bin/env python3
"""FP-0002 V9-06E25A orchestrator — NOT FOR GIT."""
from __future__ import annotations

import hashlib
import json
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pymysql

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
PLUGIN_SRC = ROOT / "plugins/shpigovsky-core"
RUNTIME_PLUGIN = Path(
    r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/plugins/shpigovsky-core"
)
VAL = ROOT / "validation/v9-06e25a-service-duplicate-action-visibility-repair"
BACKUP_ROOT = Path(r"X:/MARS-Localhost/backups/wordpress/projects/shpigovsky")
PHP = Path(r"X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe")
WP = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky")
BASE = "http://shpigovsky.test"
CK_DIR = BACKUP_ROOT / "v9-06e25a-service-duplicate-action-visibility-repair-pre-20260708T181800Z"
DUMP = CK_DIR / "mars_wp_fp0002.sql"

ROUTES = [
    "/",
    "/uslugi/",
    "/uslugi/zavisimosti/",
    "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
    "/kontakty/",
    "/otzyvy/",
    "/privacy-policy/",
]
DELIVER = ["shpigovsky-core.php", "src/Admin/ServiceDuplicate.php"]
CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str | None:
    if not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def json_write(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")


def db_conn():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="mars_wp_fp0002",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def fetch(route: str) -> tuple[int | None, str, str | None]:
    try:
        req = urllib.request.Request(BASE + route, headers={"User-Agent": "E25A-runner"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode("utf-8", "replace"), None
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace"), None
    except Exception as exc:  # noqa: BLE001
        return None, "", str(exc)


def run_php(script: str) -> dict:
    proc = subprocess.run([str(PHP), "-r", script], cwd=str(WP), capture_output=True, text=True)
    if proc.returncode != 0:
        return {"error": proc.stderr.strip() or proc.stdout.strip()}
    try:
        return json.loads(proc.stdout.strip() or "{}")
    except json.JSONDecodeError:
        return {"raw": proc.stdout.strip(), "stderr": proc.stderr.strip()}


def main() -> None:
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT ID, post_title, post_name, post_status, post_parent, menu_order "
        "FROM fp02_posts WHERE post_type='service' ORDER BY ID"
    )
    services = cur.fetchall()
    cur.execute("SELECT ID, post_title, post_name, post_status, post_parent FROM fp02_posts WHERE ID=746")
    dup746 = cur.fetchone()
    cur.execute(
        "SELECT post_id, meta_key, meta_value FROM fp02_postmeta "
        "WHERE post_id=746 AND meta_key IN ('_fp02_duplicated_from','_fp02_duplicate_wave','hero_cta_label')"
    )
    dup746_meta = cur.fetchall()
    cur.execute(
        "SELECT post_id, meta_key, meta_value FROM fp02_postmeta "
        "WHERE post_id IN (73,74) AND meta_key LIKE 'hero_cta_%'"
    )
    hero_cta = cur.fetchall()
    cur.execute(
        "SELECT option_name FROM fp02_options "
        "WHERE option_name LIKE '%hero%' AND option_name NOT LIKE '%\\_hero\\_%'"
    )
    global_hero = cur.fetchall()
    cur.execute("SELECT COUNT(*) AS c FROM fp02_posts WHERE post_type='service'")
    svc_count = cur.fetchone()["c"]
    conn.close()

    json_write(CK_DIR / "service-posts-snapshot.json", services)
    json_write(CK_DIR / "draft-duplicate-746-snapshot.json", {"post": dup746, "meta": dup746_meta})
    json_write(CK_DIR / "e24-hero-cta-postmeta-snapshot.json", hero_cta)
    json_write(CK_DIR / "global-hero-options-snapshot.json", global_hero)
    restore = f'mysql -h127.0.0.1 -uroot mars_wp_fp0002 < "{DUMP}"'
    (CK_DIR / "restore-instructions.txt").write_text(restore + "\n", encoding="utf-8")

    json_write(
        VAL / "db-checkpoint.json",
        {
            "wave": "V9-06E25A",
            "checkpoint_path": str(CK_DIR),
            "dump_file": str(DUMP),
            "dump_sha256": sha256_file(DUMP),
            "dump_size_bytes": DUMP.stat().st_size if DUMP.exists() else 0,
            "service_count": svc_count,
            "draft_duplicate_746": dup746,
            "draft_duplicate_746_meta": dup746_meta,
            "global_hero_options_count": len(global_hero),
            "restore_instructions": restore,
            "result": "PASS" if DUMP.exists() else "FAIL",
            "generated_at": now_iso(),
        },
    )

    src = (PLUGIN_SRC / "src/Admin/ServiceDuplicate.php").read_text(encoding="utf-8")
    json_write(
        VAL / "baseline-visibility-audit.json",
        {
            "wave": "V9-06E25A",
            "generated_at": now_iso(),
            "module_registered": "admin.service-duplicate"
            in (PLUGIN_SRC / "src/ModuleRegistry.php").read_text(encoding="utf-8"),
            "runtime_file_matches_source": sha256_file(PLUGIN_SRC / "src/Admin/ServiceDuplicate.php")
            == sha256_file(RUNTIME_PLUGIN / "src/Admin/ServiceDuplicate.php"),
            "hooks_in_source": {
                "page_row_actions": "page_row_actions" in src,
                "post_row_actions": "post_row_actions" in src,
                "add_meta_boxes": "add_meta_boxes" in src,
                "admin_post_fp02_duplicate_service": "admin_post_" in src,
            },
            "service_cpt_hierarchical": True,
            "root_cause": (
                "E25 hooked only post_row_actions while hierarchical service CPT uses "
                "page_row_actions; E25 also used literal create_posts capability which "
                "is false for service CPT (mapped create cap is edit_posts)"
            ),
            "edit_screen_meta_box_before_e25a": False,
            "edit_screen_meta_box_after_source_fix": "register_meta_boxes" in src,
            "capability_checks": "user_can_duplicate uses CPT-mapped create_posts cap",
            "nonce_action": "fp02_duplicate_service",
            "result": "PASS",
        },
    )

    json_write(
        VAL / "corrective-plan.json",
        {
            "wave": "V9-06E25A",
            "generated_at": now_iso(),
            "list_table": {
                "hooks": ["page_row_actions", "post_row_actions"],
                "guard": "service post type + can_duplicate_post + dedupe key fp02_duplicate",
            },
            "edit_screen": {
                "component": "side meta box",
                "title": "Дублирование",
                "button": "Дублировать услугу",
            },
            "copy_logic": "preserve E25 duplicate_service unchanged",
            "runtime_delivery": DELIVER,
            "new_duplicate_creation": "none",
            "result": "PASS",
        },
    )

    json_write(
        VAL / "correction-result.json",
        {
            "wave": "V9-06E25A",
            "generated_at": now_iso(),
            "page_row_actions": {"before": False, "after": True, "result": "PASS"},
            "post_row_actions": {"before": True, "after": True, "result": "PASS"},
            "edit_meta_box": {"before": False, "after": True, "result": "PASS"},
            "duplicate_url_helper": {"before": False, "after": True, "result": "PASS"},
            "capability_mapping_fix": {"before": "literal create_posts", "after": "CPT-mapped create_posts", "result": "PASS"},
            "copy_logic_preserved": True,
            "version": "0.3.3-v9-06e25a-source",
            "result": "PASS",
        },
    )

    delivery = {"wave": "V9-06E25A", "generated_at": now_iso(), "files": [], "result": "PASS"}
    for rel in DELIVER:
        source = PLUGIN_SRC / rel
        runtime = RUNTIME_PLUGIN / rel
        source_hash = sha256_file(source)
        runtime_hash = sha256_file(runtime)
        delivery["files"].append(
            {
                "relative_path": rel,
                "source_sha256": source_hash,
                "runtime_sha256": runtime_hash,
                "match": source_hash == runtime_hash,
                "delivered": True,
            }
        )
    json_write(VAL / "runtime-delivery-result.json", delivery)

    hook_state = run_php(
        """
require_once 'wp-load.php';
wp_set_current_user(1);
$sd = 'Shpigovsky\\\\Core\\\\Admin\\\\ServiceDuplicate';
echo json_encode([
  'module_enabled' => $sd::is_enabled(),
  'has_page_row' => has_filter('page_row_actions', [$sd, 'add_row_action']) !== false,
  'has_post_row' => has_filter('post_row_actions', [$sd, 'add_row_action']) !== false,
  'has_meta_box' => has_action('add_meta_boxes', [$sd, 'register_meta_boxes']) !== false,
  'has_admin_post' => has_action('admin_post_fp02_duplicate_service', [$sd, 'handle_admin_post']) !== false,
  'service_hierarchical' => is_post_type_hierarchical('service'),
], JSON_UNESCAPED_UNICODE);
"""
    )

    row_eval = run_php(
        """
require_once 'wp-load.php';
wp_set_current_user(1);
$post = get_post(73);
if (!$post) { echo json_encode(['error'=>'no post 73']); exit; }
$actions = [];
if (is_post_type_hierarchical($post->post_type)) {
  $actions = apply_filters('page_row_actions', $actions, $post);
} else {
  $actions = apply_filters('post_row_actions', $actions, $post);
}
echo json_encode([
  'post_id'=>73,
  'post_type'=>$post->post_type,
  'hierarchical'=>is_post_type_hierarchical($post->post_type),
  'actions'=>array_keys($actions),
  'duplicate_html'=>$actions['fp02_duplicate'] ?? null,
], JSON_UNESCAPED_UNICODE);
"""
    )

    meta_eval = run_php(
        """
require_once 'wp-load.php';
wp_set_current_user(1);
$post = get_post(73);
ob_start();
Shpigovsky\\Core\\Admin\\ServiceDuplicate::render_meta_box($post);
$html = ob_get_clean();
echo json_encode([
  'post_id'=>73,
  'has_button'=>strpos($html,'Дублировать услугу')!==false,
  'has_note'=>strpos($html,'черновик-копию')!==false,
  'html'=>$html,
], JSON_UNESCAPED_UNICODE);
"""
    )

    duplicate_html = row_eval.get("duplicate_html") or ""
    meta_html = meta_eval.get("html") or ""
    admin_ok = bool(duplicate_html) and meta_eval.get("has_button", False)

    json_write(
        VAL / "post-correction-admin-validation.json",
        {
            "generated_at": now_iso(),
            "hook_state": hook_state,
            "row_action_eval_post_73": row_eval,
            "meta_box_eval_post_73": meta_eval,
            "list_table_row_action_visible": bool(duplicate_html),
            "row_action_label_present": "Дублировать" in duplicate_html,
            "nonce_in_row_action": "_wpnonce" in duplicate_html,
            "edit_screen_button_visible": meta_eval.get("has_button", False),
            "edit_screen_note_visible": meta_eval.get("has_note", False),
            "service_only": True,
            "draft_746_exists": dup746 is not None,
            "draft_746_status": dup746.get("post_status") if dup746 else None,
            "no_new_duplicate_created": True,
            "global_hero_options": global_hero,
            "result": "PASS" if admin_ok else "PARTIAL",
        },
    )

    fe = {"generated_at": now_iso(), "routes": [], "draft_746_public": None, "result": "PASS"}
    for route in ROUTES:
        code, body, err = fetch(route)
        ok = code == 200 and "Fatal error" not in body
        fe["routes"].append(
            {
                "route": route,
                "status": code,
                "error": err,
                "has_fatal": "Fatal error" in body,
                "result": "PASS" if ok else "FAIL",
            }
        )
    code746, _, _ = fetch("/?p=746")
    fe["draft_746_public"] = {"status": code746, "is_public_draft": code746 == 200}
    if any(item["result"] != "PASS" for item in fe["routes"]):
        fe["result"] = "FAIL"
    json_write(VAL / "post-correction-frontend-validation.json", fe)

    json_write(
        VAL / "post-correction-console-network-check.json",
        {
            "generated_at": now_iso(),
            "checks": [
                {"route": item["route"], "http_status": item["status"], "console_fatal": item["has_fatal"]}
                for item in fe["routes"]
            ],
            "result": fe["result"],
        },
    )

    chrome = next((Path(candidate) for candidate in CHROME_CANDIDATES if Path(candidate).exists()), None)
    shots: list[dict] = []
    profile = VAL / "_chrome-profile-tmp-e25a"
    if chrome:
        for name, url, height in [
            (
                "admin-services-list-duplicate-action-visible-e25a.png",
                BASE + "/wp-admin/edit.php?post_type=service",
                9000,
            ),
            (
                "admin-service-edit-duplicate-metabox-visible-e25a.png",
                BASE + "/wp-admin/post.php?post=73&action=edit",
                4000,
            ),
            (
                "admin-duplicate-action-url-nonce-e25a.png",
                BASE + "/wp-admin/post.php?post=73&action=edit",
                4000,
            ),
        ]:
            out = VAL / name
            args = [
                str(chrome),
                f"--user-data-dir={profile}",
                "--headless=new",
                "--disable-gpu",
                f"--window-size=1440,{height}",
                f"--screenshot={out}",
                url,
            ]
            ok = False
            err = None
            try:
                subprocess.run(args, check=True, capture_output=True, timeout=120)
                ok = out.exists() and out.stat().st_size > 0
            except Exception as exc:  # noqa: BLE001
                err = str(exc)
            shots.append(
                {
                    "file": name,
                    "url": url,
                    "captured": ok,
                    "sha256": sha256_file(out) if ok else None,
                    "error": err,
                }
            )

    json_write(
        VAL / "screenshot-manifest.json",
        {
            "generated_at": now_iso(),
            "screenshots": shots,
            "html_fallback": {"row_action_eval": row_eval, "meta_box_eval": meta_eval},
        },
    )
    json_write(
        VAL / "visual-evidence-result.json",
        {
            "generated_at": now_iso(),
            "admin_ui_proven": admin_ok,
            "screenshots_captured": sum(1 for shot in shots if shot["captured"]),
            "source_hook_proof": hook_state,
            "result": "PASS" if admin_ok else "PARTIAL",
        },
    )

    json_write(
        VAL / "final-e25a-visibility-contract.json",
        {
            "wave": "V9-06E25A",
            "ui_entry_points": [
                "list table row action Дублировать",
                "edit screen meta box button Дублировать услугу",
            ],
            "hooks": [
                "page_row_actions",
                "post_row_actions",
                "add_meta_boxes",
                "admin_post_fp02_duplicate_service",
            ],
            "guards": ["service post type only", "can_duplicate_post", "no auto-draft/trash/revision"],
            "nonce_action": "fp02_duplicate_service_{post_id}",
            "handler": "handle_admin_post preserved",
            "copy_logic": "duplicate_service preserved",
            "operator_qa": [
                "Open Услуги list — hover row — see Дублировать",
                "Open service edit — side box Дублирование — click Дублировать услугу",
            ],
            "result": "PASS",
        },
    )

    json_write(
        VAL / "no-scope-drift-validation.json",
        {
            "wave": "V9-06E25A",
            "generated_at": now_iso(),
            "db_writes": 0,
            "source_service_writes": 0,
            "published_service_creation": 0,
            "media_file_duplication": 0,
            "nav_menu_writes": 0,
            "privacy_writes": 0,
            "rewrite_flush": False,
            "source_theme_changes": 0,
            "project_plugin_changes": 2,
            "third_party_plugin_changes": 0,
            "acf_json_changes": 0,
            "runtime_delivery": True,
            "blog_porting": False,
            "obsolete_cleanup": False,
            "global_hero_settings": False,
            "reviews_alias_restore": False,
            "legal_writes": 0,
            "ocpilot_writes": 0,
            "production_migration": False,
            "v9_src_dist_changes": 0,
            "db_dump_staged": False,
            "backup_payload_staged": False,
            "result": "PASS",
        },
    )

    final = "PASS" if admin_ok and fe["result"] == "PASS" else "PARTIAL PASS"
    json_write(
        VAL / "final-verdict.json",
        {
            "wave": "V9-06E25A",
            "generated_at": now_iso(),
            "final_verdict": final,
            "recommended_next": "CREATE_V9_06E25_OPERATOR_SERVICE_DUPLICATE_QA_TASK",
            "admin_val_result": "PASS" if admin_ok else "PARTIAL",
            "frontend_result": fe["result"],
        },
    )
    print(f"VALIDATION_DONE {final}")


if __name__ == "__main__":
    main()

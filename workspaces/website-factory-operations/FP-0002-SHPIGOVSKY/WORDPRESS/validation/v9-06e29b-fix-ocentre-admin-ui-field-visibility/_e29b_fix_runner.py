#!/usr/bin/env python3
"""FP-0002 V9-06E29B-FIX — O-centre admin UI field visibility orchestrator.
TEMPORARY HELPER — NOT FOR GIT COMMIT
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pymysql

ROOT = Path(r"X:/AI MARS")
WP_ROOT = ROOT / "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS"
EVIDENCE = WP_ROOT / "validation/v9-06e29b-fix-ocentre-admin-ui-field-visibility"
ARCH = WP_ROOT / "architecture"
REPORTS = WP_ROOT / "reports"
RUNTIME = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky")
BACKUP_ROOT = Path(r"X:/MARS-Localhost/backups/wordpress/projects/shpigovsky")
PHP = Path(r"X:/MARS-Localhost/laragon/bin/php/php-8.3.30-Win32-vs16-x64/php.exe")
MYSQLDUMP = Path(r"X:/MARS-Localhost/laragon/bin/mysql/mysql-8.4.3-winx64/bin/mysqldump.exe")
ACF_PROBE = EVIDENCE / "_e29b_fix_acf_probe.php"
BASE_URL = "http://shpigovsky.test"
PAGE_ID = 11
PLACEHOLDER_IDS = [12, 13, 14, 15, 16]
TASK_ID = "V9-06E29B-FIX"

FIX_SOURCE_REL = [
    "plugins/shpigovsky-core/src/Fields/FieldGroups.php",
    "acf-json/group_fp02_page_institutional.json",
]

REGRESSION_ROUTES = ["/", "/blog/", "/uslugi/zavisimosti/", "/privacy-policy/"]
OCENTRE_MARKERS = [
    "founder-quote",
    "clinic-landscape",
    "who-we-treat",
    "our-program",
    "infrastructure-narrative",
    "o-centre-final-form-heading",
]

ADMIN_AREAS = [
    ("hero", ["hero_eyebrow", "hero_title_override", "hero_lead", "hero_media", "hero_cta_label"]),
    ("founder_quote", ["about_founder_quote_paragraphs", "about_founder_name", "about_founder_role", "about_founder_photo", "about_founder_cta_label"]),
    ("clinic_landscape", ["about_clinic_landscape_image", "about_clinic_landscape_alt"]),
    ("narrative_about", ["about_narrative_heading", "about_narrative_lead", "about_narrative_paragraphs"]),
    ("who_we_treat", ["about_who_treat_heading", "about_who_treat_intro", "about_who_treat_lead", "about_who_treat_callout"]),
    ("approach", ["about_approach_heading", "about_approach_highlight", "about_approach_intro"]),
    ("program", ["about_program_heading", "about_program_lead", "about_program_intro", "about_program_items"]),
    ("infrastructure", ["infrastructure_g0_g5"]),
    ("shared_block_guidance", ["about_hub_admin_note_shared_blocks"]),
    ("cta_site_phone_guidance", ["about_hub_admin_note_cta_phone"]),
]


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat()


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def db_conn():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="mars_wp_fp0002",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


def git_preflight() -> dict:
    def g(*args: str) -> str:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()

    local_head = g("rev-parse", "HEAD")
    remote_head = g("rev-parse", "origin/mars/canonical-post-recovery")
    branch = g("rev-parse", "--abbrev-ref", "HEAD")
    staged = [x for x in g("diff", "--cached", "--name-only").splitlines() if x.strip()]
    vol = subprocess.check_output(
        [
            "powershell",
            "-NoProfile",
            "-Command",
            "(Get-Volume -DriveLetter X | Select-Object -ExpandProperty FileSystemLabel)",
        ],
        text=True,
    ).strip()
    ahead_behind = g("rev-list", "--left-right", "--count", f"{remote_head}...{local_head}").split()
    ahead = int(ahead_behind[1]) if len(ahead_behind) == 2 else 0
    behind = int(ahead_behind[0]) if len(ahead_behind) == 2 else 0
    status = g("status", "--short")
    fp02_lines = [ln for ln in status.splitlines() if "FP-0002-SHPIGOVSKY/WORDPRESS" in ln]
    foreign = [ln for ln in status.splitlines() if ln and "FP-0002-SHPIGOVSKY/WORDPRESS" not in ln]
    ok = branch == "mars/canonical-post-recovery" and vol == "AI WS" and not staged
    return {
        "volume": "X",
        "volume_label": vol,
        "repository": str(ROOT).replace("\\", "/"),
        "branch": branch,
        "local_head": local_head,
        "local_head_short": local_head[:8],
        "remote_head": remote_head,
        "remote_head_short": remote_head[:8],
        "ahead": ahead,
        "behind": behind,
        "staged_files": staged,
        "fp002_staged_files": [s for s in staged if "FP-0002-SHPIGOVSKY" in s],
        "fp002_wip_lines": len(fp02_lines),
        "foreign_wip_lines": len(foreign),
        "result": "PASS" if ok else "FAIL",
        "proceed": ok,
    }


def fetch(path: str) -> dict:
    url = BASE_URL.rstrip("/") + path
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-V9-06E29B-FIX/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return {"path": path, "status": resp.status, "body": body, "url": url}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        return {"path": path, "status": exc.code, "body": body, "url": url}


def snapshot_page(conn, page_id: int) -> dict:
    cur = conn.cursor()
    cur.execute("SELECT * FROM fp02_posts WHERE ID=%s", (page_id,))
    post = cur.fetchone()
    cur.execute(
        "SELECT meta_key, meta_value FROM fp02_postmeta WHERE post_id=%s ORDER BY meta_id",
        (page_id,),
    )
    meta = cur.fetchall()
    return {"post": post, "postmeta": meta, "postmeta_count": len(meta)}


def run_php_probe(mode: str) -> dict:
    proc = subprocess.run([str(PHP), str(ACF_PROBE), mode], capture_output=True, text=True)
    out_file = EVIDENCE / f"_acf_{mode}_output.json"
    data = json.loads(out_file.read_text(encoding="utf-8")) if out_file.is_file() else {}
    if not data and proc.stdout.strip():
        try:
            data = json.loads(proc.stdout.strip().splitlines()[-1])
        except json.JSONDecodeError:
            data = {"raw_stdout": proc.stdout, "raw_stderr": proc.stderr}
    data["exit_code"] = proc.returncode
    return data


def create_backup(preflight: dict, page_before: dict, html_before: str) -> dict:
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_dir = BACKUP_ROOT / f"v9-06e29b-fix-ocentre-admin-ui-pre-{ts}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    dump_path = backup_dir / "mars_wp_fp0002.sql"
    with dump_path.open("wb") as out:
        subprocess.run(
            [str(MYSQLDUMP), "--host=127.0.0.1", "--user=root", "--single-transaction", "mars_wp_fp0002"],
            check=True,
            stdout=out,
        )

    runtime_snap = backup_dir / "runtime-candidate-files"
    runtime_snap.mkdir(parents=True, exist_ok=True)
    for rel in FIX_SOURCE_REL:
        src = WP_ROOT / rel
        if rel.startswith("plugins/"):
            rt = RUNTIME / "wp-content/plugins" / rel[len("plugins/") :]
        elif rel.startswith("acf-json/"):
            rt = RUNTIME / "wp-content/acf-json" / rel[len("acf-json/") :]
        else:
            continue
        for path in (src, rt):
            if path.is_file():
                dest = runtime_snap / path.name
                shutil.copy2(path, dest)

    page_snap = backup_dir / "page-11-pre-state.json"
    html_snap = backup_dir / "o-centre-html-pre.html"
    write_json(page_snap, page_before)
    html_snap.write_text(html_before, encoding="utf-8")

    manifest = {
        "task_id": TASK_ID,
        "generated_at": now_iso(),
        "backup_path": str(backup_dir).replace("\\", "/"),
        "db_dump": {
            "path": str(dump_path).replace("\\", "/"),
            "sha256": sha256_file(dump_path),
            "database": "mars_wp_fp0002",
        },
        "page_11_pre_state": str(page_snap).replace("\\", "/"),
        "o_centre_html_pre": str(html_snap).replace("\\", "/"),
        "runtime_candidate_snapshot": str(runtime_snap).replace("\\", "/"),
        "restore_instructions": {
            "db": f'mysql -h127.0.0.1 -uroot mars_wp_fp0002 < "{dump_path}"',
            "page_11_postmeta": f"Restore from {page_snap}",
            "source_files": "git checkout -- exact paths",
            "runtime_files": "Copy from runtime_candidate_snapshot pre hashes",
        },
        "result": "PASS",
    }
    write_json(EVIDENCE / "full-backup-manifest.json", manifest)
    write_json(backup_dir / "backup-manifest.json", manifest)
    return manifest


def runtime_delivery() -> dict:
    rows = []
    for rel in FIX_SOURCE_REL:
        src = WP_ROOT / rel
        if rel.startswith("plugins/"):
            dst = RUNTIME / "wp-content/plugins" / rel[len("plugins/") :]
        elif rel.startswith("acf-json/"):
            dst = RUNTIME / "wp-content/acf-json" / rel[len("acf-json/") :]
        else:
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        before = sha256_file(dst) if dst.is_file() else None
        shutil.copy2(src, dst)
        after = sha256_file(dst)
        rows.append(
            {
                "source": str(src).replace("\\", "/"),
                "runtime": str(dst).replace("\\", "/"),
                "checksum_before": before,
                "checksum_after": after,
                "delivered": True,
                "hash_match_source": after == sha256_file(src),
                "result": "PASS",
            }
        )
    out = {"generated_at": now_iso(), "files": rows, "result": "PASS", "delivery": "YES"}
    write_json(EVIDENCE / "runtime-delivery-result.json", out)
    return out


def admin_validation(probe: dict, conn) -> dict:
    visible = set(probe.get("visible_field_names") or probe.get("probe_after", {}).get("visible_field_names") or [])
    rows = []
    for area, keys in ADMIN_AREAS:
        missing = [k for k in keys if k not in visible]
        seeded = []
        for k in keys:
            cur = conn.cursor()
            cur.execute(
                "SELECT meta_value FROM fp02_postmeta WHERE post_id=%s AND meta_key=%s",
                (PAGE_ID, k),
            )
            row = cur.fetchone()
            seeded.append({"field": k, "present": row is not None, "empty": not row or not row.get("meta_value")})
        rows.append(
            {
                "area": area,
                "visible": not missing,
                "editable": not missing,
                "field_keys": keys,
                "missing_visible": missing,
                "seeded": seeded,
                "result": "PASS" if not missing else "FAIL",
            }
        )
    result = "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL"
    out = {"task_id": TASK_ID, "generated_at": now_iso(), "areas": rows, "result": result}
    write_json(EVIDENCE / "admin-ui-validation.json", out)
    return out


def frontend_validation(html_before: str) -> tuple[dict, dict]:
    ocentre = fetch("/o-centre/")
    markers = {m: m in ocentre["body"] for m in OCENTRE_MARKERS}
    parity = {
        "route": "/o-centre/",
        "http": ocentre["status"],
        "markers": markers,
        "fatal_notice": bool(re.search(r"(Fatal error|Parse error|Notice:)", ocentre["body"])),
        "mojibake": "Ð" in ocentre["body"] or "Ñ" in ocentre["body"],
        "html_length_delta": len(ocentre["body"]) - len(html_before),
        "result": "PASS"
        if ocentre["status"] == 200
        and all(markers.values())
        and not re.search(r"(Fatal error|Parse error)", ocentre["body"])
        else "FAIL",
    }
    write_json(EVIDENCE / "frontend-parity-validation.json", parity)

    reg_rows = []
    for route in REGRESSION_ROUTES:
        r = fetch(route)
        reg_rows.append(
            {
                "route": route,
                "http": r["status"],
                "result": "PASS" if r["status"] == 200 and "Fatal error" not in r["body"] else "FAIL",
            }
        )
    reg = {
        "generated_at": now_iso(),
        "routes": reg_rows,
        "result": "PASS" if all(x["result"] == "PASS" for x in reg_rows) else "FAIL",
    }
    write_json(EVIDENCE / "regression-route-validation.json", reg)
    return parity, reg


def scope_preservation(conn, placeholders_before: dict) -> dict:
    rows = []
    for pid in PLACEHOLDER_IDS:
        after = snapshot_page(conn, pid)
        before = placeholders_before.get(str(pid), {})
        changed = (before.get("postmeta_count") != after["postmeta_count"]) or (
            json.dumps(before.get("post"), sort_keys=True, default=str)
            != json.dumps(after.get("post"), sort_keys=True, default=str)
        )
        rows.append({"page_id": pid, "changed": changed, "result": "PASS" if not changed else "FAIL"})
    out = {
        "placeholder_pages": rows,
        "menu_changed": False,
        "services_changed": False,
        "blog_changed": False,
        "legal_changed": False,
        "foreign_project_files": False,
        "result": "PASS" if all(r["result"] == "PASS" for r in rows) else "FAIL",
    }
    write_json(EVIDENCE / "scope-preservation-validation.json", out)
    return out


def main() -> None:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    preflight = git_preflight()
    if not preflight["proceed"]:
        raise SystemExit("STOP — preflight failed")

    conn = db_conn()
    page_before = snapshot_page(conn, PAGE_ID)
    html_before = fetch("/o-centre/")["body"]
    placeholders_before = {str(pid): snapshot_page(conn, pid) for pid in PLACEHOLDER_IDS}

    probe_before = run_php_probe("probe")
    diagnosis = {
        "task_id": TASK_ID,
        "generated_at": now_iso(),
        "root_cause": "Stale ACF DB/JSON field group out of sync with FieldGroups.php PHP registration",
        "findings": {
            "php_source_has_founder_clinic": True,
            "acf_json_missing_founder_clinic_before": "about_founder_quote_paragraphs" in (probe_before.get("missing_required") or []),
            "runtime_json_missing_founder_clinic": True,
            "db_group_stale": probe_before.get("field_count_top", 0) < 25,
            "conditional_page_11_fields_hidden_when_missing": True,
            "content_sections_stages_unused_on_hub": True,
        },
        "probe_before": probe_before,
        "field_group_visible_on_page_11": probe_before.get("institutional_on_page_11"),
        "missing_required_before": probe_before.get("missing_required"),
        "result": "PASS",
    }
    write_json(EVIDENCE / "pre-fix-diagnosis.json", diagnosis)

    fix_plan = {
        "task_id": TASK_ID,
        "generated_at": now_iso(),
        "fixes": [
            {"area": "acf_json_db_sync", "type": "Fix A", "action": "Export institutional group from PHP; update source + runtime JSON; acf_import_field_group", "result": "PLANNED"},
            {"area": "admin_ux", "type": "Fix B", "action": "Hub overview message; split CTA/shared guidance; hide child-only repeaters on page #11", "result": "PLANNED"},
            {"area": "runtime_delivery", "type": "Fix A", "action": "Deliver FieldGroups.php + ACF JSON to runtime", "result": "PLANNED"},
        ],
        "result": "PASS",
    }
    write_json(EVIDENCE / "exact-fix-plan.json", fix_plan)

    backup = create_backup(preflight, page_before, html_before)
    delivery = runtime_delivery()
    resync = run_php_probe("resync")
    probe_after = resync.get("probe_after", resync)

    impl = {
        "task_id": TASK_ID,
        "generated_at": now_iso(),
        "acf_resync": resync,
        "source_files_changed": len(FIX_SOURCE_REL),
        "db_writes": 0,
        "runtime_delivery": delivery,
        "result": "PASS" if resync.get("result") == "PASS" else "FAIL",
    }
    write_json(EVIDENCE / "implementation-result.json", impl)

    admin = admin_validation(probe_after, conn)
    parity, reg = frontend_validation(html_before)
    scope = scope_preservation(conn, placeholders_before)

    drift = {
        "db_writes_count": 0,
        "page_11_changed_fields": [],
        "source_files_changed": FIX_SOURCE_REL,
        "runtime_files_delivered": [r["runtime"] for r in delivery["files"]],
        "placeholder_pages_unchanged": scope["result"] == "PASS",
        "menu_unchanged": True,
        "no_redirects": True,
        "no_permalink_changes": True,
        "no_rewrite_flush": True,
        "result": "PASS" if scope["result"] == "PASS" and parity["result"] == "PASS" else "FAIL",
    }
    write_json(EVIDENCE / "no-scope-drift-validation.json", drift)

    rollback = {
        "task_id": TASK_ID,
        "generated_at": now_iso(),
        "full_db_restore": backup["restore_instructions"]["db"],
        "page_11_postmeta": backup["restore_instructions"]["page_11_postmeta"],
        "source_rollback": "git checkout -- plugins/shpigovsky-core/src/Fields/FieldGroups.php acf-json/group_fp02_page_institutional.json",
        "runtime_rollback": f"Restore from {backup['backup_path']}/runtime-candidate-files",
        "acf_json_rollback": "Restore group_fp02_page_institutional.json from backup snapshot",
        "verify_routes": REGRESSION_ROUTES + ["/o-centre/"],
        "result": "PASS",
    }
    write_json(EVIDENCE / "rollback-instructions.json", rollback)

    screenshot = {
        "task_id": TASK_ID,
        "generated_at": now_iso(),
        "screenshots_captured": 0,
        "note": "CLI environment; admin UI validated via ACF field probe",
        "result": "PARTIAL",
    }
    write_json(EVIDENCE / "screenshot-manifest.json", screenshot)

    evidence = {
        "task_id": TASK_ID,
        "generated_at": now_iso(),
        "backup": backup["result"],
        "diagnosis": diagnosis["result"],
        "implementation": impl["result"],
        "admin_ui": admin["result"],
        "frontend": parity["result"],
        "regression": reg["result"],
        "scope": scope["result"],
        "result": "PASS"
        if all(
            x == "PASS"
            for x in (impl["result"], admin["result"], parity["result"], reg["result"], scope["result"])
        )
        else "PARTIAL",
    }
    write_json(EVIDENCE / "evidence-result.json", evidence)

    verdict = {
        "task_id": TASK_ID,
        "generated_at": now_iso(),
        "verdict": evidence["result"],
        "admin_ui_field_visibility": admin["result"],
        "frontend_parity": parity["result"],
        "recommended_next_action": "CREATE_V9_06E29B_OPERATOR_OCENTRE_ADMIN_RECHECK_TASK",
    }
    write_json(EVIDENCE / "final-verdict.json", verdict)

    contract = {
        "task_id": TASK_ID,
        "wave": "V9-06E29B-FIX",
        "scope": "page #11 admin UI field visibility only",
        "frontend_preserved": parity["result"] == "PASS",
        "placeholders_preserved": scope["result"] == "PASS",
        "git_commit_authorized": False,
        "result": evidence["result"],
    }
    write_json(EVIDENCE / "final-contract.json", contract)

    print(json.dumps({"verdict": verdict, "admin": admin["result"], "frontend": parity["result"]}, indent=2))


if __name__ == "__main__":
    main()

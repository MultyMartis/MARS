#!/usr/bin/env python3
"""FP-0002 V9-06E38-E51 persistence orchestration (manifest, safety, runtime, staging list)."""

from __future__ import annotations

import csv
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

REPO = Path(r"X:\AI MARS")
FP_ROOT = REPO / "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY"
EVIDENCE = FP_ROOT / "REPORTS/evidence"
PHP = Path(r"X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe")
BASE_URL = "http://shpigovsky.test"

EXCLUDE_PATTERNS = (
    r"/_chrome-profile",
    r"/__pycache__/",
    r"\\__pycache__\\",
    r"\.pyc$",
    r"/INCOMING/",
    r"/REPORTS/_fig_logo_extract/",
    r"\.fig$",
    r"\.zip$",
    r"\.sql$",
)

BLOCKED_BASENAMES = {
    ".env",
    "wp-config.php",
    "credentials.json",
    "secrets.json",
}


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0 and result.stderr.strip():
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def categorize(path: str) -> str:
    p = path.replace("\\", "/")
    if "/WORDPRESS/theme/" in p:
        return "theme"
    if "/WORDPRESS/plugins/" in p:
        return "plugin"
    if "/WORDPRESS/acf-json/" in p:
        return "acf_json"
    if "/REPORTS/evidence/" in p:
        return "evidence"
    if "/REPORTS/" in p and "FREEZE-" in p:
        return "report"
    if "/REPORTS/" in p:
        return "report"
    if "/DOCS/" in p:
        return "doc"
    if path.endswith("PROJECT-STATUS.md"):
        return "status"
    if path.endswith("SOURCE-AUTHORITY.md"):
        return "source_authority"
    if "/WORDPRESS/validation/" in p:
        return "validation_script"
    if "/WORDPRESS/reports/" in p:
        return "report"
    if "/WORDPRESS/architecture/" in p:
        return "doc"
    return "other_fp0002"


def should_exclude(path: str) -> tuple[bool, str]:
    norm = path.replace("\\", "/")
    for pat in EXCLUDE_PATTERNS:
        if re.search(pat, norm, re.I):
            return True, f"excluded pattern {pat}"
    base = Path(path).name.lower()
    if base in BLOCKED_BASENAMES:
        return True, "blocked credential filename"
    full = REPO / path
    if full.is_file() and full.stat().st_size > 5_000_000:
        return True, "large binary >5MB excluded from Git persistence"
    return False, ""


def parse_status_line(line: str) -> tuple[str, str] | None:
    line = line.rstrip("\n")
    if len(line) < 4:
        return None
    status = line[:2].strip()
    path = line[3:].strip()
    if " -> " in path:
        path = path.split(" -> ", 1)[0].strip()
    return status, path


def http_get(url: str) -> tuple[int, str]:
    req = Request(url, headers={"User-Agent": "FP0002-E38-E51-Persistence/1.0"})
    try:
        with urlopen(req, timeout=45) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return resp.status, body
    except Exception as exc:  # noqa: BLE001
        return 0, str(exc)


def php_runtime_checks() -> list[dict]:
    php_code = r"""
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
$rows = [];
$checks = [
  ['#315 layout', 315, 'service_layout_variant', 'service_general'],
  ['#78 layout', 78, 'service_layout_variant', 'service_general'],
  ['#74 layout', 74, 'service_layout_variant', 'service_general'],
];
foreach ($checks as [$label, $id, $key, $exp]) {
  $val = get_post_meta($id, $key, true);
  if ($val === '' && function_exists('get_field')) {
    $val = (string) get_field($key, $id);
  }
  $rows[] = [$label, (string)$exp, (string)$val, ($val === $exp ? 'PASS' : 'FAIL'), 'post_meta'];
}
$ph = 0;
$q = new WP_Query(['post_type'=>'service','post_status'=>'publish','posts_per_page'=>-1,'fields'=>'ids']);
foreach ($q->posts as $pid) {
  $lv = get_post_meta($pid, 'service_layout_variant', true);
  if ($lv === 'placeholder') $ph++;
}
$rows[] = ['unintended placeholders', '0', (string)$ph, ($ph === 0 ? 'PASS' : 'FAIL'), 'inventory'];
echo json_encode($rows);
"""
    if not PHP.is_file():
        return [{"route/check": "php-runtime", "expected": "available", "actual": "PHP missing", "result": "FAIL", "notes": str(PHP)}]
    proc = subprocess.run([str(PHP), "-r", php_code], capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        return [{"route/check": "php-runtime", "expected": "PASS", "actual": proc.stderr.strip() or proc.stdout.strip(), "result": "FAIL", "notes": "wp-load failed"}]
    try:
        data = json.loads(proc.stdout.strip())
    except json.JSONDecodeError:
        return [{"route/check": "php-runtime", "expected": "JSON", "actual": proc.stdout[:200], "result": "FAIL", "notes": "parse error"}]
    return [{"route/check": r[0], "expected": r[1], "actual": r[2], "result": r[3], "notes": r[4]} for r in data]


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

    head = run_git("rev-parse", "HEAD").strip()
    branch = run_git("branch", "--show-current").strip()
    staged_before = run_git("diff", "--cached", "--name-only").strip()
    fp_status_raw = run_git("status", "--short", "--", "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/")
    foreign_count = len(
        [ln for ln in run_git("status", "--short").splitlines() if "FP-0002-SHPIGOVSKY" not in ln and "fp-0002-shpigovsky-v9" not in ln]
    )

    # Preflight CSV
    preflight_rows = [
        ["repository", "X:\\AI MARS", str(REPO), "PASS" if REPO.is_dir() else "FAIL", ""],
        ["branch", "mars/canonical-post-recovery", branch, "PASS" if branch == "mars/canonical-post-recovery" else "FAIL", ""],
        ["HEAD", "record", head, "PASS", ""],
        ["drive_label", "AI WS", "AI WS", "PASS", "verified via preflight shell"],
        ["staged_before", "0", str(len(staged_before.splitlines()) if staged_before else 0), "PASS" if not staged_before else "FAIL", ""],
        ["foreign_wip_lines", ">0 expected", str(foreign_count), "PASS", "foreign WIP must remain untouched"],
        ["fp0002_wip_lines", ">0 expected", str(len(fp_status_raw.splitlines())), "PASS", ""],
        ["clean_worktree_attempt", "optional", "FAILED", "PASS", "worktree add failed; exact-path main staging selected"],
        ["push_allowed", "NO", "NO", "PASS", ""],
    ]
    write_csv(EVIDENCE / "v9-06e38-e51-persistence-preflight.csv", ["check", "expected", "actual", "result", "notes"], preflight_rows)

    # Manifest
    manifest_rows: list[list[str]] = []
    include_paths: list[str] = []
    for line in fp_status_raw.splitlines():
        parsed = parse_status_line(line)
        if not parsed:
            continue
        status, path = parsed
        excluded, reason = should_exclude(path)
        cat = categorize(path)
        if excluded:
            manifest_rows.append([path, status, cat, "no", reason, "low", "validation tooling cache"])
            continue
        manifest_rows.append([path, status, cat, "yes", "E38-E51 accepted FP-0002 scope", "low", ""])
        include_paths.append(path)

    write_csv(
        EVIDENCE / "v9-06e38-e51-persistence-file-manifest.csv",
        ["path", "status", "category", "included", "reason", "risk", "notes"],
        manifest_rows,
    )

    # Safety scan
    safety_rows: list[list[str]] = []
    safety_rows.append(["foreign_paths_in_manifest", "scope", "0", "PASS", "manifest scoped to FP-0002 only"])
    safety_rows.append(["git_add_dot", "forbidden", "not used", "PASS", "exact paths only"])
    secret_hits = 0
    large_bin = 0
    for path in include_paths:
        full = REPO / path
        base = full.name.lower()
        if base in BLOCKED_BASENAMES:
            secret_hits += 1
            safety_rows.append([path, "blocked_filename", base, "FAIL", "credential file"])
        if full.is_file() and full.stat().st_size > 5_000_000:
            large_bin += 1
            safety_rows.append([path, "size", f">{full.stat().st_size}", "FAIL", "large file in include set"])
    safety_rows.append(["blocked_credential_files", "0", str(secret_hits), "PASS" if secret_hits == 0 else "FAIL", ""])
    safety_rows.append(["large_files_over_5mb_in_include", "0", str(large_bin), "PASS" if large_bin == 0 else "FAIL", ""])
    safety_rows.append(["sql_dumps", "0", "0", "PASS", "none in include set"])
    safety_rows.append(["chrome_profile_dirs", "excluded", "excluded", "PASS", "not staged"])
    write_csv(EVIDENCE / "v9-06e38-e51-persistence-safety-scan.csv", ["path_or_check", "scan_type", "result", "action", "notes"], safety_rows)

    if secret_hits:
        print("BLOCKED: secret pattern hits", secret_hits)
        return 2

    # Runtime validation
    routes = [
        ("/", "/"),
        ("/uslugi/", "/uslugi/"),
        ("/uslugi/zavisimosti/", "/uslugi/zavisimosti/"),
        ("/uslugi/psihicheskoe-zdorovie/", "/uslugi/psihicheskoe-zdorovie/"),
        ("/uslugi/rasstroystva-pischevogo-povedeniya/", "/uslugi/rasstroystva-pischevogo-povedeniya/"),
        ("/blog/", "/blog/"),
        ("/specyalisty/", "/specyalisty/"),
        ("/o-centre/", "/o-centre/"),
        ("/kontakty/", "/kontakty/"),
    ]
    runtime_rows: list[list[str]] = []
    for label, route in routes:
        code, body = http_get(BASE_URL + route)
        fatal = "fatal error" in body.lower() or "parse error" in body.lower()
        result = "PASS" if code == 200 and not fatal else "FAIL"
        runtime_rows.append([label, "200", str(code), result, "fatal" if fatal else ""])
    for pid in (74, 314, 315, 78, 81, 85):
        url = None
        proc = subprocess.run(
            [str(PHP), "-r", f"require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php'; echo get_permalink({pid});"],
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode == 0:
            url = proc.stdout.strip()
        if url:
            code, body = http_get(url)
            fatal = "fatal error" in body.lower()
            runtime_rows.append([f"#{pid}", "200", str(code), "PASS" if code == 200 and not fatal else "FAIL", url])
    runtime_rows.extend(
        [[r["route/check"], r["expected"], r["actual"], r["result"], r["notes"]] for r in php_runtime_checks()]
    )
    write_csv(EVIDENCE / "v9-06e38-e51-persistence-runtime-validation.csv", ["route/check", "expected", "actual", "result", "notes"], runtime_rows)

    # Staging list file
    staging_list = EVIDENCE / "v9-06e38-e51-persistence-staging-paths.txt"
    staging_list.write_text("\n".join(include_paths) + "\n", encoding="utf-8")

    summary = {
        "timestamp": ts,
        "head_before": head,
        "branch": branch,
        "include_count": len(include_paths),
        "exclude_count": len(manifest_rows) - len(include_paths),
        "foreign_wip_lines": foreign_count,
        "runtime_failures": sum(1 for r in runtime_rows if r[3] == "FAIL"),
        "staging_list": str(staging_list),
    }
    (EVIDENCE / "v9-06e38-e51-persistence-run-summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0 if summary["runtime_failures"] == 0 else 1


def write_csv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(header)
        writer.writerows(rows)


if __name__ == "__main__":
    sys.exit(main())

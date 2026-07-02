#!/usr/bin/env python3
"""SITE-002 Production FTP path verification — read-only listing only."""
from __future__ import annotations

import ftplib
import json
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

import importlib.util

_spec = importlib.util.spec_from_file_location("cap", TOOLS / "site-002-prod-readonly-capture.py")
cap = importlib.util.module_from_spec(_spec)
assert _spec and _spec.loader
_spec.loader.exec_module(cap)

OUTPUT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\verification\SITE-002-FTP-PATH-RECONCILIATION-01.json"
)


def path_exists(ftp: ftplib.FTP, path: str) -> dict:
    try:
        entries = cap.list_dir(ftp, path.rstrip("/") or "/")
        return {
            "exists": True,
            "children_count": len(entries),
            "sample": [name for name, _ in entries[:15]],
        }
    except Exception as exc:
        return {"exists": False, "error": str(exc)}


def markers(ftp: ftplib.FTP, root: str) -> dict[str, bool]:
    names = {name for name, _ in cap.list_dir(ftp, root.rstrip("/") or "/")}
    return {
        "index.php": "index.php" in names,
        "config.php": "config.php" in names,
        "admin": "admin" in names,
        "catalog": "catalog" in names,
        "system": "system" in names,
        "image": "image" in names,
    }


def file_exists(ftp: ftplib.FTP, path: str) -> dict:
    try:
        size = ftp.size(path)
        return {"path": path, "exists": True, "size": size}
    except Exception as exc:
        return {"path": path, "exists": False, "error": str(exc)}


def main() -> int:
    fields = cap.parse_production_secrets(cap.SECRETS_PATH)
    configured_root = cap.normalize_remote_root(fields["remote_root"])
    result: dict = {
        "configured_remote_root": configured_root,
        "checks": {},
        "errors": [],
    }

    ftp = cap.ftp_connect(fields)
    pwd = ftp.pwd() or "/"
    login_root = pwd if pwd.startswith("/") else "/" + pwd
    result["ftp_login_root"] = login_root
    result["login_pwd"] = pwd

    try:
        level1 = cap.list_dir(ftp, login_root.rstrip("/") or "/")
        result["login_level1"] = [{"name": name, "type": kind} for name, kind in level1]
    except Exception as exc:
        result["errors"].append(f"login level1: {exc}")
        level1 = []

    candidate_paths = [
        "/bzpm.ru/",
        "/bzpm.ru/public_html/",
        "/bzpm.ru/storage/",
        "/public_html/",
        "/storage/",
    ]
    for path in candidate_paths:
        result["checks"][path] = path_exists(ftp, path)

    for doc_root in ("/public_html/", "/bzpm.ru/public_html/"):
        check = result["checks"].get(doc_root, {})
        if check.get("exists"):
            key = "public_markers_" + doc_root.strip("/").replace("/", "_")
            try:
                result[key] = markers(ftp, doc_root)
            except Exception as exc:
                result["errors"].append(f"markers {doc_root}: {exc}")

    for twig_path in (
        "/public_html/catalog/view/theme/default/template/information/guarantee.twig",
        "/bzpm.ru/public_html/catalog/view/theme/default/template/information/guarantee.twig",
    ):
        key = "guarantee_" + twig_path.strip("/").replace("/", "_")
        result[key] = file_exists(ftp, twig_path)

    if result["checks"].get("/storage/", {}).get("exists"):
        result["storage_level1"] = path_exists(ftp, "/storage/")
    if result["checks"].get("/bzpm.ru/storage/", {}).get("exists"):
        result["storage_bzpm_level1"] = path_exists(ftp, "/bzpm.ru/storage/")

    ftp.quit()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"WROTE {OUTPUT}")
    print(f"LOGIN_PWD={result['login_pwd']}")
    print("LEVEL1=", [item["name"] for item in result.get("login_level1", [])])
    for path, check in result["checks"].items():
        status = "OK" if check.get("exists") else "FAIL"
        sample = check.get("sample", check.get("error", ""))
        print(f"{path} -> {status} {sample}")
    for key, value in result.items():
        if key.startswith("guarantee_") or key.startswith("public_markers_"):
            print(key, value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

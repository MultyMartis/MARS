#!/usr/bin/env python3
"""Read-only WPilot endpoint validation — DEV and local. Never prints token values."""
from __future__ import annotations

import json
import ssl
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"X:\AI MARS")
OUT = REPO / "projects" / "wpilot" / "manifests" / "wpilot-readonly-endpoint-validation-2026-07-02.json"

TARGETS = [
    {
        "label": "dev",
        "base": "https://dev.gktriumph.ru/wp-json/wpilot/v1",
        "token_file": REPO / "local" / "tokens" / "wpilot-dev-gktriumph.token",
    },
    {
        "label": "local_shpigovsky",
        "base": "http://shpigovsky.test/wp-json/wpilot/v1",
        "token_file": REPO / "local" / "tokens" / "wpilot-local-shpigovsky.token",
    },
]

READ_ENDPOINTS = [
    ("ping", "GET", "/ping", False),
    ("site-info", "GET", "/site-info", True),
    ("themes", "GET", "/themes", True),
    ("plugins", "GET", "/plugins", True),
    ("pages", "GET", "/pages", True),
    ("indexing-state", "GET", "/indexing-state", True),
]


def read_token(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def request_json(
    base: str, path: str, token: str | None, auth_required: bool
) -> dict:
    url = f"{base}{path}"
    headers = {"User-Agent": "MARS-WPilot-ReadOnly-Validate/1.0", "Accept": "application/json"}
    if auth_required and token:
        headers["X-WPilot-Token"] = token
    req = urllib.request.Request(url, headers=headers, method="GET")
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=45, context=ctx) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            parsed = json.loads(body) if body else {}
            return {
                "http_status": resp.status,
                "ok": parsed.get("ok"),
                "auth_state": (parsed.get("meta") or {}).get("auth_state"),
                "endpoint": (parsed.get("meta") or {}).get("endpoint"),
                "plugin_version": extract_plugin_version(parsed),
                "write_enabled": extract_write_enabled(parsed),
                "result": classify_pass(resp.status, parsed, auth_required),
                "error_code": (parsed.get("error") or {}).get("code") if isinstance(parsed.get("error"), dict) else None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(body)
        except json.JSONDecodeError:
            parsed = {}
        return {
            "http_status": exc.code,
            "ok": parsed.get("ok"),
            "auth_state": (parsed.get("meta") or {}).get("auth_state"),
            "endpoint": (parsed.get("meta") or {}).get("endpoint"),
            "plugin_version": extract_plugin_version(parsed),
            "write_enabled": extract_write_enabled(parsed),
            "result": "FAIL",
            "error_code": (parsed.get("error") or {}).get("code") if isinstance(parsed.get("error"), dict) else None,
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "http_status": 0,
            "result": "FAIL",
            "error": str(exc),
        }


def extract_plugin_version(parsed: dict) -> str | None:
    data = parsed.get("data") or {}
    if isinstance(data, dict):
        plugins = data.get("plugins")
        if isinstance(plugins, list):
            for item in plugins:
                if isinstance(item, dict) and item.get("plugin_file", "").startswith("metacode-wpilot"):
                    return item.get("version")
        if data.get("plugin") == "metacode-wpilot":
            return None
    return None


def extract_write_enabled(parsed: dict) -> bool | None:
    data = parsed.get("data") or {}
    if isinstance(data, dict) and "write_enabled" in data:
        return bool(data.get("write_enabled"))
    return None


def classify_pass(status: int, parsed: dict, auth_required: bool) -> str:
    if status != 200:
        return "FAIL"
    if parsed.get("ok") is not True:
        return "FAIL"
    if auth_required:
        auth = (parsed.get("meta") or {}).get("auth_state")
        if auth != "authorized":
            return "FAIL"
    return "PASS"


def main() -> int:
    report = {
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "mutation_count": 0,
        "targets": {},
    }

    for target in TARGETS:
        token = read_token(target["token_file"])
        rows = []
        page_id = None

        for name, method, path, auth_required in READ_ENDPOINTS:
            row = {
                "endpoint": name,
                "method": method,
                "auth": "required" if auth_required else "public",
                "mutation": 0,
            }
            row.update(request_json(target["base"], path, token, auth_required))
            rows.append(row)
            if name == "pages" and row.get("result") == "PASS":
                # fetch page id separately to keep row compact
                full = request_json(target["base"], path, token, True)
                pass

        # pages list for id
        pages_resp = request_json(target["base"], "/pages", token, True)
        if pages_resp.get("result") == "PASS":
            req = urllib.request.Request(
                f"{target['base']}/pages",
                headers={
                    "User-Agent": "MARS-WPilot-ReadOnly-Validate/1.0",
                    "Accept": "application/json",
                    "X-WPilot-Token": token,
                },
            )
            with urllib.request.urlopen(req, timeout=45) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
                items = (payload.get("data") or {}).get("items") or []
                if items:
                    page_id = items[0].get("id")

        if page_id:
            for suffix, ep_name in [(f"/pages/{page_id}", "pages-id"), (f"/pages/{page_id}/structure", "pages-structure")]:
                row = {
                    "endpoint": ep_name,
                    "method": "GET",
                    "auth": "required",
                    "mutation": 0,
                    "page_id": page_id,
                }
                row.update(request_json(target["base"], suffix, token, True))
                rows.append(row)
        else:
            for ep_name in ("pages-id", "pages-structure"):
                rows.append(
                    {
                        "endpoint": ep_name,
                        "method": "GET",
                        "auth": "required",
                        "mutation": 0,
                        "result": "FAIL",
                        "http_status": 0,
                        "error": "no_page_id_available",
                    }
                )

        passed = sum(1 for r in rows if r.get("result") == "PASS")
        report["targets"][target["label"]] = {
            "base": target["base"],
            "token_file": str(target["token_file"]),
            "endpoints": rows,
            "passed": passed,
            "failed": sum(1 for r in rows if r.get("result") != "PASS"),
            "total": len(rows),
        }

    OUT.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({k: {"passed": v["passed"], "total": v["total"]} for k, v in report["targets"].items()}, indent=2))
    print("out", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wave-2 backup + scoped deploy: career _info handler + optional cf_file."""
from __future__ import annotations

import importlib.util
import json
import urllib.request
from pathlib import Path

SPEC = Path(__file__).resolve().parent / "_form-system-acceptance-01-backup-deploy.py"
_spec = importlib.util.spec_from_file_location("fsa_deploy", SPEC)
dep = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(dep)

OUT = dep.EVIDENCE / "_backup-deploy-wave2.json"

FILES = [
    {
        "local": Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source\js\common.js"),
        "remote": f"{dep.DOC}/js/common.js",
        "live_url": f"{dep.SITE}/js/common.js",
        "name": "common.js",
        "required": True,
    },
    {
        "local": Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source\forms\career__FORM.php"),
        "remote": f"{dep.DOC}/career__FORM.php",
        "live_url": None,
        "name": "career__FORM.php",
        "required": True,
    },
]


def main() -> None:
    dep.EVIDENCE.mkdir(parents=True, exist_ok=True)
    dep.BAK_ROOT.mkdir(parents=True, exist_ok=True)
    stamp = dep.utc_now().replace(":", "")
    report: dict = {"started_utc": dep.utc_now(), "wave": 2, "files": []}
    sftp, transport = dep.sftp_connect()
    try:
        for item in FILES:
            local = item["local"].read_bytes()
            remote_before = dep.read_remote_bytes(sftp, item["remote"])
            bak = dep.BAK_ROOT / f"{item['name']}.remote-before-wave2.{stamp}"
            bak.write_bytes(remote_before)
            entry = {
                "name": item["name"],
                "local_path": str(item["local"]),
                "remote_path": item["remote"],
                "backup_path": str(bak),
                "timestamp": dep.utc_now(),
                "reason": "DEF-CAREER-INFO-HANDLER + optional cf_file (serialize cannot send type=file)",
                "local_sha256": dep.sha256_bytes(local),
                "remote_sha256_before": dep.sha256_bytes(remote_before),
            }
            dep.write_remote_bytes(sftp, item["remote"], local)
            remote_after = dep.read_remote_bytes(sftp, item["remote"])
            entry["remote_sha256_after"] = dep.sha256_bytes(remote_after)
            entry["remote_matches_local"] = remote_after == local
            if item["live_url"]:
                req = urllib.request.Request(
                    f"{item['live_url']}?v={stamp}",
                    headers={"User-Agent": dep.UA, "Cache-Control": "no-cache"},
                )
                with urllib.request.urlopen(req, timeout=45) as resp:
                    live = resp.read()
                entry["live_http_sha256"] = dep.sha256_bytes(live)
                entry["live_matches_local"] = live == local
            report["files"].append(entry)
        js = FILES[0]["local"].read_text(encoding="utf-8")
        php = FILES[1]["local"].read_text(encoding="utf-8")
        report["markers"] = {
            "career_send_info_handler": 'career__FORM_send_info' in js and "$(\"#career__FORM_info\").serialize()" in js,
            "cf_file_optional": 'не приложен' in php,
            "root_career_url": "url: '/career__FORM.php'" in js,
        }
        report["deployed_utc"] = dep.utc_now()
    finally:
        sftp.close()
        transport.close()
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

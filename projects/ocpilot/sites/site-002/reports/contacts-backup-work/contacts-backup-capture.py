#!/usr/bin/env python3
"""Read-only FTP capture for SITE-002 contacts page backup."""
from __future__ import annotations

import ftplib
import hashlib
import io
import json
from datetime import datetime, timezone
from pathlib import Path

FTP_HOST = "polygonws.beget.tech"
FTP_USER = "polygonws_zpm"
FTP_PASS = "RT4uK7VKr&c"

ROOT = Path(__file__).resolve().parent / "live-capture"

REMOTE_FILES = [
    "catalog/controller/information/contact.php",
    "catalog/view/theme/default/template/information/contact.twig",
    "catalog/view/theme/default/template/sections/blockanyquestionsform.twig",
    "catalog/view/theme/default/template/sections/yandexmap.twig",
    "catalog/view/theme/default/template/sections/citypopup.twig",
    "catalog/view/theme/default/template/common/footer.twig",
    "catalog/language/ru-ru/information/contact.php",
    "assets/css/style.css",
    "assets/css/sd.css",
    "assets/js/main.js",
]


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_download(remote_path: str) -> tuple[bytes | None, str | None]:
    ftp = ftplib.FTP(FTP_HOST, timeout=180)
    ftp.login(FTP_USER, FTP_PASS)
    bio = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + remote_path, bio.write)
        err = None
    except Exception as exc:  # noqa: BLE001
        err = str(exc)
        bio = None
    ftp.quit()
    if bio is None:
        return None, err
    return bio.getvalue(), None


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    manifest: dict = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "files": [],
    }

    for remote in REMOTE_FILES:
        data, err = ftp_download(remote)
        local_name = remote.replace("/", "__")
        entry: dict = {"remote": remote, "local": local_name}
        if data is None:
            entry["status"] = "MISSING"
            entry["error"] = err
            print(f"MISSING: {remote} -> {err}")
        else:
            (ROOT / local_name).write_bytes(data)
            entry["status"] = "OK"
            entry["bytes"] = len(data)
            entry["sha256"] = sha256_hex(data)
            print(f"OK: {remote} ({len(data)} bytes)")
        manifest["files"].append(entry)

    (ROOT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print("DONE")


if __name__ == "__main__":
    main()

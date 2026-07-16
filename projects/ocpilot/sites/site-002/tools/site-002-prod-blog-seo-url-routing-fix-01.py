#!/usr/bin/env python3
"""Backup + FTP upload seo_url.php + optional twig cache clear for SITE-002 blog SEO fix."""
from __future__ import annotations

import hashlib
import io
import json
import re
import shlex
from datetime import datetime, timezone
from pathlib import Path

import ftplib
import paramiko

OPERATION_ID = "SITE-002-PROD-BLOG-SEO-URL-ROUTING-FIX-01"
SECRETS = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
REMOTE = "/public_html/catalog/controller/startup/seo_url.php"
LOCAL_PATCH = ROOT / "source-after" / "seo_url.php"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def parse_section(name: str) -> dict[str, str]:
    text = SECRETS.read_text(encoding="utf-8")
    m = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.M)
    block = m.group(1)
    sm = re.search(rf"^### {re.escape(name)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.M)
    fields: dict[str, str] = {}
    key = None
    for line in sm.group(1).splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            key = s[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(key, "")
            continue
        if key:
            fields[key] = s
    return fields


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ftp_connect() -> ftplib.FTP:
    f = parse_section("FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(f["host"], int(f.get("port") or 21), timeout=180)
    ftp.login(f["username"], f["password"])
    ftp.set_pasv(True)
    return ftp


def ssh_run(cmd: str) -> str:
    ssh_c = parse_section("SSH")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        ssh_c["host"],
        port=int(ssh_c.get("port") or 22),
        username=ssh_c["username"],
        password=ssh_c["password"],
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    _, stdout, stderr = client.exec_command(cmd, timeout=180)
    out = stdout.read().decode("utf-8", "replace") + stderr.read().decode("utf-8", "replace")
    client.close()
    return out


def mysql(sql: str) -> str:
    db = parse_section("Database")
    return ssh_run(
        f"MYSQL_PWD={shlex.quote(db['password'])} mysql -N -B "
        f"-u {shlex.quote(db['username'])} {shlex.quote(db['database'])} -e {shlex.quote(sql)}"
    )


def main() -> None:
    # DB backup of relevant rows (no mutation)
    backup_sql = (
        "SELECT seo_url_id, store_id, language_id, query, keyword FROM oc_seo_url "
        "WHERE query LIKE 'blog_%' OR query LIKE 'blog/%' OR keyword LIKE 'blog%' "
        "ORDER BY seo_url_id;\n"
        "SELECT id, category_id, title, active, date_added FROM oc_blog_posts WHERE id=13;\n"
        "SELECT id, name, active FROM oc_blog_themes ORDER BY id;"
    )
    backup_out = mysql(
        "SELECT seo_url_id, store_id, language_id, query, keyword FROM oc_seo_url "
        "WHERE query LIKE 'blog\\_%' OR query LIKE 'blog/%' OR keyword LIKE 'blog%' "
        "ORDER BY seo_url_id;"
    )
    write_text(ROOT / "db-backup" / "blog-seo-before.sql", "-- read-only snapshot\n" + backup_sql)
    write_json(
        ROOT / "db-backup" / "blog-seo-before.json",
        {
            "captured_at": utc_now(),
            "seo_rows": backup_out,
            "post13": mysql(
                "SELECT id, category_id, title, active, date_added, reading_time_minutes FROM oc_blog_posts WHERE id=13"
            ),
            "themes": mysql("SELECT id, name, active FROM oc_blog_themes ORDER BY id"),
            "note": "DB rows already correct; fix is source-only (seo_url.php)",
        },
    )

    # FTP backup current production file
    ftp = ftp_connect()
    buf = io.BytesIO()
    ftp.retrbinary(f"RETR {REMOTE}", buf.write)
    before = buf.getvalue()
    (ROOT / "source-before" / "seo_url.php").write_bytes(before)
    write_json(
        ROOT / "source-before" / "seo_url-before-meta.json",
        {"remote": REMOTE, "sha256": sha256(before), "size": len(before), "captured_at": utc_now()},
    )

    patched = LOCAL_PATCH.read_bytes()
    assert b"blog_resolved" in patched
    assert b"SITE-002 blog SEO" in patched

    # Upload
    ftp.storbinary(f"STOR {REMOTE}", io.BytesIO(patched))
    # Verify
    buf2 = io.BytesIO()
    ftp.retrbinary(f"RETR {REMOTE}", buf2.write)
    ftp.quit()
    after = buf2.getvalue()
    ok = after == patched
    write_text(
        ROOT / "ftp-apply" / "uploaded-files.txt",
        f"{REMOTE}\nsha256_before={sha256(before)}\nsha256_after={sha256(after)}\nmatch_local={ok}\n",
    )
    write_json(
        ROOT / "ftp-apply" / "upload-result.json",
        {
            "remote": REMOTE,
            "uploaded_at": utc_now(),
            "sha256_before": sha256(before),
            "sha256_local": sha256(patched),
            "sha256_after": sha256(after),
            "verified": ok,
        },
    )
    write_text(
        ROOT / "ftp-apply" / "upload-result.txt",
        f"uploaded={REMOTE}\nverified={ok}\nbefore={sha256(before)}\nafter={sha256(after)}\n",
    )

    # Clear twig/template cache only (no broad modification wipe unless needed)
    # PHP source change does not need modification cache; optional template cache irrelevant.
    # Clear seo_pro cache if present (harmless) and any opcode is N/A.
    cache_out = ssh_run(
        "ls /home/a/assum/bzpm.ru/storage/cache/cache.seo_pro* 2>/dev/null; "
        "rm -f /home/a/assum/bzpm.ru/storage/cache/cache.seo_pro* 2>/dev/null; "
        "echo SEO_PRO_CACHE_CLEARED; "
        "ls /home/a/assum/bzpm.ru/storage/modification/catalog/controller/startup/ 2>/dev/null || echo NO_MOD_STARTUP"
    )
    write_text(
        ROOT / "cache" / "cache-actions.md",
        "# Cache actions\n\n"
        "- Source file `seo_url.php` replaced via FTP (no OpenCart modification OCMOD layer for this file).\n"
        "- Removed any `cache.seo_pro*` files if present (not used by active seo_url startup).\n"
        "- Modification cache for startup: none / untouched.\n"
        "- Twig template cache: not cleared (no twig change).\n\n"
        f"## SSH evidence\n\n```\n{cache_out}\n```\n",
    )
    print("upload verified", ok)
    print(cache_out)


if __name__ == "__main__":
    main()

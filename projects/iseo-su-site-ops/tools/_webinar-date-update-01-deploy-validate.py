#!/usr/bin/env python3
"""ISEO-SU-SITE-OPS-WEBINAR-DATE-UPDATE-01 — backup, deploy HTML only, live verify."""
from __future__ import annotations

import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

try:
    import paramiko
except ImportError:
    print("FAIL: paramiko required", file=sys.stderr)
    sys.exit(2)

REPO = Path(__file__).resolve().parents[3]
LOCAL_HTML = (
    REPO
    / "projects"
    / "iseo-su-site-ops"
    / "production-source"
    / "static-html"
    / "webinar-seo-podryadchik.html"
)
SECRETS = Path(r"X:\AI MARS\local\sites\iseo-su-production\secrets.local.md")
BACKUP_DIR = Path(r"X:\AI MARS\local\sites\iseo-su-production\_webinar-date-update-01")
REMOTE_DOCROOT = "/home/n/nikel0rv/i-seo.su/public_html"
REMOTE_HTML = f"{REMOTE_DOCROOT}/webinar-seo-podryadchik.html"
LIVE_URL = "https://i-seo.su/webinar-seo-podryadchik.html"
EVIDENCE = (
    REPO
    / "projects"
    / "iseo-su-site-ops"
    / "evidence"
    / "webinar-date-update-01"
)

OLD_NEEDLES = (
    "3 сентября 2026",
    "3 сентября",
    "2026-09-03",
    "03.09.2026",
)
NEW_DATE = "10 сентября 2026"
TIME_OK = "19:00 МСК"
META_OK = (
    "Бесплатный вебинар Никиты Швакова о выборе SEO-подрядчика. "
    "10 сентября 2026 в 19:00 МСК. Разберем критерии выбора агентства, "
    "риски и реальные результаты SEO."
)


def parse_secrets(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^([a-z0-9_]+):\s*(.*)$", line.strip())
        if m:
            out[m.group(1)] = m.group(2).strip()
    for key in (
        "ftp_or_sftp_host",
        "ftp_or_sftp_username",
        "ftp_or_sftp_password",
    ):
        if key not in out:
            raise SystemExit(f"FAIL: missing secret key {key}")
    return out


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def open_sftp(secrets: dict[str, str]):
    transport = paramiko.Transport(
        (
            secrets["ftp_or_sftp_host"],
            int(secrets.get("ftp_or_sftp_port") or 22),
        )
    )
    transport.connect(
        username=secrets["ftp_or_sftp_username"],
        password=secrets["ftp_or_sftp_password"],
    )
    return transport, paramiko.SFTPClient.from_transport(transport)


def fetch_live() -> tuple[int, str]:
    req = urllib.request.Request(
        LIVE_URL,
        headers={"User-Agent": "MARS-ISEO-WEBINAR-DATE-UPDATE-01/1.0", "Cache-Control": "no-cache"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return int(resp.status), body
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return int(e.code), body


def main() -> int:
    if not LOCAL_HTML.is_file():
        print(f"FAIL: missing {LOCAL_HTML}", file=sys.stderr)
        return 2
    if not SECRETS.is_file():
        print(f"FAIL: missing secrets {SECRETS}", file=sys.stderr)
        return 2

    local_bytes = LOCAL_HTML.read_bytes()
    local_sha = sha256_bytes(local_bytes)
    local_text = local_bytes.decode("utf-8")

    if NEW_DATE not in local_text or TIME_OK not in local_text:
        print("FAIL: local HTML missing new date or time", file=sys.stderr)
        return 2
    for needle in OLD_NEEDLES:
        if needle in local_text and needle != "3 сентября":
            # "3 сентября" alone would match substrings of other text; check full old date
            pass
    if "3 сентября 2026" in local_text or "2026-09-03" in local_text or "03.09.2026" in local_text:
        print("FAIL: local HTML still has old date", file=sys.stderr)
        return 2
    if "3 сентября" in local_text:
        print("FAIL: local HTML still has short old date", file=sys.stderr)
        return 2

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    secrets = parse_secrets(SECRETS)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    transport, sftp = open_sftp(secrets)
    try:
        with sftp.open(REMOTE_HTML, "rb") as rf:
            remote_before = rf.read()
        before_sha = sha256_bytes(remote_before)
        backup_path = BACKUP_DIR / f"webinar-seo-podryadchik.html.before-{ts}.html"
        backup_path.write_bytes(remote_before)
        meta = {
            "task": "ISEO-SU-SITE-OPS-WEBINAR-DATE-UPDATE-01",
            "timestamp_utc": ts,
            "remote_path": REMOTE_HTML,
            "backup_file": str(backup_path),
            "sha256_before": before_sha,
            "sha256_local": local_sha,
            "bytes_before": len(remote_before),
        }
        (BACKUP_DIR / f"BACKUP-META-{ts}.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"BACKUP: {backup_path}")
        print(f"SHA256_BEFORE: {before_sha}")

        tmp = f"{REMOTE_HTML}.tmp-{int(time.time())}"
        with sftp.open(tmp, "wb") as wf:
            wf.write(local_bytes)
        try:
            sftp.remove(REMOTE_HTML)
        except OSError:
            pass
        sftp.rename(tmp, REMOTE_HTML)
        with sftp.open(REMOTE_HTML, "rb") as rf:
            remote_after = rf.read()
        after_sha = sha256_bytes(remote_after)
        print(f"DEPLOYED: {REMOTE_HTML}")
        print(f"SHA256_AFTER: {after_sha}")
        print(f"ALIGNED: {after_sha == local_sha}")
    finally:
        sftp.close()
        transport.close()

    time.sleep(2)
    status, live = fetch_live()
    old_full = live.count("3 сентября 2026")
    old_short = live.count("3 сентября")
    new_count = live.count(NEW_DATE)
    meta_ok = META_OK in live
    time_ok = TIME_OK in live
    title_ok = "Вебинар: Как выбрать SEO-подрядчика" in live
    h1_ok = "<h1>Как выбрать SEO-подрядчика</h1>" in live or ">Как выбрать SEO-подрядчика<" in live

    result = {
        "http": status,
        "old_full_occurrences": old_full,
        "old_short_occurrences": old_short,
        "new_date_occurrences": new_count,
        "meta_description_updated": meta_ok,
        "time_ok": time_ok,
        "title_present": title_ok,
        "h1_present": h1_ok,
        "sha256_before": before_sha,
        "sha256_after": after_sha,
        "sha256_local": local_sha,
        "production_source_aligned": after_sha == local_sha,
        "backup_dir": str(BACKUP_DIR),
    }
    out = EVIDENCE / f"live-verify-{ts}.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))

    ok = (
        status == 200
        and old_full == 0
        and old_short == 0
        and new_count >= 4
        and meta_ok
        and time_ok
        and after_sha == local_sha
    )
    print("STATUS:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

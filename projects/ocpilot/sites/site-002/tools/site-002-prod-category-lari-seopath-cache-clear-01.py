#!/usr/bin/env python3
"""Clear seo_pro category.seopath cache after lari reparent."""
from __future__ import annotations

import json
import re
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
DEPLOY = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01"
)


def parse(sub: str) -> dict[str, str]:
    text = SECRETS.read_text(encoding="utf-8")
    block = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.M).group(1)
    part = re.search(rf"^### {re.escape(sub)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.M).group(1)
    out: dict[str, str] = {}
    key = None
    for line in part.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.endswith(":"):
            key = s[:-1].strip().lower().replace(" ", "_")
            out.setdefault(key, "")
        elif key:
            out[key] = s
    return out


def ssh(cmd: str) -> str:
    s = parse("SSH")
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(
        s["host"],
        port=int(s.get("port") or 22),
        username=s["username"],
        password=s["password"],
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    _i, o, e = c.exec_command(cmd, timeout=180)
    out = o.read().decode() + e.read().decode()
    c.close()
    return out


def http_probe(url: str) -> dict:
    r = subprocess.run(
        ["curl", "-sI", "-H", "Cache-Control: no-cache", url],
        capture_output=True,
        text=True,
        timeout=60,
    )
    status = location = ""
    for ln in r.stdout.splitlines():
        if ln.startswith("HTTP/"):
            status = ln.strip()
        if ln.lower().startswith("location:"):
            location = ln.split(":", 1)[1].strip()
    return {"url": url, "status": status, "location": location}


def main() -> None:
    cache_dir = "/home/a/assum/bzpm.ru/storage/cache"
    cmd = (
        f"cd {cache_dir} && "
        "ls -1 | grep -E 'category\\.seopath|seo_pro\\.|product\\.seopath|cat-list-header' || true; "
        "rm -f cache.category.seopath* cache.seo_pro.* cache.product.seopath* cache.cat-list-header* 2>/dev/null; "
        "echo CACHE_PURGED"
    )
    purge = ssh(f"bash -lc {shlex.quote(cmd)}")

    probes = [
        http_probe("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari"),
        http_probe("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/lari"),
        http_probe("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/skladskie-lari"),
    ]

    out = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cache_purge": purge.strip(),
        "http_probes": probes,
    }
    (DEPLOY / "verification" / "seopath-cache-purge.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

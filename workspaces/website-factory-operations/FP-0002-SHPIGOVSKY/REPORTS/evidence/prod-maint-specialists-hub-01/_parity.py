# -*- coding: utf-8 -*-
"""Source ↔ production semantic parity for deployed files."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
OUT = Path(__file__).resolve().parent
WT = Path(
    r"X:\AI MARS\worktrees\fp0002-specialists-hub-01\workspaces\website-factory-operations"
    r"\FP-0002-SHPIGOVSKY\WORDPRESS"
)

PAIRS = [
    (
        WT / "theme/shpigovsky/page-templates/specialists-hub.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/page-templates/specialists-hub.php",
    ),
    (
        WT / "theme/shpigovsky/template-parts/specialist/hub-content.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/specialist/hub-content.php",
    ),
    (
        WT / "theme/shpigovsky/template-parts/specialist/hub-list.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/specialist/hub-list.php",
    ),
    (
        WT / "theme/shpigovsky/inc/fancybox-vendors.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/inc/fancybox-vendors.php",
    ),
    (
        WT / "plugins/shpigovsky-core/src/Fields/FieldGroups.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php",
    ),
    (
        WT / "plugins/shpigovsky-core/shpigovsky-core.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/shpigovsky-core.php",
    ),
    (
        WT / "acf-json/group_fp02_page_generic_content.json",
        f"{DOCROOT}/wp-content/acf-json/group_fp02_page_generic_content.json",
    ),
]


def parse_secrets(text: str) -> dict[str, str]:
    pairs: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"^[-*]?\s*`?([A-Za-z0-9_./-]+)`?\s*[:=]\s*(.*)$", line.strip())
        if match:
            pairs[match.group(1)] = match.group(2).strip().strip("`").strip('"').strip("'")
    return pairs


def getf(pairs: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = pairs.get(key)
        if value and "<OPERATOR" not in value and value.strip():
            return value.strip()
    return None


def norm(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def main() -> None:
    pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=getf(pairs, "ssh_host", "sftp_host") or "shpigovsky.beget.tech",
        port=int(getf(pairs, "ssh_port") or "22"),
        username=getf(pairs, "ssh_username", "sftp_user"),
        password=getf(pairs, "ssh_password_or_key_reference", "sftp_password", "ftp_or_sftp_password"),
        timeout=60,
        allow_agent=False,
        look_for_keys=False,
    )
    sftp = client.open_sftp()
    rows = []
    all_ok = True
    for local, remote in PAIRS:
        src = local.read_bytes()
        with sftp.open(remote, "rb") as rf:
            prod = rf.read()
        eq = norm(src) == norm(prod)
        all_ok = all_ok and eq
        rows.append(
            {
                "local": str(local),
                "remote": remote,
                "semantic_match": eq,
                "src_sha256": hashlib.sha256(norm(src)).hexdigest(),
                "prod_sha256": hashlib.sha256(norm(prod)).hexdigest(),
                "raw_equal": src == prod,
            }
        )
        print(("MATCH" if eq else "DRIFT"), remote)

    # Page config verify
    probe = f"{DOCROOT}/wp-content/uploads/.fp02-hub-verify.php"
    php = b"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
header('Content-Type: application/json; charset=utf-8');
echo wp_json_encode(array(
  'template' => get_page_template_slug(1030),
  'blog_public' => (int) get_option('blog_public'),
  'body' => get_post_meta(1030, 'generic_page_body', true),
  'post_content' => get_post_field('post_content', 1030),
  'core' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
), JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
"""
    sftp.putfo(__import__("io").BytesIO(php), probe)
    _i, o, e = client.exec_command(f"cd {DOCROOT}; /usr/local/bin/php8.2 {probe}", timeout=120)
    raw = o.read().decode("utf-8", "replace")
    try:
        sftp.remove(probe)
    except OSError:
        pass
    start = raw.find("{")
    end = raw.rfind("}")
    cfg = json.loads(raw[start : end + 1]) if start >= 0 else {"raw": raw}
    print("CONFIG", cfg)

    out = {
        "files": rows,
        "semantic_parity": "PASS" if all_ok else "FAIL",
        "page_config": cfg,
        "match_count": f"{sum(1 for r in rows if r['semantic_match'])}/{len(rows)}",
    }
    OUT.joinpath("05-parity.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print("PARITY", out["semantic_parity"], out["match_count"])
    sftp.close()
    client.close()


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Source ↔ production parity check for deployed migration files."""
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
    r"X:\AI MARS\worktrees\fp0002-specialists-canonical-url-migration-01\workspaces"
    r"\website-factory-operations\FP-0002-SHPIGOVSKY"
)

PAIRS = [
    (
        WT / "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/shpigovsky-core.php",
    ),
    (
        WT / "WORDPRESS/plugins/shpigovsky-core/src/ContentTypes/Specialist.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/ContentTypes/Specialist.php",
    ),
    (
        WT / "WORDPRESS/plugins/shpigovsky-core/src/ModuleRegistry.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/ModuleRegistry.php",
    ),
    (
        WT / "WORDPRESS/plugins/shpigovsky-core/src/Permalinks/SpecialistLegacyRedirect.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Permalinks/SpecialistLegacyRedirect.php",
    ),
    (
        WT / "WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php",
    ),
    (
        WT / "WORDPRESS/theme/shpigovsky/inc/reusable-blocks-helpers.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/inc/reusable-blocks-helpers.php",
    ),
    (
        WT / "WORDPRESS/theme/shpigovsky/inc/search-helpers.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/inc/search-helpers.php",
    ),
    (
        WT / "WORDPRESS/theme/shpigovsky/inc/sitemap-helpers.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/inc/sitemap-helpers.php",
    ),
    (
        WT / "WORDPRESS/theme/shpigovsky/inc/v9-static-content.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/inc/v9-static-content.php",
    ),
    (
        WT / "WORDPRESS/theme/shpigovsky/page-templates/specialists-hub.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/page-templates/specialists-hub.php",
    ),
    (
        WT / "WORDPRESS/theme/shpigovsky/template-parts/home/specialists.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/home/specialists.php",
    ),
    (
        WT / "WORDPRESS/theme/shpigovsky/template-parts/service/alcohol-direct-v9/specialists.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/service/alcohol-direct-v9/specialists.php",
    ),
    (
        WT / "WORDPRESS/acf-json/group_fp02_block_specialists.json",
        f"{DOCROOT}/wp-content/acf-json/group_fp02_block_specialists.json",
    ),
    (
        WT / "WORDPRESS/acf-json/group_fp02_page_home.json",
        f"{DOCROOT}/wp-content/acf-json/group_fp02_page_home.json",
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


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def norm(data: bytes) -> bytes:
    # LF/CRLF-insensitive semantic compare
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


pairs = parse_secrets(SECRETS.read_text(encoding="utf-8", errors="replace"))
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname=getf(pairs, "ssh_host") or "shpigovsky.beget.tech",
    port=int(getf(pairs, "ssh_port") or "22"),
    username=getf(pairs, "ssh_username"),
    password=getf(pairs, "ssh_password_or_key_reference"),
    timeout=60,
    allow_agent=False,
    look_for_keys=False,
)
sftp = client.open_sftp()
rows = []
for local, remote in PAIRS:
    lb = local.read_bytes()
    with sftp.open(remote, "rb") as rf:
        rb = rf.read()
    rows.append(
        {
            "remote": remote,
            "exact_match": sha(lb) == sha(rb),
            "lf_match": sha(norm(lb)) == sha(norm(rb)),
            "local_sha": sha(lb),
            "remote_sha": sha(rb),
        }
    )

# htaccess fragment parity (custom block only)
frag = (WT / "DOCS/PRODUCTION/fp-0002-legacy-redirects.htaccess.fragment").read_text(encoding="utf-8")
with sftp.open(f"{DOCROOT}/.htaccess", "rb") as rf:
    ht = rf.read().decode("utf-8", "replace")
custom = ht.split("# BEGIN WordPress")[0]
frag_n = frag.replace("\r\n", "\n").replace("\r", "\n").strip()
custom_n = custom.replace("\r\n", "\n").replace("\r", "\n").strip()
ht_row = {
    "fragment_match": frag_n == custom_n,
    "has_https_specialisty": "https://%{HTTP_HOST}/specialisty/" in custom,
}

OUT.joinpath("06-parity.json").write_text(
    json.dumps(
        {
            "files": rows,
            "all_exact": all(r["exact_match"] for r in rows),
            "all_lf": all(r["lf_match"] for r in rows),
            "htaccess": ht_row,
        },
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
)
print("exact", all(r["exact_match"] for r in rows), "lf", all(r["lf_match"] for r in rows), "ht", ht_row)
for r in rows:
    if not r["lf_match"]:
        print("MISMATCH", r["remote"])
sftp.close()
client.close()

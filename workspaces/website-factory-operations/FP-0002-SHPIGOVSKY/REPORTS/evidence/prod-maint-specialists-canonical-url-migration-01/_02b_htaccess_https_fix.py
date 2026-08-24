# -*- coding: utf-8 -*-
"""Redeploy htaccess fragment only (HTTPS Location fix)."""
from __future__ import annotations

import hashlib
import io
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
OUT = Path(__file__).resolve().parent
WT = Path(
    r"X:\AI MARS\worktrees\fp0002-specialists-canonical-url-migration-01\workspaces"
    r"\website-factory-operations\FP-0002-SHPIGOVSKY"
)
LAYER_B = Path(
    r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-maint-specialists-canonical-url-migration-01"
)
FRAGMENT = (
    WT / "DOCS/PRODUCTION/fp-0002-legacy-redirects.htaccess.fragment"
).read_text(encoding="utf-8")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")


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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_nl(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def build_htaccess(current: str) -> str:
    current_n = normalize_nl(current)
    frag_n = normalize_nl(FRAGMENT).rstrip() + "\n"
    begin = current_n.find("# BEGIN WordPress")
    if begin < 0:
        raise SystemExit("HTACCESS_NO_WP_MARKERS")
    wp_section = current_n[begin:]
    new_n = frag_n.rstrip() + "\n\n" + wp_section.lstrip("\n")
    return new_n.replace("\n", "\r\n")


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
ht_remote = f"{DOCROOT}/.htaccess"
with sftp.open(ht_remote, "rb") as rf:
    before = rf.read()
(LAYER_B / f"htaccess.before-https-fix-{STAMP}").write_bytes(before)
ht_new = build_htaccess(before.decode("utf-8", "replace")).encode("utf-8")
tmp = ht_remote + f".fp02tmp-{STAMP}"
sftp.putfo(io.BytesIO(ht_new), tmp)
try:
    sftp.remove(ht_remote)
except OSError:
    pass
sftp.rename(tmp, ht_remote)
with sftp.open(ht_remote, "rb") as rf:
    after = rf.read()
info = {
    "before_sha256": sha256_bytes(before),
    "after_sha256": sha256_bytes(after),
    "parity_ok": sha256_bytes(after) == sha256_bytes(ht_new),
    "https_host_rule": b"https://%{HTTP_HOST}/specialisty/" in after
    or b"https://%{HTTP_HOST}/specialisty/" in after,
    "snippet": after.decode("utf-8", "replace").split("# BEGIN WordPress")[0],
}
# literal check
info["has_https_rule"] = "https://%{HTTP_HOST}/specialisty/" in after.decode("utf-8", "replace")
OUT.joinpath("03b-htaccess-https-fix.json").write_text(
    json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(json.dumps(info, ensure_ascii=False, indent=2))
sftp.close()
client.close()

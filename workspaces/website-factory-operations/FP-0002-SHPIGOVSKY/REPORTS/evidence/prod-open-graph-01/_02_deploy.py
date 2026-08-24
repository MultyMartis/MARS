# -*- coding: utf-8 -*-
"""Deploy exact files for Open Graph meta wave."""
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
    r"X:\AI MARS\worktrees\fp0002-open-graph-01\workspaces"
    r"\website-factory-operations\FP-0002-SHPIGOVSKY"
)
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-open-graph-01")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
EXPECTED_CORE = "0.3.31-open-graph-01"

OPENGRAPH = WT / "WORDPRESS/plugins/shpigovsky-core/src/OpenGraph"

UPLOADS = [
    (
        WT / "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/shpigovsky-core.php",
    ),
    (
        WT / "WORDPRESS/plugins/shpigovsky-core/src/ModuleRegistry.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/ModuleRegistry.php",
    ),
    (
        OPENGRAPH / "RequestContext.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/OpenGraph/RequestContext.php",
    ),
    (
        OPENGRAPH / "ImageResolver.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/OpenGraph/ImageResolver.php",
    ),
    (
        OPENGRAPH / "TagBuilder.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/OpenGraph/TagBuilder.php",
    ),
    (
        OPENGRAPH / "OpenGraph.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/OpenGraph/OpenGraph.php",
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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


POST_DEPLOY_PHP = r"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
header('Content-Type: application/json; charset=utf-8');
if (function_exists('wp_cache_flush')) {
  wp_cache_flush();
}
echo wp_json_encode(array(
  'blog_public' => (int)get_option('blog_public'),
  'core_version' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'schema_module_enabled' => class_exists('Shpigovsky\\Core\\StructuredData\\StructuredData'),
  'og_module_enabled' => class_exists('Shpigovsky\\Core\\OpenGraph\\OpenGraph'),
  'cache_flushed' => true,
), JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
"""


def main() -> None:
    LAYER_B.mkdir(parents=True, exist_ok=True)
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
    manifest: dict = {"ts_utc": datetime.now(timezone.utc).isoformat(), "files": []}
    lint_results = []

    for local, remote in UPLOADS:
        entry = {"local": str(local), "remote": remote, "existed": False}
        if not local.exists():
            raise SystemExit(f"MISSING_LOCAL {local}")
        data = local.read_bytes()
        entry["local_sha256"] = sha256_bytes(data)
        entry["local_bytes"] = len(data)
        try:
            with sftp.open(remote, "rb") as rf:
                raw = rf.read()
            entry["existed"] = True
            entry["before_sha256"] = sha256_bytes(raw)
            safe = remote.replace("/", "__").lstrip("_")
            (LAYER_B / safe).write_bytes(raw)
        except OSError:
            entry["existed"] = False
        manifest["files"].append(entry)

        if str(local).endswith(".php"):
            tmp = f"{DOCROOT}/wp-content/uploads/.fp02-lint-{STAMP}-{local.name}"
            sftp.putfo(io.BytesIO(data), tmp)
            _i, o, e = client.exec_command(f"/usr/local/bin/php8.2 -l {tmp}", timeout=60)
            out = o.read().decode("utf-8", "replace").strip()
            err = e.read().decode("utf-8", "replace").strip()
            lint_results.append({"file": local.name, "out": out, "err": err})
            try:
                sftp.remove(tmp)
            except OSError:
                pass

    OUT.joinpath("02-php-lint.json").write_text(
        json.dumps(lint_results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("LINT", json.dumps(lint_results, ensure_ascii=False))
    if any("No syntax errors" not in (r["out"] + r["err"]) for r in lint_results):
        raise SystemExit("PHP_LINT_FAIL")

    remote_dir = f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/OpenGraph"
    try:
        sftp.stat(remote_dir)
    except OSError:
        client.exec_command(f"mkdir -p {remote_dir}", timeout=30)

    for local, remote in UPLOADS:
        data = local.read_bytes()
        tmp = remote + f".fp02tmp-{STAMP}"
        sftp.putfo(io.BytesIO(data), tmp)
        try:
            sftp.remove(remote)
        except OSError:
            pass
        sftp.rename(tmp, remote)
        for entry in manifest["files"]:
            if entry["remote"] == remote:
                with sftp.open(remote, "rb") as rf:
                    rem = rf.read()
                entry["remote_after_sha256"] = sha256_bytes(rem)
                entry["parity_ok"] = entry["remote_after_sha256"] == entry["local_sha256"]

    OUT.joinpath("03-deploy-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if not all(e.get("parity_ok") for e in manifest["files"]):
        bad = [e["remote"] for e in manifest["files"] if not e.get("parity_ok")]
        raise SystemExit(f"PARITY_FAIL {bad}")

    probe = f"{DOCROOT}/wp-content/uploads/.fp02-post-deploy-{STAMP}.php"
    sftp.putfo(io.BytesIO(POST_DEPLOY_PHP.encode("utf-8")), probe)
    _i, o, e = client.exec_command(
        f"/usr/local/bin/php8.2 -d display_errors=0 {probe}", timeout=120
    )
    raw = o.read().decode("utf-8", "replace")
    try:
        sftp.remove(probe)
    except OSError:
        pass
    start, end = raw.find("{"), raw.rfind("}")
    data = raw[start : end + 1] if start >= 0 and end > start else raw
    OUT.joinpath("04-post-deploy.json").write_text(data, encoding="utf-8")
    print(data)
    parsed = json.loads(data)
    if parsed.get("blog_public") != 1:
        raise SystemExit("INDEXING_CHANGED")
    if parsed.get("core_version") != EXPECTED_CORE:
        raise SystemExit(f"CORE_VERSION_MISMATCH {parsed.get('core_version')}")
    if not parsed.get("schema_module_enabled"):
        raise SystemExit("SCHEMA_MODULE_NOT_LOADED")
    if not parsed.get("og_module_enabled"):
        raise SystemExit("OG_MODULE_NOT_LOADED")

    sftp.close()
    client.close()
    print("DEPLOY_OK")


if __name__ == "__main__":
    main()

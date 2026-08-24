# -*- coding: utf-8 -*-
"""Exact-file deploy + remote php -l + post QA for layout polish 01."""
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
    r"X:\AI MARS\worktrees\fp0002-specialists-hub-layout-polish-01\workspaces"
    r"\website-factory-operations\FP-0002-SHPIGOVSKY\WORDPRESS"
)
LAYER_B = OUT / "layer-b-pre"
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")

UPLOADS = [
    (
        WT / "theme/shpigovsky/page-templates/specialists-hub.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/page-templates/specialists-hub.php",
    ),
    (
        WT / "theme/shpigovsky/template-parts/specialist/hub-content.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/specialist/hub-content.php",
    ),
    (
        WT / "theme/shpigovsky/template-parts/home/rehabilitation-requirements.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/home/rehabilitation-requirements.php",
    ),
    (
        WT / "theme/shpigovsky/assets/css/v9-style.css",
        f"{DOCROOT}/wp-content/themes/shpigovsky/assets/css/v9-style.css",
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

    # Layer B backup
    for local, remote in UPLOADS:
        entry = {"local": str(local), "remote": remote, "existed": False}
        try:
            with sftp.open(remote, "rb") as rf:
                raw = rf.read()
            entry["existed"] = True
            entry["before_sha256"] = sha256_bytes(raw)
            entry["before_bytes"] = len(raw)
            safe = remote.replace("/", "__").lstrip("_")
            (LAYER_B / safe).write_bytes(raw)
        except OSError:
            entry["existed"] = False
        manifest["files"].append(entry)

    # Remote PHP lint of local-copied content via temp upload
    lint_results = []
    for local, remote in UPLOADS:
        if not str(local).endswith(".php"):
            continue
        data = local.read_bytes()
        tmp = f"{DOCROOT}/wp-content/uploads/.fp02-lint-{STAMP}-{local.name}"
        sftp.putfo(io.BytesIO(data), tmp)
        _i, o, e = client.exec_command(
            f"/usr/local/bin/php8.2 -l {tmp}", timeout=60
        )
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

    # CSS sanity: expected rule present, removed decls absent in that rule
    css = (WT / "theme/shpigovsky/assets/css/v9-style.css").read_text(
        encoding="utf-8", errors="replace"
    )
    m = re.search(r"\.plain-page-content__body\s*\{([^}]*)\}", css)
    if not m:
        raise SystemExit("CSS_RULE_MISSING")
    body = m.group(1)
    css_checks = {
        "has_color": "color: var(--color-text-secondary, #475371);" in body,
        "has_margin_bottom": "margin-bottom: var(--pad-gap);" in body,
        "no_max_width_820": "max-width: 820px;" not in body,
        "no_font_size_18": "font-size: 18px;" not in body,
        "no_line_height_24": "line-height: 24px;" not in body,
        "rule_text": m.group(0),
    }
    OUT.joinpath("02-css-sanity.json").write_text(
        json.dumps(css_checks, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("CSS", css_checks)
    if not all(
        [
            css_checks["has_color"],
            css_checks["has_margin_bottom"],
            css_checks["no_max_width_820"],
            css_checks["no_font_size_18"],
            css_checks["no_line_height_24"],
        ]
    ):
        raise SystemExit("CSS_SANITY_FAIL")

    # Upload exact files
    for local, remote in UPLOADS:
        data = local.read_bytes()
        tmp = remote + f".fp02tmp-{STAMP}"
        sftp.putfo(io.BytesIO(data), tmp)
        try:
            sftp.remove(remote)
        except OSError:
            pass
        sftp.rename(tmp, remote)
        after = sha256_bytes(data)
        for entry in manifest["files"]:
            if entry["remote"] == remote:
                entry["after_sha256"] = after
                entry["after_bytes"] = len(data)
                entry["local_sha256"] = after
                entry["match"] = True

    # Parity verify
    for entry in manifest["files"]:
        with sftp.open(entry["remote"], "rb") as rf:
            rem = rf.read()
        entry["remote_after_sha256"] = sha256_bytes(rem)
        entry["parity_ok"] = entry["remote_after_sha256"] == entry.get("local_sha256")

    OUT.joinpath("03-deploy-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("DEPLOY_OK")
    for entry in manifest["files"]:
        print(
            " ",
            Path(entry["remote"]).name,
            "parity=",
            entry.get("parity_ok"),
            "existed=",
            entry.get("existed"),
        )
    if not all(e.get("parity_ok") for e in manifest["files"]):
        raise SystemExit("PARITY_FAIL")

    # Clear WP object/template caches if possible (bounded)
    probe = f"{DOCROOT}/wp-content/uploads/.fp02-layout-cache-{STAMP}.php"
    php = """<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
header('Content-Type: application/json; charset=utf-8');
if (function_exists('wp_cache_flush')) { wp_cache_flush(); }
$out = array(
  'blog_public' => (int) get_option('blog_public'),
  'page_1030_meta' => array(
    'reusable' => get_post_meta(1030, 'generic_page_reusable_blocks', true),
    'enabled' => get_post_meta(1030, 'generic_page_reusable_blocks_enabled', true),
    'lead' => get_post_meta(1030, 'generic_page_lead', true),
    'body' => get_post_meta(1030, 'generic_page_body', true),
    'template' => get_page_template_slug(1030),
  ),
  'core_version' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
);
echo wp_json_encode($out, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
"""
    sftp.putfo(io.BytesIO(php.encode("utf-8")), probe)
    _i, o, e = client.exec_command(
        f"/usr/local/bin/php8.2 -d display_errors=0 {probe}", timeout=120
    )
    raw = o.read().decode("utf-8", "replace")
    try:
        sftp.remove(probe)
    except OSError:
        pass
    start, end = raw.find("{"), raw.rfind("}")
    if start >= 0 and end > start:
        OUT.joinpath("04-post-cache-meta.json").write_text(
            raw[start : end + 1], encoding="utf-8"
        )
        print(raw[start : end + 1])

    sftp.close()
    client.close()
    print("ALL_OK")


if __name__ == "__main__":
    main()

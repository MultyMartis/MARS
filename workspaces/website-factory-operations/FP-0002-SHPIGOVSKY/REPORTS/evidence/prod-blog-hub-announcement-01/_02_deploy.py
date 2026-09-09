# -*- coding: utf-8 -*-
"""Exact-file deploy: Blog Hub dedicated announcement field."""
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
    r"X:\AI MARS\worktrees\fp0002-blog-hub-announcement-01\workspaces"
    r"\website-factory-operations\FP-0002-SHPIGOVSKY"
)
LAYER_B = Path(r"X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-blog-hub-announcement-01")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
EXPECTED_CORE = "0.3.32-blog-hub-announcement-01"

UPLOADS = [
    (
        WT / "WORDPRESS/theme/shpigovsky/inc/blog-helpers.php",
        f"{DOCROOT}/wp-content/themes/shpigovsky/inc/blog-helpers.php",
    ),
    (
        WT / "WORDPRESS/plugins/shpigovsky-core/src/Fields/FieldGroups.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php",
    ),
    (
        WT / "WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/shpigovsky-core.php",
    ),
    (
        WT / "WORDPRESS/acf-json/group_fp02_blog_post_article_meta.json",
        f"{DOCROOT}/wp-content/acf-json/group_fp02_blog_post_article_meta.json",
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
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/';
define('WP_USE_THEMES', false);
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
if (function_exists('wp_cache_flush')) {
  wp_cache_flush();
}
$acf_names = array();
if (function_exists('acf_get_fields')) {
  $fields = acf_get_fields('group_fp02_blog_post_article_meta');
  if (is_array($fields)) {
    foreach ($fields as $field) {
      $acf_names[] = array(
        'key' => $field['key'] ?? null,
        'name' => $field['name'] ?? null,
        'label' => $field['label'] ?? null,
      );
    }
  }
}
$out = array(
  'blog_public' => (int) get_option('blog_public'),
  'core_version' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'wpilot_write_enabled' => get_option('metacode_wpilot_write_enabled', null),
  'helper_exists' => function_exists('shpigovsky_get_blog_hub_announcement'),
  'acf_field_names' => $acf_names,
  'cache_flushed' => true,
);
$json = wp_json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
file_put_contents(ABSPATH . 'wp-content/uploads/.fp02-hub-ann-post-deploy.json', $json);
echo $json;
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
            (OUT / f"backup-{safe}").write_bytes(raw)
        except OSError:
            entry["existed"] = False
        manifest["files"].append(entry)

        if str(local).endswith(".php"):
            tmp = f"/tmp/fp02-lint-{STAMP}-{local.name}"
            sftp.putfo(io.BytesIO(data), tmp)
            php_lint = f"php8.2 -l {tmp} 2>/dev/null || /usr/local/bin/php8.2 -l {tmp}"
            _i, o, e = client.exec_command(php_lint, timeout=60)
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

    probe = f"/tmp/fp02-post-deploy-{STAMP}.php"
    remote_json = f"{DOCROOT}/wp-content/uploads/.fp02-hub-ann-post-deploy.json"
    sftp.putfo(io.BytesIO(POST_DEPLOY_PHP.encode("utf-8")), probe)
    php_cmd = (
        f"php8.2 -d display_errors=1 {probe} 2>/dev/null "
        f"|| /usr/local/bin/php8.2 -d display_errors=1 {probe}"
    )
    _i, o, e = client.exec_command(php_cmd, timeout=180)
    raw = o.read().decode("utf-8", "replace")
    err = e.read().decode("utf-8", "replace")
    data = ""
    try:
        with sftp.open(remote_json, "rb") as rf:
            data = rf.read().decode("utf-8", "replace")
    except OSError:
        data = ""
    try:
        sftp.remove(probe)
    except OSError:
        pass
    try:
        sftp.remove(remote_json)
    except OSError:
        pass
    if not data.strip():
        start, end = raw.find("{"), raw.rfind("}")
        data = raw[start : end + 1] if start >= 0 and end > start else raw
    OUT.joinpath("04-post-deploy.json").write_text(data, encoding="utf-8")
    OUT.joinpath("04-post-deploy-stderr.txt").write_text(err, encoding="utf-8")
    print(data)
    parsed = json.loads(data)
    if parsed.get("blog_public") != 1:
        raise SystemExit("INDEXING_CHANGED")
    if parsed.get("core_version") != EXPECTED_CORE:
        raise SystemExit(f"CORE_VERSION_MISMATCH {parsed.get('core_version')}")
    if not parsed.get("helper_exists"):
        raise SystemExit("HELPER_MISSING")
    names = [f.get("name") for f in (parsed.get("acf_field_names") or [])]
    if "article_hub_announcement" not in names:
        raise SystemExit("ACF_FIELD_MISSING")
    if "article_lead" not in names:
        raise SystemExit("LEAD_FIELD_MISSING")

    sftp.close()
    client.close()
    print("DEPLOY_OK")


if __name__ == "__main__":
    main()

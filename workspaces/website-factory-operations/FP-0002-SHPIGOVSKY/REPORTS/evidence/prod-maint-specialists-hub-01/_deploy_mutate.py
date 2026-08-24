# -*- coding: utf-8 -*-
"""Deploy Specialists Hub files + bounded Page #1030 config mutation."""
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
    r"X:\AI MARS\worktrees\fp0002-specialists-hub-01\workspaces\website-factory-operations"
    r"\FP-0002-SHPIGOVSKY\WORDPRESS"
)
PLACEHOLDER_HTML = (
    "<!-- wp:paragraph --><p>Раздел находится в подготовке. "
    "Здесь будет опубликована информация по теме страницы.</p><!-- /wp:paragraph -->"
)
PLACEHOLDER_TEXT = (
    "Раздел находится в подготовке. Здесь будет опубликована информация по теме страницы."
)

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
        f"{DOCROOT}/wp-content/themes/shpigovsky/acf-json/group_fp02_page_generic_content.json"
        if False
        else f"{DOCROOT}/wp-content/plugins/shpigovsky-core/acf-json/group_fp02_page_generic_content.json",
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


def find_acf_json_remote(sftp, client) -> str | None:
    candidates = [
        f"{DOCROOT}/wp-content/themes/shpigovsky/acf-json/group_fp02_page_generic_content.json",
        f"{DOCROOT}/wp-content/plugins/shpigovsky-core/acf-json/group_fp02_page_generic_content.json",
        f"{DOCROOT}/wp-content/acf-json/group_fp02_page_generic_content.json",
    ]
    # Also locate via find
    _i, o, _e = client.exec_command(
        f"find {DOCROOT}/wp-content -name 'group_fp02_page_generic_content.json' 2>/dev/null | head -5",
        timeout=60,
    )
    found = [ln.strip() for ln in o.read().decode().splitlines() if ln.strip()]
    for path in found + candidates:
        try:
            sftp.stat(path)
            return path
        except OSError:
            continue
    return None


MUTATE_PHP = r'''<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
header('Content-Type: application/json; charset=utf-8');

$placeholder_html = "<!-- wp:paragraph --><p>Раздел находится в подготовке. Здесь будет опубликована информация по теме страницы.</p><!-- /wp:paragraph -->";
$placeholder_text = "Раздел находится в подготовке. Здесь будет опубликована информация по теме страницы.";

$page_id = 1030;
$page = get_post($page_id);
$out = array('ok' => false);
if (!$page) {
  $out['error'] = 'missing_page';
  echo wp_json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
  exit;
}

$before = array(
  'template' => get_page_template_slug($page_id),
  'post_content' => $page->post_content,
  'generic_page_body' => get_post_meta($page_id, 'generic_page_body', true),
  'generic_page_lead' => get_post_meta($page_id, 'generic_page_lead', true),
  'generic_page_reusable_blocks' => get_post_meta($page_id, 'generic_page_reusable_blocks', true),
  'page_layout_mode' => get_post_meta($page_id, 'page_layout_mode', true),
  'seo_title' => get_post_meta($page_id, 'seo_title', true),
  'seo_description' => get_post_meta($page_id, 'seo_description', true),
  'post_title' => $page->post_title,
  'post_name' => $page->post_name,
  'post_status' => $page->post_status,
);

$actions = array();

$new_template = 'page-templates/specialists-hub.php';
$cur_template = (string) $before['template'];
if ($cur_template !== $new_template) {
  update_post_meta($page_id, '_wp_page_template', $new_template);
  $actions[] = 'template_set_specialists_hub';
} else {
  $actions[] = 'template_already_specialists_hub';
}

$body = is_string($before['generic_page_body']) ? $before['generic_page_body'] : '';
$body_trim = trim($body);
$is_placeholder_body = ($body_trim === $placeholder_html) || ($body_trim === $placeholder_text) || (strip_tags($body_trim) === $placeholder_text);
if ($is_placeholder_body) {
  update_post_meta($page_id, 'generic_page_body', '');
  $actions[] = 'cleared_generic_page_body_placeholder';
} elseif ($body_trim !== '') {
  $actions[] = 'preserved_generic_page_body_non_placeholder';
} else {
  $actions[] = 'generic_page_body_already_empty';
}

$pc = is_string($before['post_content']) ? $before['post_content'] : '';
$pc_trim = trim($pc);
$is_placeholder_pc = ($pc_trim === $placeholder_html) || ($pc_trim === $placeholder_text) || (strip_tags($pc_trim) === $placeholder_text);
if ($is_placeholder_pc) {
  wp_update_post(array(
    'ID' => $page_id,
    'post_content' => '',
  ));
  $actions[] = 'cleared_post_content_placeholder';
} elseif ($pc_trim !== '') {
  $actions[] = 'preserved_post_content_non_placeholder';
} else {
  $actions[] = 'post_content_already_empty';
}

clean_post_cache($page_id);
wp_cache_flush();

$page2 = get_post($page_id);
$after = array(
  'template' => get_page_template_slug($page_id),
  'post_content' => $page2 ? $page2->post_content : null,
  'generic_page_body' => get_post_meta($page_id, 'generic_page_body', true),
  'generic_page_lead' => get_post_meta($page_id, 'generic_page_lead', true),
  'generic_page_reusable_blocks' => get_post_meta($page_id, 'generic_page_reusable_blocks', true),
  'page_layout_mode' => get_post_meta($page_id, 'page_layout_mode', true),
  'seo_title' => get_post_meta($page_id, 'seo_title', true),
  'seo_description' => get_post_meta($page_id, 'seo_description', true),
  'post_title' => $page2 ? $page2->post_title : null,
  'post_name' => $page2 ? $page2->post_name : null,
  'post_status' => $page2 ? $page2->post_status : null,
  'permalink' => get_permalink($page_id),
  'blog_public' => (int) get_option('blog_public'),
  'core_version' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
);

$out = array(
  'ok' => true,
  'actions' => $actions,
  'before' => $before,
  'after' => $after,
);
echo wp_json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
'''


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

    def run(cmd: str) -> str:
        _i, o, e = client.exec_command(cmd, timeout=180)
        out = o.read().decode("utf-8", errors="replace")
        err = e.read().decode("utf-8", errors="replace")
        code = o.channel.recv_exit_status()
        return out + (("\n[stderr]\n" + err) if err else "") + f"\n[exit]={code}\n"

    # Ensure specialist template-parts dir exists.
    try:
        sftp.stat(f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/specialist")
    except OSError:
        sftp.mkdir(f"{DOCROOT}/wp-content/themes/shpigovsky/template-parts/specialist")

    acf_remote = find_acf_json_remote(sftp, client)
    print("acf_json_remote=", acf_remote)

    deploy_manifest = []
    for local, remote in UPLOADS:
        if local.name == "group_fp02_page_generic_content.json":
            if not acf_remote:
                print("SKIP acf-json — not present on production (PHP FieldGroups is runtime owner)")
                continue
            remote = acf_remote
        if not local.is_file():
            raise SystemExit(f"missing local {local}")
        data = local.read_bytes()
        # Backup remote if exists
        bak_dir = OUT / "layer-b-pre-deploy"
        bak_dir.mkdir(parents=True, exist_ok=True)
        bak_name = remote.replace("/", "__")
        try:
            sftp.get(remote, str(bak_dir / (bak_name[-120:])))
            existed = True
        except OSError:
            existed = False
        sftp.putfo(io.BytesIO(data), remote)
        # Verify
        with sftp.open(remote, "rb") as rf:
            remote_data = rf.read()
        ok = hashlib.sha256(remote_data).hexdigest() == hashlib.sha256(data).hexdigest()
        # Lint PHP
        lint = ""
        if remote.endswith(".php"):
            lint = run(f"/usr/local/bin/php8.2 -l {remote}")
        entry = {
            "local": str(local),
            "remote": remote,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "existed_before": existed,
            "parity_after_upload": ok,
            "lint": lint.strip()[-200:],
        }
        deploy_manifest.append(entry)
        print("UPLOADED", remote, "ok=", ok)

    OUT.joinpath("02-deploy-manifest.json").write_text(
        json.dumps(deploy_manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Mutate page 1030
    remote_probe = f"{DOCROOT}/wp-content/uploads/.fp02-hub-mutate-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}.php"
    sftp.putfo(io.BytesIO(MUTATE_PHP.encode("utf-8")), remote_probe)
    raw = run(f"cd {DOCROOT}; /usr/local/bin/php8.2 -d display_errors=1 {remote_probe}")
    try:
        sftp.remove(remote_probe)
    except OSError:
        pass
    OUT.joinpath("03-mutate-raw.txt").write_text(raw, encoding="utf-8")
    start = raw.find("{")
    end = raw.rfind("}")
    if start >= 0 and end > start:
        data = json.loads(raw[start : end + 1])
        OUT.joinpath("03-mutate.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print("MUTATE", data.get("ok"), data.get("actions"))
        print("after_template", (data.get("after") or {}).get("template"))
        print("blog_public", (data.get("after") or {}).get("blog_public"))
        print("core", (data.get("after") or {}).get("core_version"))
    else:
        print("MUTATE_FAIL")
        print(raw[:2000])

    sftp.close()
    client.close()


if __name__ == "__main__":
    main()

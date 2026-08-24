# -*- coding: utf-8 -*-
"""Deploy files + DB slug/option + htaccess + rewrite flush for specialists URL migration."""
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
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")

UPLOADS = [
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

FRAGMENT = (
    WT / "DOCS/PRODUCTION/fp-0002-legacy-redirects.htaccess.fragment"
).read_text(encoding="utf-8")


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
    """Replace FP-0002 legacy redirect block; preserve WordPress section + CRLF."""
    current_n = normalize_nl(current)
    frag_n = normalize_nl(FRAGMENT).rstrip() + "\n"
    begin = current_n.find("# BEGIN WordPress")
    if begin < 0:
        raise SystemExit("HTACCESS_NO_WP_MARKERS")
    wp_section = current_n[begin:]
    # Keep only one blank line between custom block and WP.
    new_n = frag_n.rstrip() + "\n\n" + wp_section.lstrip("\n")
    # Production historically uses CRLF.
    return new_n.replace("\n", "\r\n")


MUTATE_PHP = r"""<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
header('Content-Type: application/json; charset=utf-8');
global $wpdb;

$before = array(
  'page_1030' => array(
    'post_name' => get_post_field('post_name', 1030),
    'permalink' => get_permalink(1030),
    'template' => get_page_template_slug(1030),
    'reusable_enabled' => get_post_meta(1030, 'generic_page_reusable_blocks_enabled', true),
    'reusable' => get_post_meta(1030, 'generic_page_reusable_blocks', true),
  ),
  'all_link' => $wpdb->get_var("SELECT option_value FROM {$wpdb->options} WHERE option_name='fp02-block-specialists_specialists_all_link_url'"),
  'cpt_rewrite' => get_post_type_object('specialist') ? get_post_type_object('specialist')->rewrite : null,
  'blog_public' => (int) get_option('blog_public'),
  'core_version' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
);

// 1) Page #1030 slug migration (same object).
$slug_result = null;
$p = get_post(1030);
if ($p && 'page' === $p->post_type) {
  if ('specialisty' !== $p->post_name) {
    $r = wp_update_post(array(
      'ID' => 1030,
      'post_name' => 'specialisty',
    ), true);
    $slug_result = is_wp_error($r) ? $r->get_error_message() : 'updated';
  } else {
    $slug_result = 'already_specialisty';
  }
  clean_post_cache(1030);
}

// 2) Clear stale hardcoded all-specialists link (prefer generated permalink).
$opt_name = 'fp02-block-specialists_specialists_all_link_url';
$old_opt = $wpdb->get_var($wpdb->prepare('SELECT option_value FROM ' . $wpdb->options . ' WHERE option_name=%s', $opt_name));
$opt_action = 'unchanged';
if (is_string($old_opt) && false !== strpos($old_opt, 'specyalisty')) {
  update_option($opt_name, '', false);
  $opt_action = 'cleared_empty';
}

// 3) Soft rewrite flush + set migration flag (also set by Specialist::maybe_flush_rewrites_once).
flush_rewrite_rules(false);
update_option('fp02_specialist_cpt_rewrite_flushed_specialisty_v1', '1', false);
if (function_exists('wp_cache_flush')) {
  wp_cache_flush();
}

$rewrite = get_option('rewrite_rules');
$has_new = false;
$has_old = false;
if (is_array($rewrite)) {
  foreach (array_keys($rewrite) as $k) {
    if (strpos($k, 'specialisty') !== false) { $has_new = true; }
    if (strpos($k, 'specyalisty') !== false) { $has_old = true; }
  }
}

$specs = get_posts(array(
  'post_type' => 'specialist',
  'post_status' => 'publish',
  'numberposts' => 50,
  'orderby' => array('menu_order' => 'ASC', 'title' => 'ASC'),
));
$spec_out = array();
foreach ($specs as $s) {
  $spec_out[] = array(
    'ID' => $s->ID,
    'post_name' => $s->post_name,
    'permalink' => get_permalink($s),
  );
}

$after = array(
  'page_1030' => array(
    'post_name' => get_post_field('post_name', 1030),
    'permalink' => get_permalink(1030),
    'template' => get_page_template_slug(1030),
    'reusable_enabled' => get_post_meta(1030, 'generic_page_reusable_blocks_enabled', true),
    'reusable' => get_post_meta(1030, 'generic_page_reusable_blocks', true),
    'title' => get_the_title(1030),
  ),
  'all_link' => $wpdb->get_var($wpdb->prepare('SELECT option_value FROM ' . $wpdb->options . ' WHERE option_name=%s', $opt_name)),
  'cpt_rewrite' => get_post_type_object('specialist') ? get_post_type_object('specialist')->rewrite : null,
  'blog_public' => (int) get_option('blog_public'),
  'core_version' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'rewrite_has_specialisty' => $has_new,
  'rewrite_has_specyalisty' => $has_old,
  'specialists' => $spec_out,
);

echo wp_json_encode(array(
  'before' => $before,
  'slug_result' => $slug_result,
  'opt_action' => $opt_action,
  'opt_before' => $old_opt,
  'after' => $after,
), JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
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

    # Layer B + lint PHP
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

    # Upload files
    for local, remote in UPLOADS:
        data = local.read_bytes()
        # Ensure parent dir for new file
        parent = str(Path(remote).as_posix().rsplit("/", 1)[0])
        try:
            sftp.stat(parent)
        except OSError:
            # mkdir -p style
            parts = parent.strip("/").split("/")
            cur = ""
            for part in parts:
                cur += "/" + part
                try:
                    sftp.stat(cur)
                except OSError:
                    sftp.mkdir(cur)
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

    # htaccess
    ht_remote = f"{DOCROOT}/.htaccess"
    with sftp.open(ht_remote, "rb") as rf:
        ht_before = rf.read()
    (LAYER_B / "htaccess.production.before").write_bytes(ht_before)
    ht_new = build_htaccess(ht_before.decode("utf-8", "replace"))
    ht_bytes = ht_new.encode("utf-8")
    (LAYER_B / "htaccess.production.after-planned").write_bytes(ht_bytes)
    tmp = ht_remote + f".fp02tmp-{STAMP}"
    sftp.putfo(io.BytesIO(ht_bytes), tmp)
    try:
        sftp.remove(ht_remote)
    except OSError:
        pass
    sftp.rename(tmp, ht_remote)
    with sftp.open(ht_remote, "rb") as rf:
        ht_after = rf.read()
    ht_info = {
        "before_sha256": sha256_bytes(ht_before),
        "after_sha256": sha256_bytes(ht_after),
        "planned_sha256": sha256_bytes(ht_bytes),
        "parity_ok": sha256_bytes(ht_after) == sha256_bytes(ht_bytes),
        "has_specyalisty_rule": b"specyalisty" in ht_after,
        "has_specialisty_target": b"/specialisty/" in ht_after,
        "wp_markers_intact": b"# BEGIN WordPress" in ht_after and b"# END WordPress" in ht_after,
    }
    OUT.joinpath("03-htaccess.json").write_text(
        json.dumps(ht_info, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("HTACCESS", ht_info)
    if not ht_info["parity_ok"] or not ht_info["wp_markers_intact"]:
        raise SystemExit("HTACCESS_FAIL")

    OUT.joinpath("03-deploy-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if not all(e.get("parity_ok") for e in manifest["files"]):
        bad = [e["remote"] for e in manifest["files"] if not e.get("parity_ok")]
        raise SystemExit(f"PARITY_FAIL {bad}")

    # DB mutate + flush
    probe = f"{DOCROOT}/wp-content/uploads/.fp02-url-mutate-{STAMP}.php"
    sftp.putfo(io.BytesIO(MUTATE_PHP.encode("utf-8")), probe)
    _i, o, e = client.exec_command(
        f"/usr/local/bin/php8.2 -d display_errors=0 {probe}", timeout=180
    )
    raw = o.read().decode("utf-8", "replace")
    err = e.read().decode("utf-8", "replace")
    try:
        sftp.remove(probe)
    except OSError:
        pass
    start, end = raw.find("{"), raw.rfind("}")
    data = raw[start : end + 1] if start >= 0 and end > start else raw
    OUT.joinpath("04-db-mutate.json").write_text(data, encoding="utf-8")
    print(data[:4000])
    if err.strip():
        print("ERR", err[:500])
    parsed = json.loads(data)
    if parsed.get("after", {}).get("page_1030", {}).get("post_name") != "specialisty":
        raise SystemExit("SLUG_FAIL")
    if not parsed.get("after", {}).get("rewrite_has_specialisty"):
        raise SystemExit("REWRITE_NEW_MISSING")
    if parsed.get("after", {}).get("rewrite_has_specyalisty"):
        raise SystemExit("REWRITE_OLD_STILL_PRESENT")
    if parsed.get("after", {}).get("blog_public") != 1:
        raise SystemExit("INDEXING_CHANGED")

    sftp.close()
    client.close()
    print("DEPLOY_MUTATE_OK")


if __name__ == "__main__":
    main()

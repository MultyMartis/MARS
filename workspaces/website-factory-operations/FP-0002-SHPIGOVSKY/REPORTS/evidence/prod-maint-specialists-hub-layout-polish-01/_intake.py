# -*- coding: utf-8 -*-
"""Fresh production intake for Specialists Hub layout polish 01."""
from __future__ import annotations

import io
import json
import re
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
OUT = Path(__file__).resolve().parent


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


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
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

    probe = f"{DOCROOT}/wp-content/uploads/.fp02-layout-intake-01.php"
    php = """<?php
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';
header('Content-Type: application/json; charset=utf-8');
$theme = wp_get_theme();
$out = array(
  'page_id' => 1030,
  'template' => get_page_template_slug(1030),
  'permalink' => get_permalink(1030),
  'blog_public' => (int) get_option('blog_public'),
  'core_version' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'theme_version' => $theme ? $theme->get('Version') : null,
  'theme_stylesheet' => get_stylesheet(),
  'meta' => array(),
);
$keys = array(
  'generic_page_lead',
  'generic_page_body',
  'generic_page_reusable_blocks',
  'generic_page_reusable_blocks_enabled',
  'page_layout_mode',
  '_wp_page_template',
);
foreach ($keys as $k) {
  $out['meta'][$k] = get_post_meta(1030, $k, true);
  $out['meta']['_'.$k] = get_post_meta(1030, '_'.$k, true);
}
global $wpdb;
$table = $wpdb->prefix . 'fp02_user_activity_log';
$exists = $wpdb->get_var($wpdb->prepare('SHOW TABLES LIKE %s', $table));
$out['activity_table_exists'] = (bool) $exists;
if ($exists) {
  $rows = $wpdb->get_results(
    $wpdb->prepare(
      'SELECT id, created_at, user_id, action, object_type, object_id, summary FROM ' . $table .
      ' WHERE object_id = %d ORDER BY id DESC LIMIT 15',
      1030
    ),
    ARRAY_A
  );
  $out['activity_page_1030'] = $rows ? $rows : array();
}
echo wp_json_encode($out, JSON_UNESCAPED_UNICODE|JSON_PRETTY_PRINT);
"""
    sftp.putfo(io.BytesIO(php.encode("utf-8")), probe)
    _i, o, e = client.exec_command(
        f"/usr/local/bin/php8.2 -d display_errors=0 {probe}", timeout=120
    )
    raw = o.read().decode("utf-8", "replace")
    err = e.read().decode("utf-8", "replace")
    try:
        sftp.remove(probe)
    except OSError:
        pass
    if err.strip():
        print("PHP_ERR", err[:800])
    start, end = raw.find("{"), raw.rfind("}")
    if start >= 0 and end > start:
        data = raw[start : end + 1]
        OUT.joinpath("01-intake.json").write_text(data, encoding="utf-8")
        print(data)
    else:
        print("RAW", raw[:2000])
        raise SystemExit(1)

    # Live HTML via remote curl (avoid local head / PowerShell pipe issues).
    cmd = (
        "python3 - <<'PY'\n"
        "import urllib.request\n"
        "req=urllib.request.Request('https://shpigovsky.ru/specyalisty/', headers={'User-Agent':'MARS-intake'})\n"
        "html=urllib.request.urlopen(req, timeout=60).read().decode('utf-8','replace')\n"
        "print(html)\n"
        "PY"
    )
    _i, o, e = client.exec_command(cmd, timeout=90)
    html = o.read().decode("utf-8", "replace")
    OUT.joinpath("01-hub-html-snippet.txt").write_text(html[:250000], encoding="utf-8")
    rehab_m = re.search(
        r"<section[^>]*home-rehabilitation-requirements[^>]*>[\s\S]{0,500}", html
    )
    checks = {
        "http_len": len(html),
        "has_internal_page_nav": "internal-page-nav" in html,
        "has_plain_page_content__body": "plain-page-content__body" in html,
        "has_rehab_class": "home-rehabilitation-requirements" in html,
        "has_is_revealed": "is-revealed" in html and "home-rehabilitation-requirements" in html,
        "rehab_open_snippet": rehab_m.group(0)[:500] if rehab_m else None,
        "rehab_has_inner_container": bool(
            rehab_m and re.search(r'class=["\']container["\']', rehab_m.group(0))
        ),
        "has_specialists_hub": "specialists-hub" in html,
        "has_h1": bool(re.search(r"<h1[^>]*>\s*Специалисты", html)),
        "card_grid_hits": html.count("home-feature-grid__card"),
    }
    OUT.joinpath("01-hub-markers.json").write_text(
        json.dumps(checks, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(checks, ensure_ascii=False, indent=2))

    for label, url in (
        ("specyalisty", "https://shpigovsky.ru/specyalisty/"),
        ("specialisty", "https://shpigovsky.ru/specialisty/"),
        ("robots", "https://shpigovsky.ru/robots.txt"),
    ):
        _i, o, e = client.exec_command(
            f"curl -sI -A MARS-intake '{url}'", timeout=30
        )
        headers = o.read().decode("utf-8", "replace")
        OUT.joinpath(f"01-{label}-headers.txt").write_text(headers, encoding="utf-8")
        print(f"=== {label} ===")
        print(headers.splitlines()[:12])

    # Current CSS rule on production for plain-page-content__body
    css_remote = f"{DOCROOT}/wp-content/themes/shpigovsky/assets/css/v9-style.css"
    with sftp.open(css_remote, "rb") as rf:
        css = rf.read().decode("utf-8", "replace")
    m = re.search(r"\.plain-page-content__body\s*\{[^}]*\}", css)
    OUT.joinpath("01-prod-plain-body-rule.txt").write_text(
        m.group(0) if m else "NOT_FOUND", encoding="utf-8"
    )
    print("CSS_RULE", m.group(0) if m else "NOT_FOUND")

    sftp.close()
    client.close()
    print("INTAKE_OK")


if __name__ == "__main__":
    main()

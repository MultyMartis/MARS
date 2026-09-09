# -*- coding: utf-8 -*-
"""Closeout Admin field object + hero Lead + Schema description. Read-only."""
from __future__ import annotations

import io
import json
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
OUT = Path(__file__).resolve().parent
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")

LEAD_1745_PREFIX = "Зависимость всегда окружали мифы"
LEAD_750_PREFIX = "Есть расхожее мнение, что алкоголизм"
SEO_1745_PREFIX = "Разберем анализ набора генетических маркеров"
SEO_750_PREFIX = "Почему при алкоголизме сила воли"


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


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "FP02-hub-ann-closeout/1.0"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", "replace")


def extract_hero_excerpt(html: str) -> str:
    match = re.search(
        r'blog-article-hero__excerpt[^>]*>[\s\S]*?<p[^>]*>([\s\S]*?)</p>',
        html,
        re.I,
    )
    if not match:
        match = re.search(r'blog-article-hero__excerpt[^>]*>([\s\S]*?)</div>', html, re.I)
    text = re.sub(r"<[^>]+>", " ", match.group(1) if match else "")
    return re.sub(r"\s+", " ", text).strip()


def extract_jsonld_descriptions(html: str) -> list[str]:
    descriptions: list[str] = []
    for block in re.findall(
        r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>([\s\S]*?)</script>',
        html,
        re.I,
    ):
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        nodes = data.get("@graph", [data]) if isinstance(data, dict) else data
        if not isinstance(nodes, list):
            nodes = [nodes]
        for node in nodes:
            if isinstance(node, dict) and isinstance(node.get("description"), str):
                descriptions.append(node["description"])
    return descriptions


CLOSEOUT_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/';
define('WP_USE_THEMES', false);
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';

$field = function_exists('get_field_object') ? get_field_object('article_hub_announcement', 1745) : null;
$lead_field = function_exists('get_field_object') ? get_field_object('article_lead', 1745) : null;
$group = acf_get_field_group('group_fp02_blog_post_article_meta');
$names = array();
if (is_array($group) && function_exists('acf_get_fields')) {
  foreach ((array) acf_get_fields($group) as $item) {
    $names[] = array(
      'key' => $item['key'] ?? null,
      'name' => $item['name'] ?? null,
      'label' => $item['label'] ?? null,
      'type' => $item['type'] ?? null,
    );
  }
}
$out = array(
  'blog_public' => (int) get_option('blog_public'),
  'core_version' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'hub_field' => array(
    'key' => is_array($field) ? ($field['key'] ?? null) : null,
    'name' => is_array($field) ? ($field['name'] ?? null) : null,
    'label' => is_array($field) ? ($field['label'] ?? null) : null,
    'type' => is_array($field) ? ($field['type'] ?? null) : null,
    'instructions' => is_array($field) ? ($field['instructions'] ?? null) : null,
    'parent' => is_array($field) ? ($field['parent'] ?? null) : null,
    'value' => is_array($field) ? ($field['value'] ?? null) : null,
  ),
  'lead_field' => array(
    'key' => is_array($lead_field) ? ($lead_field['key'] ?? null) : null,
    'name' => is_array($lead_field) ? ($lead_field['name'] ?? null) : null,
    'label' => is_array($lead_field) ? ($lead_field['label'] ?? null) : null,
  ),
  'group_title' => is_array($group) ? ($group['title'] ?? null) : null,
  'field_order_names' => array_values(array_filter(array_map(static function ($row) {
    return $row['name'] ?? null;
  }, $names))),
  'modified_1745' => get_post_modified_time('Y-m-d H:i:s', true, 1745),
  'modified_750' => get_post_modified_time('Y-m-d H:i:s', true, 750),
  'excerpt_1745' => get_post_field('post_excerpt', 1745),
  'excerpt_750' => get_post_field('post_excerpt', 750),
  'hub_meta_1745' => get_post_meta(1745, 'article_hub_announcement', true),
  'hub_meta_750' => get_post_meta(750, 'article_hub_announcement', true),
);
$json = wp_json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
file_put_contents(ABSPATH . 'wp-content/uploads/.fp02-hub-ann-closeout.json', $json);
echo $json;
"""


def main() -> None:
    pages = {}
    for slug, url in (
        ("1745", "https://shpigovsky.ru/blog/demo-pagination-article-01/"),
        ("750", "https://shpigovsky.ru/blog/lechenie-alkogolnoy-zavisimosti-pochemu-sila-voli-ni-pri-chem/"),
    ):
        html = fetch(url)
        hero = extract_hero_excerpt(html)
        descriptions = extract_jsonld_descriptions(html)
        pages[slug] = {
            "url": url,
            "hero_excerpt_preview": hero[:400],
            "hero_has_lead": hero.startswith(LEAD_1745_PREFIX if slug == "1745" else LEAD_750_PREFIX),
            "schema_descriptions": descriptions[:8],
            "schema_uses_seo": any(
                d.startswith(SEO_1745_PREFIX if slug == "1745" else SEO_750_PREFIX) for d in descriptions
            ),
            "html_has_hub_field_name": "article_hub_announcement" in html,
            "html_has_qa_marker": "QA-HUB-ANN-1745-PRIORITY-PROBE" in html,
        }

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
    probe = f"/tmp/fp02-hub-ann-closeout-{STAMP}.php"
    remote_json = f"{DOCROOT}/wp-content/uploads/.fp02-hub-ann-closeout.json"
    sftp.putfo(io.BytesIO(CLOSEOUT_PHP.encode("utf-8")), probe)
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
    sftp.close()
    client.close()
    if not data.strip():
        start, end = raw.find("{"), raw.rfind("}")
        data = raw[start : end + 1] if start >= 0 and end > start else raw
    admin = json.loads(data)
    names = admin.get("field_order_names") or []
    result = {
        "ts_utc": datetime.now(timezone.utc).isoformat(),
        "pages": pages,
        "admin": admin,
        "checks": {
            "blog_public_open": admin.get("blog_public") == 1,
            "hub_field_present": "article_hub_announcement" in names,
            "hub_after_lead": names[names.index("article_lead") + 1] == "article_hub_announcement"
            if "article_lead" in names
            else False,
            "hub_empty_1745": not bool(admin.get("hub_meta_1745")),
            "hub_empty_750": not bool(admin.get("hub_meta_750")),
            "hero_1745_lead": pages["1745"]["hero_has_lead"],
            "hero_750_lead": pages["750"]["hero_has_lead"],
            "schema_1745_seo": pages["1745"]["schema_uses_seo"],
            "schema_750_seo": pages["750"]["schema_uses_seo"],
            "no_hub_leak_html": not pages["1745"]["html_has_hub_field_name"]
            and not pages["750"]["html_has_hub_field_name"],
            "no_qa_residue": not pages["1745"]["html_has_qa_marker"] and not pages["750"]["html_has_qa_marker"],
        },
        "stderr": err,
    }
    OUT.joinpath("08-closeout-admin-schema.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(result["checks"], ensure_ascii=False, indent=2))
    if not all(result["checks"].values()):
        raise SystemExit("CLOSEOUT_FAIL")
    print("CLOSEOUT_OK")


if __name__ == "__main__":
    main()

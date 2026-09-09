# -*- coding: utf-8 -*-
"""Fresh read-only production/Olya intake before Blog Hub announcement field."""
from __future__ import annotations

import hashlib
import io
import json
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import paramiko

SECRETS = Path(r"X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md")
DOCROOT = "/home/s/shpigovsky/shpigovsky.ru/public_html"
OUT = Path(__file__).resolve().parent
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
REMOTE_PROBE = f"/tmp/fp02-hub-ann-intake-{STAMP}.php"

PUBLIC_URLS = [
    "https://shpigovsky.ru/",
    "https://shpigovsky.ru/robots.txt",
    "https://shpigovsky.ru/blog/",
    "https://shpigovsky.ru/blog/demo-pagination-article-01/",
    "https://shpigovsky.ru/blog/lechenie-alkogolnoy-zavisimosti-pochemu-sila-voli-ni-pri-chem/",
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


def fetch(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "FP02-hub-ann-intake/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            body = resp.read()
            status = resp.status
            final_url = resp.geturl()
    except urllib.error.HTTPError as exc:
        body = exc.read() if exc.fp else b""
        status = exc.code
        final_url = url
    text = body.decode("utf-8", "replace")
    return {
        "url": url,
        "status": status,
        "final_url": final_url,
        "bytes": len(body),
        "sha256": sha256_bytes(body),
        "title": (re.search(r"<title>([^<]*)</title>", text, re.I) or [None, ""])[1],
        "meta_description": (
            re.search(r'<meta\s+name="description"\s+content="([^"]*)"', text, re.I) or [None, ""]
        )[1],
        "og_description": (
            re.search(r'<meta\s+property="og:description"\s+content="([^"]*)"', text, re.I) or [None, ""]
        )[1],
        "jsonld_count": len(re.findall(r"application/ld\+json", text)),
        "preview": text[:2500],
        "text": text,
    }


PROBE_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/';
define('WP_USE_THEMES', false);
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';

$clip = static function ($v, $max = 400) {
  if ($v === null || is_bool($v) || is_int($v) || is_float($v)) {
    return $v;
  }
  $s = is_string($v) ? $v : wp_json_encode($v);
  if (!is_string($s)) {
    $s = (string) $v;
  }
  return strlen($s) > $max ? substr($s, 0, $max) . '...[truncated]' : $s;
};

$post_snapshot = static function ($post_id) use ($clip) {
  $post = get_post($post_id);
  if (!$post instanceof WP_Post) {
    return array('missing' => true, 'ID' => (int) $post_id);
  }
  $keys = array(
    'article_hub_announcement',
    'article_lead',
    'article_eyebrow',
    'fp02_seo_title',
    'fp02_seo_description',
    'seo_title',
    'seo_description',
  );
  $meta = array();
  foreach ($keys as $key) {
    $meta[$key] = get_post_meta($post_id, $key, true);
  }
  $card = null;
  if (function_exists('shpigovsky_build_blog_archive_card_args')) {
    $card = shpigovsky_build_blog_archive_card_args($post_id);
    if (is_array($card) && isset($card['excerpt'])) {
      $card = array(
        'title' => $card['title'] ?? null,
        'url' => $card['url'] ?? null,
        'excerpt' => $card['excerpt'] ?? null,
      );
    }
  }
  $lead = function_exists('shpigovsky_get_article_lead') ? shpigovsky_get_article_lead($post_id) : null;
  return array(
    'ID' => (int) $post->ID,
    'post_title' => $post->post_title,
    'post_name' => $post->post_name,
    'post_status' => $post->post_status,
    'post_modified_gmt' => $post->post_modified_gmt,
    'post_date_gmt' => $post->post_date_gmt,
    'post_author' => (int) $post->post_author,
    'permalink' => get_permalink($post),
    'post_excerpt' => $post->post_excerpt,
    'post_excerpt_empty' => ($post->post_excerpt === ''),
    'get_the_excerpt' => get_the_excerpt($post),
    'content_sha256' => hash('sha256', (string) $post->post_content),
    'content_preview' => $clip(wp_strip_all_tags((string) $post->post_content), 220),
    'featured_image_id' => (int) get_post_thumbnail_id($post_id),
    'meta' => $meta,
    'hero_lead' => $lead,
    'hub_card' => $card,
  );
};

$out = array();
$out['ts_utc'] = gmdate('c');
$out['blog_public'] = (int) get_option('blog_public');
$out['siteurl'] = get_option('siteurl');
$out['home'] = get_option('home');
$out['core_version'] = defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null;
$out['stylesheet'] = get_option('stylesheet');
$out['wpilot_write_enabled'] = get_option('metacode_wpilot_write_enabled', null);

if (class_exists('Shpigovsky\\Core\\Admin\\IndexingState') && method_exists('Shpigovsky\\Core\\Admin\\IndexingState', 'snapshot')) {
  $out['indexing_snapshot'] = \Shpigovsky\Core\Admin\IndexingState::snapshot();
}

$out['posts'] = array(
  '1745' => $post_snapshot(1745),
  '750' => $post_snapshot(750),
);

$acf_group = null;
if (function_exists('acf_get_field_group')) {
  $acf_group = acf_get_field_group('group_fp02_blog_post_article_meta');
}
$out['acf_group_present'] = is_array($acf_group);
$out['acf_field_names'] = array();
if (function_exists('acf_get_fields')) {
  $fields = acf_get_fields('group_fp02_blog_post_article_meta');
  if (is_array($fields)) {
    foreach ($fields as $field) {
      $out['acf_field_names'][] = array(
        'key' => $field['key'] ?? null,
        'name' => $field['name'] ?? null,
        'label' => $field['label'] ?? null,
      );
    }
  }
}

global $wpdb;
$table = $wpdb->prefix . 'fp02_user_activity_log';
$exists = $wpdb->get_var($wpdb->prepare('SHOW TABLES LIKE %s', $table));
$out['activity_log_table'] = $table;
$out['activity_log_exists'] = ($exists === $table);
$out['activity_log_recent'] = array();
$out['activity_log_editorial'] = array();
if ($exists === $table) {
  $cols = $wpdb->get_col("DESCRIBE {$table}", 0);
  $out['activity_log_columns'] = $cols;
  $rows = $wpdb->get_results("SELECT * FROM {$table} ORDER BY id DESC LIMIT 20", ARRAY_A);
  $clip_rows = array();
  foreach ((array) $rows as $row) {
    $safe = array();
    foreach ($row as $k => $v) {
      if (is_string($v) && strlen($v) > 300) {
        $safe[$k] = substr($v, 0, 300) . '...[truncated]';
      } else {
        $safe[$k] = $v;
      }
    }
    $clip_rows[] = $safe;
  }
  $out['activity_log_recent'] = $clip_rows;
  $ed = $wpdb->get_results(
    "SELECT * FROM {$table} WHERE object_type IN ('post','page') OR action LIKE '%post%' OR action LIKE '%edit%' ORDER BY id DESC LIMIT 15",
    ARRAY_A
  );
  $ed_clip = array();
  foreach ((array) $ed as $row) {
    $safe = array();
    foreach ($row as $k => $v) {
      if (is_string($v) && strlen($v) > 300) {
        $safe[$k] = substr($v, 0, 300) . '...[truncated]';
      } else {
        $safe[$k] = $v;
      }
    }
    $ed_clip[] = $safe;
  }
  $out['activity_log_editorial'] = $ed_clip;
}

$recent_posts = $wpdb->get_results(
  "SELECT ID, post_title, post_name, post_status, post_modified_gmt, post_author
   FROM {$wpdb->posts}
   WHERE post_type='post' AND post_status IN ('publish','draft','pending','private')
   ORDER BY post_modified_gmt DESC LIMIT 12",
  ARRAY_A
);
$out['recent_posts'] = $recent_posts;

$files = array(
  'theme/inc/blog-helpers.php' => 'wp-content/themes/shpigovsky/inc/blog-helpers.php',
  'plugin/FieldGroups.php' => 'wp-content/plugins/shpigovsky-core/src/Fields/FieldGroups.php',
  'plugin/shpigovsky-core.php' => 'wp-content/plugins/shpigovsky-core/shpigovsky-core.php',
  'acf-json/group_fp02_blog_post_article_meta.json' => 'wp-content/acf-json/group_fp02_blog_post_article_meta.json',
  'robots.txt' => 'robots.txt',
);
$out['prod_files'] = array();
foreach ($files as $label => $rel) {
  $abs = ABSPATH . $rel;
  if (is_readable($abs)) {
    $raw = file_get_contents($abs);
    $out['prod_files'][$label] = array(
      'path' => $abs,
      'bytes' => strlen($raw),
      'sha256' => hash('sha256', $raw),
      'mtime' => gmdate('c', filemtime($abs)),
    );
  } else {
    $out['prod_files'][$label] = array('missing' => true, 'path' => $abs);
  }
}

$json = wp_json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
$json_path = ABSPATH . 'wp-content/uploads/.fp02-hub-ann-intake.json';
file_put_contents($json_path, $json);
echo $json;
"""


def extract_blog_cards(html: str) -> list[dict]:
    cards = []
    for m in re.finditer(
        r'<article[^>]*class="[^"]*blog-archive-card[^"]*"[\s\S]*?</article>',
        html,
        re.I,
    ):
        block = m.group(0)
        title = (re.search(r"<h[23][^>]*>\s*<a[^>]*>([^<]+)", block, re.I) or [None, ""])[1]
        href = (re.search(r'href="([^"]+)"', block, re.I) or [None, ""])[1]
        excerpt = (re.search(r'blog-archive-card__excerpt[^>]*>\s*([^<]+)', block, re.I) or [None, ""])[1]
        cards.append(
            {
                "title": re.sub(r"\s+", " ", title).strip(),
                "href": href,
                "excerpt": re.sub(r"\s+", " ", excerpt).strip(),
            }
        )
    if not cards:
        for m in re.finditer(
            r'class="[^"]*blog-archive-card__excerpt[^"]*"[^>]*>([^<]+)',
            html,
            re.I,
        ):
            cards.append({"excerpt": re.sub(r"\s+", " ", m.group(1)).strip()})
    return cards[:12]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    public: dict = {"ts_utc": datetime.now(timezone.utc).isoformat(), "urls": []}
    for url in PUBLIC_URLS:
        entry = fetch(url)
        text = entry.pop("text")
        if url.endswith("robots.txt"):
            entry["robots_preview"] = text[:800]
            entry["has_sitemap"] = "sitemap" in text.lower()
            entry["has_disallow_root"] = bool(re.search(r"(?m)^Disallow:\s*/\s*$", text))
        if url.rstrip("/").endswith("/blog"):
            entry["cards"] = extract_blog_cards(text)
        public["urls"].append(entry)
    OUT.joinpath("01-public-intake.json").write_text(
        json.dumps(public, ensure_ascii=False, indent=2), encoding="utf-8"
    )

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
    sftp.putfo(io.BytesIO(PROBE_PHP.encode("utf-8")), REMOTE_PROBE)
    remote_json = f"{DOCROOT}/wp-content/uploads/.fp02-hub-ann-intake.json"
    php_cmd = (
        f"php8.2 -d display_errors=1 {REMOTE_PROBE} 2>/dev/null "
        f"|| /usr/local/bin/php8.2 -d display_errors=1 {REMOTE_PROBE}"
    )
    _i, o, e = client.exec_command(php_cmd, timeout=180)
    raw = o.read().decode("utf-8", "replace")
    err = e.read().decode("utf-8", "replace")
    exit_status = o.channel.recv_exit_status()
    data = ""
    try:
        with sftp.open(remote_json, "rb") as rf:
            data = rf.read().decode("utf-8", "replace")
    except OSError:
        data = ""
    try:
        sftp.remove(REMOTE_PROBE)
    except OSError:
        pass
    try:
        sftp.remove(remote_json)
    except OSError:
        pass
    if not data.strip():
        start, end = raw.find("{"), raw.rfind("}")
        data = raw[start : end + 1] if start >= 0 and end > start else raw
    OUT.joinpath("01-wp-intake-stdout.txt").write_text(raw, encoding="utf-8")
    OUT.joinpath("01-wp-intake-exit.txt").write_text(str(exit_status), encoding="utf-8")
    OUT.joinpath("01-wp-intake.json").write_text(data, encoding="utf-8")
    OUT.joinpath("01-wp-intake-stderr.txt").write_text(err, encoding="utf-8")
    parsed = json.loads(data)
    print(json.dumps({
        "blog_public": parsed.get("blog_public"),
        "core_version": parsed.get("core_version"),
        "wpilot_write_enabled": parsed.get("wpilot_write_enabled"),
        "acf_field_names": parsed.get("acf_field_names"),
        "post_1745_excerpt_empty": parsed.get("posts", {}).get("1745", {}).get("post_excerpt_empty"),
        "post_1745_card": parsed.get("posts", {}).get("1745", {}).get("hub_card"),
        "post_750_excerpt": parsed.get("posts", {}).get("750", {}).get("post_excerpt"),
        "post_750_card": parsed.get("posts", {}).get("750", {}).get("hub_card"),
        "activity_count": len(parsed.get("activity_log_recent") or []),
        "recent_posts": parsed.get("recent_posts"),
        "prod_files": parsed.get("prod_files"),
        "public_blog_cards": next((u.get("cards") for u in public["urls"] if u["url"].rstrip("/").endswith("/blog")), None),
        "robots": next(({"has_sitemap": u.get("has_sitemap"), "has_disallow_root": u.get("has_disallow_root")} for u in public["urls"] if u["url"].endswith("robots.txt")), None),
    }, ensure_ascii=False, indent=2))
    sftp.close()
    client.close()


if __name__ == "__main__":
    main()

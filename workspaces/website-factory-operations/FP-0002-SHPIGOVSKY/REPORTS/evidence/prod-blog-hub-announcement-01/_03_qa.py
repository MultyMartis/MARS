# -*- coding: utf-8 -*-
"""Live QA: Blog Hub dedicated announcement field. No editorial DB residue."""
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
QA_MARKER = "QA-HUB-ANN-1745-PRIORITY-PROBE"

PUBLIC_URLS = [
    "https://shpigovsky.ru/",
    "https://shpigovsky.ru/robots.txt",
    "https://shpigovsky.ru/blog/",
    "https://shpigovsky.ru/blog/demo-pagination-article-01/",
    "https://shpigovsky.ru/blog/lechenie-alkogolnoy-zavisimosti-pochemu-sila-voli-ni-pri-chem/",
]

EXPECTED_1745_EXCERPT_PREFIX = "Что такое генотипирование"
EXPECTED_750_EXCERPT = "В статье расскажем о подходах к лечению и профилактике зависимости"


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
    req = urllib.request.Request(url, headers={"User-Agent": "FP02-hub-ann-qa/1.0"})
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
        "meta_robots": (re.search(r'<meta\s+name=[\'"]robots[\'"]\s+content=[\'"]([^\'"]*)', text, re.I) or [None, ""])[1],
        "meta_description": (
            re.search(r'<meta\s+name="description"\s+content="([^"]*)"', text, re.I) or [None, ""]
        )[1],
        "og_description": (
            re.search(r'<meta\s+property="og:description"\s+content="([^"]*)"', text, re.I) or [None, ""]
        )[1],
        "jsonld_count": len(re.findall(r"application/ld\+json", text)),
        "has_qa_marker": QA_MARKER in text,
        "text": text,
    }


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
    return cards[:12]


PRIORITY_PHP = r"""<?php
$_SERVER['HTTP_HOST'] = 'shpigovsky.ru';
$_SERVER['SERVER_NAME'] = 'shpigovsky.ru';
$_SERVER['HTTPS'] = 'on';
$_SERVER['REQUEST_URI'] = '/';
define('WP_USE_THEMES', false);
require '/home/s/shpigovsky/shpigovsky.ru/public_html/wp-load.php';

$baseline_1745 = function_exists('shpigovsky_get_blog_hub_announcement')
  ? shpigovsky_get_blog_hub_announcement(1745)
  : null;
$baseline_750 = function_exists('shpigovsky_get_blog_hub_announcement')
  ? shpigovsky_get_blog_hub_announcement(750)
  : null;
$native_1745 = get_the_excerpt(1745);
$native_750 = get_the_excerpt(750);
$lead_1745 = function_exists('shpigovsky_get_article_lead') ? shpigovsky_get_article_lead(1745) : null;
$lead_750 = function_exists('shpigovsky_get_article_lead') ? shpigovsky_get_article_lead(750) : null;
$meta_1745 = get_post_meta(1745, 'article_hub_announcement', true);
$meta_750 = get_post_meta(750, 'article_hub_announcement', true);
$seo_1745 = get_post_meta(1745, 'fp02_seo_description', true);
$seo_750 = get_post_meta(750, 'fp02_seo_description', true);

add_filter('acf/load_value/name=article_hub_announcement', static function ($value, $post_id) {
  if ((int) $post_id === 1745) {
    return 'QA-HUB-ANN-1745-PRIORITY-PROBE';
  }
  return $value;
}, 20, 2);

$filtered_1745 = shpigovsky_get_blog_hub_announcement(1745);
$filtered_750 = shpigovsky_get_blog_hub_announcement(750);
$card_1745 = shpigovsky_build_blog_archive_card_args(1745);
$card_750 = shpigovsky_build_blog_archive_card_args(750);

$out = array(
  'blog_public' => (int) get_option('blog_public'),
  'core_version' => defined('SHPIGOVSKY_CORE_VERSION') ? SHPIGOVSKY_CORE_VERSION : null,
  'wpilot_write_enabled' => get_option('metacode_wpilot_write_enabled', null),
  'meta_1745_hub' => $meta_1745,
  'meta_750_hub' => $meta_750,
  'baseline_1745' => $baseline_1745,
  'baseline_750' => $baseline_750,
  'native_1745' => $native_1745,
  'native_750' => $native_750,
  'lead_1745' => $lead_1745,
  'lead_750' => $lead_750,
  'seo_1745' => $seo_1745,
  'seo_750' => $seo_750,
  'filtered_1745' => $filtered_1745,
  'filtered_750' => $filtered_750,
  'card_excerpt_1745_filtered' => is_array($card_1745) ? ($card_1745['excerpt'] ?? null) : null,
  'card_excerpt_750_filtered' => is_array($card_750) ? ($card_750['excerpt'] ?? null) : null,
  'priority_wins' => ($filtered_1745 === 'QA-HUB-ANN-1745-PRIORITY-PROBE'),
  '750_untouched_by_1745_filter' => ($filtered_750 === $baseline_750),
  'no_db_write' => ($meta_1745 === get_post_meta(1745, 'article_hub_announcement', true)),
);
$json = wp_json_encode($out, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
file_put_contents(ABSPATH . 'wp-content/uploads/.fp02-hub-ann-priority.json', $json);
echo $json;
"""


def main() -> None:
    public: dict = {"ts_utc": datetime.now(timezone.utc).isoformat(), "urls": []}
    for url in PUBLIC_URLS:
        entry = fetch(url)
        text = entry.pop("text")
        if url.endswith("robots.txt"):
            entry["robots_preview"] = text[:800]
            entry["has_sitemap"] = "sitemap" in text.lower()
            entry["has_disallow_root"] = bool(re.search(r"(?m)^Disallow:\s*/\s*$", text))
            entry["sha256"] = sha256_bytes(text.encode("utf-8")) if False else entry["sha256"]
        if url.rstrip("/").endswith("/blog"):
            entry["cards"] = extract_blog_cards(text)
            entry["schema_has_hub_field"] = "article_hub_announcement" in text
        if "/blog/" in url and not url.rstrip("/").endswith("/blog"):
            lead_html = (re.search(r'article-hero__lead[^>]*>\s*([^<]+)', text, re.I) or [None, ""])[1]
            entry["hero_lead_preview"] = re.sub(r"\s+", " ", lead_html).strip()[:400]
            entry["schema_has_hub_field"] = "article_hub_announcement" in text
        public["urls"].append(entry)

    blog = next(u for u in public["urls"] if u["url"].rstrip("/").endswith("/blog"))
    cards = blog.get("cards") or []
    card_1745 = next((c for c in cards if "Генотипирование" in (c.get("title") or "")), None)
    card_750 = next((c for c in cards if "алкогольной зависимости" in (c.get("title") or "")), None)
    checks = {
        "blog_200": blog["status"] == 200,
        "1745_card_present": card_1745 is not None,
        "750_card_present": card_750 is not None,
        "1745_fallback_trim": bool(card_1745 and (card_1745["excerpt"] or "").startswith(EXPECTED_1745_EXCERPT_PREFIX)),
        "750_fallback_native": bool(card_750 and card_750["excerpt"] == EXPECTED_750_EXCERPT),
        "no_live_qa_marker": not any(u.get("has_qa_marker") for u in public["urls"]),
        "robots_no_disallow_root": next(
            (not u.get("has_disallow_root") for u in public["urls"] if u["url"].endswith("robots.txt")),
            False,
        ),
        "robots_has_sitemap": next(
            (bool(u.get("has_sitemap")) for u in public["urls"] if u["url"].endswith("robots.txt")),
            False,
        ),
    }
    public["live_checks"] = checks
    public["card_1745"] = card_1745
    public["card_750"] = card_750
    OUT.joinpath("05-public-qa.json").write_text(
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
    probe = f"/tmp/fp02-hub-ann-priority-{STAMP}.php"
    remote_json = f"{DOCROOT}/wp-content/uploads/.fp02-hub-ann-priority.json"
    sftp.putfo(io.BytesIO(PRIORITY_PHP.encode("utf-8")), probe)
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
    OUT.joinpath("06-priority-qa.json").write_text(data, encoding="utf-8")
    OUT.joinpath("06-priority-qa-stderr.txt").write_text(err, encoding="utf-8")
    parsed = json.loads(data)

    summary = {
        "ts_utc": datetime.now(timezone.utc).isoformat(),
        "live_checks": checks,
        "priority": {
            "wins": parsed.get("priority_wins"),
            "filtered_1745": parsed.get("filtered_1745"),
            "filtered_750": parsed.get("filtered_750"),
            "750_untouched": parsed.get("750_untouched_by_1745_filter"),
            "meta_1745_empty": not bool(parsed.get("meta_1745_hub")),
            "meta_750_empty": not bool(parsed.get("meta_750_hub")),
            "baseline_1745": parsed.get("baseline_1745"),
            "baseline_750": parsed.get("baseline_750"),
            "blog_public": parsed.get("blog_public"),
            "core_version": parsed.get("core_version"),
        },
    }
    OUT.joinpath("07-qa-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))

    if parsed.get("blog_public") != 1:
        raise SystemExit("INDEXING_CHANGED")
    if not parsed.get("priority_wins"):
        raise SystemExit("PRIORITY_FAIL")
    if not parsed.get("750_untouched_by_1745_filter"):
        raise SystemExit("CROSS_POST_LEAK")
    if not checks["1745_fallback_trim"] or not checks["750_fallback_native"]:
        raise SystemExit("LIVE_FALLBACK_FAIL")
    if not checks["no_live_qa_marker"]:
        raise SystemExit("QA_MARKER_LEAKED_TO_PUBLIC")
    if not checks["robots_no_disallow_root"] or not checks["robots_has_sitemap"]:
        raise SystemExit("ROBOTS_REGRESSION")

    sftp.close()
    client.close()
    print("QA_OK")


if __name__ == "__main__":
    main()

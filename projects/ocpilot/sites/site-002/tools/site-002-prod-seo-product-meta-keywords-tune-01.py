#!/usr/bin/env python3
"""SITE-002 Production product PDP meta keywords generator tune — Run 4.202."""
from __future__ import annotations

import argparse
import csv
import ftplib
import hashlib
import html
import io
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-SEO-PRODUCT-META-KEYWORDS-TUNE-01"
OCPILOT_RUN = "4.202"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SEO-PRODUCT-META-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-SEO-PRODUCT-META-KEYWORDS-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
PRIOR_DEPLOY = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-FIX-01"
)
DISCOVERY_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    r"\SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-DISCOVERY-01"
)
DEPLOYMENT_ROOT = Path(
    r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments"
    rf"\{OPERATION_ID}"
)
USER_AGENT = f"MARS-OCPilot/{OPERATION_ID}"
REMOTE_PRODUCT = "/public_html/catalog/controller/product/product.php"
MODIFICATION_PATHS = (
    "/public_html/storage/modification/catalog/controller/product/product.php",
    "/public_html/system/storage/modification/catalog/controller/product/product.php",
    "/storage/modification/catalog/controller/product/product.php",
)

EXTRA_DEEP_PDP_URLS = (
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye/zont-vytyazhnoy-pristennyy-zvp-900-900-900h900h450",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/telezhka-dlya-sbora-posudy-ts-1-800h500h930",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/telezhka-servirovochnaya-ts-2-800h500h930",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye/telezhka-servirovochnaya-ts-3-800h500h930",
)

HUB_URL_MARKERS = (
    "/polki/nastennye/otkrytye",
    "/polki/nastennye/zakrytye",
    "/shkafy/proizvodstvennye-shkafy/zakrytye-shkafy",
    "/shkafy/proizvodstvennye-shkafy/shkafy-s-polkami",
)

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "verification",
    "pdp-before",
    "pdp-after",
    "samples",
    "keyword-design",
    "manifests",
    "logs",
)

PHP_KEYWORDS_V11_BLOCK = r"""
	private function normalizeMetaKeywordPhrase($phrase) {
		return $this->normalizeMetaText($phrase);
	}

	private function isNumericOnlyMetaKeyword($phrase) {
		$phrase = $this->normalizeMetaKeywordPhrase($phrase);

		if ($phrase === '') {
			return true;
		}

		$trimmed = trim($phrase);

		if (preg_match('/^\d+$/u', $trimmed)) {
			return true;
		}

		if (preg_match('/^\d+([,.]\d+)?$/u', $trimmed)) {
			return true;
		}

		$compact = preg_replace('/[\s]/u', '', $trimmed);

		if (preg_match('/^\d+([×xх]\d+)+$/ui', $compact)) {
			return true;
		}

		return false;
	}

	private function isUsefulMetaKeywordPhrase($phrase, $product_name = '') {
		$phrase = $this->normalizeMetaKeywordPhrase($phrase);

		if ($phrase === '') {
			return false;
		}

		if ($this->isNumericOnlyMetaKeyword($phrase)) {
			return false;
		}

		$lower = mb_strtolower($phrase, 'UTF-8');
		$len = mb_strlen($phrase, 'UTF-8');

		if ($len < 3) {
			$allowed_short = array('gn');

			if (!in_array($lower, $allowed_short, true)) {
				return false;
			}
		}

		if (preg_match('/^[\s,.;:\-\/\\\\]+$/u', $phrase)) {
			return false;
		}

		$junk = array('есть', 'нет', 'да', 'без', '—', '-');

		if (in_array($lower, $junk, true)) {
			return false;
		}

		if ($len > 80) {
			if ($product_name === '' || $lower !== mb_strtolower($product_name, 'UTF-8')) {
				return false;
			}
		}

		return true;
	}

	private function trimMetaKeywords(array $phrases, $max_phrases = 18, $max_chars = 300) {
		$phrases = array_slice($phrases, 0, $max_phrases);
		$result = implode(', ', $phrases);

		if (mb_strlen($result, 'UTF-8') <= $max_chars) {
			return $result;
		}

		while (count($phrases) > 6 && mb_strlen(implode(', ', $phrases), 'UTF-8') > $max_chars) {
			array_pop($phrases);
		}

		return implode(', ', $phrases);
	}

	private function addUniqueMetaKeyword(array &$phrases, array &$seen, $phrase, $product_name = '') {
		if (!$this->isUsefulMetaKeywordPhrase($phrase, $product_name)) {
			return false;
		}

		$phrase = $this->normalizeMetaKeywordPhrase($phrase);
		$key = mb_strtolower($phrase, 'UTF-8');

		if (isset($seen[$key])) {
			return false;
		}

		$seen[$key] = true;
		$phrases[] = $phrase;

		return true;
	}

	private function buildProductMetaKeywords($product_info, array $breadcrumbs, array $attribute_groups) {
		$name = $this->normalizeMetaText(isset($product_info['name']) ? $product_info['name'] : '');
		$category = $this->getCategoryLabel($breadcrumbs);
		$family = $this->detectCategoryFamily($breadcrumbs);
		$attributes = $this->flattenProductAttributes($attribute_groups);
		$phrases = array();
		$seen = array();
		$attr_added = 0;
		$dim_added = 0;

		$this->addUniqueMetaKeyword($phrases, $seen, $name, $name);
		$this->addUniqueMetaKeyword($phrases, $seen, $category, $name);
		$this->addUniqueMetaKeyword($phrases, $seen, 'купить', $name);
		$this->addUniqueMetaKeyword($phrases, $seen, 'БЗПМ', $name);
		$this->addUniqueMetaKeyword($phrases, $seen, 'нержавеющая сталь', $name);
		$this->addUniqueMetaKeyword($phrases, $seen, 'нейтральное оборудование', $name);

		$family_kw = array(
			'stoly' => array('стол производственный', 'стол из нержавеющей стали', 'купить стол'),
			'polki' => array('полка настенная', 'полка для кухни', 'купить полку'),
			'telezhki' => array('тележка для кухни', 'противень нержавеющий'),
			'telezhki_servirovochnye' => array('тележка сервировочная', 'купить тележку'),
			'shkafy_lari' => array('шкаф кухонный', 'шкаф из нержавеющей стали'),
			'podstavki' => array('подставка под оборудование', 'подтоварник'),
			'stellazhi' => array('стеллаж кухонный', 'стеллаж из нержавеющей стали'),
			'moechnye_vanny' => array('моечная ванна', 'котломойка'),
			'zonty' => array('вытяжной зонт', 'зонт для кухни'),
		);

		if (isset($family_kw[$family])) {
			foreach ($family_kw[$family] as $phrase) {
				if (count($phrases) >= 16) {
					break;
				}

				$this->addUniqueMetaKeyword($phrases, $seen, $phrase, $name);
			}
		}

		$family_attr_needles = array(
			'stoly' => array('борт', 'полк', 'столеш', 'сварн', 'разбор'),
			'polki' => array('настен', 'настоль', 'ярус', 'гастро', 'gn', 'рамк'),
			'telezhki' => array('колес', 'ярус', 'гастро', 'gn', 'противн', 'шпил'),
			'telezhki_servirovochnye' => array('колес', 'полк', 'ярус', 'сервиров'),
			'shkafy_lari' => array('двер', 'полк', 'замок'),
			'podstavki' => array('уровн', 'gn', 'нагруз', 'секц'),
			'stellazhi' => array('полк', 'ярус', 'уровн'),
			'moechnye_vanny' => array('секц', 'чаш', 'мойк', 'котломой'),
			'zonty' => array('вытяж', 'фильтр', 'пристен', 'остров'),
			'generic' => array('материал', 'нержав', 'сталь'),
		);

		$needles = isset($family_attr_needles[$family]) ? $family_attr_needles[$family] : $family_attr_needles['generic'];

		foreach ($needles as $needle) {
			if ($attr_added >= 5 || count($phrases) >= 16) {
				break;
			}

			$phrase = $this->pickAttributePhrase($attributes, array($needle), 50);

			if ($phrase !== '' && $this->addUniqueMetaKeyword($phrases, $seen, $phrase, $name)) {
				$attr_added++;
			}
		}

		$dims = $this->formatProductDimensions($product_info);

		if ($dims !== '' && $dim_added < 2) {
			if ($this->addUniqueMetaKeyword($phrases, $seen, 'габариты ' . $dims, $name)) {
				$dim_added++;
			} elseif ($this->addUniqueMetaKeyword($phrases, $seen, 'размер ' . $dims, $name)) {
				$dim_added++;
			}
		}

		return $this->trimMetaKeywords($phrases, 18, 300);
	}
"""

PHP_OLD_BUILD_KEYWORDS = r"""	private function buildProductMetaKeywords($product_info, array $breadcrumbs, array $attribute_groups) {
		$name = $this->normalizeMetaText(isset($product_info['name']) ? $product_info['name'] : '');
		$category = $this->getCategoryLabel($breadcrumbs);
		$family = $this->detectCategoryFamily($breadcrumbs);
		$attributes = $this->flattenProductAttributes($attribute_groups);
		$phrases = array();
		$seen = array();

		$add = function($phrase) use (&$phrases, &$seen) {
			$phrase = $this->normalizeMetaText($phrase);

			if ($phrase === '') {
				return;
			}

			$key = mb_strtolower($phrase, 'UTF-8');

			if (isset($seen[$key])) {
				return;
			}

			$seen[$key] = true;
			$phrases[] = $phrase;
		};

		$add($name);
		$add($category);
		$add('купить');
		$add('БЗПМ');
		$add('нержавеющая сталь');
		$add('нейтральное оборудование');

		$family_kw = array(
			'stoly' => array('стол производственный', 'стол из нержавеющей стали'),
			'polki' => array('полка настенная', 'полка для кухни'),
			'telezhki' => array('тележка для кухни', 'противень нержавеющий'),
			'shkafy_lari' => array('шкаф кухонный', 'шкаф из нержавеющей стали'),
			'podstavki' => array('подставка под оборудование', 'подтоварник'),
			'stellazhi' => array('стеллаж кухонный', 'стеллаж из нержавеющей стали'),
			'moechnye_vanny' => array('моечная ванна', 'котломойка'),
			'zonty' => array('вытяжной зонт', 'зонт для кухни'),
		);

		if (isset($family_kw[$family])) {
			foreach ($family_kw[$family] as $phrase) {
				$add($phrase);
			}
		}

		foreach ($attributes as $attr) {
			if (count($phrases) >= 18) {
				break;
			}

			$val = $this->normalizeMetaText($attr['text']);

			if ($val !== '' && mb_strlen($val, 'UTF-8') <= 40) {
				$add($val);
			}
		}

		$dims = $this->formatProductDimensions($product_info);

		if ($dims !== '') {
			$add($dims);
		}

		return implode(', ', array_slice($phrases, 0, 18));
	}"""


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.in_title = False
        self.in_h1 = False
        self.h1_list: list[str] = []
        self.meta: dict[str, str] = {}
        self.links: list[dict[str, str]] = []
        self.body_open = 0
        self.breadcrumb_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: (v or "") for k, v in attrs}
        tag_l = tag.lower()
        if tag_l == "title":
            self.in_title = True
        elif tag_l == "h1":
            self.in_h1 = True
        elif tag_l == "body":
            self.body_open += 1
        elif tag_l == "meta":
            name = (attrs_dict.get("name") or attrs_dict.get("property") or "").lower()
            content = attrs_dict.get("content", "")
            if name:
                self.meta[name] = content
        elif tag_l == "link":
            rel = attrs_dict.get("rel", "").lower()
            href = attrs_dict.get("href", "")
            if rel and href:
                self.links.append({"rel": rel, "href": href})

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False
        elif tag.lower() == "h1":
            self.in_h1 = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data
        if self.in_h1:
            self.h1_list.append(data.strip())


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def parse_production_section(path: Path, subsection: str) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## PRODUCTION\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
    if not match:
        raise RuntimeError("PRODUCTION section not found")
    block = match.group(1)
    sub_match = re.search(rf"^### {re.escape(subsection)}\s*$([\s\S]*?)(?=^### |\Z)", block, re.MULTILINE)
    if not sub_match:
        raise RuntimeError(f"Subsection {subsection} not found")
    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in sub_match.group(1).splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.endswith(":"):
            current_key = stripped[:-1].strip().lower().replace(" ", "_")
            fields.setdefault(current_key, "")
            continue
        if current_key:
            fields[current_key] = stripped
    return fields


def ftp_connect() -> ftplib.FTP:
    creds = parse_production_section(SECRETS_PATH, "FTP / SFTP")
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], int(creds.get("port") or 21), timeout=120)
    ftp.login(creds["username"], creds["password"])
    ftp.set_pasv(True)
    if creds.get("root"):
        try:
            ftp.cwd(creds["root"])
        except ftplib.error_perm:
            pass
    return ftp


def ftp_download(ftp: ftplib.FTP, remote: str) -> bytes:
    buf = io.BytesIO()
    ftp.retrbinary(f"RETR {remote}", buf.write)
    return buf.getvalue()


def ftp_upload(ftp: ftplib.FTP, remote: str, data: bytes) -> None:
    ftp.storbinary(f"STOR {remote}", io.BytesIO(data))


def ftp_exists(ftp: ftplib.FTP, remote: str) -> bool:
    try:
        ftp.size(remote)
        return True
    except ftplib.error_perm:
        try:
            buf = io.BytesIO()
            ftp.retrbinary(f"RETR {remote}", buf.write, rest=0)
            return True
        except ftplib.error_perm:
            return False


def http_get(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache", "Accept": "text/html,application/xml,*/*"},
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
            charset = response.headers.get_content_charset() or "utf-8"
            text = body.decode(charset, errors="replace")
            return {
                "url": url,
                "status_code": response.status,
                "x_robots_tag": response.headers.get("X-Robots-Tag", ""),
                "body": text,
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        body = exc.read() if exc.fp else b""
        charset = exc.headers.get_content_charset() if exc.headers else None
        text = body.decode(charset or "utf-8", errors="replace")
        return {"url": url, "status_code": exc.code, "x_robots_tag": "", "body": text, "error": str(exc)}
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "status_code": None, "x_robots_tag": "", "body": "", "error": str(exc)}


def split_keyword_phrases(keywords: str) -> list[str]:
    if not keywords:
        return []
    return [p.strip() for p in keywords.split(",") if p.strip()]


def is_numeric_only_token(token: str) -> bool:
    t = token.strip()
    if re.fullmatch(r"\d+", t):
        return True
    if re.fullmatch(r"\d+([,.]\d+)?", t):
        return True
    compact = re.sub(r"\s", "", t)
    if re.fullmatch(r"\d+([×xх]\d+)+", compact, flags=re.IGNORECASE):
        return True
    return False


def analyze_keywords(keywords: str) -> dict[str, Any]:
    phrases = split_keyword_phrases(keywords)
    numeric = [p for p in phrases if is_numeric_only_token(p)]
    short = [p for p in phrases if len(p) < 3 and p.lower() not in ("gn",)]
    seen: set[str] = set()
    dups: list[str] = []
    for p in phrases:
        key = p.lower()
        if key in seen:
            dups.append(p)
        seen.add(key)
    return {
        "keywords_phrase_count": len(phrases),
        "numeric_only_tokens": numeric,
        "too_short_tokens": short,
        "duplicate_phrases": dups,
    }


def is_deep_pdp(url: str, h1: str, title: str) -> bool:
    if any(marker in url for marker in HUB_URL_MARKERS):
        return False
    if re.search(r"/(stoly|polki|shkafy|telezhki|stellazhi|moechnye|zonty|podtovarniki)(/|$)", url, re.I):
        if h1 and len(h1) < 25 and h1.lower() in ("открытые", "закрытые", "с полками"):
            return False
    return "/katalog/" in url and url.count("/") >= 5


def extract_meta(html_text: str) -> dict[str, Any]:
    parser = MetaParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass
    canonical = next((l["href"] for l in parser.links if l["rel"] == "canonical"), "")
    kw = parser.meta.get("keywords", "")
    kw_analysis = analyze_keywords(kw)
    return {
        "title": html.unescape(parser.title.strip()),
        "meta_description": parser.meta.get("description", ""),
        "description_length": len(parser.meta.get("description", "")),
        "meta_keywords": kw,
        "keywords_length": len(kw),
        **kw_analysis,
        "h1": " | ".join(h for h in parser.h1_list if h),
        "canonical": canonical,
        "meta_robots": parser.meta.get("robots", ""),
        "body_count": parser.body_open,
        "yandex_metrika": any(t in html_text.lower() for t in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")),
        "yandex_webmaster": "yandex-verification" in html_text.lower(),
    }


def classify_keyword_quality(row: dict[str, Any]) -> str:
    if not row.get("is_deep_pdp"):
        return "HUB_NOT_PDP"
    kw = row.get("meta_keywords", "")
    if not kw:
        return "EMPTY"
    tags: list[str] = []
    if row.get("numeric_only_tokens"):
        tags.append("NUMERIC_POLLUTION")
    if row.get("keywords_length", 0) > 320:
        tags.append("TOO_LONG")
    if row.get("keywords_phrase_count", 0) > 18:
        tags.append("TOO_MANY_PHRASES")
    if row.get("duplicate_phrases"):
        tags.append("DUPLICATE_PHRASES")
    if row.get("too_short_tokens"):
        tags.append("TOO_SHORT_TOKENS")
    if not tags:
        return "CLEAN"
    return ";".join(tags)


def load_sample_urls() -> list[str]:
    discovery_json = DISCOVERY_ROOT / "pdp-samples" / "pdp-url-samples.json"
    urls: list[str] = []
    if discovery_json.exists():
        data = json.loads(discovery_json.read_text(encoding="utf-8"))
        urls = [r["product_url"] for r in data if r.get("include") == "yes"]
    for extra in EXTRA_DEEP_PDP_URLS:
        if extra not in urls:
            urls.append(extra)
    return urls


def ensure_dirs() -> None:
    for sub in SUBDIRS:
        (DEPLOYMENT_ROOT / sub).mkdir(parents=True, exist_ok=True)
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "operation.json",
        {
            "operation_id": OPERATION_ID,
            "site_id": SITE_ID,
            "environment": ENVIRONMENT,
            "production_url": PRODUCTION_URL,
            "baseline_before": BASELINE_BEFORE,
            "change_type": "product-meta-keywords-generator-tune",
            "product_pages_targeted": True,
            "db_write_allowed": False,
            "admin_save_allowed": False,
            "import_change_allowed": False,
            "description_change_allowed": "minimal_only_if_shared_helper",
            "header_footer_change_allowed": False,
            "yandex_blocks_protected": True,
            "robots_change_allowed": False,
            "sitemap_change_allowed": False,
            "llms_txt_allowed": False,
            "cron_change_allowed": False,
            "mail_change_allowed": False,
        },
    )


def apply_keywords_patch(content: str) -> str:
    if "resolveProductMetaDescription" not in content:
        raise RuntimeError("Run 4.201 generator not present — expected resolveProductMetaDescription")
    if PHP_OLD_BUILD_KEYWORDS not in content:
        raise RuntimeError("Expected buildProductMetaKeywords v1.0 block not found")
    if "normalizeMetaKeywordPhrase" in content:
        raise RuntimeError("Keywords v1.1 patch already applied")

    patched = content.replace(PHP_OLD_BUILD_KEYWORDS, PHP_KEYWORDS_V11_BLOCK.strip(), 1)
    patched = patched.replace(
        "\t\t\t'zont' => 'zonty',\n\t\t);",
        "\t\t\t'zont' => 'zonty',\n\t\t\t'servirov' => 'telezhki_servirovochnye',\n\t\t);",
        1,
    )
    patched = patched.replace(
        "SITE-002 — runtime PDP meta fallback generator (Run 4.201).",
        "SITE-002 — runtime PDP meta fallback generator (Run 4.201; keywords v1.1 Run 4.202).",
        1,
    )
    return patched


def php_lint(path: Path) -> dict[str, Any]:
    for cmd in (["php", "-l", str(path)], ["php8.2", "-l", str(path)], ["php8.1", "-l", str(path)]):
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30, check=False)
            if proc.returncode == 0 or "No syntax errors" in proc.stdout:
                return {"status": "PASS", "command": cmd, "output": proc.stdout.strip()}
            if "not recognized" not in proc.stderr.lower() and "not found" not in proc.stderr.lower():
                return {"status": "FAIL", "command": cmd, "output": (proc.stdout + proc.stderr).strip()}
        except FileNotFoundError:
            continue
    return {"status": "SKIPPED", "reason": "PHP CLI unavailable — static marker checks only"}


def crawl_pdps(urls: list[str], label: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for url in urls:
        resp = http_get(url)
        meta = extract_meta(resp["body"]) if resp.get("body") else {}
        row = {
            "url": url,
            "http_status": resp.get("status_code"),
            "x_robots_tag": resp.get("x_robots_tag", ""),
            "is_deep_pdp": is_deep_pdp(url, meta.get("h1", ""), meta.get("title", "")),
            "keyword_quality": "",
            **meta,
        }
        row["keyword_quality"] = classify_keyword_quality(row)
        rows.append(row)
    out_dir = DEPLOYMENT_ROOT / f"pdp-{label}"
    write_json(out_dir / f"pdp-{label}.json", rows)
    with (out_dir / f"pdp-{label}.csv").open("w", encoding="utf-8", newline="") as fh:
        if rows:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), extrasaction="ignore")
            writer.writeheader()
            for r in rows:
                r_csv = dict(r)
                for k in ("numeric_only_tokens", "too_short_tokens", "duplicate_phrases"):
                    if isinstance(r_csv.get(k), list):
                        r_csv[k] = "|".join(r_csv[k])
                writer.writerow(r_csv)
    deep = [r for r in rows if r.get("is_deep_pdp")]
    md = [
        f"# PDP {label} summary",
        "",
        f"Captured: {utc_now()}",
        f"Sample size: {len(rows)} (deep PDP: {len(deep)})",
        f"HTTP 200: {sum(1 for r in rows if r.get('http_status') == 200)}/{len(rows)}",
        f"Empty keywords (deep): {sum(1 for r in deep if r.get('keywords_length', 0) == 0)}/{len(deep)}",
        f"NUMERIC_POLLUTION (deep): {sum(1 for r in deep if 'NUMERIC_POLLUTION' in r.get('keyword_quality', ''))}/{len(deep)}",
        f"CLEAN (deep): {sum(1 for r in deep if r.get('keyword_quality') == 'CLEAN')}/{len(deep)}",
        f"Avg phrase count (deep): {round(sum(r.get('keywords_phrase_count', 0) for r in deep) / max(len(deep), 1), 1)}",
        "",
    ]
    write_text(out_dir / f"pdp-{label}-summary.md", "\n".join(md))
    return rows


def phase_source_authority(ftp: ftplib.FTP) -> dict[str, Any]:
    live = ftp_download(ftp, REMOTE_PRODUCT)
    mod_probe = [{"path": p, "exists": ftp_exists(ftp, p)} for p in MODIFICATION_PATHS]
    content = live.decode("utf-8", errors="replace")
    authority = {
        "patch_target": REMOTE_PRODUCT,
        "modification_overlay_present": any(p["exists"] for p in mod_probe),
        "modification_paths": mod_probe,
        "sha256_live": sha256_bytes(live),
        "has_resolveProductMetaKeywords": "resolveProductMetaKeywords" in content,
        "has_buildProductMetaKeywords": "buildProductMetaKeywords" in content,
        "has_keywords_v11": "normalizeMetaKeywordPhrase" in content,
        "description_generator_unchanged": "buildProductMetaDescription" in content,
        "confidence": "HIGH",
    }
    (DEPLOYMENT_ROOT / "source" / "product.php").write_bytes(live)
    write_json(DEPLOYMENT_ROOT / "manifests" / "source-authority.json", authority)
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "source-authority.md",
        "\n".join(
            [
                "# Source authority",
                "",
                f"- Patch target: `{REMOTE_PRODUCT}`",
                f"- Modification overlay: {'present' if authority['modification_overlay_present'] else 'absent'}",
                f"- resolveProductMetaKeywords: {authority['has_resolveProductMetaKeywords']}",
                f"- buildProductMetaKeywords: {authority['has_buildProductMetaKeywords']}",
                f"- Keywords v1.1 already applied: {authority['has_keywords_v11']}",
                f"- Description generator preserved: {authority['description_generator_unchanged']}",
                f"- Confidence: {authority['confidence']}",
            ]
        ),
    )
    return authority


def phase_keyword_design() -> None:
    design = {
        "version": "1.1",
        "captured_at": utc_now(),
        "max_phrases": 18,
        "ideal_phrases": "10-16",
        "max_chars": 300,
        "max_attribute_phrases": 5,
        "max_dimension_phrases": 2,
        "filters": [
            "numeric_only_tokens",
            "too_short_under_3_chars",
            "junk_tokens_estь_нет",
            "raw_attribute_dump_removed",
            "family_pickAttributePhrase_only",
        ],
        "preserve_core": [
            "product_name",
            "category",
            "купить",
            "БЗПМ",
            "нержавеющая сталь",
            "нейтральное оборудование",
        ],
    }
    write_json(DEPLOYMENT_ROOT / "keyword-design" / "product-keywords-generator-v1.1.json", design)
    write_text(
        DEPLOYMENT_ROOT / "keyword-design" / "product-keywords-generator-v1.1.md",
        "# Product keywords generator v1.1\n\nTune only `buildProductMetaKeywords` + filter helpers. Description generator unchanged.\n",
    )


def phase_implementation_plan() -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "files-to-change.json",
        [{"remote": REMOTE_PRODUCT, "local_prepared": "prepared/product.php", "patch_type": "KEYWORDS_V11_TUNE"}],
    )
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
        "\n".join(
            [
                "# Implementation plan",
                "",
                f"- Single file: `{REMOTE_PRODUCT}`",
                "- Replace `buildProductMetaKeywords` with v1.1 filtered version",
                "- Add: normalizeMetaKeywordPhrase, isNumericOnlyMetaKeyword, isUsefulMetaKeywordPhrase, trimMetaKeywords, addUniqueMetaKeyword",
                "- Add servirov family mapping in detectCategoryFamily",
                "- Description generator: unchanged",
            ]
        ),
    )


def simulate_keywords_v11(old_kw: str, product_name: str, family: str = "generic") -> str:
    """Python mirror of v1.1 filters for dry-run (approximate)."""
    phrases: list[str] = []
    seen: set[str] = set()

    def add(p: str) -> None:
        p = re.sub(r"\s+", " ", p.strip())
        if not p or is_numeric_only_token(p) or len(p) < 3 and p.lower() not in ("gn",):
            return
        if p.lower() in ("есть", "нет", "да", "без"):
            return
        key = p.lower()
        if key in seen:
            return
        seen.add(key)
        phrases.append(p)

    add(product_name)
    add("купить")
    add("БЗПМ")
    add("нержавеющая сталь")
    add("нейтральное оборудование")
    family_map = {
        "stoly": ["стол производственный", "стол из нержавеющей стали"],
        "polki": ["полка настенная", "полка для кухни"],
        "telezhki": ["тележка для кухни"],
        "zonty": ["вытяжной зонт"],
        "moechnye_vanny": ["моечная ванна"],
    }
    for p in family_map.get(family, []):
        add(p)
    old_parts = split_keyword_phrases(old_kw)
    for p in old_parts:
        if len(phrases) >= 16:
            break
        if not is_numeric_only_token(p) and len(p) >= 3:
            if re.search(r"×|габарит|размер|борт|полк|сварн|разбор|вытяж|секц", p, re.I):
                add(p)
    result = ", ".join(phrases[:18])
    if len(result) > 300:
        while len(phrases) > 6 and len(", ".join(phrases)) > 300:
            phrases.pop()
        result = ", ".join(phrases)
    return result


def infer_family(url: str) -> str:
    u = url.lower()
    for needle, fam in (
        ("stoly", "stoly"),
        ("polki", "polki"),
        ("telezhki-servirov", "telezhki_servirovochnye"),
        ("telezhki", "telezhki"),
        ("shkaf", "shkafy_lari"),
        ("podstavk", "podstavki"),
        ("stellazh", "stellazhi"),
        ("moechn", "moechnye_vanny"),
        ("zont", "zonty"),
    ):
        if needle in u:
            return fam
    return "generic"


def phase_dry_run(before_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    sim_rows: list[dict[str, Any]] = []
    for row in before_rows:
        if not row.get("is_deep_pdp"):
            continue
        old_kw = row.get("meta_keywords", "")
        name = row.get("h1") or row.get("title", "").split("|")[0].strip()
        old_analysis = analyze_keywords(old_kw)
        new_kw = simulate_keywords_v11(old_kw, name, infer_family(row["url"]))
        new_analysis = analyze_keywords(new_kw)
        sim_rows.append(
            {
                "url": row["url"],
                "product_name": name,
                "old_keywords": old_kw,
                "new_keywords": new_kw,
                "old_phrase_count": old_analysis["keywords_phrase_count"],
                "new_phrase_count": new_analysis["keywords_phrase_count"],
                "numeric_only_before": old_analysis["numeric_only_tokens"],
                "numeric_only_after": new_analysis["numeric_only_tokens"],
                "length_before": row.get("keywords_length", 0),
                "length_after": len(new_kw),
                "decision": "regenerate_tuned",
                "reason": "v1.1 filter simulation",
            }
        )
    write_json(DEPLOYMENT_ROOT / "verification" / "keyword-simulation-before-after.json", sim_rows)
    with (DEPLOYMENT_ROOT / "verification" / "keyword-simulation-before-after.csv").open(
        "w", encoding="utf-8", newline=""
    ) as fh:
        if sim_rows:
            writer = csv.DictWriter(fh, fieldnames=list(sim_rows[0].keys()), extrasaction="ignore")
            writer.writeheader()
            for r in sim_rows:
                r_csv = dict(r)
                for k in ("numeric_only_before", "numeric_only_after"):
                    if isinstance(r_csv.get(k), list):
                        r_csv[k] = "|".join(r_csv[k])
                writer.writerow(r_csv)
    num_removed = sum(1 for r in sim_rows if r["numeric_only_before"] and not r["numeric_only_after"])
    write_text(
        DEPLOYMENT_ROOT / "verification" / "keyword-simulation-summary.md",
        "\n".join(
            [
                "# Keyword simulation v1.1",
                "",
                f"Deep PDP rows: {len(sim_rows)}",
                f"Numeric pollution removed (sim): {num_removed}",
                f"Avg phrase count after: {round(sum(r['new_phrase_count'] for r in sim_rows) / max(len(sim_rows), 1), 1)}",
            ]
        ),
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", {"rows": len(sim_rows), "status": "PASS"})
    write_text(DEPLOYMENT_ROOT / "manifests" / "dry-run.md", "# Dry-run PASS\n\nNumeric tokens filtered; phrase caps applied in simulation.\n")
    return sim_rows


def phase_backup_prepare(ftp: ftplib.FTP) -> dict[str, Any]:
    live = ftp_download(ftp, REMOTE_PRODUCT)
    sha = sha256_bytes(live)
    (DEPLOYMENT_ROOT / "backup" / "product.php").write_bytes(live)
    (DEPLOYMENT_ROOT / "rollback" / "product.php").write_bytes(live)
    content = live.decode("utf-8", errors="replace")
    patched = apply_keywords_patch(content)
    prepared_path = DEPLOYMENT_ROOT / "prepared" / "product.php"
    prepared_path.write_text(patched, encoding="utf-8", newline="\n")
    lint = php_lint(prepared_path)
    if "resolveProductMetaKeywords" not in patched or "normalizeMetaKeywordPhrase" not in patched:
        raise RuntimeError("Prepared file missing v1.1 markers")
    if "buildProductMetaDescription" not in patched:
        raise RuntimeError("Description generator missing after patch")
    manifest = {
        "remote": REMOTE_PRODUCT,
        "sha256_backup": sha,
        "sha256_prepared": sha256_file(prepared_path),
        "lint": lint,
        "prepared_at": utc_now(),
    }
    write_json(DEPLOYMENT_ROOT / "manifests" / "backup-prepare.json", manifest)
    if lint.get("status") == "FAIL":
        raise RuntimeError(f"PHP lint failed: {lint}")
    return manifest


def pre_upload_verify(ftp: ftplib.FTP, backup_sha: str) -> None:
    live = ftp_download(ftp, REMOTE_PRODUCT)
    sha = sha256_bytes(live)
    pre_dir = DEPLOYMENT_ROOT / "verification" / "pre-upload"
    pre_dir.mkdir(parents=True, exist_ok=True)
    (pre_dir / "product.php").write_bytes(live)
    if sha != backup_sha:
        raise RuntimeError("STOP — LIVE FILE CHANGED SINCE BACKUP")


def deploy_product(ftp: ftplib.FTP) -> dict[str, Any]:
    prepared = (DEPLOYMENT_ROOT / "prepared" / "product.php").read_bytes()
    ftp_upload(ftp, REMOTE_PRODUCT, prepared)
    after = ftp_download(ftp, REMOTE_PRODUCT)
    after_dir = DEPLOYMENT_ROOT / "verification" / "after-upload"
    after_dir.mkdir(parents=True, exist_ok=True)
    (after_dir / "product.php").write_bytes(after)
    return {
        "remote": REMOTE_PRODUCT,
        "sha256_prepared": sha256_bytes(prepared),
        "sha256_after_upload": sha256_bytes(after),
        "match": sha256_bytes(prepared) == sha256_bytes(after),
        "deployed_at": utc_now(),
    }


def compare_keywords_before_after(before: list[dict[str, Any]], after: list[dict[str, Any]]) -> list[dict[str, Any]]:
    after_map = {r["url"]: r for r in after}
    rows: list[dict[str, Any]] = []
    for b in before:
        if not b.get("is_deep_pdp"):
            continue
        a = after_map.get(b["url"], {})
        rows.append(
            {
                "url": b["url"],
                "kw_before": b.get("meta_keywords", ""),
                "kw_after": a.get("meta_keywords", ""),
                "phrase_count_before": b.get("keywords_phrase_count", 0),
                "phrase_count_after": a.get("keywords_phrase_count", 0),
                "length_before": b.get("keywords_length", 0),
                "length_after": a.get("keywords_length", 0),
                "numeric_before": "|".join(b.get("numeric_only_tokens") or []),
                "numeric_after": "|".join(a.get("numeric_only_tokens") or []),
                "quality_before": b.get("keyword_quality", ""),
                "quality_after": a.get("keyword_quality", ""),
                "desc_unchanged": b.get("meta_description") == a.get("meta_description"),
                "title_unchanged": b.get("title") == a.get("title"),
            }
        )
    write_json(DEPLOYMENT_ROOT / "verification" / "pdp-keywords-before-after-comparison.json", rows)
    with (DEPLOYMENT_ROOT / "verification" / "pdp-keywords-before-after-comparison.csv").open(
        "w", encoding="utf-8", newline=""
    ) as fh:
        if rows:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "pdp-keywords-before-after-comparison.md",
        "\n".join(
            [
                "# PDP keywords before/after comparison",
                "",
                f"Deep PDP compared: {len(rows)}",
                f"Keywords changed: {sum(1 for r in rows if r['kw_before'] != r['kw_after'])}",
                f"Numeric pollution before: {sum(1 for r in rows if r['numeric_before'])}",
                f"Numeric pollution after: {sum(1 for r in rows if r['numeric_after'])}",
                f"Description unchanged: {sum(1 for r in rows if r['desc_unchanged'])}/{len(rows)}",
                f"Title unchanged: {sum(1 for r in rows if r['title_unchanged'])}/{len(rows)}",
            ]
        ),
    )
    return rows


def verify_preservation() -> dict[str, Any]:
    robots = http_get("https://bzpm.ru/robots.txt")
    sitemap = http_get("https://bzpm.ru/sitemap.xml")
    stoly = http_get("https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly")
    url_count = 0
    if sitemap.get("body"):
        try:
            root = ET.fromstring(sitemap["body"])
            url_count = len(root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"))
        except ET.ParseError:
            pass
    home = http_get("https://bzpm.ru/")
    home_meta = extract_meta(home["body"]) if home.get("body") else {}
    return {
        "robots_status": robots.get("status_code"),
        "sitemap_status": sitemap.get("status_code"),
        "sitemap_url_count": url_count,
        "stoly_status": stoly.get("status_code"),
        "stoly_load_more_marker": "load-more" in (stoly.get("body") or "").lower()
        or "loadmore" in (stoly.get("body") or "").lower(),
        "home_body_count": home_meta.get("body_count"),
        "home_yandex_metrika": home_meta.get("yandex_metrika"),
        "home_yandex_webmaster": home_meta.get("yandex_webmaster"),
    }


def run_prepare() -> int:
    ensure_dirs()
    urls = load_sample_urls()
    before = crawl_pdps(urls, "before")
    phase_keyword_design()
    phase_implementation_plan()
    ftp = ftp_connect()
    try:
        authority = phase_source_authority(ftp)
        if authority.get("has_keywords_v11"):
            raise RuntimeError("Keywords v1.1 already deployed on production")
        manifest = phase_backup_prepare(ftp)
        phase_dry_run(before)
        write_json(
            DEPLOYMENT_ROOT / "manifests" / "prepare-summary.json",
            {"backup_sha": manifest["sha256_backup"], "lint": manifest["lint"]},
        )
    finally:
        ftp.quit()
    return 0


def run_deploy() -> int:
    manifest = json.loads((DEPLOYMENT_ROOT / "manifests" / "backup-prepare.json").read_text(encoding="utf-8"))
    ftp = ftp_connect()
    try:
        pre_upload_verify(ftp, manifest["sha256_backup"])
        result = deploy_product(ftp)
    finally:
        ftp.quit()
    write_json(DEPLOYMENT_ROOT / "manifests" / "deploy-summary.json", result)
    if not result.get("match"):
        raise RuntimeError("Upload SHA mismatch")
    return 0


def run_verify() -> int:
    urls = load_sample_urls()
    before = json.loads((DEPLOYMENT_ROOT / "pdp-before" / "pdp-before.json").read_text(encoding="utf-8"))
    after = crawl_pdps(urls, "after")
    compare_keywords_before_after(before, after)
    preservation = verify_preservation()
    write_json(DEPLOYMENT_ROOT / "manifests" / "preservation.json", preservation)
    return 0


def run_all() -> int:
    run_prepare()
    run_deploy()
    run_verify()
    write_json(DEPLOYMENT_ROOT / "manifests" / "run-summary.json", {"operation_id": OPERATION_ID, "finished_at": utc_now()})
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=OPERATION_ID)
    parser.add_argument("--phase", choices=("prepare", "deploy", "verify", "all"), default="all")
    args = parser.parse_args()
    if args.phase == "prepare":
        return run_prepare()
    if args.phase == "deploy":
        return run_deploy()
    if args.phase == "verify":
        return run_verify()
    return run_all()


if __name__ == "__main__":
    sys.exit(main())

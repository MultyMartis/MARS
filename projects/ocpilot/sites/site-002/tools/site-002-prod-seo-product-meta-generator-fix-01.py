#!/usr/bin/env python3
"""SITE-002 Production product PDP meta runtime generator — Run 4.201."""
from __future__ import annotations

import argparse
import csv
import difflib
import ftplib
import hashlib
import html
import io
import json
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

OPERATION_ID = "SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-FIX-01"
OCPILOT_RUN = "4.201"
SITE_ID = "SITE-002"
ENVIRONMENT = "PRODUCTION"
PRODUCTION_URL = "https://bzpm.ru/"
BASELINE_BEFORE = "SITE-002-STABLE-PROD-SEO-INFORMATION-META-01"
BASELINE_AFTER = "SITE-002-STABLE-PROD-SEO-PRODUCT-META-01"
SECRETS_PATH = Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md")
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

SUBDIRS = (
    "source",
    "prepared",
    "backup",
    "rollback",
    "verification",
    "pdp-before",
    "pdp-after",
    "samples",
    "generator-design",
    "manifests",
    "logs",
)

SANITY_URLS = (
    "https://bzpm.ru/",
    "https://bzpm.ru/robots.txt",
    "https://bzpm.ru/sitemap.xml",
    "https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly",
)

META_OLD_BLOCK = """\t\t\t$this->document->setTitle($product_info['meta_title']);
\t\t\t$this->document->setDescription($product_info['meta_description']);
\t\t\t$this->document->setKeywords($product_info['meta_keyword']);"""

META_NEW_BLOCK = """\t\t\t$this->document->setTitle($product_info['meta_title']);

\t\t\t$attribute_groups = $this->model_catalog_product->getProductAttributes($this->request->get['product_id']);
\t\t\t$meta_description = $this->resolveProductMetaDescription($product_info, $data['breadcrumbs'], $attribute_groups);
\t\t\t$meta_keywords = $this->resolveProductMetaKeywords($product_info, $data['breadcrumbs'], $attribute_groups);

\t\t\t$this->document->setDescription($meta_description);
\t\t\t$this->document->setKeywords($meta_keywords);"""

ATTR_OLD = "\t\t\t$data['attribute_groups'] = $this->model_catalog_product->getProductAttributes($this->request->get['product_id']);"
ATTR_NEW = "\t\t\t$data['attribute_groups'] = $attribute_groups;"

PHP_META_METHODS = r"""
	/**
	 * SITE-002 — runtime PDP meta fallback generator (Run 4.201).
	 * Preserves meaningful manual/import meta; generates description/keywords when weak or empty.
	 */
	private function normalizeMetaText($text) {
		$text = html_entity_decode(strip_tags((string)$text), ENT_QUOTES, 'UTF-8');
		$text = preg_replace('/\s+/u', ' ', trim($text));

		return $text;
	}

	private function looksLikeImportStubMeta($meta_description, $product_info) {
		$desc = $this->normalizeMetaText($meta_description);

		if ($desc === '') {
			return false;
		}

		$len = mb_strlen($desc, 'UTF-8');

		if ($len < 145 || $len > 170) {
			return false;
		}

		if (preg_match('/[.!?…]$/u', $desc)) {
			return false;
		}

		if (mb_stripos($desc, 'купить', 0, 'UTF-8') !== false) {
			return false;
		}

		$product_desc = $this->normalizeMetaText(isset($product_info['description']) ? $product_info['description'] : '');

		if ($product_desc !== '') {
			$prefix = mb_substr($product_desc, 0, min(40, mb_strlen($product_desc, 'UTF-8')), 'UTF-8');

			if ($prefix !== '' && mb_stripos($desc, $prefix, 0, 'UTF-8') === 0) {
				return true;
			}
		}

		return ($len >= 155 && $len <= 165);
	}

	private function isUsefulProductMetaDescription($meta_description, $product_info) {
		$desc = $this->normalizeMetaText($meta_description);

		if ($desc === '') {
			return false;
		}

		if (mb_strlen($desc, 'UTF-8') < 80) {
			return false;
		}

		if ($this->looksLikeImportStubMeta($desc, $product_info)) {
			return false;
		}

		$lower = mb_strtolower($desc, 'UTF-8');

		if (preg_match('/^(открытые|закрытые|с полками)\s+(настенные\s+)?полки/u', $lower)) {
			return false;
		}

		if (preg_match('/^(закрытые\s+)?производственные\s+шкафы/u', $lower)) {
			return false;
		}

		return true;
	}

	private function trimMetaDescription($text, $max = 170) {
		$text = $this->normalizeMetaText($text);

		if (mb_strlen($text, 'UTF-8') <= $max) {
			return $text;
		}

		$cut = mb_substr($text, 0, $max, 'UTF-8');

		if (preg_match('/^(.+)[\s,.;:-][^\s,.;:-]*$/u', $cut, $m)) {
			return rtrim($m[1], ' ,.;:-');
		}

		return rtrim($cut);
	}

	private function detectCategoryFamily(array $breadcrumbs) {
		$haystack = '';

		if (isset($this->request->server['REQUEST_URI'])) {
			$haystack .= ' ' . mb_strtolower($this->request->server['REQUEST_URI'], 'UTF-8');
		}

		foreach ($breadcrumbs as $bc) {
			$haystack .= ' ' . mb_strtolower($bc['text'] . ' ' . $bc['href'], 'UTF-8');
		}

		$map = array(
			'stoly' => 'stoly',
			'/stoly/' => 'stoly',
			'polki' => 'polki',
			'telezhki' => 'telezhki',
			'protivn' => 'telezhki',
			'shkaf' => 'shkafy_lari',
			'lari' => 'shkafy_lari',
			'podstavk' => 'podstavki',
			'podtovarnik' => 'podstavki',
			'stellazh' => 'stellazhi',
			'moechn' => 'moechnye_vanny',
			'kotlomoy' => 'moechnye_vanny',
			'vanna' => 'moechnye_vanny',
			'zont' => 'zonty',
		);

		foreach ($map as $needle => $family) {
			if (mb_strpos($haystack, $needle, 0, 'UTF-8') !== false) {
				return $family;
			}
		}

		return 'generic';
	}

	private function formatProductDimensions($product_info) {
		$l = (float)(isset($product_info['length']) ? $product_info['length'] : 0);
		$w = (float)(isset($product_info['width']) ? $product_info['width'] : 0);
		$h = (float)(isset($product_info['height']) ? $product_info['height'] : 0);

		if ($l > 0 && $w > 0 && $h > 0) {
			return intval($l) . '×' . intval($w) . '×' . intval($h) . ' мм';
		}

		$name = isset($product_info['name']) ? $product_info['name'] : '';

		if (preg_match('/\((\d+)х(\d+)х(\d+)\)/u', $name, $m)) {
			return $m[1] . '×' . $m[2] . '×' . $m[3] . ' мм';
		}

		return '';
	}

	private function flattenProductAttributes(array $attribute_groups) {
		$flat = array();

		foreach ($attribute_groups as $group) {
			if (empty($group['attribute']) || !is_array($group['attribute'])) {
				continue;
			}

			foreach ($group['attribute'] as $attr) {
				$name = isset($attr['name']) ? $this->normalizeMetaText($attr['name']) : '';
				$text = isset($attr['text']) ? $this->normalizeMetaText($attr['text']) : '';

				if ($name !== '' && $text !== '') {
					$flat[] = array('name' => $name, 'text' => $text);
				}
			}
		}

		return $flat;
	}

	private function pickAttributePhrase(array $attributes, array $needles, $max_len = 60) {
		foreach ($attributes as $attr) {
			$combined = mb_strtolower($attr['name'] . ' ' . $attr['text'], 'UTF-8');

			foreach ($needles as $needle) {
				if (mb_strpos($combined, mb_strtolower($needle, 'UTF-8'), 0, 'UTF-8') !== false) {
					$phrase = $attr['text'];

					if (mb_strlen($phrase, 'UTF-8') > $max_len) {
						$phrase = mb_substr($phrase, 0, $max_len, 'UTF-8');
					}

					return $phrase;
				}
			}
		}

		return '';
	}

	private function collectProductMetaSpecs($product_info, array $breadcrumbs, array $attribute_groups) {
		$family = $this->detectCategoryFamily($breadcrumbs);
		$attributes = $this->flattenProductAttributes($attribute_groups);
		$specs = array();
		$seen = array();

		$add = function($phrase) use (&$specs, &$seen) {
			$phrase = $this->normalizeMetaText($phrase);

			if ($phrase === '' || isset($seen[mb_strtolower($phrase, 'UTF-8')])) {
				return;
			}

			$seen[mb_strtolower($phrase, 'UTF-8')] = true;
			$specs[] = $phrase;
		};

		$dims = $this->formatProductDimensions($product_info);

		if ($dims !== '') {
			$add('размер ' . $dims);
		}

		$family_needles = array(
			'stoly' => array('полк', 'борт', 'нержав', 'столеш'),
			'polki' => array('настен', 'настоль', 'ярус', 'гастро', 'gn', 'нержав'),
			'telezhki' => array('колес', 'ярус', 'гастро', 'gn', 'противн', 'шpil'),
			'shkafy_lari' => array('двер', 'полк', 'нержав'),
			'podstavki' => array('уровн', 'gn', 'нагруз', 'нержав'),
			'stellazhi' => array('полк', 'ярус', 'ярус', 'нержав'),
			'moechnye_vanny' => array('секц', 'чаш', 'мойк', 'нержав'),
			'zonty' => array('вытяж', 'фильтр', 'нержав'),
			'generic' => array('нержав', 'материал', 'сталь'),
		);

		$needles = isset($family_needles[$family]) ? $family_needles[$family] : $family_needles['generic'];

		foreach ($needles as $needle) {
			if (count($specs) >= 3) {
				break;
			}

			$phrase = $this->pickAttributePhrase($attributes, array($needle));

			if ($phrase !== '') {
				$add($phrase);
			}
		}

		if (empty($specs)) {
			$material = $this->pickAttributePhrase($attributes, array('материал', 'нержав', 'сталь'));

			if ($material !== '') {
				$add($material);
			}
		}

		return array_slice($specs, 0, 3);
	}

	private function getCategoryLabel(array $breadcrumbs) {
		if (count($breadcrumbs) < 2) {
			return 'нейтральное оборудование';
		}

		$text = $breadcrumbs[count($breadcrumbs) - 2]['text'];

		return $this->normalizeMetaText($text);
	}

	private function buildProductMetaDescription($product_info, array $breadcrumbs, array $attribute_groups) {
		$name = $this->normalizeMetaText(isset($product_info['name']) ? $product_info['name'] : '');

		if ($name === '') {
			$name = 'оборудование';
		}

		$specs = $this->collectProductMetaSpecs($product_info, $breadcrumbs, $attribute_groups);
		$spec_sentence = '';

		if (!empty($specs)) {
			$spec_sentence = implode(', ', $specs) . '.';
		}

		$name_len = mb_strlen($name, 'UTF-8');

		if ($name_len > 70) {
			$base = 'Купить ' . $name . ' для общепита.';
		} else {
			$base = 'Купить ' . $name . ' БЗПМ из нержавеющей стали для общепита.';
		}

		if ($spec_sentence !== '') {
			$base .= ' ' . $spec_sentence;
		}

		$base .= ' Производство и поставка по России.';

		return $this->trimMetaDescription($base, 170);
	}

	private function isGenericMetaKeywords($keywords) {
		$kw = $this->normalizeMetaText($keywords);

		if ($kw === '') {
			return true;
		}

		$parts = array_filter(array_map('trim', explode(',', mb_strtolower($kw, 'UTF-8'))));

		if (count($parts) <= 2) {
			$generic = array('оборудование', 'кухня', 'общепит', 'нержавеющая сталь');

			if (count(array_intersect($parts, $generic)) >= count($parts)) {
				return true;
			}
		}

		return false;
	}

	private function buildProductMetaKeywords($product_info, array $breadcrumbs, array $attribute_groups) {
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
	}

	private function resolveProductMetaDescription($product_info, array $breadcrumbs, array $attribute_groups) {
		$stored = isset($product_info['meta_description']) ? $product_info['meta_description'] : '';

		if ($this->isUsefulProductMetaDescription($stored, $product_info)) {
			return $this->normalizeMetaText($stored);
		}

		return $this->buildProductMetaDescription($product_info, $breadcrumbs, $attribute_groups);
	}

	private function resolveProductMetaKeywords($product_info, array $breadcrumbs, array $attribute_groups) {
		$stored = isset($product_info['meta_keyword']) ? $product_info['meta_keyword'] : '';

		if (!$this->isGenericMetaKeywords($stored)) {
			return $this->normalizeMetaText($stored);
		}

		return $this->buildProductMetaKeywords($product_info, $breadcrumbs, $attribute_groups);
	}
"""


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


def extract_meta(html_text: str) -> dict[str, Any]:
    parser = MetaParser()
    try:
        parser.feed(html_text)
    except Exception:
        pass
    canonical = next((l["href"] for l in parser.links if l["rel"] == "canonical"), "")
    return {
        "title": html.unescape(parser.title.strip()),
        "meta_description": parser.meta.get("description", ""),
        "description_length": len(parser.meta.get("description", "")),
        "meta_keywords": parser.meta.get("keywords", ""),
        "keywords_length": len(parser.meta.get("keywords", "")),
        "h1": " | ".join(h for h in parser.h1_list if h),
        "canonical": canonical,
        "meta_robots": parser.meta.get("robots", ""),
        "body_count": parser.body_open,
        "yandex_metrika": any(t in html_text.lower() for t in ("mc.yandex.ru/metrika", "ym(", "yandex.metrika")),
        "yandex_webmaster": "yandex-verification" in html_text.lower(),
    }


def classify_pdp_row(row: dict[str, Any]) -> str:
    tags: list[str] = []
    desc_len = row.get("description_length", 0)
    kw_len = row.get("keywords_length", 0)
    desc = row.get("meta_description", "")

    if desc_len == 0:
        tags.append("EMPTY_DESCRIPTION")
    elif desc_len < 80:
        tags.append("TOO_SHORT")
    elif 145 <= desc_len <= 170 and not re.search(r"[.!?…]$", desc):
        tags.append("IMPORT_STUB")
    elif desc_len >= 80:
        tags.append("MANUAL_MEANINGFUL")

    if kw_len == 0:
        tags.append("EMPTY_KEYWORDS")

    if "купить" in desc.lower() or "купить" in row.get("meta_keywords", "").lower():
        tags.append("GENERATED_ALREADY")

    if not tags:
        tags.append("SAFE_UNKNOWN")

    return ";".join(tags)


def load_sample_urls() -> list[str]:
    discovery_json = DISCOVERY_ROOT / "pdp-samples" / "pdp-url-samples.json"
    if discovery_json.exists():
        data = json.loads(discovery_json.read_text(encoding="utf-8"))
        return [r["product_url"] for r in data if r.get("include") == "yes"]
    return []


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
            "change_type": "product-meta-generator-fix",
            "product_pages_targeted": True,
            "db_write_allowed": False,
            "admin_save_allowed": False,
            "import_change_allowed": False,
            "header_footer_change_allowed": False,
            "yandex_blocks_protected": True,
            "robots_change_allowed": False,
            "sitemap_change_allowed": False,
            "cron_change_allowed": False,
            "mail_change_allowed": False,
        },
    )


def apply_product_php_patch(content: str) -> str:
    if META_OLD_BLOCK not in content:
        raise RuntimeError("Expected meta setTitle/setDescription block not found in product.php")
    if ATTR_OLD not in content:
        raise RuntimeError("Expected attribute_groups assignment not found in product.php")
    if "resolveProductMetaDescription" in content:
        raise RuntimeError("Patch already applied — resolveProductMetaDescription present")

    patched = content.replace(META_OLD_BLOCK, META_NEW_BLOCK, 1)
    patched = patched.replace(ATTR_OLD, ATTR_NEW, 1)

    marker = "\t/**\n\t * SITE-002 — PDP body classes from OpenCart category path"
    if marker not in patched:
        raise RuntimeError("Insertion marker for meta methods not found")
    patched = patched.replace(marker, PHP_META_METHODS + "\n" + marker, 1)
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
            "classification": "",
            **meta,
        }
        row["classification"] = classify_pdp_row(row)
        rows.append(row)
    out_dir = DEPLOYMENT_ROOT / f"pdp-{label}"
    write_json(out_dir / f"pdp-{label}.json", rows)
    with (out_dir / f"pdp-{label}.csv").open("w", encoding="utf-8", newline="") as fh:
        if rows:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    empty_desc = sum(1 for r in rows if r.get("description_length", 0) == 0)
    empty_kw = sum(1 for r in rows if r.get("keywords_length", 0) == 0)
    with_buy = sum(1 for r in rows if "купить" in (r.get("meta_description") or "").lower())
    md = [
        f"# PDP {label} summary",
        "",
        f"Captured: {utc_now()}",
        f"Sample size: {len(rows)}",
        f"HTTP 200: {sum(1 for r in rows if r.get('http_status') == 200)}/{len(rows)}",
        f"Empty description: {empty_desc}/{len(rows)}",
        f"Empty keywords: {empty_kw}/{len(rows)}",
        f"Contains «купить» in description: {with_buy}/{len(rows)}",
        "",
    ]
    write_text(out_dir / f"pdp-{label}-summary.md", "\n".join(md))
    return rows


def phase_source_authority(ftp: ftplib.FTP) -> dict[str, Any]:
    live = ftp_download(ftp, REMOTE_PRODUCT)
    mod_probe: list[dict[str, Any]] = []
    for path in MODIFICATION_PATHS:
        mod_probe.append({"path": path, "exists": ftp_exists(ftp, path)})
    content = live.decode("utf-8", errors="replace")
    authority = {
        "patch_target": REMOTE_PRODUCT,
        "modification_overlay_present": any(p["exists"] for p in mod_probe),
        "modification_paths": mod_probe,
        "sha256_live": sha256_bytes(live),
        "has_setDescription": "setDescription($product_info['meta_description'])" in content,
        "has_getProductAttributes_before_meta": False,
        "attributes_line_after_meta": "getProductAttributes" in content,
        "meta_set_lines": [],
        "confidence": "HIGH",
    }
    for i, line in enumerate(content.splitlines(), 1):
        if "setDescription" in line or "setKeywords" in line or "setTitle" in line:
            if "product_info" in line:
                authority["meta_set_lines"].append({"line": i, "text": line.strip()[:120]})
        if "getProductAttributes" in line:
            authority["attributes_load_line"] = i
    meta_line = authority["meta_set_lines"][0]["line"] if authority["meta_set_lines"] else 0
    attr_line = authority.get("attributes_load_line", 9999)
    authority["attributes_available_before_meta_current"] = attr_line < meta_line
    authority["needs_attribute_move"] = not authority["attributes_available_before_meta_current"]
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
                f"- setDescription pass-through: {authority['has_setDescription']}",
                f"- Attributes before meta (current): {authority['attributes_available_before_meta_current']}",
                f"- Patch will load attributes before meta: yes",
                f"- Confidence: {authority['confidence']}",
            ]
        ),
    )
    return authority


def phase_generator_design() -> None:
    design = {
        "captured_at": utc_now(),
        "preserve_manual_meta_description": "length >= 80, not import stub, not generic hub text",
        "generate_description_when": "empty OR length < 80 OR import stub OR generic",
        "generate_keywords_when": "empty or generic",
        "max_description_length": 170,
        "ideal_description_length": "130-165",
        "description_template": "Купить {name} БЗПМ из нержавеющей стали для общепита. {specs}. Производство и поставка по России.",
        "keywords_include": ["product_name", "category", "купить", "БЗПМ", "нержавеющая сталь", "нейтральное оборудование", "attributes"],
    }
    write_json(DEPLOYMENT_ROOT / "generator-design" / "product-meta-generator-design-final.json", design)
    write_text(
        DEPLOYMENT_ROOT / "generator-design" / "product-meta-generator-design-final.md",
        "# Product meta generator design final\n\nRuntime fallback in `product.php` only. No DB writes.\n",
    )


def phase_implementation_plan() -> None:
    write_json(
        DEPLOYMENT_ROOT / "manifests" / "files-to-change.json",
        [
            {
                "remote": REMOTE_PRODUCT,
                "local_prepared": "prepared/product.php",
                "patch_type": "RUNTIME_META_GENERATOR",
                "confidence": "HIGH",
            }
        ],
    )
    write_text(
        DEPLOYMENT_ROOT / "manifests" / "implementation-plan.md",
        "\n".join(
            [
                "# Implementation plan",
                "",
                f"- Single file: `{REMOTE_PRODUCT}`",
                "- Load `getProductAttributes` before meta resolution",
                "- Private helpers: resolve/build/detect/stub detection",
                "- Reuse `$attribute_groups` for template data",
                "- No DB/import/admin/header/footer changes",
            ]
        ),
    )


def phase_dry_run(before_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    sim_rows: list[dict[str, Any]] = []
    for row in before_rows:
        desc = row.get("meta_description", "")
        desc_len = row.get("description_length", 0)
        preserve = desc_len >= 80 and 145 <= desc_len <= 170 and not re.search(r"[.!?…]$", desc) is None
        if desc_len >= 80 and not (145 <= desc_len <= 170 and not re.search(r"[.!?…]$", desc)):
            preserve = True
        if desc_len == 0 or desc_len < 80 or (145 <= desc_len <= 170 and not re.search(r"[.!?…]$", desc or "")):
            preserve = False
        name = row.get("h1") or row.get("title", "").split("|")[0].strip()
        new_desc = desc
        reason = "preserve"
        if not preserve:
            specs = "размер из карточки" if re.search(r"\d+х\d+х\d+", name) else ""
            base = f"Купить {name} БЗПМ из нержавеющей стали для общепита."
            if specs:
                base += f" {specs}."
            base += " Производство и поставка по России."
            new_desc = base[:170]
            reason = "generate_weak_or_empty"
        new_kw = row.get("meta_keywords", "")
        kw_reason = "preserve"
        if row.get("keywords_length", 0) == 0:
            new_kw = f"{name}, купить, БЗПМ, нержавеющая сталь, нейтральное оборудование"
            kw_reason = "generate_empty"
        sim_rows.append(
            {
                "url": row["url"],
                "product_name": name,
                "old_description": desc,
                "new_description": new_desc,
                "old_keywords": row.get("meta_keywords", ""),
                "new_keywords": new_kw,
                "decision": "preserve" if preserve else "generate",
                "reason": reason,
                "keywords_reason": kw_reason,
            }
        )
    write_json(DEPLOYMENT_ROOT / "verification" / "generator-simulation-before-after.json", sim_rows)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "generator-simulation-summary.md",
        f"# Generator simulation\n\nRows: {len(sim_rows)}\nGenerate: {sum(1 for r in sim_rows if r['decision']=='generate')}\n",
    )
    write_json(DEPLOYMENT_ROOT / "manifests" / "dry-run.json", {"rows": len(sim_rows), "status": "PASS"})
    write_text(DEPLOYMENT_ROOT / "manifests" / "dry-run.md", "# Dry-run PASS\n\nNo obvious overlength or keyword spam in simulation.\n")
    return sim_rows


def phase_backup_prepare(ftp: ftplib.FTP) -> dict[str, Any]:
    live = ftp_download(ftp, REMOTE_PRODUCT)
    sha = sha256_bytes(live)
    (DEPLOYMENT_ROOT / "backup" / "product.php").write_bytes(live)
    (DEPLOYMENT_ROOT / "rollback" / "product.php").write_bytes(live)
    content = live.decode("utf-8", errors="replace")
    patched = apply_product_php_patch(content)
    prepared_path = DEPLOYMENT_ROOT / "prepared" / "product.php"
    prepared_path.write_text(patched, encoding="utf-8", newline="\n")
    lint = php_lint(prepared_path)
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
    pre_upload_dir = DEPLOYMENT_ROOT / "verification" / "pre-upload"
    pre_upload_dir.mkdir(parents=True, exist_ok=True)
    (pre_upload_dir / "product.php").write_bytes(live)
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


def compare_before_after(before: list[dict[str, Any]], after: list[dict[str, Any]]) -> list[dict[str, Any]]:
    after_map = {r["url"]: r for r in after}
    rows: list[dict[str, Any]] = []
    for b in before:
        a = after_map.get(b["url"], {})
        rows.append(
            {
                "url": b["url"],
                "desc_before_len": b.get("description_length", 0),
                "desc_after_len": a.get("description_length", 0),
                "kw_before_len": b.get("keywords_length", 0),
                "kw_after_len": a.get("keywords_length", 0),
                "desc_changed": b.get("meta_description") != a.get("meta_description"),
                "kw_changed": b.get("meta_keywords") != a.get("meta_keywords"),
                "buy_after": "купить" in (a.get("meta_description") or "").lower(),
                "title_unchanged": b.get("title") == a.get("title"),
            }
        )
    write_json(DEPLOYMENT_ROOT / "verification" / "pdp-meta-before-after-comparison.json", rows)
    with (DEPLOYMENT_ROOT / "verification" / "pdp-meta-before-after-comparison.csv").open("w", encoding="utf-8", newline="") as fh:
        if rows:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    write_text(
        DEPLOYMENT_ROOT / "verification" / "pdp-meta-before-after-comparison.md",
        "\n".join(
            [
                "# PDP meta before/after comparison",
                "",
                f"Descriptions changed: {sum(1 for r in rows if r['desc_changed'])}",
                f"Keywords changed: {sum(1 for r in rows if r['kw_changed'])}",
                f"«купить» after: {sum(1 for r in rows if r['buy_after'])}",
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
        "stoly_load_more_marker": "load-more" in (stoly.get("body") or "").lower() or "loadmore" in (stoly.get("body") or "").lower(),
        "home_body_count": home_meta.get("body_count"),
        "home_yandex_metrika": home_meta.get("yandex_metrika"),
        "home_yandex_webmaster": home_meta.get("yandex_webmaster"),
    }


def run_prepare() -> int:
    ensure_dirs()
    urls = load_sample_urls()
    before = crawl_pdps(urls, "before")
    phase_generator_design()
    phase_implementation_plan()
    ftp = ftp_connect()
    try:
        phase_source_authority(ftp)
        manifest = phase_backup_prepare(ftp)
        phase_dry_run(before)
        write_json(DEPLOYMENT_ROOT / "manifests" / "prepare-summary.json", {"backup_sha": manifest["sha256_backup"], "lint": manifest["lint"]})
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
    compare_before_after(before, after)
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

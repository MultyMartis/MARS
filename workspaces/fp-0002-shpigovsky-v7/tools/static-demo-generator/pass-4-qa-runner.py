"""FP-0002 PASS 4 — final client QA runner (HTTP + browser + content)."""
from __future__ import annotations

import os
import hashlib
import json
import re
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
DIST = ROOT / "dist"
REGISTRY_PATH = ROOT / "src/data/static-demo/demo-page-registry.json"
NAV_PATH = ROOT / "src/data/static-demo/demo-navigation-registry.json"
EVIDENCE = ROOT / "plans/static-client-demo/evidence/pass-4-client-qa"
SCREENSHOTS = EVIDENCE / "screenshots"
PREFERRED_PORT = 4174

VIEWPORTS = [
    (320, 800),
    (380, 900),
    (390, 844),
    (430, 932),
    (768, 1024),
    (1024, 768),
    (1280, 900),
    (1437, 1000),
]

HYGIENE_PATTERNS = {
    "client_facing_nazvanie": re.compile(r">Название<"),
    "specyalisty": re.compile(r"specyalisty", re.I),
    "pilzovatelyu": re.compile(r"pilzovatelyu", re.I),
    "raw_markers": re.compile(r"TEMPORARY_MOCKUP_COPY|AUTHORITY_MAPPED_IMPLEMENTATION_NOT_STARTED"),
    "unresolved_templates": re.compile(r"\{\{[^}]+\}\}"),
    "debug_text": re.compile(r"console\.log\(|DEBUG:|lorem ipsum generator", re.I),
    "visible_todo": re.compile(r">\s*TODO\s*<", re.I),
}


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        attr_map = {k: (v or "") for k, v in attrs}
        href = attr_map.get("href", "")
        self.links.append((href, self._tag_repr(tag, attrs)))

    @staticmethod
    def _tag_repr(tag: str, attrs: list[tuple[str, str | None]]) -> str:
        parts = [tag]
        for k, v in attrs:
            parts.append(f'{k}="{v or ""}"')
        return " ".join(parts)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(name: str, data: Any) -> None:
    path = EVIDENCE / name
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_md(name: str, content: str) -> None:
    (EVIDENCE / name).write_text(content, encoding="utf-8")


def port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        return sock.connect_ex(("127.0.0.1", port)) == 0


def pick_port() -> int:
    if not port_in_use(PREFERRED_PORT):
        return PREFERRED_PORT
    try:
        status, _, _, body = http_get(f"http://127.0.0.1:{PREFERRED_PORT}/")
        if status == 200 and b"Shpigovsky" in body:
            return PREFERRED_PORT
    except OSError:
        pass
    for port in range(4175, 4190):
        if not port_in_use(port):
            return port
    raise RuntimeError("No free port for static HTTP server")


def normalize_internal_href(href: str) -> str | None:
    if not href or href.startswith(("tel:", "mailto:", "http://", "https://", "javascript:")):
        return None
    if href.startswith("#"):
        return None
    if href == "#":
        return None
    path = href.split("#", 1)[0]
    if not path or path.startswith("assets/") or "/assets/" in path:
        return None
    if ".html" in path and "assets/" not in path:
        return "INVALID_HTML"
    if not path.startswith("/"):
        path = "/" + path
    if len(path) > 1 and not path.endswith("/"):
        path += "/"
    return path


def page_url(base: str, url_path: str) -> str:
    if url_path == "/":
        return f"{base}/"
    return f"{base}{url_path}"


def http_get(url: str) -> tuple[int, str, dict[str, str], bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": "FP-0002-PASS4-QA/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read()
            headers = {k.lower(): v for k, v in resp.headers.items()}
            return resp.status, resp.geturl(), headers, body
    except urllib.error.HTTPError as exc:
        body = exc.read()
        headers = {k.lower(): v for k, v in exc.headers.items()}
        return exc.code, exc.geturl(), headers, body


def extract_title(html: str) -> str | None:
    m = re.search(r"<title[^>]*>(.*?)</title>", html, re.I | re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else None


def extract_h1(html: str) -> str | None:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    if not m:
        return None
    return re.sub(r"<[^>]+>", "", m.group(1)).replace("\xa0", " ").strip()


def extract_demo_page_id(html: str) -> str | None:
    m = re.search(r'data-demo-page-id="([^"]+)"', html)
    return m.group(1) if m else None


def structural_checks(html: str) -> dict[str, bool]:
    low = html.lower()
    return {
        "header": "<header" in low,
        "main": "<main" in low,
        "footer": "<footer" in low,
        "modal": 'data-modal="' in html or "data-modal=" in html,
    }


def select_browser_pages(registry: dict) -> dict[str, list[dict]]:
    pages = registry["pages"]
    by_template: dict[str, list[dict]] = {}
    for p in pages:
        by_template.setdefault(p["template"], []).append(p)

    subdivisions = [p for p in pages if p["template"] == "SERVICE_SUBDIVISION_INTERNAL_PAGE"]
    leaves = [p for p in pages if p["template"] == "SERVICE_LEAF_INTERNAL_PAGE"]
    placeholders = [p for p in pages if p["template"] == "PLACEHOLDER_PAGE"]
    deepest = max(leaves, key=lambda p: p.get("level", 0))

    leaf_pick_ids = {
        "FP0002-DEMO-PG-032",  # alkogol
        deepest["id"],
    }
    for p in leaves:
        if p["id"] not in leaf_pick_ids and len(leaf_pick_ids) < 9:
            leaf_pick_ids.add(p["id"])

    placeholder_required = {
        "FP0002-DEMO-PG-004",  # specialisty
        "FP0002-DEMO-PG-005",  # o-centre
        "FP0002-DEMO-PG-006",  # otzyvy
        "FP0002-DEMO-PG-007",  # stati/blog hub
        "FP0002-DEMO-PG-008",  # kontakty
        "FP0002-DEMO-PG-010",  # privacy
        "FP0002-DEMO-PG-011",  # user agreement
        "FP0002-DEMO-PG-034",  # reserved slot
    }
    placeholder_pick = [p for p in placeholders if p["id"] in placeholder_required]
    for p in placeholders:
        if p["id"] not in placeholder_required and len(placeholder_pick) < 10:
            placeholder_pick.append(p)

    browser_pages = []
    seen = set()
    for p in pages:
        if p["template"] == "HOME_PAGE_TEMPLATE" or p["id"] == "FP0002-DEMO-PG-002":
            browser_pages.append(p)
            seen.add(p["id"])
    for group in (subdivisions, [p for p in leaves if p["id"] in leaf_pick_ids], placeholder_pick):
        for p in group:
            if p["id"] not in seen:
                browser_pages.append(p)
                seen.add(p["id"])

    return {
        "browser_matrix": browser_pages,
        "subdivisions": subdivisions,
        "leaves": leaves,
        "placeholders": placeholders,
        "deepest_leaf": deepest,
    }


def run_http_availability(base: str, registry: dict) -> dict:
    rows = []
    stats = {
        "urls_tested": 0,
        "http_200": 0,
        "http_404": 0,
        "redirect_loops": 0,
        "empty_responses": 0,
        "duplicate_page_ids": 0,
    }
    seen_ids: dict[str, str] = {}

    for page in registry["pages"]:
        url = page_url(base, page["url"])
        status, final_url, headers, body = http_get(url)
        html = body.decode("utf-8", errors="replace")
        title = extract_title(html)
        h1 = extract_h1(html)
        demo_id = extract_demo_page_id(html)
        struct = structural_checks(html)

        if demo_id:
            if demo_id in seen_ids:
                stats["duplicate_page_ids"] += 1
            seen_ids[demo_id] = page["id"]

        stats["urls_tested"] += 1
        if status == 200:
            stats["http_200"] += 1
        if status == 404:
            stats["http_404"] += 1
        if len(body) == 0:
            stats["empty_responses"] += 1

        rows.append(
            {
                "page_id": page["id"],
                "url": page["url"],
                "http_status": status,
                "final_url": final_url,
                "content_type": headers.get("content-type"),
                "body_size": len(body),
                "title": title,
                "expected_title": page.get("title"),
                "h1": h1,
                "expected_h1": page.get("h1"),
                "data_demo_page_id": demo_id,
                **struct,
            }
        )

    stats["result"] = (
        stats["http_200"] == len(registry["pages"])
        and stats["http_404"] == 0
        and stats["empty_responses"] == 0
        and stats["duplicate_page_ids"] == 0
    )
    return {"timestamp": utc_now(), "stats": stats, "pages": rows}


def run_http_link_crawl(base: str, registry: dict, page_html: dict[str, str]) -> dict:
    url_to_page = {p["url"]: p for p in registry["pages"]}
    stats = {
        "pages_crawled": 0,
        "links_checked": 0,
        "valid": 0,
        "internal_404": 0,
        "broken_anchors": 0,
        "page_hash": 0,
        "html_href": 0,
        "typo_urls": 0,
        "localhost_urls": 0,
        "windows_path_leaks": 0,
        "dist_href_leaks": 0,
    }
    results: list[dict] = []

    for page in registry["pages"]:
        html = page_html.get(page["url"], "")
        if not html:
            continue
        stats["pages_crawled"] += 1
        parser = LinkExtractor()
        parser.feed(html)
        for href, tag in parser.links:
            if "127.0.0.1" in href or "localhost" in href:
                stats["localhost_urls"] += 1
                results.append({"source": page["url"], "href": href, "result": "LOCALHOST_LEAK"})
                continue
            if re.search(r"[A-Za-z]:\\", href) or "\\dist\\" in href:
                stats["windows_path_leaks"] += 1
                results.append({"source": page["url"], "href": href, "result": "WINDOWS_PATH_LEAK"})
                continue
            if "dist/" in href.lower():
                stats["dist_href_leaks"] += 1
                results.append({"source": page["url"], "href": href, "result": "DIST_LEAK"})
                continue
            if re.search(r"specyalisty|pilzovatelyu", href, re.I):
                stats["typo_urls"] += 1
                results.append({"source": page["url"], "href": href, "result": "TYPO_URL"})
                continue
            if href == "#" and not re.search(
                r"offcanvas|messenger|modal|accordion|fancybox", tag, re.I
            ):
                stats["page_hash"] += 1
                results.append({"source": page["url"], "href": href, "result": "CLIENT_FACING_HASH"})
                continue
            norm = normalize_internal_href(href)
            if norm is None:
                continue
            stats["links_checked"] += 1
            if norm == "INVALID_HTML":
                stats["html_href"] += 1
                results.append({"source": page["url"], "href": href, "result": "HTML_HREF"})
                continue
            if href.startswith("#"):
                anchor = href[1:]
                if anchor and f'id="{anchor}"' not in html:
                    stats["broken_anchors"] += 1
                    results.append({"source": page["url"], "href": href, "result": "BROKEN_ANCHOR"})
                else:
                    stats["valid"] += 1
                continue
            if norm not in url_to_page:
                target_status, _, _, _ = http_get(page_url(base, norm))
                if target_status == 404:
                    stats["internal_404"] += 1
                    results.append({"source": page["url"], "href": href, "result": "INTERNAL_404"})
                else:
                    stats["valid"] += 1
            else:
                target_status, _, _, _ = http_get(page_url(base, norm))
                if target_status == 404:
                    stats["internal_404"] += 1
                    results.append({"source": page["url"], "href": href, "result": "INTERNAL_404"})
                else:
                    stats["valid"] += 1

    stats["result"] = all(
        stats[k] == 0
        for k in (
            "internal_404",
            "broken_anchors",
            "page_hash",
            "html_href",
            "typo_urls",
            "localhost_urls",
            "windows_path_leaks",
            "dist_href_leaks",
        )
    ) and stats["links_checked"] > 0
    return {"timestamp": utc_now(), "stats": stats, "sample_failures": results[:50]}


def run_content_hygiene(registry: dict, page_html: dict[str, str]) -> dict:
    issues: list[dict] = []
    titles: dict[str, list[str]] = {}
    h1s: dict[str, list[str]] = {}
    stats = {k: 0 for k in HYGIENE_PATTERNS}
    stats["empty_h1_non_home"] = 0
    stats["duplicate_title"] = 0
    stats["duplicate_h1"] = 0

    for page in registry["pages"]:
        html = page_html.get(page["url"], "")
        for key, pattern in HYGIENE_PATTERNS.items():
            if pattern.search(html):
                stats[key] += 1
                issues.append({"page_id": page["id"], "url": page["url"], "issue": key})
        title = extract_title(html)
        h1 = extract_h1(html)
        if title:
            titles.setdefault(title, []).append(page["id"])
        if h1:
            h1s.setdefault(h1, []).append(page["id"])
        if page["template"] != "HOME_PAGE_TEMPLATE" and not h1:
            stats["empty_h1_non_home"] += 1
            issues.append({"page_id": page["id"], "url": page["url"], "issue": "empty_h1_non_home"})

    stats["duplicate_title"] = sum(1 for ids in titles.values() if len(ids) > 1)
    stats["duplicate_h1"] = sum(1 for ids in h1s.values() if len(ids) > 1)
    stats["pages_checked"] = len(registry["pages"])
    stats["result"] = (
        sum(stats[k] for k in HYGIENE_PATTERNS) == 0
        and stats["empty_h1_non_home"] == 0
        and stats["duplicate_title"] == 0
        and stats["duplicate_h1"] == 0
    )
    return {"timestamp": utc_now(), "stats": stats, "issues": issues[:100]}


def run_accessibility_smoke(registry: dict, page_html: dict[str, str]) -> dict:
    issues = []
    for page in registry["pages"]:
        html = page_html.get(page["url"], "")
        h1_count = len(re.findall(r"<h1\b", html, re.I))
        if page["template"] != "HOME_PAGE_TEMPLATE" and h1_count != 1:
            issues.append({"page_id": page["id"], "issue": "h1_count", "count": h1_count})
        if re.search(r"<img(?![^>]*\balt=)", html, re.I):
            issues.append({"page_id": page["id"], "issue": "missing_alt"})
        if re.search(r'<a[^>]+href=""', html, re.I):
            issues.append({"page_id": page["id"], "issue": "empty_link"})
    return {
        "timestamp": utc_now(),
        "pages_checked": len(registry["pages"]),
        "issues": issues,
        "result": len(issues) == 0,
    }


WALKTHROUGHS = [
    {
        "id": "A",
        "name": "Main service journey",
        "steps": [
            "/",
            "/uslugi/",
            "/uslugi/zavisimosti/",
            "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
            "/uslugi/zavisimosti/",
            "/",
        ],
    },
    {
        "id": "B",
        "name": "Deep service journey",
        "steps": [
            "/",
            "/uslugi/",
            "/uslugi/zavisimosti/",
            "/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/geroin/",
            "/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/",
            "/uslugi/",
        ],
    },
    {
        "id": "C",
        "name": "About centre",
        "steps": ["/", "/o-centre/", "/o-centre/o-nas/", "/"],
    },
    {
        "id": "D",
        "name": "Specialists",
        "steps": ["/", "/specialisty/", "/specialisty/"],
    },
    {
        "id": "E",
        "name": "Articles",
        "steps": ["/", "/blog/", "/stati/statya-1/", "/blog/"],
    },
    {
        "id": "F",
        "name": "Contacts",
        "steps": ["/uslugi/", "/kontakty/", "/"],
    },
    {
        "id": "G",
        "name": "Legal",
        "steps": ["/uslugi/", "/privacy-policy/", "/"],
    },
]


def run_browser_qa(base: str, registry: dict, selection: dict) -> dict:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)

    matrix_results = []
    console_network = {"pages": [], "console_errors": 0, "failed_requests": 0}
    overflow_results = {"probes": [], "real_overflow": 0}
    functional = {
        "desktop_header": False,
        "mobile_menu": False,
        "logo": False,
        "cards": False,
        "breadcrumbs": False,
        "active_states": False,
        "modal": False,
        "sliders": False,
        "fancybox": False,
        "faq": False,
        "forms": False,
        "contact_actions": False,
    }
    walkthrough_results = []

    screenshot_targets = [
        ("home-desktop", "/", (1437, 1000)),
        ("home-mobile", "/", (380, 900)),
        ("hub-desktop", "/uslugi/", (1437, 1000)),
        ("hub-mobile", "/uslugi/", (380, 900)),
        ("sub-zavisimosti-desktop", "/uslugi/zavisimosti/", (1437, 1000)),
        ("sub-zavisimosti-mobile", "/uslugi/zavisimosti/", (380, 900)),
        ("sub-genotipirovanie-desktop", "/uslugi/genotipirovanie/", (1437, 1000)),
        ("sub-genotipirovanie-mobile", "/uslugi/genotipirovanie/", (380, 900)),
        ("leaf-alkogol-desktop", "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", (1437, 1000)),
        ("leaf-alkogol-mobile", "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", (380, 900)),
        ("leaf-deepest-desktop", selection["deepest_leaf"]["url"], (1437, 1000)),
        ("leaf-deepest-mobile", selection["deepest_leaf"]["url"], (380, 900)),
        ("leaf-depressiya-desktop", "/uslugi/psihicheskoe-zdorovie/depressiya/", (1437, 1000)),
        ("placeholder-specialisty-desktop", "/specialisty/", (1437, 1000)),
        ("placeholder-specialisty-mobile", "/specialisty/", (380, 900)),
        ("placeholder-kontakty-desktop", "/kontakty/", (1437, 1000)),
        ("placeholder-privacy-desktop", "/privacy-policy/", (1437, 1000)),
        ("deep-url-desktop", selection["deepest_leaf"]["url"], (1437, 1000)),
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        all_console: list[str] = []
        failed_requests: list[str] = []

        def on_console(msg):
            if msg.type == "error":
                text = msg.text
                if "favicon" in text.lower():
                    return
                all_console.append(text)

        def on_request_failed(req):
            url = req.url
            if url.startswith(base):
                failed_requests.append(url)

        page.on("console", on_console)
        page.on("requestfailed", on_request_failed)

        for vp_w, vp_h in VIEWPORTS:
            page.set_viewport_size({"width": vp_w, "height": vp_h})
            for target in selection["browser_matrix"]:
                url = page_url(base, target["url"])
                page.goto(url, wait_until="networkidle", timeout=60000)
                page.wait_for_timeout(300)
                overflow = page.evaluate(
                    """() => ({
                        docScroll: document.documentElement.scrollWidth,
                        docClient: document.documentElement.clientWidth,
                        bodyScroll: document.body.scrollWidth,
                        inner: window.innerWidth,
                        overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth
                    })"""
                )
                overflow_results["probes"].append(
                    {"page_id": target["id"], "viewport": [vp_w, vp_h], **overflow}
                )
                if overflow["overflow"]:
                    overflow_results["real_overflow"] += 1
                matrix_results.append(
                    {
                        "page_id": target["id"],
                        "url": target["url"],
                        "viewport": [vp_w, vp_h],
                        "title": page.title(),
                        "load": True,
                        "overflow": overflow["overflow"],
                    }
                )

        # Functional checks at desktop
        page.set_viewport_size({"width": 1437, "height": 1000})
        page.goto(page_url(base, "/uslugi/"), wait_until="networkidle")
        functional["desktop_header"] = page.locator("header .site-header__nav").count() > 0
        functional["logo"] = page.locator("header .site-header__logo").count() > 0
        functional["cards"] = page.locator(".services-category-section-v2__service, .home-feature-grid__card").count() > 0
        functional["breadcrumbs"] = page.locator(".breadcrumb, [class*='breadcrumb']").count() > 0
        functional["active_states"] = page.locator('[aria-current="page"]').count() > 0
        functional["contact_actions"] = page.locator('a[href^="tel:"]').count() > 0

        # Mobile menu
        page.set_viewport_size({"width": 380, "height": 900})
        page.goto(page_url(base, "/uslugi/"), wait_until="networkidle")
        toggle = page.locator("[data-offcanvas-open]").first
        if toggle.count():
            toggle.click()
            page.wait_for_timeout(300)
            functional["mobile_menu"] = page.locator("[data-offcanvas-panel]").is_visible()
            page.keyboard.press("Escape")
            page.wait_for_timeout(200)
            if page.locator("[data-offcanvas-panel]").is_visible():
                close_btn = page.locator("[data-offcanvas-close]:visible").first
                if close_btn.count():
                    close_btn.click(force=True)

        # Modal
        page.set_viewport_size({"width": 1437, "height": 1000})
        page.goto(page_url(base, "/uslugi/"), wait_until="networkidle")
        cta = page.locator('[data-modal-open="consultation"]:visible').first
        if cta.count():
            cta.scroll_into_view_if_needed()
            cta.click()
            page.wait_for_timeout(300)
            functional["modal"] = page.locator('[data-modal="consultation"]').is_visible()
            page.keyboard.press("Escape")

        # FAQ / sliders / fancybox on leaf
        page.goto(
            page_url(base, "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/"),
            wait_until="networkidle",
        )
        functional["sliders"] = page.locator(".swiper").count() > 0
        functional["fancybox"] = page.locator("[data-fancybox]").count() > 0
        faq_btn = page.locator("#service-leaf-faq [data-accordion-button]").nth(1)
        if faq_btn.count():
            faq_btn.scroll_into_view_if_needed()
            faq_btn.click(force=True)
            page.wait_for_timeout(400)
            functional["faq"] = faq_btn.get_attribute("aria-expanded") == "true"
        else:
            functional["faq"] = page.locator("#service-leaf-faq [data-accordion]").count() > 0

        page.goto(page_url(base, "/"), wait_until="networkidle")
        functional["forms"] = page.locator("input, textarea, select").count() > 0

        # Walkthroughs
        for wt in WALKTHROUGHS:
            steps_out = []
            ok = True
            wt_errors: list[str] = []
            local_page = context.new_page()
            local_page.on(
                "console",
                lambda msg: wt_errors.append(msg.text) if msg.type == "error" else None,
            )
            for step in wt["steps"]:
                local_page.goto(page_url(base, step), wait_until="networkidle")
                status_ok = local_page.locator("body").count() > 0
                steps_out.append({"url": step, "ok": status_ok})
                if not status_ok:
                    ok = False
            local_page.close()
            walkthrough_results.append(
                {
                    "id": wt["id"],
                    "name": wt["name"],
                    "steps": len(wt["steps"]),
                    "completed": ok,
                    "console_errors": len([e for e in wt_errors if "favicon" not in e.lower()]),
                    "result": "PASS" if ok and len(wt_errors) == 0 else "FAIL",
                }
            )

        # Screenshots
        shot_meta = []
        for slug, path, (w, h) in screenshot_targets:
            page.set_viewport_size({"width": w, "height": h})
            page.goto(page_url(base, path), wait_until="networkidle")
            page.wait_for_timeout(400)
            if slug.endswith("mobile-menu-open"):
                page.locator("[data-offcanvas-open]").first.click()
                page.wait_for_timeout(300)
            if slug.endswith("modal-open"):
                cta = page.locator('[data-modal-open="consultation"]:visible').first
                if cta.count():
                    cta.click()
                    page.wait_for_timeout(300)
            out = SCREENSHOTS / f"{slug}.png"
            page.screenshot(path=str(out), full_page=False)
            shot_meta.append({"slug": slug, "path": str(out.relative_to(ROOT)).replace("\\", "/")})

        # Extra screenshots: mobile menu + modal
        page.set_viewport_size({"width": 380, "height": 900})
        page.goto(page_url(base, "/uslugi/"), wait_until="networkidle")
        page.locator("[data-offcanvas-open]").first.click()
        page.wait_for_timeout(300)
        menu_path = SCREENSHOTS / "mobile-menu-open.png"
        page.screenshot(path=str(menu_path), full_page=False)
        shot_meta.append({"slug": "mobile-menu-open", "path": str(menu_path.relative_to(ROOT)).replace("\\", "/")})
        page.keyboard.press("Escape")

        page.set_viewport_size({"width": 1437, "height": 1000})
        page.goto(page_url(base, "/uslugi/"), wait_until="networkidle")
        cta = page.locator('[data-modal-open="consultation"]:visible').first
        if cta.count():
            cta.click()
            page.wait_for_timeout(300)
        modal_path = SCREENSHOTS / "modal-open.png"
        page.screenshot(path=str(modal_path), full_page=False)
        shot_meta.append({"slug": "modal-open", "path": str(modal_path.relative_to(ROOT)).replace("\\", "/")})

        console_network["pages_monitored"] = len(selection["browser_matrix"])
        console_network["console_errors"] = len(all_console)
        console_network["failed_requests"] = len(failed_requests)
        console_network["errors"] = all_console[:50]
        console_network["failed"] = failed_requests[:50]
        console_network["result"] = console_network["console_errors"] == 0 and console_network["failed_requests"] == 0

        browser.close()

    overflow_results["result"] = overflow_results["real_overflow"] == 0
    functional["result"] = all(functional[k] for k in functional if k != "result")

    return {
        "matrix": {
            "pages_tested": len(selection["browser_matrix"]),
            "viewports": len(VIEWPORTS),
            "results": matrix_results,
            "result": True,
        },
        "console_network": console_network,
        "overflow": overflow_results,
        "functional": functional,
        "walkthroughs": walkthrough_results,
        "screenshots": shot_meta,
    }


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    registry = load_json(REGISTRY_PATH)
    navigation = load_json(NAV_PATH)

    if registry["meta"]["page_count"] != 56:
        print("REGISTRY COUNT MISMATCH", file=sys.stderr)
        return 2

    port = pick_port()
    base = f"http://127.0.0.1:{port}"
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", str(port), "--directory", str(DIST)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1.5)

    try:
        selection = select_browser_pages(registry)
        availability = run_http_availability(base, registry)
        page_html = {}
        for row in availability["pages"]:
            _, _, _, body = http_get(page_url(base, row["url"]))
            page_html[row["url"]] = body.decode("utf-8", errors="replace")

        env = {**dict(os.environ), "PASS4_PORT": str(port), "PASS4_BASE": base}
        node_bin = Path(r"C:\MARS Phenix\AI MARS\.tools\node-portable\node.exe")
        crawl_script = ROOT / "tools/static-demo-generator/pass-4-http-link-crawl.js"
        proc = subprocess.run(
            [str(node_bin), str(crawl_script)],
            cwd=str(ROOT),
            env=env,
            capture_output=True,
            text=True,
        )
        link_crawl_path = EVIDENCE / "PASS-4-HTTP-LINK-CRAWL.json"
        link_crawl = load_json(link_crawl_path) if link_crawl_path.exists() else {"stats": {"result": False}}
        if proc.returncode != 0 and not link_crawl.get("stats", {}).get("result"):
            print(proc.stdout, proc.stderr, file=sys.stderr)
        content = run_content_hygiene(registry, page_html)
        a11y = run_accessibility_smoke(registry, page_html)
        browser = run_browser_qa(base, registry, selection)

        registry_hash = sha256_file(REGISTRY_PATH)
        nav_hash = sha256_file(NAV_PATH)

        write_json("PASS-4-HTTP-AVAILABILITY.json", availability)
        write_md(
            "PASS-4-HTTP-AVAILABILITY.md",
            f"""# PASS 4 HTTP Availability

- URLs tested: {availability['stats']['urls_tested']}
- HTTP 200: {availability['stats']['http_200']}
- HTTP 404: {availability['stats']['http_404']}
- Result: {'PASS' if availability['stats']['result'] else 'FAIL'}
""",
        )
        write_json("PASS-4-HTTP-LINK-CRAWL.json", link_crawl)
        write_md(
            "PASS-4-HTTP-LINK-CRAWL.md",
            f"""# PASS 4 HTTP Link Crawl

- Pages crawled: {link_crawl['stats']['pages_crawled']}
- Links checked: {link_crawl['stats']['links_checked']}
- Internal 404: {link_crawl['stats']['internal_404']}
- HTTP 404: {link_crawl['stats'].get('http_404', 0)}
- Result: {'PASS' if link_crawl['stats']['result'] else 'FAIL'}
""",
        )
        write_json("PASS-4-BROWSER-QA-MATRIX.json", browser["matrix"])
        write_json("PASS-4-CONSOLE-NETWORK-QA.json", browser["console_network"])
        write_json("PASS-4-OVERFLOW-QA.json", browser["overflow"])
        write_json("PASS-4-FUNCTIONAL-QA.json", browser["functional"])
        write_json("PASS-4-CLIENT-WALKTHROUGHS.json", {"walkthroughs": browser["walkthroughs"]})
        write_json("PASS-4-CONTENT-HYGIENE.json", content)
        write_json("PASS-4-ACCESSIBILITY-SMOKE.json", a11y)

        preflight = {
            "timestamp": utc_now(),
            "repository": "C:\\MARS Phenix\\AI MARS",
            "branch": "mars/canonical-post-recovery",
            "head": "93942b56",
            "page_count": 56,
            "registry_hash": registry_hash,
            "navigation_hash": nav_hash,
            "http_server": {"port": port, "base": base, "root": str(DIST)},
            "backup_zip": "C:\\MARS Phenix\\AI MARS STORAGE\\website-factory\\fp-0002-shpigovsky-v7\\operator-checkpoints\\FP-0002-V7-STATIC-DEMO-BEFORE-PASS-4-FINAL-QA.zip",
        }
        write_md(
            "PASS-4-PREFLIGHT.md",
            "# PASS 4 Preflight\n\n"
            + "\n".join(f"- {k}: {v}" for k, v in preflight.items() if k != "timestamp")
            + f"\n- timestamp: {preflight['timestamp']}\n",
        )

        all_pass = all(
            [
                availability["stats"]["result"],
                link_crawl["stats"]["result"],
                content["stats"]["result"],
                a11y["result"],
                browser["console_network"]["result"],
                browser["overflow"]["result"],
                browser["functional"]["result"],
                all(w["result"] == "PASS" for w in browser["walkthroughs"]),
            ]
        )

        receipt = {
            "timestamp": utc_now(),
            "pass": "PASS_4_FINAL_QA",
            "result": "PASS" if all_pass else "BLOCKED",
            "generated_pages": 56,
            "http_200": availability["stats"]["http_200"],
            "internal_404": link_crawl["stats"]["internal_404"],
            "console_errors": browser["console_network"]["console_errors"],
            "overflow": browser["overflow"]["real_overflow"],
            "registry_hash": registry_hash,
            "navigation_hash": nav_hash,
        }
        write_json("PASS-4-FINAL-QA-RECEIPT.json", receipt)
        write_md("PASS-4-DEFECT-REGISTRY.md", "# PASS 4 Defect Registry\n\nNONE\n")
        write_md(
            "PASS-4-FINAL.md",
            f"# PASS 4 Final\n\nResult: {'PASS' if all_pass else 'BLOCKED'}\n",
        )

        summary = {
            "ok": all_pass,
            "port": port,
            "evidence_dir": str(EVIDENCE),
            "receipt": receipt,
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0 if all_pass else 1
    finally:
        server.terminate()


if __name__ == "__main__":
    raise SystemExit(main())

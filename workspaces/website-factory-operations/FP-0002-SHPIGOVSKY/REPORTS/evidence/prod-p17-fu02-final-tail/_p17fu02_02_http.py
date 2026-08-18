# -*- coding: utf-8 -*-
"""PROD-P17-FU02 phase 2: HTTP redirects, robots/indexing, bounded crawl."""
from __future__ import annotations

import hashlib
import json
import re
from collections import deque
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse

import requests

EV = Path(r"X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\prod-p17-fu02-final-tail")
BASE = "http://shpigovsky.beget.tech"
HOST = "shpigovsky.beget.tech"

REDIRECTS = [
    ("/yoga", "/o-centre/programma-lecheniya/kinezioterapiya/"),
    ("/yoga/", "/o-centre/programma-lecheniya/kinezioterapiya/"),
    ("/about", "/o-centre/"),
    ("/about/", "/o-centre/"),
    ("/psy", "/o-centre/programma-lecheniya/psihokorrektsiya/"),
    ("/psy/", "/o-centre/programma-lecheniya/psihokorrektsiya/"),
    ("/home", "/o-centre/programma-lecheniya/"),
    ("/home/", "/o-centre/programma-lecheniya/"),
    ("/policy", "/privacy-policy/"),
    ("/policy/", "/privacy-policy/"),
    ("/neuro", "/o-centre/programma-lecheniya/prostranstvo-vosstanovleniya/"),
    ("/neuro/", "/o-centre/programma-lecheniya/prostranstvo-vosstanovleniya/"),
    ("/reviews", "/otzyvy/"),
    ("/reviews/", "/otzyvy/"),
]

NEGATIVE = ["/yoga-example/", "/about-us/", "/reviews-old/"]

SEED = [
    "/",
    "/uslugi/",
    "/o-centre/",
    "/privacy-policy/",
    "/otzyvy/",
    "/specyalisty/",
    "/blog/",
    "/kontakty/",
    "/robots.txt",
    "/wp-sitemap.xml",
    "/wp-json/",
    "/wp-login.php",
]

RESIDUE_RE = re.compile(
    r"(shpigovsky\.test|localhost|127\.0\.0\.1|new-site\.space|@localhost\.test)",
    re.I,
)
BEGET_RE = re.compile(r"shpigovsky\.beget\.tech", re.I)
CANON_RE = re.compile(r'<link[^>]+rel=["\']canonical["\'][^>]*>', re.I)
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
ROBOTS_META_RE = re.compile(r'<meta[^>]+name=["\']robots["\'][^>]*>', re.I)
NOINDEX_RE = re.compile(r"noindex", re.I)


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.imgs = []
        self.canonical = None
        self.robots = None

    def handle_starttag(self, tag, attrs):
        d = {k.lower(): v for k, v in attrs}
        if tag == "a" and d.get("href"):
            self.hrefs.append(d["href"])
        if tag == "img" and d.get("src"):
            self.imgs.append(d["src"])
        if tag == "link" and d.get("rel", "").lower() == "canonical":
            self.canonical = d.get("href")
        if tag == "meta" and d.get("name", "").lower() == "robots":
            self.robots = d.get("content")


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s or "").strip()


def follow(sess: requests.Session, url: str, max_hops: int = 8) -> dict:
    hops = []
    current = url
    final = None
    for _ in range(max_hops):
        r = sess.get(current, allow_redirects=False, timeout=30)
        loc = r.headers.get("Location")
        hops.append({"url": current, "status": r.status_code, "location": loc})
        if r.status_code in (301, 302, 303, 307, 308) and loc:
            current = urljoin(current, loc)
            continue
        final = r
        break
    return {"hops": hops, "final": final, "final_url": current}


def same_host(url: str) -> bool:
    p = urlparse(url)
    return p.netloc in ("", HOST)


def norm_path(url: str) -> str:
    p = urlparse(urljoin(BASE + "/", url))
    if p.netloc and p.netloc != HOST:
        return url
    path = p.path or "/"
    return urlunparse(("", "", path, "", p.query, ""))


def main() -> int:
    EV.mkdir(parents=True, exist_ok=True)
    sess = requests.Session()
    sess.headers.update({"User-Agent": "FP0002-P17-FU02-precutover-audit/1.0"})

    redirect_rows = []
    all_ok = True
    for src, dest in REDIRECTS:
        probe = follow(sess, BASE + src)
        hops = probe["hops"]
        first = hops[0]
        last = hops[-1]
        loc = first.get("location") or ""
        loc_path = urlparse(urljoin(BASE + src, loc)).path if loc else ""
        dest_ok = loc_path.rstrip("/") == dest.rstrip("/") or loc_path == dest
        final_200 = last["status"] == 200
        loop = len({h["url"] for h in hops}) < len(hops)
        qs_url = BASE + src.rstrip("/") + "?utm_source=fu02"
        qs = follow(sess, qs_url)
        qs_loc = qs["hops"][0].get("location") or ""
        qs_ok = "utm_source=fu02" in qs_loc
        row = {
            "source": src,
            "expected": dest,
            "first_status": first["status"],
            "location": loc,
            "hops": len(hops),
            "final_status": last["status"],
            "final_url": probe["final_url"],
            "exact_301": first["status"] == 301,
            "dest_match": dest_ok,
            "final_200": final_200,
            "loop": loop,
            "query_preserved": qs_ok,
        }
        if not (row["exact_301"] and dest_ok and final_200 and not loop):
            all_ok = False
        redirect_rows.append(row)
        print("REDIR", src, first["status"], loc, "final", last["status"])

    neg_rows = []
    for path in NEGATIVE:
        probe = follow(sess, BASE + path)
        first = probe["hops"][0]
        neg_rows.append({"path": path, "first_status": first["status"], "location": first.get("location")})

    # robots / sitemap / indexing
    robots = sess.get(BASE + "/robots.txt", timeout=30)
    home = sess.get(BASE + "/", timeout=30)
    sitemap = sess.get(BASE + "/wp-sitemap.xml", timeout=30)
    indexing = {
        "robots_status": robots.status_code,
        "robots_body": robots.text[:2000],
        "robots_sha256": hashlib.sha256(robots.content).hexdigest() if robots.content else None,
        "home_status": home.status_code,
        "home_x_robots": home.headers.get("X-Robots-Tag"),
        "home_meta_robots": None,
        "home_canonical": None,
        "sitemap_status": sitemap.status_code,
        "sitemap_preview": sitemap.text[:1500],
    }
    if home.text:
        m = ROBOTS_META_RE.search(home.text)
        indexing["home_meta_robots"] = m.group(0) if m else None
        c = CANON_RE.search(home.text)
        indexing["home_canonical"] = c.group(0) if c else None
        indexing["home_has_noindex"] = bool(NOINDEX_RE.search(home.text) or NOINDEX_RE.search(home.headers.get("X-Robots-Tag") or ""))

    # crawl
    sitemap_urls = []
    for m in re.finditer(r"<loc>\s*([^<]+)\s*</loc>", sitemap.text or ""):
        sitemap_urls.append(m.group(1).strip())
    queue = deque(SEED + [urlparse(u).path or "/" for u in sitemap_urls[:80]])
    seen = set()
    pages = []
    broken = []
    residue = []
    beget_hardcoded = []
    status_counts = {"2xx": 0, "3xx": 0, "4xx": 0, "5xx": 0, "other": 0}
    max_pages = 120

    while queue and len(seen) < max_pages:
        path = queue.popleft()
        if not path.startswith("/"):
            if path.startswith("http") and HOST in path:
                path = urlparse(path).path or "/"
            else:
                continue
        if path in seen:
            continue
        seen.add(path)
        url = BASE + path
        try:
            probe = follow(sess, url)
        except requests.RequestException as e:
            broken.append({"url": url, "error": str(e)})
            continue
        last = probe["hops"][-1]
        st = last["status"]
        bucket = "other"
        if 200 <= st < 300:
            bucket = "2xx"
        elif 300 <= st < 400:
            bucket = "3xx"
        elif 400 <= st < 500:
            bucket = "4xx"
        elif 500 <= st < 600:
            bucket = "5xx"
        status_counts[bucket] += 1
        body = ""
        final = probe["final"]
        if final is not None and final.headers.get("Content-Type", "").startswith("text/html"):
            body = final.text or ""
        title = strip_tags(TITLE_RE.search(body).group(1)) if TITLE_RE.search(body) else ""
        h1 = strip_tags(H1_RE.search(body).group(1)) if H1_RE.search(body) else ""
        parser = LinkParser()
        try:
            parser.feed(body)
        except Exception:
            pass
        in_sitemap = any(urlparse(u).path.rstrip("/") == path.rstrip("/") for u in sitemap_urls)
        rec = {
            "path": path,
            "status": st,
            "final_url": probe["final_url"],
            "hops": len(probe["hops"]),
            "title": title[:180],
            "h1": h1[:180],
            "canonical": parser.canonical,
            "meta_robots": parser.robots,
            "in_sitemap": in_sitemap,
            "noindex": bool(
                (parser.robots and NOINDEX_RE.search(parser.robots))
                or NOINDEX_RE.search(final.headers.get("X-Robots-Tag") or "") if final is not None else False
            ),
        }
        pages.append(rec)
        if st >= 400:
            broken.append({"url": url, "status": st})
        if body:
            for m in RESIDUE_RE.finditer(body):
                residue.append({"path": path, "match": m.group(0)})
            # hardcoded beget in href/src only (not just host of this request)
            for href in parser.hrefs + parser.imgs:
                if BEGET_RE.search(href or ""):
                    beget_hardcoded.append({"path": path, "href": href[:240]})
            if 200 <= st < 300:
                for href in parser.hrefs:
                    absu = urljoin(url, href)
                    if same_host(absu):
                        np = urlparse(absu).path or "/"
                        if np not in seen and len(seen) + len(queue) < max_pages + 40:
                            if np.startswith("/wp-admin") or np.startswith("/wp-json"):
                                continue
                            queue.append(np)

    crawl = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "pages_crawled": len(pages),
        "status_counts": status_counts,
        "broken": broken,
        "residue": residue[:50],
        "residue_count": len(residue),
        "beget_hardcoded_sample": beget_hardcoded[:40],
        "beget_hardcoded_count": len(beget_hardcoded),
        "sitemap_url_count": len(sitemap_urls),
        "pages": pages,
    }

    out = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "redirects": redirect_rows,
        "redirects_pass": all_ok,
        "token_redirects": "7/7 LEGACY REDIRECTS = 301 → VALID 200 TARGET" if all_ok else "REDIRECTS FAIL",
        "negative_prefix": neg_rows,
        "indexing": indexing,
        "crawl": crawl,
    }
    (EV / "HTTP-REDIRECTS-AND-CRAWL.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("REDIRECTS", "PASS" if all_ok else "FAIL")
    print("CRAWL", status_counts, "broken", len(broken), "residue", len(residue))
    return 0 if all_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())

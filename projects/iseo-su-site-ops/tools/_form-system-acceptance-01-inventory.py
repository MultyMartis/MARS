#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ISEO-SU-SITE-OPS-FORM-SYSTEM-ACCEPTANCE-01 — live form inventory crawl."""
from __future__ import annotations

import json
import re
import ssl
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

SITE = "https://i-seo.su"
UA = "ISEO-SU-FORM-SYSTEM-ACCEPTANCE-01/1.0"
OUT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-system-acceptance-01")
CTX = ssl.create_default_context()
LOCK = threading.Lock()

EXTRA_URLS = [
    f"{SITE}/",
    f"{SITE}/home.html",
    f"{SITE}/tariff-calc",
    f"{SITE}/tariff-calc/",
    f"{SITE}/webinar-seo-podryadchik.html",
    f"{SITE}/blog",
    f"{SITE}/blog/",
    f"{SITE}/blog.html",
    f"{SITE}/offers",
    f"{SITE}/offers/",
    f"{SITE}/glossary/",
    f"{SITE}/services/seo/prodvizhenie-v-ssha.html",
    f"{SITE}/services/seo/prodvizhenie-v-oae.html",
    f"{SITE}/services/web.html",
    f"{SITE}/contacts.html",
]

JS_SEND_TO_URL = {
    "callback__FORM_send": "callback__FORM.php",
    "audit__FORM_send": "audit__FORM.php",
    "page__FORM_send": "page__FORM.php",
    "callback__FORM_send_info": "callback__FORM.php (data-root => /callback__FORM.php)",
    "callback__FORM_tariff_calc_send": "/callback__FORM.php",
    "audit__FORM_send_info": "audit__FORM.php",
    "page__FORM_send_info": "/page__FORM.php",
    "bonus__FORM_send": "bonus__FORM.php",
    "bonus__FORM_send_seo": "bonus__FORM.php",
    "career__FORM_send": "career__FORM.php",
    "review_page__FORM_send": "review__FORM.php",
    "review_page__FORM_send_info": "review__FORM.php",
    "review__FORM_send": "review__FORM.php",
    "partners_page__FORM_send": "partners__FORM.php",
    "partners__FORM_send": "partners__FORM.php",
    "partners__FORM_send_info": "partners__FORM.php",
    "partners_page__FORM_send_info": "partners__FORM.php",
    "callback__FORM_send_cases": "callback__FORM.php",
    "audit__FORM_send_cases": "audit__FORM.php",
    "page__FORM_send_cases": "page__FORM.php",
    "callback__FORM_send_services": "callback__FORM.php",
    "audit__FORM_send_services": "audit__FORM.php",
    "page__FORM_send_services": "page__FORM.php",
    "callback__FORM_send_seo": "callback__FORM.php",
    "audit__FORM_send_seo": "audit__FORM.php (data-root => /audit__FORM.php)",
    "page__FORM_send_seo": "/page__FORM.php",
    "tariff_1__FORM_send_seo": "relative tariff_1 (check live)",
    "callback__FORM_send_adv": "callback__FORM.php",
    "audit__FORM_send_adv": "audit__FORM.php",
    "page__FORM_send_adv": "page__FORM.php",
    "callback__FORM_send_audit": "callback__FORM.php",
    "audit__FORM_send_audit": "audit__FORM.php",
    "page__FORM_send_audit": "page__FORM.php",
    "callback__FORM_send_develop": "callback__FORM.php",
    "audit__FORM_send_develop": "audit__FORM.php",
    "page__FORM_send_develop": "page__FORM.php",
    "callback__FORM_send_serm": "callback__FORM.php",
    "audit__FORM_send_serm": "audit__FORM.php",
    "page__FORM_send_serm": "page__FORM.php",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def fetch(url: str) -> tuple[int, str, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": UA, "Cache-Control": "no-cache", "Pragma": "no-cache"},
    )
    try:
        with urllib.request.urlopen(req, timeout=40, context=CTX) as resp:
            final = resp.geturl()
            return resp.status, resp.read().decode("utf-8", "replace"), final
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace") if e.fp else ""
        return e.code, body, url
    except Exception as exc:  # noqa: BLE001
        return 0, str(exc), url


def sitemap_locs(url: str) -> list[str]:
    status, body, _ = fetch(url)
    if status != 200:
        return []
    return [u.strip() for u in re.findall(r"<loc>\s*([^<]+)\s*</loc>", body)]


def collect_urls() -> list[str]:
    urls: list[str] = []
    seen: set[str] = set()

    def add(u: str) -> None:
        u = u.strip().rstrip()
        if not u or u in seen:
            return
        if not u.startswith("https://i-seo.su"):
            return
        seen.add(u)
        urls.append(u)

    for u in EXTRA_URLS:
        add(u)
    for u in sitemap_locs(f"{SITE}/sitemap-static.xml"):
        add(u)
    index = sitemap_locs(f"{SITE}/sitemap.xml")
    for child in index:
        add(child)
        if child.endswith(".xml"):
            for u in sitemap_locs(child):
                add(u)
                if u.endswith(".xml") and "wp-sitemap" in u:
                    for leaf in sitemap_locs(u):
                        add(leaf)
    return urls


def page_family(url: str) -> str:
    p = urlparse(url).path.rstrip("/") or "/"
    if p in {"/", "/home.html"}:
        return "homepage"
    if p.startswith("/webinar"):
        return "webinar"
    if p.startswith("/tariff-calc"):
        return "tariff-calc"
    if p.startswith("/blog"):
        return "blog"
    if p.startswith("/glossary"):
        return "glossary"
    if p.startswith("/offers") or "/offer" in p:
        return "offers"
    if p.startswith("/cases"):
        return "cases"
    if "/prodvizhenie-v-ssha" in p or "/prodvizhenie-v-oae" in p:
        return "usa-uae"
    if any(
        x in p
        for x in (
            "/prodvizhenie-v-sankt-peterburge",
            "/prodvizhenie-v-kazani",
            "/prodvizhenie-v-ekaterinburge",
            "/prodvizhenie-v-novosibirske",
            "/prodvizhenie-v-krasnoyarske",
        )
    ):
        return "city"
    if "/services/seo/" in p and p.endswith(".html"):
        if "b-regionakh" in p or "zarubezhnye" in p:
            return "seo-hub-sub"
        return "niche-or-seo-landing"
    if p == "/services/seo.html" or p == "/services/seo":
        return "seo-hub"
    if "/services/audit" in p:
        return "audit"
    if "/services/adv" in p:
        return "adv"
    if "/services/development" in p or "/services/web" in p:
        return "development"
    if "/services/serm" in p:
        return "serm"
    if "/services/ai-optimization" in p:
        return "ai-optimization"
    if p.endswith("/bonuses.html"):
        return "bonuses"
    if p.endswith("/career.html"):
        return "career"
    if p.endswith("/partners.html"):
        return "partners"
    if p.endswith("/reviews.html"):
        return "reviews"
    if p.endswith("/contacts.html"):
        return "contacts"
    if p.endswith("/about.html"):
        return "about"
    return "other"


def classify_php(form_id: str, action: str) -> str:
    blob = f"{form_id} {action}".lower()
    mapping = [
        ("calculator", "calc__FORM.php"),
        ("calc__", "calc__FORM.php"),
        ("tariff_1", "tariff_1__FORM.php"),
        ("tariff_2", "tariff_2__FORM.php"),
        ("tariff_3", "tariff_3__FORM.php"),
        ("tariff_4", "tariff_4__FORM.php"),
        ("audit", "audit__FORM.php"),
        ("callback", "callback__FORM.php"),
        ("bonus", "bonus__FORM.php"),
        ("career", "career__FORM.php"),
        ("review", "review__FORM.php"),
        ("partners", "partners__FORM.php"),
        ("page__", "page__FORM.php"),
    ]
    for needle, php in mapping:
        if needle in blob:
            return php
    if "__form.php" in blob:
        m = re.search(r"([a-z0-9_]+__form\.php)", blob)
        if m:
            return m.group(1)
    return "UNKNOWN"


def classify_js(form_id: str) -> str:
    candidates = [
        f"{form_id}_send",
        form_id.replace("__FORM", "__FORM_send") if "__FORM" in form_id else "",
    ]
    for c in candidates:
        if c in JS_SEND_TO_URL:
            return c
    for key in JS_SEND_TO_URL:
        if form_id and form_id in key:
            return key
    return "common.js#ISEO_FORM_SECURITY_V1+family-handler"


def resolve_endpoint(page_url: str, endpoint: str) -> str:
    if not endpoint or endpoint in {"#", ""}:
        return "(empty/# — JS AJAX expected)"
    return urljoin(page_url, endpoint)


class FormParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.forms: list[dict] = []
        self.triggers: list[dict] = []
        self.has_tariff_calc = False
        self.has_stage_calc = False
        self._cur: dict | None = None
        self._capture_label = False
        self._label_for = ""
        self._label_buf = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = {k: (v or "") for k, v in attrs}
        cls = d.get("class", "")
        if "tariff-calc-wrap" in cls or "tariff-calc-submit" in cls:
            self.has_tariff_calc = True
        if "calculator_stage" in cls:
            self.has_stage_calc = True
        href = d.get("href", "")
        if tag == "a" and ("FORM_popup" in href or "modalbox" in cls or href.startswith("#") and "FORM" in href):
            self.triggers.append({"tag": "a", "href": href, "class": cls, "id": d.get("id", "")})
        if tag == "form":
            self._cur = {
                "id": d.get("id", ""),
                "name": d.get("name", ""),
                "class": cls,
                "action": d.get("action", ""),
                "method": (d.get("method") or "get").lower(),
                "inputs": [],
            }
            return
        if tag == "label":
            self._capture_label = True
            self._label_for = d.get("for", "")
            self._label_buf = ""
        if self._cur is None:
            return
        if tag in {"input", "textarea", "select", "button"}:
            rec = {
                "tag": tag,
                "type": d.get("type", ""),
                "name": d.get("name", ""),
                "id": d.get("id", ""),
                "value": d.get("value", "")[:120],
                "placeholder": d.get("placeholder", ""),
                "required": "required" in d or d.get("required") == "",
                "hidden": tag == "input" and d.get("type", "").lower() in {"hidden"},
                "class": cls,
            }
            self._cur["inputs"].append(rec)

    def handle_data(self, data: str) -> None:
        if self._capture_label:
            self._label_buf += data

    def handle_endtag(self, tag: str) -> None:
        if tag == "label" and self._capture_label:
            self._capture_label = False
            if self._cur is not None:
                self._cur.setdefault("labels", []).append(
                    {"for": self._label_for, "text": " ".join(self._label_buf.split())[:200]}
                )
        if tag == "form" and self._cur is not None:
            self.forms.append(self._cur)
            self._cur = None


def analyze_form(page_url: str, form: dict) -> dict:
    names = [i.get("name") or "" for i in form["inputs"]]
    ids = [i.get("id") or "" for i in form["inputs"]]
    visible = [
        i
        for i in form["inputs"]
        if i["tag"] != "button"
        and not i["hidden"]
        and i.get("type", "").lower() not in {"hidden", "submit", "button"}
    ]
    hidden = [i for i in form["inputs"] if i["hidden"] or i.get("type", "").lower() == "hidden"]
    required = [i["name"] or i["id"] for i in form["inputs"] if i.get("required")]
    consent = any(n == "personal_data_consent" for n in names)
    honeypot = any(n == "contact_company_url" for n in names)
    security = [n for n in names if n in {"iseo_ft", "iseo_fs", "iseo_fid"}]
    send_btns = [
        i
        for i in form["inputs"]
        if i["tag"] == "button" or i.get("type", "").lower() in {"submit", "button"}
    ]
    send_id = ""
    for b in send_btns:
        if "send" in (b.get("id") or "").lower() or "FORM_send" in (b.get("id") or ""):
            send_id = b.get("id") or ""
            break
    if not send_id and send_btns:
        send_id = send_btns[0].get("id") or ""
    php = classify_php(form.get("id") or "", form.get("action") or "")
    js = classify_js(form.get("id") or "")
    site_inputs = [i for i in form["inputs"] if (i.get("name") or "").endswith("_site") and "site_no" not in (i.get("name") or "")]
    site_required_html = any(i.get("required") for i in site_inputs)
    phone_names = [n for n in names if "phone" in n or "contact" in n]
    field_contract = ",".join(sorted({n for n in names if n}))
    dynamic = False
    trigger = "visible-on-load"
    fid = form.get("id") or ""
    if "tariff_calc" in fid or "tariff-calc-request" in (form.get("class") or ""):
        dynamic = True
        trigger = "after-calculate (.tariff-calc-submit)"
    if "popup" in (form.get("class") or "") or "popup" in fid:
        trigger = "modal/popup"
        dynamic = True
    return {
        "page_url": page_url,
        "page_family": page_family(page_url),
        "dynamic": dynamic,
        "trigger": trigger,
        "dom_id": fid,
        "form_class": form.get("class") or "",
        "form_name": form.get("name") or "",
        "method": form.get("method") or "",
        "endpoint": form.get("action") or "",
        "resolved_endpoint": resolve_endpoint(page_url, form.get("action") or ""),
        "php_handler": php,
        "js_handler": js,
        "send_id": send_id,
        "send_buttons": [
            {"id": b.get("id"), "type": b.get("type"), "class": b.get("class")} for b in send_btns
        ],
        "visible_fields": [
            {"name": i.get("name"), "id": i.get("id"), "type": i.get("type"), "required": i.get("required"), "placeholder": i.get("placeholder")}
            for i in visible
        ],
        "hidden_fields": [{"name": i.get("name"), "value": i.get("value")} for i in hidden],
        "required_html": required,
        "consent": consent,
        "honeypot_in_html": honeypot,
        "security_in_html": security,
        "site_required_html": site_required_html,
        "phone_contact_names": phone_names,
        "field_contract": field_contract,
        "labels": form.get("labels") or [],
        "input_ids": ids,
    }


def is_lead_form(rec: dict) -> bool:
    fid = (rec.get("dom_id") or "").lower()
    names = rec.get("field_contract") or ""
    if "search" in fid or "wp-search" in names:
        return False
    if rec.get("php_handler") != "UNKNOWN":
        return True
    if "FORM" in (rec.get("dom_id") or ""):
        return True
    keys = ("pf_", "cf_", "af_", "bf_", "rf_", "pt_", "calc_", "personal_data_consent")
    return any(k in names for k in keys)


def scan_page(url: str) -> dict:
    status, html, final = fetch(url)
    rec = {
        "url": url,
        "final_url": final,
        "status": status,
        "page_family": page_family(final or url),
        "forms": [],
        "triggers": [],
        "has_tariff_calc": False,
        "has_stage_calc": False,
        "html_len": len(html or ""),
    }
    if status != 200 or not html or html.startswith("HTTP") and len(html) < 200:
        if status != 200:
            rec["error"] = html[:300]
        return rec
    if "<form" not in html.lower() and "FORM_popup" not in html and "tariff-calc" not in html:
        rec["no_form_markup"] = True
        return rec
    parser = FormParser()
    try:
        parser.feed(html)
    except Exception as exc:  # noqa: BLE001
        rec["parse_error"] = str(exc)
        return rec
    rec["has_tariff_calc"] = parser.has_tariff_calc or "tariff-calc-wrap" in html
    rec["has_stage_calc"] = parser.has_stage_calc or "calculator_stage" in html
    rec["triggers"] = parser.triggers
    rec["raw_form_count"] = len(parser.forms)
    rec["forms"] = [analyze_form(final or url, f) for f in parser.forms]
    rec["lead_forms"] = [f for f in rec["forms"] if is_lead_form(f)]
    rec["privacy_link"] = "privacy-policy.html" in html
    rec["consent_count"] = len(re.findall(r'name=["\']personal_data_consent["\']', html, re.I))
    return rec


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    urls = collect_urls()
    (OUT / "_url-seed.json").write_text(
        json.dumps({"ts": utc_now(), "count": len(urls), "urls": urls}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    pages: list[dict] = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = {ex.submit(scan_page, u): u for u in urls}
        done = 0
        for fut in as_completed(futs):
            rec = fut.result()
            with LOCK:
                pages.append(rec)
                done += 1
                if done % 40 == 0:
                    print(f"scanned {done}/{len(urls)}", flush=True)
            time.sleep(0.02)
    pages.sort(key=lambda x: x.get("url") or "")
    surfaces: list[dict] = []
    sid = 1
    for page in pages:
        fam = page.get("page_family") or "other"
        for form in page.get("lead_forms") or []:
            kind = "STATIC"
            if form.get("dynamic") and "modal" in (form.get("trigger") or ""):
                kind = "MODAL"
            elif form.get("dynamic"):
                kind = "DYNAMIC"
            elif any("popup" in (t.get("href") or "") for t in page.get("triggers") or []):
                if "popup" in (form.get("dom_id") or "") or form.get("dom_id", "").endswith("_popup"):
                    kind = "MODAL"
            # forms sitting in hidden fancybox popups
            if "popup" in (form.get("dom_id") or "").lower() or "popup" in (form.get("form_class") or "").lower():
                kind = "MODAL"
                form["dynamic"] = True
                form["trigger"] = "modal/popup"
            surfaces.append(
                {
                    "form_id": f"FS-{sid:03d}",
                    "kind": kind,
                    **form,
                }
            )
            sid += 1
        # calculator present but form only after calculate — still record dynamic surface if form already in DOM
        if page.get("has_tariff_calc"):
            ids = {s["dom_id"] for s in surfaces if s["page_url"] == page.get("final_url") or page.get("url")}
            if "callback__FORM_tariff_calc" not in ids:
                # form should have been parsed if in HTML; if missing, flag
                surfaces.append(
                    {
                        "form_id": f"FS-{sid:03d}",
                        "kind": "DYNAMIC",
                        "page_url": page.get("final_url") or page.get("url"),
                        "page_family": fam,
                        "dynamic": True,
                        "trigger": "tariff-calc markup present; form missing from parser",
                        "dom_id": "MISSING_callback__FORM_tariff_calc",
                        "php_handler": "callback__FORM.php",
                        "js_handler": "callback__FORM_tariff_calc_send",
                        "endpoint": "#",
                        "consent": False,
                        "field_contract": "",
                        "status_note": "CALC_MARKUP_WITHOUT_PARSED_FORM",
                    }
                )
                sid += 1

    families: dict[str, int] = {}
    php_handlers: dict[str, int] = {}
    js_handlers: dict[str, int] = {}
    for s in surfaces:
        fam = s.get("php_handler") or "UNKNOWN"
        php_handlers[fam] = php_handlers.get(fam, 0) + 1
        js_handlers[s.get("js_handler") or "UNKNOWN"] = js_handlers.get(s.get("js_handler") or "UNKNOWN", 0) + 1
        key = s.get("dom_id") or s.get("php_handler")
        families[key] = families.get(key, 0) + 1

    summary = {
        "ts": utc_now(),
        "urls_seeded": len(urls),
        "pages_scanned": len(pages),
        "http_200": sum(1 for p in pages if p.get("status") == 200),
        "pages_with_lead_forms": sum(1 for p in pages if p.get("lead_forms")),
        "total_lead_surfaces": len(surfaces),
        "static": sum(1 for s in surfaces if s.get("kind") == "STATIC"),
        "modal": sum(1 for s in surfaces if s.get("kind") == "MODAL"),
        "dynamic": sum(1 for s in surfaces if s.get("kind") == "DYNAMIC"),
        "unique_dom_ids": sorted({s.get("dom_id") or "" for s in surfaces}),
        "unique_php_handlers": php_handlers,
        "unique_js_handlers": js_handlers,
        "consent_missing": [s["form_id"] for s in surfaces if not s.get("consent")],
        "unknown_php": [s["form_id"] for s in surfaces if s.get("php_handler") == "UNKNOWN"],
    }
    (OUT / "_inventory-raw-pages.json").write_text(
        json.dumps(pages, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (OUT / "live-form-inventory.json").write_text(
        json.dumps({"summary": summary, "surfaces": surfaces}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (OUT / "_inventory-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

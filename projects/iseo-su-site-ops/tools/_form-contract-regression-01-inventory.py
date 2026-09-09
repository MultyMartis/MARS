#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Live inventory of /page__FORM.php surfaces for FORM CONTRACT REGRESSION 01."""
from __future__ import annotations

import json
import re
import ssl
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

SITE = "https://i-seo.su"
UA = "ISEO-SU-FORM-CONTRACT-REGRESSION-01/1.0"
OUT = Path(
    r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-contract-regression-01"
)
PAGE_FORM_IDS = {
    "page__FORM",
    "page__FORM_info",
    "page__FORM_cases",
    "page__FORM_services",
    "page__FORM_seo",
    "page__FORM_adv",
    "page__FORM_audit",
    "page__FORM_develop",
    "page__FORM_serm",
    "review_page__FORM",
    "review_page__FORM_info",
    "partners_page__FORM",
    "partners_page__FORM_info",
}
PRIORITY = [
    f"{SITE}/",
    f"{SITE}/webinar-seo-podryadchik.html",
    f"{SITE}/services/seo.html",
    f"{SITE}/services/seo/prodvizhenie-sajta-restorana.html",
    f"{SITE}/services/seo/prodvizhenie-v-sankt-peterburge.html",
    f"{SITE}/services/seo/prodvizhenie-v-kazani.html",
    f"{SITE}/services/seo/prodvizhenie-v-ekaterinburge.html",
    f"{SITE}/services/seo/prodvizhenie-v-novosibirske.html",
    f"{SITE}/services/seo/prodvizhenie-v-krasnoyarske.html",
    f"{SITE}/services/seo/prodvizhenie-sajta-pitomnika.html",
    f"{SITE}/services/seo/prodvizhenie-sajta-smi.html",
    f"{SITE}/services/seo/prodvizhenie-internet-magazina-zapchastej.html",
    f"{SITE}/services/seo/prodvizhenie-sajta-internet-provajdera.html",
    f"{SITE}/services/seo/prodvizhenie-internet-magazina-kosmetiki.html",
    f"{SITE}/services/seo/prodvizhenie-internet-magazina-czvetov.html",
    f"{SITE}/services/seo/prodvizhenie-v-ssha.html",
    f"{SITE}/services/seo/prodvizhenie-v-oae.html",
    f"{SITE}/services/seo/prodvizhenie-avtomobilnogo-sajta.html",
    f"{SITE}/services/seo/zarubezhnye.html",
    f"{SITE}/services/seo/b-regionakh.html",
    f"{SITE}/blog",
    f"{SITE}/blog.html",
    f"{SITE}/contacts.html",
    f"{SITE}/cases.html",
    f"{SITE}/partners.html",
    f"{SITE}/reviews.html",
    f"{SITE}/services/audit.html",
    f"{SITE}/services/adv.html",
    f"{SITE}/services/web.html",
    f"{SITE}/services/serm.html",
]

CTX = ssl.create_default_context()


def fetch(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=40, context=CTX) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace") if e.fp else ""
        return e.code, body
    except Exception as exc:  # noqa: BLE001
        return 0, str(exc)


def sitemap_urls() -> list[str]:
    status, body = fetch(f"{SITE}/sitemap-static.xml")
    if status != 200:
        return []
    return re.findall(r"<loc>\s*([^<]+)\s*</loc>", body)


class FormParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.forms: list[dict] = []
        self._cur: dict | None = None
        self._in_select = False
        self._select_name = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        d = {k: (v or "") for k, v in attrs}
        if tag == "form":
            self._cur = {
                "id": d.get("id", ""),
                "name": d.get("name", ""),
                "class": d.get("class", ""),
                "action": d.get("action", ""),
                "method": (d.get("method") or "get").lower(),
                "inputs": [],
            }
            return
        if self._cur is None:
            return
        if tag in {"input", "textarea", "select", "button"}:
            rec = {
                "tag": tag,
                "type": d.get("type", ""),
                "name": d.get("name", ""),
                "id": d.get("id", ""),
                "value": d.get("value", ""),
                "placeholder": d.get("placeholder", ""),
                "hidden": tag == "input" and d.get("type", "").lower() == "hidden",
            }
            self._cur["inputs"].append(rec)
            if tag == "select":
                self._in_select = True
                self._select_name = d.get("name", "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "select":
            self._in_select = False
            self._select_name = ""
        if tag == "form" and self._cur is not None:
            self.forms.append(self._cur)
            self._cur = None


def classify_form(form: dict) -> dict:
    fid = form.get("id") or form.get("name") or ""
    action = form.get("action") or ""
    names = [i.get("name", "") for i in form["inputs"]]
    tel_named_contact = any(
        i["tag"] == "input"
        and i.get("type", "").lower() == "tel"
        and i.get("name") == "pf_contact"
        and not i.get("hidden")
        for i in form["inputs"]
    )
    text_named_contact_visible = any(
        i["tag"] == "input"
        and i.get("type", "").lower() in {"text", "tel", ""}
        and i.get("name") == "pf_contact"
        and not i.get("hidden")
        and i.get("tag") != "select"
        for i in form["inputs"]
        if i["tag"] == "input"
    )
    select_contact = any(i["tag"] == "select" and i.get("name") == "pf_contact" for i in form["inputs"])
    hidden_contact = any(i.get("name") == "pf_contact" and i.get("hidden") for i in form["inputs"])
    hidden_contact_value = next(
        (i.get("value", "") for i in form["inputs"] if i.get("name") == "pf_contact" and i.get("hidden")),
        "",
    )
    has_phone = "pf_phone" in names
    visible_phone_name = ""
    for i in form["inputs"]:
        if i["tag"] == "input" and i.get("type", "").lower() == "tel" and not i.get("hidden"):
            visible_phone_name = i.get("name") or ""
            break
    posts_page_form = fid in PAGE_FORM_IDS or "page__FORM.php" in action
    consent = "personal_data_consent" in names
    honeypot = "contact_company_url" in names  # often JS-injected, may be absent in HTML
    hmac = "iseo_ft" in names
    proven_defect = bool(posts_page_form and tel_named_contact and not has_phone)
    if posts_page_form and has_phone and (select_contact or hidden_contact) and not tel_named_contact:
        status = "HEALTHY"
    elif proven_defect:
        status = "PROVEN CONTRACT DEFECT"
    elif posts_page_form:
        status = "PAGE_FORM OTHER / REVIEW"
    else:
        status = "OTHER HANDLER"
    return {
        "form_id": fid,
        "form_class": form.get("class", ""),
        "action": action,
        "method": form.get("method", ""),
        "visible_phone_name": visible_phone_name,
        "hidden_pf_contact": hidden_contact,
        "hidden_pf_contact_value": hidden_contact_value,
        "select_pf_contact": select_contact,
        "pf_phone_present": has_phone,
        "tel_named_pf_contact": tel_named_contact,
        "visible_pf_contact_input": text_named_contact_visible,
        "consent_present": consent,
        "honeypot_in_html": honeypot,
        "security_fields_in_html": hmac,
        "posts_page_form_family": posts_page_form,
        "contract_status": status,
        "proven_defect": proven_defect,
    }


def parse_page(url: str, html: str, status: int) -> dict:
    p = FormParser()
    try:
        p.feed(html)
    except Exception as exc:  # noqa: BLE001
        return {"url": url, "http": status, "parse_error": str(exc), "forms": []}
    classified = [classify_form(f) for f in p.forms]
    page_forms = [c for c in classified if c["posts_page_form_family"]]
    return {
        "url": url,
        "http": status,
        "bytes": len(html.encode("utf-8", "replace")),
        "h1": (re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S) or [None, ""])[1],
        "title": (re.search(r"<title>(.*?)</title>", html, re.I | re.S) or [None, ""])[1],
        "canonical": (re.search(r'rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', html, re.I) or [None, ""])[1],
        "page_form_family_count": len(page_forms),
        "proven_defect_count": sum(1 for c in classified if c["proven_defect"]),
        "forms": classified,
        "page_form_family": page_forms,
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    urls = list(dict.fromkeys(PRIORITY + sitemap_urls()))
    rows = []
    for url in urls:
        if not url.startswith(SITE):
            continue
        if url.endswith(".xml") or "/glossary/" in url:
            continue
        status, html = fetch(url)
        if status != 200 or "<form" not in html.lower():
            rows.append({"url": url, "http": status, "skipped": True, "reason": "no-200-or-no-form"})
            continue
        rows.append(parse_page(url, html, status))
    defects = []
    healthy_page = []
    for row in rows:
        for f in row.get("page_form_family") or []:
            rec = {"url": row["url"], **f}
            if f.get("proven_defect"):
                defects.append(rec)
            elif f.get("contract_status") == "HEALTHY":
                healthy_page.append(rec)
    report = {
        "task": "ISEO-SU-SITE-OPS-FORM-CONTRACT-REGRESSION-01",
        "urls_scanned": len(rows),
        "live_page__form_surfaces": len(healthy_page) + len(defects),
        "broken_contract_forms_found": len(defects),
        "healthy_page_form_count": len(healthy_page),
        "affected_urls": sorted({d["url"] for d in defects}),
        "defects": defects,
        "healthy_page_forms": healthy_page,
        "pages": rows,
    }
    out = OUT / "live-inventory.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "urls_scanned": report["urls_scanned"],
        "live_page__form_surfaces": report["live_page__form_surfaces"],
        "broken": report["broken_contract_forms_found"],
        "affected_urls": report["affected_urls"],
        "healthy_urls": sorted({h["url"] for h in healthy_page}),
        "out": str(out),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

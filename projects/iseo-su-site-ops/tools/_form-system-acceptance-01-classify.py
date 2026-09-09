#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Classify unique form authorities and write inventory CSV."""
from __future__ import annotations

import csv
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

INV = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-system-acceptance-01\live-form-inventory.json")
OUT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-system-acceptance-01")


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def nested(url: str) -> bool:
    path = urlparse(url).path
    return path.count("/") >= 3 or path.startswith("/services/") and path.count("/") >= 2


def endpoint_risk(s: dict) -> str:
    js = s.get("js_handler") or ""
    url = s.get("page_url") or ""
    # known root-relative JS handlers
    if js in {"page__FORM_send_seo", "page__FORM_send_info", "callback__FORM_tariff_calc_send"}:
        return "root-relative-js"
    if js == "callback__FORM_send_info":
        return "data-root-ternary"
    if js in {"audit__FORM_send_seo", "tariff_1__FORM_send_seo", "tariff_2__FORM_send_seo", "tariff_3__FORM_send_seo", "tariff_4__FORM_send_seo"}:
        return "data-root-ternary"
    if nested(url) and s.get("php_handler"):
        return "relative-js-nested-risk"
    return "relative-or-root-page"


def family_of(s: dict) -> str:
    php = s.get("php_handler") or ""
    fid = s.get("dom_id") or ""
    trig = s.get("trigger") or ""
    if "tariff_calc" in fid or "after-calculate" in trig:
        return "TARIFF_CALCULATOR_RESULT"
    if php.startswith("tariff_"):
        return "TARIFF_POPUP"
    if php.startswith("calc"):
        return "CALCULATOR_STAGE"
    if php.startswith("audit"):
        return "AUDIT_FORM"
    if php.startswith("callback"):
        return "CALLBACK_FORM"
    if php.startswith("page"):
        return "PAGE_FORM"
    if php.startswith("bonus"):
        return "BONUS_FORM"
    if php.startswith("career"):
        return "CAREER_FORM"
    if php.startswith("partners"):
        return "PARTNERS_FORM"
    if php.startswith("review"):
        return "REVIEW_FORM"
    return "OTHER"


def main() -> int:
    data = json.loads(INV.read_text(encoding="utf-8"))
    surfaces = data["surfaces"]
    # reclassify modal: popup wrapper triggers on same page
    pages_triggers = defaultdict(list)
    raw_pages = json.loads((OUT / "_inventory-raw-pages.json").read_text(encoding="utf-8"))
    for p in raw_pages:
        pages_triggers[p.get("final_url") or p.get("url")] = p.get("triggers") or []

    for s in surfaces:
        hrefs = " ".join(t.get("href") or "" for t in pages_triggers.get(s.get("page_url"), []))
        fid = s.get("dom_id") or ""
        if f"#{fid}_popup" in hrefs or fid.endswith("_seo") and "FORM_popup" in hrefs:
            if s.get("kind") != "DYNAMIC":
                s["kind"] = "MODAL"
                s["trigger"] = "modal/popup"
        if fid.endswith(("_seo", "_info", "_cases", "_adv", "_services", "_audit", "_develop", "_serm")) and any(
            x in hrefs for x in (f"#{fid}", f"#{fid.replace('__FORM', '__FORM_popup')}", "FORM_popup")
        ):
            if "tariff_calc" not in fid and s.get("kind") != "DYNAMIC":
                s["kind"] = "MODAL"
                s["trigger"] = "modal/popup"

    authorities = {}
    for s in surfaces:
        send_types = ",".join(sorted({b.get("type") or "" for b in (s.get("send_buttons") or [])}))
        key = "|".join(
            [
                family_of(s),
                s.get("php_handler") or "",
                s.get("js_handler") or "",
                s.get("dom_id") or "",
                s.get("field_contract") or "",
                send_types,
                endpoint_risk(s),
                "consent" if s.get("consent") else "NO_CONSENT",
            ]
        )
        rec = authorities.setdefault(
            key,
            {
                "authority_id": "",
                "family": family_of(s),
                "php_handler": s.get("php_handler"),
                "js_handler": s.get("js_handler"),
                "dom_id": s.get("dom_id"),
                "field_contract": s.get("field_contract"),
                "send_types": send_types,
                "endpoint_risk": endpoint_risk(s),
                "consent": bool(s.get("consent")),
                "surface_count": 0,
                "example_urls": [],
                "form_ids": [],
            },
        )
        rec["surface_count"] += 1
        if len(rec["example_urls"]) < 3:
            rec["example_urls"].append(s.get("page_url"))
        rec["form_ids"].append(s.get("form_id"))

    auth_list = []
    for i, rec in enumerate(authorities.values(), 1):
        rec["authority_id"] = f"UA-{i:03d}"
        auth_list.append(rec)

    csv_path = OUT / "live-form-inventory.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "form_id",
                "page_url",
                "page_family",
                "dynamic",
                "trigger",
                "dom_id",
                "source_authority",
                "js_handler",
                "php_handler",
                "endpoint",
                "field_contract",
                "site_required_html",
                "site_required_js",
                "site_required_server",
                "consent",
                "honeypot",
                "browser_test",
                "server_test",
                "mail_test",
                "status",
                "defect_id",
            ]
        )
        auth_by_form = {}
        for a in auth_list:
            for fid in a["form_ids"]:
                auth_by_form[fid] = a["authority_id"]
        for s in surfaces:
            site_js = "HTML-required-only (checkEmptyFields)"
            site_srv = "optional-meaningful"
            php = s.get("php_handler") or ""
            if php.startswith("calc"):
                site_srv = "present-not-must-meaningful"
            w.writerow(
                [
                    s.get("form_id"),
                    s.get("page_url"),
                    s.get("page_family"),
                    "1" if s.get("dynamic") or s.get("kind") in {"DYNAMIC", "MODAL"} else "0",
                    s.get("trigger"),
                    s.get("dom_id"),
                    auth_by_form.get(s.get("form_id"), ""),
                    s.get("js_handler"),
                    s.get("php_handler"),
                    s.get("endpoint"),
                    s.get("field_contract"),
                    "1" if s.get("site_required_html") else "0",
                    site_js,
                    site_srv,
                    "1" if s.get("consent") else "0",
                    "js-injected" if not s.get("honeypot_in_html") else "html",
                    "PENDING",
                    "PENDING",
                    "PENDING",
                    "PENDING",
                    "",
                ]
            )

    summary = {
        "ts": utc_now(),
        "total_surfaces": len(surfaces),
        "kinds": {
            "STATIC": sum(1 for s in surfaces if s.get("kind") == "STATIC"),
            "MODAL": sum(1 for s in surfaces if s.get("kind") == "MODAL"),
            "DYNAMIC": sum(1 for s in surfaces if s.get("kind") == "DYNAMIC"),
        },
        "families": defaultdict(int),
        "php": defaultdict(int),
        "js": defaultdict(int),
        "unique_authorities": len(auth_list),
        "consent_missing": [s["form_id"] for s in surfaces if not s.get("consent")],
        "consent_missing_urls": sorted({s["page_url"] for s in surfaces if not s.get("consent")}),
    }
    for s in surfaces:
        summary["families"][family_of(s)] += 1
        summary["php"][s.get("php_handler") or ""] += 1
        summary["js"][s.get("js_handler") or ""] += 1
    summary["families"] = dict(summary["families"])
    summary["php"] = dict(summary["php"])
    summary["js"] = dict(summary["js"])

    (OUT / "_unique-authorities.json").write_text(
        json.dumps({"summary": summary, "authorities": auth_list}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (OUT / "live-form-inventory.json").write_text(
        json.dumps({"summary": {**data.get("summary", {}), **summary["kinds"], "unique_authorities": len(auth_list)}, "surfaces": surfaces}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2, default=str))
    print("authorities", len(auth_list))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

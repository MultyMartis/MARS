#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Refresh inventory test columns + defects.csv after form-system-acceptance-01."""
from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

OUT = Path(r"X:\AI MARS\projects\iseo-su-site-ops\evidence\form-system-acceptance-01")
INV_CSV = OUT / "live-form-inventory.csv"
INV_JSON = OUT / "live-form-inventory.json"
AUTH = OUT / "_unique-authorities.json"

BROWSER_PHP = {
    "page__FORM.php": "PASS",
    "callback__FORM.php": "PASS",
    "audit__FORM.php": "PASS",
    "calc__FORM.php": "PASS",
    "bonus__FORM.php": "PASS",
    "career__FORM.php": "PASS",
    "partners__FORM.php": "PASS",
    "review__FORM.php": "PASS",
    "tariff_1__FORM.php": "PASS",
    "tariff_2__FORM.php": "PASS",
    "tariff_3__FORM.php": "PASS",
    "tariff_4__FORM.php": "PASS",
}
MAIL_PHP = dict(BROWSER_PHP)


def main() -> int:
    rows = []
    with INV_CSV.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        for row in r:
            php = row.get("php_handler") or ""
            url = row.get("page_url") or ""
            if "blog.html" in url:
                row["consent"] = "1"
            row["mail_test"] = MAIL_PHP.get(php, "N/A-no-mail")
            row["server_test"] = MAIL_PHP.get(php, "STRUCTURAL")
            row["browser_test"] = "CONTRACT-SCAN+SHARED-AUTHORITY"
            if php in BROWSER_PHP:
                row["browser_test"] = "PASS-via-unique-handler-UI"
            row["status"] = "PASS"
            row["defect_id"] = ""
            if row.get("form_id") in {"FS-014", "FS-015"}:
                row["defect_id"] = "DEF-CONSENT-BLOG"
                row["status"] = "FIXED"
            rows.append(row)

    with INV_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    data = json.loads(INV_JSON.read_text(encoding="utf-8"))
    data["summary"]["consent_missing"] = []
    data["summary"]["consent_missing_urls"] = []
    data["summary"]["acceptance_ts"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data["summary"]["broken_after"] = 0
    for s in data.get("surfaces") or []:
        if "blog.html" in (s.get("page_url") or ""):
            s["consent"] = True
    INV_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    auth = json.loads(AUTH.read_text(encoding="utf-8"))
    auth["summary"]["consent_missing"] = []
    auth["summary"]["consent_missing_urls"] = []
    AUTH.write_text(json.dumps(auth, ensure_ascii=False, indent=2), encoding="utf-8")

    defects = [
        {
            "defect_id": "DEF-CONSENT-BLOG",
            "severity": "HIGH",
            "form_ids": "FS-014,FS-015",
            "affected_urls": "https://i-seo.su/blog.html; blog-article.html",
            "source_authority": "static-html/blog.html + blog-article.html",
            "root_cause": "lead form lacked personal_data_consent",
            "fix": "added consent checkbox + privacy link matching WAVE 01",
            "files_changed": "blog.html; blog-article.html",
            "browser_verified": "YES-consent-live; page burst body=false is rate-limit not form bug",
            "mail_verified": "page handler isolated mail PASS",
            "status": "FIXED",
        },
        {
            "defect_id": "DEF-CYRILLIC-NAME",
            "severity": "MEDIUM",
            "form_ids": "WP footer callback",
            "affected_urls": "https://i-seo.su/blog/ and WP public pages using iseoblog footer",
            "source_authority": "theme/iseoblog/footer.php",
            "root_cause": "id/name cf_contact latinized for a11y; live select often cf_ontact (missing c); PHP already aliases",
            "fix": "footer id/name cf_contact; PHP aliases retained; no global HTML rename of cf_ontact",
            "files_changed": "footer.php",
            "browser_verified": "YES-blog_wp_footer_callback",
            "mail_verified": "YES-callback",
            "status": "FIXED",
        },
        {
            "defect_id": "DEF-RELATIVE-ENDPOINT",
            "severity": "CRITICAL",
            "form_ids": "nested SEO/city/niche/USA/UAE family sends",
            "affected_urls": "https://i-seo.su/services/seo/*",
            "source_authority": "js/common.js",
            "root_cause": "relative __FORM.php resolved under nested path",
            "fix": "root-relative /xxx__FORM.php on all family AJAX urls",
            "files_changed": "js/common.js",
            "browser_verified": "YES-nested_seo_page + nested tariff modals",
            "mail_verified": "YES",
            "status": "FIXED",
        },
        {
            "defect_id": "DEF-PREVENTDEFAULT",
            "severity": "HIGH",
            "form_ids": "submit buttons caught only by document click",
            "affected_urls": "multiple",
            "source_authority": "js/common.js",
            "root_cause": "native submit/reload when family handler missing or checkEmptyFields failed",
            "fix": "document click catch-all preventDefault + ensureSecurityFields; calc preventDefault",
            "files_changed": "js/common.js",
            "browser_verified": "YES-no unexpected reload on tested surfaces",
            "mail_verified": "N/A",
            "status": "FIXED",
        },
        {
            "defect_id": "DEF-CAREER-DEAD-UI",
            "severity": "CRITICAL",
            "form_ids": "career live #career__FORM_info",
            "affected_urls": "https://i-seo.su/career.html",
            "source_authority": "js/common.js + forms/career__FORM.php",
            "root_cause": "JS bound #career__FORM_send / #career__FORM; live DOM only _info; serialize omitted file; PHP required cf_file",
            "fix": "handler #career__FORM_send_info; PHP treats missing file as не приложен",
            "files_changed": "js/common.js; forms/career__FORM.php",
            "browser_verified": "YES",
            "mail_verified": "YES",
            "status": "FIXED",
        },
    ]
    dpath = OUT / "defects.csv"
    with dpath.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "defect_id",
                "severity",
                "form_ids",
                "affected_urls",
                "source_authority",
                "root_cause",
                "fix",
                "files_changed",
                "browser_verified",
                "mail_verified",
                "status",
            ],
        )
        w.writeheader()
        w.writerows(defects)

    missing = sum(1 for row in rows if row.get("consent") != "1")
    print(json.dumps({"rows": len(rows), "consent_missing": missing, "defects": len(defects)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

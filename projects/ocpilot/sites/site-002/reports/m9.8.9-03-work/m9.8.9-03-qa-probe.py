#!/usr/bin/env python3
"""M9.8.9-03 — live HTML QA probe."""
from __future__ import annotations

import json
import re
import urllib.request

URLS = {
    "stoly": "https://zpm.new-site.space/stoly-serii-premium/stoly/",
    "moechnye": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
    "podtovarniki": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/",
    "home": "https://zpm.new-site.space/",
    "katalog": "https://zpm.new-site.space/katalog/",
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-QA/1.0"})
    return urllib.request.urlopen(req, timeout=60).read().decode("utf-8", errors="replace")


def analyze(name: str, html: str, is_plp: bool) -> dict:
    cert_sections = len(re.findall(r'<section class="certificates"', html))
    commercial = "zpm-commercial-trust" in html
    dealers_sections = len(re.findall(r'<section class="zpm-dealers"', html))
    forms_dialog7 = len(re.findall(r'name="dialog"\s+value="7"', html))
    fancybox_plp = html.count('data-fancybox="certificates-plp"')
    fancybox_legacy = html.count('data-fancybox="certificates"')
    cert_slider = "js-certificates-slider" in html

    cert_hrefs = re.findall(
        r'data-fancybox="certificates-plp"[^>]*href="([^"]+)"', html
    )
    if not cert_hrefs:
        cert_hrefs = re.findall(
            r'href="(/assets/img/certificates/[^"]+)"[^>]*data-fancybox="certificates"', html
        )

    unique_certs = sorted(set(cert_hrefs))

    return {
        "url": URLS[name],
        "commercial_trust": commercial,
        "certificates_section_count": cert_sections,
        "dealers_section_count": dealers_sections,
        "forms_dialog7_count": forms_dialog7,
        "fancybox_plp_links": fancybox_plp,
        "fancybox_legacy_links": fancybox_legacy,
        "cert_slider_present": cert_slider,
        "unique_certificate_hrefs": unique_certs,
        "duplicate_cert_files_noted": len(cert_hrefs) > len(unique_certs),
        "plp_expectations": {
            "has_commercial_trust": commercial if is_plp else "n/a",
            "no_legacy_cert_section": cert_sections == 0 if is_plp else "n/a",
            "single_form": forms_dialog7 == 1 if is_plp else "n/a",
        },
        "pass": (
            (commercial and cert_sections == 0 and forms_dialog7 == 1)
            if is_plp
            else (commercial is False and cert_sections >= 1 and forms_dialog7 >= 1)
        ),
    }


def main() -> None:
    results = {}
    for name, url in URLS.items():
        html = fetch(url)
        results[name] = analyze(name, html, is_plp=name in {"stoly", "moechnye", "podtovarniki"})

    out = WORK_DIR / "qa-live-probe.json"
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    from pathlib import Path

    WORK_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-03-work")
    main()

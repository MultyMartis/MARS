#!/usr/bin/env python3
"""M9.8.9-03C — live HTML QA probe."""
from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

WORK_DIR = Path(r"C:\AI MARS\projects\ocpilot\sites\site-002\reports\m9.8.9-03c-work")

URLS = {
    "stoly": "https://zpm.new-site.space/stoly-serii-premium/stoly/",
    "moechnye": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/moechnye-vanny/",
    "podtovarniki": "https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki/",
    "home": "https://zpm.new-site.space/",
    "katalog": "https://zpm.new-site.space/katalog/",
}

EXPECTED_HEADINGS = {
    "stoly": "Нужна помощь с выбором столов?",
    "moechnye": "Нужна помощь с выбором моечных ванн?",
    "podtovarniki": "Нужна помощь с выбором подтоварников и подставок?",
}


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "MARS-QA/1.0"})
    return urllib.request.urlopen(req, timeout=60).read().decode("utf-8", errors="replace")


def extract_trust_title(html: str) -> str | None:
    match = re.search(
        r'class="zpm-commercial-trust__title"[^>]*>([^<]+)<',
        html,
    )
    if not match:
        return None
    return re.sub(r"\s+", " ", match.group(1).replace("&nbsp;", " ")).strip()


def analyze(name: str, html: str, is_plp: bool) -> dict:
    cert_sections = len(re.findall(r'<section class="certificates"', html))
    commercial = "zpm-commercial-trust" in html
    card = "zpm-commercial-trust__card" in html
    benefits = len(re.findall(r'<li class="zpm-commercial-trust__benefit"', html))
    services = len(re.findall(r'<div class="zpm-commercial-trust__service"', html))
    forms_dialog7 = len(re.findall(r'name="dialog"\s+value="7"', html))
    fancybox_plp = html.count('data-fancybox="certificates-plp"')
    cert_slider = "js-commercial-trust-certs" in html
    visible_cert_imgs = len(
        re.findall(r'zpm-commercial-trust__cert-img', html)
    )
    has_comment_label = ">Комментарий<" in html or ">Комментарий</label>" in html
    has_vopros_label = re.search(
        r'for="dealerMsg"[^>]*>[^<]*Вопрос', html
    ) is not None
    form_title = "Получить прайс-лист" in html
    submit_btn = "Отправить заявку" in html
    form_note = "Отправим актуальный прайс-лист" in html
    label_help = "Поможем с" in html and "выбором" in html

    cert_hrefs = re.findall(
        r'data-fancybox="certificates-plp"[^>]*href="([^"]+)"', html
    )
    if not cert_hrefs:
        cert_hrefs = re.findall(
            r'href="(/assets/img/certificates/[^"]+)"[^>]*data-fancybox="certificates-plp"',
            html,
        )
    unique_certs = sorted(set(cert_hrefs))

    title = extract_trust_title(html) if commercial else None
    expected_title = EXPECTED_HEADINGS.get(name)

    plp_pass = (
        commercial
        and card
        and cert_sections == 0
        and forms_dialog7 == 1
        and benefits == 6
        and services == 4
        and visible_cert_imgs == 1
        and has_comment_label
        and not has_vopros_label
        and form_title
        and submit_btn
        and form_note
        and label_help
        and (expected_title is None or title == expected_title)
    )

    control_pass = (
        not commercial
        and cert_sections >= 1
        and forms_dialog7 >= 1
    )

    return {
        "url": URLS[name],
        "commercial_trust": commercial,
        "unified_card": card,
        "dynamic_title": title,
        "expected_title": expected_title,
        "title_match": title == expected_title if expected_title else "n/a",
        "benefits_count": benefits,
        "services_count": services,
        "visible_cert_images": visible_cert_imgs,
        "unique_certificate_hrefs": unique_certs,
        "certificates_section_count": cert_sections,
        "forms_dialog7_count": forms_dialog7,
        "fancybox_plp_links": fancybox_plp,
        "cert_slider_present": cert_slider,
        "comment_label": has_comment_label,
        "vopros_label_absent": not has_vopros_label,
        "form_title_present": form_title,
        "submit_button_text": submit_btn,
        "form_note_present": form_note,
        "pass": plp_pass if is_plp else control_pass,
    }


def main() -> None:
    results = {}
    for name, url in URLS.items():
        html = fetch(url)
        results[name] = analyze(name, html, is_plp=name in EXPECTED_HEADINGS)

    out = WORK_DIR / "qa-live-probe.json"
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

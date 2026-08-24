# -*- coding: utf-8 -*-
"""Focused live QA for Specialists Hub."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from urllib.request import Request, urlopen

OUT = Path(__file__).resolve().parent
UA = "Mozilla/5.0 (compatible; FP0002-SpecialistsHubQA/1.0)"


def fetch(url: str, timeout: int = 45) -> tuple[int, bytes, dict]:
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=timeout) as resp:
        body = resp.read()
        headers = {k.lower(): v for k, v in resp.headers.items()}
        return resp.status, body, headers


def main() -> None:
    report: dict = {"checks": []}

    def add(name: str, ok: bool, detail=None):
        report["checks"].append({"name": name, "ok": ok, "detail": detail})
        print(("PASS" if ok else "FAIL"), name, detail if detail is not None else "")

    # Hub
    status, body, headers = fetch("https://shpigovsky.ru/specyalisty/")
    html = body.decode("utf-8", "replace")
    OUT.joinpath("04-hub.html").write_text(html, encoding="utf-8")
    add("hub_http_200", status == 200, status)
    add("no_placeholder", PLACEHOLDER not in html and "находится в подготовке" not in html)
    add("has_h1", bool(re.search(r"<h1[^>]*>\s*Специалисты\s*</h1>", html)))
    add("has_breadcrumbs", "breadcrumbs" in html)
    add("has_hub_list", 'data-specialists-hub-list' in html)
    add("uses_feature_grid", "home-feature-grid__card-grid" in html)
    add("uses_specialist_card", "specialists__card" in html)
    add("uses_card_link", "specialists__card-link" in html)
    add("no_swiper_on_hub", "data-specialists-slider" not in html)
    cards = re.findall(r'class="specialists__card"[^>]*>', html)
    names = re.findall(r'class="specialists__name"[^>]*>([^<]+)<', html)
    links = re.findall(r'class="specialists__card-link"[^>]*href="([^"]+)"', html)
    add("card_count_9", len(names) == 9, {"names": names, "n": len(names), "links_n": len(links)})
    add("no_duplicate_names", len(names) == len(set(names)), names)
    expected_order = [
        "Сергей Юрьевич Шпиговский",
        "Максим Михайлович Казаков",
        "Дарья Владимировна Костюк",
        "Ханикова Светлана Николаевна",
        "Шапигузова Татьяна Андреевна",
        "Литвинов Кирилл Алексеевич",
        "Поверинов Александр Константинович",
        "Филиппов Илья Владимирович",
        "Филиппова Мария Михайловна",
    ]
    add("order_matches_menu_order", names == expected_order, {"got": names, "expected": expected_order})
    add("all_links_under_specyalisty", all("/specyalisty/" in u for u in links), links)
    add("no_php_warning", "Warning:" not in html and "Fatal error" not in html and "Notice:" not in html)
    add("canonical_hint", "specyalisty" in html.lower())

    # /specialisty/ untouched
    try:
        st2, b2, _ = fetch("https://shpigovsky.ru/specialisty/")
        add("specialisty_still_404", st2 == 404, st2)
    except Exception as exc:
        # urlopen raises on 404 sometimes
        add("specialisty_still_404", "404" in str(exc), str(exc))

    # Singles smoke
    for slug in ("shpigovsky", "kostyuk", "filippova"):
        url = f"https://shpigovsky.ru/specyalisty/{slug}/"
        st, b, _ = fetch(url)
        h = b.decode("utf-8", "replace")
        add(f"single_{slug}_200", st == 200, st)
        add(f"single_{slug}_no_fatal", "Fatal error" not in h)

    # Home specialists slider still present
    st, b, _ = fetch("https://shpigovsky.ru/")
    h = b.decode("utf-8", "replace")
    add("home_200", st == 200, st)
    add("home_specialists_slider", "data-specialists-slider" in h)
    home_names = re.findall(r'class="specialists__name"[^>]*>([^<]+)<', h)
    add("home_specialists_count_ge_1", len(home_names) >= 1, len(home_names))

    # Services hub
    st, b, _ = fetch("https://shpigovsky.ru/uslugi/")
    h = b.decode("utf-8", "replace")
    add("uslugi_200", st == 200, st)

    # Robots / indexing surfaces
    st, b, _ = fetch("https://shpigovsky.ru/robots.txt")
    robots = b.decode("utf-8", "replace")
    OUT.joinpath("04-robots.txt").write_text(robots, encoding="utf-8")
    add("robots_200", st == 200, st)
    add("robots_sha_unchanged", hashlib.sha256(b).hexdigest() == "2594093919d01f067bcd3776d50d973cfa20a1faf4a6d63fc23f21367d08529e", hashlib.sha256(b).hexdigest())

    st, b, _ = fetch("https://shpigovsky.ru/wp-sitemap.xml")
    add("sitemap_200", st == 200, st)

    failed = [c for c in report["checks"] if not c["ok"]]
    report["verdict"] = "PASS" if not failed else "FAIL"
    report["failed"] = failed
    OUT.joinpath("04-live-qa.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("VERDICT", report["verdict"], "failed", len(failed))


PLACEHOLDER = "Раздел находится в подготовке. Здесь будет опубликована информация по теме страницы."

if __name__ == "__main__":
    main()

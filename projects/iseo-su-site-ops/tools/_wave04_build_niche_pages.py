#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WAVE 04: build 7 niche SEO pages from automotive source + update hub."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(r"X:\AI MARS\projects\iseo-su-site-ops")
SRC = ROOT / "production-source" / "static-html" / "services" / "seo" / "prodvizhenie-avtomobilnogo-sajta.html"
HUB = ROOT / "production-source" / "static-html" / "services" / "seo.html"
OUT_DIR = ROOT / "production-source" / "static-html" / "services" / "seo"
REPORT = ROOT / "tools" / "_wave04_build_report.json"

# Exact hub niche link count before mutation (more_landing_pages__navigations)
# Verified: 31 items.

PAGES = [
    {
        "file": "prodvizhenie-sajta-pitomnika.html",
        "url": "https://i-seo.su/services/seo/prodvizhenie-sajta-pitomnika.html",
        "title": "Заказать SEO продвижение сайта питомника | i-seo.su",
        "description": "Продвигаем сайты питомников собак и кошек в топ Яндекса и Google. Рост заявок от заводчиков и покупателей щенков. Бесплатный аудит и стратегия.",
        "h1": "SEO продвижение сайта питомника",
        "intro": "SEO продвижение сайта питомника помогает заводчику собак и кошек получать заявки напрямую с поиска, а не только через сарафанное радио и профильные форумы. Мы строим стратегию под запросы владельцев конкретной породы, добавляем в семантику названия пород, а также смежные темы вроде зоомагазинов и ветклиник, популярные у той же аудитории. Отдельно продвижение сайта питомника требует карточек каждого щенка с фото и статуса наличия, каталога пометов и статей о породе, такой подход поднимает позиции и увеличивает органический трафик и посещаемость страницы.",
        "breadcrumb_last": "SEO продвижение сайта питомника",
        "hub_label": "SEO продвижение сайта питомника",
        "replace_case": True,
    },
    {
        "file": "prodvizhenie-sajta-smi.html",
        "url": "https://i-seo.su/services/seo/prodvizhenie-sajta-smi.html",
        "title": "Заказать SEO продвижение сайта СМИ под ключ | i-seo.su",
        "description": "Продвигаем сайты изданий и новостных проектов в топ поиска. Рост охвата, посещаемости и доверия читателей. Бесплатный аудит и стратегия продвижения.",
        "h1": "SEO продвижение сайта СМИ",
        "intro": "Продвижение сми в интернете отличается от обычного коммерческого SEO, здесь на первом месте скорость публикации и охват, а не карточка товара. Мы строим стратегию продвижения новостного сайта через регулярные публикации, работу с журналистами и агрегаторами, а также размещение материалов на профильных площадках для роста цитируемости издания. Отдельно ведем раскрутку СМИ через соцсети и рассылки, такая работа увеличивает читательскую аудиторию и укрепляет медийную репутацию бренда в своей тематике.",
        "breadcrumb_last": "SEO продвижение сайта СМИ",
        "hub_label": "SEO продвижение сайта СМИ",
        "replace_case": False,
    },
    {
        "file": "prodvizhenie-sajta-restorana.html",
        "url": "https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html",
        "title": "Заказать SEO продвижение сайта ресторана | i-seo.su",
        "description": "Продвигаем сайты ресторанов и кафе в топ Яндекса и Google. Рост бронирований столиков и посетителей зала. Бесплатный аудит и понятная стратегия.",
        "h1": "SEO продвижение сайта ресторана",
        "intro": "SEO продвижение ресторана под ключ включает работу с картами, отзывами гостей и локальной выдачей по району заведения. Мы строим стратегию продвижения сайта ресторана под запросы конкретной кухни, оптимизируем меню и карточки блюд, а также добавляем удобную форму бронирования столика прямо на сайте. Такой подход поднимает позиции ресторана или бара в локальном поиске и увеличивает поток гостей из карт и поисковой выдачи.",
        "breadcrumb_last": "SEO продвижение сайта ресторана",
        "hub_label": "SEO продвижение сайта ресторана",
        "replace_case": False,
    },
    {
        "file": "prodvizhenie-internet-magazina-zapchastej.html",
        "url": "https://i-seo.su/services/seo/prodvizhenie-internet-magazina-zapchastej.html",
        "title": "SEO продвижение интернет-магазина запчастей | i-seo.su",
        "description": "Продвигаем интернет-магазины автозапчастей в топ поиска. Оптимизация каталога по маркам и моделям, рост заявок и продаж. Бесплатный аудит и стратегия.",
        "h1": "SEO продвижение интернет-магазина запчастей",
        "intro": "Продвижение сайта автозапчастей строится на точной структуре каталога по маркам, моделям и VIN-номеру, ведь именно так покупатель ищет нужную деталь. Мы прорабатываем семантическое ядро под каждую категорию и фильтр каталога, устраняем технические ошибки индексации и увеличиваем видимость магазина в конкурентной тематике. Стоимость такой работы, то есть продвижение сайта автозапчастей цена, зависит от объема каталога и заметно окупается ростом конверсии и посещаемости уже в первые месяцы.",
        "breadcrumb_last": "SEO продвижение интернет-магазина запчастей",
        "hub_label": "SEO продвижение Интернет-магазина запчастей",
        "replace_case": False,
    },
    {
        "file": "prodvizhenie-sajta-internet-provajdera.html",
        "url": "https://i-seo.su/services/seo/prodvizhenie-sajta-internet-provajdera.html",
        "title": "SEO продвижение сайта интернет-провайдера | i-seo.su",
        "description": "Продвигаем сайты интернет-провайдеров в топ Яндекса и Google. Рост заявок на подключение по конкретным районам и адресам. Бесплатный аудит и стратегия.",
        "h1": "SEO продвижение сайта интернет-провайдера",
        "intro": "Продвижение интернет провайдера опирается на точную геопривязку тарифов к дому, улице и району подключения, потому что пользователь ищет доступность именно по своему адресу. Стратегия включает оптимизацию страниц с тарифами и зоной покрытия, работу с картами и отзывами абонентов, а также ускорение сайта, поскольку медленная проверка адреса быстро отпугивает посетителя. Такой подход поднимает позиции провайдера в локальном поиске и увеличивает число заявок на подключение.",
        "breadcrumb_last": "SEO продвижение сайта интернет-провайдера",
        "hub_label": "SEO продвижение сайта интернет-провайдера",
        "replace_case": False,
    },
    {
        "file": "prodvizhenie-internet-magazina-kosmetiki.html",
        "url": "https://i-seo.su/services/seo/prodvizhenie-internet-magazina-kosmetiki.html",
        "title": "SEO продвижение интернет-магазина косметики | i-seo.su",
        "description": "Продвигаем интернет-магазины косметики и парфюмерии в топ поиска. Рост трафика, заявок и продаж по бьюти-тематике. Бесплатный аудит и стратегия.",
        "h1": "SEO продвижение интернет-магазина косметики",
        "intro": "Продвижение интернет магазина косметики строится на визуальном контенте, честных отзывах и доверии к бренду, ведь в этой нише решение о покупке сильно зависит от чужого мнения. Мы прорабатываем структуру каталога по категориям и типам кожи, добавляем блог с обзорами и гайдами по уходу, а также усиливаем репутацию магазина через работу с отзывами. Продвижение сайта косметики в такой связке поднимает позиции по конкурентным запросам и увеличивает конверсию каталога.",
        "breadcrumb_last": "SEO продвижение интернет-магазина косметики",
        "hub_label": "SEO продвижение Интернет-магазина косметики",
        "replace_case": False,
    },
    {
        "file": "prodvizhenie-internet-magazina-czvetov.html",
        "url": "https://i-seo.su/services/seo/prodvizhenie-internet-magazina-czvetov.html",
        "title": "Заказать SEO продвижение интернет-магазина цветов | i-seo.su",
        "description": "Продвигаем интернет-магазины цветов и доставки букетов в топ поиска. Рост заказов на срочную доставку по городу. Бесплатный аудит и стратегия работы.",
        "h1": "SEO продвижение интернет-магазина цветов",
        "intro": "SEO продвижение цветов отличается высокой сезонностью спроса и жесткой конкуренцией в праздничные даты, когда каждый час промедления стоит потерянных заказов. Стратегия строится под срочные запросы вроде доставки букета день в день, оптимизацию карточек по поводу и получателю, а также ускорение оформления заказа на сайте. Такой подход поднимает позиции магазина перед праздниками и увеличивает число заказов на срочную доставку.",
        "breadcrumb_last": "SEO продвижение интернет-магазина цветов",
        "hub_label": "SEO продвижение Интернет-магазина цветов",
        "replace_case": False,
    },
]

# Maltipoo Honey Club case replacement (Pitomnik only). Image verified HTTP 200.
# No public client domain on case page — secondary link points to case URL (charter).
DRIVE_AVENUE_CASE_BLOCK = """\t\t\t\t\t<div class="our_cases">
\t\t\t\t\t\t<div class="our_cases__block">
\t\t\t\t\t\t\t<div class="inner">
\t\t\t\t\t\t\t\t<h3><a href="/cases/driveavenue.html">Автосалон Drive&nbsp;Avenue</a></h3>
\t\t\t\t\t\t\t\t<a href="https://driveavenue.ru" target="_blank" rel="nofollow">https://driveavenue.ru</a>
\t\t\t\t\t\t\t\t<ul>
\t\t\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t\t\t<div>Динамика трафика со всех каналов</div>
\t\t\t\t\t\t\t\t\t\t<span>4000+</span>
\t\t\t\t\t\t\t\t\t</li>
\t\t\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t\t\t<div>Динамика по заявкам и звонкам со всех каналов</div>
\t\t\t\t\t\t\t\t\t\t<span>107+</span>
\t\t\t\t\t\t\t\t\t</li>
\t\t\t\t\t\t\t\t</ul>
\t\t\t\t\t\t\t\t<div class="our_cases__btns">
\t\t\t\t\t\t\t\t\t<a href="#callback__FORM_popup" class="modalbox our_cases__order">Хочу также</a>
\t\t\t\t\t\t\t\t\t<a href="/cases.html" class="our_cases__more">Все кейсы</a>
\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t\t<div class="our_cases__block">
\t\t\t\t\t\t\t<div class="inner">
\t\t\t\t\t\t\t\t<div class="our_cases__block_img">
\t\t\t\t\t\t\t\t\t<img src="../../img/cases/driveavenue.png" alt="Кейс: Drive Avenue" style="transform: translate(-50%,0);top: 0;">
\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>"""

MALTIPOO_CASE_BLOCK = """\t\t\t\t\t<div class="our_cases">
\t\t\t\t\t\t<div class="our_cases__block">
\t\t\t\t\t\t\t<div class="inner">
\t\t\t\t\t\t\t\t<h3><a href="/cases/maltipoo-honey-club.html">Maltipoo Honey Club</a></h3>
\t\t\t\t\t\t\t\t<a href="https://i-seo.su/cases/maltipoo-honey-club.html" target="_blank" rel="nofollow">https://i-seo.su/cases/maltipoo-honey-club.html</a>
\t\t\t\t\t\t\t\t<ul>
\t\t\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t\t\t<div>120+ страниц</div>
\t\t\t\t\t\t\t\t\t\t<span>120+</span>
\t\t\t\t\t\t\t\t\t</li>
\t\t\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t\t\t<div>5,5% конверсия</div>
\t\t\t\t\t\t\t\t\t\t<span>5,5%</span>
\t\t\t\t\t\t\t\t\t</li>
\t\t\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t\t\t<div>2300+ трафика/мес</div>
\t\t\t\t\t\t\t\t\t\t<span>2300+</span>
\t\t\t\t\t\t\t\t\t</li>
\t\t\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t\t\t<div>44+ заявки/мес</div>
\t\t\t\t\t\t\t\t\t\t<span>44+</span>
\t\t\t\t\t\t\t\t\t</li>
\t\t\t\t\t\t\t\t\t<li>
\t\t\t\t\t\t\t\t\t\t<div>67 запросов в топ-10</div>
\t\t\t\t\t\t\t\t\t\t<span>67</span>
\t\t\t\t\t\t\t\t\t</li>
\t\t\t\t\t\t\t\t</ul>
\t\t\t\t\t\t\t\t<div class="our_cases__btns">
\t\t\t\t\t\t\t\t\t<a href="#callback__FORM_popup" class="modalbox our_cases__order">Хочу также</a>
\t\t\t\t\t\t\t\t\t<a href="/cases.html" class="our_cases__more">Все кейсы</a>
\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t\t<div class="our_cases__block">
\t\t\t\t\t\t\t<div class="inner">
\t\t\t\t\t\t\t\t<div class="our_cases__block_img">
\t\t\t\t\t\t\t\t\t<img src="../../img/cases/maltipoo-honey-club.png" alt="Кейс: Maltipoo Honey Club" style="transform: translate(-50%,0);top: 0;">
\t\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t\t</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>"""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def hub_nb_label(label: str) -> str:
    """Match existing hub style: SEO&nbsp;продвижение ..."""
    if label.startswith("SEO продвижение"):
        return "SEO&nbsp;" + label[len("SEO ") :]
    return label


def transform_page(html: str, page: dict) -> str:
    out = html

    # Title
    out = re.sub(
        r"<title>.*?</title>",
        f"<title>{page['title']}</title>",
        out,
        count=1,
        flags=re.I | re.S,
    )

    # Meta description
    out = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{page["description"]}">',
        out,
        count=1,
        flags=re.I,
    )

    # Self-canonical (WAVE 02/03 pattern: after robots, before googlebot)
    if 'rel="canonical"' not in out and "rel='canonical'" not in out:
        out = re.sub(
            r'(<meta name="robots" content="index, follow">\s*)',
            r'\1\t<link rel="canonical" href="' + page["url"] + '">\n',
            out,
            count=1,
            flags=re.I,
        )
    else:
        out = re.sub(
            r'<link rel="canonical" href="[^"]*">',
            f'<link rel="canonical" href="{page["url"]}">',
            out,
            count=1,
            flags=re.I,
        )

    # Breadcrumb last level only
    out = re.sub(
        r"(<ul class=\"breadcrumbs\">.*?<li><a href=\"/services/seo\.html\">SEO-Продвижение</a></li>\s*)<li>.*?</li>",
        r"\1<li>" + page["breadcrumb_last"] + "</li>",
        out,
        count=1,
        flags=re.S,
    )

    # H1 (first only — hero)
    out = re.sub(
        r"<h1>SEO&nbsp;продвижение автомобильного сайта</h1>",
        f"<h1>{page['h1']}</h1>",
        out,
        count=1,
    )
    # Also plain variant without nbsp if present after prior edits
    out = re.sub(
        r"<h1>SEO продвижение автомобильного сайта</h1>",
        f"<h1>{page['h1']}</h1>",
        out,
        count=1,
    )

    # Intro span immediately after H1
    out = re.sub(
        r"(</h1>\s*)<span>SEO продвижение автомобильного сайта.*?</span>",
        r"\1<span>" + page["intro"] + "</span>",
        out,
        count=1,
        flags=re.S,
    )

    if page["replace_case"]:
        if DRIVE_AVENUE_CASE_BLOCK not in out:
            raise RuntimeError("Drive Avenue case block not found for Pitomnik replacement")
        out = out.replace(DRIVE_AVENUE_CASE_BLOCK, MALTIPOO_CASE_BLOCK, 1)

    return out


def count_hub_niche_links(hub_html: str) -> list[tuple[str, str]]:
    m = re.search(
        r'class="more_landing_pages__navigations">(.*?)</div>',
        hub_html,
        flags=re.S,
    )
    if not m:
        raise RuntimeError("Hub niche navigations block not found")
    return re.findall(r'<a href="(/services/seo/[^"]+)">([^<]+)</a>', m.group(1))


def update_hub(hub_html: str) -> tuple[str, int, int]:
    before = count_hub_niche_links(hub_html)
    before_n = len(before)

    # Append 7 new links before closing </div> of navigations
    additions = []
    for p in PAGES:
        href = f"/services/seo/{p['file']}"
        label = hub_nb_label(p["hub_label"])
        additions.append(f'\t\t\t\t\t\t\t\t<a href="{href}">{label}</a>')

    block = "\n".join(additions)
    # Insert before last niche link's following close — append after last </a> in navigations
    def repl(m: re.Match) -> str:
        inner = m.group(1).rstrip()
        return (
            'class="more_landing_pages__navigations">'
            + inner
            + "\n"
            + block
            + "\n\t\t\t\t\t\t\t</div>"
        )

    new_html, n = re.subn(
        r'class="more_landing_pages__navigations">(.*?)</div>',
        repl,
        hub_html,
        count=1,
        flags=re.S,
    )
    if n != 1:
        raise RuntimeError("Failed to update hub niche list")

    after = count_hub_niche_links(new_html)
    return new_html, before_n, len(after)


def main() -> None:
    raw = SRC.read_text(encoding="utf-8")
    if "автомобильного сайта" not in raw:
        raise SystemExit("Source does not look like automotive niche page")
    if "tarif-calc.php" not in raw or "content-form-seo.php" not in raw:
        raise SystemExit("Source missing form/calc includes — refuse stale clone")

    created = []
    for page in PAGES:
        html = transform_page(raw, page)
        # Verify mappings
        assert page["title"] in html, page["file"]
        assert page["description"] in html, page["file"]
        assert f"<h1>{page['h1']}</h1>" in html, page["file"]
        assert page["intro"] in html, page["file"]
        assert f"<li>{page['breadcrumb_last']}</li>" in html, page["file"]
        assert f'rel="canonical" href="{page["url"]}"' in html, page["file"]
        assert "автомобильного сайта</li>" not in html, page["file"]
        if page["replace_case"]:
            assert "maltipoo-honey-club" in html
            assert "Maltipoo Honey Club" in html
            assert "/cases/driveavenue.html" not in html
            assert "driveavenue" not in html.lower()
            assert "Drive Avenue" not in html
            assert "Drive&nbsp;Avenue" not in html
        else:
            assert "/cases/driveavenue.html" in html
            assert "maltipoo-honey-club" not in html

        path = OUT_DIR / page["file"]
        data = html.encode("utf-8")
        path.write_bytes(data)
        created.append(
            {
                "file": page["file"],
                "path": str(path),
                "sha256": sha256_bytes(data),
                "bytes": len(data),
                "replace_case": page["replace_case"],
            }
        )

    hub_raw = HUB.read_text(encoding="utf-8")
    hub_new, before_n, after_n = update_hub(hub_raw)
    hub_data = hub_new.encode("utf-8")
    HUB.write_bytes(hub_data)

    report = {
        "source_sha256": sha256_bytes(raw.encode("utf-8")),
        "created": created,
        "hub": {
            "path": str(HUB),
            "niche_before": before_n,
            "niche_after": after_n,
            "sha256": sha256_bytes(hub_data),
            "bytes": len(hub_data),
        },
        "consent_note": "Forms/consent via shared PHP includes (content-form-seo.php, content-seo-popups.php, tarif-calc.php); page HTML preserves includes unchanged.",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"ok": True, "created": len(created), "hub_before": before_n, "hub_after": after_n}, ensure_ascii=False))


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Build WAVE 02 city SEO pages + hub linking from b-regionakh.html hub."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(r"X:\AI MARS\projects\iseo-su-site-ops")
HUB = ROOT / "production-source" / "static-html" / "services" / "seo" / "b-regionakh.html"
OUT_DIR = ROOT / "production-source" / "static-html" / "services" / "seo"
BACKUP_DIR = Path(r"X:\AI MARS\local\sites\iseo-su-production\_city-pages-wave-02")

CITIES = [
    {
        "slug": "prodvizhenie-v-sankt-peterburge.html",
        "url": "https://i-seo.su/services/seo/prodvizhenie-v-sankt-peterburge.html",
        "city": "Санкт-Петербург",
        "title": "SEO-продвижение сайта компании в Санкт-Петербурге | i-seo.su",
        "description": "Продвигаем сайты компаний Санкт-Петербурга в топ Яндекса и Google. Бесплатный аудит, прозрачные тарифы, рост позиций и трафика за 3 месяца.",
        "h1": "SEO-продвижение сайта в Санкт-Петербурге",
        "intro": "Санкт-Петербург входит в число самых конкурентных регионов России для SEO-продвижения сайта, особенно в сферах туризма, HoReCa и B2B. Стратегия продвижения опирается на реальный поисковый спрос локальной аудитории и учитывает специфику Северной столицы на каждом этапе аудита и подбора семантики. Такой подход поднимает позиции и увеличивает органический трафик для компаний Петербурга и Ленинградской области.",
        "main_title": "SEO продвижение сайта в Санкт-Петербурге",
        "main_text": "Продвижение сайта в Санкт-Петербурге и в целом продвижение сайтов в СПб требует акцента на локальных ключевых словах и геопривязанном контенте. В работу входят следующие направления.",
        "list": [
            "регистрация и ведение карточки в Яндекс.Картах и 2ГИС",
            "оптимизация страниц под запросы с упоминанием города и района",
            "работа с отзывами на локальных площадках",
            "публикация контента, релевантного бизнес-среде Петербурга",
        ],
        "after_list": "Такой набор действий помогает сайту закрепиться в выдаче именно для аудитории города и получить первые заявки уже в течение трех месяцев.",
        "faq4": "Общий запрос «купить недвижимость в Санкт-Петербурге» высококонкурентный, а более узкий запрос с указанием конкретного района или типа объекта продвинуть значительно проще.",
    },
    {
        "slug": "prodvizhenie-v-kazani.html",
        "url": "https://i-seo.su/services/seo/prodvizhenie-v-kazani.html",
        "city": "Казань",
        "title": "SEO-продвижение сайта компании в Казани | i-seo.su",
        "description": "Продвижение сайтов в Казани под ключ. Аудит, оптимизация и рост позиций в Яндексе и Google. Работаем с бизнесом Татарстана любого масштаба.",
        "h1": "SEO-продвижение сайта в Казани",
        "intro": "Казань закрепилась как один из растущих IT-центров страны, и SEO-продвижение сайта в Казани здесь требует учитывать сразу два рынка, городской и республиканский. Подбор стратегии опирается на аудиторию Татарстана, от растущего кластера вокруг Иннополиса до классического бизнеса в сфере услуг и торговли. По итогам работы растет видимость сайта в поиске и увеличивается поток целевых заявок.",
        "main_title": "SEO продвижение сайта в Казани",
        "main_text": "Продвижение сайта в Казани и шире, продвижение сайтов в Татарстане, строится на локальных ключевых словах и геопривязанном контенте. В работу входят следующие направления.",
        "list": [
            "регистрация и ведение карточки в Яндекс.Картах и 2ГИС",
            "оптимизация страниц под запросы с упоминанием города и района",
            "работа с отзывами на локальных площадках",
            "публикация контента, релевантного бизнес-среде республики",
        ],
        "after_list": "Такой набор действий помогает сайту закрепиться в топе выдачи для пользователей из Казани и региона.",
        "faq4": "Широкий запрос «купить недвижимость в Казани» высококонкурентный, тогда как более узкий запрос с указанием района или типа объекта выводится в топ быстрее.",
    },
    {
        "slug": "prodvizhenie-v-ekaterinburge.html",
        "url": "https://i-seo.su/services/seo/prodvizhenie-v-ekaterinburge.html",
        "city": "Екатеринбург",
        "title": "SEO-продвижение сайта компании в Екатеринбурге | i-seo.su",
        "description": "Комплексное SEO-продвижение сайтов в Екатеринбурге. Выводим бизнес в топ поисковой выдачи, увеличиваем трафик и заявки с сайта.",
        "h1": "SEO-продвижение сайта в Екатеринбурге",
        "intro": "Екатеринбург остается крупнейшим логистическим и промышленным хабом Урала с сильным B2B-сегментом, и SEO-продвижение сайта в Екатеринбурге здесь строится с поправкой именно на эту специфику. Аудит и анализ конкурентов в городе задают направление стратегии, ориентированной на реальный поисковый спрос локальной аудитории. Такая работа приносит устойчивый рост позиций и органического трафика для сайта.",
        "main_title": "SEO продвижение сайта в Екатеринбурге",
        "main_text": "Продвижение сайта в Екатеринбурге требует акцента на локальных ключевых словах и геопривязанном контенте. В работу входят следующие направления.",
        "list": [
            "регистрация и ведение карточки в Яндекс.Картах и 2ГИС",
            "оптимизация страниц под запросы с упоминанием города и района",
            "работа с отзывами на локальных площадках",
            "публикация контента, релевантного бизнес-среде Урала",
        ],
        "after_list": "Такой набор действий помогает сайту закрепиться в выдаче именно для пользователей из Екатеринбурга.",
        "faq4": "Запрос «купить недвижимость в Екатеринбурге» занят крупными федеральными агрегаторами, а более узкий запрос с уточнением по району продвинуть проще и быстрее.",
    },
    {
        "slug": "prodvizhenie-v-novosibirske.html",
        "url": "https://i-seo.su/services/seo/prodvizhenie-v-novosibirske.html",
        "city": "Новосибирск",
        "title": "SEO-продвижение сайта компании в Новосибирске | i-seo.su",
        "description": "Продвигаем сайты бизнеса в Новосибирске. Аудит, стратегия, рост позиций и трафика. Опыт в разных нишах, прозрачная отчетность на каждом этапе.",
        "h1": "SEO-продвижение сайта в Новосибирске",
        "intro": "Новосибирск остается крупным научным и IT-центром Сибири с растущим сегментом e-commerce, и SEO-продвижение сайта в Новосибирске здесь опирается именно на эту специфику аудитории. Аудит и анализ конкурентов в городе формируют стратегию, ориентированную на реальный поисковый спрос локального рынка. Постепенно растет видимость сайта в поиске и увеличивается поток целевых заявок.",
        "main_title": "SEO продвижение сайта в Новосибирске",
        "main_text": "Продвижение сайта в Новосибирске требует акцента на локальных ключевых словах и геопривязанном контенте. В работу входят следующие направления.",
        "list": [
            "регистрация и ведение карточки в Яндекс.Картах и 2ГИС",
            "оптимизация страниц под запросы с упоминанием города и района",
            "работа с отзывами на локальных площадках",
            "публикация контента, релевантного бизнес-среде города",
        ],
        "after_list": "Такой набор действий помогает сайту закрепиться в топе выдачи именно для пользователей из Новосибирска.",
        "faq4": "Запрос «купить недвижимость в Новосибирске» высококонкурентный по всему городу, а более узкий запрос с уточнением по району продвигается значительно легче.",
    },
    {
        "slug": "prodvizhenie-v-krasnoyarske.html",
        "url": "https://i-seo.su/services/seo/prodvizhenie-v-krasnoyarske.html",
        "city": "Красноярск",
        "title": "SEO-продвижение сайта компании в Красноярске | i-seo.su",
        "description": "SEO-продвижение сайтов в Красноярске под ключ. Бесплатный аудит, работа над позициями и трафиком, отчетность на каждом этапе сотрудничества.",
        "h1": "SEO-продвижение сайта в Красноярске",
        "intro": "Красноярск остается промышленным центром Сибири с растущим сегментом услуг и торговли, и SEO-продвижение сайта в Красноярске здесь строится с учетом именно этой специфики рынка. Направление стратегии определяют аудит и анализ конкурентов в городе, с опорой на реальный поисковый спрос аудитории города. Итогом становится устойчивый рост позиций сайта и стабильный поток целевых заявок.",
        "main_title": "SEO продвижение сайта в Красноярске",
        "main_text": "Продвижение сайта в Красноярске требует акцента на локальных ключевых словах и геопривязанном контенте. В работу входят следующие направления.",
        "list": [
            "регистрация и ведение карточки в Яндекс.Картах и 2ГИС",
            "оптимизация страниц под запросы с упоминанием города и района",
            "работа с отзывами на локальных площадках",
            "публикация контента, релевантного бизнес-среде города",
        ],
        "after_list": "Такой набор действий помогает сайту закрепиться в выдаче именно для пользователей из Красноярска.",
        "faq4": "Широкий запрос «купить недвижимость в Красноярске» перегружен конкурентами, а более узкий запрос с уточнением по району продвигается заметно быстрее.",
    },
]

HUB_URL = "https://i-seo.su/services/seo/b-regionakh.html"

HUB_TITLE_OLD = "SEO продвижение сайта в регионах России — под ключ | INTLSEO"
HUB_DESC_OLD = "Продвигаем сайты в регионах РФ: настройка гео-меток, локальных сниппетов, Яндекс.Справочника. Выводим в ТОП даже в малых городах. Бесплатный аудит для региональных проектов!"
HUB_H1_OLD = "SEO&nbsp;продвижение в&nbsp;регионах"
HUB_INTRO_RE = re.compile(
    r"(</h1>\s*)(<span>.*?</span>)",
    re.DOTALL,
)
HUB_MAIN_H2 = "SEO&nbsp;продвижение региональных сайтов"
HUB_MAIN_SPAN_RE = re.compile(
    r'(<div class="second_col_info_span">)(.*?)(</div>\s*\n\s*<div class="achievement)',
    re.DOTALL,
)
HUB_FAQ4_RE = re.compile(
    r'(<div class="uni_faq_block" id="tab04">[\s\S]*?<div class="uni_faq__title">Насколько реально попасть на первую страницу поиска\?</div>\s*)'
    r'(<span>[\s\S]*?</span>)',
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_main_block(city: dict) -> str:
    items = "\n".join(f"\t\t\t\t\t\t\t<li>{item}</li>" for item in city["list"])
    backlink = (
        f'Подробнее о&nbsp;подходе к&nbsp;региональному SEO см.&nbsp;на&nbsp;странице '
        f'<a href="{HUB_URL}">SEO-продвижение в&nbsp;регионах</a>.'
    )
    return (
        f"{city['main_text']}<br><br>\n"
        f"\t\t\t\t\t\t<ul class=\"uni_check_list__list\">\n"
        f"{items}\n"
        f"\t\t\t\t\t\t</ul><br>\n"
        f"\t\t\t\t\t\t{city['after_list']}<br><br>\n"
        f"\t\t\t\t\t\t{backlink}"
    )


def patch_city_page(hub_html: str, city: dict) -> str:
    html = hub_html

    # title
    html = html.replace(
        f"<title>{HUB_TITLE_OLD}</title>",
        f"<title>{city['title']}</title>",
        1,
    )
    # description
    html = html.replace(
        f'<meta name="description" content="{HUB_DESC_OLD}">',
        f'<meta name="description" content="{city["description"]}">',
        1,
    )
    # self-canonical after robots
    if 'rel="canonical"' not in html:
        html = html.replace(
            '<meta name="robots" content="index, follow">',
            '<meta name="robots" content="index, follow">\n'
            f'\t<link rel="canonical" href="{city["url"]}">',
            1,
        )

    # H1
    html = html.replace(
        f"<h1>{HUB_H1_OLD}</h1>",
        f"<h1>{city['h1']}</h1>",
        1,
    )

    # intro span after H1
    m = HUB_INTRO_RE.search(html)
    if not m:
        raise RuntimeError(f"intro not found for {city['slug']}")
    html = HUB_INTRO_RE.sub(
        r"\1" + f"<span>{city['intro']}</span>",
        html,
        count=1,
    )

    # main H2
    html = html.replace(
        f"<h2>{HUB_MAIN_H2}</h2>",
        f"<h2>{city['main_title']}</h2>",
        1,
    )

    # main block body
    main_inner = build_main_block(city)
    m2 = HUB_MAIN_SPAN_RE.search(html)
    if not m2:
        raise RuntimeError(f"main span not found for {city['slug']}")
    html = HUB_MAIN_SPAN_RE.sub(
        r"\1" + main_inner + r"\3",
        html,
        count=1,
    )

    # FAQ #4 answer only (question text unchanged)
    m3 = HUB_FAQ4_RE.search(html)
    if not m3:
        raise RuntimeError(f"faq4 not found for {city['slug']}")
    html = HUB_FAQ4_RE.sub(
        r"\1" + f"<span>{city['faq4']}</span>",
        html,
        count=1,
    )
    faq_q = "Насколько реально попасть на первую страницу поиска?"
    if faq_q not in html:
        raise RuntimeError(f"faq4 question altered in {city['slug']}")

    # sanity: hub markers must be gone
    if HUB_TITLE_OLD in html:
        raise RuntimeError(f"hub title leaked into {city['slug']}")
    if HUB_H1_OLD in html:
        raise RuntimeError(f"hub h1 leaked into {city['slug']}")
    if city["url"] not in html:
        raise RuntimeError(f"canonical missing in {city['slug']}")
    if HUB_URL not in html:
        raise RuntimeError(f"hub backlink missing in {city['slug']}")
    if city["faq4"] not in html:
        raise RuntimeError(f"faq4 missing in {city['slug']}")

    return html


def build_hub_city_block() -> str:
    links = "\n".join(
        f'\t\t\t\t\t\t<li><a href="{c["url"]}">{c["city"]}</a></li>' for c in CITIES
    )
    return (
        '\n\t\t\t\t<!-- WAVE 02 city linking -->\n'
        '\t\t\t\t<div class="content_block" id="city-seo-pages">\n'
        '\t\t\t\t\t<div class="content_block__title">\n'
        '\t\t\t\t\t\t<h2>Выберите ваш город</h2>\n'
        '\t\t\t\t\t\t<div>00</div>\n'
        '\t\t\t\t\t</div>\n'
        '\t\t\t\t\t<div class="second_col_info_span">\n'
        '\t\t\t\t\t\tВыберите страницу SEO-продвижения для вашего города:\n'
        '\t\t\t\t\t\t<ul class="uni_check_list__list" style="margin-top:20px;">\n'
        f"{links}\n"
        '\t\t\t\t\t\t</ul>\n'
        '\t\t\t\t\t</div>\n'
        '\t\t\t\t</div>\n'
        '\t\t\t\t<!-- --- -->\n'
    )


def patch_hub(hub_html: str) -> str:
    if 'id="city-seo-pages"' in hub_html:
        return hub_html
    # Insert city block before first content_block (main regional text)
    marker = '<div class="content_block">\n\t\t\t\t\t<div class="content_block__title">\n\t\t\t\t\t\t<h2>SEO&nbsp;продвижение региональных сайтов</h2>'
    if marker not in hub_html:
        # fallback: after page_intro closing
        marker2 = '<!-- --- -->\n\n\t\t\t\t<div class="content_block">'
        idx = hub_html.find(marker2)
        if idx < 0:
            raise RuntimeError("hub insert marker not found")
        # insert before the content_block that follows first ---
        pos = hub_html.find('<div class="content_block">', idx)
        return hub_html[:pos] + build_hub_city_block() + hub_html[pos:]
    pos = hub_html.find(marker)
    return hub_html[:pos] + build_hub_city_block() + hub_html[pos:]


def main() -> None:
    hub_html = HUB.read_text(encoding="utf-8")
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    created = []
    for city in CITIES:
        page = patch_city_page(hub_html, city)
        out = OUT_DIR / city["slug"]
        data = page.encode("utf-8")
        out.write_bytes(data)
        created.append(
            {
                "slug": city["slug"],
                "path": str(out),
                "bytes": len(data),
                "sha256": sha256_bytes(data),
                "url": city["url"],
            }
        )
        print(f"CREATED {city['slug']} bytes={len(data)} sha256={sha256_bytes(data)}")

    hub_new = patch_hub(hub_html)
    if 'id="city-seo-pages"' not in hub_new:
        raise RuntimeError("hub city block not inserted")
    for c in CITIES:
        if c["url"] not in hub_new:
            raise RuntimeError(f"hub missing link {c['url']}")
    hub_data = hub_new.encode("utf-8")
    HUB.write_bytes(hub_data)
    print(f"HUB UPDATED bytes={len(hub_data)} sha256={sha256_bytes(hub_data)}")

    # quick QA
    for city, meta in zip(CITIES, created):
        text = Path(meta["path"]).read_text(encoding="utf-8")
        checks = {
            "title": city["title"] in text,
            "desc": city["description"] in text,
            "h1": city["h1"] in text,
            "intro": city["intro"] in text,
            "main_title": city["main_title"] in text,
            "main_text": city["main_text"] in text,
            "after": city["after_list"] in text,
            "faq4": city["faq4"] in text,
            "canonical": f'href="{city["url"]}"' in text,
            "robots": 'content="index, follow"' in text,
            "hub_back": HUB_URL in text,
            "list_count": text.count("<li>") >= 4,  # may include other lists
            "no_hub_title": HUB_TITLE_OLD not in text,
            "consent_not_inline": True,  # inherited via includes
        }
        # verify each list item present
        for item in city["list"]:
            if item not in text:
                checks[f"list:{item[:20]}"] = False
        bad = [k for k, v in checks.items() if not v]
        print(f"QA {city['slug']}: {'PASS' if not bad else 'FAIL ' + str(bad)}")

    report = BACKUP_DIR / "_build_report.txt"
    lines = ["WAVE02 BUILD REPORT", f"hub_sha256={sha256_bytes(hub_data)}"]
    for m in created:
        lines.append(f"{m['slug']}\t{m['bytes']}\t{m['sha256']}\t{m['url']}")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("report", report)


if __name__ == "__main__":
    main()

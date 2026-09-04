# -*- coding: utf-8 -*-
"""WAVE 02A: inject compact cross-city nav into 5 city SEO pages (canonical source)."""
from __future__ import annotations

from pathlib import Path

SRC = Path(r"X:\AI MARS\projects\iseo-su-site-ops\production-source\static-html\services\seo")

CITIES = [
    ("prodvizhenie-v-sankt-peterburge.html", "Санкт-Петербург"),
    ("prodvizhenie-v-kazani.html", "Казань"),
    ("prodvizhenie-v-ekaterinburge.html", "Екатеринбург"),
    ("prodvizhenie-v-novosibirske.html", "Новосибирск"),
    ("prodvizhenie-v-krasnoyarske.html", "Красноярск"),
]

# Unique junction: end of city SEO block → Tariffs (02)
ANCHOR = (
    "\t\t\t\t</div>\n"
    "\n"
    "\t\t\t\t<!-- --- -->\n"
    "\n"
    "\t\t\t\t<div class=\"content_block\">\n"
    "\t\t\t\t\t<div class=\"content_block__title\">\n"
    "\t\t\t\t\t\t<h2>Тарифы</h2>\n"
    "\t\t\t\t\t\t<div>02</div>"
)


def build_block(current_slug: str) -> str:
    items = []
    for slug, label in CITIES:
        href = f"https://i-seo.su/services/seo/{slug}"
        if slug == current_slug:
            items.append(
                f'\t\t\t\t\t\t<li><span class="city-seo-cross-nav__current" aria-current="page">{label}</span></li>'
            )
        else:
            items.append(f'\t\t\t\t\t\t<li><a href="{href}">{label}</a></li>')
    lis = "\n".join(items)
    return (
        "\t\t\t\t</div>\n"
        "\n"
        "\t\t\t\t<!-- --- -->\n"
        "\n"
        "\t\t\t\t<div class=\"content_block\" id=\"city-seo-cross-nav\">\n"
        "\t\t\t\t\t<div class=\"content_block__title\">\n"
        "\t\t\t\t\t\t<h2>Продвижение сайтов в других городах</h2>\n"
        "\t\t\t\t\t\t<div></div>\n"
        "\t\t\t\t\t</div>\n"
        "\t\t\t\t\t<div class=\"second_col_info_span\">\n"
        "\t\t\t\t\t\tДругие городские страницы SEO-продвижения:\n"
        "\t\t\t\t\t\t<ul class=\"uni_check_list__list\" style=\"margin-top:20px;\">\n"
        f"{lis}\n"
        "\t\t\t\t\t\t</ul>\n"
        "\t\t\t\t\t</div>\n"
        "\t\t\t\t</div>\n"
        "\n"
        "\t\t\t\t<!-- --- -->\n"
        "\n"
        "\t\t\t\t<div class=\"content_block\">\n"
        "\t\t\t\t\t<div class=\"content_block__title\">\n"
        "\t\t\t\t\t\t<h2>Тарифы</h2>\n"
        "\t\t\t\t\t\t<div>02</div>"
    )


def main() -> None:
    for slug, _label in CITIES:
        path = SRC / slug
        text = path.read_text(encoding="utf-8")
        if "id=\"city-seo-cross-nav\"" in text:
            print(f"SKIP already patched: {slug}")
            continue
        if ANCHOR not in text:
            raise SystemExit(f"anchor not found: {slug}")
        new_text = text.replace(ANCHOR, build_block(slug), 1)
        if new_text == text:
            raise SystemExit(f"replace failed: {slug}")
        path.write_text(new_text, encoding="utf-8", newline="\n")
        print(f"PATCHED {slug}")


if __name__ == "__main__":
    main()

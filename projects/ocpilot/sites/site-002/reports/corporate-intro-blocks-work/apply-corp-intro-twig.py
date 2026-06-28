#!/usr/bin/env python3
"""Build patched corporate page twigs with zpm-corp-intro blocks."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CAPTURE = ROOT.parent / "corporate-intro-images-work" / "live-capture"
CTA_WORK = ROOT.parent / "corp-cta-v2-work"

INTRO_PAGES = {
    "delivery": {
        "remote": "catalog/view/theme/default/template/information/delivery.twig",
        "source": CAPTURE / "catalog__view__theme__default__template__information__delivery.twig",
        "image": "delivery-intro.jpg",
        "alt": "Подготовка оборудования к отправке",
    },
    "payment": {
        "remote": "catalog/view/theme/default/template/information/payment.twig",
        "source": CAPTURE / "catalog__view__theme__default__template__information__payment.twig",
        "image": "payment-intro.jpg",
        "alt": "Согласование заказа и документов",
    },
    "guarantee": {
        "remote": "catalog/view/theme/default/template/information/guarantee.twig",
        "source": CAPTURE / "catalog__view__theme__default__template__information__guarantee.twig",
        "image": "warranty-intro.jpg",
        "alt": "Проверка оборудования сервисным инженером",
    },
    "dealers": {
        "remote": "catalog/view/theme/default/template/information/dealers.twig",
        "source": CAPTURE / "catalog__view__theme__default__template__information__dealers.twig",
        "image": "dealers-intro.jpg",
        "alt": "Деловая встреча с партнёром",
    },
    "custom_equipment": {
        "remote": "catalog/view/theme/default/template/information/custom_equipment.twig",
        "source": CTA_WORK / "custom_equipment.twig",
        "image": "custom-intro.jpg",
        "alt": "Проектирование оборудования на заказ",
    },
}

OLD_LEAD = re.compile(
    r'  <section class="zpm-corp-page-lead" aria-label="Вводная информация">\s*'
    r'<div class="container zpm-corp-page-lead__body">\s*'
    r"\{\{ page_lead\|raw \}\}\s*"
    r"</div>\s*"
    r"</section>",
    re.MULTILINE,
)


def intro_block(image: str, alt: str, body: str) -> str:
    return f"""  <section class="zpm-corp-page-lead zpm-corp-intro" aria-label="Вводная информация">
    <div class="container">
      <div class="zpm-corp-intro__grid">
        <div class="zpm-corp-intro__media">
          <img src="/assets/img/corporate/{image}" alt="{alt}" loading="lazy" />
        </div>
        <div class="zpm-corp-intro__body zpm-corp-page-lead__body">
{body}
        </div>
      </div>
    </div>
  </section>"""


def patch_page_lead_page(meta: dict) -> str:
    src = meta["source"].read_text(encoding="utf-8")
    if "zpm-corp-intro" in src:
        return src
    body = "          {{ page_lead|raw }}"
    block = intro_block(meta["image"], meta["alt"], body)
    patched, count = OLD_LEAD.subn(block, src, count=1)
    if count != 1:
        raise RuntimeError(f"Lead block not found in {meta['source']}")
    return patched


def patch_about() -> str:
    src = (CTA_WORK / "about.twig").read_text(encoding="utf-8")
    if "zpm-corp-intro" in src:
        return src
    company_text_match = re.search(
        r'(<p class="zpm-about-company__text">.*?</p>)', src, re.DOTALL
    )
    if not company_text_match:
        raise RuntimeError("about company text paragraph not found")
    company_para = company_text_match.group(1)
    src = src.replace(company_para + "\n", "", 1)
    body = "          " + company_para.strip()
    block = intro_block("about-intro.jpg", "Производственный цех ЗПМ", body)
    marker = "  </section>\n\n  {# §02 — About company + proof cards #}"
    if marker not in src:
        raise RuntimeError("about hero end marker not found")
    return src.replace(marker, "  </section>\n\n" + block + "\n\n  {# §02 — About company + proof cards #}", 1)


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    about_out = ROOT / "about.twig"
    about_out.write_text(patch_about(), encoding="utf-8")
    for key, meta in INTRO_PAGES.items():
        out = ROOT / f"{key}.twig"
        out.write_text(patch_page_lead_page(meta), encoding="utf-8")
    print("Wrote patched twigs:", sorted(p.name for p in ROOT.glob("*.twig")))


if __name__ == "__main__":
    main()

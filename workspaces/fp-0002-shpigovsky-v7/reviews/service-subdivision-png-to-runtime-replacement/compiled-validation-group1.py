"""Compiled validation for GROUP 1."""
import re
from pathlib import Path

dist = Path(__file__).resolve().parents[2] / "dist" / "usluga-podrazdel-v1.html"
html = dist.read_text(encoding="utf-8")

checks = {
    "intro_count": html.count("service-subdivision-intro-v1"),
    "procedure_count": html.count("service-subdivision-procedure-v1"),
    "wrong_intro_heading": html.count("Шпиговский дом — восстановление с уважением к личности")
        + html.count("Шпиговский дом&nbsp;&mdash; восстановление"),
    "dependencies_section": html.count('id="service-subdivision-dependencies"'),
    "rehab_row": html.count(">Реабилитация<"),
    "nature_section": html.count('id="service-subdivision-nature"'),
    "neurobiology": html.count("Нейробиология"),
    "genotyping_heading": html.count(">Генотипирование<"),
    "genotyping_link": html.count("Подробнее о&nbsp;генотипировании"),
    "lifebuoy": html.lower().count("lifebuoy") + html.count("спасатель"),
    "footer": html.count("<footer"),
    "modal": html.count("data-modal-open"),
}

rows = re.findall(
    r'services-category-section-v2__service-name">([^<]+)</span>',
    html,
)
dep_block = html.split('id="service-subdivision-dependencies"')[1].split('id="service-subdivision-nature"')[0]
dep_rows = re.findall(
    r'services-category-section-v2__service-name">([^<]+)</span>',
    dep_block,
)
checks["dependencies_rows"] = len(dep_rows)
checks["dependency_row_labels"] = dep_rows
checks["dependencies_lead"] = dep_block.count("services-category-section-v2__lead")
checks["dependencies_cta"] = dep_block.count("services-category-section-v2__cta")
checks["nature_lead"] = html.split('id="service-subdivision-nature"')[1].split("service-subdivision-first-cta")[0].count("services-category-section-v2__lead")

ids = re.findall(r'\bid="([^"]+)"', html)
from collections import Counter
dupes = [k for k, v in Counter(ids).items() if v > 1]
checks["duplicate_ids"] = len(dupes)
checks["duplicate_id_list"] = dupes

anchors = re.findall(r'href="#([^"]+)"', html)
subnav_block = html.split("services-page-subnav")[1].split("</nav>")[0] if "services-page-subnav" in html else ""
subnav_anchors = re.findall(r'href="#([^"]+)"', subnav_block)
orphans = [a for a in subnav_anchors if f'id="{a}"' not in html]
checks["orphan_anchors"] = len(orphans)
checks["orphan_anchor_list"] = orphans
checks["placeholder_hrefs"] = html.count('href="#"')

for k, v in checks.items():
    print(f"{k}: {v}")

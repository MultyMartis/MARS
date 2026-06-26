"""Compiled validation for GROUP 2."""
import re
from collections import Counter
from pathlib import Path

dist = Path(__file__).resolve().parents[2] / "dist" / "usluga-podrazdel-v1.html"
html = dist.read_text(encoding="utf-8")

program_block = html.split('class="services-program-v2 services-program-v2--subdivision')[1].split('id="service-subdivision-stages"')[0]
program_head_links = len(re.findall(r'<a class="services-program-v2__head-link"', program_block))
program_foot_links = len(re.findall(r'<a class="services-program-v2__foot-link"', program_block))
card_titles = re.findall(r"services-program-v2__item-title\">([^<]+)</h3>", program_block)

checks = {
    "cta_01_section": html.count('id="service-subdivision-start"'),
    "cta_01_modal_source": html.count('data-modal-source="service-subdivision-cta-01"'),
    "cta_01_meeting_title": html.count("Запишитесь на&nbsp;встречу"),
    "program_section": html.count('id="service-subdivision-program"'),
    "program_card_count": len(card_titles),
    "program_card_titles": card_titles,
    "program_head_link": program_head_links,
    "program_foot_link": program_foot_links,
    "program_embedded_cta": program_block.count("services-program-v2__cta-band"),
    "program_lorem_lead": program_block.count("services-program-v2__lead"),
    "program_production_intro": program_block.count("Каждый человек приходит"),
    "second_cta_section": html.count('id="service-subdivision-second-cta"'),
    "second_cta_lorem_intro": html.count("service-subdivision-second-cta-v1__intro"),
    "dependencies_section": html.count('id="service-subdivision-dependencies"'),
    "nature_section": html.count('id="service-subdivision-nature"'),
    "lifebuoy": html.lower().count("lifebuoy") + html.count("спасатель"),
    "footer": html.count("<footer"),
    "modal_open": html.count('data-modal-open="consultation"'),
    "placeholder_hrefs": html.count('href="#"'),
}

ids = re.findall(r'\bid="([^"]+)"', html)
dupes = [k for k, v in Counter(ids).items() if v > 1]
checks["duplicate_ids"] = len(dupes)
checks["duplicate_id_list"] = dupes

for k, v in checks.items():
    print(f"{k}: {v}")

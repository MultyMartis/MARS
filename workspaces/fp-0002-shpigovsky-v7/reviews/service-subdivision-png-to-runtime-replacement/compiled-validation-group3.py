"""Compiled validation for GROUP 3."""
import re
from collections import Counter
from pathlib import Path

dist = Path(__file__).resolve().parents[2] / "dist" / "usluga-podrazdel-v1.html"
html = dist.read_text(encoding="utf-8")

stages_start = html.index('id="service-subdivision-stages"')
team_start = html.index('id="service-subdivision-team-stats"')
stages_block = html[stages_start:team_start]

step_titles = re.findall(r"home-rehabilitation-requirements__step-title\">([^<]+)</h3>", stages_block)
support_items = re.findall(r"home-rehabilitation-requirements__support-item\">([^<]+)</li>", stages_block)

checks = {
    "rehabilitation_section": html.count('id="service-subdivision-stages"'),
    "heading_count": stages_block.count('id="service-subdivision-stages-heading"'),
    "stage_count": len(step_titles),
    "stage_titles": step_titles,
    "stage_order": [t[:20] for t in step_titles],
    "empty_stage_descriptions": stages_block.count('home-rehabilitation-requirements__step-text"></p>'),
    "support_block_count": stages_block.count("home-rehabilitation-requirements__support"),
    "support_item_count": len(support_items),
    "support_items": support_items,
    "cta_in_stages": stages_block.count("service-subdivision-stages-v1__cta"),
    "cta_guest_visit_title": stages_block.count("Запишитесь на&nbsp;гостевой визит"),
    "cta_modal_source": stages_block.count('data-modal-source="service-subdivision-stages-cta-v1"'),
    "wrong_team_inside_scope": stages_block.count('id="service-subdivision-team-stats"'),
    "dependencies_section": html.count('id="service-subdivision-dependencies"'),
    "nature_section": html.count('id="service-subdivision-nature"'),
    "program_section": html.count('id="service-subdivision-program"'),
    "cta_01_section": html.count('id="service-subdivision-start"'),
    "second_cta_section": html.count('id="service-subdivision-second-cta"'),
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

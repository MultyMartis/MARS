"""Compiled/browser validation for GROUP 4."""
from pathlib import Path
import json
import re

ws = Path(__file__).resolve().parents[2]
html = (ws / "dist" / "usluga-podrazdel-v1.html").read_text(encoding="utf-8")

approach_start = html.index('id="service-subdivision-approach"')
gallery_marker = 'service-subdivision-approach-v1--gallery-only'
gallery_start = html.index(gallery_marker)
group4_block = html[approach_start:gallery_start]

results = {
    "group1_dependencies": html.count('id="service-subdivision-dependencies"'),
    "group1_nature": html.count('id="service-subdivision-nature"'),
    "group2_cta01": html.count('id="service-subdivision-start"'),
    "group2_program": html.count('id="service-subdivision-program"'),
    "group3_stages": html.count('id="service-subdivision-stages"'),
    "group3_stage_items": html.count("home-rehabilitation-requirements__step-number"),
    "group3_guest_cta": html.count("Запишитесь на&nbsp;гостевой визит"),
    "group3_support_items": html.count("home-rehabilitation-requirements__support-item"),
    "group4_section_count": html.count('id="service-subdivision-approach"'),
    "corridor_image_count": group4_block.count("service-subdivision-team-stats-v1__corridor-image"),
    "team_image_count": group4_block.count("service-subdivision-team-stats-v1__staff-image"),
    "approach_card_count": group4_block.count('class="home-feature-grid__card service-subdivision-team-stats-v1__approach-card"'),
    "removed_home_stats_titles": group4_block.count("дипломированные специалисты"),
    "removed_old_corridor_class": group4_block.count("service-subdivision-team-stats-v1__photo"),
    "gallery_section_count": html.count("service-subdivision-approach-v1--gallery-only"),
    "gallery_image_count": html[gallery_start:].count("service-subdivision-approach-v1__gallery-image"),
    "duplicate_ids": len(re.findall(r'id="([^"]+)"', html)) - len(set(re.findall(r'id="([^"]+)"', html))),
    "lifebuoy_refs": html.lower().count("lifebuoy"),
    "footer_count": html.count('class="site-footer"'),
    "modal_count": html.count('data-modal-open="consultation"'),
    "group3_stages_count": html.count('id="service-subdivision-stages"'),
    "group3_support_count": group4_block.count("home-rehabilitation-requirements__support"),
    "order_corridor_before_team": group4_block.find("corridor-image") < group4_block.find("staff-image"),
    "order_team_before_cards": group4_block.find("staff-image") < group4_block.find("approach-card"),
    "order_cards_before_gallery": html.find("approach-card") < html.find("gallery-only"),
}

out = Path(__file__).parent / "compiled-validation-group4-result.json"
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(results, ensure_ascii=False, indent=2))

"""Compiled DOM validation for SERVICE LEAF GROUP 2."""
import json
import re
from pathlib import Path

html_path = Path(__file__).resolve().parents[2] / "dist" / "usluga-konechnaya-v1.html"
html = html_path.read_text(encoding="utf-8")

def count(pattern, flags=0):
    return len(re.findall(pattern, html, flags))

results = {
    "group1": {
        "header": count(r'<header\b'),
        "hero": count(r'services-inner-hero-v2'),
        "breadcrumbs": count(r'class="breadcrumbs'),
        "subnav": count(r'services-page-subnav'),
        "intro": count(r'service-leaf-intro-v1'),
        "bordered_info": count(r'service-leaf-bordered-info-v1'),
        "cta01": count(r'service-leaf-cta-01-v1'),
    },
    "group2": {
        "signs_section": count(r'service-leaf-signs-v1'),
        "main_heading": count(r'id="service-leaf-signs-heading"'),
        "internal_headings": count(r'<h3\b', re.I) - html.count("visually-hidden"),  # approximate
        "h3_in_signs": len(re.findall(r'service-leaf-signs-v1[\s\S]*?</section>', html, re.I)),
        "paragraphs_in_signs": len(re.findall(r'<p class="service-leaf-signs-v1__', html)),
        "list_count": count(r'<ul class="service-leaf-signs-v1__list"'),
        "list_items": count(r'class="service-leaf-signs-v1__list-item"'),
        "links": count(r'<a[^>]+class="[^"]*service-leaf-signs'),
        "accent_regions": count(r'service-leaf-signs-v1__read-more'),
        "group2_boundary": count(r'SERVICE-LEAF-GROUP-2-BOUNDARY'),
        "wrong_group1_boundary": count(r'SERVICE-LEAF-GROUP-1-BOUNDARY'),
        "next_approach_heading": count(r'Наш подход к лечению алкогольной зависимости'),
    },
    "general": {
        "footer": count(r'<footer\b'),
        "modal": count(r'modal-consultation'),
        "lifebuoy": count(r'lifebuoy', re.I),
        "template_garbage": sum(
            count(p) for p in [r'else \{', r'@@if', r'@@else', r'undefined', r'\[object Object\]']
        ),
    },
}

# fix h3 count in signs only
signs_block = re.search(r'<section class="service-leaf-signs-v1"[\s\S]*?</section>', html)
if signs_block:
    block = signs_block.group(0)
    results["group2"]["paragraphs_in_signs"] = len(re.findall(r'<p class="service-leaf-signs-v1__', block))
    results["group2"]["internal_headings"] = len(re.findall(r'<h3\b', block, re.I))
    results["group2"]["links"] = len(re.findall(r'<a\b', block, re.I))

out = Path(__file__).parent / "qa-results.json"
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(results, ensure_ascii=False, indent=2))

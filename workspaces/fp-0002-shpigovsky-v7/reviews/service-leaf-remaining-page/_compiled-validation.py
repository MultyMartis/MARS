"""Compiled output validation for SERVICE LEAF full page."""
import json
import re
from pathlib import Path

dist = Path(__file__).resolve().parents[2] / "dist" / "usluga-konechnaya-v1.html"
text = dist.read_text(encoding="utf-8")

ids = re.findall(r'\bid="([^"]+)"', text)
id_counts = {}
for i in ids:
    id_counts[i] = id_counts.get(i, 0) + 1
duplicate_ids = {k: v for k, v in id_counts.items() if v > 1}

subnav_hrefs = re.findall(r'services-page-subnav__link[^>]*href="([^"]+)"', text)
anchor_targets = [h[1:] for h in subnav_hrefs if h.startswith("#")]

results = {
    "header": len(re.findall(r'<header class="site-header"', text)),
    "hero": len(re.findall(r'<section class="services-inner-hero-v2"', text)),
    "breadcrumbs": len(re.findall(r'<nav class="breadcrumbs"', text)),
    "subnav": len(re.findall(r'<nav class="services-page-subnav"', text)),
    "group1_intro": len(re.findall(r'<section class="service-leaf-intro-v1"', text)),
    "group1_bordered": len(re.findall(r'<section class="service-leaf-bordered-info-v1"', text)),
    "cta01": len(re.findall(r'<section class="service-leaf-cta-01-v1"', text)),
    "group2_signs": len(re.findall(r'<section class="service-leaf-signs-v1"', text)),
    "group3_approach": len(re.findall(r'<section class="service-leaf-approach-v1"', text)),
    "group3_team_image": text.count("service-leaf-approach-v1__staff-image"),
    "group3_cards": len(re.findall(r'class="home-feature-grid__card service-leaf-approach-v1__approach-card"', text)),
    "clinic_landscape": text.count("service-leaf-landscape-v1"),
    "program": text.count('id="service-leaf-program"'),
    "program_cards": len(re.findall(r'services-program-v2__item"', text)),
    "rehab_section": len(re.findall(r'<section class="service-leaf-stages-v1"', text)),
    "stages": len(re.findall(r'home-rehabilitation-requirements__step"', text)),
    "stage_cta": text.count("service-leaf-stages-cta-v1"),
    "support_block": len(
        re.findall(
            r'<section class="service-leaf-stages-v1"[\s\S]*?class="home-rehabilitation-requirements__support service-leaf-stages-v1__support"',
            text,
        )
    ),
    "support_items": len(re.findall(r'home-rehabilitation-requirements__support-item', text)),
    "corridor": len(re.findall(r'<section class="service-leaf-corridor-v1"', text)),
    "specialists": text.count('id="service-leaf-specialists"'),
    "founder": len(re.findall(r'<section class="home-founder-quote', text)),
    "comfort": text.count('id="service-leaf-comfort"'),
    "reviews": text.count('id="service-leaf-reviews"'),
    "faq": text.count('id="service-leaf-faq"'),
    "final_form": text.count('id="service-leaf-final-form-heading"'),
    "footer": len(re.findall(r'<footer class="site-footer"', text)),
    "modal": text.count('data-modal="consultation"'),
    "duplicate_ids": duplicate_ids,
    "orphan_anchors": [a for a in anchor_targets if f'id="{a}"' not in text],
    "lifebuoy_refs": len(re.findall(r"lifebuoy", text, re.I)),
    "template_garbage": len(re.findall(r"\[object Object\]|@@if|@@else|undefined|null", text)),
}

checks = {
    "header_eq_1": results["header"] == 1,
    "hero_eq_1": results["hero"] == 1,
    "group1_eq_1": all(
        results[k] == 1
        for k in ("group1_intro", "group1_bordered", "cta01", "breadcrumbs", "subnav")
    ),
    "group2_eq_1": results["group2_signs"] == 1,
    "group3_eq_1": results["group3_approach"] == 1 and results["group3_team_image"] == 1,
    "group3_cards_eq_4": results["group3_cards"] == 4,
    "landscape_eq_1": results["clinic_landscape"] == 1,
    "program_eq_1": results["program"] == 1,
    "program_cards_eq_4": results["program_cards"] == 4,
    "group5_eq_1": results["rehab_section"] == 1,
    "stages_eq_4": results["stages"] == 4,
    "support_eq_1": results["support_block"] == 1,
    "support_items_eq_4": results["support_items"] == 4,
    "corridor_eq_1": results["corridor"] == 1,
    "shared_lower_eq_1": all(
        results[k] == 1
        for k in ("specialists", "founder", "comfort", "reviews", "faq")
    ),
    "final_form_present": results["final_form"] >= 1,
    "footer_eq_1": results["footer"] == 1,
    "modal_eq_1": results["modal"] == 1,
    "duplicate_ids_zero": len(duplicate_ids) == 0,
    "orphan_anchors_zero": len(results["orphan_anchors"]) == 0,
    "lifebuoy_zero": results["lifebuoy_refs"] == 0,
    "template_garbage_zero": results["template_garbage"] == 0,
}

results["checks"] = checks
results["pass"] = all(checks.values())

out = Path(__file__).parent / "compiled-validation.json"
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"pass": results["pass"], "checks": checks, "counts": {k: results[k] for k in results if k not in ("checks", "duplicate_ids", "orphan_anchors")}}, ensure_ascii=False, indent=2))

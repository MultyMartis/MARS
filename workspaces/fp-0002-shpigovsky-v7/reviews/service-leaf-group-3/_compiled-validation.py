"""Compiled validation for GROUP 3."""
import re
from pathlib import Path

html = Path(__file__).parents[2] / "dist" / "usluga-konechnaya-v1.html"
text = html.read_text(encoding="utf-8")


def count(pattern):
    return len(re.findall(pattern, text, flags=re.I))


checks = {
    "group1_hero": count(r"Центр лечения алкогольной зависимости"),
    "group2_signs_section": len(re.findall(r'<section class="service-leaf-signs-v1"', text)),
    "group3_approach_section": len(re.findall(r'<section class="service-leaf-approach-v1"', text)),
    "group3_heading": count(r"Наш подход к&nbsp;лечению алкогольной зависимости"),
    "group3_team_images": text.count("shpigovsky-staff-group.webp"),
    "group3_approach_cards": len(re.findall(r'class="[^"]*service-leaf-approach-v1__approach-card"', text)),
    "group3_landscape_images": text.count("shpigovsky-clinic-landscape.webp"),
    "group3_boundary": text.count("SERVICE-LEAF-GROUP-3-BOUNDARY"),
    "program_section": text.count('id="service-leaf-program"'),
    "program_heading": count(r"Наша программа включает 4"),
    "footer": text.count("<footer"),
    "modal": text.count("modal-consultation"),
    "lifebuoy": text.count("lifebuoy"),
    "duplicate_service_leaf_approach_id": len(re.findall(r'id="service-leaf-approach"', text)),
}

print(checks)
for k, v in checks.items():
    ok = True
    if k == "group3_approach_section" and v != 1:
        ok = False
    if k == "group3_approach_cards" and v != 4:
        ok = False
    if k == "program_section" and v != 0:
        ok = False
    if k == "lifebuoy" and v != 0:
        ok = False
    if k == "duplicate_service_leaf_approach_id" and v != 1:
        ok = False
    print(k, v, "PASS" if ok else "FAIL")

"""Compiled validation for GROUP 4."""
import re
from pathlib import Path

html = Path(__file__).parents[2] / "dist" / "usluga-konechnaya-v1.html"
text = html.read_text(encoding="utf-8")


def count(pattern):
    return len(re.findall(pattern, text, flags=re.I))


checks = {
    "group3_approach_section": len(re.findall(r'<section class="service-leaf-approach-v1"', text)),
    "group3_landscape": text.count("service-leaf-landscape-v1"),
    "group3_boundary": text.count("SERVICE-LEAF-GROUP-3-BOUNDARY"),
    "program_section": text.count('id="service-leaf-program"'),
    "program_heading": count(r"Наша программа включает 4"),
    "program_cards": len(re.findall(r'class="services-program-v2__item"', text)),
    "program_genotyping": text.count("program-genotyping.webp"),
    "program_neuro": text.count("program-neuropsychology.webp"),
    "program_psycho": text.count("program-psychocorrection.webp"),
    "program_kinesio": text.count("program-kinesiotherapy.webp"),
    "group4_boundary": text.count("SERVICE-LEAF-GROUP-4-BOUNDARY"),
    "rehab_heading": count(r"Что нужно для прохождения реабилитации"),
    "embedded_cta_band_in_program": len(
        re.findall(
            r'id="service-leaf-program"[\s\S]*?services-program-v2__cta-band',
            text,
        )
    ),
    "lifebuoy": text.count("lifebuoy"),
    "footer": text.count("<footer"),
    "modal": text.count("modal-consultation"),
}

print(checks)
rules = {
    "group3_approach_section": 1,
    "program_section": 1,
    "program_cards": 4,
    "group4_boundary": 1,
    "group3_boundary": 0,
    "rehab_heading": 0,
    "embedded_cta_band_in_program": 0,
    "lifebuoy": 0,
}
for k, expected in rules.items():
    print(k, checks[k], "PASS" if checks[k] == expected else "FAIL")

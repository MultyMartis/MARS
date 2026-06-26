"""Compiled validation for service subdivision final corrections."""
import re
import subprocess
from pathlib import Path

ws = Path(r"C:\MARS Phenix\AI MARS\workspaces\fp-0002-shpigovsky-v7")
html_path = ws / "dist" / "usluga-podrazdel-v1.html"
html = html_path.read_text(encoding="utf-8")

checks = {
    "approach_v1_count": html.count("service-subdivision-approach-v1"),
    "home_clinic_landscape_count": html.count("home-clinic-landscape"),
    "else_brace_count": len(re.findall(r"else\s*\{", html)),
    "at_else_count": html.count("@@else"),
    "dependencies_section": html.count("service-subdivision-dependencies"),
    "dependencies_rows": html.count('class="services-category-section-v2__service"'),
    "specialists": html.count('id="service-subdivision-specialists"'),
    "founder": html.count("home-founder-quote"),
    "comfort": html.count('id="service-subdivision-comfort"'),
    "reviews": html.count("home-reviews"),
    "faq": html.count('id="service-subdivision-faq"'),
    "final_form": html.count('id="service-subdivision-final-form-heading"'),
    "footer": html.count('class="site-footer"'),
    "modal": html.count("modal-consultation"),
    "lifebuoy": html.count("lifebuoy"),
}

# GROUP markers
group_markers = {
    "g1_dependencies": "service-subdivision-dependencies-v1",
    "g2_nature": "service-subdivision-nature-v1",
    "g3_stages": "service-subdivision-stages-v1",
    "g4_team": "service-subdivision-team-stats-v1",
    "g4_approach_cards": "service-subdivision-team-stats-v1__approach-cards",
}
for k, v in group_markers.items():
    checks[k] = html.count(v)

# duplicate ids
ids = re.findall(r'\bid="([^"]+)"', html)
from collections import Counter
dupes = [i for i, c in Counter(ids).items() if c > 1]
checks["duplicate_ids"] = len(dupes)
checks["duplicate_id_list"] = dupes[:10]

# regression pages
for page in ["index.html", "uslugi-v2.html", "uslugi-v1.html"]:
    p = ws / "dist" / page
    if p.exists():
        h = p.read_text(encoding="utf-8")
        checks[f"{page}_else"] = len(re.findall(r"else\s*\{", h))
        checks[f"{page}_at_else"] = h.count("@@else")

print("FILE", html_path)
for k, v in checks.items():
    print(f"{k}={v}")

pass_approach = checks["approach_v1_count"] == 0
pass_landscape = checks["home_clinic_landscape_count"] >= 1
pass_else = checks["else_brace_count"] == 0 and checks["at_else_count"] == 0
pass_rows = checks["dependencies_rows"] == 4
print("PASS_APPROACH", pass_approach)
print("PASS_LANDSCAPE", pass_landscape)
print("PASS_ELSE", pass_else)
print("PASS_ROWS", pass_rows)
print("OVERALL", pass_approach and pass_landscape and pass_else and pass_rows)

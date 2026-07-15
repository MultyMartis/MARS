#!/usr/bin/env python3
"""Quick DOM probe for E12 baseline."""
import re
import urllib.request

url = "http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/"
html = urllib.request.urlopen(url, timeout=30).read().decode("utf-8", "replace")
checks = {
    "service-leaf-approach": "service-leaf-approach" in html,
    "service-leaf-start": "service-leaf-start" in html,
    "service-leaf-faq": "service-leaf-faq" in html,
    "shpigovsky-service": "shpigovsky-service" in html,
    "staff-image": "service-leaf-approach-v1__staff-image" in html,
    "stages-lead": "service-leaf-stages-v1__lead" in html,
    "stages-support": "service-leaf-stages-v1__support" in html,
}
sections = re.findall(r'<section[^>]*class="([^"]*)"[^>]*(?:id="([^"]*)")?', html)
print("checks:", checks)
print("section_count:", len(sections))
for cls, sid in sections[:25]:
    print(f"  {sid or '-'} | {cls[:80]}")

for sid in ("service-leaf-approach", "service-leaf-start", "service-leaf-faq"):
    m = re.search(rf'id="{sid}"[^>]*>(.*?)</section>', html, re.S)
    print(f"\n=== {sid} snippet ===")
    print((m.group(1)[:1500] if m else "NOT FOUND"))

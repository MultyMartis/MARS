import json
from pathlib import Path

ROOT = Path(__file__).parent
extract = json.loads((ROOT / "_service-leaf-fig-extract.json").read_text(encoding="utf-8"))

keys = [
    "алкогол",
    "приговор",
    "признак",
    "эффектив",
    "комплекс",
    "стоимость",
    "коридор",
    "шпиговск",
    "зависимост",
    "лечение",
    "консультац",
    "гостевой",
]

print("=== KEY DESKTOP TEXTS ===")
for t in extract["desktopTexts"]:
    tx = t["text"].lower()
    if any(k in tx for k in keys) or (len(t["text"]) > 45 and t["depth"] <= 3):
        print(f"{t['id']} d{t['depth']} {t['name']}: {t['text'][:180]}")

y = 0
print("\n=== DESKTOP Y-RANGES ===")
for i, s in enumerate(extract["desktopSections"], 1):
    h = s["h"]
    print(f"{i:02d} Y{y}-{y + h} | {s['name']} | {s['id']}")
    y += h
print("cumulative", y, "frame", extract["desktop"]["h"])

y = 0
print("\n=== MOBILE Y-RANGES ===")
for i, s in enumerate(extract["mobileSections"], 1):
    h = s["h"]
    print(f"{i:02d} Y{y}-{y + h} | {s['name']} | {s['id']}")
    y += h
print("cumulative", y, "frame", extract["mobile"]["h"])

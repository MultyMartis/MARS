#!/usr/bin/env python3
import hashlib
import json
import re
import ssl
import urllib.request
from pathlib import Path

ROOT = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002")
CAP = ROOT / "reports/site-002-operator-manual-polish-01-work/live-capture"
W11 = ROOT / "reports/site-002-visual-polish-pass1.1-work"
W12 = ROOT / "reports/site-002-visual-polish-pass1.2-work"
M913 = ROOT / "reports/m9.13-restore-work"
M04A = ROOT / "reports/m9.8.9-04a-work/live-capture"


def sha(path: Path | None) -> str | None:
    if path is None or not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def live_path(remote: str) -> Path:
    return CAP / remote.replace("/", "__")


refs: list[tuple[str, Path, str]] = [
    ("assets/css/style.css", W12 / "style.css", "pass1.2-work"),
    ("assets/css/style.css", W11 / "style.css", "pass1.1-work"),
    ("assets/js/main.js", M04A / "assets__js__main.js", "04a-capture"),
    ("assets/js/main.js", ROOT / "backups/main.js.pre-m9.18-custom.bak", "pre-m9.18"),
    (
        "catalog/view/theme/default/template/information/about.twig",
        M913 / "live-capture/catalog__view__theme__default__template__information__about.twig",
        "m913-restore",
    ),
    (
        "catalog/controller/information/about.php",
        M913 / "live-capture/catalog__controller__information__about.php",
        "m913-restore",
    ),
]

for name in ["delivery", "payment", "guarantee", "dealers", "custom_equipment"]:
    refs.append(
        (
            f"catalog/view/theme/default/template/information/{name}.twig",
            W11 / f"{name}.twig",
            "pass1.1-work",
        )
    )
    refs.append((f"catalog/controller/information/{name}.php", W11 / f"{name}.php", "pass1.1-work"))

changed: dict[str, list[dict]] = {}
same: list[str] = []

for remote, ref_path, label in refs:
    live_sha = sha(live_path(remote))
    ref_sha = sha(ref_path)
    if live_sha is None:
        continue
    if ref_sha is None:
        continue
    if live_sha != ref_sha:
        changed.setdefault(remote, []).append(
            {"label": label, "live_sha256": live_sha, "ref_sha256": ref_sha}
        )
    else:
        same.append(f"{remote} vs {label}")

print("=== CHANGED vs repo references ===")
for remote, items in changed.items():
    print(remote)
    for item in items:
        print(f"  vs {item['label']}")
        print(f"    live {item['live_sha256']}")
        print(f"    ref  {item['ref_sha256']}")

print("\n=== SAME (sample) ===")
for line in same[:8]:
    print(line)

ctx = ssl.create_default_context()
html = urllib.request.urlopen("https://zpm.new-site.space/katalog/stoly/", context=ctx, timeout=20).read().decode(
    "utf-8", "replace"
)
links = sorted(set(re.findall(r'href="(https://zpm\.new-site\.space/katalog/[^"]+)"', html)))
print("\n=== PDP probe ===")
for url in links[:5]:
    try:
        status = urllib.request.urlopen(url, context=ctx, timeout=20).status
        print(status, url)
    except Exception as exc:
        print("ERR", url, exc)

out = {"changed": changed, "same_count": len(same)}
(ROOT / "reports/site-002-operator-manual-polish-01-work/diff-vs-pass12.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
)

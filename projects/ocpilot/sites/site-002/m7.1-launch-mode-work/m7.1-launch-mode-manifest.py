#!/usr/bin/env python3
"""SITE-002 M7.1 Launch Mode — prepare patch manifest (no deploy by default)."""
import hashlib
import json
import os
from datetime import datetime, timezone

BASE = r"C:\AI MARS\projects\ocpilot\sites\site-002\m7.1-launch-mode-work"
PATCH = os.path.join(BASE, "patch")
BACKUP = os.path.join(BASE, "backups")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

REMOTE_MAP = {
    "system/library/zpm/category_visibility.php": "system/library/zpm/category_visibility.php",
    "catalog/controller/product/katalog.php": "catalog/controller/product/katalog.php",
    "catalog/controller/product/category.php": "catalog/controller/product/category.php",
    "catalog/controller/common/header.php": "catalog/controller/common/header.php",
    "catalog/controller/common/footer.php": "catalog/controller/common/footer.php",
    "catalog/controller/common/home.php": "catalog/controller/common/home.php",
    "catalog/view/theme/default/template/common/megamenu.twig": "catalog/view/theme/default/template/common/megamenu.twig",
    "catalog/view/theme/default/template/common/footer.twig": "catalog/view/theme/default/template/common/footer.twig",
    "catalog/view/theme/default/template/sections/catalogsections.twig": "catalog/view/theme/default/template/sections/catalogsections.twig",
    "catalog/view/theme/default/template/sections/offcanvasmenu.twig": "catalog/view/theme/default/template/sections/offcanvasmenu.twig",
}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    manifest = {
        "task": "M7.1 Launch Mode",
        "site": "SITE-002",
        "test_url": "https://zpm.new-site.space/",
        "generated_at_utc": STAMP,
        "deploy": False,
        "files": [],
    }

    for rel in REMOTE_MAP:
        local = os.path.join(PATCH, rel.replace("/", os.sep))
        if not os.path.isfile(local):
            raise SystemExit(f"missing patch file: {local}")
        manifest["files"].append(
            {
                "remote": REMOTE_MAP[rel],
                "local": local,
                "sha256": sha256(local),
                "action": "create" if rel.endswith("category_visibility.php") else "modify",
            }
        )

    out = os.path.join(BACKUP, f"m7.1-launch-mode-manifest-{STAMP}.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(out)
    print(f"files: {len(manifest['files'])}")


if __name__ == "__main__":
    main()

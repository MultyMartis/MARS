#!/usr/bin/env python3
"""Patch corporate page PHP controllers: move pageintro description to page_lead."""
from __future__ import annotations

import re
from pathlib import Path

WORK = Path(__file__).resolve().parent

CONTROLLERS = [
    "delivery.php",
    "payment.php",
    "guarantee.php",
    "dealers.php",
    "custom_equipment.php",
]

DESC_PATTERN = re.compile(
    r"\t\t\$pageintro->description = (?P<desc>.+?);\n\t\t\$this->document->setPageintro",
    re.DOTALL,
)


def main() -> None:
    for name in CONTROLLERS:
        path = WORK / name
        src = path.read_text(encoding="utf-8")
        match = DESC_PATTERN.search(src)
        if not match:
            raise SystemExit(f"{name}: could not find pageintro description block")
        desc = match.group("desc").strip()
        src = DESC_PATTERN.sub(
            "\t\t$this->document->setPageintro",
            src,
            count=1,
        )
        insert = f"\n\t\t$data['page_lead'] = {desc};\n"
        anchor = "\t\t$this->document->setPageintro($pageintro->render());\n"
        if anchor not in src:
            raise SystemExit(f"{name}: setPageintro anchor missing")
        src = src.replace(anchor, anchor + insert, 1)
        path.write_text(src, encoding="utf-8")
        print(f"Patched {name}")


if __name__ == "__main__":
    main()

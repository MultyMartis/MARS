#!/usr/bin/env python3
"""Insert zpm-corp-page-lead block at start of corporate page main."""
from __future__ import annotations

from pathlib import Path

WORK = Path(__file__).resolve().parent

TWIGS = [
    "delivery.twig",
    "payment.twig",
    "guarantee.twig",
    "dealers.twig",
    "custom_equipment.twig",
]

LEAD = """
  <section class="zpm-corp-page-lead" aria-label="Вводная информация">
    <div class="container zpm-corp-page-lead__body">
      {{ page_lead|raw }}
    </div>
  </section>
"""


def main() -> None:
    for name in TWIGS:
        path = WORK / name
        src = path.read_text(encoding="utf-8")
        marker = "\n\n  {#"
        needle = "<main class=\"main zpm-"
        idx = src.find(needle)
        if idx == -1:
            raise SystemExit(f"{name}: main tag not found")
        line_end = src.find(">", idx) + 1
        if "zpm-corp-page-lead" in src:
            print(f"Skip {name} (already patched)")
            continue
        path.write_text(src[:line_end] + LEAD + src[line_end:], encoding="utf-8")
        print(f"Patched {name}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Apply SITE-002 Corporate Pages Visual Polish Pass 1.2 CSS edits in-place."""
from __future__ import annotations

from pathlib import Path

WORK = Path(__file__).resolve().parent
STYLE = WORK / "style.css"

APPEND = """
/* ==========================================================================
   SITE-002 — Corporate Pages Visual Polish Pass 1.2 (VP12-01+)
   Authority: Home page rhythm — no global padding-top:0 resets
   ========================================================================== */

/* VP12-01 — H1-only page intro air (home hero title→lead gap token) */
.page-intro > .container:not(:has(.page-intro__description)) {
  gap: var(--pad-gap);
}

/* VP12-02 — corp lead paragraph rhythm (home dealers text stack) */
.zpm-corp-page-lead__body {
  gap: var(--pad-gap);
}

/* VP12-03 — corp table cell breathing */
.zpm-delivery-carriers__table th,
.zpm-delivery-carriers__table td,
.zpm-payment-methods__table th,
.zpm-payment-methods__table td,
.zpm-warranty-coverage__table th,
.zpm-warranty-coverage__table td,
.zpm-warranty-docs__table th,
.zpm-warranty-docs__table td,
.zpm-dealers-matrix__table th,
.zpm-dealers-matrix__table td,
.zpm-dealers-outcomes__table th,
.zpm-dealers-outcomes__table td,
.zpm-dealers-crosslinks__table th,
.zpm-dealers-crosslinks__table td,
.zpm-custom-tasks__table th,
.zpm-custom-tasks__table td,
.zpm-custom-scope__table th,
.zpm-custom-scope__table td,
.zpm-custom-requirements__table th,
.zpm-custom-requirements__table td,
.zpm-custom-outcomes__table th,
.zpm-custom-outcomes__table td {
  padding: var(--pad-gap) var(--pad-gap);
}

/* VP12-04 — payment proof card internal air (home adv-card text stack) */
.zpm-payment-proof-card {
  gap: var(--pad-gap);
}
"""


def main() -> None:
    css = STYLE.read_text(encoding="utf-8")

    replacements = [
        (
            ".zpm-delivery-point-card {\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n",
            ".zpm-delivery-point-card {\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-delivery-summary__label {\n  margin: 0 0 6px;\n",
            ".zpm-delivery-summary__label {\n  margin: 0 0 var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-delivery-packaging__list {\n  margin: 0 0 var(--pad-gap-mini);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: 6px;\n}",
            ".zpm-delivery-packaging__list {\n  margin: 0 0 var(--pad-gap-mini);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n}",
        ),
        (
            ".zpm-delivery-coverage__factors {\n  margin: 0 0 var(--pad-gap-mini);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: 8px;\n}",
            ".zpm-delivery-coverage__factors {\n  margin: 0 0 var(--pad-gap-mini);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n}",
        ),
        (
            ".zpm-payment-method__list {\n  margin: 0 0 var(--pad-gap-mini);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: 6px;\n",
            ".zpm-payment-method__list {\n  margin: 0 0 var(--pad-gap-mini);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-payment-proof-card {\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n",
            ".zpm-payment-proof-card {\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-payment-legal__label {\n  margin: 0 0 6px;\n",
            ".zpm-payment-legal__label {\n  margin: 0 0 var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-warranty-summary__label {\n  margin: 0 0 6px;\n",
            ".zpm-warranty-summary__label {\n  margin: 0 0 var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-dealers-matrix__tag {\n  display: inline-flex;\n  align-items: center;\n  gap: 6px;\n  margin-bottom: 6px;\n",
            ".zpm-dealers-matrix__tag {\n  display: inline-flex;\n  align-items: center;\n  gap: var(--pad-gap-mini);\n  margin-bottom: var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-dealers-oem-row__grid {\n  display: grid;\n  grid-template-columns: repeat(4, minmax(0, 1fr));\n  gap: var(--pad-gap-line);\n",
            ".zpm-dealers-oem-row__grid {\n  display: grid;\n  grid-template-columns: repeat(4, minmax(0, 1fr));\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-dealers-oem-row__label {\n  margin: 0 0 6px;\n",
            ".zpm-dealers-oem-row__label {\n  margin: 0 0 var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-dealers-chain__node {\n  position: relative;\n  display: flex;\n  align-items: center;\n  gap: 12px;\n  padding: 14px 16px;\n",
            ".zpm-dealers-chain__node {\n  position: relative;\n  display: flex;\n  align-items: center;\n  gap: var(--pad-gap-line);\n  padding: var(--pad-gap) var(--pad-gap-line);\n",
        ),
        (
            ".zpm-dealers-chain__node:not(:last-child)::after {\n  content: \"\";\n  position: absolute;\n  left: 28px;\n  bottom: -12px;\n  width: 2px;\n  height: 12px;\n",
            ".zpm-dealers-chain__node:not(:last-child)::after {\n  content: \"\";\n  position: absolute;\n  left: 28px;\n  bottom: calc(var(--pad-gap-line) * -1);\n  width: 2px;\n  height: var(--pad-gap-line);\n",
        ),
        (
            ".zpm-dealers-chain__node + .zpm-dealers-chain__node {\n  margin-top: 12px;\n}",
            ".zpm-dealers-chain__node + .zpm-dealers-chain__node {\n  margin-top: var(--pad-gap-line);\n}",
        ),
        (
            ".zpm-custom-tasks__tag {\n  display: inline-flex;\n  align-items: center;\n  gap: 6px;\n  margin-bottom: 6px;\n",
            ".zpm-custom-tasks__tag {\n  display: inline-flex;\n  align-items: center;\n  gap: var(--pad-gap-mini);\n  margin-bottom: var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-custom-triggers__list {\n  margin: 0 0 var(--pad-gap);\n  padding-left: 1.25em;\n  display: flex;\n  flex-direction: column;\n  gap: 10px;\n",
            ".zpm-custom-triggers__list {\n  margin: 0 0 var(--pad-gap);\n  padding-left: 1.25em;\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-custom-scope__group ul {\n  margin: 0 0 var(--pad-gap-mini);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: 8px;\n",
            ".zpm-custom-scope__group ul {\n  margin: 0 0 var(--pad-gap-mini);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-custom-oem__stack {\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-line);\n",
            ".zpm-custom-oem__stack {\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-custom-oem__strip-label {\n  margin: 0 0 6px;\n",
            ".zpm-custom-oem__strip-label {\n  margin: 0 0 var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-custom-oem__badge {\n  display: inline-flex;\n  align-items: center;\n  gap: 10px;\n  margin: var(--pad-gap-mini) 0 var(--pad-gap);\n  padding: 10px 14px;\n",
            ".zpm-custom-oem__badge {\n  display: inline-flex;\n  align-items: center;\n  gap: var(--pad-gap-mini);\n  margin: var(--pad-gap-mini) 0 var(--pad-gap);\n  padding: var(--pad-gap-mini) var(--pad-gap-line);\n",
        ),
        (
            ".zpm-custom-oem__proof-strip {\n  display: grid;\n  grid-template-columns: repeat(3, minmax(0, 1fr));\n  gap: var(--pad-gap-line);\n",
            ".zpm-custom-oem__proof-strip {\n  display: grid;\n  grid-template-columns: repeat(3, minmax(0, 1fr));\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-warranty-verification__list {\n  margin: 0 0 var(--pad-gap);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n  max-width: 920px;\n",
            ".zpm-warranty-verification__list {\n  margin: 0 0 var(--pad-gap);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap);\n  max-width: 920px;\n",
        ),
        (
            ".zpm-warranty-outcome__title {\n  margin: 0 0 var(--pad-gap-mini);\n",
            ".zpm-warranty-outcome__title {\n  margin: 0;\n",
        ),
        (
            ".zpm-delivery-outcome__title {\n  margin: 0 0 8px;\n",
            ".zpm-delivery-outcome__title {\n  margin: 0;\n",
        ),
        (
            ".zpm-warranty-outcome {\n  padding: var(--pad-inner);\n  border: 1px solid var(--border-color);\n  border-radius: var(--radius-main);\n  background-color: #fff;\n",
            ".zpm-warranty-outcome {\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n  padding: var(--pad-inner);\n  border: 1px solid var(--border-color);\n  border-radius: var(--radius-main);\n  background-color: #fff;\n",
        ),
        (
            ".zpm-delivery-outcome {\n  padding: var(--pad-inner);\n  border: 1px solid var(--border-color);\n  border-radius: var(--radius-main);\n  background-color: #fff;\n",
            ".zpm-delivery-outcome {\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n  padding: var(--pad-inner);\n  border: 1px solid var(--border-color);\n  border-radius: var(--radius-main);\n  background-color: #fff;\n",
        ),
    ]

    for old, new in replacements:
        if old not in css:
            raise SystemExit(f"Missing expected CSS block:\n{old[:120]}...")
        css = css.replace(old, new, 1)

    if "Corporate Pages Visual Polish Pass 1.2" in css:
        raise SystemExit("Pass 1.2 block already applied")

    css = css.rstrip() + APPEND
    STYLE.write_text(css + "\n", encoding="utf-8")
    print(f"Patched {STYLE} ({STYLE.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

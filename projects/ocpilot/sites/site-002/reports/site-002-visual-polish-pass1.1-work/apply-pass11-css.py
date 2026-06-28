#!/usr/bin/env python3
"""Apply SITE-002 Corporate Pages Visual Polish Pass 1.1 CSS edits in-place."""
from __future__ import annotations

from pathlib import Path

WORK = Path(__file__).resolve().parent
STYLE = WORK / "style.css"

APPEND = """
/* ==========================================================================
   SITE-002 — Corporate Pages Visual Polish Pass 1.1 (VP11-01+)
   Authority: Home page rhythm — no global padding-top:0 resets
   ========================================================================== */

/* VP11-01 — page lead inside main (replaces page-intro__description) */
.zpm-corp-page-lead__body {
  display: flex;
  flex-direction: column;
  gap: var(--pad-gap-mini);
  max-width: 920px;
}

.zpm-corp-page-lead__body p {
  margin: 0;
  font-size: var(--base-Font-size);
  line-height: var(--base-Line-height);
}

/* VP11-02 — delivery point icons aligned with home mini asset scale */
.zpm-delivery-point-card__icon {
  width: var(--img-mini-width);
  height: var(--img-mini-width);
  font-size: 28px;
}

/* VP11-03 — corp FAQ list gap (catalog-faq / commercial-trust card rhythm) */
.zpm-delivery-page .zpm-corp-faq__list,
.zpm-warranty-page .zpm-corp-faq__list,
.zpm-dealers-page .zpm-corp-faq__list,
.zpm-custom-page .zpm-corp-faq__list {
  gap: var(--pad-gap);
}

/* VP11-04 — payment proof cards: home adv-cards density (4-col desktop) */
@media (min-width: 1025px) {
  .zpm-payment-proof__grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: var(--pad-gap);
  }

  .zpm-delivery-summary,
  .zpm-warranty-summary,
  .zpm-payment-legal__facts {
    gap: var(--pad-gap);
  }
}

/* VP11-05 — custom timeline desktop cap (home row4 pattern) */
.zpm-custom-timeline.zpm-corp-timeline {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}
"""


def main() -> None:
    css = STYLE.read_text(encoding="utf-8")

    replacements = [
        (
            ".zpm-delivery-section {\n  padding-top: var(--pad-y);\n}\n",
            "/* VP11: top padding from main > section */\n",
        ),
        (
            ".zpm-payment-section {\n  padding-top: var(--pad-y);\n}\n",
            "/* VP11: top padding from main > section */\n",
        ),
        (
            ".zpm-warranty-section {\n  padding-top: var(--pad-y);\n}\n",
            "/* VP11: top padding from main > section */\n",
        ),
        (
            ".zpm-dealers-section {\n  padding-top: var(--pad-y);\n}\n",
            "/* VP11: top padding from main > section */\n",
        ),
        (
            ".zpm-custom-section {\n  padding-top: var(--pad-y);\n}\n",
            "/* VP11: top padding from main > section */\n",
        ),
        (
            ".zpm-delivery-cta {\n  padding-top: var(--pad-y);\n}\n",
            "/* VP11: top padding from main > section */\n",
        ),
        (
            ".zpm-payment-cta {\n  padding-top: var(--pad-y);\n}\n",
            "/* VP11: top padding from main > section */\n",
        ),
        (
            ".zpm-warranty-cta {\n  padding-top: var(--pad-y);\n}\n",
            "/* VP11: top padding from main > section */\n",
        ),
        (
            ".zpm-dealers-cta {\n  padding-top: var(--pad-y);\n}\n",
            "/* VP11: top padding from main > section */\n",
        ),
        (
            ".zpm-custom-cta {\n  padding-top: var(--pad-y);\n}\n",
            "/* VP11: top padding from main > section */\n",
        ),
        (
            ".zpm-warranty-verification {\n  padding-top: calc(var(--pad-y) * 0.75);\n}\n\n",
            "",
        ),
        (
            ".zpm-dealers-oem-row {\n  padding-top: calc(var(--pad-y) * 0.5);\n  padding-bottom: calc(var(--pad-y) * 0.5);\n}\n\n",
            "/* VP11: OEM row uses main > section vertical rhythm */\n\n",
        ),
        (
            ".zpm-corp-timeline {\n  list-style: none;\n  margin: var(--pad-gap) 0;\n  padding: 0;\n  display: grid;\n  grid-template-columns: repeat(7, minmax(0, 1fr));\n  gap: var(--pad-gap-line);\n",
            ".zpm-corp-timeline {\n  list-style: none;\n  margin: var(--pad-gap) 0;\n  padding: 0;\n  display: grid;\n  grid-template-columns: repeat(7, minmax(0, 1fr));\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-corp-timeline__step {\n  position: relative;\n  display: flex;\n  flex-direction: column;\n  gap: 8px;\n",
            ".zpm-corp-timeline__step {\n  position: relative;\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-delivery-point-card__icon {\n  display: inline-flex;\n  align-items: center;\n  justify-content: center;\n  width: 52px;\n  height: 52px;\n  border: 1px solid var(--border-color);\n  border-radius: 50%;\n  font-size: 22px;\n",
            ".zpm-delivery-point-card__icon {\n  display: inline-flex;\n  align-items: center;\n  justify-content: center;\n  border: 1px solid var(--border-color);\n  border-radius: 50%;\n",
        ),
        (
            ".zpm-payment-proof__grid {\n  display: grid;\n  grid-template-columns: repeat(5, minmax(0, 1fr));\n  gap: var(--pad-gap-line);\n",
            ".zpm-payment-proof__grid {\n  display: grid;\n  grid-template-columns: repeat(4, minmax(0, 1fr));\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-delivery-org__list {\n  margin: 0 0 var(--pad-gap-mini);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: 8px;\n}",
            ".zpm-delivery-org__list {\n  margin: 0 0 var(--pad-gap-mini);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n}",
        ),
        (
            ".zpm-delivery-summary {\n  display: grid;\n  grid-template-columns: repeat(4, minmax(0, 1fr));\n  gap: var(--pad-gap-line);\n",
            ".zpm-delivery-summary {\n  display: grid;\n  grid-template-columns: repeat(4, minmax(0, 1fr));\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-delivery-outcomes__list {\n  display: grid;\n  grid-template-columns: repeat(2, minmax(0, 1fr));\n  gap: var(--pad-gap-line);\n",
            ".zpm-delivery-outcomes__list {\n  display: grid;\n  grid-template-columns: repeat(2, minmax(0, 1fr));\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-warranty-outcomes__list {\n  display: grid;\n  grid-template-columns: repeat(2, minmax(0, 1fr));\n  gap: var(--pad-gap-line);\n",
            ".zpm-warranty-outcomes__list {\n  display: grid;\n  grid-template-columns: repeat(2, minmax(0, 1fr));\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-warranty-outcome__title {\n  margin: 0 0 8px;\n",
            ".zpm-warranty-outcome__title {\n  margin: 0 0 var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-warranty-verification__list {\n  margin: 0 0 var(--pad-gap);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: 8px;\n",
            ".zpm-warranty-verification__list {\n  margin: 0 0 var(--pad-gap);\n  padding-left: 1.2em;\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n",
        ),
        (
            ".zpm-dealers-proof__stack {\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-line);\n",
            ".zpm-dealers-proof__stack {\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-dealers-cta__actions {\n  display: flex;\n  flex-wrap: wrap;\n  align-items: center;\n  gap: 12px 20px;\n  margin-bottom: var(--pad-gap-mini);\n}",
            ".zpm-dealers-cta__actions {\n  display: flex;\n  flex-wrap: wrap;\n  align-items: center;\n  gap: var(--pad-gap-line);\n  margin-top: var(--pad-gap);\n  margin-bottom: 0;\n}",
        ),
        (
            ".zpm-dealers-cta__contacts {\n  display: flex;\n  flex-wrap: wrap;\n  gap: 12px 24px;\n  margin-bottom: var(--pad-gap-mini);\n}",
            ".zpm-dealers-cta__contacts {\n  display: flex;\n  flex-wrap: wrap;\n  gap: var(--pad-gap-line) var(--pad-gap);\n  margin-top: var(--pad-gap-mini);\n  margin-bottom: 0;\n}",
        ),
        (
            ".zpm-custom-process {\n  background-color: var(--main-light-color, #f8f8f8);\n  padding-top: var(--pad-y);\n  padding-bottom: var(--pad-y);\n  border-top: 2px solid var(--accent-color-01, #c4a35a);\n  border-bottom: 2px solid var(--accent-color-01, #c4a35a);\n}",
            ".zpm-custom-process {\n  background-color: var(--main-light-color, #f8f8f8);\n  padding-bottom: var(--pad-y);\n  border-top: 1px solid var(--border-color);\n  border-bottom: 1px solid var(--border-color);\n}",
        ),
        (
            ".zpm-custom-timeline.zpm-corp-timeline {\n  grid-template-columns: repeat(8, minmax(0, 1fr));\n",
            ".zpm-custom-timeline.zpm-corp-timeline {\n  grid-template-columns: repeat(4, minmax(0, 1fr));\n",
        ),
        (
            ".zpm-custom-process .zpm-corp-timeline__step {\n  border-width: 2px;\n  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);\n}",
            ".zpm-custom-process .zpm-corp-timeline__step {\n  border-width: 1px;\n  box-shadow: none;\n}",
        ),
        (
            ".zpm-custom-outcomes {\n  border-top: 3px solid var(--accent-color-01, #c4a35a);\n  padding-top: var(--pad-y);\n}",
            ".zpm-custom-outcomes {\n  border-top: 1px solid var(--border-color);\n}",
        ),
        (
            ".zpm-custom-outcomes__table thead th {\n  padding-top: 14px;\n  padding-bottom: 14px;\n  font-size: calc(var(--base-Font-size) * 1.05);\n  border-bottom: 2px solid var(--accent-color-01, #c4a35a);\n}",
            ".zpm-custom-outcomes__table thead th {\n  padding-top: 14px;\n  padding-bottom: 14px;\n  font-size: var(--base-Font-size);\n  border-bottom: 1px solid var(--border-color);\n}",
        ),
        (
            ".zpm-custom-cta__actions {\n  display: flex;\n  flex-wrap: wrap;\n  align-items: center;\n  gap: 12px 20px;\n  margin-bottom: var(--pad-gap-mini);\n}",
            ".zpm-custom-cta__actions {\n  display: flex;\n  flex-wrap: wrap;\n  align-items: center;\n  gap: var(--pad-gap-line);\n  margin-top: var(--pad-gap);\n  margin-bottom: 0;\n}",
        ),
        (
            ".zpm-warranty-summary {\n  display: grid;\n  grid-template-columns: repeat(4, minmax(0, 1fr));\n  gap: var(--pad-gap-line);\n",
            ".zpm-warranty-summary {\n  display: grid;\n  grid-template-columns: repeat(4, minmax(0, 1fr));\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-custom-cta__contacts {\n  display: flex;\n  flex-wrap: wrap;\n  gap: 12px 24px;\n  margin-bottom: var(--pad-gap-mini);\n}",
            ".zpm-custom-cta__contacts {\n  display: flex;\n  flex-wrap: wrap;\n  gap: var(--pad-gap-line) var(--pad-gap);\n  margin-top: var(--pad-gap-mini);\n  margin-bottom: 0;\n}",
        ),
        (
            ".zpm-corp-faq__list {\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap-mini);\n",
            ".zpm-corp-faq__list {\n  display: flex;\n  flex-direction: column;\n  gap: var(--pad-gap);\n",
        ),
        (
            ".zpm-payment-legal__facts {\n  display: grid;\n  grid-template-columns: repeat(3, minmax(0, 1fr));\n  gap: var(--pad-gap-line);\n",
            ".zpm-payment-legal__facts {\n  display: grid;\n  grid-template-columns: repeat(3, minmax(0, 1fr));\n  gap: var(--pad-gap);\n",
        ),
    ]

    for old, new in replacements:
        if old not in css:
            raise SystemExit(f"Missing expected CSS block:\n{old[:120]}...")
        css = css.replace(old, new, 1)

    if "Corporate Pages Visual Polish Pass 1.1" in css:
        raise SystemExit("Pass 1.1 block already applied")

    css = css.rstrip() + APPEND
    STYLE.write_text(css + "\n", encoding="utf-8")
    print(f"Patched {STYLE} ({STYLE.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

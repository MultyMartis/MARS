#!/usr/bin/env python3
"""One-off CF-011 SCSS migration: replace services-program-v2__cta-* with program-cta-band."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCSS = ROOT / "src" / "scss" / "style.scss"

NEW_BLOCK = """
/* CF-011 program-cta-band */
.program-cta-band-section {
\tpadding: var(--pad-gap) 0;
}

.program-cta-band-section__container {
\tpadding-top: 0;
\tpadding-bottom: 0;
}

.program-cta-band {
\tposition: relative;
\tdisplay: grid;
\tgrid-template-columns: minmax(0, 1fr) auto auto;
\talign-items: center;
\tgap: var(--pad-gap);
\tbox-sizing: border-box;
\tmargin-bottom: var(--pad-gap-line);
\tpadding: var(--pad-gap);
\tborder-radius: var(--radius-main);
\tbackground-color: var(--color-text-primary);
\tcolor: var(--color-text-inverse);
}

.program-cta-band--flush {
\tmargin-bottom: 0;
}

.program-cta-band::before {
\tcontent: "";
\tposition: absolute;
\tinset: 0;
\tbackground-image: url("../img/content/home-final-form/home-final-form-background.webp");
\tbackground-repeat: no-repeat;
\tbackground-position: center;
\tbackground-size: cover;
\topacity: 0.1;
\tpointer-events: none;
\tborder-radius: inherit;
}

.program-cta-band > * {
\tposition: relative;
\tz-index: 1;
}

.program-cta-band__title {
\tmargin: 0 0 4px;
\tfont-size: var(--font-size-large);
\tline-height: var(--line-height-large);
\tfont-weight: var(--font-weight-heading);
\tcolor: var(--color-text-inverse);
}

.program-cta-band__subtitle {
\tmargin: 0;
\tfont-size: var(--font-size-base);
\tline-height: var(--line-height-base);
\tfont-weight: var(--font-weight-base);
\tcolor: var(--color-text-inverse);
}

.program-cta-band__phone {
\tfont-size: 40px;
\tfont-weight: var(--font-weight-heading);
\tline-height: 40px;
\tcolor: var(--color-text-inverse);
\ttext-decoration: none;
\twhite-space: nowrap;
}

.program-cta-band__phone:hover,
.program-cta-band__phone:focus-visible {
\tcolor: var(--color-text-inverse);
\topacity: 0.9;
}

.program-cta-band__phone-hint {
\tfont-size: var(--font-size-base);
\tline-height: var(--line-height-base);
\tfont-weight: var(--font-weight-base);
\twhite-space: normal;
\tcolor: var(--color-text-inverse);
}

.program-cta-band__button {
\tflex-shrink: 0;
}

.program-cta-band--button-first .program-cta-band__copy {
\torder: 1;
}

.program-cta-band--button-first .program-cta-band__button {
\torder: 2;
}

.program-cta-band--button-first .program-cta-band__phone {
\tdisplay: inline-flex;
\tflex-direction: column;
\talign-items: flex-start;
\tgap: 4px;
\torder: 3;
}

@media (max-width: 1024px) {
\t.program-cta-band {
\t\tgrid-template-columns: minmax(0, 1fr);
\t\tgap: var(--pad-gap-line);
\t}

\t.program-cta-band__phone {
\t\tfont-size: 32px;
\t\tline-height: 32px;
\t\twhite-space: normal;
\t}

\t.program-cta-band__button {
\t\twidth: 100%;
\t\tmax-width: 334px;
\t}
}

@media (max-width: 660px) {
\t.program-cta-band__phone {
\t\tfont-size: 28px;
\t\tline-height: 28px;
\t}
}

"""


def strip_cta_rules(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if "services-program-v2__cta" in line:
            # skip selector line and following rule block until blank line or next top-level selector
            if line.strip().endswith("{"):
                depth = line.count("{") - line.count("}")
                i += 1
                while i < len(lines) and depth > 0:
                    depth += lines[i].count("{") - lines[i].count("}")
                    i += 1
                continue
            # skip single-line or media-only selector lines without opening brace on same line
            if "{" not in line:
                i += 1
                continue
        # skip orphaned wrapper-only blocks for deleted partials
        if re.search(
            r"\.(service-subdivision-first-cta-v1|service-leaf-cta-01-v1|service-subdivision-second-cta-v1)",
            line,
        ):
            if "{" in line:
                depth = line.count("{") - line.count("}")
                i += 1
                while i < len(lines) and depth > 0:
                    depth += lines[i].count("{") - lines[i].count("}")
                    i += 1
                continue
            i += 1
            continue
        out.append(line)
        i += 1
    return "".join(out)


def main() -> None:
    text = SCSS.read_text(encoding="utf-8")
    if ".program-cta-band {" in text:
        print("CF-011 block already present")
        return
    text = strip_cta_rules(text)
    marker = ".page-uslugi-v2 .services-program-v2__foot-link {"
    if marker not in text:
        # insert before foot-link after program item styles
        marker = ".page-uslugi-v2 .services-program-v2__foot-link {"
    if marker in text:
        text = text.replace(marker, NEW_BLOCK + marker, 1)
    else:
        raise SystemExit("insert marker not found")
    if "services-program-v2__cta" in text:
        raise SystemExit("remaining services-program-v2__cta references")
    SCSS.write_text(text, encoding="utf-8")
    print("SCSS migration complete")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""CF-012: consolidate services-program-v2 page-scoped CSS into functional modifiers."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCSS = ROOT / "src" / "scss" / "style.scss"

PROGRAM_HEAD = """/* ==========================================================================
   CF-012 — services-program-v2 (canonical program family)
   ========================================================================== */

.services-program-v2 {
\tpadding: var(--pad-y) 0;
}

.services-program-v2__head {
\tdisplay: flex;
\talign-items: center;
\tjustify-content: space-between;
\tgap: var(--pad-gap-line);
\tmargin-bottom: var(--pad-gap);
}

.services-program-v2__heading {
\tmargin: 0;
\tfont-size: var(--font-size-h2);
\tline-height: var(--line-height-h2);
\tfont-weight: var(--font-weight-heading);
\tcolor: var(--color-text-primary);
}

.services-program-v2__head-link {
\tdisplay: inline-flex;
\talign-items: center;
\tgap: var(--pad-gap-line);
\tfont-size: 15px;
\tline-height: var(--line-height-nav);
\tfont-weight: var(--font-weight-button);
\tcolor: var(--color-text-primary);
\ttext-decoration: none;
\ttext-transform: uppercase;
\tflex-shrink: 0;
}

.services-program-v2__head-link:hover,
.services-program-v2__head-link:focus-visible {
\tcolor: var(--color-accent);
}

.services-program-v2__head-link-icon {
\tdisplay: inline-flex;
\tflex-shrink: 0;
}

.services-program-v2__head-link-icon-image {
\tdisplay: block;
\twidth: 20px;
\theight: 20px;
}

.services-program-v2__lead {
\tmargin: 0 0 var(--pad-gap-line);
\tpadding: var(--pad-gap-line) 0 var(--pad-gap-line) var(--pad-gap);
\tborder-left: 5px solid var(--color-accent);
\tfont-size: var(--font-size-base);
\tline-height: var(--line-height-base);
\tcolor: var(--color-text-secondary);
\ttext-transform: uppercase;
}

.services-program-v2__intro {
\tmargin: 0 0 var(--pad-gap);
\tfont-size: var(--font-size-base);
\tline-height: var(--line-height-base);
\tcolor: var(--color-text-secondary);
}

.services-program-v2__grid {
\tdisplay: grid;
\tgrid-template-columns: repeat(2, minmax(0, 1fr));
\tgap: var(--pad-gap-line);
\tmargin-bottom: var(--pad-gap);
}

.services-program-v2__item {
\tdisplay: flex;
\tflex-direction: column;
\toverflow: hidden;
\tpadding: var(--pad-gap-line);
\tborder: var(--border-width) solid var(--color-text-primary);
\tborder-radius: var(--radius-main);
}

.services-program-v2__item-body {
\tdisplay: flex;
\tflex-direction: column;
}

.services-program-v2__item-media {
\tdisplay: block;
\toverflow: hidden;
\tpadding: 0;
}

.services-program-v2--media-frame-fixed .services-program-v2__item-media {
\theight: 410px;
\tborder-radius: var(--radius-main);
}

.services-program-v2__item-image {
\tdisplay: block;
\twidth: 100%;
\theight: auto;
\tobject-fit: cover;
\tobject-position: center;
\tborder-radius: var(--radius-main);
}

.services-program-v2__item-title {
\tdisplay: flex;
\tflex-direction: column;
\tgap: var(--pad-gap-line);
\tpadding: 0 0 var(--pad-gap);
\tfont-size: var(--font-size-base);
\tfont-weight: var(--font-weight-heading);
\tline-height: var(--line-height-base);
}

.services-program-v2--intro-stacked .services-program-v2__intro--continued {
\tmargin-top: calc(var(--pad-gap-line) * -1);
}

.services-program-v2--grid-compact .services-program-v2__grid {
\tgap: var(--pad-gap);
}

.services-program-v2--play-link .services-program-v2__head-link-icon .fas,
.services-program-v2--play-link .services-program-v2__foot-link-icon .fas {
\tfont-size: 12px;
\tcolor: var(--color-accent);
}

.services-program-v2--media-contain .services-program-v2__item-image {
\tobject-fit: contain;
}

.services-program-v2--title-block .services-program-v2__item-title {
\tdisplay: block;
\tmargin: 0;
\tgap: 0;
\tpadding: 0;
\tcolor: var(--color-text-primary);
}

.services-program-v2--title-flush .services-program-v2__item-title {
\tpadding: 0;
}

.services-program-v2--item-body-spaced .services-program-v2__item-body {
\tgap: var(--pad-gap-line);
\tpadding: 0 0 var(--pad-gap);
}

.services-program-v2__foot-link {
\tdisplay: none;
\talign-items: center;
\tjustify-content: center;
\tgap: var(--pad-gap-line);
\tmargin-top: var(--pad-gap-line);
\tfont-size: 15px;
\tline-height: var(--line-height-nav);
\tfont-weight: var(--font-weight-button);
\tcolor: var(--color-text-primary);
\ttext-decoration: none;
\ttext-transform: uppercase;
}

.services-program-v2__foot-link:hover,
.services-program-v2__foot-link:focus-visible {
\tcolor: var(--color-accent);
}

.services-program-v2__foot-link-icon-image {
\tdisplay: block;
\twidth: 20px;
\theight: 20px;
}

@media (max-width: 1024px) {
\t.services-program-v2__head {
\t\tflex-direction: column;
\t\talign-items: flex-start;
\t}

\t.services-program-v2__head-link {
\t\tdisplay: none;
\t}

\t.services-program-v2__grid {
\t\tgrid-template-columns: minmax(0, 1fr);
\t\tgap: var(--pad-gap);
\t}

\t.services-program-v2--item-image-stack-tall .services-program-v2__item-image {
\t\theight: 280px;
\t}

\t.services-program-v2--item-body-mobile-pad .services-program-v2__item-body {
\t\tpadding: 0 0 var(--pad-gap-line);
\t}

\t.services-program-v2--item-media-mobile-pad .services-program-v2__item-media {
\t\tpadding: 0 var(--pad-gap-line) var(--pad-gap-line);
\t}

\t.services-program-v2__foot-link {
\t\tdisplay: inline-flex;
\t\twidth: 100%;
\t}
}

@media (max-width: 660px) {
\t.services-program-v2--item-image-mobile-short .services-program-v2__item-image {
\t\theight: 280px;
\t}
}
"""

MARKER_OLD_START = "/* ==========================================================================\n   Services V2 — program block (Services-specific)"
MARKER_CTA = "/* CF-011 program-cta-band */"
MARKER_FOOT_START = ".page-uslugi-v2 .services-program-v2__foot-link"
MARKER_FOOT_END = "@media (max-width: 660px) {\n\t.page-uslugi-v2 .services-program-v2__item-image"
MARKER_SUBDIVISION_PROGRAM = ".page-service-subdivision-v1 .service-subdivision-program-v1 {"
MARKER_SUBDIVISION_STAGES = ".page-service-subdivision-v1 .service-subdivision-stages-v1 {"
MARKER_LEAF_PROGRAM = ".page-service-leaf-v1 .service-leaf-program-v1 {"
MARKER_LEAF_STAGES = ".page-service-leaf-v1 .service-leaf-stages-v1 {"


def remove_block(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"start marker not found: {start[:60]}")
    j = text.find(end, i)
    if j < 0:
        raise SystemExit(f"end marker not found after {start[:60]}")
    return text[:i] + text[j:]


def remove_subdivision_responsive(text: str) -> str:
    patterns = [
        r"\n\t\.page-service-subdivision-v1 \.service-subdivision-program-v1 \.services-program-v2__head \{[^}]+\}\n",
        r"\n\t\.page-service-subdivision-v1 \.service-subdivision-program-v1 \.services-program-v2__head-link \{[^}]+\}\n",
        r"\n\t\.page-service-subdivision-v1 \.service-subdivision-program-v1 \.services-program-v2__grid \{[^}]+\}\n",
        r"\n\t// \.page-service-subdivision-v1 \.service-subdivision-program-v1 \.services-program-v2__item-image \{[^}]+\}\n",
        r"\n\t\.page-service-subdivision-v1 \.service-subdivision-program-v1 \.services-program-v2__foot-link \{[^}]+\}\n",
        r"\n@media \(max-width: 660px\) \{\n\t\.page-service-subdivision-v1 \.service-subdivision-program-v1 \.services-program-v2__item-image \{[^}]+\}\n\n\}\n",
    ]
    for pat in patterns:
        text, n = re.subn(pat, "\n", text, count=1)
        if n == 0 and "660px" in pat:
            text, _ = re.subn(
                r"\n@media \(max-width: 660px\) \{\n\t\.page-service-subdivision-v1 \.service-subdivision-program-v1 \.services-program-v2__item-image \{[^}]+\}\n\}\n",
                "\n",
                text,
                count=1,
            )
    return text


def remove_leaf_responsive(text: str) -> str:
    block = re.compile(
        r"\n\t\.page-service-leaf-v1 \.service-leaf-program-v1 \.services-program-v2__[^\n]+\n(?:\t[^\n]+\n)*",
        re.MULTILINE,
    )
    return block.sub("\n", text)


def main() -> None:
    text = SCSS.read_text(encoding="utf-8")

    # Replace hub program block (before CTA) with canonical head
    i0 = text.find(MARKER_OLD_START)
    i1 = text.find(MARKER_CTA)
    if i0 < 0 or i1 < 0:
        raise SystemExit("program/cta markers missing")
    text = text[:i0] + PROGRAM_HEAD + "\n\n" + text[i1:]

    # Remove old hub foot-link block (after CTA, before subdivision pass comment)
    i2 = text.find(MARKER_FOOT_START)
    i3 = text.find("/* FP-0002 Service Subdivision Pass 1 */")
    if i2 < 0 or i3 < 0:
        raise SystemExit("foot/subdivision markers missing")
  # foot block sits between CTA end and subdivision comment
    cta_end = text.find("@media (max-width: 660px) {\n\t.program-cta-band__phone", text.find(MARKER_CTA))
    cta_close = text.find("\n}\n", cta_end)
    cta_close = text.find("\n", cta_close + 3)  # after closing brace line
    if i2 > cta_close:
        text = text[:cta_close] + "\n" + text[i3:]
    else:
        text = text[:i2] + text[i3:]

    # Remove subdivision program duplicate block
    text = remove_block(text, MARKER_SUBDIVISION_PROGRAM, MARKER_SUBDIVISION_STAGES)

    # Remove shared triple item-media selector remnants if any
    text = re.sub(
        r"\.page-uslugi-v2 \.services-program-v2__item-media,\n\.page-service-leaf-v1 \.service-leaf-program-v1 \.services-program-v2__item-media,\n\.page-service-subdivision-v1 \.service-subdivision-program-v1 \.services-program-v2__item-media \{[^}]+\}\n\n",
        "",
        text,
        count=1,
    )

    text = remove_subdivision_responsive(text)

    # Remove leaf program duplicate block
    text = remove_block(text, MARKER_LEAF_PROGRAM, MARKER_LEAF_STAGES)

    text = remove_leaf_responsive(text)

    # Retired page-named modifiers must be gone from SCSS
    for retired in (
        "service-subdivision-program-v1",
        "service-leaf-program-v1",
        ".page-uslugi-v2 .services-program-v2",
    ):
        if retired in text:
            raise SystemExit(f"retired selector still present: {retired}")

    SCSS.write_text(text, encoding="utf-8")
    print("CF-012 SCSS migration complete")


if __name__ == "__main__":
    main()

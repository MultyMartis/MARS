#!/usr/bin/env python3
"""Generate BZPM PDP desktop wireframe SVG schematics — review artifacts only."""

from pathlib import Path

OUT = Path(__file__).resolve().parent

# Wireframe palette — no branding, no design system
C = {
    "bg": "#f8f8f8",
    "page": "#ffffff",
    "stroke": "#333333",
    "stroke_light": "#999999",
    "fill_zone": "#eeeeee",
    "fill_hero": "#e8e8e8",
    "fill_warn": "#fff3cd",
    "fill_ok": "#e8f4ea",
    "fill_band": "#dde4ee",
    "fill_gallery": "#f0f0f0",
    "text": "#222222",
    "text_muted": "#666666",
    "fold": "#cc4444",
    "accent_a": "#4a7c59",
    "accent_b": "#3d5a80",
    "accent_current": "#8b6914",
}


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def rect(x, y, w, h, fill=C["page"], stroke=C["stroke"], sw=1.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
    )


def text(x, y, s, size=11, weight="normal", fill=C["text"], anchor="start"):
    return (
        f'<text x="{x}" y="{y}" font-family="Segoe UI, Arial, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
        f'text-anchor="{anchor}">{esc(s)}</text>'
    )


def label_block(x, y, w, h, title, lines=None, fill=C["fill_zone"], tag=None):
    parts = [rect(x, y, w, h, fill=fill)]
    ty = y + 16
    parts.append(text(x + 8, ty, title, size=10, weight="bold"))
    if tag:
        parts.append(text(x + w - 8, ty, tag, size=9, fill=C["text_muted"], anchor="end"))
    if lines:
        for i, line in enumerate(lines):
            parts.append(text(x + 8, ty + 18 + i * 14, line, size=9, fill=C["text_muted"]))
    return "\n  ".join(parts)


def fold_line(y, x1, x2, label="FIRST SCREEN FOLD"):
    return f"""
  <line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{C['fold']}" stroke-width="1.5" stroke-dasharray="8,4"/>
  {text((x1 + x2) / 2, y - 6, label, size=10, weight="bold", fill=C["fold"], anchor="middle")}"""


def header_bar(x, y, w, title, subtitle=None, accent=C["stroke"]):
    h = 52 if subtitle else 40
    parts = [
        rect(x, y, w, h, fill=accent, stroke=accent),
        text(x + w / 2, y + (22 if subtitle else 26), title, size=13, weight="bold", fill="#fff", anchor="middle"),
    ]
    if subtitle:
        parts.append(text(x + w / 2, y + 38, subtitle, size=9, fill="#eee", anchor="middle"))
    return "\n  ".join(parts), y + h + 8


def svg_wrap(w, h, body, title=None):
    title_el = ""
    if title:
        title_el = f'<title>{esc(title)}</title>\n  '
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  {title_el}<rect width="{w}" height="{h}" fill="{C['bg']}"/>
  {body}
</svg>
'''


def scroll_zone(x, y, w, label, blocks_html, h=90):
    return f"""
  {rect(x, y, w, h, fill=C["fill_zone"], stroke=C["stroke_light"], sw=1)}
  {text(x + 10, y + 18, label, size=10, weight="bold")}
  {blocks_html}
"""


# ── CURRENT PDP (audit baseline) ──────────────────────────────────────────

def schematic_current():
    W, H = 920, 1180
    mx, my = 40, 20
    pw = W - 80
    y = my

    parts = []
    parts.append(header_bar(mx, y, pw, "CURRENT PDP — Desktop Schematic", "Audit baseline · zpm.new-site.space · W1A/W2 findings")[0])
    y += 60

    parts.append(label_block(mx, y, pw, 28, "SITE HEADER", tag="out of scope"))
    y += 36

    parts.append(label_block(mx, y, pw, 36, "Breadcrumb", ["Главная › Каталог › … › ПРЕМИУМ-3 › SKU"], tag="WH-13 series here only"))
    y += 44

    # Hero 2-col
    gal_w = int(pw * 0.42)
    info_w = pw - gal_w - 12
    hero_h = 340
    parts.append(f'{rect(mx, y, pw, hero_h, fill=C["fill_hero"])}')
    parts.append(text(mx + 10, y + 16, "HERO — 2-column (W2-F-02)", size=10, weight="bold"))

    gy = y + 24
    parts.append(label_block(mx + 8, gy, gal_w - 16, hero_h - 32, "GALLERY", [
        "[ product image ]",
        "~520px tall · 1 slide (W2-F-01)",
        "no thumbnails · high void (WH-16)",
    ], fill=C["fill_gallery"]))

    ix = mx + gal_w + 4
    parts.append(label_block(ix, gy, info_w - 8, 52, "H1 + IDENTITY", [
        "Ванна моечная цельнотянутая …",
        "[AssuM logo] · mini-desc placeholder (W1A-F-03/04)",
    ]))
    parts.append(label_block(ix, gy + 58, info_w - 8, 36, "Артикул: ВМЦ-П3-2/500"))
    parts.append(label_block(ix, gy + 100, info_w - 8, 88, "BUY BOX (W1A-F-12)", [
        "● В наличии · 3 шт.",
        "142 500 ₽ · Qty [1] · [ В КОРЗИНУ ]",
    ], fill=C["fill_ok"]))
    parts.append(label_block(ix, gy + 194, info_w - 8, 36, "Compare / Fav", ["icon-only (W1A-F-07)"], fill=C["fill_warn"]))
    parts.append(label_block(ix, gy + 236, info_w - 8, 56, "4 PROPS ONLY (W1A-F-02)", [
        "L 1150 │ W 700 │ H 850 │ 68 кг",
        "no sections · bowl · material · construction (WH-14)",
    ]))

    y += hero_h + 8
    parts.append(fold_line(y, mx, mx + pw))
    y += 14

    parts.append(label_block(mx, y, pw, 72, "TABS (W1A-F-05 · W2-F-03)", [
        "[ Описание ● ]  [ Характеристики ]  [ Документы ]  ← 2/3 hidden on load",
        "20+ spec rows behind inactive «Характеристики» tab",
    ], fill=C["fill_warn"]))
    y += 80

    parts.append(scroll_zone(mx, y, pw, "FIRST SCROLL — tab content + deep blocks", f"""
  {label_block(mx + 10, y + 28, pw - 20, 48, "«Похожие товары» (W1A-F-06)", ["Cross-family: котломойки ВКС-* — NOT ПРЕМИУМ-3 siblings"], fill=C["fill_warn"])}
  """, h=88))
    y += 96

    parts.append(label_block(mx, y, pw, 48, "Deep scroll", ["Certificates slider · Dealer form inline · Advantages grids (W2-F-07)"]))
    y += 56

    parts.append(label_block(mx, y, pw, 28, "SITE FOOTER"))
    y += 36

    parts.append(text(mx, y, "Density: LOW · ~6 facts first screen · Series: breadcrumb only", size=10, fill=C["accent_current"]))
    parts.append(text(mx, y + 16, "Source: BZPM-PDP-CONCEPT-ALPHA-v1 · BZPM-FINDINGS-REGISTER-v1 · Mockup comparison baseline", size=9, fill=C["text_muted"]))

    return svg_wrap(W, H, "\n  ".join(parts), "BZPM Current PDP Desktop Schematic")


# ── MOCKUP A ──────────────────────────────────────────────────────────────

def schematic_mockup_a():
    W, H = 920, 1120
    mx, my = 40, 20
    pw = W - 80
    y = my

    parts = []
    parts.append(header_bar(mx, y, pw, "MOCKUP A — Conservative Evolution", "Desktop · USR-PDP-00–21 unchanged · BZPM-PDP-MOCKUP-A-v1", accent=C["accent_a"])[0])
    y += 60

    parts.append(label_block(mx, y, pw, 28, "USR-PDP-00 Breadcrumb"))
    y += 36

    gal_w = int(pw * 0.40)
    info_w = pw - gal_w - 12
    hero_h = 300
    parts.append(f'{rect(mx, y, pw, hero_h, fill=C["fill_hero"])}')
    parts.append(text(mx + 10, y + 16, "HERO — Classic BZPM two-column + fit strip", size=10, weight="bold"))

    gy = y + 24
    parts.append(label_block(mx + 8, gy, gal_w - 16, hero_h - 32, "USR-PDP-06 MEDIA", [
        "[ product image ] ~40% width",
        "[ thumb ][ thumb ]",
    ], fill=C["fill_gallery"]))

    ix = mx + gal_w + 4
    parts.append(label_block(ix, gy, info_w - 8, 48, "USR-PDP-01 IDENTITY", ["H1 · Артикул: ВМЦ-П3-2/500 [copy]"]))
    parts.append(label_block(ix, gy + 54, info_w - 8, 32, "USR-PDP-02 SERIES", ["Серия: ПРЕМИУМ-3 → все модели (one line)"]))
    parts.append(label_block(ix, gy + 92, info_w - 8, 80, "USR-PDP-03 COMMERCIAL", [
        "● В наличии · 3 шт. · 142 500 ₽",
        "Qty [ - 1 + ] · [ В КОРЗИНУ ]",
    ], fill=C["fill_ok"]))
    parts.append(label_block(ix, gy + 178, info_w - 8, 32, "USR-PDP-07", ["[ Сравнить ] [ Избранное ] — labeled"]))

    y += hero_h + 4
    parts.append(label_block(mx, y, pw, 44, "USR-PDP-04 + USR-PDP-05 FIT STRIP", [
        "L 1150 │ W 700 │ H 850 │ 68 кг │ 2 сек │ чаша 500×400 │ AISI 304 │ Цельнотянутая",
    ]))
    y += 52
    parts.append(fold_line(y, mx, mx + pw))
    y += 14

    for label, blocks in [
        ("P2 — FIRST SCROLL", [
            "USR-PDP-08 Description (prose)",
            "USR-PDP-09 Min Spec Summary — DEFAULT ON (5–8 rows)",
            "USR-PDP-19 Consult CTA · USR-PDP-10 Full Specs [▼ collapsed] · USR-PDP-11 Docs",
        ]),
        ("P3 — DEEP SCROLL", [
            "USR-PDP-12 In-Series Alternatives (carousel — familiar slot)",
            "USR-PDP-13/14 Compare · Return-to-series",
            "USR-PDP-15–17 Reference · Cross-family (labeled)",
            "USR-PDP-18/20/21 Commercial detail · trust · legal",
        ]),
    ]:
        bh = 28 + len(blocks) * 14
        parts.append(f'{rect(mx, y, pw, bh, fill=C["fill_zone"], stroke=C["stroke_light"], sw=1)}')
        parts.append(text(mx + 10, y + 18, label, size=10, weight="bold"))
        for i, b in enumerate(blocks):
            parts.append(text(mx + 14, y + 34 + i * 14, b, size=9, fill=C["text_muted"]))
        y += bh + 8

    parts.append(text(mx, y, "Visual weight: Gallery HIGH · Buy box HIGH · Series MEDIUM-LOW · Fit MEDIUM strip", size=10, fill=C["accent_a"]))
    return svg_wrap(W, y + 30, "\n  ".join(parts), "BZPM Mockup A Desktop Schematic")


# ── MOCKUP B ──────────────────────────────────────────────────────────────

def schematic_mockup_b():
    W, H = 920, 1140
    mx, my = 40, 20
    pw = W - 80
    y = my

    parts = []
    parts.append(header_bar(mx, y, pw, "MOCKUP B — Industrial Procurement", "Desktop · USR-PDP-00–21 unchanged · BZPM-PDP-MOCKUP-B-v1", accent=C["accent_b"])[0])
    y += 60

    parts.append(label_block(mx, y, pw, 28, "USR-PDP-00 Breadcrumb (compact)"))
    y += 36

    parts.append(label_block(mx, y, pw, 52, "USR-PDP-02 SERIES CONTEXT BAND", [
        "СЕРИЯ: ПРЕМИУМ-3 │ Цельнотянутые ванны премиум-класса",
        "[ → Все SKU серии (10) ] │ См. также: ПРЕМИУМ · СТАНДАРТ",
    ], fill=C["fill_band"], tag="STRONG WH-13 fix"))
    y += 60

    hero_h = 280
    thumb_w = 100
    panel_w = pw - thumb_w - 12
    parts.append(f'{rect(mx, y, pw, hero_h, fill=C["fill_hero"])}')
    parts.append(text(mx + 10, y + 16, "HERO — Procurement panel (data-first)", size=10, weight="bold"))

    gy = y + 24
    parts.append(label_block(mx + 8, gy, thumb_w - 8, hero_h - 32, "USR-PDP-06", [
        "[img]",
        "~25%",
        "[+2]",
        "thumbs",
    ], fill=C["fill_gallery"]))

    px = mx + thumb_w + 4
    parts.append(label_block(px, gy, panel_w - 8, 44, "USR-PDP-01 IDENTITY", ["H1 · Артикул · [copy] │ ЗПМ · OEM"]))
    parts.append(label_block(px, gy + 50, panel_w - 8, 72, "USR-PDP-04 + USR-PDP-05 FIT GRID (2×4)", [
        "L:1150 │ W:700 │ H:850 │ 68 кг",
        "Секций:2 │ Чаша:500×400 │ AISI 304 │ Цельнот.",
    ]))
    parts.append(label_block(px, gy + 128, panel_w - 8, 72, "USR-PDP-03 + USR-PDP-07 + USR-PDP-18 preview", [
        "● В наличии · 3 шт. │ 142 500 ₽ │ Qty [1] │ [ В КОРЗИНУ ]",
        "[ Сравнить ] [ Избранное ] │ Доставка: от 3 дн. → │ Купить как дилер →",
    ], fill=C["fill_ok"]))

    y += hero_h + 8
    parts.append(fold_line(y, mx, mx + pw))
    y += 14

    for label, blocks in [
        ("P2 — FIRST SCROLL (dense)", [
            "USR-PDP-09 Min Spec — table continuation DEFAULT ON",
            "USR-PDP-08 Description (compact · expand)",
            "USR-PDP-19 Consult links · USR-PDP-10 Full Specs [▼] · USR-PDP-11 Docs",
        ]),
        ("P3 — DEEP SCROLL", [
            "USR-PDP-12 In-Series Alternatives — table/cards (6 SKU columns)",
            "USR-PDP-13/14 · USR-PDP-18 detail · USR-PDP-15–17",
            "USR-PDP-20/21 trust micro · legal (single line)",
        ]),
    ]:
        bh = 28 + len(blocks) * 14
        parts.append(f'{rect(mx, y, pw, bh, fill=C["fill_zone"], stroke=C["stroke_light"], sw=1)}')
        parts.append(text(mx + 10, y + 18, label, size=10, weight="bold"))
        for i, b in enumerate(blocks):
            parts.append(text(mx + 14, y + 34 + i * 14, b, size=9, fill=C["text_muted"]))
        y += bh + 8

    parts.append(text(mx, y, "Visual weight: Series band HIGHEST · Fit grid HIGH · Commercial HIGH · Media LOW", size=10, fill=C["accent_b"]))
    return svg_wrap(W, y + 30, "\n  ".join(parts), "BZPM Mockup B Desktop Schematic")


# ── SIDE-BY-SIDE COMPARISON (first screen) ────────────────────────────────

def schematic_comparison():
    W = 2760
    col_w = 860
    gap = 30
    mx = 30
    my = 20
    hero_h = 380

    def col_x(i):
        return mx + i * (col_w + gap)

    parts = []
    parts.append(header_bar(mx, my, W - 60, "BZPM PDP — Desktop First Screen Comparison", "Current · Mockup A · Mockup B · For operator review before design work · No implementation")[0])
    y0 = my + 60

    titles = [
        ("CURRENT PDP", "Audit baseline", C["accent_current"]),
        ("MOCKUP A", "Conservative Evolution", C["accent_a"]),
        ("MOCKUP B", "Industrial Procurement", C["accent_b"]),
    ]

    for i, (title, sub, accent) in enumerate(titles):
        cx = col_x(i)
        parts.append(f'{rect(cx, y0, col_w, 36, fill=accent, stroke=accent)}')
        parts.append(text(cx + col_w / 2, y0 + 16, title, size=12, weight="bold", fill="#fff", anchor="middle"))
        parts.append(text(cx + col_w / 2, y0 + 30, sub, size=9, fill="#eee", anchor="middle"))

    y = y0 + 44
    for i in range(3):
        cx = col_x(i)
        parts.append(label_block(cx, y, col_w, 32, "Breadcrumb"))

    y += 40

    # Column-specific hero layouts
    # CURRENT
    cx = col_x(0)
    gal_w = int(col_w * 0.42)
    info_w = col_w - gal_w - 8
    parts.append(f'{rect(cx, y, col_w, hero_h, fill=C["fill_hero"])}')
    parts.append(label_block(cx + 6, y + 8, gal_w - 12, hero_h - 16, "GALLERY", ["~520px · 1 image", "HIGH void WH-16"], fill=C["fill_gallery"]))
    ix = cx + gal_w + 4
    parts.append(label_block(ix, y + 8, info_w - 8, 48, "H1 + placeholder", ["AssuM · mini-desc"]))
    parts.append(label_block(ix, y + 60, info_w - 8, 32, "Article"))
    parts.append(label_block(ix, y + 96, info_w - 8, 72, "BUY BOX", ["price · CTA"], fill=C["fill_ok"]))
    parts.append(label_block(ix, y + 174, info_w - 8, 28, "icons only"))
    parts.append(label_block(ix, y + 206, info_w - 8, 48, "4 dims only", ["L W H mass"], fill=C["fill_warn"]))
    parts.append(label_block(cx, y + hero_h + 6, col_w, 40, "TABS — 2/3 hidden", fill=C["fill_warn"]))
    parts.append(text(cx + 8, y + hero_h + 58, "~6 facts · series in breadcrumb only", size=9, fill=C["accent_current"]))

    # MOCKUP A
    cx = col_x(1)
    gal_w = int(col_w * 0.40)
    info_w = col_w - gal_w - 8
    parts.append(f'{rect(cx, y, col_w, hero_h, fill=C["fill_hero"])}')
    parts.append(label_block(cx + 6, y + 8, gal_w - 12, hero_h - 16, "MEDIA ~40%", ["thumbnails"], fill=C["fill_gallery"]))
    ix = cx + gal_w + 4
    parts.append(label_block(ix, y + 8, info_w - 8, 40, "H1 + article"))
    parts.append(label_block(ix, y + 52, info_w - 8, 28, "Series line", ["ПРЕМИУМ-3 →"]))
    parts.append(label_block(ix, y + 84, info_w - 8, 72, "BUY BOX", ["familiar right column"], fill=C["fill_ok"]))
    parts.append(label_block(ix, y + 160, info_w - 8, 28, "labeled actions"))
    parts.append(label_block(cx, y + hero_h - 52, col_w - 12, 44, "FIT STRIP (8 attrs)", ["compact horizontal row"]))
    parts.append(text(cx + 8, y + hero_h + 58, "~14 facts · min spec on scroll", size=9, fill=C["accent_a"]))

    # MOCKUP B — series band between breadcrumb and hero
    cx = col_x(2)
    band_y = y
    parts.append(label_block(cx, band_y, col_w, 40, "SERIES BAND", ["full-width · dominant · USR-PDP-02"], fill=C["fill_band"]))
    hero_y_b = band_y + 46
    hero_h_b = hero_h - 46
    parts.append(f'{rect(cx, hero_y_b, col_w, hero_h_b, fill=C["fill_hero"])}')
    parts.append(label_block(cx + 6, hero_y_b + 8, 90, hero_h_b - 16, "MEDIA", ["~25%", "thumb"], fill=C["fill_gallery"]))
    px = cx + 100
    pw = col_w - 106
    parts.append(label_block(px, hero_y_b + 8, pw, 36, "H1 + article + OEM"))
    parts.append(label_block(px, hero_y_b + 48, pw, 64, "FIT GRID 2×4", ["dense attribute table"]))
    parts.append(label_block(px, hero_y_b + 116, pw, hero_h_b - 124, "COMMERCIAL ROW", ["CTA + compare + delivery + dealer"], fill=C["fill_ok"]))
    parts.append(text(cx + 8, y + hero_h + 58, "~18–20 facts · B2B inline", size=9, fill=C["accent_b"]))

    fold_y = y + hero_h + 72
    for i in range(3):
        parts.append(fold_line(fold_y, col_x(i), col_x(i) + col_w, "FOLD"))

    # Legend row
    ly = fold_y + 20
    parts.append(f'{rect(mx, ly, W - 60, 120, fill=C["page"], stroke=C["stroke_light"], sw=1)}')
    parts.append(text(mx + 16, ly + 22, "Shared IA (unchanged in A & B): USR-PDP-00–21 · Same decision ladder · In-series alts replace «Похожие»", size=10, weight="bold"))
    legend = [
        "Series visibility:  Current breadcrumb only  →  A: line under H1  →  B: prominent band",
        "Fit validation:     Current 4 dims  →  A: chip strip  →  B: 2×4 grid",
        "Specs packaging:    Current hidden tabs  →  A & B: min spec default-visible + collapsed full spec",
        "Alternatives:       Current cross-family «Похожие»  →  A & B: in-series only (USR-PDP-12)",
    ]
    for i, line in enumerate(legend):
        parts.append(text(mx + 16, ly + 42 + i * 18, line, size=9, fill=C["text_muted"]))

    parts.append(text(mx, ly + 130, "Sources: BZPM-PDP-WIREFRAME-ALPHA-v1 · BZPM-PDP-MOCKUP-A-v1 · BZPM-PDP-MOCKUP-B-v1 · BZPM-PDP-MOCKUP-COMPARISON-v1", size=9, fill=C["text_muted"]))

    H = ly + 160
    return svg_wrap(W, H, "\n  ".join(parts), "BZPM PDP Desktop Comparison")


def main():
    files = {
        "BZPM-PDP-SCHEMATIC-CURRENT-v1.svg": schematic_current(),
        "BZPM-PDP-SCHEMATIC-MOCKUP-A-v1.svg": schematic_mockup_a(),
        "BZPM-PDP-SCHEMATIC-MOCKUP-B-v1.svg": schematic_mockup_b(),
        "BZPM-PDP-SCHEMATIC-COMPARISON-v1.svg": schematic_comparison(),
    }
    for name, content in files.items():
        path = OUT / name
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate BZPM PDP Hi-Fi Alpha visual renders — stakeholder review artifacts."""

from pathlib import Path

OUT = Path(__file__).resolve().parent

# Hi-Fi palette — industrial OEM B2B (from BZPM-PDP-HIFI-ALPHA-v1)
P = {
    "page_bg": "#F4F5F7",
    "card": "#FFFFFF",
    "border": "#DDE1E6",
    "border_light": "#E8EAED",
    "text": "#1A1F26",
    "text_secondary": "#4A5568",
    "text_muted": "#6B7280",
    "text_label": "#9CA3AF",
    "brand": "#1E5A8A",
    "brand_dark": "#164A72",
    "brand_light": "#E8EEF5",
    "series_tint": "#EEF2F7",
    "stock": "#2D7A4F",
    "stock_bg": "#EDF7F1",
    "stock_order": "#B8860B",
    "price": "#1A1F26",
    "header_bg": "#FFFFFF",
    "header_border": "#DDE1E6",
    "footer_bg": "#2C3440",
    "footer_text": "#A0A8B4",
    "media_bg": "#ECEEF1",
    "media_stroke": "#C5CAD1",
    "chip_bg": "#FAFBFC",
    "shadow": "0 1px 3px rgba(26,31,38,0.08)",
    "cta": "#1E5A8A",
    "link": "#1E5A8A",
    "divider": "#E8EAED",
}

FONT = "Segoe UI, Arial, sans-serif"
MONO = "Consolas, 'Courier New', monospace"


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def svg_open(w, h, title):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <title>{esc(title)}</title>
  <defs>
    <filter id="cardShadow" x="-2%" y="-2%" width="104%" height="108%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#1A1F26" flood-opacity="0.08"/>
    </filter>
    <linearGradient id="productGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D8DCE2"/>
      <stop offset="100%" stop-color="#C0C6CE"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="{P['page_bg']}"/>
'''


def svg_close():
    return "</svg>\n"


def r(x, y, w, h, fill=P["card"], stroke=P["border"], sw=1, rx=5, opacity=1, filt=None):
    f = f' filter="url(#cardShadow)"' if filt else ""
    o = f' opacity="{opacity}"' if opacity != 1 else ""
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{o}{f}/>'
    )


def t(x, y, s, size=14, weight="normal", fill=P["text"], anchor="start", family=FONT, letter_spacing=None):
    ls = f' letter-spacing="{letter_spacing}"' if letter_spacing else ""
    return (
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{ls}>{esc(s)}</text>'
    )


def line(x1, y1, x2, y2, stroke=P["divider"], sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def btn(x, y, w, h, label, fill=P["cta"], text_fill="#FFFFFF", rx=5, size=13):
    return (
        f'{r(x, y, w, h, fill=fill, stroke=fill, rx=rx)}\n'
        f'  {t(x + w / 2, y + h / 2 + 5, label, size=size, weight="600", fill=text_fill, anchor="middle")}'
    )


def ghost_btn(x, y, w, h, label, rx=5):
    return (
        f'{r(x, y, w, h, fill=P["card"], stroke=P["border"], rx=rx)}\n'
        f'  {t(x + w / 2, y + h / 2 + 5, label, size=12, weight="500", fill=P["text_secondary"], anchor="middle")}'
    )


def label_caps(x, y, s):
    return t(x, y, s.upper(), size=10, weight="600", fill=P["text_label"], letter_spacing="0.06em")


def spec_row(x, y, w, key, val, row_h=32):
    parts = [
        line(x, y + row_h, x + w, y + row_h, stroke=P["border_light"]),
        t(x + 16, y + 21, key, size=13, fill=P["text_secondary"]),
        t(x + w - 16, y + 21, val, size=13, weight="500", fill=P["text"], anchor="end"),
    ]
    return "\n  ".join(parts)


def grid_cell(x, y, w, h, label, value):
    parts = [
        r(x, y, w, h, fill=P["chip_bg"], stroke=P["border_light"], rx=4),
        label_caps(x + 10, y + 16, label),
        t(x + 10, y + 34, value, size=14, weight="500"),
    ]
    return "\n  ".join(parts)


def product_silhouette(x, y, w, h):
    """Stylized stainless sink illustration."""
    cx = x + w / 2
    return f'''
  {r(x, y, w, h, fill=P["media_bg"], stroke=P["media_stroke"], rx=4)}
  <rect x="{x + 20}" y="{y + 24}" width="{w - 40}" height="{h - 48}" rx="3" fill="url(#productGrad)" stroke="#A8B0BA" stroke-width="1"/>
  <rect x="{x + 28}" y="{y + 36}" width="{(w - 56) / 2 - 4}" height="{h * 0.35}" rx="2" fill="#B8BEC8" stroke="#9AA3AD" stroke-width="0.8"/>
  <rect x="{x + 28 + (w - 56) / 2 + 4}" y="{y + 36}" width="{(w - 56) / 2 - 4}" height="{h * 0.35}" rx="2" fill="#B8BEC8" stroke="#9AA3AD" stroke-width="0.8"/>
  <ellipse cx="{cx}" cy="{y + h - 28}" rx="18" ry="6" fill="#A0A8B0" opacity="0.5"/>
  {t(cx, y + h - 12, "ВМЦ-П3-2/500", size=9, fill=P["text_muted"], anchor="middle", family=MONO)}
'''


def thumb(x, y, active=False):
    fill = P["card"] if active else P["media_bg"]
    stroke = P["brand"] if active else P["media_stroke"]
    sw = 2 if active else 1
    return r(x, y, 52, 40, fill=fill, stroke=stroke, sw=sw, rx=3)


def sibling_card(x, y, w, article, dims, secs, price, status, status_color, in_stock=True):
    h = 168
    parts = [
        r(x, y, w, h, fill=P["card"], stroke=P["border"], rx=5, filt=True),
        r(x + 8, y + 8, w - 16, 64, fill=P["media_bg"], stroke=P["media_stroke"], rx=3),
        t(x + w / 2, y + 44, article, size=10, fill=P["text_muted"], anchor="middle", family=MONO),
        t(x + 12, y + 88, article, size=12, weight="600", family=MONO),
        t(x + 12, y + 106, dims, size=11, fill=P["text_secondary"]),
        t(x + 12, y + 122, secs, size=11, fill=P["text_secondary"]),
        t(x + 12, y + 142, price, size=13, weight="700", fill=P["price"]),
        t(x + 12, y + 160, status, size=10, weight="500", fill=status_color),
    ]
    if in_stock:
        parts.insert(-1, f'<circle cx="{x + 18}" cy="{y + 154}" r="3" fill="{status_color}"/>')
    else:
        parts.insert(-1, f'<circle cx="{x + 22}" cy="{y + 154}" r="3" fill="{status_color}"/>')
    return "\n  ".join(parts)


def desktop_header(cx, content_w):
    x = cx
    parts = [
        r(x, 0, content_w, 64, fill=P["header_bg"], stroke="none", rx=0),
        line(x, 64, x + content_w, 64, stroke=P["header_border"]),
        t(x + 24, 40, "BZPM", size=20, weight="700", fill=P["brand"]),
        t(x + 100, 40, "Каталог", size=13, fill=P["text_secondary"]),
        t(x + 180, 40, "Поиск", size=13, fill=P["text_secondary"]),
        t(x + 250, 40, "Дилерам", size=13, fill=P["text_secondary"]),
        r(x + content_w - 180, 18, 156, 32, fill=P["page_bg"], stroke=P["border"], rx=16),
        t(x + content_w - 102, 40, "🔍  Поиск по каталогу…", size=11, fill=P["text_muted"]),
        t(x + content_w - 48, 40, "🛒", size=16, anchor="middle"),
    ]
    return "\n  ".join(parts)


def desktop_footer(cx, y, content_w):
    h = 96
    parts = [
        r(cx, y, content_w, h, fill=P["footer_bg"], stroke="none", rx=0),
        t(cx + 24, y + 32, "© Завод профессионального оборудования · BZPM", size=11, fill=P["footer_text"]),
        t(cx + 24, y + 52, "Каталог · Доставка · Гарантия · Контакты · Политика конфиденциальности", size=10, fill="#6B7280"),
        t(cx + 24, y + 72, "8 (800) 000-00-00  ·  info@bzpm.ru", size=10, fill="#6B7280"),
    ]
    return "\n  ".join(parts)


def product_context_block_desktop(cx, y, cw, mode=1):
    """Universal Product Context Block — Mode 1 shown for reference SKU."""
    band_h = 56
    parts = [
        t(cx + 24, y - 2, "Product Context · Mode 1 (Series)", size=8, fill="#9CA3AF"),
        f'<rect x="{cx}" y="{y + 6}" width="4" height="{band_h}" fill="{P["brand"]}" rx="0"/>',
        r(cx, y + 6, cw, band_h, fill=P["series_tint"], stroke=P["border_light"], rx=5),
        t(cx + 20, y + 28, "Серия ПРЕМИУМ-3", size=14, weight="700", fill=P["brand"]),
        t(cx + 200, y + 28, "Цельнотянутые моечные ванны", size=13, fill=P["text_secondary"]),
        t(cx + 20, y + 48, "10 моделей в серии", size=11, weight="500", fill=P["link"]),
    ]
    return "\n  ".join(parts), band_h + 22


def product_context_block_mobile(m, y, cw, mode=1):
    """Compact Product Context Block for mobile P1."""
    band_h = 64
    parts = [
        t(m, y, "Product Context · Mode 1", size=7, fill="#9CA3AF"),
        f'<rect x="{m}" y="{y + 8}" width="3" height="{band_h}" fill="{P["brand"]}"/>',
        r(m, y + 8, cw, band_h, fill=P["series_tint"], stroke=P["border_light"], rx=5),
        t(m + 14, y + 30, "Серия ПРЕМИУМ-3", size=13, weight="700", fill=P["brand"]),
        t(m + 14, y + 48, "Цельнотянутые моечные ванны", size=11, fill=P["text_secondary"]),
        t(m + 14, y + 64, "10 моделей в серии", size=10, weight="500", fill=P["link"]),
    ]
    return "\n  ".join(parts), band_h + 16


def legend_note_desktop(cx, y, cw):
    parts = [
        r(cx, y, cw, 36, fill="#FAFBFC", stroke=P["border_light"], rx=4),
        t(
            cx + 16,
            y + 22,
            "Блок условный: серия / линейка / группа. Если контекста нет — скрывается.",
            size=10,
            fill=P["text_muted"],
        ),
    ]
    return "\n  ".join(parts), 44


def legend_note_mobile(m, y, cw):
    parts = [
        t(
            m,
            y + 10,
            "Блок условный: серия / линейка / группа. Если контекста нет — скрывается.",
            size=8,
            fill=P["text_muted"],
        ),
    ]
    return "\n  ".join(parts), 20


def compact_gallery_mobile(m, y, cw, height=148):
    parts = [
        product_silhouette(m, y, cw, height),
    ]
    for i, tx in enumerate([m, m + 58, m + 116]):
        parts.append(thumb(tx, y + height + 8, active=(i == 0)))
    return "\n  ".join(parts), height + 56


def generate_desktop(version="v1"):
    W = 1440
    CW = 1200
    CX = (W - CW) // 2
    H = 2720 if version == "v2" else 2680
    title = "BZPM PDP Hi-Fi Alpha — Desktop" + (" · v2" if version == "v2" else "")
    parts = [svg_open(W, H, title)]

    y = 0
    parts.append(desktop_header(CX, CW))
    y = 80

    # Breadcrumb
    parts.append(t(CX + 24, y + 16, "Главная  ›  Каталог  ›  Нейтральное  ›  Моечные ванны  ›  ПРЕМИУМ-3  ›  ВМЦ-П3-2/500", size=12, fill=P["text_muted"]))
    y += 36

    if version == "v2":
        ctx, ctx_h = product_context_block_desktop(CX, y, CW)
        parts.append(ctx)
        y += ctx_h
    else:
        # Series band (v1)
        band_h = 60
        parts.append(f'<rect x="{CX}" y="{y}" width="4" height="{band_h}" fill="{P["brand"]}" rx="0"/>')
        parts.append(r(CX, y, CW, band_h, fill=P["series_tint"], stroke=P["border_light"], rx=5))
        parts.append(label_caps(CX + 20, y + 22, "Серия"))
        parts.append(t(CX + 72, y + 22, "ПРЕМИУМ-3", size=15, weight="700", fill=P["brand"]))
        parts.append(t(CX + 200, y + 22, "Цельнотянутые ванны премиум-класса", size=13, fill=P["text_secondary"]))
        parts.append(r(CX + 20, y + 34, 168, 22, fill=P["card"], stroke=P["brand"], rx=4))
        parts.append(t(CX + 104, y + 50, "Все модели серии (10) →", size=11, weight="500", fill=P["brand"], anchor="middle"))
        parts.append(t(CX + 220, y + 50, "См. также:", size=11, fill=P["text_muted"]))
        parts.append(t(CX + 300, y + 50, "ПРЕМИУМ", size=11, weight="500", fill=P["link"]))
        parts.append(t(CX + 380, y + 50, "СТАНДАРТ", size=11, weight="500", fill=P["link"]))
        y += band_h + 16

    # Hero card
    hero_h = 468
    parts.append(r(CX, y, CW, hero_h, fill=P["card"], stroke=P["border"], rx=6, filt=True))

    media_w = int(CW * 0.30) - 32
    media_x = CX + 16
    media_y = y + 16
    media_h = 280
    parts.append(product_silhouette(media_x, media_y, media_w, media_h))
    for i, tx in enumerate([media_x, media_x + 58, media_x + 116]):
        parts.append(thumb(tx, media_y + media_h + 12, active=(i == 0)))

    data_x = CX + media_w + 32
    data_w = CW - media_w - 48

    # Identity
    parts.append(t(data_x, y + 36, "Ванна моечная цельнотянутая 2-секционная 500×400 мм,", size=22, weight="600"))
    parts.append(t(data_x, y + 62, "левая/правая чаша", size=22, weight="600"))
    parts.append(t(data_x, y + 92, "Артикул", size=11, fill=P["text_muted"]))
    parts.append(t(data_x + 58, y + 92, "ВМЦ-П3-2/500", size=14, weight="600", family=MONO))
    parts.append(r(data_x + 200, y + 78, 28, 22, fill=P["page_bg"], stroke=P["border"], rx=3))
    parts.append(t(data_x + 214, y + 94, "⧉", size=12, fill=P["text_muted"], anchor="middle"))
    parts.append(t(data_x + 250, y + 92, "ЗПМ · OEM", size=11, weight="500", fill=P["text_muted"]))

    # Fit grid 4x2
    gy = y + 108
    gw = (data_w - 24) // 4
    gh = 52
    grid_data = [
        ("L", "1150 мм"), ("W", "700 мм"), ("H", "850 мм"), ("Масса", "68 кг"),
        ("Секций", "2"), ("Чаша", "500×400"), ("Материал", "AISI 304"), ("Конструкция", "Цельнотян."),
    ]
    for i, (lbl, val) in enumerate(grid_data):
        col = i % 4
        row = i // 4
        parts.append(grid_cell(data_x + col * (gw + 8), gy + row * (gh + 8), gw, gh, lbl, val))

    # Buy row
    buy_y = y + 248
    buy_w = 300
    buy_x = data_x
    parts.append(r(buy_x, buy_y, buy_w, 200, fill=P["card"], stroke=P["border"], rx=6, filt=True))
    parts.append(f'<circle cx="{buy_x + 20}" cy="{buy_y + 28}" r="4" fill="{P["stock"]}"/>')
    parts.append(t(buy_x + 32, buy_y + 32, "В наличии · 3 шт.", size=12, weight="500", fill=P["stock"]))
    parts.append(t(buy_x + 20, buy_y + 68, "142 500 ₽", size=30, weight="700"))
    parts.append(t(buy_x + 20, buy_y + 92, "Цена с НДС", size=10, fill=P["text_muted"]))
    # qty
    parts.append(r(buy_x + 20, buy_y + 108, 120, 36, fill=P["page_bg"], stroke=P["border"], rx=4))
    parts.append(t(buy_x + 38, buy_y + 132, "−", size=16, fill=P["text_muted"]))
    parts.append(t(buy_x + 80, buy_y + 132, "1", size=14, weight="600", anchor="middle"))
    parts.append(t(buy_x + 118, buy_y + 132, "+", size=16, fill=P["text_muted"], anchor="end"))
    parts.append(btn(buy_x + 20, buy_y + 156, buy_w - 40, 44, "В КОРЗИНУ", size=14))

    # Actions + B2B
    act_x = buy_x + buy_w + 24
    act_w = data_w - buy_w - 24
    parts.append(ghost_btn(act_x, buy_y + 8, 110, 36, "Сравнить"))
    parts.append(ghost_btn(act_x + 118, buy_y + 8, 120, 36, "В избранное"))
    parts.append(t(act_x, buy_y + 68, "Доставка:", size=13, fill=P["text_secondary"]))
    parts.append(t(act_x + 78, buy_y + 68, "от 3 дн.", size=13, weight="600", fill=P["link"]))
    parts.append(t(act_x + 148, buy_y + 68, "→", size=13, fill=P["link"]))
    parts.append(t(act_x, buy_y + 96, "Купить как дилер", size=13, weight="500", fill=P["link"]))
    parts.append(t(act_x + 130, buy_y + 96, "→", size=13, fill=P["link"]))

    y += hero_h + 24

    # Fold indicator
    parts.append(line(CX, y - 8, CX + CW, y - 8, stroke="#CC4444", sw=1.5, dash="6,4"))
    parts.append(t(CX + CW / 2, y - 14, "— first scroll —", size=10, weight="600", fill="#CC4444", anchor="middle"))

    # Min spec
    ms_h = 248
    parts.append(r(CX, y, CW, ms_h, fill=P["card"], stroke=P["border"], rx=6, filt=True))
    parts.append(t(CX + 24, y + 32, "Ключевые параметры", size=16, weight="600"))
    parts.append(line(CX + 24, y + 44, CX + CW - 24, y + 44, stroke=P["divider"]))
    spec_data = [
        ("Количество секций", "2"),
        ("Материал", "AISI 304"),
        ("Тип конструкции", "Цельнотянутая"),
        ("Вес нетто", "65 кг"),
        ("Вес брутто", "72 кг"),
        ("Габариты упаковки", "1200 × 750 × 900 мм"),
        ("Гарантия", "24 мес."),
    ]
    for i, (k, v) in enumerate(spec_data):
        parts.append(spec_row(CX + 8, y + 52 + i * 28, CW - 16, k, v, row_h=28))
    y += ms_h + 20

    # Description
    desc_h = 120
    parts.append(r(CX, y, CW, desc_h, fill=P["card"], stroke=P["border"], rx=6, filt=True))
    parts.append(t(CX + 24, y + 32, "Моечная ванна цельнотянутая двухсекционная для профессиональных кухонь,", size=14, fill=P["text_secondary"]))
    parts.append(t(CX + 24, y + 52, "столовых и пищеблоков. Левая и правая чаша 500×400 мм.", size=14, fill=P["text_secondary"]))
    parts.append(t(CX + 24, y + 72, "Комплектация: ванна, сифон, крепёжный комплект. Ключевое отличие серии ПРЕМИУМ-3 —", size=14, fill=P["text_secondary"]))
    parts.append(t(CX + 24, y + 92, "цельнотянутая конструкция без сварных швов в чаше.", size=14, fill=P["text_secondary"]))
    parts.append(t(CX + 24, y + 112, "Показать полностью ▼", size=12, weight="500", fill=P["link"]))
    y += desc_h + 16

    # Consult
    parts.append(t(CX + 24, y + 16, "Задать вопрос", size=13, weight="500", fill=P["link"]))
    parts.append(t(CX + 140, y + 16, "Поможем подобрать", size=13, weight="500", fill=P["link"]))
    y += 36

    # Full specs collapsed
    parts.append(r(CX, y, CW, 44, fill=P["page_bg"], stroke=P["border"], rx=5))
    parts.append(t(CX + 24, y + 28, "Характеристики — развернуть все 24 параметра ▼", size=13, weight="500", fill=P["text_secondary"]))
    y += 56

    # Documents
    parts.append(t(CX + 24, y + 8, "Документы", size=14, weight="600"))
    parts.append(t(CX + 24, y + 32, "📄  Паспорт ВМЦ-П3.pdf", size=13, fill=P["link"]))
    parts.append(t(CX + 220, y + 32, "📄  Сертификат соответствия.pdf", size=13, fill=P["link"]))
    y += 56

    # In-series alternatives
    alt_h = 220
    parts.append(r(CX, y, CW, alt_h, fill=P["card"], stroke=P["border"], rx=6, filt=True))
    parts.append(t(CX + 24, y + 32, "Другие модели серии ПРЕМИУМ-3", size=16, weight="600"))
    siblings = [
        ("ВМЦ-П3-1/500", "1150×600", "1 сек", "98 200 ₽", "● В наличии", P["stock"], True),
        ("ВМЦ-П3-2/600", "1400×700", "2 сек", "156 800 ₽", "● Под заказ", P["stock_order"], False),
        ("ВМЦ-П3-3/500", "1150×700", "3 сек", "178 400 ₽", "● В наличии", P["stock"], True),
        ("ВМЦ-П3-2/700", "1400×850", "2 сек", "189 500 ₽", "● В наличии", P["stock"], True),
        ("ВМЦ-П3-1/600", "1150×600", "1 сек", "94 100 ₽", "● В наличии", P["stock"], True),
    ]
    card_w = 196
    for i, sib in enumerate(siblings):
        parts.append(sibling_card(CX + 24 + i * (card_w + 12), y + 48, card_w, *sib))
    parts.append(t(CX + CW - 32, y + 130, "→", size=20, fill=P["text_muted"], anchor="middle"))
    y += alt_h + 20

    # Return to series
    parts.append(t(CX + 24, y + 16, "← Вернуться к серии ПРЕМИУМ-3", size=13, weight="500", fill=P["link"]))
    y += 36

    # Related equipment
    parts.append(t(CX + 24, y + 8, "Сопутствующее оборудование", size=14, weight="600"))
    for i, (name, price) in enumerate([("Сифон DN50 нержавеющий", "4 200 ₽"), ("Крепёжный комплект ВМЦ", "2 800 ₽")]):
        rx = CX + 24 + i * 280
        parts.append(r(rx, y + 24, 260, 72, fill=P["card"], stroke=P["border"], rx=5))
        parts.append(t(rx + 16, y + 52, name, size=12, weight="500"))
        parts.append(t(rx + 16, y + 72, price, size=13, weight="600"))
    y += 112

    # Commercial support / trust (USR-PDP-20/21)
    parts.append(r(CX, y, CW, 56, fill=P["brand_light"], stroke=P["border_light"], rx=5))
    parts.append(t(CX + 24, y + 34, "Гарантия производителя · Сертифицированное оборудование · Доставка по РФ · B2B-консультация", size=12, fill=P["text_secondary"]))
    y += 72

    if version == "v2":
        legend, legend_h = legend_note_desktop(CX, y, CW)
        parts.append(legend)
        y += legend_h

    parts.append(desktop_footer(CX, y, CW))

    # Watermark
    wm = "Hi-Fi Alpha v2 · Concept only · Not implementation" if version == "v2" else "Hi-Fi Alpha v1 · Concept only · Not implementation"
    parts.append(t(CX + CW - 24, H - 16, wm, size=9, fill=P["text_muted"], anchor="end"))

    parts.append(svg_close())
    suffix = version
    path = OUT / f"BZPM-PDP-HIFI-ALPHA-DESKTOP-{suffix}.svg"
    path.write_text("\n  ".join(parts), encoding="utf-8")
    print(f"Wrote {path}")


def mobile_header(page_w):
    parts = [
        r(0, 0, page_w, 52, fill=P["header_bg"], stroke="none", rx=0),
        line(0, 52, page_w, 52, stroke=P["header_border"]),
        t(16, 32, "☰", size=16),
        t(44, 32, "BZPM", size=16, weight="700", fill=P["brand"]),
        t(page_w - 24, 32, "🛒", size=16, anchor="middle"),
    ]
    return "\n  ".join(parts)


def generate_mobile(version="v1"):
    W = 390
    M = 16
    CW = W - 2 * M
    H = 2520 if version == "v2" else 2480
    title = "BZPM PDP Hi-Fi Alpha — Mobile" + (" · v2" if version == "v2" else "")
    parts = [svg_open(W, H, title)]

    y = 0
    parts.append(mobile_header(W))
    y = 64

    # Breadcrumb truncated
    parts.append(t(M + 4, y + 14, "… › ПРЕМИУМ-3 › ВМЦ-П3-2/500", size=11, fill=P["text_muted"]))
    y += 28

    if version == "v2":
        # ── P1: Context → Identity → Gallery → Commercial ──
        parts.append(t(M, y + 4, "P1 — CRITICAL", size=9, weight="700", fill=P["brand"], letter_spacing="0.05em"))
        y += 16

        ctx, ctx_h = product_context_block_mobile(M, y, CW)
        parts.append(ctx)
        y += ctx_h + 4

        parts.append(t(M, y + 4, "ВМЦ-П3-2/500", size=13, weight="600", family=MONO))
        parts.append(t(M + 130, y + 4, "⧉", size=12, fill=P["text_muted"]))
        parts.append(t(M, y + 28, "Ванна моечная цельнотянутая", size=18, weight="600"))
        parts.append(t(M, y + 50, "2-секционная 500×400 мм", size=18, weight="600"))
        y += 64

        gal, gal_h = compact_gallery_mobile(M, y, CW, height=140)
        parts.append(gal)
        y += gal_h + 8

        parts.append(r(M, y, CW, 152, fill=P["card"], stroke=P["border"], rx=6, filt=True))
        parts.append(f'<circle cx="{M + 20}" cy="{y + 24}" r="4" fill="{P["stock"]}"/>')
        parts.append(t(M + 32, y + 28, "В наличии · 3 шт.", size=12, weight="500", fill=P["stock"]))
        parts.append(t(M + 20, y + 56, "142 500 ₽", size=28, weight="700"))
        parts.append(r(M + 20, y + 76, 100, 32, fill=P["page_bg"], stroke=P["border"], rx=4))
        parts.append(t(M + 38, y + 98, "−", size=16, fill=P["text_muted"]))
        parts.append(t(M + 70, y + 98, "1", size=14, weight="600", anchor="middle"))
        parts.append(t(M + 102, y + 98, "+", size=16, fill=P["text_muted"], anchor="end"))
        parts.append(btn(M + 20, y + 112, CW - 40, 40, "В КОРЗИНУ", size=14))
        y += 164

        parts.append(t(M, y + 8, "Доставка от 3 дн. →", size=12, weight="500", fill=P["link"]))
        parts.append(t(M, y + 28, "Купить как дилер →", size=12, weight="500", fill=P["link"]))
        y += 44

        # ── P2: Fit Verification + Critical properties ──
        parts.append(line(M, y, M + CW, y, stroke=P["divider"], sw=2))
        parts.append(t(M, y + 16, "P2 — HIGH", size=9, weight="700", fill=P["brand"], letter_spacing="0.05em"))
        y += 28

        gw = (CW - 8) // 2
        gh = 48
        grid_data = [
            ("L", "1150 мм"), ("W", "700 мм"),
            ("H", "850 мм"), ("Масса", "68 кг"),
            ("Секций", "2"), ("Чаша", "500×400"),
            ("Материал", "AISI 304"), ("Конструкция", "Цельнотян."),
        ]
        for i, (lbl, val) in enumerate(grid_data):
            col = i % 2
            row = i // 2
            parts.append(grid_cell(M + col * (gw + 8), y + row * (gh + 6), gw, gh, lbl, val))
        y += 4 * (gh + 6) + 12

        parts.append(ghost_btn(M, y, (CW - 8) // 2, 40, "Сравнить"))
        parts.append(ghost_btn(M + (CW - 8) // 2 + 8, y, (CW - 8) // 2, 40, "Избранное"))
        y += 52

        ms_h = 196
        parts.append(r(M, y, CW, ms_h, fill=P["card"], stroke=P["border"], rx=6, filt=True))
        parts.append(t(M + 16, y + 28, "Ключевые параметры", size=15, weight="600"))
        for i, (k, v) in enumerate([
            ("Количество секций", "2"), ("Материал", "AISI 304"),
            ("Тип конструкции", "Цельнотянутая"), ("Вес нетто", "65 кг"), ("Гарантия", "24 мес."),
        ]):
            parts.append(spec_row(M, y + 36 + i * 32, CW, k, v))
        y += ms_h + 16

        # ── P3: Min Spec Summary (description) ──
        parts.append(line(M, y, M + CW, y, stroke=P["divider"], sw=2))
        parts.append(t(M, y + 16, "P3 — MEDIUM", size=9, weight="700", fill=P["brand"], letter_spacing="0.05em"))
        y += 28
        parts.append(t(M, y + 4, "Моечная ванна цельнотянутая двухсекционная для профессиональных кухонь…", size=13, fill=P["text_secondary"]))
        parts.append(t(M, y + 24, "Комплектация: ванна, сифон, крепёжный комплект.", size=13, fill=P["text_secondary"]))
        parts.append(t(M, y + 44, "Показать полностью ▼", size=12, weight="500", fill=P["link"]))
        y += 64

        # ── P4: Full specs + Documents ──
        parts.append(line(M, y, M + CW, y, stroke=P["divider"], sw=2))
        parts.append(t(M, y + 16, "P4 — LOWER", size=9, weight="700", fill=P["brand"], letter_spacing="0.05em"))
        y += 28
        parts.append(r(M, y, CW, 40, fill=P["page_bg"], stroke=P["border"], rx=5))
        parts.append(t(M + 16, y + 26, "Характеристики — 24 параметра ▼", size=12, fill=P["text_secondary"]))
        y += 52
        parts.append(t(M, y + 4, "📄  Паспорт ВМЦ-П3.pdf", size=12, fill=P["link"]))
        parts.append(t(M, y + 24, "📄  Сертификат соответствия.pdf", size=12, fill=P["link"]))
        y += 48

        # ── P5: Alternatives + Commercial support ──
        parts.append(line(M, y, M + CW, y, stroke=P["divider"], sw=2))
        parts.append(t(M, y + 16, "P5 — COLLAPSE", size=9, weight="700", fill=P["text_muted"], letter_spacing="0.05em"))
        y += 28
        parts.append(t(M, y + 4, "Другие модели серии ПРЕМИУМ-3", size=14, weight="600"))
        y += 24
        card_w = 156
        for i, sib in enumerate([
            ("ВМЦ-П3-1/500", "1150×600", "1 сек", "98 200 ₽", "● В наличии", P["stock"], True),
            ("ВМЦ-П3-2/600", "1400×700", "2 сек", "156 800 ₽", "● Под заказ", P["stock_order"], False),
        ]):
            parts.append(sibling_card(M + i * (card_w + 10), y, card_w, *sib))
        y += 180

        parts.append(t(M, y + 8, "← Вернуться к серии ПРЕМИУМ-3", size=12, fill=P["link"]))
        y += 28
        parts.append(t(M, y + 4, "Задать вопрос  ·  Поможем подобрать", size=12, fill=P["link"]))
        y += 24
        parts.append(t(M, y + 4, "Сопутствующее оборудование (2)", size=12, weight="500", fill=P["text_secondary"]))
        y += 20
        legend, legend_h = legend_note_mobile(M, y, CW)
        parts.append(legend)
        y += legend_h
        parts.append(r(M, y, CW, 48, fill=P["footer_bg"], stroke="none", rx=5))
        parts.append(t(M + 16, y + 30, "© BZPM · 8 (800) 000-00-00", size=10, fill=P["footer_text"]))

        parts.append(t(M + CW, H - 12, "Hi-Fi Alpha · Mobile · v2", size=8, fill=P["text_muted"], anchor="end"))
    else:
        # P1 label
        parts.append(t(M, y + 4, "P1 — CRITICAL", size=9, weight="700", fill=P["brand"], letter_spacing="0.05em"))
        y += 16

        # Commercial first (v1)
        parts.append(r(M, y, CW, 168, fill=P["card"], stroke=P["border"], rx=6, filt=True))
        parts.append(f'<circle cx="{M + 20}" cy="{y + 28}" r="4" fill="{P["stock"]}"/>')
        parts.append(t(M + 32, y + 32, "В наличии · 3 шт.", size=12, weight="500", fill=P["stock"]))
        parts.append(t(M + 20, y + 64, "142 500 ₽", size=28, weight="700"))
        parts.append(r(M + 20, y + 84, 100, 36, fill=P["page_bg"], stroke=P["border"], rx=4))
        parts.append(t(M + 38, y + 108, "−", size=16, fill=P["text_muted"]))
        parts.append(t(M + 70, y + 108, "1", size=14, weight="600", anchor="middle"))
        parts.append(t(M + 102, y + 108, "+", size=16, fill=P["text_muted"], anchor="end"))
        parts.append(btn(M + 20, y + 128, CW - 40, 44, "В КОРЗИНУ", size=14))
        y += 180

        band_h = 72
        parts.append(f'<rect x="{M}" y="{y}" width="3" height="{band_h}" fill="{P["brand"]}"/>')
        parts.append(r(M, y, CW, band_h, fill=P["series_tint"], stroke=P["border_light"], rx=5))
        parts.append(label_caps(M + 14, y + 22, "Серия"))
        parts.append(t(M + 62, y + 22, "ПРЕМИУМ-3", size=14, weight="700", fill=P["brand"]))
        parts.append(t(M + 14, y + 42, "Цельнотянутые ванны премиум-класса", size=12, fill=P["text_secondary"]))
        parts.append(t(M + 14, y + 62, "Все модели (10) →", size=11, weight="500", fill=P["link"]))
        y += band_h + 12

        parts.append(t(M, y + 4, "ВМЦ-П3-2/500", size=13, weight="600", family=MONO))
        parts.append(t(M + 130, y + 4, "⧉", size=12, fill=P["text_muted"]))
        parts.append(t(M, y + 28, "Ванна моечная цельнотянутая", size=18, weight="600"))
        parts.append(t(M, y + 50, "2-секционная 500×400 мм", size=18, weight="600"))
        y += 68

        gw = (CW - 8) // 2
        gh = 48
        grid_data = [
            ("L", "1150 мм"), ("W", "700 мм"),
            ("H", "850 мм"), ("Масса", "68 кг"),
            ("Секций", "2"), ("Чаша", "500×400"),
            ("Материал", "AISI 304"), ("Конструкция", "Цельнотян."),
        ]
        for i, (lbl, val) in enumerate(grid_data):
            col = i % 2
            row = i // 2
            parts.append(grid_cell(M + col * (gw + 8), y + row * (gh + 6), gw, gh, lbl, val))
        y += 4 * (gh + 6) + 8

        parts.append(t(M, y + 16, "Доставка от 3 дн. →", size=12, weight="500", fill=P["link"]))
        parts.append(t(M, y + 38, "Купить как дилер →", size=12, weight="500", fill=P["link"]))
        y += 56

        parts.append(line(M, y, M + CW, y, stroke=P["divider"], sw=2))
        parts.append(t(M, y + 16, "P2 — HIGH", size=9, weight="700", fill=P["brand"], letter_spacing="0.05em"))
        y += 28
        parts.append(ghost_btn(M, y, (CW - 8) // 2, 40, "Сравнить"))
        parts.append(ghost_btn(M + (CW - 8) // 2 + 8, y, (CW - 8) // 2, 40, "Избранное"))
        y += 52

        ms_h = 196
        parts.append(r(M, y, CW, ms_h, fill=P["card"], stroke=P["border"], rx=6, filt=True))
        parts.append(t(M + 16, y + 28, "Ключевые параметры", size=15, weight="600"))
        for i, (k, v) in enumerate([
            ("Количество секций", "2"), ("Материал", "AISI 304"),
            ("Тип конструкции", "Цельнотянутая"), ("Вес нетто", "65 кг"), ("Гарантия", "24 мес."),
        ]):
            parts.append(spec_row(M, y + 36 + i * 32, CW, k, v))
        y += ms_h + 16

        parts.append(line(M, y, M + CW, y, stroke=P["divider"], sw=2))
        parts.append(t(M, y + 16, "P3 — MEDIUM", size=9, weight="700", fill=P["brand"], letter_spacing="0.05em"))
        y += 28

        parts.append(t(M, y + 4, "Другие модели серии ПРЕМИУМ-3", size=14, weight="600"))
        y += 24
        card_w = 156
        for i, sib in enumerate([
            ("ВМЦ-П3-1/500", "1150×600", "1 сек", "98 200 ₽", "● В наличии", P["stock"], True),
            ("ВМЦ-П3-2/600", "1400×700", "2 сек", "156 800 ₽", "● Под заказ", P["stock_order"], False),
        ]):
            parts.append(sibling_card(M + i * (card_w + 10), y, card_w, *sib))
        y += 180

        parts.append(t(M, y + 8, "Задать вопрос  ·  Поможем подобрать", size=12, fill=P["link"]))
        y += 28
        parts.append(t(M, y + 4, "Моечная ванна цельнотянутая двухсекционная для профессиональных кухонь…", size=13, fill=P["text_secondary"]))
        parts.append(t(M, y + 24, "Показать полностью ▼", size=12, weight="500", fill=P["link"]))
        y += 48

        parts.append(line(M, y, M + CW, y, stroke=P["divider"], sw=2))
        parts.append(t(M, y + 16, "P4 — LOWER", size=9, weight="700", fill=P["brand"], letter_spacing="0.05em"))
        y += 28
        parts.append(r(M, y, CW, 40, fill=P["page_bg"], stroke=P["border"], rx=5))
        parts.append(t(M + 16, y + 26, "Характеристики — 24 параметра ▼", size=12, fill=P["text_secondary"]))
        y += 52
        parts.append(t(M, y + 4, "📄  Паспорт ВМЦ-П3.pdf", size=12, fill=P["link"]))
        parts.append(t(M, y + 24, "📄  Сертификат соответствия.pdf", size=12, fill=P["link"]))
        y += 48

        parts.append(t(M, y + 4, "Фото", size=13, weight="600"))
        y += 20
        parts.append(product_silhouette(M, y, CW, 200))
        for i, tx in enumerate([M, M + 58, M + 116]):
            parts.append(thumb(tx, y + 212, active=(i == 0)))
        y += 268

        parts.append(line(M, y, M + CW, y, stroke=P["divider"], sw=2))
        parts.append(t(M, y + 16, "P5 — COLLAPSE", size=9, weight="700", fill=P["text_muted"], letter_spacing="0.05em"))
        y += 32
        parts.append(t(M, y + 4, "← Вернуться к серии ПРЕМИУМ-3", size=12, fill=P["link"]))
        y += 28
        parts.append(t(M, y + 4, "Сопутствующее оборудование (2)", size=12, weight="500", fill=P["text_secondary"]))
        y += 24
        parts.append(r(M, y, CW, 48, fill=P["footer_bg"], stroke="none", rx=5))
        parts.append(t(M + 16, y + 30, "© BZPM · 8 (800) 000-00-00", size=10, fill=P["footer_text"]))

        parts.append(t(M + CW, H - 12, "Hi-Fi Alpha · Mobile · v1", size=8, fill=P["text_muted"], anchor="end"))

    parts.append(svg_close())
    path = OUT / f"BZPM-PDP-HIFI-ALPHA-MOBILE-{version}.svg"
    path.write_text("\n  ".join(parts), encoding="utf-8")
    print(f"Wrote {path}")


if __name__ == "__main__":
    generate_desktop("v1")
    generate_mobile("v1")
    generate_desktop("v2")
    generate_mobile("v2")

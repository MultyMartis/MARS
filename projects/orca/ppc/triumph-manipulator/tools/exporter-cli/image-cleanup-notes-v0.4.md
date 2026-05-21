# Image / creative cleanup notes v0.4

**Phase:** ORCA Commander Import Refinement v0.4  
**Scope:** Sheet1 ZIP patch only · rows **16+** · metadata rows **1–15 untouched**

---

## Commander symptom

Popup: *«В импортируемых данных есть ссылки на изображения или креативы»*.

---

## Forensics (template `triumph-manipulator-commander-template-v0.xlsx`)

| Column | Header (row 14) | Row 14 logical key | Evidence |
|--------|-----------------|-------------------|----------|
| **64** (BL) | Изображение | `ads.image` | Rows **25–35** contain `https://direct.yandex.ru/images/direct/…` in `sheet1.xml` |
| **65** | Креатив | `ads.creative` | Cleared with image column |
| **66** | Статус модерации креатива | `ads.creative_moderation_status` | Cleared with image column |
| **2** | Тип объявления | `ads.ad_type` | Template default **Текстово-графическое** — graphic ad type marker |

ExcelJS read of row 30 col 64: `https://direct.yandex.ru/image` (stale template residue).

**Export block for Triumph fixture:** rows **16–30** (15 rows). Rows **25–30** inherit empty region **and** image URLs from template → trigger Commander warnings.

---

## Cleanup mask (v0.4)

| Action | Rows | Columns |
|--------|------|---------|
| Clear image/creative cells | `16 … 16+N−1` | 64, 65, 66 → empty `<v></v>` |
| Clear image/creative on stale tail | `16+N …` (if `--no-row-removal`) | Same + stale cleanup keys |
| Ad type literal (search-only) | `16 … 16+N−1` | col **2** → **Текстово-графическое** (v0.5; was `-` in v0.4 — see [ad-type-literal-fix-v0.5.md](ad-type-literal-fix-v0.5.md)) |

**NOT touched:** rows 1–15, sheet2 **Регионы**, sheet3 dictionary, combinatorics cols 16–47.

---

## Implementation

| Module | Role |
|--------|------|
| [commander-header-map-v0.json](commander-header-map-v0.json) | Verified `ads.image`, `ads.creative`, `ads.creative_moderation_status` |
| [sheet1-xml-builder.js](sheet1-xml-builder.js) | `IMAGE_CREATIVE_CLEANUP_KEYS`, export + stale clear |
| [mapping.js](mapping.js) | `ad_type_transport: "Текстово-графическое"` on fill rows (v0.5) |

---

## Future (HR / РСЯ)

When image export is intentional, gate cleanup behind a flag (e.g. `--allow-creative-columns`) — **not implemented in v0.4**.

---

## SAFE UNKNOWN

- v0.5 resolves `-` mask → explicit **Текстово-графическое**; human re-import confirms Commander accepts without image popup.
- Whether Commander still warns if combinatorics object cells (cols 26–35) retain graphic metadata — **not cleared** in v0.4.

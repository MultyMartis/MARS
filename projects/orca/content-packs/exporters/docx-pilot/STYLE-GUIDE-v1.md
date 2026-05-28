# DOCX Pilot Style Guide v1

## Document character

Target look: **internal agency operational specification** — not marketing brochure, not academic report, not raw Markdown dump.

## Typography

| Element | Convention |
|---------|------------|
| Body | Calibri 11pt equivalent (docx size 22 half-points) |
| Headings | Calibri bold; H1 section numbers `01 — Hero` |
| IDs / URLs | Consolas where marked `mono` in metadata tables |
| Line spacing | ~1.15 (276 twips) on body paragraphs |

## Color semantics (shading)

| Block type | Background | Use |
|------------|------------|-----|
| Metadata table | `#F5F5F5` | Cover fields, contracts |
| CTA | `#E8F4FD` | Primary/secondary CTA rows |
| SAFE UNKNOWN | `#FFF3CD` | Warnings — must stand out |
| Semantic lock | `#EEEEEE` | Lock lines with 🔒 prefix |
| Divider | `#CCCCCC` border | Section separation |

## Structural patterns

- **Cover:** centered title, metadata table, approval snapshot
- **Sections:** H1 label → purpose → content → CTA box → locks → factory notes
- **Lists:** Word bullet paragraphs for copy bullets
- **Tables:** 2-column label/value for specs and PPC/SEO

## CTA blocks

Render as shaded single-cell table:

```
Primary: Рассчитать стоимость → #contacts
Secondary: Позвонить → tel:+79004658331
```

## Warning blocks

Title prefix `⚠` required. Never downgrade UNKNOWN to body text.

## Word compatibility

- No custom macros
- Standard OOXML via `docx` package
- Test open in Microsoft Word desktop

## Anti-patterns

| Avoid | Why |
|-------|-----|
| Stock photo placeholders in DOCX | Factory layer only |
| Marketing gradient covers | Wrong document class |
| Stripping 🔒 or ⚠ markers | Operator trust |
| Resolving UNKNOWN inline | Violates MODE 1 |

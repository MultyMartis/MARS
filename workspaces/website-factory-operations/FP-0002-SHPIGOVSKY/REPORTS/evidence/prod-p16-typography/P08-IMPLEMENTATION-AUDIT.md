# P08 TYPOGRAPHY IMPLEMENTATION AUDIT — PROD-P16

**Date:** 2026-08-17

## What P08 owned

| Artifact | Role |
|----------|------|
| `_p08_typo_nbsp_source.py` | One-shot source string rewriter (Unicode NBSP) |
| `TYPOGRAPHY-SOURCE-MUTATIONS.md` | ~193 strings / 610 NBSP in 5 helper files |
| Specialist migrate script | Stored plain/WYSIWYG typography on write for 4 specialists |
| OWNERSHIP-MAP | Explicitly **no** global runtime filter at P08 |

## Gap left open

Broad live ACF/WYSIWYG/options mass rewrite intentionally deferred (HTML/shortcode safety).

## P16 decision

- **Do not** create a second engine.
- **Canonize** P08 rule set into `RussianTypography` (PHP).
- **Add** bounded `TypographyFilters` as the single runtime owner.
- Prefer **render-time** over stored mass rewrite (Admin UX + search + future Olya content).

## Required

`ONE TYPOGRAPHY OWNER ONLY` → `typography.russian` / `RussianTypography`

# FP-0002 V9-04 Menus and Navigation v1

**Date:** 2026-07-02

## Registered locations

| Location | Purpose |
|----------|---------|
| `primary_desktop` | Header desktop nav |
| `primary_mobile` | Offcanvas menu |
| `footer_services` | Service links column |
| `footer_o_centre` | O-Centre links |
| `footer_legal` | Legal links |

## Required links (preserve)

- "Все отзывы" → `/otzyvy/`
- "Все статьи" → `/blog/`
- Service slugs per manifest
- Legal routes in footer

## Active states

Use WordPress `current-menu-item` / ancestor classes matching V9 `aria-current` patterns.

## Policy

**Explicit menus** — do not auto-generate from page tree if order conflicts with approved design.

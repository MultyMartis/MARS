# FP-0002 V9-03C — G6 Source Audit v1

## Canonical source

| Field | Value |
|-------|-------|
| File | `src/partials/sections/infrastructure-narrative.html` |
| Occurrence count | **1** (lines 56–61 before removal) |
| Page usage | `src/pages/o-centre.html` only |
| Reuse | **Not shared** — section included only on `/o-centre/` |

## Deletion boundary

Removed complete element:

```html
<div class="infrastructure-narrative__group infrastructure-narrative__group--g6 infrastructure-narrative__group--mobile-close" data-inf-group="g6">
  … two mobile-only figures (infrastructure-19, infrastructure-20) …
</div>
```

**Preceding sibling:** G5 comfort-gallery include  
**Following sibling:** closing `</div>` of `infrastructure-narrative__container`

## Content removed

- Mobile stack subgallery with 2 images (`o-centre-infrastructure-19.webp`, `o-centre-infrastructure-20.webp`)
- No G6-only HTML comments

## Shared boundary result

**Non-shared** — safe to remove without affecting other pages.

# FP-0002 Services V2 — Lifebuoy Decor Removal v1

## Operator decision

Remove lifebuoy (`services-hub-decor`) decor completely from Services V2 category architecture.

## Runtime references before

| Location | Count |
|----------|------:|
| `services-category-section-v2.html` decor markup | 1 partial |
| `uslugi-v2.html` `decorImage` include params | 4 |
| `style.scss` V2 decor rules (desktop + mobile) | 18 selectors |
| Asset runtime refs in V2 | 4 (`services-hub-decor.webp`) |

## Runtime references after

| Probe | Count |
|-------|------:|
| `.services-category-section-v2__decor` | 0 |
| `img[src*="services-hub-decor"]` on `uslugi-v2.html` | 0 |

## HTML removed

- `services-category-section-v2__decor` wrapper + image from partial
- `decorImage` parameter from all four V2 category includes

## SCSS removed

- All `.page-uslugi-v2 .services-category-section-v2__decor*` rules
- Section `position:relative` / `overflow:hidden` used only for decor stacking

## Assets physically deleted

None (`ORPHANED_NOT_IN_RUNTIME` — `assets/img/content/services/services-hub-decor.webp` may remain on disk; still referenced by V1 `uslugi.html` hub decor).

## Verdict

`LIFEBUOY_DECOR_RUNTIME_PRESENCE_ZERO` on Services V2.

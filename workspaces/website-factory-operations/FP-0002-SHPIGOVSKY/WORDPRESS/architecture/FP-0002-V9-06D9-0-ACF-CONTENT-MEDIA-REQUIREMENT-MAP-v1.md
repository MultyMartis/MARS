# FP-0002 V9-06D9-0 ACF Content Media Requirement Map v1

**Date:** 2026-07-05  
**Evidence:** `validation/v9-06d9-0-full-visual-port-charter/acf-content-media-requirement-map.json`

## Requirement matrix

| Item | Source repair | ACF schema | DB seed | Media | Operator data | Review |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| Hero image | yes | no | yes | yes | no | no |
| Gallery images | no | no | yes | yes | no | no |
| Reviews block | yes | yes | yes | yes | no | yes |
| Specialists block | yes | yes | yes | yes | no | yes |
| Articles teaser | no | no | yes | yes | no | yes |
| Header messenger URLs | yes | no | no* | no | yes† | no |
| Header messenger icons (visual) | yes | no | no | no | no | no |
| Map URL (contacts) | no | no | yes | no | yes | no |
| Legal identifiers | no | no | yes | no | yes | yes |
| Service 74 clinical copy | no | no | no | no | no | yes |
| FAQ copy | no | no | no | no | no | yes |
| Home missing section fields | yes | yes | yes | yes | no | yes |
| WP primary menu | no | no | yes | no | no | no |

\* Visual parity via `#` fallback needs no DB seed.  
† Required only for functional production links.

## Notes

- D8-A…E seeded MVP content under strict allowlists; many media-heavy fields intentionally skipped.
- New ACF field groups may be required for D9-D sections not covered by existing `group_fp02_page_home`.
- Operator data (messengers, map, legal) can follow visual parity; static `#` placeholders acceptable interim.

## Result

ACF/content/media map complete.

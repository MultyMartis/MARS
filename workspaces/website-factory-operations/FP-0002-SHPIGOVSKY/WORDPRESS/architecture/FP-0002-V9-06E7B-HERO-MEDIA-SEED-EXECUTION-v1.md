# FP-0002 V9-06E7B — Hero Media Seed Execution v1

**Date:** 2026-07-06  
**PHP:** `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe`

## Seed targets (post-correction)

| Key | Object ID | Asset | Attachment | Result |
|-----|----------:|-------|------------|--------|
| home | 4 | hero-main.png | 302 | PASS |
| services_hub | 5 | services-hero.webp | 303 | PASS |
| service_subdivision | 73 | service-subdivision-hero.webp | 304 | PASS |
| service_leaf_alcohol | **74** | service-leaf-alcohol-hero.webp | 305 | PASS |

## Alcohol ID correction

Initial E7 WIP seed runner referenced object ID **77** (Психическое здоровье). Correct alcohol leaf service is ID **74** (`lechenie-alkogolnoy-zavisimosti`). Corrected within E7B: cleared `hero_media` on 77, seeded attachment 305 on 74.

## Rules observed

- Local V9 static assets only (`workspaces/fp-0002-shpigovsky-v9/src/img`)
- No external downloads
- `hero_media` + attachment records only

Authority: `validation/v9-06e7b-hero-system-finalization-scope-reconciliation/hero-media-seed-execution.json`, `hero-alcohol-id-correction.json`

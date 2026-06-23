# FP-0002 V6 HOME SECTION 03 OPERATOR STABLE 01 — Backup Manifest

**Release ID:** FP-0002-V6-HOME-SECTION-03-OPERATOR-STABLE-01  
**Archive:** `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-HOME-SECTION-03-OPERATOR-STABLE-01-SOURCE.zip`  
**Archive SHA-256:** `87389fd57ad03bedc986e9dcc43f41048539ad05d30efb236fbbf271364f9ce7`

## Scope

Responsive shell, Hero, Section 01, Section 02, Section 03 with clickable service links and FA5 `fa-external-link-alt` icons, Footer, local Inter, current style foundation.

## Not in scope

Gallery, pre-reviews blocks, Reviews, `dist/`, `node_modules/`.

## Verification

- Archive checksum verification: PASS
- Temporary restore + `npm ci` + `npm run build`: PASS
- Section 03 service links present in restored build: PASS
- Gallery absent in restored build: PASS

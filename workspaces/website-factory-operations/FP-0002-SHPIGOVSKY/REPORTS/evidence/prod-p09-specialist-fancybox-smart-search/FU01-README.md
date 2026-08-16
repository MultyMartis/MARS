# PROD-P09-FU01 — Evidence Index

**Wave:** Mobile Smart Search Parity + Operator CSS Canonization  
**Host:** http://shpigovsky.beget.tech/  
**Rollback:** `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p09-fu01-layer-b-pre\`  
**Prod-after:** `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p09-fu01-prod-after\`

## Artifacts

| File | Purpose |
|------|---------|
| `FU01-OPERATOR-CSS-DRIFT-BEFORE.json` | Production-before hashes vs local |
| `FU01-OPERATOR-CSS-CANONIZATION.json` / `.md` | Canonization proof |
| `fu01-diffs/` | Local↔prod CSS diffs |
| `FU01-MOBILE-OWNERSHIP.md` | Offcanvas ownership map |
| `FU01-LAYER-B-MANIFEST.json` | Exact-file rollback manifest |
| `FU01-EXACT-FILE-ROLLBACK-READY.md` | Rollback ready gate |
| `FU01-DEPLOY-MANIFEST.json` | Upload + after hashes |
| `FU01-SOURCE-PROD-PARITY.json` | SFTP SOURCE↔PRODUCTION MATCH |
| `FU01-PLAYWRIGHT-QA.json` | Desktop/mobile/Fancybox matrix |
| `fu01-screenshots/` | Mobile + desktop captures |
| `FU01-P07-P08-REGRESSION.md` | Smoke regression |

## Required statements evidenced

- `OPERATOR CSS DRIFT CANONIZED BEFORE FU01 IMPLEMENTATION`
- `OPERATOR CSS DRIFT PRESERVED AND CANONIZED`
- `SMART SEARCH LIVE SUGGESTIONS ACTIVE ON MOBILE OFFCANVAS`
- `DESKTOP SMART SEARCH ACCEPTED BEHAVIOR PRESERVED`
- `SPECIALIST CERTIFICATE GALLERY FANCYBOX = PASS`
- `SOURCE ↔ PRODUCTION MATCH` (3/3 FU01 files)

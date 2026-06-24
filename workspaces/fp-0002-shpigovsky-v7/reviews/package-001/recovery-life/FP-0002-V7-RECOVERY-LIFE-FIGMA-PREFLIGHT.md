# FP-0002 V7 — Recovery Life Figma Preflight

**Package:** #001 Phase 3C  
**Date:** 2026-06-24

## Source

| Field | Value |
|-------|-------|
| Path | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig` |
| SHA-256 | `BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041` |
| Inspection method | `openfig-core` offline parse + zip image extraction |
| Live Dev Mode | NOT AVAILABLE in agent session |
| Historical Figma used | NO |

## Frames

| Variant | Frame ID | Name | Size | Status |
|---------|----------|------|------|--------|
| Desktop home | `1:875` | Главная страница | 1437×16809 | VERIFIED |
| Desktop section root | `77:4225` | Нас выбирают (layer name) | 1437×864 | VERIFIED |
| Mobile home | `1:3992` | Главная страница - моб | 380×22883 | VERIFIED |
| Mobile section root | NOT FOUND | — | — | SAFE UNKNOWN — dedicated mobile recovery-life frame absent; responsive derived from desktop geometry |

## Section heading node

| Field | Value |
|-------|-------|
| Node ID | `77:4227` |
| Visible text | Как меняется жизнь человека в процессе восстановления |
| Visible | YES |

## Visibility audit

| Metric | Count |
|--------|------:|
| Visible text nodes in section | 9 |
| Hidden nodes included in implementation | 0 |
| Layer-name vs visible-content conflicts | 1 (`77:4225`/`77:4226` name «Нас выбирают» vs visible heading) |
| Instance overrides in section | NONE |

## Evidence files

- `reviews/package-001/recovery-life/_fig_extract_temp/recovery-life-section.json`
- `reviews/package-001/recovery-life/_fig_extract_temp/recovery-life-extract.json`

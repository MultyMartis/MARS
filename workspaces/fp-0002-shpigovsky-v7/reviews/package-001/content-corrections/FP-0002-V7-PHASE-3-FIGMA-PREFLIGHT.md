# FP-0002 V7 Phase 3 — Figma Preflight

**Date:** 2026-06-24  
**Package:** #001 Phase 3A–3B  
**Authority:** `foundation/FP-0002-V7-FIGMA-AUTHORITY-RULES.md`

## Active Figma source

| Field | Value |
|-------|-------|
| Path | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig` |
| SHA-256 | `BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041` |
| Status | ACTIVE |
| Historical file used | NO (`Шпиговский.fig` — DO NOT USE) |

## Inspection method

| Field | Value |
|-------|-------|
| Method | Offline `openfig-core` parse of `Spig_v1.2.fig` + `symbolOverrides` instance text resolution + `fillGeometry.commandsBlob` SVG path decode |
| Dev Mode | NOT AVAILABLE (offline `.fig` only; no linked Figma cloud file key for REST/MCP export) |
| Extraction artifacts | `reviews/package-001/content-corrections/_fig_extract_temp/` |

## Target frames / groups

| Block | Desktop frame | Node ID | Mobile frame | Mobile node ID |
|-------|---------------|---------|--------------|----------------|
| Intro | `2 - Дом - вступление` | `1:927` | `Дом вступление` | `1:4036` |
| Founder quote mark | `Слово спецу` | `1:1208` (vector `1:1217`) | same section on mobile canvas | SAFE UNKNOWN — vector reused in mobile slice; mark node `1:1217` visible on desktop |
| Gallery | `3- Услуги` → `Frame 81513740` `1:983` | images `1:986`–`1:989` | `Главная страница - моб` `1:3992` uses different service-card subtree; gallery asset hashes mapped to desktop nodes per `GALLERY-ASSET-PROVENANCE.md` |

## Visibility summary

| Area | Visible text nodes | Hidden excluded |
|------|-------------------:|----------------:|
| Intro desktop `1:927` | 14 | 0 |
| Intro mobile `1:4036` | 14 | 0 |
| Intro benefits instances `1:933`–`1:936` | 4 (via overrides) | duplicate row instances `13:4517`+ excluded from content map (carousel duplicate, same override text) |
| Gallery captions desktop `1:986`–`1:989` | 4 | slide `1:990` caption hidden from implementation (not in frontend slide set) |
| Founder quote vector `1:1217` | 1 | decorative background vector `1:1213` excluded |

## Layer-name / visible-content conflicts

| Layer name | Visible content | Authority | Status |
|------------|-----------------|-----------|--------|
| `Услуга` (gallery images) | Instance image fill + caption override text | VISIBLE OVERRIDE TEXT | `LAYER_NAME_CONTENT_CONFLICT` — caption not derived from layer name |
| `Маркированный список` instances | Override `textData.characters` per instance | INSTANCE OVERRIDE | NO CONFLICT |
| `"` (vector `1:1217`) | Decorative quote glyph path | VISIBLE VECTOR | NO CONFLICT |

## Verdict

`FIGMA EXACT EXTRACTION` — **PASS** (offline parse; Dev Mode not used)

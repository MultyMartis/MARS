# FP-0002-PG-004 — Service Leaf Pass Opening v1

**Page ID:** FP-0002-PG-004  
**Page name:** Услуга конечная  
**Reference type:** SERVICE_LEAF_INTERNAL_PAGE  
**Example service:** Лечение алкогольной зависимости  
**Pass:** OPENING ONLY — planning and evidence; no runtime implementation

## Scope completed

- Git preflight at HEAD `e4a92c82`
- Mandatory operator backup ZIP created
- Desktop + mobile PNG authority validated (SHA-256 recorded)
- Exact Figma frames confirmed offline from `Spig_v1.2.fig`
- Fresh design authority rasters copied to evidence (not committed as operator PNG)
- Desktop + mobile block registries
- Visible text anchors from PNG + Figma extract
- Asset + reuse + group registries
- GROUP 1 implementation plan prepared
- Baseline `npm run build` smoke (no new page)

## Authority stack

1. Approved desktop PNG (`Услуга - десктоп.png`, 1437×13313)
2. Approved mobile PNG (`Услуга - мобильная.png`, 380×18136)
3. Figma `Spig_v1.2.fig` frames `Услуга конечная` / `Услуга конечная - моб` for node IDs, text, assets after PNG identification
4. Stable references: Service Subdivision (`eb10c71b`), Services V2 (`3a3c648b`), Home

## Direct Figma MCP

- **Result:** BLOCKED — `get_metadata` requires `fileKey`; active desktop document not wired with fileKey in this session
- **Continued via:** offline `openfig-core` parse of canonical `Spig_v1.2.fig` (not claimed as MCP read)

## Implementation status

| Item | Status |
|------|--------|
| New page source | NOT CREATED |
| HTML/SCSS/JS | NOT STARTED |
| Asset export | NOT STARTED |
| GROUP 1 | PLAN READY |

## Gate

**READY_FOR_FP0002_SERVICE_LEAF_GROUP_1**

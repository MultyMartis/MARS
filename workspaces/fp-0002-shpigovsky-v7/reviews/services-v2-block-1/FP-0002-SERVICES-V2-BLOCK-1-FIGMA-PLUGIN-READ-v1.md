# FP-0002 — Services V2 Block 1 Figma Plugin Read v1

**Date:** 2026-06-26  
**Authority commit (start):** `edfa2e67`  
**Design pack:** `Spig_v1.2.fig` @ SHA-256 `BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041`

## Current document

| Field | Value |
| ----- | ----- |
| Local authority | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig` |
| Other Figma file searched | **ZERO** |
| Cloud `fileKey` in repo | **SAFE UNKNOWN** |

## MCP session

| Check | Result |
| ----- | ------ |
| MCP server | CONNECTED (`plugin-figma-figma`) |
| `whoami` | PASS — `Ignis Martis` / `reg@polygon-ws.ru` |
| `get_design_context` (`fileKey: active`, `1:1311`) | **BLOCKED** — no edit/view access |
| `get_metadata` | **BLOCKED** — `fileKey` required; no verified cloud key |
| `get_screenshot` | Not attempted (same blocker) |
| Write tools | **NONE** |

## Read method used for Block 1

```text
MCP authentication → BLOCKED live node read
Supplement (authorized): offline openfig-core parse of local Spig_v1.2.fig
Cross-check: approved PNG 26.06.2026 + committed anatomy audit edfa2e67
```

## Target nodes (offline-confirmed)

| Node | Name | Read via MCP | Read via offline parse |
| ---- | ---- | ------------ | ---------------------- |
| `1:1310` | Услуги хаб | NO | YES |
| `1:1311` | Inner Hero | NO | YES |
| `1:1353`–`1:1359` | Hero content / CTA | NO | YES |
| `1:1363` | Breadcrumbs | NO | YES |
| `1:1367`–`1:1373` | Page submenu tags | NO | YES |
| `1:4624` / `1:4625` | Mobile hub / hero | NO | YES |

## Screenshots

| Asset | Source |
| ----- | ------ |
| `FIGMA-HERO-DESKTOP.png` | Audit `TARGET-DESKTOP-FULL.png` (MCP screenshot unavailable) |
| `FIGMA-HERO-MOBILE.png` | Audit `TARGET-MOBILE-FULL.png` |
| `FIGMA-BREADCRUMBS-DESKTOP.png` | Approved PNG authority (upper crop proxy) |
| `FIGMA-BREADCRUMBS-MOBILE.png` | Approved mobile PNG authority |
| `FIGMA-SUBNAV-DESKTOP.png` | Approved PNG authority |
| `FIGMA-SUBNAV-MOBILE.png` | Approved mobile PNG authority |

## Properties read directly (offline parse)

- Hero shell 1400×628, overlay gradient, left copy column 582px
- Eyebrow / H1 / lead text nodes `1:1355`–`1:1357`
- CTA instance `1:1359` (334×53 desktop)
- Breadcrumb chain `1:1364`–`1:1366`
- Six tag labels via `symbolOverrides` on `1:1368`–`1:1373`
- Mobile hero `1:4625`, breadcrumbs `1:4672`, horizontal tag row `1:4665`

## Values from PNG only

- Exact hero content inset px (desktop left padding tuned against PNG)
- Subnav pill visual weight on white page band

## SAFE UNKNOWN

- Live MCP color tokens for tag hover/active (all instances same fill in offline parse)
- Cloud `fileKey` for future MCP re-run

## Verdict

```text
FIGMA ACTIVE DOCUMENT ACCESS — LIVE MCP READ BLOCKED (fileKey + share)
OFFLINE SPIG_V1.2.FIG PARSE — USED FOR BLOCK 1 (no other file searched)
```

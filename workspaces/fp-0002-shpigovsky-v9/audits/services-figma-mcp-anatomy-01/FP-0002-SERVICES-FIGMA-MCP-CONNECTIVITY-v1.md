# FP-0002 — Services Figma MCP Connectivity v1

**Date:** 2026-06-26  
**Authority commit:** `641295e1`  
**Task:** read-only Figma MCP audit (no writes)

## MCP session

| Check | Result |
| ----- | ------ |
| MCP server | **CONNECTED** (`plugin-figma-figma`) |
| `whoami` | **PASS** — `Ignis Martis` / `reg@polygon-ws.ru` |
| Plan | Polygon Web Studio — **Pro**, seat **Full (expert)** |
| Write tools used | **NONE** (forbidden) |

## Read tools availability

| Tool | Invoked | Result |
| ---- | ------- | ------ |
| `whoami` | Yes | Success |
| `get_metadata` | Yes | **BLOCKED** — permission error |
| `get_design_context` | No | Not attempted after metadata block |
| `get_screenshot` | No | Not attempted after metadata block |
| `get_variable_defs` | No | Blocked — requires verified `fileKey` |
| `search_design_system` | Yes | **BLOCKED** — permission error |
| `get_libraries` | No | Blocked — requires verified `fileKey` |

## Target file identity

| Field | Value |
| ----- | ----- |
| Local authority | `Spig_v1.2.fig` |
| Local SHA-256 | `BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041` |
| Exported file name (meta.json) | `Шпиговский` (UTF-8 garbled in zip meta) |
| Exported at | `2026-06-23T15:35:03.541Z` |
| Cloud `fileKey` in repo | **SAFE UNKNOWN** — no `figma.com/design/...` URL in project records |
| MCP read attempts | `Spig_v1.2`, `shpigovsky`, hash prefix — all returned *"don't have edit access to this file"* |

## Verdict

```text
MCP AUTHENTICATION — VERIFIED
LIVE TARGET FILE READ — BLOCKED (no fileKey + no confirmed cloud share)
READ-ONLY MCP ANATOMY PASS — NOT COMPLETED VIA MCP
```

**Operator action required before MCP re-run:** provide live Figma Design URL (`fileKey` + optional `node-id`) with view access for `reg@polygon-ws.ru`, or share cloud file to Polygon Web Studio team.

## Supplementary evidence used (not MCP)

Offline visible-node parse of local `Spig_v1.2.fig` (openfig-core) + approved PNG 26.06.2026 — documented separately; **does not replace** live MCP verification per task boundary, but enables anatomy/differential audit while cloud access is blocked.

**Evidence:** `evidence/metadata/offline-services-hub-parse.json`

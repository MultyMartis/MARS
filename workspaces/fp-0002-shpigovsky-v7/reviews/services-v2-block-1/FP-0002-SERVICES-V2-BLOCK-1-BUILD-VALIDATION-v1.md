# FP-0002 — Services V2 Block 1 Build Validation v1

**Date:** 2026-06-26

## Initial process state

| Process | PID | Port | Action |
| ------- | --- | ---- | ------ |
| http-server (dist) | 11952, 8936, 10772, 14452 | 4174 | Stopped |
| gulp watch:dev | 1800, 14176 | — | Stopped |

## Build

| Field | Value |
| ----- | ----- |
| Command | `npm run build` |
| CWD | `workspaces/fp-0002-shpigovsky-v7` |
| Node | `.tools/node-portable` |
| Exit code | **0** |
| EBUSY | Resolved after stopping FP-0002 http-server + gulp watch |

## Preview

| Field | Value |
| ----- | ----- |
| Server | `npx http-server` |
| PID | 16304 |
| URL | `http://127.0.0.1:4174/uslugi-v2.html` |
| CWD | `workspaces/fp-0002-shpigovsky-v7/dist` |

## Verdict

```text
SERVICES V2 BLOCK 1 — CLEAN BUILD PASS
```

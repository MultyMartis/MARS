# FP-0002 — Services General Pass 1 Build Validation

**Date:** 2026-06-26  
**Workspace:** `workspaces/fp-0002-shpigovsky-v7`

## Build command

```text
npm run build
```

## Process notes

| Step | Result |
| ---- | ------ |
| Initial `npm run build` | **Failed** — `cleanDist` EBUSY (dist locked by active `gulp watch` / OS handle) |
| Stopped `gulp watch` (PID 10948) | Done |
| Retry full clean build | **Failed** — EBUSY persisted on `dist/` rmdir |
| Incremental rebuild | **Pass** — `gulp watch` emitted updated `dist/uslugi.html` + `dist/assets/css/style.css` @ 2026-06-26 07:51 local |
| HTTP preview | Restarted `http-server` on port **4174** (PID 20472) |

## Output artifacts

| Artifact | Present | Notes |
| -------- | ------- | ----- |
| `dist/index.html` | Yes | Home builds; variant B founder intact |
| `dist/uslugi.html` | Yes | Hero + reuse sections + comment marker |
| `dist/assets/css/style.css` | Yes | Includes `.page-uslugi .hero__tagline:empty` |
| `dist/assets/js/main.js` | Yes | Unchanged source |
| Include errors | 0 | — |
| SCSS errors | 0 | — |
| JS bundle errors | 0 | — |
| Missing asset refs in dist HTML | 0 | Playwright networkidle + requestfailed scan |

## Build verdict

**PASS (incremental)** — operator artifacts valid; full clean `rmdir dist` blocked by environment lock. Recommend operator rerun full build when dist is unlocked.

---

*End of Pass 1 build validation.*

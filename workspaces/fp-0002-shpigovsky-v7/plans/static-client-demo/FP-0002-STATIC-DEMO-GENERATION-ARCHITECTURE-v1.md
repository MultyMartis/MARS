# FP-0002 Static Demo — Generation Architecture v1

## Recommended model

**B — Four parameterized templates + data registry + generator** (with Gulp build hook = variant C-lite)

## Data format

- `plans/static-client-demo/data/demo-page-registry.json` (promoted from `.draft.json` in PASS 2)
- `demo-navigation-registry.json`
- Page records: id, template, url, title, h1, breadcrumbs, parent, overrides

## Generator location

`workspaces/fp-0002-shpigovsky-v7/tools/static-demo-generator/` (new in PASS 2)

## Build integration

- Gulp task `build:demo-pages` reads registry, emits nested `dist/**/index.html`
- Canonical template sources remain **unmodified** — generator copies/processes from protected template paths

## Output model

```
dist/index.html
dist/uslugi/index.html
dist/uslugi/<section>/index.html
...
```

## Canonical-template protection

- Read-only reference paths per `FP-0002-V7-CANONICAL-DEMO-TEMPLATE-REGISTRY-v1.md`
- Generator writes to **new** page instance paths only
- CI check: hash of four template files unchanged

## Rollback

- Revert generator commit; delete generated `src/pages/demo-*` or dist-only outputs per implementation choice
- Baseline tag `fp-0002-v7-four-template-canonical-demo-baseline-01` remains restore point

## Rejected alternatives

| Option | Reason |
| ------ | ------ |
| A Manual HTML copy | ~56 pages — error-prone, breaks template protection |
| D Client-side routing | Violates static hosting / SEO demo requirements |

## Expected PASS 2 files changed

- `tools/static-demo-generator/**`
- `gulpfile.js` (task only)
- `plans/static-client-demo/data/*.json` (promoted)
- Generated dist outputs (not committed)

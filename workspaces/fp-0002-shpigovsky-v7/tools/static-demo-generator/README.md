# FP-0002 Static Demo Generator (PASS 2)

Minimal Node generator for 56 static demo page instances.

## Command

```bash
npm run build:demo
```

Runs `gulp build`, then `node tools/static-demo-generator/index.js`.

## Architecture

| Module | Role |
| --- | --- |
| `registry-loader.js` | Draft → final registry normalization (operator decisions) |
| `validation.js` | Registry + output validation |
| `template-renderer.js` | Canonical template instance field injection |
| `placeholder-renderer.js` | Placeholder shell from compiled home layout |
| `path-utils.js` | URL/output helpers + root-relative asset rewrite |
| `index.js` | Orchestration + generation receipt |

## Data

- Final registry: `src/data/static-demo/demo-page-registry.json`
- Navigation registry: `src/data/static-demo/demo-navigation-registry.json`
- Draft sources: `plans/static-client-demo/data/*.draft.json`

## Output

Generated HTML only under `dist/` (not committed). Canonical source templates in `src/pages/` are never modified.

## Canonical protection

Generator reads compiled templates from `dist/uslugi-v2.html`, `dist/usluga-podrazdel-v1.html`, `dist/usluga-konechnaya-v1.html`, and home shell from `dist/index.html`.

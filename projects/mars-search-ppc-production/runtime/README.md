# MARS Search PPC Runtime — Wave 1 State Enforcement

**Status:** `IMPLEMENTED — OPERATOR REVIEW REQUIRED`  
**Authority:** [MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md](../MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md)  
**Checkpoint:** lifecycle package committed separately; Wave 1 runtime is **uncommitted** pending operator review.

---

## Structure

| Path | Role |
|------|------|
| `cli/search-ppc.mjs` | Lifecycle CLI (status, can-start, transition, report) |
| `src/` | Transition engine, artifact resolver, enforcement modules |
| `schemas/` | Manifest v2, blocker report, Cursor task contract |
| `fixtures/` | Synthetic test manifests |
| `tests/run-synthetic-matrix.mjs` | 20-case synthetic test matrix |
| `config/lifecycle-defaults.json` | Default paths and version pins |

---

## CLI commands

```bash
node projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs <manifest>

node projects/mars-search-ppc-production/runtime/cli/search-ppc.mjs status <manifest>

node projects/mars-search-ppc-production/runtime/cli/search-ppc.mjs can-start <manifest> <stage-id>

node projects/mars-search-ppc-production/runtime/cli/search-ppc.mjs transition <manifest> <stage-id> <status> --dry-run

node projects/mars-search-ppc-production/runtime/cli/search-ppc.mjs report <manifest> --out-json reports/out.json --out-md reports/out.md
```

Exit codes: `0` = READY / allowed; `2` = BLOCKED; `1` = error.

---

## Synthetic tests

```bash
node projects/mars-search-ppc-production/runtime/tests/run-synthetic-matrix.mjs
```

---

## Related

- [validators/README.md](../validators/README.md)
- [web-gpt/WEB-GPT-SEARCH-PPC-EXECUTION-CONTRACT-v1.md](../web-gpt/WEB-GPT-SEARCH-PPC-EXECUTION-CONTRACT-v1.md)
- [cursor/CURSOR-SEARCH-PPC-TASK-STARTER-v1.md](../cursor/CURSOR-SEARCH-PPC-TASK-STARTER-v1.md)

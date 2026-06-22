# Cursor Search PPC Task Starter Contract v1

**Authority:** [MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md](../MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md)

---

## Reusable task template

Every Cursor task for search PPC must state:

| Field | Required |
|-------|----------|
| Target folder | `C:\AI MARS` |
| Mode | Agent / Ask |
| Project ID | e.g. `corvonero-direct-v2-clean-room` |
| **Manifest path** | e.g. `projects/orca/projects/<id>/state/project-ppc-state-manifest-v1.json` |
| Lifecycle stage | SPPC-NN |
| Requested transition | e.g. `IN PROGRESS → READY FOR REVIEW` |
| Authoritative inputs | Registered artifact paths |
| Required outputs | Stage contract outputs only |
| Forbidden outputs | Downstream artifacts per lifecycle |
| Stage prerequisites | Prior SPPC stages COMPLETED |
| Validator command (before) | See below |
| Validator command (after) | See below |
| Expected status transition | Per lifecycle statuses |
| Git scope | Paths allowed for commit |
| Report heading | `# REPORT — <task name>` |
| Git boundary | Commit only when operator requests |

**Machine-readable contract:** [cursor-search-ppc-task-contract-example-v1.json](./cursor-search-ppc-task-contract-example-v1.json)  
**Schema:** [../runtime/schemas/cursor-search-ppc-task-contract-v1.schema.json](../runtime/schemas/cursor-search-ppc-task-contract-v1.schema.json)

---

## Validation commands

Before execution:

```bash
node projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs <manifest>
node projects/mars-search-ppc-production/runtime/cli/search-ppc.mjs can-start <manifest> <stage-id>
```

After execution:

```bash
node projects/mars-search-ppc-production/runtime/cli/search-ppc.mjs report <manifest> --out-json <report.json> --out-md <report.md>
```

Non-zero exit on blockers.

---

## Example task header

```text
# CURSOR TASK — <project> — SPPC-NN <stage name>

Project ID: <id>
Lifecycle stage: SPPC-NN
Authoritative inputs: <paths>
Required outputs: <per stage contract>
Forbidden: Commander Export, Campaign Production, …
Prerequisites: SPPC-01..NN-1 COMPLETED with artifacts
Validation: node projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs --manifest ...
```

---

## Stop rules

- Do not resume Corvonero production without operator charter  
- Do not treat P0-I pilot as production corpus workflow  
- Do not commit lifecycle package changes without operator approval when status is PROPOSED  

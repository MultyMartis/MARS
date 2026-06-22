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
| Lifecycle stage | SPPC-NN |
| Authoritative inputs | Registered artifact paths |
| Required outputs | Stage contract outputs only |
| Forbidden outputs | Downstream artifacts per lifecycle |
| Stage prerequisites | Prior SPPC stages COMPLETED |
| Validation command | See below |
| Status transitions | Per lifecycle statuses |
| Report heading | `# REPORT — <task name>` |
| Git boundary | Commit only when operator requests |

---

## Validation command

```bash
node projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs \
  --manifest <project-manifest.json> \
  --out-json <report.json> \
  --out-md <report.md>
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

# MARS Search PPC Production

**Canonical cross-system lifecycle** for Yandex Direct **search** campaign production.

| Item | Value |
|------|-------|
| **Authority** | [MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md](MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md) |
| **Status** | `APPROVED — IMPLEMENTATION AUTHORIZED` |
| **Wave 1** | `OPERATIONAL WITH DOCUMENTED PLATFORM BOUNDARY` |
| **Wave 2** | `IMPLEMENTED — OPERATOR REVIEW REQUIRED` — MIG evidence: [../mig/search-ppc-evidence/README.md](../mig/search-ppc-evidence/README.md) |
| **Stages** | SPPC-01 … SPPC-23 |
| **Validator** | `validators/validate-search-ppc-lifecycle.mjs` |
| **Placement** | [architecture/PLACEMENT-DECISION-v1.md](architecture/PLACEMENT-DECISION-v1.md) |

---

## Structure

| Path | Role |
|------|------|
| `architecture/` | Integration map, placement, degraded-evidence mode |
| `contracts/` | Machine-readable lifecycle contract |
| `stages/` | Human-readable stage contracts |
| `schemas/` | JSON Schema for lifecycle + project manifest |
| `state/` | Project PPC state manifest template + synthetic fixtures |
| `validators/` | Lifecycle readiness validator |
| `web-gpt/` | Web-GPT execution contract |
| `cursor/` | Cursor task starter contract |
| `reports/` | Gap audit, bypass audit, task reports |
| `decisions/` | Operator decision records |
| `roadmap/` | Repair roadmap |

---

## Quick validation

```bash
node projects/mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs \
  --manifest projects/mars-search-ppc-production/state/fixtures/synthetic-blocked-v1.json
```

---

## Related systems

- [ORCA Operational Index](../orca/OPERATIONAL-INDEX.md)
- [MIG contracts](../mig/contracts/)
- [ATLAS lifecycle foundation](../atlas/foundation/ATLAS-LIFECYCLE-MODEL-v1.md)

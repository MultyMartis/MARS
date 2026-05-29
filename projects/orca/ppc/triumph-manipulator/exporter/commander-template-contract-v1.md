# Commander Template Contract v1

**Role:** Contract between ORCA exporter and the reference Excel asset.  
**Asset (production):** [triumph-manipulator-commander-template-v1.xlsx](../assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx)  
**Freeze SoT:** [freeze/ppc-exporter-production-baseline-v1/COMMANDER-TEMPLATE-SOT-v1.md](../../freeze/ppc-exporter-production-baseline-v1/COMMANDER-TEMPLATE-SOT-v1.md)  
**README:** [assets/direct-commander-template/README.md](../assets/direct-commander-template/README.md)

---

## Template role

| Role | Description |
|------|-------------|
| **Transport schema** | Defines shape Commander expects on import |
| **Limit reference** | Annotations for field max lengths (symbol validation authority #1) |
| **Draft examples** | Shows how draft vs active rows appear |
| **NOT SoT** | Does not define intent, segmentation, or landing meaning |

---

## Transport-only doctrine

```
ORCA document (SoT)  →  validation  →  exporter  →  template-shaped xlsx  →  Commander
```

Excel produced by export is a **snapshot for import**, not the campaign system of record.

**Forbidden:**

- Editing template in place as “the campaign” without JSON reconciliation  
- Treating template formulas/macros as business logic (**none expected**)  
- Re-importing xlsx back into ORCA entities in v1 (one-way export)

---

## Version compatibility

| Field | Value |
|-------|-------|
| **template_id** | `triumph-manipulator-commander-template` |
| **template_revision** | `v1` (production baseline 2026-05-29) |
| **filename** | `triumph-manipulator-commander-template-v1.xlsx` |
| **legacy_filename** | `triumph-manipulator-commander-template-v0.xlsx` — reference only |
| **exporter_mapping_rev** | `entity-to-commander-mapping-v1` |

Exporter config must pin `template_id` + `template_revision`. Mismatch → `UNSUPPORTED_TEMPLATE_REVISION`.

### Future template-version strategy

1. Copy `v0` → `v1` when Commander structure changes.  
2. Update [entity-to-commander-mapping-v1.md](entity-to-commander-mapping-v1.md) or add `v2` mapping doc.  
3. Keep validator SY limits in sync with new template annotations.  
4. Golden export fixtures per template revision.  
5. Do **not** auto-upgrade old documents — human migration.

---

## Manual operator verification

Before first production import of a new template revision:

| Step | Action |
|------|--------|
| 1 | Open xlsx — list sheet names and header row literals |
| 2 | Update mapping doc logical keys → literal headers |
| 3 | Export one fixture group from [triumph-s-tier-draft-v1.json](../schema/instances/triumph-s-tier-draft-v1.json) |
| 4 | Import in Commander **test** account |
| 5 | Log UI errors in pack notes (not governance) |

---

## Drift risks (Direct UI vs template)

| Risk | Mitigation |
|------|------------|
| Column renamed in Commander | Re-export reference template from live account; bump revision |
| Field limit changed | Update SY rules + template annotations; re-validate |
| New required column for account type | `safe_unknown` until mapping updated |
| Draft status literal changed | Update enum map in mapping doc |

**SAFE UNKNOWN:** Exact sheet names, column order, and header strings in `v0` xlsx — **must be verified** by implementer reading the binary file; Phase 5 docs use **logical column keys** only.

---

## What implementer extracts from xlsx

| Extract | Use |
|---------|-----|
| Sheet names | Row generation section targeting |
| Header row (row 1) | Map logical → literal column names |
| Example draft row | Draft status literal |
| Example active row | Active status literal |
| Limit comments/notes | Cross-check SY validation |

Do **not** commit speculative column names into mapping tables without verification.

---

## Template contents (expected, non-exhaustive)

Based on pack doctrine and export-mapping schema:

- Campaign / group / keyword / ad sections  
- Negative keyword rows  
- Extension rows (fastlinks, callouts)  
- Cyrillic examples  
- Draft row examples  

**SAFE UNKNOWN:** Exact section layout — verify from file.

---

## Provenance

Copied from `incoming/orca-triumph-raw-pack/` during normalization (2026-05-20). Production-proven on live Triumph campaign export per [direct-commander-foundation-v0.md](../export/direct-commander-foundation-v0.md).

---

## Related

- [entity-to-commander-mapping-v1.md](entity-to-commander-mapping-v1.md)  
- [export-blocking-rules-v1.md](export-blocking-rules-v1.md)

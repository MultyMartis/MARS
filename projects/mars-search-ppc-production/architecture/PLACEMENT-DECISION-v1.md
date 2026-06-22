# MARS Search PPC Production — Canonical Placement Decision v1

**Date:** 2026-06-22  
**Status:** **RECORDED**

---

## Inspected locations

| Path | Role found | PPC lifecycle ownership? |
|------|------------|--------------------------|
| `projects/orca/contracts/` | `ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1` — campaign SoT invariants | Partial — stages 14–20 consumer obligations only |
| `projects/orca/semantic-intelligence/integration/` | P0-I admission integration, runtime lock | Partial — stages 05–09 only |
| `projects/orca/ppc/triumph-manipulator/` | Triumph project pipeline, Commander baseline | Project-specific — not universal lifecycle |
| `projects/orca/research/ppc-semantic-intelligence/` | World practice research pack | Analytical source — not lifecycle authority |
| `projects/mig/contracts/` | Source registry, keyword surface, ORCA handoff | Partial — stages 02–03, 10–11 evidence |
| `projects/atlas/foundation/` | ATLAS lifecycle models (entity/relationship) | Entity lifecycle — not search PPC production |
| `governance/` | Cross-system topology, execution contracts | Meta-governance — not stage contracts |
| `web-gpt-sources/` | Chat sync packs | Execution discipline — needs consumer contract |
| `projects/mars-website-factory/` | Website production lifecycle | Parallel pattern — different domain |

---

## Existing ownership (summary)

No single repository locus owned the **full 23-stage cross-system Search PPC lifecycle**. Ownership was fragmented across ORCA campaign contract, MIG evidence contracts, Triumph project freeze, and ORCA semantic integration.

---

## Selected canonical owner

```text
projects/mars-search-ppc-production/
```

**Rationale:** Cross-system lifecycle (ATLAS → MIG → ORCA → Strategist → Production → QA → Commander → Launch → Learning). Follows `projects/mars-website-factory/` pattern for domain production systems without nesting under a single subsystem.

---

## Rejected duplicate locations

| Rejected | Reason |
|----------|--------|
| `projects/orca/ppc/` | ORCA-centric; hides MIG/ATLAS/QA boundaries |
| `governance/search-ppc/` | Governance is meta-layer; would mix policy with production contracts |
| `projects/orca/semantic-intelligence/` | Covers semantic stages only |
| New repo root folder outside `projects/` | Breaks MARS `projects/*` pack convention |

---

## Cross-system references (consumer obligations)

| System | Local responsibility doc | Links to |
|--------|-------------------------|----------|
| ATLAS | `projects/atlas/` project registry | SPPC-01 |
| MIG | `projects/mig/contracts/` | SPPC-02, 03, 10, 11 |
| ORCA Semantic Intelligence | `projects/orca/semantic-intelligence/` | SPPC-04–09 |
| ORCA Campaign Production | `projects/orca/contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md` | SPPC-14–20 |
| Commander Export | Triumph freeze / ORCA export foundation | SPPC-20 |
| Web-GPT | `web-gpt-sources/` sync pack addendum | Execution contract in this package |

**Rule:** One canonical authority here; subsystem docs keep concise local responsibility + links — no full lifecycle copy.

# Forge WordPress Synthetic Test Case Specification v1

**Document type:** Synthetic validation specification  
**Version:** v1  
**Stage:** FW-04  
**Execution:** FW-05 — **not in FW-04**

---

## Purpose

Define a **small, artificial, client-free** test case sufficient to exercise the full Forge WordPress prompt-driven pipeline before admitting a real client pilot.

**FW-04 specifies only.** FW-05 creates and runs the synthetic project.

---

## Synthetic frontend (minimum)

| Page / region | Requirement |
|---------------|-------------|
| Home page | Hero, services teaser, CTA |
| Service archive | CPT archive layout |
| Single service page | CPT single layout |
| FAQ section | Accordion or expandable |
| Contact form | Local stub acceptable |
| Global options | Phone, email, social |
| Header | Nav + logo |
| Footer | Links + copyright |
| Responsive | Desktop + mobile breakpoints |

**Source:** Artificial HTML/CSS — not FP-0002, not client data.

---

## Synthetic WordPress requirements

| Requirement | Detail |
|-------------|--------|
| Custom theme | Project theme slug e.g. `forge-synthetic-v1` |
| CPT `service` | Archive + single |
| Taxonomy | Optional — only if content model justifies |
| ACF fields | Page + options + service fields |
| Options page | Global settings |
| Template hierarchy | front-page, archive, single, page |
| Editable regions | Per block map |
| Admin UX | Simple editor paths |
| Local validation | Full validator chain |
| Visual comparison | Against synthetic frontend static build |
| Release package | RC zip + manifest |
| WPilot handoff | Artifact per FW-C-03 — **no live deployment** |

---

## Pipeline exercise map

```text
FW-SK-01 inspection (synthetic handoff)
→ FW-SK-02 WAD
→ FW-SK-03 content model
→ FW-SK-04 block map
→ FW-SK-05 theme architecture
→ FW-SK-06 ACF
→ FW-SK-07 CPT service
→ FW-SK-08 admin UX
→ FW-SK-09 implementation spec
→ FW-SK-10 implementation
→ FW-SK-11 validation
→ FW-SK-12 visual parity
→ FW-SK-13 release
→ FW-SK-14 handoff simulation
```

---

## Acceptance criteria (FW-05)

| Criterion | Pass condition |
|-----------|----------------|
| Full pipeline | All skills executed with reports |
| Validators | FW-V-01–07 run; blockers resolved |
| Visual parity | Operator approves WV6 on synthetic case |
| Release | FW-V-07 PASS |
| Handoff | FW-C-03 checklist complete — simulation only |
| No production | Zero production URLs or credentials |
| No client data | Zero FP-0002 or real client artifacts |
| Capability proof | Readiness matrix updated to support OPERATIONAL candidacy |

---

## Explicit exclusions

- Do not create synthetic project in FW-04
- Do not use FP-0002 frontend
- Do not register `project_id` for synthetic unless operator charters workspace path

---

## Related

- [FORGE-WORDPRESS-CAPABILITY-READINESS-MATRIX-v1.md](../FORGE-WORDPRESS-CAPABILITY-READINESS-MATRIX-v1.md)
- [../../reports/FORGE-WORDPRESS-FW-05-LOCAL-ENABLEMENT-AND-SYNTHETIC-VALIDATION-INPUT-v1.md](../../reports/FORGE-WORDPRESS-FW-05-LOCAL-ENABLEMENT-AND-SYNTHETIC-VALIDATION-INPUT-v1.md)

---

*Synthetic test spec v1 — specification only; execution in FW-05.*

# OCPilot Knowledge Layer

**Status:** skeleton only — Run 3.5 bootstrap. **No** content collection, **no** external downloads.

**Purpose:** future reference knowledge layer for OpenCart/ocStore audit and comparison work.

**Rule:** Documents here are **supporting reference**, not governance truth and not runtime products.

---

## Planned structure

| Path | Intended scope |
|------|----------------|
| [opencart/](opencart/README.md) | Upstream OpenCart concepts, version notes |
| [ocstore/](ocstore/README.md) | ocStore distribution deltas, rs builds |
| [database/](database/README.md) | Schema, prefixes, install SQL interpretation |
| [ocmod/](ocmod/README.md) | OCMOD modification system |
| [controllers/](controllers/README.md) | MVC controller layout and audit patterns |
| [models/](models/README.md) | Model layer patterns |
| [seo-url/](seo-url/README.md) | SEO URL / routing behavior |

### Active inspection rules

| Document | Scope |
|----------|-------|
| [OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md](OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md) | Controller + DB meta generator audit — SITE-001, BZPM, future OpenCart sites |

## Relation to baselines

- **Baselines** (`baselines/`) — version-pinned reference trees and metadata.
- **Knowledge layer** — cross-cutting explanations and audit playbooks (future).
- **Canonical ZIP** — remains acquisition source per [baselines/storage-policy.md](../baselines/storage-policy.md).

---

## SAFE UNKNOWN

- Population schedule, authoring owner, and sync with external ocStore/OpenCart docs — not defined in Run 3.5.

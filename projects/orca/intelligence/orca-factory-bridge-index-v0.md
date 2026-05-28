# ORCA → Website Factory Bridge Index v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — navigation index for cross-lane handoff (ORCA Lane B → Website Factory Lane A).

Not an API bridge. Not deployment automation.

## Purpose

Describe how ORCA delivers materials to Website Factory and what happens after implementation — single operator-readable flow.

## End-to-End Flow

```
ORCA research (human sessions)
  → normalized intelligence + evidence grading
  → landing content pack (semantic SoT) — see content-packs/export-pipeline-v0.md
  → approved landing brief / pack
  → approved_for_factory gate
  → semantic lock (MODE 1) — see orca-website-factory-semantic-lock-v0.md
  → DOCX sign-off (primary approved export) or operational Markdown
  → Website Factory handoff package
  → frontend implementation (workspace / dist)
  → PPC landing QA — see ppc-landing-qa-contract-v0.md
  → landing-route-registry update
  → approved_for_ads
  → (parallel) keyword pack + export when gates allow
  → approved_for_commander_import → human import
  → approved_for_launch (human only)
```

## Handoff Inputs (ORCA → Factory)

| Artifact | Typical path | Required gate |
|----------|--------------|---------------|
| Landing content pack | `content-packs/examples/` or `projects/<id>/content-packs/` | `approved_for_factory` |
| Landing brief | `landing-briefs/<route>.md` | `approved_for_factory` |
| Handoff doc | `artifacts/handoff/` or pack `handoff/` | `approved_for_factory` |
| Semantic lock mode | MODE 1 in session brief | Approved ORCA copy exists |
| Route registry | `landing-route-registry.json` | Recommended before ads URL lock |
| Assets list | Screenshots, brand, legal | Evidence-graded |

**Validated precedent:** Triumph v5 page-01 handoff — `ppc/triumph-manipulator/handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md` → `workspaces/triumph-manipulator-landing-v4/`.

## Content Lock Rules

| ORCA state | Factory behavior |
|------------|------------------|
| Approved brief + handoff exists | **Content locked** — MODE 1; presentation changes only |
| Draft ORCA only | **Demo content allowed** — must mark `draft` / `placeholder` in build and registry |
| No brief | Factory may prototype — **not** `approved_for_ads` without new brief |

See [orca-website-factory-semantic-lock-v0.md](orca-website-factory-semantic-lock-v0.md) for locked vs allowed domains.

## Factory Outputs (back to ORCA)

| Output | ORCA consumer |
|--------|---------------|
| Built page URL / dist path | `landing-route-registry` `website_factory_page` |
| QA report | `artifacts/qa/` per [ppc-landing-qa-contract-v0.md](ppc-landing-qa-contract-v0.md) |
| Implementation notes | `logs/` or project memory |

## Intake → Export Chain (same project)

For full project lifecycle, see also:

```
incoming/orca/<project-id>-raw-pack/
  → intake manifest + distribute
  → projects/orca/projects/<project-id>/normalized/
  → research/ + competitors/ + serp/
  → strategy/ + campaign-modes/
  → landing-briefs/ + artifacts/
  → exports/ (Commander transport)
```

Mode separation: [orca-campaign-mode-architecture-v0.md](../campaign-modes/orca-campaign-mode-architecture-v0.md).

## Registry and Display URL

- Factory and ORCA agree on **landing URL** via [landing-route-registry-contract-v0.md](landing-route-registry-contract-v0.md).
- **Display URL** is set in PPC export artifact — not in Factory repo.

## SAFE UNKNOWN

- Production domain vs staging
- CDN cache invalidation timing
- Whether client CMS replaces static build later

## Related Documents

- [content-packs/README.md](../content-packs/README.md) — landing semantic export layer (pack ≠ HTML)
- [content-packs/semantic-lock-export-rules-v0.md](../content-packs/semantic-lock-export-rules-v0.md)
- [orca-website-factory-semantic-lock-v0.md](orca-website-factory-semantic-lock-v0.md)
- [landing-route-registry-contract-v0.md](landing-route-registry-contract-v0.md)
- [ppc-landing-qa-contract-v0.md](ppc-landing-qa-contract-v0.md)
- [approval-gates-contract-v0.md](../artifacts/approval-gates-contract-v0.md)
- [project-md-contract-v0.md](../projects/project-md-contract-v0.md)
- [orca-universal-intake-architecture-v0.md](../intake/orca-universal-intake-architecture-v0.md)

## Boundary

Navigation and operational routing documentation only. No Factory plugin, no ORCA runtime.

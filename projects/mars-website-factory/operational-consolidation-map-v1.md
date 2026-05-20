# Operational consolidation map v1 (Wave 6)

**Status:** **documented** — single routing layer; reduces duplicate operator paths.  
**Session default:** [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) (Tier 2).

**Not:** full pack inventory — see [README.md](README.md) Pack index only when searching.

---

## Canonical entries (use these first)

| Concern | Canonical entry | Do not default to |
|---------|-----------------|-------------------|
| **Session start** | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | README full table |
| **Onboarding** | [onboarding-flow-v1.md](onboarding-flow-v1.md) | scattered v0 runbooks |
| **Block library** | [curated-library-index-v1.md](curated-library-index-v1.md) | raw block-registry only |
| **Block quality** | [block-quality-tiers-v1.md](block-quality-tiers-v1.md) | ad hoc “production-ready” claims |
| **Extraction** | [implementation-extraction-discipline-v1.md](implementation-extraction-discipline-v1.md) | re-reading Wave 4–5 reports for rules |
| **Extraction examples** | `operational-examples/wave5-extraction-report-faq-v1.md`, `wave6-extraction-report-*.md` | Triumph workspace AGENTS |
| **QA after build** | [operational-qa-entry-v1.md](operational-qa-entry-v1.md) | Forge README checklist table |
| **Reference QA detail** | [reference-workspace-qa-flow-v1.md](reference-workspace-qa-flow-v1.md) | duplicate checklist copies |
| **Freeze** | [freeze-discipline-v1.md](freeze-discipline-v1.md) | production-readiness governance triad |
| **Registry vs code** | [registry-sync-discipline-v1.md](registry-sync-discipline-v1.md) | assuming registry auto-syncs |
| **Pilot client** | [pilot-adoption-flow-v1.md](pilot-adoption-flow-v1.md) | inventing adoption steps |
| **Hardening edge cases** | [production-hardening-rules-v1.md](production-hardening-rules-v1.md) | Extended governance rows |
| **Golden implementation** | [golden-implementation-slice-v1.md](golden-implementation-slice-v1.md) + [workspaces/website-factory-reference-v1/](../../workspaces/website-factory-reference-v1/) | Triumph V2 as library SoT |

---

## Compact routing by task

```text
New operator     → OPERATIONAL-INDEX → onboarding-flow-v1 Path A
New workspace    → _template-client-v1 → pilot-adoption-flow-v1
Add block        → curated-library-index → copy partial → block-quality tier check
Extract block    → implementation-extraction-discipline → REPORT in operational-examples
QA               → operational-qa-entry-v1
Freeze delivery  → freeze-discipline-v1 → hardening rules if Standard+
Replace section  → section-replacement-contract → section-swap-demo-flow
Drift / naming   → registry-sync-discipline
```

---

## Wave 6 consolidation outcomes

| Before | After |
|--------|-------|
| Library quality implicit | [block-quality-tiers-v1.md](block-quality-tiers-v1.md) |
| Blocks scattered across Wave 3–5 docs | [curated-library-index-v1.md](curated-library-index-v1.md) |
| Freeze mentioned in several places | [freeze-discipline-v1.md](freeze-discipline-v1.md) |
| Registry vs reference unclear | [registry-sync-discipline-v1.md](registry-sync-discipline-v1.md) |
| No pilot procedure | [pilot-adoption-flow-v1.md](pilot-adoption-flow-v1.md) |

---

## Explicitly not canonical (escalation only)

- Individual `*-governance.md` taxonomy files  
- [agents/mars-forge/README.md](../../agents/mars-forge/README.md) full checklist index  
- Triumph/ORCA workspaces as operational SoT  

---

*Wave 6 — operational consolidation map.*
